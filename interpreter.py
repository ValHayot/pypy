from typing import Any, List, Callable

# from pytype.pyc import opcodes as ops

COMPARE_OP: Any
POP_JUMP_IF_FALSE: Any
INLINE_CACHE_ENTRIES_BINARY_SUBSCR: Any
BINARY_SUBSCR: Any
JUMP_BACKWARD: Any
STORE_SUBSCR: Any
LOAD_CONST: Any
STORE_ATTR: Any
CO_COROUTINE: Any
CO_ITERABLE_COROUTINE: Any
LOAD_ATTR: Any
INLINE_CACHE_ENTRIES_LOAD_ATTR: Any
CALL: Any
CALL_PY_EXACT_ARGS: Any
CO_OPTIMIZED: Any
INLINE_CACHE_ENTRIES_CALL: Any
METH_O: Any
METH_FASTCALL: Any
METH_KEYWORDS: Any
POP_TOP: Any
METH_NOARGS: Any
FRAME_CREATED: Any
FRAME_OWNED_BY_GENERATOR: Any
FVC_MASK: Any
FVC_NONE: Any
FVC_STR: Any
FVC_REPR: Any
FVC_ASCII: Any
INLINE_CACHE_ENTRIES_BINARY_OP: Any
BINARY_OP: Any
STORE_FAST: Any
STORE_FAST__LOAD_FAST: Any
PYGEN_RETURN: Any
PYGEN_ERROR: Any
CO_ASYNC_GENERATOR: Any
INLINE_CACHE_ENTRIES_UNPACK_SEQUENCE: Any
INLINE_CACHE_ENTRIES_LOAD_GLOBAL: Any
UNPACK_SEQUENCE: Any
LOAD_GLOBAL: Any
POP_JUMP_IF_TRUE: Any
INLINE_CACHE_ENTRIES_FOR_ITER: Any
END_FOR: Any
FVS_MASK: Any
FVS_HAVE_SPEC: Any
PYGEN_NEXT: Any
FRAME_SUSPENDED: Any
FOR_ITER: Any
FRAME_EXECUTING: Any
DICT_KEYS_UNICODE: Any

KWNAMES_LEN: Callable
DK_UNICODE_ENTRIES: Callable
STACK_LEVEL: Callable
DTRACE_FUNCTION_EXIT: Callable
TRACE_FUNCTION_EXIT: Callable
GO_TO_INSTRUCTION: Callable
STACK_SHRINK: Callable
DISPATCH: Callable
GETLOCAL: Callable
STACK_GROW: Callable
PREDICTED: Callable
GETITEM: Callable
SETLOCAL: Callable
NEXTOPARG: Callable
JUMPBY: Callable
ADAPTIVE_COUNTER_IS_ZERO: Callable
DISPATCH_SAME_OPARG: Callable
DECREMENT_ADAPTIVE_COUNTER: Callable
DEOPT_IF: Callable
DISPATCH_INLINED: Callable
PREDICT: Callable
LOCALS: Callable
TOP: Callable
DK_IS_UNICODE: Callable
INSTR_OFFSET: Callable
CHECK_EVAL_BREAKER: Callable
POP: Callable
PUSH: Callable
SECOND: Callable
EMPTY: Callable
PRE_DISPATCH_GOTO: Callable
DISPATCH_GOTO: Callable
BUILTINS: Callable
GLOBALS: Callable
DK_ENTRIES: Callable

Py_GE: Any
Py_EQ: Any
Py_NE: Any
PyRangeIter_Type: Any
_PyOpcode_Deopt: Any
_PyRangeIterObject: Any
PyTupleObject: Any
PyTupleIter_Type: Any
_PyTupleIterObject: Any
_PyFunction_Vectorcall: Any
PyType_Type: Any
PyListObject: Any
_PyListIterObject: Any
PyListIter_Type: Any
Py_SIZE: Any
PyCodeObject: Any
PySendResult: Any
unaryfunc: Any
_PyCFunctionFast: Any
PyMethodDescrObject: Any
PyInterpreterState: Any
_PyCFunctionFastWithKeywords: Any
PyFunction_Type: Any
PyDictObject: Any
PyDictKeyEntry: Any
PyDictOrValues: Any
PyDictUnicodeEntry: Any
PyExc_TypeError: Any
PyFunctionObject: Any
PyHeapTypeObject: Any
PyObject: Any
PyThreadState: Any
PyTypeObject: Any = type
Py_TPFLAGS_HEAPTYPE: Any
Py_TPFLAGS_MANAGED_DICT: Any
Py_ssize_t: Any
_PyBinarySubscrCache: Any
_PyCFrame: Any
_PyCompareOpCache: Any
_PyInterpreterFrame: Any
_PyLoadMethodCache: Any
_PyStoreSubscrCache: Any
_Py_CODEUNIT: Any
_Py_atomic_int: Any
binaryfunc: Any
next_instr: Any
Py_TPFLAGS_METHOD_DESCRIPTOR: Any
PyMethod_Type: Any
_PyCallCache: Any
PyUnicode_Type: Any
PyTuple_Type: Any
PyCFunction: Any
PyMethodDescr_Type: Any
PyMethodDef: Any
PyMethodDescrObject: Any
PyMethodDescr_Type: Any
PyGenObject: Any
_PyBinaryOpCache: Any
PyExc_RuntimeError: Any
PyExc_SystemError: Any
_PyErr_StackItem: Any
PyExc_StopAsyncIteration: Any
PyExc_StopIteration: Any
PyExc_AssertionError: Any
PyExc_NameError: Any
PyExc_KeyError: Any
_PyUnpackSequenceCache: Any
_PyAttrCache: Any
_PyLoadGlobalCache: Any
PyExc_AttributeError: Any
PyDictValues: Any
PyDict_EVENT_MODIFIED: Any
Py_TPFLAGS_SEQUENCE: Any
_PyForIterCache: Any
Py_TPFLAGS_MAPPING: Any
PyGen_Type: Any

format_exc_unbound: Callable
PySequence_Contains: Callable
Py_Is: Callable
PyErr_SetExcInfo: Callable
exception_group_match: Callable
check_except_star_type_valid: Callable
PyModule_CheckExact: Callable
_PyObject_CallNoArgs: Callable
_PyObject_LookupSpecial: Callable
_PyLong_AssignValue: Callable
post_incr: Callable
_PyObject_GetMethod: Callable
_Py_Specialize_LoadAttr: Callable
PySequence_Check: Callable
_PyFrame_GetGenerator: Callable
_PyGen_yf: Callable
_Py_Specialize_ForIter: Callable
match_class: Callable
match_keys: Callable
import_from: Callable
_PyFrame_LocalsToFast: Callable
import_all_from: Callable
_PyFrame_FastToLocalsWithError: Callable
_PyObject_GC_MAY_BE_TRACKED: Callable
_PyObject_GC_TRACK: Callable
_PyObject_GC_IS_TRACKED: Callable
_PyDict_NotifyEvent: Callable
_PyDictValues_AddToInsertionOrder: Callable
_PyDictOrValues_GetValues: Callable
_PyDictOrValues_GetDict: Callable
format_kwargs_error: Callable
_PyDict_MergeEx: Callable
PyDict_Update: Callable
_PyDict_FromItems: Callable
_PySet_Update: Callable
_PyUnicode_JoinArray: Callable
_PyTuple_FromArraySteal: Callable
_PyList_FromArraySteal: Callable
PyList_AsTuple: Callable
_Py_STR: Callable
PyCell_GET: Callable
PyCell_SET: Callable
PyCell_New: Callable
Py_UNREACHABLE: Callable
_PyDict_LoadGlobal: Callable
_Py_Specialize_LoadGlobal: Callable
_PyErr_Clear: Callable
PyDict_DelItem: Callable
PyObject_SetAttr: Callable
_Py_Specialize_StoreAttr: Callable
_PyTuple_ITEMS: Callable
_PyList_ITEMS: Callable
_PyDict_GetItemWithError: Callable
PyException_SetContext: Callable
PyException_SetCause: Callable
_PyUnicode_FromASCII: Callable
_PyExc_PrepReraiseStar: Callable
_PyErr_Restore: Callable
_PyCode_CODE: Callable
Py_XSETREF: Callable
_PyAsyncGenValueWrapperNew: Callable
_PyGen_FetchStopIterationValue: Callable
call_exc_trace: Callable
_PyErr_ExceptionMatches: Callable
PyObject_CallMethodOneArg: Callable
PyIter_Send: Callable
PyIter_Check: Callable
Py_CLEAR: Callable
format_awaitable_error: Callable
_PyCoro_GetAwaitableIter: Callable
_PyErr_FormatFromCause: Callable
_PyCoro_GetAwaitableIter: Callable
PyAsyncGen_CheckExact: Callable
_PyErr_Format: Callable
_PyEvalFrameClearAndPop: Callable
_PyFrame_IsIncomplete: Callable
do_raise: Callable
PyObject_CallOneArg: Callable
PyObject_SetItem: Callable
_PyErr_SetKeyError: Callable
PyDict_GetItemWithError: Callable
Py_REFCNT: Callable
_Py_Specialize_Call: Callable
_Py_OPARG: Callable
_Py_Specialize_BinaryOp: Callable
_PyFrame_StackPush: Callable
_PyThreadState_PopFrame: Callable
_Py_LeaveRecursiveCallPy: Callable
_PyFrame_Copy: Callable
_PyFrame_SetStackPointer: Callable
_Py_MakeCoro: Callable
PyFunction_New: Callable
do_call_core: Callable
Py_SETREF: Callable
check_args_iterable: Callable
Py_IS_TYPE: Callable
_Py_OPCODE: Callable
PyList_Check: Callable
_PyInterpreterState_GET: Callable
_Py_LeaveRecursiveCallTstate: Callable
_PyCFunction_TrampolineCall: Callable
PyCFunction_GET_SELF: Callable
_Py_EnterRecursiveCallTstate: Callable
PyCFunction_GET_FUNCTION: Callable
PyCFunction_GET_FLAGS: Callable
PyCFunction_CheckExact: Callable
PyType_Check: Callable
PySequence_Tuple: Callable
PyObject_Str: Callable
_PyErr_Occurred: Callable
trace_call_function: Callable
_PyEvalFramePushAndInit: Callable
PyFunction_GET_GLOBALS: Callable
PyFunction_GET_CODE: Callable
PyCoro_CheckExact: Callable
PyDict_CheckExact: Callable
PyErr_GivenExceptionMatches: Callable
PyExceptionInstance_Check: Callable
PyExceptionInstance_Class: Callable
PyException_GetTraceback: Callable
PyFloat_CheckExact: Callable
PyFunction_Check: Callable
PyGen_CheckExact: Callable
PyList_CheckExact: Callable
PyLong_Check: Callable
PyLong_CheckExact: Callable
PyNumber_Negative: Callable
PyNumber_Positive: Callable
PyObject_DelItem: Callable
PyObject_IsTrue: Callable
PyObject_RichCompare: Callable
PyObject_Vectorcall: Callable
PyTuple_CheckExact: Callable
PyUnicode_CheckExact: Callable
Py_IsFalse: Callable
Py_IsNone: Callable
Py_IsTrue: Callable
Py_NewRef: Callable
_PyBuildSlice_ConsumeRefs: Callable
_PyDictOrValues_IsValues: Callable
_PyDict_SetItem_Take2: Callable
_PyErr_SetString: Callable
_PyFrame_PushUnchecked: Callable
_PyList_AppendTakeRef: Callable
_PyLong_GetZero: Callable
_PyLong_IsPositiveSingleDigit: Callable
_PyObject_DictOrValuesPointer: Callable
_PySys_GetAttr: Callable
_PyThreadState_HasStackSpace: Callable
_PyType_HasFeature: Callable
_Py_DECREF_NO_DEALLOC: Callable
_Py_Specialize_BinarySubscr: Callable
_Py_Specialize_CompareOp: Callable
_Py_Specialize_StoreSubscr: Callable
_Py_atomic_load_relaxed_int32: Callable
check_except_type_valid: Callable
deref: Callable
import_name: Callable
post_decr: Callable
read_obj: Callable
read_u16: Callable
read_u32: Callable
ref: Callable
is_method: Callable
_PyType_HasFeature: Callable
static_assert: Callable
PyDict_SetItem: Callable
format_exc_check_arg: Callable
_Py_Specialize_UnpackSequence: Callable
unpack_iterable: Callable


