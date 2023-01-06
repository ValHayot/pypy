"""C AST generalization."""
import ast
import logging
import typing as t
from typing import Dict, Any

import pycparser.c_ast as c_ast

import ast as typed_ast3

_LOG = logging.getLogger(__name__)


STANDALONE_EXPRESSION_TYPES = (
    typed_ast3.Call,
    typed_ast3.UnaryOp,
    typed_ast3.BinOp,
    typed_ast3.BoolOp,
    typed_ast3.Compare,
    typed_ast3.IfExp,
    typed_ast3.Attribute,
    typed_ast3.Name,
    typed_ast3.Subscript,
    typed_ast3.Num,
    typed_ast3.Str,
    typed_ast3.FormattedValue,
    typed_ast3.JoinedStr,
    typed_ast3.Bytes,
    typed_ast3.List,
    typed_ast3.Tuple,
    typed_ast3.Set,
    typed_ast3.Dict,
    typed_ast3.Ellipsis,
    typed_ast3.NameConstant,
)


def fix_stmts_in_body(stmts: t.List[typed_ast3.AST]) -> t.List[typed_ast3.AST]:
    assert isinstance(stmts, list)
    if not stmts:
        return [typed_ast3.Pass()]
    return [
        typed_ast3.Expr(value=stmt)
        if isinstance(stmt, STANDALONE_EXPRESSION_TYPES)
        else stmt
        for stmt in stmts
    ]


def make_range_call(
    begin: t.Optional[typed_ast3.AST] = None,
    end: typed_ast3.AST = None,
    step: t.Optional[typed_ast3.AST] = None,
) -> typed_ast3.Call:
    """Create a typed_ast node equivalent to: range(begin, end, step)."""
    assert isinstance(end, typed_ast3.AST), end
    if step is None:
        if begin is None:
            args = [end]
        else:
            args = [begin, end]
    else:
        assert isinstance(step, typed_ast3.AST), step
        assert isinstance(begin, typed_ast3.AST), begin
        args = [begin, end, step]
    return typed_ast3.Call(
        func=typed_ast3.Name(id="range", ctx=typed_ast3.Load()), args=args or [], keywords=[]
    )


def _node_debug(node: c_ast.Node):
    if isinstance(node, c_ast.Node):
        return _node_str(node)
    if isinstance(node, tuple):
        return tuple([_node_debug(_) for _ in node])
    if isinstance(node, list):
        return [_node_debug(_) for _ in node]
    raise NotImplementedError()


def _node_str(node: c_ast.Node):
    return "{}({})".format(type(node), {_: getattr(node, _) for _ in node.__slots__})


C_UNARY_OPERATORS_TO_PYTHON = {
    "+": (typed_ast3.UnaryOp, typed_ast3.UAdd),
    "-": (typed_ast3.UnaryOp, typed_ast3.USub),
    "sizeof": (typed_ast3.Call, "sizeof"),
    "&": (typed_ast3.Call, "ref"),
    "*": (typed_ast3.Call, "deref"),
    "++": (typed_ast3.AugAssign, typed_ast3.Add),
    "--": (typed_ast3.AugAssign, typed_ast3.Sub),
    "p++": (typed_ast3.AugAssign, typed_ast3.Add),
    "p--": (typed_ast3.AugAssign, typed_ast3.Sub),
    "!": (typed_ast3.UnaryOp, typed_ast3.Not),
}

C_BINARY_OPERATORS_TO_PYTHON = {
    "+": (typed_ast3.BinOp, typed_ast3.Add),
    "-": (typed_ast3.BinOp, typed_ast3.Sub),
    "*": (typed_ast3.BinOp, typed_ast3.Mult),
    "/": (typed_ast3.BinOp, typed_ast3.Div),
    "%": (typed_ast3.BinOp, typed_ast3.Mod),
    "<<": (typed_ast3.BinOp, typed_ast3.LShift),
    ">>": (typed_ast3.BinOp, typed_ast3.RShift),
    "|": (typed_ast3.BinOp, typed_ast3.BitOr),
    "^": (typed_ast3.BinOp, typed_ast3.BitXor),
    "&": (typed_ast3.BinOp, typed_ast3.BitAnd),
    "==": (typed_ast3.Compare, typed_ast3.Eq),
    "!=": (typed_ast3.Compare, typed_ast3.NotEq),
    "<": (typed_ast3.Compare, typed_ast3.Lt),
    "<=": (typed_ast3.Compare, typed_ast3.LtE),
    ">": (typed_ast3.Compare, typed_ast3.Gt),
    ">=": (typed_ast3.Compare, typed_ast3.GtE),
    "&&": (typed_ast3.BoolOp, typed_ast3.And),
    "||": (typed_ast3.BoolOp, typed_ast3.Or),
}

C_ASSIGNMENT_OPERATORS_TO_PYTHON = {
    "=": (typed_ast3.Assign, None),
    "+=": (typed_ast3.AugAssign, typed_ast3.Add),
    "-=": (typed_ast3.AugAssign, typed_ast3.Sub),
}

INITIALIZABLE_DECLARATIONS = (c_ast.ArrayDecl, c_ast.PtrDecl, c_ast.TypeDecl)

DECL_DATA_LENGTHS = {
    c_ast.FuncDecl: 3,
    c_ast.ArrayDecl: 2,
    c_ast.PtrDecl: 2,
    c_ast.TypeDecl: 2,
}


class CAstGeneralizerBackend(
    c_ast.NodeVisitor
):  # pylint: disable=too-many-public-methods

    """Traverse pycparser's nodes and convert them to typed_ast.ast3 nodes.

    Use pycparser's NodeVisitor class.
    """

    # def __init__(self):
    #    super().__init__()

    def visit(self, node):
        if node is None:
            _LOG.debug("None")
            return None
        _LOG.debug("%s", _node_str(node))
        return super().visit(node)

    def visit_FileAST(self, node) -> typed_ast3.Module:  # pylint: disable=invalid-name
        ext = [
            self.visit(subnode)
            for subnode in node.ext
            if isinstance(subnode, c_ast.FuncDef) and subnode.decl.name == "interpreter"
        ]
        _ = self.visit(node.coord)
        module = typed_ast3.Module(body=fix_stmts_in_body(ext), type_ignores=[])
        return module

    def visit_FuncDef(
        self, node
    ) -> typed_ast3.FunctionDef:  # pylint: disable=invalid-name
        """Transform FuncDef."""
        assert node.decl is not None
        name, args, return_type = self.visit(node.decl)
        param_decls = self.visit(node.param_decls)
        if param_decls is not None:
            raise NotImplementedError(_node_debug(node.param_decls), str(param_decls))
        body = self.visit(node.body)
        assert isinstance(body, list) and body
        _ = self.visit(node.coord)
        funcdef = typed_ast3.FunctionDef(
            lineno=node.coord.line,
            name=name,
            args=args,
            body=fix_stmts_in_body(body),
            decorator_list=[],
            returns=return_type,
        )
        return funcdef

    def visit_FuncDecl(  # pylint: disable=invalid-name
        self, node
    ) -> t.Tuple[str, typed_ast3.arguments, typed_ast3.AST]:
        """Return a tuple: function name, its declared arguments and its return type"""
        args = self.visit(node.args)
        assert isinstance(args, typed_ast3.arguments)
        name, return_type = self.visit(node.type)
        assert isinstance(name, str)
        assert isinstance(return_type, typed_ast3.AST)
        # if type_ is not None:
        #    raise NotImplementedError(_node_debug(node.type), str(type_))
        _ = self.visit(node.coord)
        return name, args, return_type

    def visit_ParamList(
        self, node
    ) -> typed_ast3.arguments:  # pylint: disable=invalid-name
        """Transform ParamList."""
        params = [self.visit(subnode) for subnode in node.params]
        # assert all(isinstance(param, tuple) for param in params), params
        # params = [typed_ast3.arg(arg=param[0], annotation=param[1]) for param in params]
        assert all(isinstance(param, typed_ast3.AnnAssign) for param in params), params
        assert all(
            isinstance(param.target, typed_ast3.Name) for param in params
        ), params
        params = [
            typed_ast3.arg(arg=param.target.id, annotation=param.annotation)
            for param in params
        ]
        _ = self.visit(node.coord)
        return typed_ast3.arguments(
            posonlyargs=[],
            args=params,
            vararg=None,
            kwonlyargs=[],
            kwarg=None,
            defaults=[],
            kw_defaults=[],
        )

    def visit_Return(self, node) -> typed_ast3.Return:  # pylint: disable=invalid-name
        expr = self.visit(node.expr)
        assert isinstance(expr, typed_ast3.AST)
        _ = self.visit(node.coord)
        return typed_ast3.Return(value=expr)

    def visit_For(self, node) -> typed_ast3.For:  # pylint: disable=invalid-name
        """Transform For(init, cond, next, stmt: list, coord: t.Optional[Coord])."""
        init = self.visit(node.init)
        assert isinstance(init, (typed_ast3.Assign, typed_ast3.AnnAssign))
        if isinstance(init, typed_ast3.Assign):
            assert len(init.targets) == 1
            target = init.targets[0]
        else:
            target = init.target
        begin = init.value
        assert isinstance(target, typed_ast3.Name)
        cond = self.visit(node.cond)
        assert isinstance(cond, typed_ast3.Compare)
        assert isinstance(cond.left, typed_ast3.Name)
        assert len(cond.ops) == 1
        assert len(cond.comparators) == 1
        end = cond.comparators[0]
        assert cond.left.id == target.id
        next_ = self.visit(node.next)
        assert isinstance(next_, typed_ast3.AugAssign)
        step = next_.value
        assert isinstance(step, typed_ast3.Num)

        # todo check this thinking
        if isinstance(cond.ops[0], typed_ast3.Lt):
            assert isinstance(next_.op, typed_ast3.Add)
            iter_ = make_range_call(begin, end, step)
        elif isinstance(cond.ops[0], typed_ast3.Gt):
            assert isinstance(next_.op, typed_ast3.Sub)
            step.n = -step.n
            iter_ = make_range_call(end, begin, step)

        stmt = self.visit(node.stmt)
        assert stmt is not None
        if not isinstance(stmt, list):
            stmt = [stmt]
        _ = self.visit(node.coord)
        return typed_ast3.For(
            lineno=node.coord.line,
            target=target, iter=iter_, body=fix_stmts_in_body(stmt), orelse=[]
        )

    def visit_If(self, node):  # pylint: disable=invalid-name
        """Transform If(cond, iftrue, iffalse, coord: t.Optional[Coord])."""
        cond = self.visit(node.cond)
        iftrue = self.visit(node.iftrue)
        if iftrue is not None:
            if not isinstance(iftrue, list):
                iftrue = [iftrue]
            iftrue = fix_stmts_in_body(iftrue)
        iffalse = self.visit(node.iffalse)
        if iffalse is None:
            iffalse = []
        else:
            if not isinstance(iffalse, list):
                iffalse = [iffalse]
            iffalse = fix_stmts_in_body(iffalse)
        _ = self.visit(node.coord)
        if isinstance(iftrue, str) or isinstance(iffalse, str) or isinstance(cond, str):
            print(iftrue, iffalse)
            raise
        if any(isinstance(b, str) for b in iftrue):
            print(iftrue)
            raise
        if any(isinstance(b, str) for b in iffalse):
            print(iffalse)
            raise
        return typed_ast3.If(test=cond, body=iftrue, orelse=iffalse)

    def visit_Compound(self, node):  # pylint: disable=invalid-name
        """Transform Compound."""
        block_items = [self.visit(subnode) for subnode in node.block_items]
        _ = self.visit(node.coord)
        return fix_stmts_in_body(block_items)

    def visit_BinaryOp(self, node):  # pylint: disable=invalid-name
        """Transform BinaryOp."""
        op_type, op_ = C_BINARY_OPERATORS_TO_PYTHON[node.op]
        left = self.visit(node.left)
        right = self.visit(node.right)
        _ = self.visit(node.coord)
        if op_type is typed_ast3.BinOp:
            if isinstance(left, list):
                print(node.coord.line)
                print(left, right)
                raise
            return op_type(left=left, op=op_(), right=right)
        if op_type is typed_ast3.Compare:
            return op_type(left=left, ops=[op_()], comparators=[right])
        if op_type is typed_ast3.BoolOp:
            return op_type(op=op_(), values=[left, right])
        return self.generic_visit(node)

    def visit_UnaryOp(self, node):  # pylint: disable=invalid-name
        """Transform UnaryOp."""
        op_type, op_ = C_UNARY_OPERATORS_TO_PYTHON[node.op]
        expr = self.visit(node.expr)
        _ = self.visit(node.coord)
        if op_type is typed_ast3.Call:
            return op_type(
                func=typed_ast3.Name(id=op_, ctx=typed_ast3.Load()),
                args=[expr],
                keywords=[],
            )
        if op_type is typed_ast3.AugAssign:
            if isinstance(op_(), typed_ast3.Not):
                print(expr, op_(), node.coord.line)
                raise
            return op_type(target=expr, op=op_(), value=typed_ast3.Num(n=1))
            # raise NotImplementedError()
        return op_type(op=op_(), operand=expr)

    def visit_Cast(self, node):  # pylint: disable=invalid-name
        """Transform C cast into cast() function call."""
        to_type = self.visit(node.to_type)
        expr = self.visit(node.expr)
        _ = self.visit(node.coord)
        return typed_ast3.Call(
            func=typed_ast3.Name(id="cast", ctx=typed_ast3.Load()),
            args=[expr],
            keywords=[typed_ast3.keyword(arg="type", value=to_type)],
        )

    def visit_ID(self, node):  # pylint: disable=invalid-name
        name = node.name
        _ = self.visit(node.coord)
        return typed_ast3.Name(id=name, ctx=typed_ast3.Load())

    def visit_Constant(self, node):  # pylint: disable=invalid-name
        """Transform Constant into Num or Str."""
        type_ = node.type
        value = node.value
        _ = self.visit(node.coord)
        if type_ in ("int", "unsigned long int"):
            return typed_ast3.Num(int(eval(value.replace("U", "").replace("L", ""))))
        if type_ in ("string",):
            assert value[0] == '"' and value[-1] == '"', value
            return typed_ast3.Str(value[1:-1], "")
        return self.generic_visit(node)

    def visit_Assignment(  # pylint: disable=invalid-name
        self, node
    ) -> t.Union[typed_ast3.Assign, typed_ast3.AugAssign]:
        """Transform Assignment."""
        op_type, op_ = C_ASSIGNMENT_OPERATORS_TO_PYTHON[node.op]
        lvalue = self.visit(node.lvalue)
        assert isinstance(lvalue, typed_ast3.AST)
        rvalue = self.visit(node.rvalue)
        assert isinstance(rvalue, typed_ast3.AST)
        _ = self.visit(node.coord)
        if op_type is typed_ast3.Assign:
            return op_type(targets=[lvalue], value=rvalue, type_comment=None,
                           lineno=node.coord.line,
                           )
        return op_type(target=lvalue, op=op_(), value=rvalue, lineno=node.coord.line)

    def visit_Decl(
        self, node
    ) -> t.Union[
        typed_ast3.AnnAssign,  # pylint: disable=invalid-name
        t.Tuple[str, typed_ast3.arguments, typed_ast3.AST],
    ]:
        """Transform Decl."""
        name = node.name
        assert isinstance(name, str), type(name)
        quals = node.quals
        if quals:
            _LOG.warning("ignoring unsupported C grammar: %s", quals)
        storage = [
            self.visit(subnode) if isinstance(node.storage, c_ast.Node) else subnode
            for subnode in node.storage
        ]
        if storage:
            _LOG.warning("ignoring unsupported C grammar: %s", storage)
        funcspec = [self.visit(subnode) for subnode in node.funcspec]
        if funcspec:
            raise NotImplementedError(_node_debug(node.funcspec), str(funcspec))
        type_data = self.visit(node.type)
        assert isinstance(type_data, tuple)
        assert len(type_data) == DECL_DATA_LENGTHS[type(node.type)], (
            type(node.type),
            type_data,
        )
        init = self.visit(node.init)
        if init is not None:
            assert isinstance(node.type, INITIALIZABLE_DECLARATIONS)
            # assert isinstance(node.type, c_ast.TypeDecl), type(node.type)
            # raise NotImplementedError(_node_debug(node.init), str(init))
        bitsize = self.visit(node.bitsize)
        if bitsize is not None:
            raise NotImplementedError(_node_debug(node.bitsize), str(bitsize))
        _ = self.visit(node.coord)
        if init is not None and isinstance(init, ast.List):
            init.elts = list(filter(None, init.elts))
            if not init.elts:
                _LOG.warning(f"no elements in list initializer {node.coord.line}")
                print("wtfbbq")
        if init is not None or isinstance(node.type, INITIALIZABLE_DECLARATIONS):
            name_, type_ = type_data
            assert name_ == name
            print(type_)
            return typed_ast3.AnnAssign(
                lineno=node.coord.line,
                target=typed_ast3.Name(id=name_, ctx=typed_ast3.Store()),
                annotation=type_,
                value=init,
                simple=1,
            )
        if isinstance(node.type, (c_ast.FuncDecl,)):
            return type_data
        return self.generic_visit(node)

    def visit_TypeDecl(
        self, node
    ) -> t.Tuple[str, typed_ast3.Name]:  # pylint: disable=invalid-name
        """Return a tuple: identifier and its type."""
        declname = node.declname
        assert declname is None or isinstance(declname, str)
        quals = node.quals
        type_ = self.visit(node.type)
        assert isinstance(type_, typed_ast3.Name), type(type_)
        for qual in quals:
            assert isinstance(qual, str)
            type_ = typed_ast3.Subscript(
                value=typed_ast3.Attribute(
                    value=typed_ast3.Name(id="st", ctx=typed_ast3.Load()),
                    attr=qual.title(),
                    ctx=typed_ast3.Load(),
                ),
                slice=typed_ast3.Index(value=type_),
                ctx=typed_ast3.Load(),
            )
        _ = self.visit(node.coord)
        return declname, type_

    def visit_IdentifierType(
        self, node
    ) -> typed_ast3.Name:  # pylint: disable=invalid-name
        """Transform IdentifierType(names: t.List[str], coord: t.Optional[Coord])."""
        names = node.names
        if len(names) > 1:
            _LOG.warning(f"concatting names {names}")
            names = ["_".join(names)]
        assert len(names) == 1, names
        name = names[0]
        assert isinstance(name, str)
        _ = self.visit(node.coord)
        return typed_ast3.Name(id=name, ctx=typed_ast3.Load())

    def visit_ArrayDecl(  # pylint: disable=invalid-name
        self, node
    ) -> t.Tuple[str, typed_ast3.Subscript]:
        """Return tuple of: name, st.ndarray[..., ...] for given array type information."""
        name, type_ = self.visit(node.type)
        assert isinstance(name, str)
        assert isinstance(type_, typed_ast3.AST)
        dim = self.visit(node.dim)
        if dim is not None:
            _LOG.warning(f"not handling dims for array decl {node.coord.line}")
            # raise NotImplementedError(_node_debug(node.dim), str(dim))
        dim_quals = [self.visit(subnode) for subnode in node.dim_quals]
        if dim_quals:
            raise NotImplementedError(_node_debug(node.dim_quals), str(dim_quals))
        _ = self.visit(node.coord)
        return name, typed_ast3.Subscript(
            value=typed_ast3.Attribute(
                value=typed_ast3.Name(id="st", ctx=typed_ast3.Load()),
                attr="ndarray",
                ctx=typed_ast3.Load(),
            ),
            slice=typed_ast3.ExtSlice(
                dims=[
                    typed_ast3.Index(value=typed_ast3.Ellipsis()),
                    typed_ast3.Index(value=type_)  # ,
                    # typed_ast3.Index(value=typed_ast3.Tuple(n=-1))
                ]
            ),
            ctx=typed_ast3.Load(),
        )

    def visit_ArrayRef(self, node):  # pylint: disable=invalid-name
        name = self.visit(node.name)
        subscript = self.visit(node.subscript)
        _ = self.visit(node.coord)
        return typed_ast3.Subscript(
            value=name, slice=typed_ast3.Index(subscript), ctx=typed_ast3.Load()
        )

    def visit_PtrDecl(self, node):  # pylint: disable=invalid-name
        """Return st.Pointer[...] for given pointer type."""
        quals = node.quals
        if quals:
            _LOG.warning("ignoring unsupported C grammar: %s", quals)
        name, type_ = self.visit(node.type)
        assert name is None or isinstance(name, str)
        assert isinstance(type_, typed_ast3.AST), type(type_)
        _ = self.visit(node.coord)
        # assert type_ is not None, _node_str(node)
        return name, typed_ast3.Subscript(
            value=typed_ast3.Attribute(
                value=typed_ast3.Name(id="st", ctx=typed_ast3.Load()),
                attr="Pointer",
                ctx=typed_ast3.Load(),
            ),
            slice=typed_ast3.Index(value=type_),
            ctx=typed_ast3.Load(),
        )

    def visit_FuncCall(self, node) -> typed_ast3.Call:  # pylint: disable=invalid-name
        """Return a call."""
        name = self.visit(node.name)
        assert isinstance(
            name, (typed_ast3.Name, typed_ast3.Call, typed_ast3.Subscript)
        ) or (
            isinstance(name, typed_ast3.Attribute)
        ), name
        args = self.visit(node.args)
        _ = self.visit(node.coord)
        return typed_ast3.Call(func=name, args=args or [], keywords=[])

    def visit_ExprList(
        self, node
    ) -> t.List[typed_ast3.AST]:  # pylint: disable=invalid-name
        """Return raw list of transformed expressions."""
        exprs = [self.visit(subnode) for subnode in node.exprs]
        assert all(isinstance(expr, typed_ast3.AST) for expr in exprs)
        _ = self.visit(node.coord)
        return exprs

    def visit_Typename(self, node):  # pylint: disable=invalid-name
        """Transform Typename."""
        name = self.visit(node.name)
        assert name is None or isinstance(name, typed_ast3.Name), type(name)
        if name is not None:
            raise NotImplementedError(_node_debug(node.name), str(name))
        quals = node.quals
        if quals:
            _LOG.warning("ignoring unsupported C grammar: %s", quals)
        name_, type_ = self.visit(node.type)
        assert name_ is None, type(name_)
        assert isinstance(type_, typed_ast3.AST), type(type_)
        _ = self.visit(node.coord)
        return type_

    def visit_Typedef(self, node):  # pylint: disable=invalid-name
        """Transform Typedef."""
        name = node.name
        assert isinstance(name, str), type(name)
        quals = node.quals
        if quals:
            _LOG.warning("ignoring unsupported C grammar: %s", quals)
        assert node.storage == ["typedef"], node.storage
        name_, type_ = self.visit(node.type)
        assert name == name_, (name, name_)
        _ = self.visit(node.coord)
        return typed_ast3.AnnAssign(
            lineno=node.coord.line,
            target=typed_ast3.Name(name, typed_ast3.Store()),
            value=type_,
            annotation=typed_ast3.Name("type", typed_ast3.Load()),
            simple=1,
        )

    def visit_Struct(self, node):  # pylint: disable=invalid-name
        """Transform Struct."""
        name = node.name
        assert isinstance(name, str), (node, type(name))
        assert node.decls is None, node.decls
        _ = self.visit(node.coord)
        return typed_ast3.Name(name, typed_ast3.Load())
        # body = [typed_ast3.Pass()]
        # return typed_ast3.ClassDef(
        #     decorator_list=[], name=name,
        #     bases=[typed_ast3.Name('struct', typed_ast3.Load())], keywords=[], body=body)

    # def visit_(self, node):  # pylint: disable=invalid-name
    #     """Transform ."""
    #     return

    def visit_Coord(self, node) -> dict[str, Any]:  # pylint: disable=invalid-name
        """Transform Coord(file: str, line: int, column: int)."""
        return {"path": node.file, "lineno": node.line, "col": node.column}

    def visit_Switch(self, node: c_ast.Switch):
        cases = []
        for case in node.stmt:
            cases.append(self.visit(case))
            print(cases[-1])
            print(case.coord.line)
            print(ast.unparse(cases[-1]))

        subject = self.visit(node.cond)
        return ast.Match(subject, cases)

    def visit_Case(self, node: c_ast.Case):
        cond = self.visit(node.expr)
        body = [self.visit(s) for s in node.stmts]
        if isinstance(body, list) and len(body) == 1:
            body = body[0]
        if body is None or cond is None:
            print(node.coord.line)
            raise
        return ast.match_case(pattern=cond, guard=None, body=body)

    def visit_Default(self, node: c_ast.Default):
        body = [self.visit(s) for s in node.stmts]
        if not body:
            raise
        return ast.match_case(pattern=typed_ast3.Constant(True), guard=None, body=body)

    def visit_Label(self, n):
        return ast.Constant("# label: n.name")
        # return typed_ast3.Return("label: " + n.name + ":\n" + self._generate_stmt(n.stmt))

    def visit_Goto(self, n):
        return typed_ast3.Constant("break # goto " + n.name)

    def visit_StructRef(self, n):
        sref = self.visit(n.name)
        field = self.visit(n.field)
        assert n.type in {".", "->"}, f"unknown struct ref type {n.type}"
        if sref is None:
            print(n, sref, field)
            raise
        if isinstance(sref, list):
            sref = sref[0]
        return typed_ast3.Attribute(value=sref, attr=field.id, ctx=typed_ast3.Load())

    def visit_TernaryOp(self, n):
        test = self.visit(n.iftrue)
        body = self.visit(n.cond)
        orelse = self.visit(n.iffalse)
        if test is None or body is None or orelse is None:
            print(test, body, orelse, n.coord.line)
            raise
        return typed_ast3.IfExp(test, body, orelse)

    def visit_EmptyStatement(self, n):
        return typed_ast3.Pass()

    def visit_StaticAssert(self, n):
        cond = self.visit(n.cond)
        msg = None
        if n.message:
            msg = self.visit(n.message)
        return typed_ast3.Assert(cond, msg)

    def visit_DeclList(self, n):
        s = self.visit(n.decls[0])
        if len(n.decls) > 1:
            s = [s] + [self.visit_Decl(decl) for decl in n.decls[1:]]
        return s

    def visit_Break(self, n):
        return typed_ast3.Return()

    def visit_While(self, n):
        cond = self.visit(n.cond)
        body = self.visit(n.stmt)
        if isinstance(
            cond, (typed_ast3.Assign, typed_ast3.AnnAssign, typed_ast3.AugAssign)
        ):
            return typed_ast3.While(test=typed_ast3.Expr(cond.target), body=body + [cond], orelse=[])
        return typed_ast3.While(cond, body, [])

    def visit_InitList(self, n):
        visited_subexprs = []
        for expr in n.exprs:
            visited_subexprs.append(self._visit_expr(expr))
        return typed_ast3.List(elts=visited_subexprs)

    # def visit_DoWhile(self, n):
    #     init =
    #     s = "do\n"
    #     s += self._generate_stmt(n.stmt, add_indent=True)
    #     s += self._make_indent() + "while ("
    #     if n.cond:
    #         s += self.visit(n.cond)
    #     s += ")"
    #     return s

    def generic_visit(self, node):
        raise NotImplementedError("{} cannot be processed".format(_node_str(node)))

    def _visit_expr(self, n):
        if isinstance(n, c_ast.InitList):
            return "[" + self.visit(n) + "]"
        elif isinstance(n, c_ast.ExprList):
            # return "(" + self.visit(n) + ")"
            # else:
            return self.visit(n)

    def _parenthesize_if(self, n, condition):
        """Visits 'n' and returns its string representation, parenthesized
        if the condition function applied to the node returns True.
        """
        s = self._visit_expr(n)
        if condition(n):
            return typed_ast3.Expr(s)
        else:
            return s

    def _parenthesize_unless_simple(self, n):
        """Common use case for _parenthesize_if"""
        return self._parenthesize_if(n, lambda d: not self._is_simple_node(d))

    def _is_simple_node(self, n):
        """Returns True for nodes that are "simple" - i.e. nodes that always
        have higher precedence than operators.
        """
        return isinstance(
            n,
            (c_ast.Constant, c_ast.ID, c_ast.ArrayRef, c_ast.StructRef, c_ast.FuncCall),
        )