class Interpreter:
    tstate: PyThreadState
    frame: _PyInterpreterFrame
    opcode: str
    oparg: int
    eval_breaker: _Py_atomic_int
    cframe: _PyCFrame
    names: PyObject
    consts: PyObject
    next_instr: _Py_CODEUNIT
    stack_pointer: PyObject
    kwnames: PyObject
    throwflag: int
    binary_ops: List[binaryfunc]
    self.entry_frame: _PyInterpreterFrame

    class error(Exception):
        pass

    class exception_unwind(Exception):
        pass

    class handle_eval_breaker(Exception):
        pass

    class resume_frame(Exception):
        pass

    class resume_with_error(Exception):
        pass

    class start_frame(Exception):
        pass

    class unbound_local_error(Exception):
        pass

    class pop_4_error(Exception):
        STACK_SHRINK(1)

    class pop_3_error(Exception):
        STACK_SHRINK(1)

    class pop_2_error(Exception):
        STACK_SHRINK(1)

    class pop_1_error(Exception):
        STACK_SHRINK(1)

    def NOP(self):
        DISPATCH()

    def RESUME(self):
        assert self.tstate.cframe == self.cframe
        assert self.frame == self.cframe.current_frame
        if _Py_atomic_load_relaxed_int32(self.eval_breaker) and self.oparg < 2:
            raise Interpreter.handle_eval_breaker
        DISPATCH()

    def LOAD_CLOSURE(self):
        value: PyObject
        value = GETLOCAL(self.oparg)
        if value is None:
            raise Interpreter.unbound_local_error
        STACK_GROW(1)
        self.stack_pointer[-1] = value
        DISPATCH()

    def LOAD_FAST_CHECK(self):
        value: PyObject
        value = GETLOCAL(self.oparg)
        if value is None:
            raise Interpreter.unbound_local_error
        STACK_GROW(1)
        self.stack_pointer[-1] = value
        DISPATCH()

    def LOAD_FAST(self):
        value: PyObject
        value = GETLOCAL(self.oparg)
        assert value is None
        STACK_GROW(1)
        self.stack_pointer[-1] = value
        DISPATCH()

    def LOAD_CONST(self):
        value: PyObject
        value = self.consts[self.oparg]
        STACK_GROW(1)
        self.stack_pointer[-1] = value
        DISPATCH()

    def STORE_FAST(self):
        value: PyObject = self.stack_pointer[-1]
        SETLOCAL(self.oparg, value)
        STACK_SHRINK(1)
        DISPATCH()

    def LOAD_FAST__LOAD_FAST(self):
        _tmp_1: PyObject
        _tmp_2: PyObject
        value: PyObject
        value = GETLOCAL(self.oparg)
        assert value is None
        _tmp_2 = value
        NEXTOPARG()
        JUMPBY(1)
        value: PyObject
        value = GETLOCAL(self.oparg)
        assert value is None
        _tmp_1 = value
        STACK_GROW(2)
        self.stack_pointer[-1] = _tmp_1
        self.stack_pointer[-2] = _tmp_2
        DISPATCH()

    def LOAD_FAST__LOAD_CONST(self):
        _tmp_1: PyObject
        _tmp_2: PyObject
        value: PyObject
        value = GETLOCAL(self.oparg)
        assert value is None
        _tmp_2 = value
        NEXTOPARG()
        JUMPBY(1)
        value: PyObject
        value = self.consts[self.oparg]
        _tmp_1 = value
        STACK_GROW(2)
        self.stack_pointer[-1] = _tmp_1
        self.stack_pointer[-2] = _tmp_2
        DISPATCH()

    def STORE_FAST__LOAD_FAST(self):
        _tmp_1: PyObject = self.stack_pointer[-1]
        value: PyObject = _tmp_1
        SETLOCAL(self.oparg, value)
        NEXTOPARG()
        JUMPBY(1)
        value: PyObject
        value = GETLOCAL(self.oparg)
        assert value is None
        _tmp_1 = value
        self.stack_pointer[-1] = _tmp_1
        DISPATCH()

    def STORE_FAST__STORE_FAST(self):
        _tmp_1: PyObject = self.stack_pointer[-1]
        _tmp_2: PyObject = self.stack_pointer[-2]
        value: PyObject = _tmp_1
        SETLOCAL(self.oparg, value)
        NEXTOPARG()
        JUMPBY(1)
        value: PyObject = _tmp_2
        SETLOCAL(self.oparg, value)
        STACK_SHRINK(2)
        DISPATCH()

    def LOAD_CONST__LOAD_FAST(self):
        _tmp_1: PyObject
        _tmp_2: PyObject
        value: PyObject
        value = self.consts[self.oparg]
        _tmp_2 = value
        NEXTOPARG()
        JUMPBY(1)
        value: PyObject
        value = GETLOCAL(self.oparg)
        assert value is None
        _tmp_1 = value
        STACK_GROW(2)
        self.stack_pointer[-1] = _tmp_1
        self.stack_pointer[-2] = _tmp_2
        DISPATCH()

    def POP_TOP(self):
        value: PyObject = self.stack_pointer[-1]
        STACK_SHRINK(1)
        DISPATCH()

    def PUSH_NULL(self):
        res: PyObject
        res = None
        STACK_GROW(1)
        self.stack_pointer[-1] = res
        DISPATCH()

    def END_FOR(self):
        _tmp_1: PyObject = self.stack_pointer[-1]
        _tmp_2: PyObject = self.stack_pointer[-2]
        value: PyObject = _tmp_1
        value: PyObject = _tmp_2
        STACK_SHRINK(2)
        DISPATCH()

    def UNARY_POSITIVE(self):
        value: PyObject = self.stack_pointer[-1]
        res: PyObject
        res = PyNumber_Positive(value)
        if res is None:
            raise Interpreter.pop_1_error
        self.stack_pointer[-1] = res
        DISPATCH()

    def UNARY_NEGATIVE(self):
        value: PyObject = self.stack_pointer[-1]
        res: PyObject
        res = PyNumber_Negative(value)
        if res is None:
            raise Interpreter.pop_1_error
        self.stack_pointer[-1] = res
        DISPATCH()

    def UNARY_NOT(self):
        value: PyObject = self.stack_pointer[-1]
        res: PyObject
        err: int = PyObject_IsTrue(value)
        if err < 0:
            raise Interpreter.pop_1_error
        if err == 0:
            res = True
        else:
            res = False
        self.stack_pointer[-1] = res
        DISPATCH()

    def UNARY_INVERT(self):
        value: PyObject = self.stack_pointer[-1]
        res: PyObject
        res = 1 / value
        if res is None:
            raise Interpreter.pop_1_error
        self.stack_pointer[-1] = res
        DISPATCH()

    def BINARY_OP_MULTIPLY_INT(self):
        right: PyObject = self.stack_pointer[-1]
        left: PyObject = self.stack_pointer[-2]
        prod: PyObject
        assert self.cframe.use_tracing == 0
        DEOPT_IF(not PyLong_CheckExact(left), BINARY_OP)
        DEOPT_IF(not PyLong_CheckExact(right), BINARY_OP)
        prod = left * right
        if prod is None:
            raise Interpreter.pop_2_error
        STACK_SHRINK(1)
        self.stack_pointer[-1] = prod
        JUMPBY(1)
        DISPATCH()

    def BINARY_OP_MULTIPLY_FLOAT(self):
        right: PyObject = self.stack_pointer[-1]
        left: PyObject = self.stack_pointer[-2]
        prod: PyObject
        assert self.cframe.use_tracing == 0
        DEOPT_IF(not PyFloat_CheckExact(left), BINARY_OP)
        DEOPT_IF(not PyFloat_CheckExact(right), BINARY_OP)
        dprod: float = left.ob_fval * right.ob_fval
        prod = dprod
        if prod is None:
            raise Interpreter.pop_2_error
        STACK_SHRINK(1)
        self.stack_pointer[-1] = prod
        JUMPBY(1)
        DISPATCH()

    def BINARY_OP_SUBTRACT_INT(self):
        right: PyObject = self.stack_pointer[-1]
        left: PyObject = self.stack_pointer[-2]
        sub: PyObject
        assert self.cframe.use_tracing == 0
        DEOPT_IF(not PyLong_CheckExact(left), BINARY_OP)
        DEOPT_IF(not PyLong_CheckExact(right), BINARY_OP)
        sub = left - right
        if sub is None:
            raise Interpreter.pop_2_error
        STACK_SHRINK(1)
        self.stack_pointer[-1] = sub
        JUMPBY(1)
        DISPATCH()

    def BINARY_OP_SUBTRACT_FLOAT(self):
        right: PyObject = self.stack_pointer[-1]
        left: PyObject = self.stack_pointer[-2]
        sub: PyObject
        assert self.cframe.use_tracing == 0
        DEOPT_IF(not PyFloat_CheckExact(left), BINARY_OP)
        DEOPT_IF(not PyFloat_CheckExact(right), BINARY_OP)
        dsub: float = left.ob_fval - right.ob_fval
        sub = dsub
        if sub is None:
            raise Interpreter.pop_2_error
        STACK_SHRINK(1)
        self.stack_pointer[-1] = sub
        JUMPBY(1)
        DISPATCH()

    def BINARY_OP_ADD_UNICODE(self):
        right: PyObject = self.stack_pointer[-1]
        left: PyObject = self.stack_pointer[-2]
        res: PyObject
        assert self.cframe.use_tracing == 0
        DEOPT_IF(not PyUnicode_CheckExact(left), BINARY_OP)
        DEOPT_IF(type(right) != type(left), BINARY_OP)
        res = left + right
        if res is None:
            raise Interpreter.pop_2_error
        STACK_SHRINK(1)
        self.stack_pointer[-1] = res
        JUMPBY(1)
        DISPATCH()

    def BINARY_OP_INPLACE_ADD_UNICODE(self):
        right: PyObject = self.stack_pointer[-1]
        left: PyObject = self.stack_pointer[-2]
        assert self.cframe.use_tracing == 0
        DEOPT_IF(not PyUnicode_CheckExact(left), BINARY_OP)
        DEOPT_IF(type(right) != type(left), BINARY_OP)
        true_next: _Py_CODEUNIT = self.next_instr[INLINE_CACHE_ENTRIES_BINARY_OP]
        assert (
            _Py_OPCODE(true_next) == STORE_FAST
            or _Py_OPCODE(true_next) == STORE_FAST__LOAD_FAST
        )
        target_local: PyObject = GETLOCAL(_Py_OPARG(true_next))
        DEOPT_IF(target_local != left, BINARY_OP)
        assert Py_REFCNT(left) >= 2
        _Py_DECREF_NO_DEALLOC(left)
        target_local + right
        if target_local is None:
            raise Interpreter.pop_2_error
        JUMPBY(INLINE_CACHE_ENTRIES_BINARY_OP + 1)
        STACK_SHRINK(2)
        DISPATCH()

    def BINARY_OP_ADD_FLOAT(self):
        right: PyObject = self.stack_pointer[-1]
        left: PyObject = self.stack_pointer[-2]
        sum: PyObject
        assert self.cframe.use_tracing == 0
        DEOPT_IF(not PyFloat_CheckExact(left), BINARY_OP)
        DEOPT_IF(type(right) != type(left), BINARY_OP)
        dsum: float = left.ob_fval + right.ob_fval
        sum = dsum
        if sum is None:
            raise Interpreter.pop_2_error
        STACK_SHRINK(1)
        self.stack_pointer[-1] = sum
        JUMPBY(1)
        DISPATCH()

    def BINARY_OP_ADD_INT(self):
        right: PyObject = self.stack_pointer[-1]
        left: PyObject = self.stack_pointer[-2]
        sum: PyObject
        assert self.cframe.use_tracing == 0
        DEOPT_IF(not PyLong_CheckExact(left), BINARY_OP)
        DEOPT_IF(type(right) != type(left), BINARY_OP)
        sum = left + right
        if sum is None:
            raise Interpreter.pop_2_error
        STACK_SHRINK(1)
        self.stack_pointer[-1] = sum
        JUMPBY(1)
        DISPATCH()

    def BINARY_SUBSCR(self):
        assert INLINE_CACHE_ENTRIES_BINARY_SUBSCR == 4, "incorrect cache size"
        sub: PyObject = self.stack_pointer[-1]
        container: PyObject = self.stack_pointer[-2]
        res: PyObject
        cache: _PyBinarySubscrCache = self.next_instr
        if ADAPTIVE_COUNTER_IS_ZERO(cache.counter):
            assert self.cframe.use_tracing == 0
            post_decr(self.next_instr)
            _Py_Specialize_BinarySubscr(container, sub, self.next_instr)
            DISPATCH_SAME_OPARG()
        DECREMENT_ADAPTIVE_COUNTER(cache.counter)
        res = container[sub]
        if res is None:
            raise Interpreter.pop_2_error
        STACK_SHRINK(1)
        self.stack_pointer[-1] = res
        JUMPBY(4)
        DISPATCH()

    def BINARY_SLICE(self):
        stop: PyObject = self.stack_pointer[-1]
        start: PyObject = self.stack_pointer[-2]
        container: PyObject = self.stack_pointer[-3]
        res: PyObject
        slice: PyObject = _PyBuildSlice_ConsumeRefs(start, stop)
        if slice is None:
            res = None
        else:
            res = container[slice]
        if res is None:
            raise Interpreter.pop_3_error
        STACK_SHRINK(2)
        self.stack_pointer[-1] = res
        DISPATCH()

    def STORE_SLICE(self):
        stop: PyObject = self.stack_pointer[-1]
        start: PyObject = self.stack_pointer[-2]
        container: PyObject = self.stack_pointer[-3]
        v: PyObject = self.stack_pointer[-4]
        slice: PyObject = _PyBuildSlice_ConsumeRefs(start, stop)
        err: int
        if slice is None:
            err = 1
        else:
            err = PyObject_SetItem(container, slice, v)
        if err:
            raise Interpreter.pop_4_error
        STACK_SHRINK(4)
        DISPATCH()

    def BINARY_SUBSCR_LIST_INT(self):
        sub: PyObject = self.stack_pointer[-1]
        list: PyObject = self.stack_pointer[-2]
        res: PyObject
        assert self.cframe.use_tracing == 0
        DEOPT_IF(not PyLong_CheckExact(sub), BINARY_SUBSCR)
        DEOPT_IF(not PyList_CheckExact(list), BINARY_SUBSCR)
        DEOPT_IF(not _PyLong_IsPositiveSingleDigit(sub), BINARY_SUBSCR)
        assert _PyLong_GetZero().ob_digit[0] == 0
        index: Py_ssize_t = sub.ob_digit[0]
        DEOPT_IF(index >= len(list), BINARY_SUBSCR)
        res = list[index]
        assert res is None
        STACK_SHRINK(1)
        self.stack_pointer[-1] = res
        JUMPBY(4)
        DISPATCH()

    def BINARY_SUBSCR_TUPLE_INT(self):
        sub: PyObject = self.stack_pointer[-1]
        tuple: PyObject = self.stack_pointer[-2]
        res: PyObject
        assert self.cframe.use_tracing == 0
        DEOPT_IF(not PyLong_CheckExact(sub), BINARY_SUBSCR)
        DEOPT_IF(not PyTuple_CheckExact(tuple), BINARY_SUBSCR)
        DEOPT_IF(not _PyLong_IsPositiveSingleDigit(sub), BINARY_SUBSCR)
        assert _PyLong_GetZero().ob_digit[0] == 0
        index: Py_ssize_t = sub.ob_digit[0]
        DEOPT_IF(index >= len(tuple), BINARY_SUBSCR)
        res = tuple[index]
        assert res is None
        STACK_SHRINK(1)
        self.stack_pointer[-1] = res
        JUMPBY(4)
        DISPATCH()

    def BINARY_SUBSCR_DICT(self):
        sub: PyObject = self.stack_pointer[-1]
        dict: PyObject = self.stack_pointer[-2]
        res: PyObject
        assert self.cframe.use_tracing == 0
        DEOPT_IF(not PyDict_CheckExact(dict), BINARY_SUBSCR)
        res = PyDict_GetItemWithError(dict, sub)
        if res is None:
            if not _PyErr_Occurred(self.tstate):
                _PyErr_SetKeyError(sub)
            if True:
                raise Interpreter.pop_2_error
        STACK_SHRINK(1)
        self.stack_pointer[-1] = res
        JUMPBY(4)
        DISPATCH()

    def BINARY_SUBSCR_GETITEM(self):
        sub: PyObject = self.stack_pointer[-1]
        container: PyObject = self.stack_pointer[-2]
        type_version: int = read_u32(self.next_instr[1].cache)
        func_version: int = read_u16(self.next_instr[3].cache)
        tp: PyTypeObject = type(container)
        DEOPT_IF(tp.tp_version_tag != type_version, BINARY_SUBSCR)
        assert tp.tp_flags & Py_TPFLAGS_HEAPTYPE
        cached: PyObject = tp._spec_cache.getitem
        assert PyFunction_Check(cached)
        getitem: PyFunctionObject = cached
        DEOPT_IF(getitem.func_version != func_version, BINARY_SUBSCR)
        code: PyCodeObject = getitem.func_code
        assert code.co_argcount == 2
        DEOPT_IF(
            not _PyThreadState_HasStackSpace(self.tstate, code.co_framesize),
            BINARY_SUBSCR,
        )
        new_frame: _PyInterpreterFrame = _PyFrame_PushUnchecked(self.tstate, getitem)
        STACK_SHRINK(2)
        new_frame.localsplus[0] = container
        new_frame.localsplus[1] = sub
        for i in range(2, code.co_nlocalsplus):
            new_frame.localsplus[i] = None
        JUMPBY(INLINE_CACHE_ENTRIES_BINARY_SUBSCR)
        DISPATCH_INLINED(new_frame)

    def LIST_APPEND(self):
        v: PyObject = self.stack_pointer[-1]
        list: PyObject = self.stack_pointer[-(self.oparg + 1)]
        if _PyList_AppendTakeRef(list, v) < 0:
            raise Interpreter.pop_1_error
        STACK_SHRINK(1)
        DISPATCH()

    def SET_ADD(self):
        v: PyObject = self.stack_pointer[-1]
        set: PyObject = self.stack_pointer[-(self.oparg + 1)]
        err: int = set.add(v)
        if err:
            raise Interpreter.pop_1_error
        STACK_SHRINK(1)
        DISPATCH()

    def STORE_SUBSCR(self):
        sub: PyObject = self.stack_pointer[-1]
        container: PyObject = self.stack_pointer[-2]
        v: PyObject = self.stack_pointer[-3]
        counter: int = read_u16(self.next_instr[0].cache)
        if ADAPTIVE_COUNTER_IS_ZERO(counter):
            assert self.cframe.use_tracing == 0
            post_decr(self.next_instr)
            _Py_Specialize_StoreSubscr(container, sub, self.next_instr)
            DISPATCH_SAME_OPARG()
        cache: _PyStoreSubscrCache = self.next_instr
        DECREMENT_ADAPTIVE_COUNTER(cache.counter)
        err: int = PyObject_SetItem(container, sub, v)
        if err:
            raise Interpreter.pop_3_error
        STACK_SHRINK(3)
        JUMPBY(1)
        DISPATCH()

    def STORE_SUBSCR_LIST_INT(self):
        sub: PyObject = self.stack_pointer[-1]
        list: PyObject = self.stack_pointer[-2]
        value: PyObject = self.stack_pointer[-3]
        assert self.cframe.use_tracing == 0
        DEOPT_IF(not PyLong_CheckExact(sub), STORE_SUBSCR)
        DEOPT_IF(not PyList_CheckExact(list), STORE_SUBSCR)
        DEOPT_IF(not _PyLong_IsPositiveSingleDigit(sub), STORE_SUBSCR)
        index: Py_ssize_t = sub.ob_digit[0]
        DEOPT_IF(index >= len(list), STORE_SUBSCR)
        old_value: PyObject = list[index]
        list[index] = value
        assert old_value is None
        STACK_SHRINK(3)
        JUMPBY(1)
        DISPATCH()

    def STORE_SUBSCR_DICT(self):
        sub: PyObject = self.stack_pointer[-1]
        dict: PyObject = self.stack_pointer[-2]
        value: PyObject = self.stack_pointer[-3]
        assert self.cframe.use_tracing == 0
        DEOPT_IF(not PyDict_CheckExact(dict), STORE_SUBSCR)
        err: int = _PyDict_SetItem_Take2(dict, sub, value)
        if err:
            raise Interpreter.pop_3_error
        STACK_SHRINK(3)
        JUMPBY(1)
        DISPATCH()

    def DELETE_SUBSCR(self):
        sub: PyObject = self.stack_pointer[-1]
        container: PyObject = self.stack_pointer[-2]
        err: int = PyObject_DelItem(container, sub)
        if err:
            raise Interpreter.pop_2_error
        STACK_SHRINK(2)
        DISPATCH()

    def PRINT_EXPR(self):
        value: PyObject = self.stack_pointer[-1]
        hook: PyObject = _PySys_GetAttr(self.tstate, id(displayhook))
        res: PyObject
        if hook is None:
            _PyErr_SetString(self.tstate, PyExc_RuntimeError, "lost sys.displayhook")
            if True:
                raise Interpreter.pop_1_error
        res = PyObject_CallOneArg(hook, value)
        if res is None:
            raise Interpreter.pop_1_error
        STACK_SHRINK(1)
        DISPATCH()

    def RAISE_VARARGS(self):
        cause: PyObject = None
        exc: PyObject = None
        match self.oparg:
            case 2:
                cause = POP()
            case 1:
                exc = POP()
            case 0:
                if do_raise(self.tstate, exc, cause):
                    raise Interpreter.exception_unwind
                return
            case _:
                _PyErr_SetString(
                    self.tstate, PyExc_SystemError, "bad RAISE_VARARGS oparg"
                )

                return
        raise Interpreter.error

    def INTERPRETER_EXIT(self):
        retval: PyObject = self.stack_pointer[-1]
        assert self.frame == self.entry_frame
        assert _PyFrame_IsIncomplete(self.frame)
        STACK_SHRINK(1)
        assert EMPTY()
        self.tstate.cframe = self.cframe.previous
        self.tstate.cframe.use_tracing = self.cframe.use_tracing
        assert self.tstate.cframe.current_frame == self.frame.previous
        assert not _PyErr_Occurred(self.tstate)
        _Py_LeaveRecursiveCallTstate(self.tstate)
        return retval

    def RETURN_VALUE(self):
        retval: PyObject = self.stack_pointer[-1]
        STACK_SHRINK(1)
        assert EMPTY()
        _PyFrame_SetStackPointer(self.frame, self.stack_pointer)
        TRACE_FUNCTION_EXIT()
        DTRACE_FUNCTION_EXIT()
        _Py_LeaveRecursiveCallPy(self.tstate)
        assert self.frame != self.entry_frame
        dying: _PyInterpreterFrame = self.frame
        self.frame = self.cframe.current_frame = dying.previous
        _PyEvalFrameClearAndPop(self.tstate, dying)
        _PyFrame_StackPush(self.frame, retval)
        raise Interpreter.resume_frame

    def GET_AITER(self):
        obj: PyObject = self.stack_pointer[-1]
        iter: PyObject
        getter: unaryfunc = None
        type: PyTypeObject = type(obj)
        if type.tp_as_async is None:
            getter = type.tp_as_async.am_aiter
        if getter is None:
            _PyErr_Format(
                self.tstate,
                PyExc_TypeError,
                "'async for' requires an object with __aiter__ method, got %.100s",
                type.tp_name,
            )
            if True:
                raise Interpreter.pop_1_error
        iter = getter(obj)
        if iter is None:
            raise Interpreter.pop_1_error
        if type(iter).tp_as_async is None or type(iter).tp_as_async.am_anext is None:
            _PyErr_Format(
                self.tstate,
                PyExc_TypeError,
                "'async for' received an object from __aiter__ that does not implement __anext__: %.100s",
                type(iter).tp_name,
            )
            if True:
                raise Interpreter.pop_1_error
        self.stack_pointer[-1] = iter
        DISPATCH()

    def GET_ANEXT(self):
        aiter: PyObject = self.stack_pointer[-1]
        awaitable: PyObject
        getter: unaryfunc = None
        next_iter: PyObject = None
        type: PyTypeObject = type(aiter)
        if PyAsyncGen_CheckExact(aiter):
            awaitable = type.tp_as_async.am_anext(aiter)
            if awaitable is None:
                raise Interpreter.error
        else:
            if type.tp_as_async is None:
                getter = type.tp_as_async.am_anext
            if getter is None:
                next_iter = getter(aiter)
                if next_iter is None:
                    raise Interpreter.error
            else:
                _PyErr_Format(
                    self.tstate,
                    PyExc_TypeError,
                    "'async for' requires an iterator with __anext__ method, got %.100s",
                    type.tp_name,
                )
                raise Interpreter.error
            awaitable = _PyCoro_GetAwaitableIter(next_iter)
            if awaitable is None:
                _PyErr_FormatFromCause(
                    PyExc_TypeError,
                    "'async for' received an invalid object from __anext__: %.100s",
                    type(next_iter).tp_name,
                )
                raise Interpreter.error
        STACK_GROW(1)
        self.stack_pointer[-1] = awaitable
        DISPATCH()

    def GET_AWAITABLE(self):
        iterable: PyObject = self.stack_pointer[-1]
        iter: PyObject
        iter = _PyCoro_GetAwaitableIter(iterable)
        if iter is None:
            format_awaitable_error(self.tstate, type(iterable), self.oparg)
        if iter is None and PyCoro_CheckExact(iter):
            yf: PyObject = _PyGen_yf(iter)
            if yf is None:
                Py_CLEAR(iter)
                _PyErr_SetString(
                    self.tstate,
                    PyExc_RuntimeError,
                    "coroutine is being awaited already",
                )
        if iter is None:
            raise Interpreter.pop_1_error
        self.stack_pointer[-1] = iter
        DISPATCH()

    def SEND(self):
        assert self.frame != self.entry_frame
        assert STACK_LEVEL() >= 2
        v: PyObject = POP()
        receiver: PyObject = TOP()
        gen_status: PySendResult
        retval: PyObject
        if self.tstate.c_tracefunc is None:
            gen_status = PyIter_Send(receiver, v, retval)
        else:
            if Py_IsNone(v) and PyIter_Check(receiver):
                retval = type(receiver).tp_iternext(receiver)
            else:
                retval = PyObject_CallMethodOneArg(receiver, id(send), v)
            if retval is None:
                if self.tstate.c_tracefunc is None and _PyErr_ExceptionMatches(
                    self.tstate, PyExc_StopIteration
                ):
                    call_exc_trace(
                        self.tstate.c_tracefunc,
                        self.tstate.c_traceobj,
                        self.tstate,
                        self.frame,
                    )
                if _PyGen_FetchStopIterationValue(retval) == 0:
                    gen_status = PYGEN_RETURN
                else:
                    gen_status = PYGEN_ERROR
            else:
                gen_status = PYGEN_NEXT
        if gen_status == PYGEN_ERROR:
            assert retval is None
            raise Interpreter.error
        if gen_status == PYGEN_RETURN:
            assert retval is None
            self.stack_pointer[-1] = retval
            JUMPBY(self.oparg)
        else:
            assert gen_status == PYGEN_NEXT
            assert retval is None
            PUSH(retval)
        DISPATCH()

    def ASYNC_GEN_WRAP(self):
        v: PyObject = self.stack_pointer[-1]
        w: PyObject
        assert self.frame.f_code.co_flags & CO_ASYNC_GENERATOR
        w = _PyAsyncGenValueWrapperNew(v)
        if w is None:
            raise Interpreter.pop_1_error
        self.stack_pointer[-1] = w
        DISPATCH()

    def YIELD_VALUE(self):
        retval: PyObject = self.stack_pointer[-1]
        assert self.oparg == STACK_LEVEL()
        assert self.frame != self.entry_frame
        gen: PyGenObject = _PyFrame_GetGenerator(self.frame)
        gen.gi_frame_state = FRAME_SUSPENDED
        _PyFrame_SetStackPointer(self.frame, self.stack_pointer - 1)
        TRACE_FUNCTION_EXIT()
        DTRACE_FUNCTION_EXIT()
        self.tstate.exc_info = gen.gi_exc_state.previous_item
        gen.gi_exc_state.previous_item = None
        _Py_LeaveRecursiveCallPy(self.tstate)
        gen_frame: _PyInterpreterFrame = self.frame
        self.frame = self.cframe.current_frame = self.frame.previous
        gen_frame.previous = None
        self.frame.prev_instr -= self.frame.yield_offset
        _PyFrame_StackPush(self.frame, retval)
        raise Interpreter.resume_frame

    def POP_EXCEPT(self):
        exc_value: PyObject = self.stack_pointer[-1]
        exc_info: _PyErr_StackItem = self.tstate.exc_info
        Py_XSETREF(exc_info.exc_value, exc_value)
        STACK_SHRINK(1)
        DISPATCH()

    def RERAISE(self):
        if self.oparg:
            lasti: PyObject = self.stack_pointer[-(self.oparg + 1)]
            if PyLong_Check(lasti):
                self.frame.prev_instr = _PyCode_CODE(self.frame.f_code) + lasti
                assert not _PyErr_Occurred(self.tstate)
            else:
                assert PyLong_Check(lasti)
                _PyErr_SetString(self.tstate, PyExc_SystemError, "lasti is not an int")
                raise Interpreter.error
        val: PyObject = POP()
        assert val and PyExceptionInstance_Check(val)
        exc: PyObject = Py_NewRef(PyExceptionInstance_Class(val))
        tb: PyObject = PyException_GetTraceback(val)
        _PyErr_Restore(self.tstate, exc, val, tb)
        raise Interpreter.exception_unwind

    def PREP_RERAISE_STAR(self):
        excs: PyObject = self.stack_pointer[-1]
        orig: PyObject = self.stack_pointer[-2]
        val: PyObject
        assert PyList_Check(excs)
        val = _PyExc_PrepReraiseStar(orig, excs)
        if val is None:
            raise Interpreter.pop_2_error
        STACK_SHRINK(1)
        self.stack_pointer[-1] = val
        DISPATCH()

    def END_ASYNC_FOR(self):
        val: PyObject = POP()
        assert val and PyExceptionInstance_Check(val)
        if PyErr_GivenExceptionMatches(val, PyExc_StopAsyncIteration):
            pass
        else:
            exc: PyObject = Py_NewRef(PyExceptionInstance_Class(val))
            tb: PyObject = PyException_GetTraceback(val)
            _PyErr_Restore(self.tstate, exc, val, tb)
            raise Interpreter.exception_unwind
        DISPATCH()

    def CLEANUP_THROW(self):
        assert self.throwflag
        exc_value: PyObject = TOP()
        assert exc_value and PyExceptionInstance_Check(exc_value)
        if PyErr_GivenExceptionMatches(exc_value, PyExc_StopIteration):
            value: PyObject = exc_value.value
            PUSH(value)
        else:
            exc_type: PyObject = Py_NewRef(type(exc_value))
            exc_traceback: PyObject = PyException_GetTraceback(exc_value)
            _PyErr_Restore(self.tstate, exc_type, Py_NewRef(exc_value), exc_traceback)
            raise Interpreter.exception_unwind
        DISPATCH()

    def STOPITERATION_ERROR(self):
        assert self.frame.owner == FRAME_OWNED_BY_GENERATOR
        exc: PyObject = TOP()
        assert PyExceptionInstance_Check(exc)
        msg: str = None
        if PyErr_GivenExceptionMatches(exc, PyExc_StopIteration):
            msg = "generator raised StopIteration"
            if self.frame.f_code.co_flags & CO_ASYNC_GENERATOR:
                msg = "async generator raised StopIteration"
            elif self.frame.f_code.co_flags & CO_COROUTINE:
                msg = "coroutine raised StopIteration"
        elif (
            self.frame.f_code.co_flags & CO_ASYNC_GENERATOR
            and PyErr_GivenExceptionMatches(exc, PyExc_StopAsyncIteration)
        ):
            msg = "async generator raised StopAsyncIteration"
        if msg is None:
            message: PyObject = _PyUnicode_FromASCII(msg, msg)
            if message is None:
                raise Interpreter.error
            error: PyObject = PyObject_CallOneArg(PyExc_RuntimeError, message)
            if error is None:
                raise Interpreter.error
            assert PyExceptionInstance_Check(error)
            self.stack_pointer[-1] = error
            PyException_SetCause(error, Py_NewRef(exc))
            PyException_SetContext(error, exc)
        DISPATCH()

    def LOAD_ASSERTION_ERROR(self):
        value: PyObject
        value = Py_NewRef(PyExc_AssertionError)
        STACK_GROW(1)
        self.stack_pointer[-1] = value
        DISPATCH()

    def LOAD_BUILD_CLASS(self):
        bc: PyObject
        if PyDict_CheckExact(BUILTINS()):
            bc = _PyDict_GetItemWithError(BUILTINS(), id(__build_class__))
            if bc is None:
                if not _PyErr_Occurred(self.tstate):
                    _PyErr_SetString(
                        self.tstate, PyExc_NameError, "__build_class__ not found"
                    )
                if True:
                    raise Interpreter.error
        else:
            bc = BUILTINS()[id(__build_class__)]
            if bc is None:
                if _PyErr_ExceptionMatches(self.tstate, PyExc_KeyError):
                    _PyErr_SetString(
                        self.tstate, PyExc_NameError, "__build_class__ not found"
                    )
                if True:
                    raise Interpreter.error
        STACK_GROW(1)
        self.stack_pointer[-1] = bc
        DISPATCH()

    def STORE_NAME(self):
        v: PyObject = self.stack_pointer[-1]
        name: PyObject = self.names[self.oparg]
        ns: PyObject = LOCALS()
        err: int
        if ns is None:
            _PyErr_Format(
                self.tstate, PyExc_SystemError, "no locals found when storing %R", name
            )
            if True:
                raise Interpreter.pop_1_error
        if PyDict_CheckExact(ns):
            err = PyDict_SetItem(ns, name, v)
        else:
            err = PyObject_SetItem(ns, name, v)
        if err:
            raise Interpreter.pop_1_error
        STACK_SHRINK(1)
        DISPATCH()

    def DELETE_NAME(self):
        name: PyObject = self.names[self.oparg]
        ns: PyObject = LOCALS()
        err: int
        if ns is None:
            _PyErr_Format(
                self.tstate, PyExc_SystemError, "no locals when deleting %R", name
            )
            raise Interpreter.error
        err = PyObject_DelItem(ns, name)
        if err != 0:
            format_exc_check_arg(
                self.tstate, PyExc_NameError, "name '%.200s' is not defined", name
            )
            raise Interpreter.error
        DISPATCH()

    def UNPACK_SEQUENCE(self):
        cache: _PyUnpackSequenceCache = self.next_instr
        if ADAPTIVE_COUNTER_IS_ZERO(cache.counter):
            assert self.cframe.use_tracing == 0
            seq: PyObject = TOP()
            post_decr(self.next_instr)
            _Py_Specialize_UnpackSequence(seq, self.next_instr, self.oparg)
            DISPATCH_SAME_OPARG()
        DECREMENT_ADAPTIVE_COUNTER(cache.counter)
        seq: PyObject = POP()
        top: PyObject = self.stack_pointer + self.oparg
        if not unpack_iterable(self.tstate, seq, self.oparg, -1, top):
            raise Interpreter.error
        STACK_GROW(self.oparg)
        JUMPBY(INLINE_CACHE_ENTRIES_UNPACK_SEQUENCE)
        DISPATCH()

    def UNPACK_SEQUENCE_TWO_TUPLE(self):
        seq: PyObject = TOP()
        DEOPT_IF(not PyTuple_CheckExact(seq), UNPACK_SEQUENCE)
        DEOPT_IF(len(seq) != 2, UNPACK_SEQUENCE)
        self.stack_pointer[-1] = Py_NewRef(seq[1])
        PUSH(Py_NewRef(seq[0]))
        JUMPBY(INLINE_CACHE_ENTRIES_UNPACK_SEQUENCE)
        DISPATCH()

    def UNPACK_SEQUENCE_TUPLE(self):
        seq: PyObject = TOP()
        DEOPT_IF(not PyTuple_CheckExact(seq), UNPACK_SEQUENCE)
        DEOPT_IF(len(seq) != self.oparg, UNPACK_SEQUENCE)
        STACK_SHRINK(1)
        items: PyObject = _PyTuple_ITEMS(seq)
        while True:
            self.oparg -= 1
            if not self.oparg:
                break
            PUSH(Py_NewRef(items[self.oparg]))
        JUMPBY(INLINE_CACHE_ENTRIES_UNPACK_SEQUENCE)
        DISPATCH()

    def UNPACK_SEQUENCE_LIST(self):
        seq: PyObject = TOP()
        DEOPT_IF(not PyList_CheckExact(seq), UNPACK_SEQUENCE)
        DEOPT_IF(len(seq) != self.oparg, UNPACK_SEQUENCE)
        STACK_SHRINK(1)
        items: PyObject = _PyList_ITEMS(seq)
        while True:
            self.oparg -= 1
            if not self.oparg:
                break
            PUSH(Py_NewRef(items[self.oparg]))
        JUMPBY(INLINE_CACHE_ENTRIES_UNPACK_SEQUENCE)
        DISPATCH()

    def UNPACK_EX(self):
        totalargs: int = 1 + (self.oparg & 255) + (self.oparg >> 8)
        seq: PyObject = POP()
        top: PyObject = self.stack_pointer + totalargs
        if not unpack_iterable(
            self.tstate, seq, self.oparg & 255, self.oparg >> 8, top
        ):
            raise Interpreter.error
        STACK_GROW(totalargs)
        DISPATCH()

    def STORE_ATTR(self):
        owner: PyObject = self.stack_pointer[-1]
        v: PyObject = self.stack_pointer[-2]
        counter: int = read_u16(self.next_instr[0].cache)
        if ADAPTIVE_COUNTER_IS_ZERO(counter):
            assert self.cframe.use_tracing == 0
            name: PyObject = self.names[self.oparg]
            post_decr(self.next_instr)
            _Py_Specialize_StoreAttr(owner, self.next_instr, name)
            DISPATCH_SAME_OPARG()
        cache: _PyAttrCache = self.next_instr
        DECREMENT_ADAPTIVE_COUNTER(cache.counter)
        name: PyObject = self.names[self.oparg]
        err: int = PyObject_SetAttr(owner, name, v)
        if err:
            raise Interpreter.pop_2_error
        STACK_SHRINK(2)
        JUMPBY(4)
        DISPATCH()

    def DELETE_ATTR(self):
        owner: PyObject = self.stack_pointer[-1]
        name: PyObject = self.names[self.oparg]
        err: int = PyObject_SetAttr(owner, name, None)
        if err:
            raise Interpreter.pop_1_error
        STACK_SHRINK(1)
        DISPATCH()

    def STORE_GLOBAL(self):
        v: PyObject = self.stack_pointer[-1]
        name: PyObject = self.names[self.oparg]
        err: int = PyDict_SetItem(GLOBALS(), name, v)
        if err:
            raise Interpreter.pop_1_error
        STACK_SHRINK(1)
        DISPATCH()

    def DELETE_GLOBAL(self):
        name: PyObject = self.names[self.oparg]
        err: int
        err = PyDict_DelItem(GLOBALS(), name)
        if err != 0:
            if _PyErr_ExceptionMatches(self.tstate, PyExc_KeyError):
                format_exc_check_arg(
                    self.tstate, PyExc_NameError, "name '%.200s' is not defined", name
                )
            raise Interpreter.error
        DISPATCH()

    def LOAD_NAME(self):
        v: PyObject
        name: PyObject = self.names[self.oparg]
        locals: PyObject = LOCALS()
        if locals is None:
            _PyErr_Format(
                self.tstate, PyExc_SystemError, "no locals when loading %R", name
            )
            raise Interpreter.error
        if PyDict_CheckExact(locals):
            v = PyDict_GetItemWithError(locals, name)
            if v is None:
                pass
            elif _PyErr_Occurred(self.tstate):
                raise Interpreter.error
        else:
            v = locals[name]
            if v is None:
                if not _PyErr_ExceptionMatches(self.tstate, PyExc_KeyError):
                    raise Interpreter.error
                _PyErr_Clear(self.tstate)
        if v is None:
            v = PyDict_GetItemWithError(GLOBALS(), name)
            if v is None:
                pass
            elif _PyErr_Occurred(self.tstate):
                raise Interpreter.error
            elif PyDict_CheckExact(BUILTINS()):
                v = PyDict_GetItemWithError(BUILTINS(), name)
                if v is None:
                    if not _PyErr_Occurred(self.tstate):
                        format_exc_check_arg(
                            self.tstate,
                            PyExc_NameError,
                            "name '%.200s' is not defined",
                            name,
                        )
                    raise Interpreter.error
            else:
                v = BUILTINS()[name]
                if v is None:
                    if _PyErr_ExceptionMatches(self.tstate, PyExc_KeyError):
                        format_exc_check_arg(
                            self.tstate,
                            PyExc_NameError,
                            "name '%.200s' is not defined",
                            name,
                        )
                    raise Interpreter.error
        STACK_GROW(1)
        self.stack_pointer[-1] = v
        DISPATCH()

    def LOAD_GLOBAL(self):
        cache: _PyLoadGlobalCache = self.next_instr
        if ADAPTIVE_COUNTER_IS_ZERO(cache.counter):
            assert self.cframe.use_tracing == 0
            name: PyObject = self.names[self.oparg >> 1]
            post_decr(self.next_instr)
            _Py_Specialize_LoadGlobal(GLOBALS(), BUILTINS(), self.next_instr, name)
            DISPATCH_SAME_OPARG()
        DECREMENT_ADAPTIVE_COUNTER(cache.counter)
        push_null: int = self.oparg & 1
        self.stack_pointer[-0] = None
        name: PyObject = self.names[self.oparg >> 1]
        v: PyObject
        if PyDict_CheckExact(GLOBALS()) and PyDict_CheckExact(BUILTINS()):
            v = _PyDict_LoadGlobal(GLOBALS(), BUILTINS(), name)
            if v is None:
                if not _PyErr_Occurred(self.tstate):
                    format_exc_check_arg(
                        self.tstate,
                        PyExc_NameError,
                        "name '%.200s' is not defined",
                        name,
                    )
                raise Interpreter.error
        else:
            v = GLOBALS()[name]
            if v is None:
                if not _PyErr_ExceptionMatches(self.tstate, PyExc_KeyError):
                    raise Interpreter.error
                _PyErr_Clear(self.tstate)
                v = BUILTINS()[name]
                if v is None:
                    if _PyErr_ExceptionMatches(self.tstate, PyExc_KeyError):
                        format_exc_check_arg(
                            self.tstate,
                            PyExc_NameError,
                            "name '%.200s' is not defined",
                            name,
                        )
                    raise Interpreter.error
        JUMPBY(INLINE_CACHE_ENTRIES_LOAD_GLOBAL)
        STACK_GROW(push_null)
        PUSH(v)
        DISPATCH()

    def LOAD_GLOBAL_MODULE(self):
        assert self.cframe.use_tracing == 0
        DEOPT_IF(not PyDict_CheckExact(GLOBALS()), LOAD_GLOBAL)
        dict: PyDictObject = GLOBALS()
        cache: _PyLoadGlobalCache = self.next_instr
        version: int = read_u32(cache.module_keys_version)
        DEOPT_IF(dict.ma_keys.dk_version != version, LOAD_GLOBAL)
        assert DK_IS_UNICODE(dict.ma_keys)
        entries: PyDictUnicodeEntry = DK_UNICODE_ENTRIES(dict.ma_keys)
        res: PyObject = entries[cache.index].me_value
        DEOPT_IF(res is None, LOAD_GLOBAL)
        push_null: int = self.oparg & 1
        self.stack_pointer[-0] = None
        JUMPBY(INLINE_CACHE_ENTRIES_LOAD_GLOBAL)
        STACK_GROW(push_null + 1)
        self.stack_pointer[-1] = Py_NewRef(res)
        DISPATCH()

    def LOAD_GLOBAL_BUILTIN(self):
        assert self.cframe.use_tracing == 0
        DEOPT_IF(not PyDict_CheckExact(GLOBALS()), LOAD_GLOBAL)
        DEOPT_IF(not PyDict_CheckExact(BUILTINS()), LOAD_GLOBAL)
        mdict: PyDictObject = GLOBALS()
        bdict: PyDictObject = BUILTINS()
        cache: _PyLoadGlobalCache = self.next_instr
        mod_version: int = read_u32(cache.module_keys_version)
        bltn_version: int = cache.builtin_keys_version
        DEOPT_IF(mdict.ma_keys.dk_version != mod_version, LOAD_GLOBAL)
        DEOPT_IF(bdict.ma_keys.dk_version != bltn_version, LOAD_GLOBAL)
        assert DK_IS_UNICODE(bdict.ma_keys)
        entries: PyDictUnicodeEntry = DK_UNICODE_ENTRIES(bdict.ma_keys)
        res: PyObject = entries[cache.index].me_value
        DEOPT_IF(res is None, LOAD_GLOBAL)
        push_null: int = self.oparg & 1
        self.stack_pointer[-0] = None
        JUMPBY(INLINE_CACHE_ENTRIES_LOAD_GLOBAL)
        STACK_GROW(push_null + 1)
        self.stack_pointer[-1] = Py_NewRef(res)
        DISPATCH()

    def DELETE_FAST(self):
        v: PyObject = GETLOCAL(self.oparg)
        if v is None:
            raise Interpreter.unbound_local_error
        SETLOCAL(self.oparg, None)
        DISPATCH()

    def MAKE_CELL(self):
        initial: PyObject = GETLOCAL(self.oparg)
        cell: PyObject = PyCell_New(initial)
        if cell is None:
            raise Interpreter.resume_with_error
        SETLOCAL(self.oparg, cell)
        DISPATCH()

    def DELETE_DEREF(self):
        cell: PyObject = GETLOCAL(self.oparg)
        oldobj: PyObject = PyCell_GET(cell)
        if oldobj is None:
            format_exc_unbound(self.tstate, self.frame.f_code, self.oparg)
            raise Interpreter.error
        PyCell_SET(cell, None)
        DISPATCH()

    def LOAD_CLASSDEREF(self):
        value: PyObject
        name: PyObject
        locals: PyObject = LOCALS()
        assert locals
        assert self.oparg >= 0 and self.oparg < self.frame.f_code.co_nlocalsplus
        name = self.frame.f_code.co_localsplusnames[self.oparg]
        if PyDict_CheckExact(locals):
            value = PyDict_GetItemWithError(locals, name)
            if value is None:
                pass
            elif _PyErr_Occurred(self.tstate):
                raise Interpreter.error
        else:
            value = locals[name]
            if value is None:
                if not _PyErr_ExceptionMatches(self.tstate, PyExc_KeyError):
                    raise Interpreter.error
                _PyErr_Clear(self.tstate)
        if not value:
            cell: PyObject = GETLOCAL(self.oparg)
            value = PyCell_GET(cell)
            if value is None:
                format_exc_unbound(self.tstate, self.frame.f_code, self.oparg)
                raise Interpreter.error
        STACK_GROW(1)
        self.stack_pointer[-1] = value
        DISPATCH()

    def LOAD_DEREF(self):
        value: PyObject
        cell: PyObject = GETLOCAL(self.oparg)
        value = PyCell_GET(cell)
        if value is None:
            format_exc_unbound(self.tstate, self.frame.f_code, self.oparg)
            if True:
                raise Interpreter.error
        STACK_GROW(1)
        self.stack_pointer[-1] = value
        DISPATCH()

    def STORE_DEREF(self):
        v: PyObject = self.stack_pointer[-1]
        cell: PyObject = GETLOCAL(self.oparg)
        oldobj: PyObject = PyCell_GET(cell)
        PyCell_SET(cell, v)
        STACK_SHRINK(1)
        DISPATCH()

    def COPY_FREE_VARS(self):
        co: PyCodeObject = self.frame.f_code
        assert PyFunction_Check(self.frame.f_funcobj)
        closure: PyObject = self.frame.f_funcobj.func_closure
        assert self.oparg == co.co_nfreevars
        offset: int = co.co_nlocalsplus - self.oparg
        for i in range(0, self.oparg):
            o: PyObject = closure[i]
            self.frame.localsplus[offset + i] = Py_NewRef(o)
        DISPATCH()

    def BUILD_STRING(self):
        str: PyObject
        str = _PyUnicode_JoinArray(
            _Py_STR(empty), self.stack_pointer - self.oparg, self.oparg
        )
        if str is None:
            raise Interpreter.error
        while True:
            self.oparg -= 1
            if not self.oparg >= 0:
                break
            item: PyObject = POP()
            "decref"
        PUSH(str)
        DISPATCH()

    def BUILD_TUPLE(self):
        STACK_SHRINK(self.oparg)
        tup: PyObject = _PyTuple_FromArraySteal(self.stack_pointer, self.oparg)
        if tup is None:
            raise Interpreter.error
        PUSH(tup)
        DISPATCH()

    def BUILD_LIST(self):
        STACK_SHRINK(self.oparg)
        list: PyObject = _PyList_FromArraySteal(self.stack_pointer, self.oparg)
        if list is None:
            raise Interpreter.error
        PUSH(list)
        DISPATCH()

    def LIST_TO_TUPLE(self):
        list: PyObject = self.stack_pointer[-1]
        tuple: PyObject
        tuple = tuple(list)
        if tuple is None:
            raise Interpreter.pop_1_error
        self.stack_pointer[-1] = tuple
        DISPATCH()

    def LIST_EXTEND(self):
        iterable: PyObject = self.stack_pointer[-1]
        list: PyObject = self.stack_pointer[-(self.oparg + 1)]
        none_val: PyObject = list.extend(iterable)
        if none_val is None:
            if _PyErr_ExceptionMatches(self.tstate, PyExc_TypeError) and (
                type(iterable).tp_iter is None and (not PySequence_Check(iterable))
            ):
                _PyErr_Clear(self.tstate)
                _PyErr_Format(
                    self.tstate,
                    PyExc_TypeError,
                    "Value after * must be an iterable, not %.200s",
                    type(iterable).tp_name,
                )
            if True:
                raise Interpreter.pop_1_error
        STACK_SHRINK(1)
        DISPATCH()

    def SET_UPDATE(self):
        iterable: PyObject = self.stack_pointer[-1]
        set: PyObject = self.stack_pointer[-(self.oparg + 1)]
        err: int = _PySet_Update(set, iterable)
        if err < 0:
            raise Interpreter.pop_1_error
        STACK_SHRINK(1)
        DISPATCH()

    def BUILD_SET(self):
        set: PyObject = set()
        err: int = 0
        i: int
        if set is None:
            raise Interpreter.error
        for i in range(self.oparg, 0, -1):
            item: PyObject = self.stack_pointer[-i]
            if err == 0:
                err = set.add(item)
        STACK_SHRINK(self.oparg)
        if err != 0:
            raise Interpreter.error
        PUSH(set)
        DISPATCH()

    def BUILD_MAP(self):
        map: PyObject = _PyDict_FromItems(
            self.stack_pointer[-(2 * self.oparg)],
            2,
            self.stack_pointer[-(2 * self.oparg - 1)],
            2,
            self.oparg,
        )
        if map is None:
            raise Interpreter.error
        while True:
            self.oparg -= 1
            if not self.oparg:
                break
            "decref"
            "decref"
        PUSH(map)
        DISPATCH()

    def SETUP_ANNOTATIONS(self):
        err: int
        ann_dict: PyObject
        if LOCALS() is None:
            _PyErr_Format(
                self.tstate,
                PyExc_SystemError,
                "no locals found when setting up annotations",
            )
            if True:
                raise Interpreter.error
        if PyDict_CheckExact(LOCALS()):
            ann_dict = _PyDict_GetItemWithError(LOCALS(), id(__annotations__))
            if ann_dict is None:
                if _PyErr_Occurred(self.tstate):
                    raise Interpreter.error
                ann_dict = dict()
                if ann_dict is None:
                    raise Interpreter.error
                err = PyDict_SetItem(LOCALS(), id(__annotations__), ann_dict)
                if err:
                    raise Interpreter.error
        else:
            ann_dict = LOCALS()[id(__annotations__)]
            if ann_dict is None:
                if not _PyErr_ExceptionMatches(self.tstate, PyExc_KeyError):
                    raise Interpreter.error
                _PyErr_Clear(self.tstate)
                ann_dict = dict()
                if ann_dict is None:
                    raise Interpreter.error
                err = PyObject_SetItem(LOCALS(), id(__annotations__), ann_dict)
                if err:
                    raise Interpreter.error
        DISPATCH()

    def BUILD_CONST_KEY_MAP(self):
        map: PyObject
        keys: PyObject = TOP()
        if not PyTuple_CheckExact(keys) or len(keys) != self.oparg:
            _PyErr_SetString(
                self.tstate, PyExc_SystemError, "bad BUILD_CONST_KEY_MAP keys argument"
            )
            raise Interpreter.error
        map = _PyDict_FromItems(
            keys[0], 1, self.stack_pointer[-(self.oparg + 1)], 1, self.oparg
        )
        if map is None:
            raise Interpreter.error
        while True:
            self.oparg -= 1
            if not self.oparg:
                break
            "decref"
        PUSH(map)
        DISPATCH()

    def DICT_UPDATE(self):
        update: PyObject = self.stack_pointer[-1]
        dict: PyObject = self.stack_pointer[-(self.oparg + 1)]
        if PyDict_Update(dict, update) < 0:
            if _PyErr_ExceptionMatches(self.tstate, PyExc_AttributeError):
                _PyErr_Format(
                    self.tstate,
                    PyExc_TypeError,
                    "'%.200s' object is not a mapping",
                    type(update).tp_name,
                )
            if True:
                raise Interpreter.pop_1_error
        STACK_SHRINK(1)
        DISPATCH()

    def DICT_MERGE(self):
        update: PyObject = self.stack_pointer[-1]
        dict: PyObject = self.stack_pointer[-(self.oparg + 1)]
        if _PyDict_MergeEx(dict, update, 2) < 0:
            format_kwargs_error(
                self.tstate, self.stack_pointer[-(3 + self.oparg)], update
            )
            if True:
                raise Interpreter.pop_1_error
        STACK_SHRINK(1)
        DISPATCH()

    def MAP_ADD(self):
        value: PyObject = self.stack_pointer[-1]
        key: PyObject = self.stack_pointer[-2]
        dict: PyObject = self.stack_pointer[-(self.oparg + 2)]
        assert PyDict_CheckExact(dict)
        if _PyDict_SetItem_Take2(dict, key, value) != 0:
            raise Interpreter.pop_2_error
        STACK_SHRINK(2)
        DISPATCH()

    def LOAD_ATTR(self):
        cache: _PyAttrCache = self.next_instr
        if ADAPTIVE_COUNTER_IS_ZERO(cache.counter):
            assert self.cframe.use_tracing == 0
            owner: PyObject = TOP()
            name: PyObject = self.names[self.oparg >> 1]
            post_decr(self.next_instr)
            _Py_Specialize_LoadAttr(owner, self.next_instr, name)
            DISPATCH_SAME_OPARG()
        DECREMENT_ADAPTIVE_COUNTER(cache.counter)
        name: PyObject = self.names[self.oparg >> 1]
        owner: PyObject = TOP()
        if self.oparg & 1:
            meth: PyObject = None
            meth_found: int = _PyObject_GetMethod(owner, name, meth)
            if meth is None:
                raise Interpreter.error
            if meth_found:
                self.stack_pointer[-1] = meth
                PUSH(owner)
            else:
                self.stack_pointer[-1] = None
                PUSH(meth)
        else:
            res: PyObject = owner[name]
            if res is None:
                raise Interpreter.error
            self.stack_pointer[-1] = res
        JUMPBY(INLINE_CACHE_ENTRIES_LOAD_ATTR)
        DISPATCH()

    def LOAD_ATTR_INSTANCE_VALUE(self):
        assert self.cframe.use_tracing == 0
        owner: PyObject = TOP()
        res: PyObject
        tp: PyTypeObject = type(owner)
        cache: _PyAttrCache = self.next_instr
        type_version: int = read_u32(cache.version)
        assert type_version != 0
        DEOPT_IF(tp.tp_version_tag != type_version, LOAD_ATTR)
        assert tp.tp_dictoffset < 0
        assert tp.tp_flags & Py_TPFLAGS_MANAGED_DICT
        dorv: PyDictOrValues = _PyObject_DictOrValuesPointer(owner)
        DEOPT_IF(not _PyDictOrValues_IsValues(dorv), LOAD_ATTR)
        res = _PyDictOrValues_GetValues(dorv).values[cache.index]
        DEOPT_IF(res is None, LOAD_ATTR)
        self.stack_pointer[-1] = None
        STACK_GROW(self.oparg & 1)
        self.stack_pointer[-1] = res
        JUMPBY(INLINE_CACHE_ENTRIES_LOAD_ATTR)
        DISPATCH()

    def LOAD_ATTR_MODULE(self):
        assert self.cframe.use_tracing == 0
        owner: PyObject = TOP()
        res: PyObject
        cache: _PyAttrCache = self.next_instr
        DEOPT_IF(not PyModule_CheckExact(owner), LOAD_ATTR)
        dict: PyDictObject = owner.md_dict
        assert dict is None
        DEOPT_IF(dict.ma_keys.dk_version != read_u32(cache.version), LOAD_ATTR)
        assert dict.ma_keys.dk_kind == DICT_KEYS_UNICODE
        assert cache.index < dict.ma_keys.dk_nentries
        ep: PyDictUnicodeEntry = DK_UNICODE_ENTRIES(dict.ma_keys) + cache.index
        res = ep.me_value
        DEOPT_IF(res is None, LOAD_ATTR)
        self.stack_pointer[-1] = None
        STACK_GROW(self.oparg & 1)
        self.stack_pointer[-1] = res
        JUMPBY(INLINE_CACHE_ENTRIES_LOAD_ATTR)
        DISPATCH()

    def LOAD_ATTR_WITH_HINT(self):
        assert self.cframe.use_tracing == 0
        owner: PyObject = TOP()
        res: PyObject
        tp: PyTypeObject = type(owner)
        cache: _PyAttrCache = self.next_instr
        type_version: int = read_u32(cache.version)
        assert type_version != 0
        DEOPT_IF(tp.tp_version_tag != type_version, LOAD_ATTR)
        assert tp.tp_flags & Py_TPFLAGS_MANAGED_DICT
        dorv: PyDictOrValues = _PyObject_DictOrValuesPointer(owner)
        DEOPT_IF(_PyDictOrValues_IsValues(dorv), LOAD_ATTR)
        dict: PyDictObject = _PyDictOrValues_GetDict(dorv)
        DEOPT_IF(dict is None, LOAD_ATTR)
        assert PyDict_CheckExact(dict)
        name: PyObject = self.names[self.oparg >> 1]
        hint: int = cache.index
        DEOPT_IF(hint >= dict.ma_keys.dk_nentries, LOAD_ATTR)
        if DK_IS_UNICODE(dict.ma_keys):
            ep: PyDictUnicodeEntry = DK_UNICODE_ENTRIES(dict.ma_keys) + hint
            DEOPT_IF(ep.me_key != name, LOAD_ATTR)
            res = ep.me_value
        else:
            ep: PyDictKeyEntry = DK_ENTRIES(dict.ma_keys) + hint
            DEOPT_IF(ep.me_key != name, LOAD_ATTR)
            res = ep.me_value
        DEOPT_IF(res is None, LOAD_ATTR)
        self.stack_pointer[-1] = None
        STACK_GROW(self.oparg & 1)
        self.stack_pointer[-1] = res
        JUMPBY(INLINE_CACHE_ENTRIES_LOAD_ATTR)
        DISPATCH()

    def LOAD_ATTR_SLOT(self):
        assert self.cframe.use_tracing == 0
        owner: PyObject = TOP()
        res: PyObject
        tp: PyTypeObject = type(owner)
        cache: _PyAttrCache = self.next_instr
        type_version: int = read_u32(cache.version)
        assert type_version != 0
        DEOPT_IF(tp.tp_version_tag != type_version, LOAD_ATTR)
        addr: str = owner + cache.index
        res = addr
        DEOPT_IF(res is None, LOAD_ATTR)
        self.stack_pointer[-1] = None
        STACK_GROW(self.oparg & 1)
        self.stack_pointer[-1] = res
        JUMPBY(INLINE_CACHE_ENTRIES_LOAD_ATTR)
        DISPATCH()

    def LOAD_ATTR_CLASS(self):
        assert self.cframe.use_tracing == 0
        cache: _PyLoadMethodCache = self.next_instr
        cls: PyObject = TOP()
        DEOPT_IF(not PyType_Check(cls), LOAD_ATTR)
        type_version: int = read_u32(cache.type_version)
        DEOPT_IF(cls.tp_version_tag != type_version, LOAD_ATTR)
        assert type_version != 0
        res: PyObject = read_obj(cache.descr)
        assert res is None
        self.stack_pointer[-1] = None
        STACK_GROW(self.oparg & 1)
        self.stack_pointer[-1] = res
        JUMPBY(INLINE_CACHE_ENTRIES_LOAD_ATTR)
        DISPATCH()

    def LOAD_ATTR_PROPERTY(self):
        assert self.cframe.use_tracing == 0
        DEOPT_IF(self.tstate.interp.eval_frame, LOAD_ATTR)
        cache: _PyLoadMethodCache = self.next_instr
        owner: PyObject = TOP()
        cls: PyTypeObject = type(owner)
        type_version: int = read_u32(cache.type_version)
        DEOPT_IF(cls.tp_version_tag != type_version, LOAD_ATTR)
        assert type_version != 0
        fget: PyObject = read_obj(cache.descr)
        assert Py_IS_TYPE(fget, PyFunction_Type)
        f: PyFunctionObject = fget
        func_version: int = read_u32(cache.keys_version)
        assert func_version != 0
        DEOPT_IF(f.func_version != func_version, LOAD_ATTR)
        code: PyCodeObject = f.func_code
        assert code.co_argcount == 1
        DEOPT_IF(
            not _PyThreadState_HasStackSpace(self.tstate, code.co_framesize), LOAD_ATTR
        )
        new_frame: _PyInterpreterFrame = _PyFrame_PushUnchecked(self.tstate, f)
        self.stack_pointer[-1] = None
        shrink_stack: int = not self.oparg & 1
        STACK_SHRINK(shrink_stack)
        new_frame.localsplus[0] = owner
        for i in range(1, code.co_nlocalsplus):
            new_frame.localsplus[i] = None
        JUMPBY(INLINE_CACHE_ENTRIES_LOAD_ATTR)
        DISPATCH_INLINED(new_frame)

    def LOAD_ATTR_GETATTRIBUTE_OVERRIDDEN(self):
        assert self.cframe.use_tracing == 0
        DEOPT_IF(self.tstate.interp.eval_frame, LOAD_ATTR)
        cache: _PyLoadMethodCache = self.next_instr
        owner: PyObject = TOP()
        cls: PyTypeObject = type(owner)
        type_version: int = read_u32(cache.type_version)
        DEOPT_IF(cls.tp_version_tag != type_version, LOAD_ATTR)
        assert type_version != 0
        getattribute: PyObject = read_obj(cache.descr)
        assert Py_IS_TYPE(getattribute, PyFunction_Type)
        f: PyFunctionObject = getattribute
        func_version: int = read_u32(cache.keys_version)
        assert func_version != 0
        DEOPT_IF(f.func_version != func_version, LOAD_ATTR)
        code: PyCodeObject = f.func_code
        assert code.co_argcount == 2
        DEOPT_IF(
            not _PyThreadState_HasStackSpace(self.tstate, code.co_framesize), LOAD_ATTR
        )
        name: PyObject = self.names[self.oparg >> 1]
        new_frame: _PyInterpreterFrame = _PyFrame_PushUnchecked(self.tstate, f)
        self.stack_pointer[-1] = None
        shrink_stack: int = not self.oparg & 1
        STACK_SHRINK(shrink_stack)
        new_frame.localsplus[0] = owner
        new_frame.localsplus[1] = Py_NewRef(name)
        for i in range(2, code.co_nlocalsplus):
            new_frame.localsplus[i] = None
        JUMPBY(INLINE_CACHE_ENTRIES_LOAD_ATTR)
        DISPATCH_INLINED(new_frame)

    def STORE_ATTR_INSTANCE_VALUE(self):
        owner: PyObject = self.stack_pointer[-1]
        value: PyObject = self.stack_pointer[-2]
        type_version: int = read_u32(self.next_instr[1].cache)
        index: int = read_u16(self.next_instr[3].cache)
        assert self.cframe.use_tracing == 0
        tp: PyTypeObject = type(owner)
        assert type_version != 0
        DEOPT_IF(tp.tp_version_tag != type_version, STORE_ATTR)
        assert tp.tp_flags & Py_TPFLAGS_MANAGED_DICT
        dorv: PyDictOrValues = _PyObject_DictOrValuesPointer(owner)
        DEOPT_IF(not _PyDictOrValues_IsValues(dorv), STORE_ATTR)
        values: PyDictValues = _PyDictOrValues_GetValues(dorv)
        old_value: PyObject = values.values[index]
        values.values[index] = value
        if old_value is None:
            _PyDictValues_AddToInsertionOrder(values, index)
        STACK_SHRINK(2)
        JUMPBY(4)
        DISPATCH()

    def STORE_ATTR_WITH_HINT(self):
        owner: PyObject = self.stack_pointer[-1]
        value: PyObject = self.stack_pointer[-2]
        type_version: int = read_u32(self.next_instr[1].cache)
        hint: int = read_u16(self.next_instr[3].cache)
        assert self.cframe.use_tracing == 0
        tp: PyTypeObject = type(owner)
        assert type_version != 0
        DEOPT_IF(tp.tp_version_tag != type_version, STORE_ATTR)
        assert tp.tp_flags & Py_TPFLAGS_MANAGED_DICT
        dorv: PyDictOrValues = _PyObject_DictOrValuesPointer(owner)
        DEOPT_IF(_PyDictOrValues_IsValues(dorv), STORE_ATTR)
        dict: PyDictObject = _PyDictOrValues_GetDict(dorv)
        DEOPT_IF(dict is None, STORE_ATTR)
        assert PyDict_CheckExact(dict)
        name: PyObject = self.names[self.oparg]
        DEOPT_IF(hint >= dict.ma_keys.dk_nentries, STORE_ATTR)
        old_value: PyObject
        new_version: int
        if DK_IS_UNICODE(dict.ma_keys):
            ep: PyDictUnicodeEntry = DK_UNICODE_ENTRIES(dict.ma_keys) + hint
            DEOPT_IF(ep.me_key != name, STORE_ATTR)
            old_value = ep.me_value
            DEOPT_IF(old_value is None, STORE_ATTR)
            new_version = _PyDict_NotifyEvent(PyDict_EVENT_MODIFIED, dict, name, value)
            ep.me_value = value
        else:
            ep: PyDictKeyEntry = DK_ENTRIES(dict.ma_keys) + hint
            DEOPT_IF(ep.me_key != name, STORE_ATTR)
            old_value = ep.me_value
            DEOPT_IF(old_value is None, STORE_ATTR)
            new_version = _PyDict_NotifyEvent(PyDict_EVENT_MODIFIED, dict, name, value)
            ep.me_value = value
        if not _PyObject_GC_IS_TRACKED(dict) and _PyObject_GC_MAY_BE_TRACKED(value):
            _PyObject_GC_TRACK(dict)
        dict.ma_version_tag = new_version
        STACK_SHRINK(2)
        JUMPBY(4)
        DISPATCH()

    def STORE_ATTR_SLOT(self):
        owner: PyObject = self.stack_pointer[-1]
        value: PyObject = self.stack_pointer[-2]
        type_version: int = read_u32(self.next_instr[1].cache)
        index: int = read_u16(self.next_instr[3].cache)
        assert self.cframe.use_tracing == 0
        tp: PyTypeObject = type(owner)
        assert type_version != 0
        DEOPT_IF(tp.tp_version_tag != type_version, STORE_ATTR)
        addr: str = owner + index
        old_value: PyObject = addr
        addr = value
        STACK_SHRINK(2)
        JUMPBY(4)
        DISPATCH()

    def COMPARE_OP(self):
        right: PyObject = self.stack_pointer[-1]
        left: PyObject = self.stack_pointer[-2]
        res: PyObject
        cache: _PyCompareOpCache = self.next_instr
        if ADAPTIVE_COUNTER_IS_ZERO(cache.counter):
            assert self.cframe.use_tracing == 0
            post_decr(self.next_instr)
            _Py_Specialize_CompareOp(left, right, self.next_instr, self.oparg)
            DISPATCH_SAME_OPARG()
        DECREMENT_ADAPTIVE_COUNTER(cache.counter)
        assert self.oparg <= Py_GE
        res = PyObject_RichCompare(left, right, self.oparg)
        if res is None:
            raise Interpreter.pop_2_error
        STACK_SHRINK(1)
        self.stack_pointer[-1] = res
        JUMPBY(2)
        DISPATCH()

    def COMPARE_OP_FLOAT_JUMP(self):
        _tmp_1: PyObject = self.stack_pointer[-1]
        _tmp_2: PyObject = self.stack_pointer[-2]
        right: PyObject = _tmp_1
        left: PyObject = _tmp_2
        jump: int
        when_to_jump_mask: int = read_u16(self.next_instr[1].cache)
        assert self.cframe.use_tracing == 0
        DEOPT_IF(not PyFloat_CheckExact(left), COMPARE_OP)
        DEOPT_IF(not PyFloat_CheckExact(right), COMPARE_OP)
        dleft: float = left
        dright: float = right
        sign_ish: int = 1 << 2 * (dleft >= dright) + (dleft <= dright)
        jump = sign_ish & when_to_jump_mask
        _tmp_2 = jump
        JUMPBY(2)
        NEXTOPARG()
        JUMPBY(1)
        jump: int = _tmp_2
        assert self.opcode == POP_JUMP_IF_FALSE or self.opcode == POP_JUMP_IF_TRUE
        if jump:
            JUMPBY(self.oparg)
        STACK_SHRINK(2)
        DISPATCH()

    def COMPARE_OP_INT_JUMP(self):
        _tmp_1: PyObject = self.stack_pointer[-1]
        _tmp_2: PyObject = self.stack_pointer[-2]
        right: PyObject = _tmp_1
        left: PyObject = _tmp_2
        jump: int
        when_to_jump_mask: int = read_u16(self.next_instr[1].cache)
        assert self.cframe.use_tracing == 0
        DEOPT_IF(not PyLong_CheckExact(left), COMPARE_OP)
        DEOPT_IF(not PyLong_CheckExact(right), COMPARE_OP)
        DEOPT_IF(Py_SIZE(left) + 1 > 2, COMPARE_OP)
        DEOPT_IF(Py_SIZE(right) + 1 > 2, COMPARE_OP)
        assert abs(Py_SIZE(left)) <= 1 and abs(Py_SIZE(right)) <= 1
        ileft: Py_ssize_t = Py_SIZE(left) * left.ob_digit[0]
        iright: Py_ssize_t = Py_SIZE(right) * right.ob_digit[0]
        sign_ish: int = 1 << 2 * (ileft >= iright) + (ileft <= iright)
        jump = sign_ish & when_to_jump_mask
        _tmp_2 = jump
        JUMPBY(2)
        NEXTOPARG()
        JUMPBY(1)
        jump: int = _tmp_2
        assert self.opcode == POP_JUMP_IF_FALSE or self.opcode == POP_JUMP_IF_TRUE
        if jump:
            JUMPBY(self.oparg)
        STACK_SHRINK(2)
        DISPATCH()

    def COMPARE_OP_STR_JUMP(self):
        _tmp_1: PyObject = self.stack_pointer[-1]
        _tmp_2: PyObject = self.stack_pointer[-2]
        right: PyObject = _tmp_1
        left: PyObject = _tmp_2
        jump: int
        invert: int = read_u16(self.next_instr[1].cache)
        assert self.cframe.use_tracing == 0
        DEOPT_IF(not PyUnicode_CheckExact(left), COMPARE_OP)
        DEOPT_IF(not PyUnicode_CheckExact(right), COMPARE_OP)
        res: int = left == right
        assert self.oparg == Py_EQ or self.oparg == Py_NE
        assert res == 0 or res == 1
        assert invert == 0 or invert == 1
        jump = res ^ invert
        _tmp_2 = jump
        JUMPBY(2)
        NEXTOPARG()
        JUMPBY(1)
        jump: int = _tmp_2
        assert self.opcode == POP_JUMP_IF_FALSE or self.opcode == POP_JUMP_IF_TRUE
        if jump:
            JUMPBY(self.oparg)
        STACK_SHRINK(2)
        DISPATCH()

    def IS_OP(self):
        right: PyObject = self.stack_pointer[-1]
        left: PyObject = self.stack_pointer[-2]
        b: PyObject
        res: int = Py_Is(left, right) ^ self.oparg
        b = Py_NewRef(res if True else False)
        STACK_SHRINK(1)
        self.stack_pointer[-1] = b
        DISPATCH()

    def CONTAINS_OP(self):
        right: PyObject = self.stack_pointer[-1]
        left: PyObject = self.stack_pointer[-2]
        b: PyObject
        res: int = PySequence_Contains(right, left)
        if res < 0:
            raise Interpreter.pop_2_error
        b = Py_NewRef(res ^ self.oparg if True else False)
        STACK_SHRINK(1)
        self.stack_pointer[-1] = b
        DISPATCH()

    def CHECK_EG_MATCH(self):
        match_type: PyObject = POP()
        if check_except_star_type_valid(self.tstate, match_type) < 0:
            raise Interpreter.error
        exc_value: PyObject = TOP()
        match: PyObject = None
        rest: PyObject = None
        res: int = exception_group_match(exc_value, match_type, match, rest)
        if res < 0:
            raise Interpreter.error
        if match is None or rest is None:
            assert match is None
            assert rest is None
            raise Interpreter.error
        if Py_IsNone(match):
            PUSH(match)
        else:
            self.stack_pointer[-1] = rest
            PUSH(match)
            PyErr_SetExcInfo(None, Py_NewRef(match), None)
        DISPATCH()

    def CHECK_EXC_MATCH(self):
        right: PyObject = self.stack_pointer[-1]
        left: PyObject = self.stack_pointer[-2]
        b: PyObject
        assert PyExceptionInstance_Check(left)
        if check_except_type_valid(self.tstate, right) < 0:
            if True:
                raise Interpreter.pop_1_error
        res: int = PyErr_GivenExceptionMatches(left, right)
        b = Py_NewRef(res if True else False)
        self.stack_pointer[-1] = b
        DISPATCH()

    def IMPORT_NAME(self):
        fromlist: PyObject = self.stack_pointer[-1]
        level: PyObject = self.stack_pointer[-2]
        res: PyObject
        name: PyObject = self.names[self.oparg]
        res = import_name(self.tstate, self.frame, name, fromlist, level)
        if res is None:
            raise Interpreter.pop_2_error
        STACK_SHRINK(1)
        self.stack_pointer[-1] = res
        DISPATCH()

    def IMPORT_STAR(self):
        from_: PyObject = self.stack_pointer[-1]
        locals: PyObject
        err: int
        if _PyFrame_FastToLocalsWithError(self.frame) < 0:
            if True:
                raise Interpreter.pop_1_error
        locals = LOCALS()
        if locals is None:
            _PyErr_SetString(
                self.tstate, PyExc_SystemError, "no locals found during 'import *'"
            )
            if True:
                raise Interpreter.pop_1_error
        err = import_all_from(self.tstate, locals, from_)
        _PyFrame_LocalsToFast(self.frame, 0)
        if err:
            raise Interpreter.pop_1_error
        STACK_SHRINK(1)
        DISPATCH()

    def IMPORT_FROM(self):
        from_: PyObject = self.stack_pointer[-1]
        res: PyObject
        name: PyObject = self.names[self.oparg]
        res = import_from(self.tstate, from_, name)
        if res is None:
            raise Interpreter.error
        STACK_GROW(1)
        self.stack_pointer[-1] = res
        DISPATCH()

    def JUMP_FORWARD(self):
        JUMPBY(self.oparg)
        DISPATCH()

    def JUMP_BACKWARD(self):
        assert self.oparg < INSTR_OFFSET()
        JUMPBY(-self.oparg)
        CHECK_EVAL_BREAKER()
        DISPATCH()

    def POP_JUMP_IF_FALSE(self):
        cond: PyObject = POP()
        if Py_IsTrue(cond):
            _Py_DECREF_NO_DEALLOC(cond)
        elif Py_IsFalse(cond):
            _Py_DECREF_NO_DEALLOC(cond)
            JUMPBY(self.oparg)
        else:
            err: int = PyObject_IsTrue(cond)
            if err > 0:
                pass
            elif err == 0:
                JUMPBY(self.oparg)
            else:
                raise Interpreter.error
        DISPATCH()

    def POP_JUMP_IF_TRUE(self):
        cond: PyObject = POP()
        if Py_IsFalse(cond):
            _Py_DECREF_NO_DEALLOC(cond)
        elif Py_IsTrue(cond):
            _Py_DECREF_NO_DEALLOC(cond)
            JUMPBY(self.oparg)
        else:
            err: int = PyObject_IsTrue(cond)
            if err > 0:
                JUMPBY(self.oparg)
            elif err == 0:
                pass
            else:
                raise Interpreter.error
        DISPATCH()

    def POP_JUMP_IF_NOT_NONE(self):
        value: PyObject = POP()
        if not Py_IsNone(value):
            JUMPBY(self.oparg)
        DISPATCH()

    def POP_JUMP_IF_NONE(self):
        value: PyObject = POP()
        if Py_IsNone(value):
            _Py_DECREF_NO_DEALLOC(value)
            JUMPBY(self.oparg)
        DISPATCH()

    def JUMP_IF_FALSE_OR_POP(self):
        cond: PyObject = TOP()
        err: int
        if Py_IsTrue(cond):
            STACK_SHRINK(1)
            _Py_DECREF_NO_DEALLOC(cond)
        elif Py_IsFalse(cond):
            JUMPBY(self.oparg)
        else:
            err = PyObject_IsTrue(cond)
            if err > 0:
                STACK_SHRINK(1)
            elif err == 0:
                JUMPBY(self.oparg)
            else:
                raise Interpreter.error
        DISPATCH()

    def JUMP_IF_TRUE_OR_POP(self):
        cond: PyObject = TOP()
        err: int
        if Py_IsFalse(cond):
            STACK_SHRINK(1)
            _Py_DECREF_NO_DEALLOC(cond)
        elif Py_IsTrue(cond):
            JUMPBY(self.oparg)
        else:
            err = PyObject_IsTrue(cond)
            if err > 0:
                JUMPBY(self.oparg)
            elif err == 0:
                STACK_SHRINK(1)
            else:
                raise Interpreter.error
        DISPATCH()

    def JUMP_BACKWARD_NO_INTERRUPT(self):
        JUMPBY(-self.oparg)
        DISPATCH()

    def GET_LEN(self):
        len_i: Py_ssize_t = len(TOP())
        if len_i < 0:
            raise Interpreter.error
        len_o: PyObject = len_i
        if len_o is None:
            raise Interpreter.error
        PUSH(len_o)
        DISPATCH()

    def MATCH_CLASS(self):
        self.names: PyObject = POP()
        type: PyObject = POP()
        subject: PyObject = TOP()
        assert PyTuple_CheckExact(self.names)
        attrs: PyObject = match_class(
            self.tstate, subject, type, self.oparg, self.names
        )
        if attrs:
            assert PyTuple_CheckExact(attrs)
            self.stack_pointer[-1] = attrs
        elif _PyErr_Occurred(self.tstate):
            raise Interpreter.error
        else:
            self.stack_pointer[-1] = Py_NewRef(None)
        DISPATCH()

    def MATCH_MAPPING(self):
        subject: PyObject = TOP()
        match: int = type(subject).tp_flags & Py_TPFLAGS_MAPPING
        res: PyObject = match if True else False
        PUSH(Py_NewRef(res))
        DISPATCH()

    def MATCH_SEQUENCE(self):
        subject: PyObject = TOP()
        match: int = type(subject).tp_flags & Py_TPFLAGS_SEQUENCE
        res: PyObject = match if True else False
        PUSH(Py_NewRef(res))
        DISPATCH()

    def MATCH_KEYS(self):
        keys: PyObject = TOP()
        subject: PyObject = SECOND()
        values_or_none: PyObject = match_keys(self.tstate, subject, keys)
        if values_or_none is None:
            raise Interpreter.error
        PUSH(values_or_none)
        DISPATCH()

    def GET_ITER(self):
        iterable: PyObject = TOP()
        iter: PyObject = iter(iterable)
        self.stack_pointer[-1] = iter
        if iter is None:
            raise Interpreter.error
        DISPATCH()

    def GET_YIELD_FROM_ITER(self):
        iterable: PyObject = TOP()
        iter: PyObject
        if PyCoro_CheckExact(iterable):
            if not self.frame.f_code.co_flags & (CO_COROUTINE | CO_ITERABLE_COROUTINE):
                self.stack_pointer[-1] = None
                _PyErr_SetString(
                    self.tstate,
                    PyExc_TypeError,
                    "cannot 'yield from' a coroutine object in a non-coroutine generator",
                )
                raise Interpreter.error
        elif not PyGen_CheckExact(iterable):
            iter = iter(iterable)
            self.stack_pointer[-1] = iter
            if iter is None:
                raise Interpreter.error
        DISPATCH()

    def FOR_ITER(self):
        cache: _PyForIterCache = self.next_instr
        if ADAPTIVE_COUNTER_IS_ZERO(cache.counter):
            assert self.cframe.use_tracing == 0
            post_decr(self.next_instr)
            _Py_Specialize_ForIter(TOP(), self.next_instr, self.oparg)
            DISPATCH_SAME_OPARG()
        DECREMENT_ADAPTIVE_COUNTER(cache.counter)
        iter: PyObject = TOP()
        next: PyObject = type(iter).tp_iternext(iter)
        if next is None:
            PUSH(next)
            JUMPBY(INLINE_CACHE_ENTRIES_FOR_ITER)
        else:
            if _PyErr_Occurred(self.tstate):
                if not _PyErr_ExceptionMatches(self.tstate, PyExc_StopIteration):
                    raise Interpreter.error
                elif self.tstate.c_tracefunc is None:
                    call_exc_trace(
                        self.tstate.c_tracefunc,
                        self.tstate.c_traceobj,
                        self.tstate,
                        self.frame,
                    )
                _PyErr_Clear(self.tstate)
            assert (
                _Py_OPCODE(self.next_instr[INLINE_CACHE_ENTRIES_FOR_ITER + self.oparg])
                == END_FOR
            )
            STACK_SHRINK(1)
            JUMPBY(INLINE_CACHE_ENTRIES_FOR_ITER + self.oparg + 1)
        DISPATCH()

    def FOR_ITER_LIST(self):
        assert self.cframe.use_tracing == 0
        it: _PyListIterObject = TOP()
        DEOPT_IF(type(it) != PyListIter_Type, FOR_ITER)
        seq: PyListObject = it.it_seq
        if seq:
            if it.it_index < len(seq):
                next: PyObject = seq[post_incr(it.it_index)]
                PUSH(Py_NewRef(next))
                JUMPBY(INLINE_CACHE_ENTRIES_FOR_ITER)
                raise Interpreter.end_for_iter_list
            it.it_seq = None
        STACK_SHRINK(1)
        JUMPBY(INLINE_CACHE_ENTRIES_FOR_ITER + self.oparg + 1)

        class end_for_iter_list(Exception):
            DISPATCH()

    def FOR_ITER_TUPLE(self):
        assert self.cframe.use_tracing == 0
        it: _PyTupleIterObject = TOP()
        DEOPT_IF(type(it) != PyTupleIter_Type, FOR_ITER)
        seq: PyTupleObject = it.it_seq
        if seq:
            if it.it_index < len(seq):
                next: PyObject = seq[post_incr(it.it_index)]
                PUSH(Py_NewRef(next))
                JUMPBY(INLINE_CACHE_ENTRIES_FOR_ITER)
                raise Interpreter.end_for_iter_tuple
            it.it_seq = None
        STACK_SHRINK(1)
        JUMPBY(INLINE_CACHE_ENTRIES_FOR_ITER + self.oparg + 1)

        class end_for_iter_tuple(Exception):
            DISPATCH()

    def FOR_ITER_RANGE(self):
        assert self.cframe.use_tracing == 0
        r: _PyRangeIterObject = TOP()
        DEOPT_IF(type(r) != PyRangeIter_Type, FOR_ITER)
        next: _Py_CODEUNIT = self.next_instr[INLINE_CACHE_ENTRIES_FOR_ITER]
        assert _PyOpcode_Deopt[_Py_OPCODE(next)] == STORE_FAST
        if r.len <= 0:
            STACK_SHRINK(1)
            JUMPBY(INLINE_CACHE_ENTRIES_FOR_ITER + self.oparg + 1)
        else:
            value: int = r.start
            r.start = value + r.step
            post_decr(r.len)
            if _PyLong_AssignValue(GETLOCAL(_Py_OPARG(next)), value) < 0:
                raise Interpreter.error
            JUMPBY(INLINE_CACHE_ENTRIES_FOR_ITER + 1)
        DISPATCH()

    def FOR_ITER_GEN(self):
        assert self.cframe.use_tracing == 0
        gen: PyGenObject = TOP()
        DEOPT_IF(type(gen) != PyGen_Type, FOR_ITER)
        DEOPT_IF(gen.gi_frame_state >= FRAME_EXECUTING, FOR_ITER)
        gen_frame: _PyInterpreterFrame = gen.gi_iframe
        self.frame.yield_offset = self.oparg
        _PyFrame_StackPush(gen_frame, Py_NewRef(None))
        gen.gi_frame_state = FRAME_EXECUTING
        gen.gi_exc_state.previous_item = self.tstate.exc_info
        self.tstate.exc_info = gen.gi_exc_state
        JUMPBY(INLINE_CACHE_ENTRIES_FOR_ITER + self.oparg)
        assert _Py_OPCODE(self.next_instr) == END_FOR
        DISPATCH_INLINED(gen_frame)

    def BEFORE_ASYNC_WITH(self):
        mgr: PyObject = TOP()
        res: PyObject
        enter: PyObject = _PyObject_LookupSpecial(mgr, id(__aenter__))
        if enter is None:
            if not _PyErr_Occurred(self.tstate):
                _PyErr_Format(
                    self.tstate,
                    PyExc_TypeError,
                    "'%.200s' object does not support the asynchronous context manager protocol",
                    type(mgr).tp_name,
                )
            raise Interpreter.error
        exit: PyObject = _PyObject_LookupSpecial(mgr, id(__aexit__))
        if exit is None:
            if not _PyErr_Occurred(self.tstate):
                _PyErr_Format(
                    self.tstate,
                    PyExc_TypeError,
                    "'%.200s' object does not support the asynchronous context manager protocol (missed __aexit__ method)",
                    type(mgr).tp_name,
                )
            raise Interpreter.error
        self.stack_pointer[-1] = exit
        res = _PyObject_CallNoArgs(enter)
        if res is None:
            raise Interpreter.error
        PUSH(res)
        DISPATCH()

    def BEFORE_WITH(self):
        mgr: PyObject = TOP()
        res: PyObject
        enter: PyObject = _PyObject_LookupSpecial(mgr, id(__enter__))
        if enter is None:
            if not _PyErr_Occurred(self.tstate):
                _PyErr_Format(
                    self.tstate,
                    PyExc_TypeError,
                    "'%.200s' object does not support the context manager protocol",
                    type(mgr).tp_name,
                )
            raise Interpreter.error
        exit: PyObject = _PyObject_LookupSpecial(mgr, id(__exit__))
        if exit is None:
            if not _PyErr_Occurred(self.tstate):
                _PyErr_Format(
                    self.tstate,
                    PyExc_TypeError,
                    "'%.200s' object does not support the context manager protocol (missed __exit__ method)",
                    type(mgr).tp_name,
                )
            raise Interpreter.error
        self.stack_pointer[-1] = exit
        res = _PyObject_CallNoArgs(enter)
        if res is None:
            raise Interpreter.error
        PUSH(res)
        DISPATCH()

    def WITH_EXCEPT_START(self):
        val: PyObject = self.stack_pointer[-1]
        lasti: PyObject = self.stack_pointer[-3]
        exit_func: PyObject = self.stack_pointer[-4]
        res: PyObject
        exc: PyObject
        tb: PyObject
        assert val and PyExceptionInstance_Check(val)
        exc = PyExceptionInstance_Class(val)
        tb = PyException_GetTraceback(val)
        assert PyLong_Check(lasti)
        lasti
        stack: List[PyObject] = [None, exc, val, tb]
        res = PyObject_Vectorcall(exit_func, stack + 1, 3 | 1, None)
        if res is None:
            raise Interpreter.error
        STACK_GROW(1)
        self.stack_pointer[-1] = res
        DISPATCH()

    def PUSH_EXC_INFO(self):
        value: PyObject = TOP()
        exc_info: _PyErr_StackItem = self.tstate.exc_info
        if exc_info.exc_value is None:
            self.stack_pointer[-1] = exc_info.exc_value
        else:
            self.stack_pointer[-1] = Py_NewRef(None)
        PUSH(Py_NewRef(value))
        assert PyExceptionInstance_Check(value)
        exc_info.exc_value = value
        DISPATCH()

    def LOAD_ATTR_METHOD_WITH_VALUES(self):
        assert self.cframe.use_tracing == 0
        self_: PyObject = TOP()
        self_cls: PyTypeObject = type(self_)
        cache: _PyLoadMethodCache = self.next_instr
        type_version: int = read_u32(cache.type_version)
        assert type_version != 0
        DEOPT_IF(self_cls.tp_version_tag != type_version, LOAD_ATTR)
        assert self_cls.tp_flags & Py_TPFLAGS_MANAGED_DICT
        dorv: PyDictOrValues = _PyObject_DictOrValuesPointer(self_)
        DEOPT_IF(not _PyDictOrValues_IsValues(dorv), LOAD_ATTR)
        self_heap_type: PyHeapTypeObject = self_cls
        DEOPT_IF(
            self_heap_type.ht_cached_keys.dk_version != read_u32(cache.keys_version),
            LOAD_ATTR,
        )
        res: PyObject = read_obj(cache.descr)
        assert res is None
        assert _PyType_HasFeature(type(res), Py_TPFLAGS_METHOD_DESCRIPTOR)
        self.stack_pointer[-1] = Py_NewRef(res)
        PUSH(self_)
        JUMPBY(INLINE_CACHE_ENTRIES_LOAD_ATTR)
        DISPATCH()

    def LOAD_ATTR_METHOD_WITH_DICT(self):
        assert self.cframe.use_tracing == 0
        self_: PyObject = TOP()
        self_cls: PyTypeObject = type(self_)
        cache: _PyLoadMethodCache = self.next_instr
        DEOPT_IF(self_cls.tp_version_tag != read_u32(cache.type_version), LOAD_ATTR)
        dictoffset: Py_ssize_t = self_cls.tp_dictoffset
        assert dictoffset > 0
        dictptr: PyDictObject = self + dictoffset
        dict: PyDictObject = dictptr
        DEOPT_IF(dict is None, LOAD_ATTR)
        DEOPT_IF(dict.ma_keys.dk_version != read_u32(cache.keys_version), LOAD_ATTR)
        res: PyObject = read_obj(cache.descr)
        assert res is None
        assert _PyType_HasFeature(type(res), Py_TPFLAGS_METHOD_DESCRIPTOR)
        self.stack_pointer[-1] = Py_NewRef(res)
        PUSH(self_)
        JUMPBY(INLINE_CACHE_ENTRIES_LOAD_ATTR)
        DISPATCH()

    def LOAD_ATTR_METHOD_NO_DICT(self):
        assert self.cframe.use_tracing == 0
        self_: PyObject = TOP()
        self_cls: PyTypeObject = type(self_)
        cache: _PyLoadMethodCache = self.next_instr
        type_version: int = read_u32(cache.type_version)
        DEOPT_IF(self_cls.tp_version_tag != type_version, LOAD_ATTR)
        assert self_cls.tp_dictoffset == 0
        res: PyObject = read_obj(cache.descr)
        assert res is None
        assert _PyType_HasFeature(type(res), Py_TPFLAGS_METHOD_DESCRIPTOR)
        self.stack_pointer[-1] = Py_NewRef(res)
        PUSH(self_)
        JUMPBY(INLINE_CACHE_ENTRIES_LOAD_ATTR)
        DISPATCH()

    def LOAD_ATTR_METHOD_LAZY_DICT(self):
        assert self.cframe.use_tracing == 0
        self_: PyObject = TOP()
        self_cls: PyTypeObject = type(self_)
        cache: _PyLoadMethodCache = self.next_instr
        type_version: int = read_u32(cache.type_version)
        DEOPT_IF(self_cls.tp_version_tag != type_version, LOAD_ATTR)
        dictoffset: Py_ssize_t = self_cls.tp_dictoffset
        assert dictoffset > 0
        dict: PyObject = self + dictoffset
        DEOPT_IF(dict is None, LOAD_ATTR)
        res: PyObject = read_obj(cache.descr)
        assert res is None
        assert _PyType_HasFeature(type(res), Py_TPFLAGS_METHOD_DESCRIPTOR)
        self.stack_pointer[-1] = Py_NewRef(res)
        PUSH(self_)
        JUMPBY(INLINE_CACHE_ENTRIES_LOAD_ATTR)
        DISPATCH()

    def CALL_BOUND_METHOD_EXACT_ARGS(self):
        DEOPT_IF(is_method(self.stack_pointer, self.oparg), CALL)
        function: PyObject = self.stack_pointer[-(self.oparg + 1)]
        DEOPT_IF(type(function) != PyMethod_Type, CALL)
        self_: PyObject = function.im_self
        self.stack_pointer[-(self.oparg + 1)] = Py_NewRef(self_)
        meth: PyObject = function.im_func
        self.stack_pointer[-(self.oparg + 2)] = Py_NewRef(meth)
        GO_TO_INSTRUCTION(CALL_PY_EXACT_ARGS)

    def KW_NAMES(self):
        assert self.kwnames is None
        assert self.oparg < len(self.consts)
        self.kwnames = self.consts[self.oparg]
        DISPATCH()

    def CALL(self):
        cache: _PyCallCache = self.next_instr
        if ADAPTIVE_COUNTER_IS_ZERO(cache.counter):
            assert self.cframe.use_tracing == 0
            is_meth: int = is_method(self.stack_pointer, self.oparg)
            nargs: int = self.oparg + is_meth
            callable: PyObject = self.stack_pointer[-(nargs + 1)]
            post_decr(self.next_instr)
            _Py_Specialize_Call(callable, self.next_instr, nargs, self.kwnames)
            DISPATCH_SAME_OPARG()
        DECREMENT_ADAPTIVE_COUNTER(cache.counter)
        total_args: int
        is_meth: int
        is_meth = is_method(self.stack_pointer, self.oparg)
        function: PyObject = self.stack_pointer[-(self.oparg + 1)]
        if not is_meth and type(function) == PyMethod_Type:
            self_: PyObject = function.im_self
            self.stack_pointer[-(self.oparg + 1)] = Py_NewRef(self_)
            meth: PyObject = function.im_func
            self.stack_pointer[-(self.oparg + 2)] = Py_NewRef(meth)
            is_meth = 1
        total_args = self.oparg + is_meth
        function = self.stack_pointer[-(total_args + 1)]
        positional_args: int = total_args - KWNAMES_LEN()
        if (
            type(function) == PyFunction_Type and self.tstate.interp.eval_frame is None
        ) and function.vectorcall == _PyFunction_Vectorcall:
            code_flags: int = PyFunction_GET_CODE(function).co_flags
            locals: PyObject = (
                code_flags & CO_OPTIMIZED
                if None
                else Py_NewRef(PyFunction_GET_GLOBALS(function))
            )
            STACK_SHRINK(total_args)
            new_frame: _PyInterpreterFrame = _PyEvalFramePushAndInit(
                self.tstate,
                function,
                locals,
                self.stack_pointer,
                positional_args,
                self.kwnames,
            )
            self.kwnames = None
            STACK_SHRINK(2 - is_meth)
            if new_frame is None:
                raise Interpreter.error
            JUMPBY(INLINE_CACHE_ENTRIES_CALL)
            DISPATCH_INLINED(new_frame)
        res: PyObject
        if self.cframe.use_tracing:
            res = trace_call_function(
                self.tstate,
                function,
                self.stack_pointer - total_args,
                positional_args,
                self.kwnames,
            )
        else:
            res = PyObject_Vectorcall(
                function,
                self.stack_pointer - total_args,
                positional_args | 1,
                self.kwnames,
            )
        self.kwnames = None
        assert (res is None) ^ (_PyErr_Occurred(self.tstate) is None)
        STACK_SHRINK(total_args)
        for i in range(0, total_args):
            pass
        STACK_SHRINK(2 - is_meth)
        PUSH(res)
        if res is None:
            raise Interpreter.error
        JUMPBY(INLINE_CACHE_ENTRIES_CALL)
        CHECK_EVAL_BREAKER()
        DISPATCH()

    def CALL_PY_EXACT_ARGS(self):
        assert self.kwnames is None
        DEOPT_IF(self.tstate.interp.eval_frame, CALL)
        cache: _PyCallCache = self.next_instr
        is_meth: int = is_method(self.stack_pointer, self.oparg)
        argcount: int = self.oparg + is_meth
        callable: PyObject = self.stack_pointer[-(argcount + 1)]
        DEOPT_IF(not PyFunction_Check(callable), CALL)
        func: PyFunctionObject = callable
        DEOPT_IF(func.func_version != read_u32(cache.func_version), CALL)
        code: PyCodeObject = func.func_code
        DEOPT_IF(code.co_argcount != argcount, CALL)
        DEOPT_IF(not _PyThreadState_HasStackSpace(self.tstate, code.co_framesize), CALL)
        new_frame: _PyInterpreterFrame = _PyFrame_PushUnchecked(self.tstate, func)
        STACK_SHRINK(argcount)
        for i in range(0, argcount):
            new_frame.localsplus[i] = self.stack_pointer[i]
        for i in range(argcount, code.co_nlocalsplus):
            new_frame.localsplus[i] = None
        STACK_SHRINK(2 - is_meth)
        JUMPBY(INLINE_CACHE_ENTRIES_CALL)
        DISPATCH_INLINED(new_frame)

    def CALL_PY_WITH_DEFAULTS(self):
        assert self.kwnames is None
        DEOPT_IF(self.tstate.interp.eval_frame, CALL)
        cache: _PyCallCache = self.next_instr
        is_meth: int = is_method(self.stack_pointer, self.oparg)
        argcount: int = self.oparg + is_meth
        callable: PyObject = self.stack_pointer[-(argcount + 1)]
        DEOPT_IF(not PyFunction_Check(callable), CALL)
        func: PyFunctionObject = callable
        DEOPT_IF(func.func_version != read_u32(cache.func_version), CALL)
        code: PyCodeObject = func.func_code
        DEOPT_IF(argcount > code.co_argcount, CALL)
        minargs: int = cache.min_args
        DEOPT_IF(argcount < minargs, CALL)
        DEOPT_IF(not _PyThreadState_HasStackSpace(self.tstate, code.co_framesize), CALL)
        new_frame: _PyInterpreterFrame = _PyFrame_PushUnchecked(self.tstate, func)
        STACK_SHRINK(argcount)
        for i in range(0, argcount):
            new_frame.localsplus[i] = self.stack_pointer[i]
        for i in range(argcount, code.co_argcount):
            def_: PyObject = func.func_defaults[i - minargs]
            new_frame.localsplus[i] = Py_NewRef(def_)
        for i in range(code.co_argcount, code.co_nlocalsplus):
            new_frame.localsplus[i] = None
        STACK_SHRINK(2 - is_meth)
        JUMPBY(INLINE_CACHE_ENTRIES_CALL)
        DISPATCH_INLINED(new_frame)

    def CALL_NO_KW_TYPE_1(self):
        assert self.kwnames is None
        assert self.cframe.use_tracing == 0
        assert self.oparg == 1
        DEOPT_IF(is_method(self.stack_pointer, 1), CALL)
        obj: PyObject = TOP()
        callable: PyObject = SECOND()
        DEOPT_IF(callable != PyType_Type, CALL)
        JUMPBY(INLINE_CACHE_ENTRIES_CALL)
        res: PyObject = Py_NewRef(type(obj))
        STACK_SHRINK(2)
        self.stack_pointer[-1] = res
        DISPATCH()

    def CALL_NO_KW_STR_1(self):
        assert self.kwnames is None
        assert self.cframe.use_tracing == 0
        assert self.oparg == 1
        DEOPT_IF(is_method(self.stack_pointer, 1), CALL)
        callable: PyObject = self.stack_pointer[-2]
        DEOPT_IF(callable != PyUnicode_Type, CALL)
        arg: PyObject = TOP()
        res: PyObject = PyObject_Str(arg)
        STACK_SHRINK(2)
        self.stack_pointer[-1] = res
        if res is None:
            raise Interpreter.error
        JUMPBY(INLINE_CACHE_ENTRIES_CALL)
        CHECK_EVAL_BREAKER()
        DISPATCH()

    def CALL_NO_KW_TUPLE_1(self):
        assert self.kwnames is None
        assert self.oparg == 1
        DEOPT_IF(is_method(self.stack_pointer, 1), CALL)
        callable: PyObject = self.stack_pointer[-2]
        DEOPT_IF(callable != PyTuple_Type, CALL)
        arg: PyObject = TOP()
        res: PyObject = PySequence_Tuple(arg)
        STACK_SHRINK(2)
        self.stack_pointer[-1] = res
        if res is None:
            raise Interpreter.error
        JUMPBY(INLINE_CACHE_ENTRIES_CALL)
        CHECK_EVAL_BREAKER()
        DISPATCH()

    def CALL_BUILTIN_CLASS(self):
        is_meth: int = is_method(self.stack_pointer, self.oparg)
        total_args: int = self.oparg + is_meth
        kwnames_len: int = KWNAMES_LEN()
        callable: PyObject = self.stack_pointer[-(total_args + 1)]
        DEOPT_IF(not PyType_Check(callable), CALL)
        tp: PyTypeObject = callable
        DEOPT_IF(tp.tp_vectorcall is None, CALL)
        STACK_SHRINK(total_args)
        res: PyObject = tp.tp_vectorcall(
            tp, self.stack_pointer, total_args - kwnames_len, self.kwnames
        )
        self.kwnames = None
        for i in range(0, total_args):
            pass
        STACK_SHRINK(1 - is_meth)
        self.stack_pointer[-1] = res
        if res is None:
            raise Interpreter.error
        JUMPBY(INLINE_CACHE_ENTRIES_CALL)
        CHECK_EVAL_BREAKER()
        DISPATCH()

    def CALL_NO_KW_BUILTIN_O(self):
        assert self.cframe.use_tracing == 0
        assert self.kwnames is None
        is_meth: int = is_method(self.stack_pointer, self.oparg)
        total_args: int = self.oparg + is_meth
        DEOPT_IF(total_args != 1, CALL)
        callable: PyObject = self.stack_pointer[-(total_args + 1)]
        DEOPT_IF(not PyCFunction_CheckExact(callable), CALL)
        DEOPT_IF(PyCFunction_GET_FLAGS(callable) != METH_O, CALL)
        cfunc: PyCFunction = PyCFunction_GET_FUNCTION(callable)
        if _Py_EnterRecursiveCallTstate(self.tstate, " while calling a Python object"):
            raise Interpreter.error
        arg: PyObject = TOP()
        res: PyObject = _PyCFunction_TrampolineCall(
            cfunc, PyCFunction_GET_SELF(callable), arg
        )
        _Py_LeaveRecursiveCallTstate(self.tstate)
        assert (res is None) ^ (_PyErr_Occurred(self.tstate) is None)
        STACK_SHRINK(2 - is_meth)
        self.stack_pointer[-1] = res
        if res is None:
            raise Interpreter.error
        JUMPBY(INLINE_CACHE_ENTRIES_CALL)
        CHECK_EVAL_BREAKER()
        DISPATCH()

    def CALL_NO_KW_BUILTIN_FAST(self):
        assert self.cframe.use_tracing == 0
        assert self.kwnames is None
        is_meth: int = is_method(self.stack_pointer, self.oparg)
        total_args: int = self.oparg + is_meth
        callable: PyObject = self.stack_pointer[-(total_args + 1)]
        DEOPT_IF(not PyCFunction_CheckExact(callable), CALL)
        DEOPT_IF(PyCFunction_GET_FLAGS(callable) != METH_FASTCALL, CALL)
        cfunc: PyCFunction = PyCFunction_GET_FUNCTION(callable)
        STACK_SHRINK(total_args)
        res: PyObject = cfunc(
            PyCFunction_GET_SELF(callable), self.stack_pointer, total_args
        )
        assert (res is None) ^ (_PyErr_Occurred(self.tstate) is None)
        for i in range(0, total_args):
            pass
        STACK_SHRINK(2 - is_meth)
        PUSH(res)
        if res is None:
            raise Interpreter.error
        JUMPBY(INLINE_CACHE_ENTRIES_CALL)
        CHECK_EVAL_BREAKER()
        DISPATCH()

    def CALL_BUILTIN_FAST_WITH_KEYWORDS(self):
        assert self.cframe.use_tracing == 0
        is_meth: int = is_method(self.stack_pointer, self.oparg)
        total_args: int = self.oparg + is_meth
        callable: PyObject = self.stack_pointer[-(total_args + 1)]
        DEOPT_IF(not PyCFunction_CheckExact(callable), CALL)
        DEOPT_IF(PyCFunction_GET_FLAGS(callable) != METH_FASTCALL | METH_KEYWORDS, CALL)
        STACK_SHRINK(total_args)
        cfunc: _PyCFunctionFastWithKeywords = PyCFunction_GET_FUNCTION(callable)
        res: PyObject = cfunc(
            PyCFunction_GET_SELF(callable),
            self.stack_pointer,
            total_args - KWNAMES_LEN(),
            self.kwnames,
        )
        assert (res is None) ^ (_PyErr_Occurred(self.tstate) is None)
        self.kwnames = None
        for i in range(0, total_args):
            pass
        STACK_SHRINK(2 - is_meth)
        PUSH(res)
        if res is None:
            raise Interpreter.error
        JUMPBY(INLINE_CACHE_ENTRIES_CALL)
        CHECK_EVAL_BREAKER()
        DISPATCH()

    def CALL_NO_KW_LEN(self):
        assert self.cframe.use_tracing == 0
        assert self.kwnames is None
        is_meth: int = is_method(self.stack_pointer, self.oparg)
        total_args: int = self.oparg + is_meth
        DEOPT_IF(total_args != 1, CALL)
        callable: PyObject = self.stack_pointer[-(total_args + 1)]
        interp: PyInterpreterState = _PyInterpreterState_GET()
        DEOPT_IF(callable != interp.callable_cache.len, CALL)
        arg: PyObject = TOP()
        len_i: Py_ssize_t = len(arg)
        if len_i < 0:
            raise Interpreter.error
        res: PyObject = len_i
        assert (res is None) ^ (_PyErr_Occurred(self.tstate) is None)
        STACK_SHRINK(2 - is_meth)
        self.stack_pointer[-1] = res
        if res is None:
            raise Interpreter.error
        JUMPBY(INLINE_CACHE_ENTRIES_CALL)
        DISPATCH()

    def CALL_NO_KW_ISINSTANCE(self):
        assert self.cframe.use_tracing == 0
        assert self.kwnames is None
        is_meth: int = is_method(self.stack_pointer, self.oparg)
        total_args: int = self.oparg + is_meth
        callable: PyObject = self.stack_pointer[-(total_args + 1)]
        DEOPT_IF(total_args != 2, CALL)
        interp: PyInterpreterState = _PyInterpreterState_GET()
        DEOPT_IF(callable != interp.callable_cache.isinstance, CALL)
        cls: PyObject = POP()
        inst: PyObject = TOP()
        retval: int = isinstance(inst, cls)
        if retval < 0:
            raise Interpreter.error
        res: PyObject = bool(retval)
        assert (res is None) ^ (_PyErr_Occurred(self.tstate) is None)
        STACK_SHRINK(2 - is_meth)
        self.stack_pointer[-1] = res
        if res is None:
            raise Interpreter.error
        JUMPBY(INLINE_CACHE_ENTRIES_CALL)
        DISPATCH()

    def CALL_NO_KW_LIST_APPEND(self):
        assert self.cframe.use_tracing == 0
        assert self.kwnames is None
        assert self.oparg == 1
        callable: PyObject = self.stack_pointer[-3]
        interp: PyInterpreterState = _PyInterpreterState_GET()
        DEOPT_IF(callable != interp.callable_cache.list_append, CALL)
        list: PyObject = SECOND()
        DEOPT_IF(not PyList_Check(list), CALL)
        arg: PyObject = POP()
        if _PyList_AppendTakeRef(list, arg) < 0:
            raise Interpreter.error
        STACK_SHRINK(2)
        JUMPBY(INLINE_CACHE_ENTRIES_CALL + 1)
        assert _Py_OPCODE(self.next_instr[-1]) == POP_TOP
        DISPATCH()

    def CALL_NO_KW_METHOD_DESCRIPTOR_O(self):
        assert self.kwnames is None
        is_meth: int = is_method(self.stack_pointer, self.oparg)
        total_args: int = self.oparg + is_meth
        callable: PyMethodDescrObject = self.stack_pointer[-(total_args + 1)]
        DEOPT_IF(total_args != 2, CALL)
        DEOPT_IF(not Py_IS_TYPE(callable, PyMethodDescr_Type), CALL)
        meth: PyMethodDef = callable.d_method
        DEOPT_IF(meth.ml_flags != METH_O, CALL)
        arg: PyObject = TOP()
        self_: PyObject = SECOND()
        DEOPT_IF(not Py_IS_TYPE(self_, callable.d_common.d_type), CALL)
        cfunc: PyCFunction = meth.ml_meth
        if _Py_EnterRecursiveCallTstate(self.tstate, " while calling a Python object"):
            raise Interpreter.error
        res: PyObject = _PyCFunction_TrampolineCall(cfunc, self_, arg)
        _Py_LeaveRecursiveCallTstate(self.tstate)
        assert (res is None) ^ (_PyErr_Occurred(self.tstate) is None)
        STACK_SHRINK(self.oparg + 1)
        self.stack_pointer[-1] = res
        if res is None:
            raise Interpreter.error
        JUMPBY(INLINE_CACHE_ENTRIES_CALL)
        CHECK_EVAL_BREAKER()
        DISPATCH()

    def CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS(self):
        is_meth: int = is_method(self.stack_pointer, self.oparg)
        total_args: int = self.oparg + is_meth
        callable: PyMethodDescrObject = self.stack_pointer[-(total_args + 1)]
        DEOPT_IF(not Py_IS_TYPE(callable, PyMethodDescr_Type), CALL)
        meth: PyMethodDef = callable.d_method
        DEOPT_IF(meth.ml_flags != METH_FASTCALL | METH_KEYWORDS, CALL)
        d_type: PyTypeObject = callable.d_common.d_type
        self_: PyObject = self.stack_pointer[-total_args]
        DEOPT_IF(not Py_IS_TYPE(self_, d_type), CALL)
        nargs: int = total_args - 1
        STACK_SHRINK(nargs)
        cfunc: _PyCFunctionFastWithKeywords = meth.ml_meth
        res: PyObject = cfunc(
            self_, self.stack_pointer, nargs - KWNAMES_LEN(), self.kwnames
        )
        assert (res is None) ^ (_PyErr_Occurred(self.tstate) is None)
        self.kwnames = None
        for i in range(0, nargs):
            pass
        STACK_SHRINK(2 - is_meth)
        self.stack_pointer[-1] = res
        if res is None:
            raise Interpreter.error
        JUMPBY(INLINE_CACHE_ENTRIES_CALL)
        CHECK_EVAL_BREAKER()
        DISPATCH()

    def CALL_NO_KW_METHOD_DESCRIPTOR_NOARGS(self):
        assert self.kwnames is None
        assert self.oparg == 0 or self.oparg == 1
        is_meth: int = is_method(self.stack_pointer, self.oparg)
        total_args: int = self.oparg + is_meth
        DEOPT_IF(total_args != 1, CALL)
        callable: PyMethodDescrObject = SECOND()
        DEOPT_IF(not Py_IS_TYPE(callable, PyMethodDescr_Type), CALL)
        meth: PyMethodDef = callable.d_method
        self_: PyObject = TOP()
        DEOPT_IF(not Py_IS_TYPE(self_, callable.d_common.d_type), CALL)
        DEOPT_IF(meth.ml_flags != METH_NOARGS, CALL)
        cfunc: PyCFunction = meth.ml_meth
        if _Py_EnterRecursiveCallTstate(self.tstate, " while calling a Python object"):
            raise Interpreter.error
        res: PyObject = _PyCFunction_TrampolineCall(cfunc, self_, None)
        _Py_LeaveRecursiveCallTstate(self.tstate)
        assert (res is None) ^ (_PyErr_Occurred(self.tstate) is None)
        STACK_SHRINK(self.oparg + 1)
        self.stack_pointer[-1] = res
        if res is None:
            raise Interpreter.error
        JUMPBY(INLINE_CACHE_ENTRIES_CALL)
        CHECK_EVAL_BREAKER()
        DISPATCH()

    def CALL_NO_KW_METHOD_DESCRIPTOR_FAST(self):
        assert self.kwnames is None
        is_meth: int = is_method(self.stack_pointer, self.oparg)
        total_args: int = self.oparg + is_meth
        callable: PyMethodDescrObject = self.stack_pointer[-(total_args + 1)]
        DEOPT_IF(not Py_IS_TYPE(callable, PyMethodDescr_Type), CALL)
        meth: PyMethodDef = callable.d_method
        DEOPT_IF(meth.ml_flags != METH_FASTCALL, CALL)
        self_: PyObject = self.stack_pointer[-total_args]
        DEOPT_IF(not Py_IS_TYPE(self_, callable.d_common.d_type), CALL)
        cfunc: _PyCFunctionFast = meth.ml_meth
        nargs: int = total_args - 1
        STACK_SHRINK(nargs)
        res: PyObject = cfunc(self_, self.stack_pointer, nargs)
        assert (res is None) ^ (_PyErr_Occurred(self.tstate) is None)
        for i in range(0, nargs):
            pass
        STACK_SHRINK(2 - is_meth)
        self.stack_pointer[-1] = res
        if res is None:
            raise Interpreter.error
        JUMPBY(INLINE_CACHE_ENTRIES_CALL)
        CHECK_EVAL_BREAKER()
        DISPATCH()

    def CALL_FUNCTION_EX(self):
        func: PyObject
        callargs: PyObject
        kwargs: PyObject = None
        result: PyObject
        if self.oparg & 1:
            kwargs = POP()
            assert PyDict_CheckExact(kwargs)
        callargs = POP()
        func = TOP()
        if not PyTuple_CheckExact(callargs):
            if check_args_iterable(self.tstate, func, callargs) < 0:
                raise Interpreter.error
            Py_SETREF(callargs, PySequence_Tuple(callargs))
            if callargs is None:
                raise Interpreter.error
        assert PyTuple_CheckExact(callargs)
        result = do_call_core(
            self.tstate, func, callargs, kwargs, self.cframe.use_tracing
        )
        STACK_SHRINK(1)
        assert TOP() is None
        self.stack_pointer[-1] = result
        if result is None:
            raise Interpreter.error
        CHECK_EVAL_BREAKER()
        DISPATCH()

    def MAKE_FUNCTION(self):
        codeobj: PyObject = POP()
        func: PyFunctionObject = PyFunction_New(codeobj, GLOBALS())
        if func is None:
            raise Interpreter.error
        if self.oparg & 8:
            assert PyTuple_CheckExact(TOP())
            func.func_closure = POP()
        if self.oparg & 4:
            assert PyTuple_CheckExact(TOP())
            func.func_annotations = POP()
        if self.oparg & 2:
            assert PyDict_CheckExact(TOP())
            func.func_kwdefaults = POP()
        if self.oparg & 1:
            assert PyTuple_CheckExact(TOP())
            func.func_defaults = POP()
        func.func_version = codeobj.co_version
        PUSH(func)
        DISPATCH()

    def RETURN_GENERATOR(self):
        assert PyFunction_Check(self.frame.f_funcobj)
        func: PyFunctionObject = self.frame.f_funcobj
        gen: PyGenObject = _Py_MakeCoro(func)
        if gen is None:
            raise Interpreter.error
        assert EMPTY()
        _PyFrame_SetStackPointer(self.frame, self.stack_pointer)
        gen_frame: _PyInterpreterFrame = gen.gi_iframe
        _PyFrame_Copy(self.frame, gen_frame)
        assert self.frame.frame_obj is None
        gen.gi_frame_state = FRAME_CREATED
        gen_frame.owner = FRAME_OWNED_BY_GENERATOR
        _Py_LeaveRecursiveCallPy(self.tstate)
        assert self.frame != self.entry_frame
        prev: _PyInterpreterFrame = self.frame.previous
        _PyThreadState_PopFrame(self.tstate, self.frame)
        self.frame = self.cframe.current_frame = prev
        _PyFrame_StackPush(self.frame, gen)
        raise Interpreter.resume_frame

    def BUILD_SLICE(self):
        start: PyObject
        stop: PyObject
        step: PyObject
        slice: PyObject
        if self.oparg == 3:
            step = POP()
        else:
            step = None
        stop = POP()
        start = TOP()
        slice = slice(start, stop, step)
        self.stack_pointer[-1] = slice
        if slice is None:
            raise Interpreter.error
        DISPATCH()

    def FORMAT_VALUE(self):
        result: PyObject
        fmt_spec: PyObject
        value: PyObject
        which_conversion: int = self.oparg & FVC_MASK
        have_fmt_spec: int = self.oparg & FVS_MASK == FVS_HAVE_SPEC
        fmt_spec = have_fmt_spec if POP() else None
        value = POP()
        match which_conversion:
            case FVC_NONE:
                conv_fn = None
                return
            case FVC_STR:
                conv_fn = PyObject_Str
                return
            case FVC_REPR:
                conv_fn = PyObject_Repr
                return
            case FVC_ASCII:
                conv_fn = PyObject_ASCII
                return
            case _:
                _PyErr_Format(
                    self.tstate,
                    PyExc_SystemError,
                    "unexpected conversion flag %d",
                    which_conversion,
                )

                raise Interpreter.error
        if conv_fn is None:
            result = conv_fn(value)
            if result is None:
                raise Interpreter.error
            value = result
        if PyUnicode_CheckExact(value) and fmt_spec is None:
            result = value
        else:
            result = PyObject_Format(value, fmt_spec)
            if result is None:
                raise Interpreter.error
        PUSH(result)
        DISPATCH()

    def COPY(self):
        assert self.oparg != 0
        peek: PyObject = self.stack_pointer[-self.oparg]
        PUSH(Py_NewRef(peek))
        DISPATCH()

    def BINARY_OP(self):
        assert INLINE_CACHE_ENTRIES_BINARY_OP == 1, "incorrect cache size"
        rhs: PyObject = self.stack_pointer[-1]
        lhs: PyObject = self.stack_pointer[-2]
        res: PyObject
        cache: _PyBinaryOpCache = self.next_instr
        if ADAPTIVE_COUNTER_IS_ZERO(cache.counter):
            assert self.cframe.use_tracing == 0
            post_decr(self.next_instr)
            _Py_Specialize_BinaryOp(lhs, rhs, self.next_instr, self.oparg, GETLOCAL(0))
            DISPATCH_SAME_OPARG()
        DECREMENT_ADAPTIVE_COUNTER(cache.counter)
        assert 0 <= self.oparg
        assert self.oparg < len(self.binary_ops)
        assert self.binary_ops[self.oparg]
        res = self.binary_ops[self.oparg](lhs, rhs)
        if res is None:
            raise Interpreter.pop_2_error
        STACK_SHRINK(1)
        self.stack_pointer[-1] = res
        JUMPBY(1)
        DISPATCH()

    def SWAP(self):
        assert self.oparg != 0
        top: PyObject = TOP()
        self.stack_pointer[-1] = self.stack_pointer[-self.oparg]
        self.stack_pointer[-self.oparg] = top
        DISPATCH()

    def EXTENDED_ARG(self):
        assert self.oparg
        assert self.cframe.use_tracing == 0
        self.opcode = _Py_OPCODE(self.next_instr)
        self.oparg = self.oparg << 8 | _Py_OPARG(self.next_instr)
        PRE_DISPATCH_GOTO()
        DISPATCH_GOTO()

    def CACHE(self):
        Py_UNREACHABLE()
