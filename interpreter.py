from typing import Any
from pytype.pyc import opcodes as ops

NULL = None
PyObject = Any
PyThreadState = Any
_PyInterpreterFrame = Any
_Py_atomic_int = Any
_PyCFrame = Any
_Py_CODEUNIT = Any
binaryfunc = Any
PyLongObject = Any
destructor = Any
PyFloatObject = Any
_PyBinarySubscrCache = Any
_PyObject_Free = Any
Py_ssize_t = Any
PyTypeObject = Any
PyHeapTypeObject = Any
PyFunctionObject = Any
PyCodeObject = Any
PyListObject = Any
_PyStoreSubscrCache = Any
PyDictObject = Any
unaryfunc = Any
PyGenObject = Any
PySendResult = Any
_PyErr_StackItem = Any
PyStopIterationObject = Any
_PyUnpackSequenceCache = Any
_PyAttrCache = Any
_PyLoadGlobalCache = Any
PyDictUnicodeEntry = Any
PyDictOrValues = Any
PyModuleObject = Any
PyDictKeyEntry = Any
_PyLoadMethodCache = Any
PyDictValues = Any
_PyCompareOpCache = Any
_PyForIterCache = Any
_PyListIterObject = Any
_PyTupleIterObject = Any
PyTupleObject = Any
_PyRangeIterObject = Any
PyMethodObject = Any
_PyCallCache = Any
PyCFunction = Any
_PyCFunctionFast = Any
_PyCFunctionFastWithKeywords = Any
PyInterpreterState = Any
PyMethodDescrObject = Any
PyMethodDef = Any
_PyBinaryOpCache = Any
PyObject_Free: _PyObject_Free
# void _PyFloat_ExactDealloc(PyObject)
# void _PyUnicode_ExactDealloc(PyObject)
value: PyObject
value1: PyObject
value2: PyObject
left: PyObject
right: PyObject
res: PyObject
sum: PyObject
prod: PyObject
sub: PyObject
container: PyObject
start: PyObject
stop: PyObject
v: PyObject
lhs: PyObject
rhs: PyObject
list: PyObject
tuple: PyObject
dict: PyObject
owner: PyObject
exit_func: PyObject
lasti: PyObject
val: PyObject
retval: PyObject
obj: PyObject
iter: PyObject
aiter: PyObject
awaitable: PyObject
iterable: PyObject
w: PyObject
exc_value: PyObject
bc: PyObject
orig: PyObject
excs: PyObject
update: PyObject
b: PyObject
fromlist: PyObject
level: PyObject
from_: PyObject
long_unsigned_int_size_t = Any
jump: size_t
unsigned_short_uint16_t = Any
when_to_jump_mask: uint16_t
invert: uint16_t
counter: uint16_t
index: uint16_t
hint: uint16_t
unsigned_int_uint32_t = Any
type_version: uint32_t
unsigned_long_uint64_t = Any


def dummy_func(
    tstate,
    frame,
    opcode,
    oparg,
    eval_breaker,
    cframe,
    names,
    consts,
    next_instr,
    stack_pointer,
    kwnames,
    throwflag,
    binary_ops,
):
    entry_frame: _PyInterpreterFrame
    match opcode:
        case ops.NOP:
            DISPATCH()
        case ops.RESUME:
            assert tstate.cframe == (cframe)
            assert frame == cframe.current_frame
            if _Py_atomic_load_relaxed_int32(eval_breaker) and (oparg < 2):
                return  # goto handle_eval_breaker
            else:
                print()
            DISPATCH()
        case ops.LOAD_CLOSURE:
            value: PyObject
            value = frame.localsplus[oparg]
            if value == NULL:
                return  # goto unbound_local_error
            else:
                print()
            Py_INCREF(value)
            STACK_GROW(1)
            POKE(1, value)
            DISPATCH()
        case ops.LOAD_FAST_CHECK:
            value: PyObject
            value = frame.localsplus[oparg]
            if value == NULL:
                return  # goto unbound_local_error
            else:
                print()
            Py_INCREF(value)
            STACK_GROW(1)
            POKE(1, value)
            DISPATCH()
        case ops.LOAD_FAST:
            value: PyObject
            value = frame.localsplus[oparg]
            assert value != NULL
            Py_INCREF(value)
            STACK_GROW(1)
            POKE(1, value)
            DISPATCH()
        case ops.LOAD_CONST:
            PREDICTED(LOAD_CONST)
            value: PyObject
            value = GETITEM(consts, oparg)
            Py_INCREF(value)
            STACK_GROW(1)
            POKE(1, value)
            DISPATCH()
        case ops.STORE_FAST:
            value: PyObject = PEEK(1)
            SETLOCAL(oparg, value)
            STACK_SHRINK(1)
            DISPATCH()
        case ops.LOAD_FAST__LOAD_FAST:
            _tmp_1: PyObject
            _tmp_2: PyObject
            value: PyObject
            value = frame.localsplus[oparg]
            assert value != NULL
            Py_INCREF(value)
            _tmp_2 = value
            NEXTOPARG()
            JUMPBY(1)
            value: PyObject
            value = frame.localsplus[oparg]
            assert value != NULL
            Py_INCREF(value)
            _tmp_1 = value
            STACK_GROW(2)
            POKE(1, _tmp_1)
            POKE(2, _tmp_2)
            DISPATCH()
        case ops.LOAD_FAST__LOAD_CONST:
            _tmp_1: PyObject
            _tmp_2: PyObject
            value: PyObject
            value = frame.localsplus[oparg]
            assert value != NULL
            Py_INCREF(value)
            _tmp_2 = value
            NEXTOPARG()
            JUMPBY(1)
            value: PyObject
            value = GETITEM(consts, oparg)
            Py_INCREF(value)
            _tmp_1 = value
            STACK_GROW(2)
            POKE(1, _tmp_1)
            POKE(2, _tmp_2)
            DISPATCH()
        case ops.STORE_FAST__LOAD_FAST:
            _tmp_1: PyObject = PEEK(1)
            value: PyObject = _tmp_1
            SETLOCAL(oparg, value)
            NEXTOPARG()
            JUMPBY(1)
            value: PyObject
            value = frame.localsplus[oparg]
            assert value != NULL
            Py_INCREF(value)
            _tmp_1 = value
            POKE(1, _tmp_1)
            DISPATCH()
        case ops.STORE_FAST__STORE_FAST:
            _tmp_1: PyObject = PEEK(1)
            _tmp_2: PyObject = PEEK(2)
            value: PyObject = _tmp_1
            SETLOCAL(oparg, value)
            NEXTOPARG()
            JUMPBY(1)
            value: PyObject = _tmp_2
            SETLOCAL(oparg, value)
            STACK_SHRINK(2)
            DISPATCH()
        case ops.LOAD_CONST__LOAD_FAST:
            _tmp_1: PyObject
            _tmp_2: PyObject
            value: PyObject
            value = GETITEM(consts, oparg)
            Py_INCREF(value)
            _tmp_2 = value
            NEXTOPARG()
            JUMPBY(1)
            value: PyObject
            value = frame.localsplus[oparg]
            assert value != NULL
            Py_INCREF(value)
            _tmp_1 = value
            STACK_GROW(2)
            POKE(1, _tmp_1)
            POKE(2, _tmp_2)
            DISPATCH()
        case ops.POP_TOP:
            value: PyObject = PEEK(1)
            Py_DECREF(value)
            STACK_SHRINK(1)
            DISPATCH()
        case ops.PUSH_NULL:
            res: PyObject
            res = NULL
            STACK_GROW(1)
            POKE(1, res)
            DISPATCH()
        case ops.END_FOR:
            _tmp_1: PyObject = PEEK(1)
            _tmp_2: PyObject = PEEK(2)
            value: PyObject = _tmp_1
            Py_DECREF(value)
            value: PyObject = _tmp_2
            Py_DECREF(value)
            STACK_SHRINK(2)
            DISPATCH()
        case ops.UNARY_POSITIVE:
            value: PyObject = PEEK(1)
            res: PyObject
            res = PyNumber_Positive(value)
            Py_DECREF(value)
            if res == NULL:
                return  # goto pop_1_error
            else:
                print()
            POKE(1, res)
            DISPATCH()
        case ops.UNARY_NEGATIVE:
            value: PyObject = PEEK(1)
            res: PyObject
            res = PyNumber_Negative(value)
            Py_DECREF(value)
            if res == NULL:
                return  # goto pop_1_error
            else:
                print()
            POKE(1, res)
            DISPATCH()
        case ops.UNARY_NOT:
            value: PyObject = PEEK(1)
            res: PyObject
            err: int = PyObject_IsTrue(value)
            Py_DECREF(value)
            if err < 0:
                return  # goto pop_1_error
            else:
                print()
            if err == 0:
                res = Py_True
            else:
                res = Py_False
            Py_INCREF(res)
            POKE(1, res)
            DISPATCH()
        case ops.UNARY_INVERT:
            value: PyObject = PEEK(1)
            res: PyObject
            res = PyNumber_Invert(value)
            Py_DECREF(value)
            if res == NULL:
                return  # goto pop_1_error
            else:
                print()
            POKE(1, res)
            DISPATCH()
        case ops.BINARY_OP_MULTIPLY_INT:
            right: PyObject = PEEK(1)
            left: PyObject = PEEK(2)
            prod: PyObject
            assert cframe.use_tracing == 0
            DEOPT_IF(not PyLong_CheckExact(left), BINARY_OP)
            DEOPT_IF(not PyLong_CheckExact(right), BINARY_OP)
            STAT_INC(BINARY_OP, hit)
            prod = _PyLong_Multiply(PyLongObject(left), PyLongObject(right))
            _Py_DECREF_SPECIALIZED(right, destructor(PyObject_Free))
            _Py_DECREF_SPECIALIZED(left, destructor(PyObject_Free))
            if prod == NULL:
                return  # goto pop_2_error
            else:
                print()
            STACK_SHRINK(1)
            POKE(1, prod)
            JUMPBY(1)
            DISPATCH()
        case ops.BINARY_OP_MULTIPLY_FLOAT:
            right: PyObject = PEEK(1)
            left: PyObject = PEEK(2)
            prod: PyObject
            assert cframe.use_tracing == 0
            DEOPT_IF(not PyFloat_CheckExact(left), BINARY_OP)
            DEOPT_IF(not PyFloat_CheckExact(right), BINARY_OP)
            STAT_INC(BINARY_OP, hit)
            dprod: double = (PyFloatObject(left)).ob_fval * (
                PyFloatObject(right)
            ).ob_fval
            prod = PyFloat_FromDouble(dprod)
            _Py_DECREF_SPECIALIZED(right, _PyFloat_ExactDealloc)
            _Py_DECREF_SPECIALIZED(left, _PyFloat_ExactDealloc)
            if prod == NULL:
                return  # goto pop_2_error
            else:
                print()
            STACK_SHRINK(1)
            POKE(1, prod)
            JUMPBY(1)
            DISPATCH()
        case ops.BINARY_OP_SUBTRACT_INT:
            right: PyObject = PEEK(1)
            left: PyObject = PEEK(2)
            sub: PyObject
            assert cframe.use_tracing == 0
            DEOPT_IF(not PyLong_CheckExact(left), BINARY_OP)
            DEOPT_IF(not PyLong_CheckExact(right), BINARY_OP)
            STAT_INC(BINARY_OP, hit)
            sub = _PyLong_Subtract(PyLongObject(left), PyLongObject(right))
            _Py_DECREF_SPECIALIZED(right, destructor(PyObject_Free))
            _Py_DECREF_SPECIALIZED(left, destructor(PyObject_Free))
            if sub == NULL:
                return  # goto pop_2_error
            else:
                print()
            STACK_SHRINK(1)
            POKE(1, sub)
            JUMPBY(1)
            DISPATCH()
        case ops.BINARY_OP_SUBTRACT_FLOAT:
            right: PyObject = PEEK(1)
            left: PyObject = PEEK(2)
            sub: PyObject
            assert cframe.use_tracing == 0
            DEOPT_IF(not PyFloat_CheckExact(left), BINARY_OP)
            DEOPT_IF(not PyFloat_CheckExact(right), BINARY_OP)
            STAT_INC(BINARY_OP, hit)
            dsub: double = (PyFloatObject(left)).ob_fval - (
                PyFloatObject(right)
            ).ob_fval
            sub = PyFloat_FromDouble(dsub)
            _Py_DECREF_SPECIALIZED(right, _PyFloat_ExactDealloc)
            _Py_DECREF_SPECIALIZED(left, _PyFloat_ExactDealloc)
            if sub == NULL:
                return  # goto pop_2_error
            else:
                print()
            STACK_SHRINK(1)
            POKE(1, sub)
            JUMPBY(1)
            DISPATCH()
        case ops.BINARY_OP_ADD_UNICODE:
            right: PyObject = PEEK(1)
            left: PyObject = PEEK(2)
            res: PyObject
            assert cframe.use_tracing == 0
            DEOPT_IF(not PyUnicode_CheckExact(left), BINARY_OP)
            DEOPT_IF(Py_TYPE(right) != Py_TYPE(left), BINARY_OP)
            STAT_INC(BINARY_OP, hit)
            res = PyUnicode_Concat(left, right)
            _Py_DECREF_SPECIALIZED(left, _PyUnicode_ExactDealloc)
            _Py_DECREF_SPECIALIZED(right, _PyUnicode_ExactDealloc)
            if res == NULL:
                return  # goto pop_2_error
            else:
                print()
            STACK_SHRINK(1)
            POKE(1, res)
            JUMPBY(1)
            DISPATCH()
        case ops.BINARY_OP_INPLACE_ADD_UNICODE:
            right: PyObject = PEEK(1)
            left: PyObject = PEEK(2)
            assert cframe.use_tracing == 0
            DEOPT_IF(not PyUnicode_CheckExact(left), BINARY_OP)
            DEOPT_IF(Py_TYPE(right) != Py_TYPE(left), BINARY_OP)
            true_next: _Py_CODEUNIT = next_instr[INLINE_CACHE_ENTRIES_BINARY_OP]
            assert (_Py_OPCODE(true_next) == STORE_FAST) or (
                _Py_OPCODE(true_next) == STORE_FAST__LOAD_FAST
            )
            target_local: PyObject = frame.localsplus[_Py_OPARG(true_next)]
            DEOPT_IF((target_local) != left, BINARY_OP)
            STAT_INC(BINARY_OP, hit)
            assert Py_REFCNT(left) >= 2
            _Py_DECREF_NO_DEALLOC(left)
            PyUnicode_Append(target_local, right)
            _Py_DECREF_SPECIALIZED(right, _PyUnicode_ExactDealloc)
            if (target_local) == NULL:
                return  # goto pop_2_error
            else:
                print()
            JUMPBY(INLINE_CACHE_ENTRIES_BINARY_OP + 1)
            STACK_SHRINK(2)
            DISPATCH()
        case ops.BINARY_OP_ADD_FLOAT:
            right: PyObject = PEEK(1)
            left: PyObject = PEEK(2)
            sum: PyObject
            assert cframe.use_tracing == 0
            DEOPT_IF(not PyFloat_CheckExact(left), BINARY_OP)
            DEOPT_IF(Py_TYPE(right) != Py_TYPE(left), BINARY_OP)
            STAT_INC(BINARY_OP, hit)
            dsum: double = (PyFloatObject(left)).ob_fval + (
                PyFloatObject(right)
            ).ob_fval
            sum = PyFloat_FromDouble(dsum)
            _Py_DECREF_SPECIALIZED(right, _PyFloat_ExactDealloc)
            _Py_DECREF_SPECIALIZED(left, _PyFloat_ExactDealloc)
            if sum == NULL:
                return  # goto pop_2_error
            else:
                print()
            STACK_SHRINK(1)
            POKE(1, sum)
            JUMPBY(1)
            DISPATCH()
        case ops.BINARY_OP_ADD_INT:
            right: PyObject = PEEK(1)
            left: PyObject = PEEK(2)
            sum: PyObject
            assert cframe.use_tracing == 0
            DEOPT_IF(not PyLong_CheckExact(left), BINARY_OP)
            DEOPT_IF(Py_TYPE(right) != Py_TYPE(left), BINARY_OP)
            STAT_INC(BINARY_OP, hit)
            sum = _PyLong_Add(PyLongObject(left), PyLongObject(right))
            _Py_DECREF_SPECIALIZED(right, destructor(PyObject_Free))
            _Py_DECREF_SPECIALIZED(left, destructor(PyObject_Free))
            if sum == NULL:
                return  # goto pop_2_error
            else:
                print()
            STACK_SHRINK(1)
            POKE(1, sum)
            JUMPBY(1)
            DISPATCH()
        case ops.BINARY_SUBSCR:
            PREDICTED(BINARY_SUBSCR)
            static_assert(
                INLINE_CACHE_ENTRIES_BINARY_SUBSCR == 4, "incorrect cache size"
            )
            sub: PyObject = PEEK(1)
            container: PyObject = PEEK(2)
            res: PyObject
            cache: _PyBinarySubscrCache = _PyBinarySubscrCache(next_instr)
            if ADAPTIVE_COUNTER_IS_ZERO(cache.counter):
                assert cframe.use_tracing == 0
                next_instr -= 1
                _Py_Specialize_BinarySubscr(container, sub, next_instr)
                DISPATCH_SAME_OPARG()
            else:
                print()
            STAT_INC(BINARY_SUBSCR, deferred)
            DECREMENT_ADAPTIVE_COUNTER(cache.counter)
            res = PyObject_GetItem(container, sub)
            Py_DECREF(container)
            Py_DECREF(sub)
            if res == NULL:
                return  # goto pop_2_error
            else:
                print()
            STACK_SHRINK(1)
            POKE(1, res)
            JUMPBY(4)
            DISPATCH()
        case ops.BINARY_SLICE:
            stop: PyObject = PEEK(1)
            start: PyObject = PEEK(2)
            container: PyObject = PEEK(3)
            res: PyObject
            slice: PyObject = _PyBuildSlice_ConsumeRefs(start, stop)
            if slice == NULL:
                res = NULL
            else:
                res = PyObject_GetItem(container, slice)
                Py_DECREF(slice)
            Py_DECREF(container)
            if res == NULL:
                return  # goto pop_3_error
            else:
                print()
            STACK_SHRINK(2)
            POKE(1, res)
            DISPATCH()
        case ops.STORE_SLICE:
            stop: PyObject = PEEK(1)
            start: PyObject = PEEK(2)
            container: PyObject = PEEK(3)
            v: PyObject = PEEK(4)
            slice: PyObject = _PyBuildSlice_ConsumeRefs(start, stop)
            err: int
            if slice == NULL:
                err = 1
            else:
                err = PyObject_SetItem(container, slice, v)
                Py_DECREF(slice)
            Py_DECREF(v)
            Py_DECREF(container)
            if err:
                return  # goto pop_4_error
            else:
                print()
            STACK_SHRINK(4)
            DISPATCH()
        case ops.BINARY_SUBSCR_LIST_INT:
            sub: PyObject = PEEK(1)
            list: PyObject = PEEK(2)
            res: PyObject
            assert cframe.use_tracing == 0
            DEOPT_IF(not PyLong_CheckExact(sub), BINARY_SUBSCR)
            DEOPT_IF(not PyList_CheckExact(list), BINARY_SUBSCR)
            DEOPT_IF(not _PyLong_IsPositiveSingleDigit(sub), BINARY_SUBSCR)
            assert (PyLongObject(_PyLong_GetZero())).ob_digit[0] == 0
            index: Py_ssize_t = (PyLongObject(sub)).ob_digit[0]
            DEOPT_IF(index >= PyList_GET_SIZE(list), BINARY_SUBSCR)
            STAT_INC(BINARY_SUBSCR, hit)
            res = PyList_GET_ITEM(list, index)
            assert res != NULL
            Py_INCREF(res)
            _Py_DECREF_SPECIALIZED(sub, destructor(PyObject_Free))
            Py_DECREF(list)
            STACK_SHRINK(1)
            POKE(1, res)
            JUMPBY(4)
            DISPATCH()
        case ops.BINARY_SUBSCR_TUPLE_INT:
            sub: PyObject = PEEK(1)
            tuple: PyObject = PEEK(2)
            res: PyObject
            assert cframe.use_tracing == 0
            DEOPT_IF(not PyLong_CheckExact(sub), BINARY_SUBSCR)
            DEOPT_IF(not PyTuple_CheckExact(tuple), BINARY_SUBSCR)
            DEOPT_IF(not _PyLong_IsPositiveSingleDigit(sub), BINARY_SUBSCR)
            assert (PyLongObject(_PyLong_GetZero())).ob_digit[0] == 0
            index: Py_ssize_t = (PyLongObject(sub)).ob_digit[0]
            DEOPT_IF(index >= PyTuple_GET_SIZE(tuple), BINARY_SUBSCR)
            STAT_INC(BINARY_SUBSCR, hit)
            res = PyTuple_GET_ITEM(tuple, index)
            assert res != NULL
            Py_INCREF(res)
            _Py_DECREF_SPECIALIZED(sub, destructor(PyObject_Free))
            Py_DECREF(tuple)
            STACK_SHRINK(1)
            POKE(1, res)
            JUMPBY(4)
            DISPATCH()
        case ops.BINARY_SUBSCR_DICT:
            sub: PyObject = PEEK(1)
            dict: PyObject = PEEK(2)
            res: PyObject
            assert cframe.use_tracing == 0
            DEOPT_IF(not PyDict_CheckExact(dict), BINARY_SUBSCR)
            STAT_INC(BINARY_SUBSCR, hit)
            res = PyDict_GetItemWithError(dict, sub)
            if res == NULL:
                if not _PyErr_Occurred(tstate):
                    _PyErr_SetKeyError(sub)
                else:
                    print()
                Py_DECREF(dict)
                Py_DECREF(sub)
                if true:
                    return  # goto pop_2_error
                else:
                    print()
            else:
                print()
            Py_INCREF(res)
            Py_DECREF(dict)
            Py_DECREF(sub)
            STACK_SHRINK(1)
            POKE(1, res)
            JUMPBY(4)
            DISPATCH()
        case ops.BINARY_SUBSCR_GETITEM:
            sub: PyObject = PEEK(1)
            container: PyObject = PEEK(2)
            type_version: uint32_t = read_u32(next_instr[1].cache)
            func_version: uint16_t = read_u16(next_instr[3].cache)
            tp: PyTypeObject = Py_TYPE(container)
            DEOPT_IF(tp.tp_version_tag != type_version, BINARY_SUBSCR)
            assert tp.tp_flags & Py_TPFLAGS_HEAPTYPE
            cached: PyObject = (PyHeapTypeObject(tp))._spec_cache.getitem
            assert PyFunction_Check(cached)
            getitem: PyFunctionObject = PyFunctionObject(cached)
            DEOPT_IF(getitem.func_version != func_version, BINARY_SUBSCR)
            code: PyCodeObject = PyCodeObject(getitem.func_code)
            assert code.co_argcount == 2
            DEOPT_IF(
                not _PyThreadState_HasStackSpace(tstate, code.co_framesize),
                BINARY_SUBSCR,
            )
            STAT_INC(BINARY_SUBSCR, hit)
            Py_INCREF(getitem)
            new_frame: _PyInterpreterFrame = _PyFrame_PushUnchecked(tstate, getitem)
            STACK_SHRINK(2)
            new_frame.localsplus[0] = container
            new_frame.localsplus[1] = sub
            i: int = 2
            while i < code.co_nlocalsplus:
                new_frame.localsplus[i] = NULL
                i += 1
            JUMPBY(INLINE_CACHE_ENTRIES_BINARY_SUBSCR)
            DISPATCH_INLINED(new_frame)
        case ops.LIST_APPEND:
            v: PyObject = PEEK(1)
            list: PyObject = PEEK(oparg + 1)
            if _PyList_AppendTakeRef(PyListObject(list), v) < 0:
                return  # goto pop_1_error
            else:
                print()
            STACK_SHRINK(1)
            PREDICT(JUMP_BACKWARD)
            DISPATCH()
        case ops.SET_ADD:
            v: PyObject = PEEK(1)
            set: PyObject = PEEK(oparg + 1)
            err: int = PySet_Add(set, v)
            Py_DECREF(v)
            if err:
                return  # goto pop_1_error
            else:
                print()
            STACK_SHRINK(1)
            PREDICT(JUMP_BACKWARD)
            DISPATCH()
        case ops.STORE_SUBSCR:
            PREDICTED(STORE_SUBSCR)
            sub: PyObject = PEEK(1)
            container: PyObject = PEEK(2)
            v: PyObject = PEEK(3)
            counter: uint16_t = read_u16(next_instr[0].cache)
            if ADAPTIVE_COUNTER_IS_ZERO(counter):
                assert cframe.use_tracing == 0
                next_instr -= 1
                _Py_Specialize_StoreSubscr(container, sub, next_instr)
                DISPATCH_SAME_OPARG()
            else:
                print()
            STAT_INC(STORE_SUBSCR, deferred)
            cache: _PyStoreSubscrCache = _PyStoreSubscrCache(next_instr)
            DECREMENT_ADAPTIVE_COUNTER(cache.counter)
            err: int = PyObject_SetItem(container, sub, v)
            Py_DECREF(v)
            Py_DECREF(container)
            Py_DECREF(sub)
            if err:
                return  # goto pop_3_error
            else:
                print()
            STACK_SHRINK(3)
            JUMPBY(1)
            DISPATCH()
        case ops.STORE_SUBSCR_LIST_INT:
            sub: PyObject = PEEK(1)
            list: PyObject = PEEK(2)
            value: PyObject = PEEK(3)
            assert cframe.use_tracing == 0
            DEOPT_IF(not PyLong_CheckExact(sub), STORE_SUBSCR)
            DEOPT_IF(not PyList_CheckExact(list), STORE_SUBSCR)
            DEOPT_IF(not _PyLong_IsPositiveSingleDigit(sub), STORE_SUBSCR)
            index: Py_ssize_t = (PyLongObject(sub)).ob_digit[0]
            DEOPT_IF(index >= PyList_GET_SIZE(list), STORE_SUBSCR)
            STAT_INC(STORE_SUBSCR, hit)
            old_value: PyObject = PyList_GET_ITEM(list, index)
            PyList_SET_ITEM(list, index, value)
            assert old_value != NULL
            Py_DECREF(old_value)
            _Py_DECREF_SPECIALIZED(sub, destructor(PyObject_Free))
            Py_DECREF(list)
            STACK_SHRINK(3)
            JUMPBY(1)
            DISPATCH()
        case ops.STORE_SUBSCR_DICT:
            sub: PyObject = PEEK(1)
            dict: PyObject = PEEK(2)
            value: PyObject = PEEK(3)
            assert cframe.use_tracing == 0
            DEOPT_IF(not PyDict_CheckExact(dict), STORE_SUBSCR)
            STAT_INC(STORE_SUBSCR, hit)
            err: int = _PyDict_SetItem_Take2(PyDictObject(dict), sub, value)
            Py_DECREF(dict)
            if err:
                return  # goto pop_3_error
            else:
                print()
            STACK_SHRINK(3)
            JUMPBY(1)
            DISPATCH()
        case ops.DELETE_SUBSCR:
            sub: PyObject = PEEK(1)
            container: PyObject = PEEK(2)
            err: int = PyObject_DelItem(container, sub)
            Py_DECREF(container)
            Py_DECREF(sub)
            if err:
                return  # goto pop_2_error
            else:
                print()
            STACK_SHRINK(2)
            DISPATCH()
        case ops.PRINT_EXPR:
            value: PyObject = PEEK(1)
            hook: PyObject = _PySys_GetAttr(tstate, _Py_ID(displayhook))
            res: PyObject
            if hook == NULL:
                _PyErr_SetString(tstate, PyExc_RuntimeError, "lost sys.displayhook")
                Py_DECREF(value)
                if true:
                    return  # goto pop_1_error
                else:
                    print()
            else:
                print()
            res = PyObject_CallOneArg(hook, value)
            Py_DECREF(value)
            if res == NULL:
                return  # goto pop_1_error
            else:
                print()
            Py_DECREF(res)
            STACK_SHRINK(1)
            DISPATCH()
        case ops.RAISE_VARARGS:
            cause: PyObject = NULL
            exc: PyObject = NULL
            match oparg:
                case 2:
                    cause = POP()
                case 1:
                    exc = POP()
                case 0:
                    if do_raise(tstate, exc, cause):
                        return  # goto exception_unwind
                    else:
                        print()
                    return
                case _:
                    _PyErr_SetString(
                        tstate, PyExc_SystemError, "bad RAISE_VARARGS oparg"
                    )
                    return
            return  # goto error
        case ops.INTERPRETER_EXIT:
            retval: PyObject = PEEK(1)
            assert frame == (entry_frame)
            assert _PyFrame_IsIncomplete(frame)
            STACK_SHRINK(1)
            assert EMPTY()
            tstate.cframe = cframe.previous
            tstate.cframe.use_tracing = cframe.use_tracing
            assert tstate.cframe.current_frame == frame.previous
            assert not _PyErr_Occurred(tstate)
            _Py_LeaveRecursiveCallTstate(tstate)
            return retval
        case ops.RETURN_VALUE:
            retval: PyObject = PEEK(1)
            STACK_SHRINK(1)
            assert EMPTY()
            _PyFrame_SetStackPointer(frame, stack_pointer)
            TRACE_FUNCTION_EXIT()
            DTRACE_FUNCTION_EXIT()
            _Py_LeaveRecursiveCallPy(tstate)
            assert frame != (entry_frame)
            dying: _PyInterpreterFrame = frame
            frame = (
                cframe.current_frame
            ) = dying.previous  # (cframe.current_frame = dying.previous)
            _PyEvalFrameClearAndPop(tstate, dying)
            _PyFrame_StackPush(frame, retval)
            return  # goto resume_frame
        case ops.GET_AITER:
            obj: PyObject = PEEK(1)
            iter: PyObject
            getter: unaryfunc = NULL
            type: PyTypeObject = Py_TYPE(obj)
            if type.tp_as_async != NULL:
                getter = type.tp_as_async.am_aiter
            else:
                print()
            if getter == NULL:
                _PyErr_Format(
                    tstate,
                    PyExc_TypeError,
                    "'async for' requires an object with __aiter__ method, got %.100s",
                    type.tp_name,
                )
                Py_DECREF(obj)
                if true:
                    return  # goto pop_1_error
                else:
                    print()
            else:
                print()
            iter = (getter)(obj)
            Py_DECREF(obj)
            if iter == NULL:
                return  # goto pop_1_error
            else:
                print()
            if (Py_TYPE(iter).tp_as_async == NULL) or (
                Py_TYPE(iter).tp_as_async.am_anext == NULL
            ):
                _PyErr_Format(
                    tstate,
                    PyExc_TypeError,
                    "'async for' received an object from __aiter__ that does not implement __anext__: %.100s",
                    Py_TYPE(iter).tp_name,
                )
                Py_DECREF(iter)
                if true:
                    return  # goto pop_1_error
                else:
                    print()
            else:
                print()
            POKE(1, iter)
            DISPATCH()
        case ops.GET_ANEXT:
            aiter: PyObject = PEEK(1)
            awaitable: PyObject
            getter: unaryfunc = NULL
            next_iter: PyObject = NULL
            type: PyTypeObject = Py_TYPE(aiter)
            if PyAsyncGen_CheckExact(aiter):
                awaitable = type.tp_as_async.am_anext(aiter)
                if awaitable == NULL:
                    return  # goto error
                else:
                    print()
            else:
                if type.tp_as_async != NULL:
                    getter = type.tp_as_async.am_anext
                else:
                    print()
                if getter != NULL:
                    next_iter = (getter)(aiter)
                    if next_iter == NULL:
                        return  # goto error
                    else:
                        print()
                else:
                    _PyErr_Format(
                        tstate,
                        PyExc_TypeError,
                        "'async for' requires an iterator with __anext__ method, got %.100s",
                        type.tp_name,
                    )
                    return  # goto error
                awaitable = _PyCoro_GetAwaitableIter(next_iter)
                if awaitable == NULL:
                    _PyErr_FormatFromCause(
                        PyExc_TypeError,
                        "'async for' received an invalid object from __anext__: %.100s",
                        Py_TYPE(next_iter).tp_name,
                    )
                    Py_DECREF(next_iter)
                    return  # goto error
                else:
                    Py_DECREF(next_iter)
            STACK_GROW(1)
            POKE(1, awaitable)
            PREDICT(LOAD_CONST)
            DISPATCH()
        case ops.GET_AWAITABLE:
            PREDICTED(GET_AWAITABLE)
            iterable: PyObject = PEEK(1)
            iter: PyObject
            iter = _PyCoro_GetAwaitableIter(iterable)
            if iter == NULL:
                format_awaitable_error(tstate, Py_TYPE(iterable), oparg)
            else:
                print()
            Py_DECREF(iterable)
            if (iter != NULL) and PyCoro_CheckExact(iter):
                yf: PyObject = _PyGen_yf(PyGenObject(iter))
                if yf != NULL:
                    Py_DECREF(yf)
                    Py_CLEAR(iter)
                    _PyErr_SetString(
                        tstate, PyExc_RuntimeError, "coroutine is being awaited already"
                    )
                else:
                    print()
            else:
                print()
            if iter == NULL:
                return  # goto pop_1_error
            else:
                print()
            POKE(1, iter)
            PREDICT(LOAD_CONST)
            DISPATCH()
        case ops.SEND:
            assert frame != (entry_frame)
            assert STACK_LEVEL() >= 2
            v: PyObject = POP()
            receiver: PyObject = PEEK(1)
            gen_status: PySendResult
            retval: PyObject
            if tstate.c_tracefunc == NULL:
                gen_status = PyIter_Send(receiver, v, retval)
            else:
                if Py_IsNone(v) and PyIter_Check(receiver):
                    retval = Py_TYPE(receiver).tp_iternext(receiver)
                else:
                    retval = PyObject_CallMethodOneArg(receiver, _Py_ID(send), v)
                if retval == NULL:
                    if (tstate.c_tracefunc != NULL) and _PyErr_ExceptionMatches(
                        tstate, PyExc_StopIteration
                    ):
                        call_exc_trace(
                            tstate.c_tracefunc, tstate.c_traceobj, tstate, frame
                        )
                    else:
                        print()
                    if _PyGen_FetchStopIterationValue(retval) == 0:
                        gen_status = PYGEN_RETURN
                    else:
                        gen_status = PYGEN_ERROR
                else:
                    gen_status = PYGEN_NEXT
            Py_DECREF(v)
            if gen_status == PYGEN_ERROR:
                assert retval == NULL
                return  # goto error
            else:
                print()
            if gen_status == PYGEN_RETURN:
                assert retval != NULL
                Py_DECREF(receiver)
                SET_TOP(retval)
                JUMPBY(oparg)
            else:
                assert gen_status == PYGEN_NEXT
                assert retval != NULL
                PUSH(retval)
            DISPATCH()
        case ops.ASYNC_GEN_WRAP:
            v: PyObject = PEEK(1)
            w: PyObject
            assert frame.f_code.co_flags & CO_ASYNC_GENERATOR
            w = _PyAsyncGenValueWrapperNew(v)
            Py_DECREF(v)
            if w == NULL:
                return  # goto pop_1_error
            else:
                print()
            POKE(1, w)
            DISPATCH()
        case ops.YIELD_VALUE:
            retval: PyObject = PEEK(1)
            assert oparg == STACK_LEVEL()
            assert frame != (entry_frame)
            gen: PyGenObject = _PyFrame_GetGenerator(frame)
            gen.gi_frame_state = FRAME_SUSPENDED
            _PyFrame_SetStackPointer(frame, stack_pointer - 1)
            TRACE_FUNCTION_EXIT()
            DTRACE_FUNCTION_EXIT()
            tstate.exc_info = gen.gi_exc_state.previous_item
            gen.gi_exc_state.previous_item = NULL
            _Py_LeaveRecursiveCallPy(tstate)
            gen_frame: _PyInterpreterFrame = frame
            frame = (
                cframe.current_frame
            ) = frame.previous  # (cframe.current_frame = frame.previous)
            gen_frame.previous = NULL
            frame.prev_instr -= frame.yield_offset
            _PyFrame_StackPush(frame, retval)
            return  # goto resume_frame
        case ops.POP_EXCEPT:
            exc_value: PyObject = PEEK(1)
            exc_info: _PyErr_StackItem = tstate.exc_info
            Py_XSETREF(exc_info.exc_value, exc_value)
            STACK_SHRINK(1)
            DISPATCH()
        case ops.RERAISE:
            if oparg:
                lasti: PyObject = PEEK(oparg + 1)
                if PyLong_Check(lasti):
                    frame.prev_instr = _PyCode_CODE(frame.f_code) + PyLong_AsLong(lasti)
                    assert not _PyErr_Occurred(tstate)
                else:
                    assert PyLong_Check(lasti)
                    _PyErr_SetString(tstate, PyExc_SystemError, "lasti is not an int")
                    return  # goto error
            else:
                print()
            val: PyObject = POP()
            assert val and PyExceptionInstance_Check(val)
            exc: PyObject = Py_NewRef(PyExceptionInstance_Class(val))
            tb: PyObject = PyException_GetTraceback(val)
            _PyErr_Restore(tstate, exc, val, tb)
            return  # goto exception_unwind
        case ops.PREP_RERAISE_STAR:
            excs: PyObject = PEEK(1)
            orig: PyObject = PEEK(2)
            val: PyObject
            assert PyList_Check(excs)
            val = _PyExc_PrepReraiseStar(orig, excs)
            Py_DECREF(orig)
            Py_DECREF(excs)
            if val == NULL:
                return  # goto pop_2_error
            else:
                print()
            STACK_SHRINK(1)
            POKE(1, val)
            DISPATCH()
        case ops.END_ASYNC_FOR:
            val: PyObject = POP()
            assert val and PyExceptionInstance_Check(val)
            if PyErr_GivenExceptionMatches(val, PyExc_StopAsyncIteration):
                Py_DECREF(val)
                Py_DECREF(POP())
            else:
                exc: PyObject = Py_NewRef(PyExceptionInstance_Class(val))
                tb: PyObject = PyException_GetTraceback(val)
                _PyErr_Restore(tstate, exc, val, tb)
                return  # goto exception_unwind
            DISPATCH()
        case ops.CLEANUP_THROW:
            assert throwflag
            exc_value: PyObject = PEEK(1)
            assert exc_value and PyExceptionInstance_Check(exc_value)
            if PyErr_GivenExceptionMatches(exc_value, PyExc_StopIteration):
                value: PyObject = (PyStopIterationObject(exc_value)).value
                Py_INCREF(value)
                Py_DECREF(POP())
                Py_DECREF(POP())
                Py_DECREF(POP())
                PUSH(value)
            else:
                exc_type: PyObject = Py_NewRef(Py_TYPE(exc_value))
                exc_traceback: PyObject = PyException_GetTraceback(exc_value)
                _PyErr_Restore(tstate, exc_type, Py_NewRef(exc_value), exc_traceback)
                return  # goto exception_unwind
            DISPATCH()
        case ops.STOPITERATION_ERROR:
            assert frame.owner == FRAME_OWNED_BY_GENERATOR
            exc: PyObject = PEEK(1)
            assert PyExceptionInstance_Check(exc)
            msg: char = NULL
            if PyErr_GivenExceptionMatches(exc, PyExc_StopIteration):
                msg = "generator raised StopIteration"
                if frame.f_code.co_flags & CO_ASYNC_GENERATOR:
                    msg = "async generator raised StopIteration"
                else:
                    if frame.f_code.co_flags & CO_COROUTINE:
                        msg = "coroutine raised StopIteration"
                    else:
                        print()
            else:
                if (
                    frame.f_code.co_flags & CO_ASYNC_GENERATOR
                ) and PyErr_GivenExceptionMatches(exc, PyExc_StopAsyncIteration):
                    msg = "async generator raised StopAsyncIteration"
                else:
                    print()
            if msg != NULL:
                message: PyObject = _PyUnicode_FromASCII(msg, strlen(msg))
                if message == NULL:
                    return  # goto error
                else:
                    print()
                error: PyObject = PyObject_CallOneArg(PyExc_RuntimeError, message)
                if error == NULL:
                    Py_DECREF(message)
                    return  # goto error
                else:
                    print()
                assert PyExceptionInstance_Check(error)
                SET_TOP(error)
                PyException_SetCause(error, Py_NewRef(exc))
                PyException_SetContext(error, exc)
                Py_DECREF(message)
            else:
                print()
            DISPATCH()
        case ops.LOAD_ASSERTION_ERROR:
            value: PyObject
            value = Py_NewRef(PyExc_AssertionError)
            STACK_GROW(1)
            POKE(1, value)
            DISPATCH()
        case ops.LOAD_BUILD_CLASS:
            bc: PyObject
            if PyDict_CheckExact(BUILTINS()):
                bc = _PyDict_GetItemWithError(BUILTINS(), _Py_ID(__build_class__))
                if bc == NULL:
                    if not _PyErr_Occurred(tstate):
                        _PyErr_SetString(
                            tstate, PyExc_NameError, "__build_class__ not found"
                        )
                    else:
                        print()
                    if true:
                        return  # goto error
                    else:
                        print()
                else:
                    print()
                Py_INCREF(bc)
            else:
                bc = PyObject_GetItem(BUILTINS(), _Py_ID(__build_class__))
                if bc == NULL:
                    if _PyErr_ExceptionMatches(tstate, PyExc_KeyError):
                        _PyErr_SetString(
                            tstate, PyExc_NameError, "__build_class__ not found"
                        )
                    else:
                        print()
                    if true:
                        return  # goto error
                    else:
                        print()
                else:
                    print()
            STACK_GROW(1)
            POKE(1, bc)
            DISPATCH()
        case ops.STORE_NAME:
            v: PyObject = PEEK(1)
            name: PyObject = GETITEM(names, oparg)
            ns: PyObject = LOCALS()
            err: int
            if ns == NULL:
                _PyErr_Format(
                    tstate, PyExc_SystemError, "no locals found when storing %R", name
                )
                Py_DECREF(v)
                if true:
                    return  # goto pop_1_error
                else:
                    print()
            else:
                print()
            if PyDict_CheckExact(ns):
                err = PyDict_SetItem(ns, name, v)
            else:
                err = PyObject_SetItem(ns, name, v)
            Py_DECREF(v)
            if err:
                return  # goto pop_1_error
            else:
                print()
            STACK_SHRINK(1)
            DISPATCH()
        case ops.DELETE_NAME:
            name: PyObject = GETITEM(names, oparg)
            ns: PyObject = LOCALS()
            err: int
            if ns == NULL:
                _PyErr_Format(
                    tstate, PyExc_SystemError, "no locals when deleting %R", name
                )
                return  # goto error
            else:
                print()
            err = PyObject_DelItem(ns, name)
            if err != 0:
                format_exc_check_arg(
                    tstate, PyExc_NameError, "name '%.200s' is not defined", name
                )
                return  # goto error
            else:
                print()
            DISPATCH()
        case ops.UNPACK_SEQUENCE:
            PREDICTED(UNPACK_SEQUENCE)
            cache: _PyUnpackSequenceCache = _PyUnpackSequenceCache(next_instr)
            if ADAPTIVE_COUNTER_IS_ZERO(cache.counter):
                assert cframe.use_tracing == 0
                seq: PyObject = PEEK(1)
                next_instr -= 1
                _Py_Specialize_UnpackSequence(seq, next_instr, oparg)
                DISPATCH_SAME_OPARG()
            else:
                print()
            STAT_INC(UNPACK_SEQUENCE, deferred)
            DECREMENT_ADAPTIVE_COUNTER(cache.counter)
            seq: PyObject = POP()
            top: PyObject = stack_pointer + oparg
            if not unpack_iterable(tstate, seq, oparg, -1, top):
                Py_DECREF(seq)
                return  # goto error
            else:
                print()
            STACK_GROW(oparg)
            Py_DECREF(seq)
            JUMPBY(INLINE_CACHE_ENTRIES_UNPACK_SEQUENCE)
            DISPATCH()
        case ops.UNPACK_SEQUENCE_TWO_TUPLE:
            seq: PyObject = PEEK(1)
            DEOPT_IF(not PyTuple_CheckExact(seq), UNPACK_SEQUENCE)
            DEOPT_IF(PyTuple_GET_SIZE(seq) != 2, UNPACK_SEQUENCE)
            STAT_INC(UNPACK_SEQUENCE, hit)
            SET_TOP(Py_NewRef(PyTuple_GET_ITEM(seq, 1)))
            PUSH(Py_NewRef(PyTuple_GET_ITEM(seq, 0)))
            Py_DECREF(seq)
            JUMPBY(INLINE_CACHE_ENTRIES_UNPACK_SEQUENCE)
            DISPATCH()
        case ops.UNPACK_SEQUENCE_TUPLE:
            seq: PyObject = PEEK(1)
            DEOPT_IF(not PyTuple_CheckExact(seq), UNPACK_SEQUENCE)
            DEOPT_IF(PyTuple_GET_SIZE(seq) != oparg, UNPACK_SEQUENCE)
            STAT_INC(UNPACK_SEQUENCE, hit)
            STACK_SHRINK(1)
            items: PyObject = _PyTuple_ITEMS(seq)
            while oparg > 0:
                PUSH(Py_NewRef(items[oparg]))
                oparg -= 1
            Py_DECREF(seq)
            JUMPBY(INLINE_CACHE_ENTRIES_UNPACK_SEQUENCE)
            DISPATCH()
        case ops.UNPACK_SEQUENCE_LIST:
            seq: PyObject = PEEK(1)
            DEOPT_IF(not PyList_CheckExact(seq), UNPACK_SEQUENCE)
            DEOPT_IF(PyList_GET_SIZE(seq) != oparg, UNPACK_SEQUENCE)
            STAT_INC(UNPACK_SEQUENCE, hit)
            STACK_SHRINK(1)
            items: PyObject = _PyList_ITEMS(seq)
            while oparg > 0:
                PUSH(Py_NewRef(items[oparg]))
                oparg -= 1
            Py_DECREF(seq)
            JUMPBY(INLINE_CACHE_ENTRIES_UNPACK_SEQUENCE)
            DISPATCH()
        case ops.UNPACK_EX:
            totalargs: int = (1 + (oparg & 0xFF)) + (oparg >> 8)
            seq: PyObject = POP()
            top: PyObject = stack_pointer + totalargs
            oparg = oparg >> 8
            if not unpack_iterable(tstate, seq, oparg & 0xFF, oparg, top):
                Py_DECREF(seq)
                return  # goto error
            else:
                print()
            STACK_GROW(totalargs)
            Py_DECREF(seq)
            DISPATCH()
        case ops.STORE_ATTR:
            PREDICTED(STORE_ATTR)
            owner: PyObject = PEEK(1)
            v: PyObject = PEEK(2)
            counter: uint16_t = read_u16(next_instr[0].cache)
            if ADAPTIVE_COUNTER_IS_ZERO(counter):
                assert cframe.use_tracing == 0
                name: PyObject = GETITEM(names, oparg)
                next_instr -= 1
                _Py_Specialize_StoreAttr(owner, next_instr, name)
                DISPATCH_SAME_OPARG()
            else:
                print()
            STAT_INC(STORE_ATTR, deferred)
            cache: _PyAttrCache = _PyAttrCache(next_instr)
            DECREMENT_ADAPTIVE_COUNTER(cache.counter)
            name: PyObject = GETITEM(names, oparg)
            err: int = PyObject_SetAttr(owner, name, v)
            Py_DECREF(v)
            Py_DECREF(owner)
            if err:
                return  # goto pop_2_error
            else:
                print()
            STACK_SHRINK(2)
            JUMPBY(4)
            DISPATCH()
        case ops.DELETE_ATTR:
            owner: PyObject = PEEK(1)
            name: PyObject = GETITEM(names, oparg)
            err: int = PyObject_SetAttr(owner, name, PyObject(NULL))
            Py_DECREF(owner)
            if err:
                return  # goto pop_1_error
            else:
                print()
            STACK_SHRINK(1)
            DISPATCH()
        case ops.STORE_GLOBAL:
            v: PyObject = PEEK(1)
            name: PyObject = GETITEM(names, oparg)
            err: int = PyDict_SetItem(GLOBALS(), name, v)
            Py_DECREF(v)
            if err:
                return  # goto pop_1_error
            else:
                print()
            STACK_SHRINK(1)
            DISPATCH()
        case ops.DELETE_GLOBAL:
            name: PyObject = GETITEM(names, oparg)
            err: int
            err = PyDict_DelItem(GLOBALS(), name)
            if err != 0:
                if _PyErr_ExceptionMatches(tstate, PyExc_KeyError):
                    format_exc_check_arg(
                        tstate, PyExc_NameError, "name '%.200s' is not defined", name
                    )
                else:
                    print()
                return  # goto error
            else:
                print()
            DISPATCH()
        case ops.LOAD_NAME:
            v: PyObject
            name: PyObject = GETITEM(names, oparg)
            locals: PyObject = LOCALS()
            if locals == NULL:
                _PyErr_Format(
                    tstate, PyExc_SystemError, "no locals when loading %R", name
                )
                return  # goto error
            else:
                print()
            if PyDict_CheckExact(locals):
                v = PyDict_GetItemWithError(locals, name)
                if v != NULL:
                    Py_INCREF(v)
                else:
                    if _PyErr_Occurred(tstate):
                        return  # goto error
                    else:
                        print()
            else:
                v = PyObject_GetItem(locals, name)
                if v == NULL:
                    if not _PyErr_ExceptionMatches(tstate, PyExc_KeyError):
                        return  # goto error
                    else:
                        print()
                    _PyErr_Clear(tstate)
                else:
                    print()
            if v == NULL:
                v = PyDict_GetItemWithError(GLOBALS(), name)
                if v != NULL:
                    Py_INCREF(v)
                else:
                    if _PyErr_Occurred(tstate):
                        return  # goto error
                    else:
                        if PyDict_CheckExact(BUILTINS()):
                            v = PyDict_GetItemWithError(BUILTINS(), name)
                            if v == NULL:
                                if not _PyErr_Occurred(tstate):
                                    format_exc_check_arg(
                                        tstate,
                                        PyExc_NameError,
                                        "name '%.200s' is not defined",
                                        name,
                                    )
                                else:
                                    print()
                                return  # goto error
                            else:
                                print()
                            Py_INCREF(v)
                        else:
                            v = PyObject_GetItem(BUILTINS(), name)
                            if v == NULL:
                                if _PyErr_ExceptionMatches(tstate, PyExc_KeyError):
                                    format_exc_check_arg(
                                        tstate,
                                        PyExc_NameError,
                                        "name '%.200s' is not defined",
                                        name,
                                    )
                                else:
                                    print()
                                return  # goto error
                            else:
                                print()
            else:
                print()
            STACK_GROW(1)
            POKE(1, v)
            DISPATCH()
        case ops.LOAD_GLOBAL:
            PREDICTED(LOAD_GLOBAL)
            cache: _PyLoadGlobalCache = _PyLoadGlobalCache(next_instr)
            if ADAPTIVE_COUNTER_IS_ZERO(cache.counter):
                assert cframe.use_tracing == 0
                oparg = oparg >> 1
                name: PyObject = GETITEM(names, oparg)
                next_instr -= 1
                _Py_Specialize_LoadGlobal(GLOBALS(), BUILTINS(), next_instr, name)
                DISPATCH_SAME_OPARG()
            else:
                print()
            STAT_INC(LOAD_GLOBAL, deferred)
            DECREMENT_ADAPTIVE_COUNTER(cache.counter)
            push_null: int = oparg & 1
            # PEEK(0) = NULL
            oparg = oparg >> 1
            name: PyObject = GETITEM(names, oparg)
            v: PyObject
            if PyDict_CheckExact(GLOBALS()) and PyDict_CheckExact(BUILTINS()):
                v = _PyDict_LoadGlobal(
                    PyDictObject(GLOBALS()), PyDictObject(BUILTINS()), name
                )
                if v == NULL:
                    if not _PyErr_Occurred(tstate):
                        format_exc_check_arg(
                            tstate,
                            PyExc_NameError,
                            "name '%.200s' is not defined",
                            name,
                        )
                    else:
                        print()
                    return  # goto error
                else:
                    print()
                Py_INCREF(v)
            else:
                v = PyObject_GetItem(GLOBALS(), name)
                if v == NULL:
                    if not _PyErr_ExceptionMatches(tstate, PyExc_KeyError):
                        return  # goto error
                    else:
                        print()
                    _PyErr_Clear(tstate)
                    v = PyObject_GetItem(BUILTINS(), name)
                    if v == NULL:
                        if _PyErr_ExceptionMatches(tstate, PyExc_KeyError):
                            format_exc_check_arg(
                                tstate,
                                PyExc_NameError,
                                "name '%.200s' is not defined",
                                name,
                            )
                        else:
                            print()
                        return  # goto error
                    else:
                        print()
                else:
                    print()
            JUMPBY(INLINE_CACHE_ENTRIES_LOAD_GLOBAL)
            STACK_GROW(push_null)
            PUSH(v)
            DISPATCH()
        case ops.LOAD_GLOBAL_MODULE:
            assert cframe.use_tracing == 0
            DEOPT_IF(not PyDict_CheckExact(GLOBALS()), LOAD_GLOBAL)
            dict: PyDictObject = PyDictObject(GLOBALS())
            cache: _PyLoadGlobalCache = _PyLoadGlobalCache(next_instr)
            version: uint32_t = read_u32(cache.module_keys_version)
            DEOPT_IF(dict.ma_keys.dk_version != version, LOAD_GLOBAL)
            assert DK_IS_UNICODE(dict.ma_keys)
            entries: PyDictUnicodeEntry = DK_UNICODE_ENTRIES(dict.ma_keys)
            res: PyObject = entries[cache.index].me_value
            DEOPT_IF(res == NULL, LOAD_GLOBAL)
            push_null: int = oparg & 1
            # PEEK(0) = NULL
            JUMPBY(INLINE_CACHE_ENTRIES_LOAD_GLOBAL)
            STAT_INC(LOAD_GLOBAL, hit)
            STACK_GROW(push_null + 1)
            SET_TOP(Py_NewRef(res))
            DISPATCH()
        case ops.LOAD_GLOBAL_BUILTIN:
            assert cframe.use_tracing == 0
            DEOPT_IF(not PyDict_CheckExact(GLOBALS()), LOAD_GLOBAL)
            DEOPT_IF(not PyDict_CheckExact(BUILTINS()), LOAD_GLOBAL)
            mdict: PyDictObject = PyDictObject(GLOBALS())
            bdict: PyDictObject = PyDictObject(BUILTINS())
            cache: _PyLoadGlobalCache = _PyLoadGlobalCache(next_instr)
            mod_version: uint32_t = read_u32(cache.module_keys_version)
            bltn_version: uint16_t = cache.builtin_keys_version
            DEOPT_IF(mdict.ma_keys.dk_version != mod_version, LOAD_GLOBAL)
            DEOPT_IF(bdict.ma_keys.dk_version != bltn_version, LOAD_GLOBAL)
            assert DK_IS_UNICODE(bdict.ma_keys)
            entries: PyDictUnicodeEntry = DK_UNICODE_ENTRIES(bdict.ma_keys)
            res: PyObject = entries[cache.index].me_value
            DEOPT_IF(res == NULL, LOAD_GLOBAL)
            push_null: int = oparg & 1
            # PEEK(0) = NULL
            JUMPBY(INLINE_CACHE_ENTRIES_LOAD_GLOBAL)
            STAT_INC(LOAD_GLOBAL, hit)
            STACK_GROW(push_null + 1)
            SET_TOP(Py_NewRef(res))
            DISPATCH()
        case ops.DELETE_FAST:
            v: PyObject = frame.localsplus[oparg]
            if v == NULL:
                return  # goto unbound_local_error
            else:
                print()
            SETLOCAL(oparg, NULL)
            DISPATCH()
        case ops.MAKE_CELL:
            initial: PyObject = frame.localsplus[oparg]
            cell: PyObject = PyCell_New(initial)
            if cell == NULL:
                return  # goto resume_with_error
            else:
                print()
            SETLOCAL(oparg, cell)
            DISPATCH()
        case ops.DELETE_DEREF:
            cell: PyObject = frame.localsplus[oparg]
            oldobj: PyObject = PyCell_GET(cell)
            if oldobj == NULL:
                format_exc_unbound(tstate, frame.f_code, oparg)
                return  # goto error
            else:
                print()
            PyCell_SET(cell, NULL)
            Py_DECREF(oldobj)
            DISPATCH()
        case ops.LOAD_CLASSDEREF:
            value: PyObject
            name: PyObject
            locals: PyObject = LOCALS()
            assert locals
            assert (oparg >= 0) and (oparg < frame.f_code.co_nlocalsplus)
            name = PyTuple_GET_ITEM(frame.f_code.co_localsplusnames, oparg)
            if PyDict_CheckExact(locals):
                value = PyDict_GetItemWithError(locals, name)
                if value != NULL:
                    Py_INCREF(value)
                else:
                    if _PyErr_Occurred(tstate):
                        return  # goto error
                    else:
                        print()
            else:
                value = PyObject_GetItem(locals, name)
                if value == NULL:
                    if not _PyErr_ExceptionMatches(tstate, PyExc_KeyError):
                        return  # goto error
                    else:
                        print()
                    _PyErr_Clear(tstate)
                else:
                    print()
            if not value:
                cell: PyObject = frame.localsplus[oparg]
                value = PyCell_GET(cell)
                if value == NULL:
                    format_exc_unbound(tstate, frame.f_code, oparg)
                    return  # goto error
                else:
                    print()
                Py_INCREF(value)
            else:
                print()
            STACK_GROW(1)
            POKE(1, value)
            DISPATCH()
        case ops.LOAD_DEREF:
            value: PyObject
            cell: PyObject = frame.localsplus[oparg]
            value = PyCell_GET(cell)
            if value == NULL:
                format_exc_unbound(tstate, frame.f_code, oparg)
                if true:
                    return  # goto error
                else:
                    print()
            else:
                print()
            Py_INCREF(value)
            STACK_GROW(1)
            POKE(1, value)
            DISPATCH()
        case ops.STORE_DEREF:
            v: PyObject = PEEK(1)
            cell: PyObject = frame.localsplus[oparg]
            oldobj: PyObject = PyCell_GET(cell)
            PyCell_SET(cell, v)
            Py_XDECREF(oldobj)
            STACK_SHRINK(1)
            DISPATCH()
        case ops.COPY_FREE_VARS:
            co: PyCodeObject = frame.f_code
            assert PyFunction_Check(frame.f_funcobj)
            closure: PyObject = (PyFunctionObject(frame.f_funcobj)).func_closure
            assert oparg == co.co_nfreevars
            offset: int = co.co_nlocalsplus - oparg
            i: int = 0
            while i < oparg:
                o: PyObject = PyTuple_GET_ITEM(closure, i)
                frame.localsplus[offset + i] = Py_NewRef(o)
                ++i
            DISPATCH()
        case ops.BUILD_STRING:
            str: PyObject
            str = _PyUnicode_JoinArray(_Py_STR(empty), stack_pointer - oparg, oparg)
            if str == NULL:
                return  # goto error
            else:
                print()
            while (--oparg) >= 0:
                item: PyObject = POP()
                Py_DECREF(item)
                (--oparg) >= 0
            PUSH(str)
            DISPATCH()
        case ops.BUILD_TUPLE:
            STACK_SHRINK(oparg)
            tup: PyObject = _PyTuple_FromArraySteal(stack_pointer, oparg)
            if tup == NULL:
                return  # goto error
            else:
                print()
            PUSH(tup)
            DISPATCH()
        case ops.BUILD_LIST:
            STACK_SHRINK(oparg)
            list: PyObject = _PyList_FromArraySteal(stack_pointer, oparg)
            if list == NULL:
                return  # goto error
            else:
                print()
            PUSH(list)
            DISPATCH()
        case ops.LIST_TO_TUPLE:
            list: PyObject = PEEK(1)
            tuple: PyObject
            tuple = PyList_AsTuple(list)
            Py_DECREF(list)
            if tuple == NULL:
                return  # goto pop_1_error
            else:
                print()
            POKE(1, tuple)
            DISPATCH()
        case ops.LIST_EXTEND:
            iterable: PyObject = PEEK(1)
            list: PyObject = PEEK(oparg + 1)
            none_val: PyObject = _PyList_Extend(PyListObject(list), iterable)
            if none_val == NULL:
                if _PyErr_ExceptionMatches(tstate, PyExc_TypeError) and (
                    (Py_TYPE(iterable).tp_iter == NULL)
                    and (not PySequence_Check(iterable))
                ):
                    _PyErr_Clear(tstate)
                    _PyErr_Format(
                        tstate,
                        PyExc_TypeError,
                        "Value after * must be an iterable, not %.200s",
                        Py_TYPE(iterable).tp_name,
                    )
                else:
                    print()
                Py_DECREF(iterable)
                if true:
                    return  # goto pop_1_error
                else:
                    print()
            else:
                print()
            Py_DECREF(none_val)
            Py_DECREF(iterable)
            STACK_SHRINK(1)
            DISPATCH()
        case ops.SET_UPDATE:
            iterable: PyObject = PEEK(1)
            set: PyObject = PEEK(oparg + 1)
            err: int = _PySet_Update(set, iterable)
            Py_DECREF(iterable)
            if err < 0:
                return  # goto pop_1_error
            else:
                print()
            STACK_SHRINK(1)
            DISPATCH()
        case ops.BUILD_SET:
            set: PyObject = PySet_New(NULL)
            err: int = 0
            i: int
            if set == NULL:
                return  # goto error
            else:
                print()
            i = oparg
            while i > 0:
                item: PyObject = PEEK(i)
                if err == 0:
                    err = PySet_Add(set, item)
                else:
                    print()
                Py_DECREF(item)
                i -= 1
            STACK_SHRINK(oparg)
            if err != 0:
                Py_DECREF(set)
                return  # goto error
            else:
                print()
            PUSH(set)
            DISPATCH()
        case ops.BUILD_MAP:
            map: PyObject = _PyDict_FromItems(
                PEEK(2 * oparg), 2, PEEK((2 * oparg) - 1), 2, oparg
            )
            if map == NULL:
                return  # goto error
            else:
                print()
            while oparg > 0:
                Py_DECREF(POP())
                Py_DECREF(POP())
                oparg -= 1
            PUSH(map)
            DISPATCH()
        case ops.SETUP_ANNOTATIONS:
            err: int
            ann_dict: PyObject
            if LOCALS() == NULL:
                _PyErr_Format(
                    tstate,
                    PyExc_SystemError,
                    "no locals found when setting up annotations",
                )
                if true:
                    return  # goto error
                else:
                    print()
            else:
                print()
            if PyDict_CheckExact(LOCALS()):
                ann_dict = _PyDict_GetItemWithError(LOCALS(), _Py_ID(__annotations__))
                if ann_dict == NULL:
                    if _PyErr_Occurred(tstate):
                        return  # goto error
                    else:
                        print()
                    ann_dict = PyDict_New()
                    if ann_dict == NULL:
                        return  # goto error
                    else:
                        print()
                    err = PyDict_SetItem(LOCALS(), _Py_ID(__annotations__), ann_dict)
                    Py_DECREF(ann_dict)
                    if err:
                        return  # goto error
                    else:
                        print()
                else:
                    print()
            else:
                ann_dict = PyObject_GetItem(LOCALS(), _Py_ID(__annotations__))
                if ann_dict == NULL:
                    if not _PyErr_ExceptionMatches(tstate, PyExc_KeyError):
                        return  # goto error
                    else:
                        print()
                    _PyErr_Clear(tstate)
                    ann_dict = PyDict_New()
                    if ann_dict == NULL:
                        return  # goto error
                    else:
                        print()
                    err = PyObject_SetItem(LOCALS(), _Py_ID(__annotations__), ann_dict)
                    Py_DECREF(ann_dict)
                    if err:
                        return  # goto error
                    else:
                        print()
                else:
                    Py_DECREF(ann_dict)
            DISPATCH()
        case ops.BUILD_CONST_KEY_MAP:
            map: PyObject
            keys: PyObject = PEEK(1)
            if (not PyTuple_CheckExact(keys)) or (
                PyTuple_GET_SIZE(keys) != (Py_ssize_t(oparg))
            ):
                _PyErr_SetString(
                    tstate, PyExc_SystemError, "bad BUILD_CONST_KEY_MAP keys argument"
                )
                return  # goto error
            else:
                print()
            map = _PyDict_FromItems(
                PyTuple_GET_ITEM(keys, 0), 1, PEEK(oparg + 1), 1, oparg
            )
            if map == NULL:
                return  # goto error
            else:
                print()
            Py_DECREF(POP())
            while oparg > 0:
                Py_DECREF(POP())
                oparg -= 1
            PUSH(map)
            DISPATCH()
        case ops.DICT_UPDATE:
            update: PyObject = PEEK(1)
            dict: PyObject = PEEK(oparg + 1)
            if PyDict_Update(dict, update) < 0:
                if _PyErr_ExceptionMatches(tstate, PyExc_AttributeError):
                    _PyErr_Format(
                        tstate,
                        PyExc_TypeError,
                        "'%.200s' object is not a mapping",
                        Py_TYPE(update).tp_name,
                    )
                else:
                    print()
                Py_DECREF(update)
                if true:
                    return  # goto pop_1_error
                else:
                    print()
            else:
                print()
            Py_DECREF(update)
            STACK_SHRINK(1)
            DISPATCH()
        case ops.DICT_MERGE:
            update: PyObject = PEEK(1)
            dict: PyObject = PEEK(oparg + 1)
            if _PyDict_MergeEx(dict, update, 2) < 0:
                format_kwargs_error(tstate, PEEK(3 + oparg), update)
                Py_DECREF(update)
                if true:
                    return  # goto pop_1_error
                else:
                    print()
            else:
                print()
            Py_DECREF(update)
            STACK_SHRINK(1)
            PREDICT(CALL_FUNCTION_EX)
            DISPATCH()
        case ops.MAP_ADD:
            value: PyObject = PEEK(1)
            key: PyObject = PEEK(2)
            dict: PyObject = PEEK(oparg + 2)
            assert PyDict_CheckExact(dict)
            if _PyDict_SetItem_Take2(PyDictObject(dict), key, value) != 0:
                return  # goto pop_2_error
            else:
                print()
            STACK_SHRINK(2)
            PREDICT(JUMP_BACKWARD)
            DISPATCH()
        case ops.LOAD_ATTR:
            PREDICTED(LOAD_ATTR)
            cache: _PyAttrCache = _PyAttrCache(next_instr)
            if ADAPTIVE_COUNTER_IS_ZERO(cache.counter):
                assert cframe.use_tracing == 0
                owner: PyObject = PEEK(1)
                oparg = oparg >> 1
                name: PyObject = GETITEM(names, oparg)
                next_instr -= 1
                _Py_Specialize_LoadAttr(owner, next_instr, name)
                DISPATCH_SAME_OPARG()
            else:
                print()
            STAT_INC(LOAD_ATTR, deferred)
            DECREMENT_ADAPTIVE_COUNTER(cache.counter)
            oparg = oparg >> 1
            name: PyObject = GETITEM(names, oparg)
            owner: PyObject = PEEK(1)
            if oparg & 1:
                meth: PyObject = NULL
                meth_found: int = _PyObject_GetMethod(owner, name, meth)
                if meth == NULL:
                    return  # goto error
                else:
                    print()
                if meth_found:
                    SET_TOP(meth)
                    PUSH(owner)
                else:
                    SET_TOP(NULL)
                    Py_DECREF(owner)
                    PUSH(meth)
            else:
                res: PyObject = PyObject_GetAttr(owner, name)
                if res == NULL:
                    return  # goto error
                else:
                    print()
                Py_DECREF(owner)
                SET_TOP(res)
            JUMPBY(INLINE_CACHE_ENTRIES_LOAD_ATTR)
            DISPATCH()
        case ops.LOAD_ATTR_INSTANCE_VALUE:
            assert cframe.use_tracing == 0
            owner: PyObject = PEEK(1)
            res: PyObject
            tp: PyTypeObject = Py_TYPE(owner)
            cache: _PyAttrCache = _PyAttrCache(next_instr)
            type_version: uint32_t = read_u32(cache.version)
            assert type_version != 0
            DEOPT_IF(tp.tp_version_tag != type_version, LOAD_ATTR)
            assert tp.tp_dictoffset < 0
            assert tp.tp_flags & Py_TPFLAGS_MANAGED_DICT
            dorv: PyDictOrValues = _PyObject_DictOrValuesPointer(owner)
            DEOPT_IF(not _PyDictOrValues_IsValues(dorv), LOAD_ATTR)
            res = _PyDictOrValues_GetValues(dorv).values[cache.index]
            DEOPT_IF(res == NULL, LOAD_ATTR)
            STAT_INC(LOAD_ATTR, hit)
            Py_INCREF(res)
            SET_TOP(NULL)
            STACK_GROW(oparg & 1)
            SET_TOP(res)
            Py_DECREF(owner)
            JUMPBY(INLINE_CACHE_ENTRIES_LOAD_ATTR)
            DISPATCH()
        case ops.LOAD_ATTR_MODULE:
            assert cframe.use_tracing == 0
            owner: PyObject = PEEK(1)
            res: PyObject
            cache: _PyAttrCache = _PyAttrCache(next_instr)
            DEOPT_IF(not PyModule_CheckExact(owner), LOAD_ATTR)
            dict: PyDictObject = PyDictObject((PyModuleObject(owner)).md_dict)
            assert dict != NULL
            DEOPT_IF(dict.ma_keys.dk_version != read_u32(cache.version), LOAD_ATTR)
            assert dict.ma_keys.dk_kind == DICT_KEYS_UNICODE
            assert cache.index < dict.ma_keys.dk_nentries
            ep: PyDictUnicodeEntry = DK_UNICODE_ENTRIES(dict.ma_keys) + cache.index
            res = ep.me_value
            DEOPT_IF(res == NULL, LOAD_ATTR)
            STAT_INC(LOAD_ATTR, hit)
            Py_INCREF(res)
            SET_TOP(NULL)
            STACK_GROW(oparg & 1)
            SET_TOP(res)
            Py_DECREF(owner)
            JUMPBY(INLINE_CACHE_ENTRIES_LOAD_ATTR)
            DISPATCH()
        case ops.LOAD_ATTR_WITH_HINT:
            assert cframe.use_tracing == 0
            owner: PyObject = PEEK(1)
            res: PyObject
            tp: PyTypeObject = Py_TYPE(owner)
            cache: _PyAttrCache = _PyAttrCache(next_instr)
            type_version: uint32_t = read_u32(cache.version)
            assert type_version != 0
            DEOPT_IF(tp.tp_version_tag != type_version, LOAD_ATTR)
            assert tp.tp_flags & Py_TPFLAGS_MANAGED_DICT
            dorv: PyDictOrValues = _PyObject_DictOrValuesPointer(owner)
            DEOPT_IF(_PyDictOrValues_IsValues(dorv), LOAD_ATTR)
            dict: PyDictObject = PyDictObject(_PyDictOrValues_GetDict(dorv))
            DEOPT_IF(dict == NULL, LOAD_ATTR)
            assert PyDict_CheckExact(PyObject(dict))
            oparg = oparg >> 1
            name: PyObject = GETITEM(names, oparg)
            hint: uint16_t = cache.index
            DEOPT_IF(hint >= (size_t(dict.ma_keys.dk_nentries)), LOAD_ATTR)
            if DK_IS_UNICODE(dict.ma_keys):
                ep: PyDictUnicodeEntry = DK_UNICODE_ENTRIES(dict.ma_keys) + hint
                DEOPT_IF(ep.me_key != name, LOAD_ATTR)
                res = ep.me_value
            else:
                ep: PyDictKeyEntry = DK_ENTRIES(dict.ma_keys) + hint
                DEOPT_IF(ep.me_key != name, LOAD_ATTR)
                res = ep.me_value
            DEOPT_IF(res == NULL, LOAD_ATTR)
            STAT_INC(LOAD_ATTR, hit)
            Py_INCREF(res)
            SET_TOP(NULL)
            STACK_GROW(oparg & 1)
            SET_TOP(res)
            Py_DECREF(owner)
            JUMPBY(INLINE_CACHE_ENTRIES_LOAD_ATTR)
            DISPATCH()
        case ops.LOAD_ATTR_SLOT:
            assert cframe.use_tracing == 0
            owner: PyObject = PEEK(1)
            res: PyObject
            tp: PyTypeObject = Py_TYPE(owner)
            cache: _PyAttrCache = _PyAttrCache(next_instr)
            type_version: uint32_t = read_u32(cache.version)
            assert type_version != 0
            DEOPT_IF(tp.tp_version_tag != type_version, LOAD_ATTR)
            addr: char = (char(owner)) + cache.index
            res = PyObject(addr)
            DEOPT_IF(res == NULL, LOAD_ATTR)
            STAT_INC(LOAD_ATTR, hit)
            Py_INCREF(res)
            SET_TOP(NULL)
            STACK_GROW(oparg & 1)
            SET_TOP(res)
            Py_DECREF(owner)
            JUMPBY(INLINE_CACHE_ENTRIES_LOAD_ATTR)
            DISPATCH()
        case ops.LOAD_ATTR_CLASS:
            assert cframe.use_tracing == 0
            cache: _PyLoadMethodCache = _PyLoadMethodCache(next_instr)
            cls: PyObject = PEEK(1)
            DEOPT_IF(not PyType_Check(cls), LOAD_ATTR)
            type_version: uint32_t = read_u32(cache.type_version)
            DEOPT_IF((PyTypeObject(cls)).tp_version_tag != type_version, LOAD_ATTR)
            assert type_version != 0
            STAT_INC(LOAD_ATTR, hit)
            res: PyObject = read_obj(cache.descr)
            assert res != NULL
            Py_INCREF(res)
            SET_TOP(NULL)
            STACK_GROW(oparg & 1)
            SET_TOP(res)
            Py_DECREF(cls)
            JUMPBY(INLINE_CACHE_ENTRIES_LOAD_ATTR)
            DISPATCH()
        case ops.LOAD_ATTR_PROPERTY:
            assert cframe.use_tracing == 0
            DEOPT_IF(tstate.interp.eval_frame, LOAD_ATTR)
            cache: _PyLoadMethodCache = _PyLoadMethodCache(next_instr)
            owner: PyObject = PEEK(1)
            cls: PyTypeObject = Py_TYPE(owner)
            type_version: uint32_t = read_u32(cache.type_version)
            DEOPT_IF(cls.tp_version_tag != type_version, LOAD_ATTR)
            assert type_version != 0
            fget: PyObject = read_obj(cache.descr)
            assert Py_IS_TYPE(fget, PyFunction_Type)
            f: PyFunctionObject = PyFunctionObject(fget)
            func_version: uint32_t = read_u32(cache.keys_version)
            assert func_version != 0
            DEOPT_IF(f.func_version != func_version, LOAD_ATTR)
            code: PyCodeObject = PyCodeObject(f.func_code)
            assert code.co_argcount == 1
            DEOPT_IF(
                not _PyThreadState_HasStackSpace(tstate, code.co_framesize), LOAD_ATTR
            )
            STAT_INC(LOAD_ATTR, hit)
            Py_INCREF(fget)
            new_frame: _PyInterpreterFrame = _PyFrame_PushUnchecked(tstate, f)
            SET_TOP(NULL)
            shrink_stack: int = not (oparg & 1)
            STACK_SHRINK(shrink_stack)
            new_frame.localsplus[0] = owner
            i: int = 1
            while i < code.co_nlocalsplus:
                new_frame.localsplus[i] = NULL
                i += 1
            JUMPBY(INLINE_CACHE_ENTRIES_LOAD_ATTR)
            DISPATCH_INLINED(new_frame)
        case ops.LOAD_ATTR_GETATTRIBUTE_OVERRIDDEN:
            assert cframe.use_tracing == 0
            DEOPT_IF(tstate.interp.eval_frame, LOAD_ATTR)
            cache: _PyLoadMethodCache = _PyLoadMethodCache(next_instr)
            owner: PyObject = PEEK(1)
            cls: PyTypeObject = Py_TYPE(owner)
            type_version: uint32_t = read_u32(cache.type_version)
            DEOPT_IF(cls.tp_version_tag != type_version, LOAD_ATTR)
            assert type_version != 0
            getattribute: PyObject = read_obj(cache.descr)
            assert Py_IS_TYPE(getattribute, PyFunction_Type)
            f: PyFunctionObject = PyFunctionObject(getattribute)
            func_version: uint32_t = read_u32(cache.keys_version)
            assert func_version != 0
            DEOPT_IF(f.func_version != func_version, LOAD_ATTR)
            code: PyCodeObject = PyCodeObject(f.func_code)
            assert code.co_argcount == 2
            DEOPT_IF(
                not _PyThreadState_HasStackSpace(tstate, code.co_framesize), LOAD_ATTR
            )
            STAT_INC(LOAD_ATTR, hit)
            oparg = oparg >> 1
            name: PyObject = GETITEM(names, oparg)
            Py_INCREF(f)
            new_frame: _PyInterpreterFrame = _PyFrame_PushUnchecked(tstate, f)
            SET_TOP(NULL)
            shrink_stack: int = not (oparg & 1)
            STACK_SHRINK(shrink_stack)
            new_frame.localsplus[0] = owner
            new_frame.localsplus[1] = Py_NewRef(name)
            i: int = 2
            while i < code.co_nlocalsplus:
                new_frame.localsplus[i] = NULL
                i += 1
            JUMPBY(INLINE_CACHE_ENTRIES_LOAD_ATTR)
            DISPATCH_INLINED(new_frame)
        case ops.STORE_ATTR_INSTANCE_VALUE:
            owner: PyObject = PEEK(1)
            value: PyObject = PEEK(2)
            type_version: uint32_t = read_u32(next_instr[1].cache)
            index: uint16_t = read_u16(next_instr[3].cache)
            assert cframe.use_tracing == 0
            tp: PyTypeObject = Py_TYPE(owner)
            assert type_version != 0
            DEOPT_IF(tp.tp_version_tag != type_version, STORE_ATTR)
            assert tp.tp_flags & Py_TPFLAGS_MANAGED_DICT
            dorv: PyDictOrValues = _PyObject_DictOrValuesPointer(owner)
            DEOPT_IF(not _PyDictOrValues_IsValues(dorv), STORE_ATTR)
            STAT_INC(STORE_ATTR, hit)
            values: PyDictValues = _PyDictOrValues_GetValues(dorv)
            old_value: PyObject = values.values[index]
            values.values[index] = value
            if old_value == NULL:
                _PyDictValues_AddToInsertionOrder(values, index)
            else:
                Py_DECREF(old_value)
            Py_DECREF(owner)
            STACK_SHRINK(2)
            JUMPBY(4)
            DISPATCH()
        case ops.STORE_ATTR_WITH_HINT:
            owner: PyObject = PEEK(1)
            value: PyObject = PEEK(2)
            type_version: uint32_t = read_u32(next_instr[1].cache)
            hint: uint16_t = read_u16(next_instr[3].cache)
            assert cframe.use_tracing == 0
            tp: PyTypeObject = Py_TYPE(owner)
            assert type_version != 0
            DEOPT_IF(tp.tp_version_tag != type_version, STORE_ATTR)
            assert tp.tp_flags & Py_TPFLAGS_MANAGED_DICT
            dorv: PyDictOrValues = _PyObject_DictOrValuesPointer(owner)
            DEOPT_IF(_PyDictOrValues_IsValues(dorv), STORE_ATTR)
            dict: PyDictObject = PyDictObject(_PyDictOrValues_GetDict(dorv))
            DEOPT_IF(dict == NULL, STORE_ATTR)
            assert PyDict_CheckExact(PyObject(dict))
            name: PyObject = GETITEM(names, oparg)
            DEOPT_IF(hint >= (size_t(dict.ma_keys.dk_nentries)), STORE_ATTR)
            old_value: PyObject
            new_version: uint64_t
            if DK_IS_UNICODE(dict.ma_keys):
                ep: PyDictUnicodeEntry = DK_UNICODE_ENTRIES(dict.ma_keys) + hint
                DEOPT_IF(ep.me_key != name, STORE_ATTR)
                old_value = ep.me_value
                DEOPT_IF(old_value == NULL, STORE_ATTR)
                new_version = _PyDict_NotifyEvent(
                    PyDict_EVENT_MODIFIED, dict, name, value
                )
                ep.me_value = value
            else:
                ep: PyDictKeyEntry = DK_ENTRIES(dict.ma_keys) + hint
                DEOPT_IF(ep.me_key != name, STORE_ATTR)
                old_value = ep.me_value
                DEOPT_IF(old_value == NULL, STORE_ATTR)
                new_version = _PyDict_NotifyEvent(
                    PyDict_EVENT_MODIFIED, dict, name, value
                )
                ep.me_value = value
            Py_DECREF(old_value)
            STAT_INC(STORE_ATTR, hit)
            if (not _PyObject_GC_IS_TRACKED(dict)) and _PyObject_GC_MAY_BE_TRACKED(
                value
            ):
                _PyObject_GC_TRACK(dict)
            else:
                print()
            dict.ma_version_tag = new_version
            Py_DECREF(owner)
            STACK_SHRINK(2)
            JUMPBY(4)
            DISPATCH()
        case ops.STORE_ATTR_SLOT:
            owner: PyObject = PEEK(1)
            value: PyObject = PEEK(2)
            type_version: uint32_t = read_u32(next_instr[1].cache)
            index: uint16_t = read_u16(next_instr[3].cache)
            assert cframe.use_tracing == 0
            tp: PyTypeObject = Py_TYPE(owner)
            assert type_version != 0
            DEOPT_IF(tp.tp_version_tag != type_version, STORE_ATTR)
            addr: char = (char(owner)) + index
            STAT_INC(STORE_ATTR, hit)
            old_value: PyObject = PyObject(addr)
            # (PyObject(addr)) = value
            Py_XDECREF(old_value)
            Py_DECREF(owner)
            STACK_SHRINK(2)
            JUMPBY(4)
            DISPATCH()
        case ops.COMPARE_OP:
            PREDICTED(COMPARE_OP)
            right: PyObject = PEEK(1)
            left: PyObject = PEEK(2)
            res: PyObject
            cache: _PyCompareOpCache = _PyCompareOpCache(next_instr)
            if ADAPTIVE_COUNTER_IS_ZERO(cache.counter):
                assert cframe.use_tracing == 0
                next_instr -= 1
                _Py_Specialize_CompareOp(left, right, next_instr, oparg)
                DISPATCH_SAME_OPARG()
            else:
                print()
            STAT_INC(COMPARE_OP, deferred)
            DECREMENT_ADAPTIVE_COUNTER(cache.counter)
            assert oparg <= Py_GE
            res = PyObject_RichCompare(left, right, oparg)
            Py_DECREF(left)
            Py_DECREF(right)
            if res == NULL:
                return  # goto pop_2_error
            else:
                print()
            STACK_SHRINK(1)
            POKE(1, res)
            JUMPBY(2)
            DISPATCH()
        case ops.COMPARE_OP_FLOAT_JUMP:
            _tmp_1: PyObject = PEEK(1)
            _tmp_2: PyObject = PEEK(2)
            right: PyObject = _tmp_1
            left: PyObject = _tmp_2
            jump: size_t
            when_to_jump_mask: uint16_t = read_u16(next_instr[1].cache)
            assert cframe.use_tracing == 0
            DEOPT_IF(not PyFloat_CheckExact(left), COMPARE_OP)
            DEOPT_IF(not PyFloat_CheckExact(right), COMPARE_OP)
            STAT_INC(COMPARE_OP, hit)
            dleft: double = PyFloat_AS_DOUBLE(left)
            dright: double = PyFloat_AS_DOUBLE(right)
            sign_ish: int = 1 << ((2 * (dleft >= dright)) + (dleft <= dright))
            _Py_DECREF_SPECIALIZED(left, _PyFloat_ExactDealloc)
            _Py_DECREF_SPECIALIZED(right, _PyFloat_ExactDealloc)
            jump = sign_ish & when_to_jump_mask
            _tmp_2 = PyObject(jump)
            JUMPBY(2)
            NEXTOPARG()
            JUMPBY(1)
            jump: size_t = size_t(_tmp_2)
            assert (opcode == POP_JUMP_IF_FALSE) or (opcode == POP_JUMP_IF_TRUE)
            if jump:
                JUMPBY(oparg)
            else:
                print()
            STACK_SHRINK(2)
            DISPATCH()
        case ops.COMPARE_OP_INT_JUMP:
            _tmp_1: PyObject = PEEK(1)
            _tmp_2: PyObject = PEEK(2)
            right: PyObject = _tmp_1
            left: PyObject = _tmp_2
            jump: size_t
            when_to_jump_mask: uint16_t = read_u16(next_instr[1].cache)
            assert cframe.use_tracing == 0
            DEOPT_IF(not PyLong_CheckExact(left), COMPARE_OP)
            DEOPT_IF(not PyLong_CheckExact(right), COMPARE_OP)
            DEOPT_IF((size_t((Py_SIZE(left) + 1))) > 2, COMPARE_OP)
            DEOPT_IF((size_t((Py_SIZE(right) + 1))) > 2, COMPARE_OP)
            STAT_INC(COMPARE_OP, hit)
            assert (Py_ABS(Py_SIZE(left)) <= 1) and (Py_ABS(Py_SIZE(right)) <= 1)
            ileft: Py_ssize_t = Py_SIZE(left) * (PyLongObject(left)).ob_digit[0]
            iright: Py_ssize_t = Py_SIZE(right) * (PyLongObject(right)).ob_digit[0]
            sign_ish: int = 1 << ((2 * (ileft >= iright)) + (ileft <= iright))
            _Py_DECREF_SPECIALIZED(left, destructor(PyObject_Free))
            _Py_DECREF_SPECIALIZED(right, destructor(PyObject_Free))
            jump = sign_ish & when_to_jump_mask
            _tmp_2 = PyObject(jump)
            JUMPBY(2)
            NEXTOPARG()
            JUMPBY(1)
            jump: size_t = size_t(_tmp_2)
            assert (opcode == POP_JUMP_IF_FALSE) or (opcode == POP_JUMP_IF_TRUE)
            if jump:
                JUMPBY(oparg)
            else:
                print()
            STACK_SHRINK(2)
            DISPATCH()
        case ops.COMPARE_OP_STR_JUMP:
            _tmp_1: PyObject = PEEK(1)
            _tmp_2: PyObject = PEEK(2)
            right: PyObject = _tmp_1
            left: PyObject = _tmp_2
            jump: size_t
            invert: uint16_t = read_u16(next_instr[1].cache)
            assert cframe.use_tracing == 0
            DEOPT_IF(not PyUnicode_CheckExact(left), COMPARE_OP)
            DEOPT_IF(not PyUnicode_CheckExact(right), COMPARE_OP)
            STAT_INC(COMPARE_OP, hit)
            res: int = _PyUnicode_Equal(left, right)
            assert (oparg == Py_EQ) or (oparg == Py_NE)
            _Py_DECREF_SPECIALIZED(left, _PyUnicode_ExactDealloc)
            _Py_DECREF_SPECIALIZED(right, _PyUnicode_ExactDealloc)
            assert (res == 0) or (res == 1)
            assert (invert == 0) or (invert == 1)
            jump = res ^ invert
            _tmp_2 = PyObject(jump)
            JUMPBY(2)
            NEXTOPARG()
            JUMPBY(1)
            jump: size_t = size_t(_tmp_2)
            assert (opcode == POP_JUMP_IF_FALSE) or (opcode == POP_JUMP_IF_TRUE)
            if jump:
                JUMPBY(oparg)
            else:
                print()
            STACK_SHRINK(2)
            DISPATCH()
        case ops.IS_OP:
            right: PyObject = PEEK(1)
            left: PyObject = PEEK(2)
            b: PyObject
            res: int = Py_Is(left, right) ^ oparg
            Py_DECREF(left)
            Py_DECREF(right)
            b = Py_NewRef(Py_True if res else Py_False)
            STACK_SHRINK(1)
            POKE(1, b)
            DISPATCH()
        case ops.CONTAINS_OP:
            right: PyObject = PEEK(1)
            left: PyObject = PEEK(2)
            b: PyObject
            res: int = PySequence_Contains(right, left)
            Py_DECREF(left)
            Py_DECREF(right)
            if res < 0:
                return  # goto pop_2_error
            else:
                print()
            b = Py_NewRef(Py_True if res ^ oparg else Py_False)
            STACK_SHRINK(1)
            POKE(1, b)
            DISPATCH()
        case ops.CHECK_EG_MATCH:
            match_type: PyObject = POP()
            if check_except_star_type_valid(tstate, match_type) < 0:
                Py_DECREF(match_type)
                return  # goto error
            else:
                print()
            exc_value: PyObject = PEEK(1)
            match: PyObject = NULL
            rest: PyObject = NULL
            res: int = exception_group_match(exc_value, match_type, match, rest)
            Py_DECREF(match_type)
            if res < 0:
                return  # goto error
            else:
                print()
            if (match == NULL) or (rest == NULL):
                assert match == NULL
                assert rest == NULL
                return  # goto error
            else:
                print()
            if Py_IsNone(match):
                PUSH(match)
                Py_XDECREF(rest)
            else:
                SET_TOP(rest)
                PUSH(match)
                PyErr_SetExcInfo(NULL, Py_NewRef(match), NULL)
                Py_DECREF(exc_value)
            DISPATCH()
        case ops.CHECK_EXC_MATCH:
            right: PyObject = PEEK(1)
            left: PyObject = PEEK(2)
            b: PyObject
            assert PyExceptionInstance_Check(left)
            if check_except_type_valid(tstate, right) < 0:
                Py_DECREF(right)
                if true:
                    return  # goto pop_1_error
                else:
                    print()
            else:
                print()
            res: int = PyErr_GivenExceptionMatches(left, right)
            Py_DECREF(right)
            b = Py_NewRef(Py_True if res else Py_False)
            POKE(1, b)
            DISPATCH()
        case ops.IMPORT_NAME:
            fromlist: PyObject = PEEK(1)
            level: PyObject = PEEK(2)
            res: PyObject
            name: PyObject = GETITEM(names, oparg)
            res = import_name(tstate, frame, name, fromlist, level)
            Py_DECREF(level)
            Py_DECREF(fromlist)
            if res == NULL:
                return  # goto pop_2_error
            else:
                print()
            STACK_SHRINK(1)
            POKE(1, res)
            DISPATCH()
        case ops.IMPORT_STAR:
            from_: PyObject = PEEK(1)
            locals: PyObject
            err: int
            if _PyFrame_FastToLocalsWithError(frame) < 0:
                Py_DECREF(from_)
                if true:
                    return  # goto pop_1_error
                else:
                    print()
            else:
                print()
            locals = LOCALS()
            if locals == NULL:
                _PyErr_SetString(
                    tstate, PyExc_SystemError, "no locals found during 'import *'"
                )
                Py_DECREF(from_)
                if true:
                    return  # goto pop_1_error
                else:
                    print()
            else:
                print()
            err = import_all_from(tstate, locals, from_)
            _PyFrame_LocalsToFast(frame, 0)
            Py_DECREF(from_)
            if err:
                return  # goto pop_1_error
            else:
                print()
            STACK_SHRINK(1)
            DISPATCH()
        case ops.IMPORT_FROM:
            from_: PyObject = PEEK(1)
            res: PyObject
            name: PyObject = GETITEM(names, oparg)
            res = import_from(tstate, from_, name)
            if res == NULL:
                return  # goto error
            else:
                print()
            STACK_GROW(1)
            POKE(1, res)
            DISPATCH()
        case ops.JUMP_FORWARD:
            JUMPBY(oparg)
            DISPATCH()
        case ops.JUMP_BACKWARD:
            PREDICTED(JUMP_BACKWARD)
            assert oparg < INSTR_OFFSET()
            JUMPBY(-oparg)
            CHECK_EVAL_BREAKER()
            DISPATCH()
        case ops.POP_JUMP_IF_FALSE:
            PREDICTED(POP_JUMP_IF_FALSE)
            cond: PyObject = POP()
            if Py_IsTrue(cond):
                _Py_DECREF_NO_DEALLOC(cond)
            else:
                if Py_IsFalse(cond):
                    _Py_DECREF_NO_DEALLOC(cond)
                    JUMPBY(oparg)
                else:
                    err: int = PyObject_IsTrue(cond)
                    Py_DECREF(cond)
                    if err > 0:
                        print()
                    else:
                        if err == 0:
                            JUMPBY(oparg)
                        else:
                            return  # goto error
            DISPATCH()
        case ops.POP_JUMP_IF_TRUE:
            cond: PyObject = POP()
            if Py_IsFalse(cond):
                _Py_DECREF_NO_DEALLOC(cond)
            else:
                if Py_IsTrue(cond):
                    _Py_DECREF_NO_DEALLOC(cond)
                    JUMPBY(oparg)
                else:
                    err: int = PyObject_IsTrue(cond)
                    Py_DECREF(cond)
                    if err > 0:
                        JUMPBY(oparg)
                    else:
                        if err == 0:
                            print()
                        else:
                            return  # goto error
            DISPATCH()
        case ops.POP_JUMP_IF_NOT_NONE:
            value: PyObject = POP()
            if not Py_IsNone(value):
                JUMPBY(oparg)
            else:
                print()
            Py_DECREF(value)
            DISPATCH()
        case ops.POP_JUMP_IF_NONE:
            value: PyObject = POP()
            if Py_IsNone(value):
                _Py_DECREF_NO_DEALLOC(value)
                JUMPBY(oparg)
            else:
                Py_DECREF(value)
            DISPATCH()
        case ops.JUMP_IF_FALSE_OR_POP:
            cond: PyObject = PEEK(1)
            err: int
            if Py_IsTrue(cond):
                STACK_SHRINK(1)
                _Py_DECREF_NO_DEALLOC(cond)
            else:
                if Py_IsFalse(cond):
                    JUMPBY(oparg)
                else:
                    err = PyObject_IsTrue(cond)
                    if err > 0:
                        STACK_SHRINK(1)
                        Py_DECREF(cond)
                    else:
                        if err == 0:
                            JUMPBY(oparg)
                        else:
                            return  # goto error
            DISPATCH()
        case ops.JUMP_IF_TRUE_OR_POP:
            cond: PyObject = PEEK(1)
            err: int
            if Py_IsFalse(cond):
                STACK_SHRINK(1)
                _Py_DECREF_NO_DEALLOC(cond)
            else:
                if Py_IsTrue(cond):
                    JUMPBY(oparg)
                else:
                    err = PyObject_IsTrue(cond)
                    if err > 0:
                        JUMPBY(oparg)
                    else:
                        if err == 0:
                            STACK_SHRINK(1)
                            Py_DECREF(cond)
                        else:
                            return  # goto error
            DISPATCH()
        case ops.JUMP_BACKWARD_NO_INTERRUPT:
            JUMPBY(-oparg)
            DISPATCH()
        case ops.GET_LEN:
            len_i: Py_ssize_t = PyObject_Length(PEEK(1))
            if len_i < 0:
                return  # goto error
            else:
                print()
            len_o: PyObject = PyLong_FromSsize_t(len_i)
            if len_o == NULL:
                return  # goto error
            else:
                print()
            PUSH(len_o)
            DISPATCH()
        case ops.MATCH_CLASS:
            names: PyObject = POP()
            type: PyObject = POP()
            subject: PyObject = PEEK(1)
            assert PyTuple_CheckExact(names)
            attrs: PyObject = match_class(tstate, subject, type, oparg, names)
            Py_DECREF(names)
            Py_DECREF(type)
            if attrs:
                assert PyTuple_CheckExact(attrs)
                SET_TOP(attrs)
            else:
                if _PyErr_Occurred(tstate):
                    return  # goto error
                else:
                    SET_TOP(Py_NewRef(Py_None))
            Py_DECREF(subject)
            DISPATCH()
        case ops.MATCH_MAPPING:
            subject: PyObject = PEEK(1)
            match: int = Py_TYPE(subject).tp_flags & Py_TPFLAGS_MAPPING
            res: PyObject = Py_True if match else Py_False
            PUSH(Py_NewRef(res))
            PREDICT(POP_JUMP_IF_FALSE)
            DISPATCH()
        case ops.MATCH_SEQUENCE:
            subject: PyObject = PEEK(1)
            match: int = Py_TYPE(subject).tp_flags & Py_TPFLAGS_SEQUENCE
            res: PyObject = Py_True if match else Py_False
            PUSH(Py_NewRef(res))
            PREDICT(POP_JUMP_IF_FALSE)
            DISPATCH()
        case ops.MATCH_KEYS:
            keys: PyObject = PEEK(1)
            subject: PyObject = PEEK(2)
            values_or_none: PyObject = match_keys(tstate, subject, keys)
            if values_or_none == NULL:
                return  # goto error
            else:
                print()
            PUSH(values_or_none)
            DISPATCH()
        case ops.GET_ITER:
            iterable: PyObject = PEEK(1)
            iter: PyObject = PyObject_GetIter(iterable)
            Py_DECREF(iterable)
            SET_TOP(iter)
            if iter == NULL:
                return  # goto error
            else:
                print()
            DISPATCH()
        case ops.GET_YIELD_FROM_ITER:
            iterable: PyObject = PEEK(1)
            iter: PyObject
            if PyCoro_CheckExact(iterable):
                if not (frame.f_code.co_flags & (CO_COROUTINE | CO_ITERABLE_COROUTINE)):
                    Py_DECREF(iterable)
                    SET_TOP(NULL)
                    _PyErr_SetString(
                        tstate,
                        PyExc_TypeError,
                        "cannot 'yield from' a coroutine object in a non-coroutine generator",
                    )
                    return  # goto error
                else:
                    print()
            else:
                if not PyGen_CheckExact(iterable):
                    iter = PyObject_GetIter(iterable)
                    Py_DECREF(iterable)
                    SET_TOP(iter)
                    if iter == NULL:
                        return  # goto error
                    else:
                        print()
                else:
                    print()
            PREDICT(LOAD_CONST)
            DISPATCH()
        case ops.FOR_ITER:
            PREDICTED(FOR_ITER)
            cache: _PyForIterCache = _PyForIterCache(next_instr)
            if ADAPTIVE_COUNTER_IS_ZERO(cache.counter):
                assert cframe.use_tracing == 0
                next_instr -= 1
                _Py_Specialize_ForIter(PEEK(1), next_instr, oparg)
                DISPATCH_SAME_OPARG()
            else:
                print()
            STAT_INC(FOR_ITER, deferred)
            DECREMENT_ADAPTIVE_COUNTER(cache.counter)
            iter: PyObject = PEEK(1)
            next: PyObject = (Py_TYPE(iter).tp_iternext)(iter)
            if next != NULL:
                PUSH(next)
                JUMPBY(INLINE_CACHE_ENTRIES_FOR_ITER)
            else:
                if _PyErr_Occurred(tstate):
                    if not _PyErr_ExceptionMatches(tstate, PyExc_StopIteration):
                        return  # goto error
                    else:
                        if tstate.c_tracefunc != NULL:
                            call_exc_trace(
                                tstate.c_tracefunc, tstate.c_traceobj, tstate, frame
                            )
                        else:
                            print()
                    _PyErr_Clear(tstate)
                else:
                    print()
                assert (
                    _Py_OPCODE(next_instr[INLINE_CACHE_ENTRIES_FOR_ITER + oparg])
                    == END_FOR
                )
                STACK_SHRINK(1)
                Py_DECREF(iter)
                JUMPBY((INLINE_CACHE_ENTRIES_FOR_ITER + oparg) + 1)
            DISPATCH()
        case ops.FOR_ITER_LIST:
            assert cframe.use_tracing == 0
            it: _PyListIterObject = _PyListIterObject(PEEK(1))
            DEOPT_IF(Py_TYPE(it) != (PyListIter_Type), FOR_ITER)
            STAT_INC(FOR_ITER, hit)
            seq: PyListObject = it.it_seq
            if seq:
                if it.it_index < PyList_GET_SIZE(seq):
                    it.it_index += 1
                    next: PyObject = PyList_GET_ITEM(seq, it.it_index)
                    PUSH(Py_NewRef(next))
                    JUMPBY(INLINE_CACHE_ENTRIES_FOR_ITER)
                    return  # goto end_for_iter_list
                else:
                    print()
                it.it_seq = NULL
                Py_DECREF(seq)
            else:
                print()
            STACK_SHRINK(1)
            Py_DECREF(it)
            JUMPBY((INLINE_CACHE_ENTRIES_FOR_ITER + oparg) + 1)
            # label: end_for_iter_list:
            DISPATCH()
        case ops.FOR_ITER_TUPLE:
            assert cframe.use_tracing == 0
            it: _PyTupleIterObject = _PyTupleIterObject(PEEK(1))
            DEOPT_IF(Py_TYPE(it) != (PyTupleIter_Type), FOR_ITER)
            STAT_INC(FOR_ITER, hit)
            seq: PyTupleObject = it.it_seq
            if seq:
                if it.it_index < PyTuple_GET_SIZE(seq):
                    it.it_index += 1
                    next: PyObject = PyTuple_GET_ITEM(seq, it.it_index)
                    PUSH(Py_NewRef(next))
                    JUMPBY(INLINE_CACHE_ENTRIES_FOR_ITER)
                    return  # goto end_for_iter_tuple
                else:
                    print()
                it.it_seq = NULL
                Py_DECREF(seq)
            else:
                print()
            STACK_SHRINK(1)
            Py_DECREF(it)
            JUMPBY((INLINE_CACHE_ENTRIES_FOR_ITER + oparg) + 1)
            # label: end_for_iter_tuple:
            DISPATCH()
        case ops.FOR_ITER_RANGE:
            assert cframe.use_tracing == 0
            r: _PyRangeIterObject = _PyRangeIterObject(PEEK(1))
            DEOPT_IF(Py_TYPE(r) != (PyRangeIter_Type), FOR_ITER)
            STAT_INC(FOR_ITER, hit)
            next: _Py_CODEUNIT = next_instr[INLINE_CACHE_ENTRIES_FOR_ITER]
            assert _PyOpcode_Deopt[_Py_OPCODE(next)] == STORE_FAST
            if r.len <= 0:
                STACK_SHRINK(1)
                Py_DECREF(r)
                JUMPBY((INLINE_CACHE_ENTRIES_FOR_ITER + oparg) + 1)
            else:
                value: long = r.start
                r.start = value + r.step
                r.len -= 1
                if _PyLong_AssignValue(frame.localsplus[_Py_OPARG(next)], value) < 0:
                    return  # goto error
                else:
                    print()
                JUMPBY(INLINE_CACHE_ENTRIES_FOR_ITER + 1)
            DISPATCH()
        case ops.FOR_ITER_GEN:
            assert cframe.use_tracing == 0
            gen: PyGenObject = PyGenObject(PEEK(1))
            DEOPT_IF(Py_TYPE(gen) != (PyGen_Type), FOR_ITER)
            DEOPT_IF(gen.gi_frame_state >= FRAME_EXECUTING, FOR_ITER)
            STAT_INC(FOR_ITER, hit)
            gen_frame: _PyInterpreterFrame = _PyInterpreterFrame(gen.gi_iframe)
            frame.yield_offset = oparg
            _PyFrame_StackPush(gen_frame, Py_NewRef(Py_None))
            gen.gi_frame_state = FRAME_EXECUTING
            gen.gi_exc_state.previous_item = tstate.exc_info
            tstate.exc_info = gen.gi_exc_state
            JUMPBY(INLINE_CACHE_ENTRIES_FOR_ITER + oparg)
            assert _Py_OPCODE(next_instr) == END_FOR
            DISPATCH_INLINED(gen_frame)
        case ops.BEFORE_ASYNC_WITH:
            mgr: PyObject = PEEK(1)
            res: PyObject
            enter: PyObject = _PyObject_LookupSpecial(mgr, _Py_ID(__aenter__))
            if enter == NULL:
                if not _PyErr_Occurred(tstate):
                    _PyErr_Format(
                        tstate,
                        PyExc_TypeError,
                        "'%.200s' object does not support the asynchronous context manager protocol",
                        Py_TYPE(mgr).tp_name,
                    )
                else:
                    print()
                return  # goto error
            else:
                print()
            exit: PyObject = _PyObject_LookupSpecial(mgr, _Py_ID(__aexit__))
            if exit == NULL:
                if not _PyErr_Occurred(tstate):
                    _PyErr_Format(
                        tstate,
                        PyExc_TypeError,
                        "'%.200s' object does not support the asynchronous context manager protocol (missed __aexit__ method)",
                        Py_TYPE(mgr).tp_name,
                    )
                else:
                    print()
                Py_DECREF(enter)
                return  # goto error
            else:
                print()
            SET_TOP(exit)
            Py_DECREF(mgr)
            res = _PyObject_CallNoArgs(enter)
            Py_DECREF(enter)
            if res == NULL:
                return  # goto error
            else:
                print()
            PUSH(res)
            PREDICT(GET_AWAITABLE)
            DISPATCH()
        case ops.BEFORE_WITH:
            mgr: PyObject = PEEK(1)
            res: PyObject
            enter: PyObject = _PyObject_LookupSpecial(mgr, _Py_ID(__enter__))
            if enter == NULL:
                if not _PyErr_Occurred(tstate):
                    _PyErr_Format(
                        tstate,
                        PyExc_TypeError,
                        "'%.200s' object does not support the context manager protocol",
                        Py_TYPE(mgr).tp_name,
                    )
                else:
                    print()
                return  # goto error
            else:
                print()
            exit: PyObject = _PyObject_LookupSpecial(mgr, _Py_ID(__exit__))
            if exit == NULL:
                if not _PyErr_Occurred(tstate):
                    _PyErr_Format(
                        tstate,
                        PyExc_TypeError,
                        "'%.200s' object does not support the context manager protocol (missed __exit__ method)",
                        Py_TYPE(mgr).tp_name,
                    )
                else:
                    print()
                Py_DECREF(enter)
                return  # goto error
            else:
                print()
            SET_TOP(exit)
            Py_DECREF(mgr)
            res = _PyObject_CallNoArgs(enter)
            Py_DECREF(enter)
            if res == NULL:
                return  # goto error
            else:
                print()
            PUSH(res)
            DISPATCH()
        case ops.WITH_EXCEPT_START:
            val: PyObject = PEEK(1)
            lasti: PyObject = PEEK(3)
            exit_func: PyObject = PEEK(4)
            res: PyObject
            exc: PyObject
            tb: PyObject
            assert val and PyExceptionInstance_Check(val)
            exc = PyExceptionInstance_Class(val)
            tb = PyException_GetTraceback(val)
            Py_XDECREF(tb)
            assert PyLong_Check(lasti)
            void(lasti)
            stack: PyObject = [NULL, exc, val, tb]
            res = PyObject_Vectorcall(
                exit_func, stack + 1, 3 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL
            )
            if res == NULL:
                return  # goto error
            else:
                print()
            STACK_GROW(1)
            POKE(1, res)
            DISPATCH()
        case ops.PUSH_EXC_INFO:
            value: PyObject = PEEK(1)
            exc_info: _PyErr_StackItem = tstate.exc_info
            if exc_info.exc_value != NULL:
                SET_TOP(exc_info.exc_value)
            else:
                SET_TOP(Py_NewRef(Py_None))
            PUSH(Py_NewRef(value))
            assert PyExceptionInstance_Check(value)
            exc_info.exc_value = value
            DISPATCH()
        case ops.LOAD_ATTR_METHOD_WITH_VALUES:
            assert cframe.use_tracing == 0
            self: PyObject = PEEK(1)
            self_cls: PyTypeObject = Py_TYPE(self)
            cache: _PyLoadMethodCache = _PyLoadMethodCache(next_instr)
            type_version: uint32_t = read_u32(cache.type_version)
            assert type_version != 0
            DEOPT_IF(self_cls.tp_version_tag != type_version, LOAD_ATTR)
            assert self_cls.tp_flags & Py_TPFLAGS_MANAGED_DICT
            dorv: PyDictOrValues = _PyObject_DictOrValuesPointer(self)
            DEOPT_IF(not _PyDictOrValues_IsValues(dorv), LOAD_ATTR)
            self_heap_type: PyHeapTypeObject = PyHeapTypeObject(self_cls)
            DEOPT_IF(
                self_heap_type.ht_cached_keys.dk_version
                != read_u32(cache.keys_version),
                LOAD_ATTR,
            )
            STAT_INC(LOAD_ATTR, hit)
            res: PyObject = read_obj(cache.descr)
            assert res != NULL
            assert _PyType_HasFeature(Py_TYPE(res), Py_TPFLAGS_METHOD_DESCRIPTOR)
            SET_TOP(Py_NewRef(res))
            PUSH(self)
            JUMPBY(INLINE_CACHE_ENTRIES_LOAD_ATTR)
            DISPATCH()
        case ops.LOAD_ATTR_METHOD_WITH_DICT:
            assert cframe.use_tracing == 0
            self: PyObject = PEEK(1)
            self_cls: PyTypeObject = Py_TYPE(self)
            cache: _PyLoadMethodCache = _PyLoadMethodCache(next_instr)
            DEOPT_IF(self_cls.tp_version_tag != read_u32(cache.type_version), LOAD_ATTR)
            dictoffset: Py_ssize_t = self_cls.tp_dictoffset
            assert dictoffset > 0
            dictptr: PyDictObject = PyDictObject(((char(self)) + dictoffset))
            dict: PyDictObject = dictptr
            DEOPT_IF(dict == NULL, LOAD_ATTR)
            DEOPT_IF(dict.ma_keys.dk_version != read_u32(cache.keys_version), LOAD_ATTR)
            STAT_INC(LOAD_ATTR, hit)
            res: PyObject = read_obj(cache.descr)
            assert res != NULL
            assert _PyType_HasFeature(Py_TYPE(res), Py_TPFLAGS_METHOD_DESCRIPTOR)
            SET_TOP(Py_NewRef(res))
            PUSH(self)
            JUMPBY(INLINE_CACHE_ENTRIES_LOAD_ATTR)
            DISPATCH()
        case ops.LOAD_ATTR_METHOD_NO_DICT:
            assert cframe.use_tracing == 0
            self: PyObject = PEEK(1)
            self_cls: PyTypeObject = Py_TYPE(self)
            cache: _PyLoadMethodCache = _PyLoadMethodCache(next_instr)
            type_version: uint32_t = read_u32(cache.type_version)
            DEOPT_IF(self_cls.tp_version_tag != type_version, LOAD_ATTR)
            assert self_cls.tp_dictoffset == 0
            STAT_INC(LOAD_ATTR, hit)
            res: PyObject = read_obj(cache.descr)
            assert res != NULL
            assert _PyType_HasFeature(Py_TYPE(res), Py_TPFLAGS_METHOD_DESCRIPTOR)
            SET_TOP(Py_NewRef(res))
            PUSH(self)
            JUMPBY(INLINE_CACHE_ENTRIES_LOAD_ATTR)
            DISPATCH()
        case ops.LOAD_ATTR_METHOD_LAZY_DICT:
            assert cframe.use_tracing == 0
            self: PyObject = PEEK(1)
            self_cls: PyTypeObject = Py_TYPE(self)
            cache: _PyLoadMethodCache = _PyLoadMethodCache(next_instr)
            type_version: uint32_t = read_u32(cache.type_version)
            DEOPT_IF(self_cls.tp_version_tag != type_version, LOAD_ATTR)
            dictoffset: Py_ssize_t = self_cls.tp_dictoffset
            assert dictoffset > 0
            dict: PyObject = PyObject(((char(self)) + dictoffset))
            DEOPT_IF(dict != NULL, LOAD_ATTR)
            STAT_INC(LOAD_ATTR, hit)
            res: PyObject = read_obj(cache.descr)
            assert res != NULL
            assert _PyType_HasFeature(Py_TYPE(res), Py_TPFLAGS_METHOD_DESCRIPTOR)
            SET_TOP(Py_NewRef(res))
            PUSH(self)
            JUMPBY(INLINE_CACHE_ENTRIES_LOAD_ATTR)
            DISPATCH()
        case ops.CALL_BOUND_METHOD_EXACT_ARGS:
            DEOPT_IF(is_method(stack_pointer, oparg), CALL)
            function: PyObject = PEEK(oparg + 1)
            DEOPT_IF(Py_TYPE(function) != (PyMethod_Type), CALL)
            STAT_INC(CALL, hit)
            self: PyObject = (PyMethodObject(function)).im_self
            # PEEK(oparg + 1) = Py_NewRef(self)
            meth: PyObject = (PyMethodObject(function)).im_func
            # PEEK(oparg + 2) = Py_NewRef(meth)
            Py_DECREF(function)
            GO_TO_INSTRUCTION(CALL_PY_EXACT_ARGS)
        case ops.KW_NAMES:
            assert kwnames == NULL
            assert oparg < PyTuple_GET_SIZE(consts)
            kwnames = GETITEM(consts, oparg)
            DISPATCH()
        case ops.CALL:
            PREDICTED(CALL)
            cache: _PyCallCache = _PyCallCache(next_instr)
            if ADAPTIVE_COUNTER_IS_ZERO(cache.counter):
                assert cframe.use_tracing == 0
                is_meth: int = is_method(stack_pointer, oparg)
                nargs: int = oparg + is_meth
                callable: PyObject = PEEK(nargs + 1)
                next_instr -= 1
                _Py_Specialize_Call(callable, next_instr, nargs, kwnames)
                DISPATCH_SAME_OPARG()
            else:
                print()
            STAT_INC(CALL, deferred)
            DECREMENT_ADAPTIVE_COUNTER(cache.counter)
            total_args: int
            is_meth: int
            is_meth = is_method(stack_pointer, oparg)
            function: PyObject = PEEK(oparg + 1)
            if (not is_meth) and (Py_TYPE(function) == (PyMethod_Type)):
                self: PyObject = (PyMethodObject(function)).im_self
                # PEEK(oparg + 1) = Py_NewRef(self)
                meth: PyObject = (PyMethodObject(function)).im_func
                # PEEK(oparg + 2) = Py_NewRef(meth)
                Py_DECREF(function)
                is_meth = 1
            else:
                print()
            total_args = oparg + is_meth
            function = PEEK(total_args + 1)
            positional_args: int = total_args - KWNAMES_LEN()
            if (
                (Py_TYPE(function) == (PyFunction_Type))
                and (tstate.interp.eval_frame == NULL)
            ) and ((PyFunctionObject(function)).vectorcall == _PyFunction_Vectorcall):
                code_flags: int = (PyCodeObject(PyFunction_GET_CODE(function))).co_flags
                locals: PyObject = (
                    NULL
                    if code_flags & CO_OPTIMIZED
                    else Py_NewRef(PyFunction_GET_GLOBALS(function))
                )
                STACK_SHRINK(total_args)
                new_frame: _PyInterpreterFrame = _PyEvalFramePushAndInit(
                    tstate,
                    PyFunctionObject(function),
                    locals,
                    stack_pointer,
                    positional_args,
                    kwnames,
                )
                kwnames = NULL
                STACK_SHRINK(2 - is_meth)
                if new_frame == NULL:
                    return  # goto error
                else:
                    print()
                JUMPBY(INLINE_CACHE_ENTRIES_CALL)
                DISPATCH_INLINED(new_frame)
            else:
                print()
            res: PyObject
            if cframe.use_tracing:
                res = trace_call_function(
                    tstate,
                    function,
                    stack_pointer - total_args,
                    positional_args,
                    kwnames,
                )
            else:
                res = PyObject_Vectorcall(
                    function,
                    stack_pointer - total_args,
                    positional_args | PY_VECTORCALL_ARGUMENTS_OFFSET,
                    kwnames,
                )
            kwnames = NULL
            assert (res != NULL) ^ (_PyErr_Occurred(tstate) != NULL)
            Py_DECREF(function)
            STACK_SHRINK(total_args)
            i: int = 0
            while i < total_args:
                Py_DECREF(stack_pointer[i])
                i += 1
            STACK_SHRINK(2 - is_meth)
            PUSH(res)
            if res == NULL:
                return  # goto error
            else:
                print()
            JUMPBY(INLINE_CACHE_ENTRIES_CALL)
            CHECK_EVAL_BREAKER()
            DISPATCH()
        case ops.CALL_PY_EXACT_ARGS:
            PREDICTED(CALL_PY_EXACT_ARGS)
            assert kwnames == NULL
            DEOPT_IF(tstate.interp.eval_frame, CALL)
            cache: _PyCallCache = _PyCallCache(next_instr)
            is_meth: int = is_method(stack_pointer, oparg)
            argcount: int = oparg + is_meth
            callable: PyObject = PEEK(argcount + 1)
            DEOPT_IF(not PyFunction_Check(callable), CALL)
            func: PyFunctionObject = PyFunctionObject(callable)
            DEOPT_IF(func.func_version != read_u32(cache.func_version), CALL)
            code: PyCodeObject = PyCodeObject(func.func_code)
            DEOPT_IF(code.co_argcount != argcount, CALL)
            DEOPT_IF(not _PyThreadState_HasStackSpace(tstate, code.co_framesize), CALL)
            STAT_INC(CALL, hit)
            new_frame: _PyInterpreterFrame = _PyFrame_PushUnchecked(tstate, func)
            STACK_SHRINK(argcount)
            i: int = 0
            while i < argcount:
                new_frame.localsplus[i] = stack_pointer[i]
                i += 1
            i: int = argcount
            while i < code.co_nlocalsplus:
                new_frame.localsplus[i] = NULL
                i += 1
            STACK_SHRINK(2 - is_meth)
            JUMPBY(INLINE_CACHE_ENTRIES_CALL)
            DISPATCH_INLINED(new_frame)
        case ops.CALL_PY_WITH_DEFAULTS:
            assert kwnames == NULL
            DEOPT_IF(tstate.interp.eval_frame, CALL)
            cache: _PyCallCache = _PyCallCache(next_instr)
            is_meth: int = is_method(stack_pointer, oparg)
            argcount: int = oparg + is_meth
            callable: PyObject = PEEK(argcount + 1)
            DEOPT_IF(not PyFunction_Check(callable), CALL)
            func: PyFunctionObject = PyFunctionObject(callable)
            DEOPT_IF(func.func_version != read_u32(cache.func_version), CALL)
            code: PyCodeObject = PyCodeObject(func.func_code)
            DEOPT_IF(argcount > code.co_argcount, CALL)
            minargs: int = cache.min_args
            DEOPT_IF(argcount < minargs, CALL)
            DEOPT_IF(not _PyThreadState_HasStackSpace(tstate, code.co_framesize), CALL)
            STAT_INC(CALL, hit)
            new_frame: _PyInterpreterFrame = _PyFrame_PushUnchecked(tstate, func)
            STACK_SHRINK(argcount)
            i: int = 0
            while i < argcount:
                new_frame.localsplus[i] = stack_pointer[i]
                i += 1
            i: int = argcount
            while i < code.co_argcount:
                def_: PyObject = PyTuple_GET_ITEM(func.func_defaults, i - minargs)
                new_frame.localsplus[i] = Py_NewRef(def_)
                i += 1
            i: int = code.co_argcount
            while i < code.co_nlocalsplus:
                new_frame.localsplus[i] = NULL
                i += 1
            STACK_SHRINK(2 - is_meth)
            JUMPBY(INLINE_CACHE_ENTRIES_CALL)
            DISPATCH_INLINED(new_frame)
        case ops.CALL_NO_KW_TYPE_1:
            assert kwnames == NULL
            assert cframe.use_tracing == 0
            assert oparg == 1
            DEOPT_IF(is_method(stack_pointer, 1), CALL)
            obj: PyObject = PEEK(1)
            callable: PyObject = PEEK(2)
            DEOPT_IF(callable != (PyObject((PyType_Type))), CALL)
            STAT_INC(CALL, hit)
            JUMPBY(INLINE_CACHE_ENTRIES_CALL)
            res: PyObject = Py_NewRef(Py_TYPE(obj))
            Py_DECREF(callable)
            Py_DECREF(obj)
            STACK_SHRINK(2)
            SET_TOP(res)
            DISPATCH()
        case ops.CALL_NO_KW_STR_1:
            assert kwnames == NULL
            assert cframe.use_tracing == 0
            assert oparg == 1
            DEOPT_IF(is_method(stack_pointer, 1), CALL)
            callable: PyObject = PEEK(2)
            DEOPT_IF(callable != (PyObject((PyUnicode_Type))), CALL)
            STAT_INC(CALL, hit)
            arg: PyObject = PEEK(1)
            res: PyObject = PyObject_Str(arg)
            Py_DECREF(arg)
            Py_DECREF(PyUnicode_Type)
            STACK_SHRINK(2)
            SET_TOP(res)
            if res == NULL:
                return  # goto error
            else:
                print()
            JUMPBY(INLINE_CACHE_ENTRIES_CALL)
            CHECK_EVAL_BREAKER()
            DISPATCH()
        case ops.CALL_NO_KW_TUPLE_1:
            assert kwnames == NULL
            assert oparg == 1
            DEOPT_IF(is_method(stack_pointer, 1), CALL)
            callable: PyObject = PEEK(2)
            DEOPT_IF(callable != (PyObject((PyTuple_Type))), CALL)
            STAT_INC(CALL, hit)
            arg: PyObject = PEEK(1)
            res: PyObject = PySequence_Tuple(arg)
            Py_DECREF(arg)
            Py_DECREF(PyTuple_Type)
            STACK_SHRINK(2)
            SET_TOP(res)
            if res == NULL:
                return  # goto error
            else:
                print()
            JUMPBY(INLINE_CACHE_ENTRIES_CALL)
            CHECK_EVAL_BREAKER()
            DISPATCH()
        case ops.CALL_BUILTIN_CLASS:
            is_meth: int = is_method(stack_pointer, oparg)
            total_args: int = oparg + is_meth
            kwnames_len: int = KWNAMES_LEN()
            callable: PyObject = PEEK(total_args + 1)
            DEOPT_IF(not PyType_Check(callable), CALL)
            tp: PyTypeObject = PyTypeObject(callable)
            DEOPT_IF(tp.tp_vectorcall == NULL, CALL)
            STAT_INC(CALL, hit)
            STACK_SHRINK(total_args)
            res: PyObject = tp.tp_vectorcall(
                PyObject(tp), stack_pointer, total_args - kwnames_len, kwnames
            )
            kwnames = NULL
            i: int = 0
            while i < total_args:
                Py_DECREF(stack_pointer[i])
                i += 1
            Py_DECREF(tp)
            STACK_SHRINK(1 - is_meth)
            SET_TOP(res)
            if res == NULL:
                return  # goto error
            else:
                print()
            JUMPBY(INLINE_CACHE_ENTRIES_CALL)
            CHECK_EVAL_BREAKER()
            DISPATCH()
        case ops.CALL_NO_KW_BUILTIN_O:
            assert cframe.use_tracing == 0
            assert kwnames == NULL
            is_meth: int = is_method(stack_pointer, oparg)
            total_args: int = oparg + is_meth
            DEOPT_IF(total_args != 1, CALL)
            callable: PyObject = PEEK(total_args + 1)
            DEOPT_IF(not PyCFunction_CheckExact(callable), CALL)
            DEOPT_IF(PyCFunction_GET_FLAGS(callable) != METH_O, CALL)
            STAT_INC(CALL, hit)
            cfunc: PyCFunction = PyCFunction_GET_FUNCTION(callable)
            if _Py_EnterRecursiveCallTstate(tstate, " while calling a Python object"):
                return  # goto error
            else:
                print()
            arg: PyObject = PEEK(1)
            res: PyObject = _PyCFunction_TrampolineCall(
                cfunc, PyCFunction_GET_SELF(callable), arg
            )
            _Py_LeaveRecursiveCallTstate(tstate)
            assert (res != NULL) ^ (_PyErr_Occurred(tstate) != NULL)
            Py_DECREF(arg)
            Py_DECREF(callable)
            STACK_SHRINK(2 - is_meth)
            SET_TOP(res)
            if res == NULL:
                return  # goto error
            else:
                print()
            JUMPBY(INLINE_CACHE_ENTRIES_CALL)
            CHECK_EVAL_BREAKER()
            DISPATCH()
        case ops.CALL_NO_KW_BUILTIN_FAST:
            assert cframe.use_tracing == 0
            assert kwnames == NULL
            is_meth: int = is_method(stack_pointer, oparg)
            total_args: int = oparg + is_meth
            callable: PyObject = PEEK(total_args + 1)
            DEOPT_IF(not PyCFunction_CheckExact(callable), CALL)
            DEOPT_IF(PyCFunction_GET_FLAGS(callable) != METH_FASTCALL, CALL)
            STAT_INC(CALL, hit)
            cfunc: PyCFunction = PyCFunction_GET_FUNCTION(callable)
            STACK_SHRINK(total_args)
            res: PyObject = (_PyCFunctionFast((void()(void)(cfunc))))(
                PyCFunction_GET_SELF(callable), stack_pointer, total_args
            )
            assert (res != NULL) ^ (_PyErr_Occurred(tstate) != NULL)
            i: int = 0
            while i < total_args:
                Py_DECREF(stack_pointer[i])
                i += 1
            STACK_SHRINK(2 - is_meth)
            PUSH(res)
            Py_DECREF(callable)
            if res == NULL:
                return  # goto error
            else:
                print()
            JUMPBY(INLINE_CACHE_ENTRIES_CALL)
            CHECK_EVAL_BREAKER()
            DISPATCH()
        case ops.CALL_BUILTIN_FAST_WITH_KEYWORDS:
            assert cframe.use_tracing == 0
            is_meth: int = is_method(stack_pointer, oparg)
            total_args: int = oparg + is_meth
            callable: PyObject = PEEK(total_args + 1)
            DEOPT_IF(not PyCFunction_CheckExact(callable), CALL)
            DEOPT_IF(
                PyCFunction_GET_FLAGS(callable) != (METH_FASTCALL | METH_KEYWORDS), CALL
            )
            STAT_INC(CALL, hit)
            STACK_SHRINK(total_args)
            cfunc: _PyCFunctionFastWithKeywords = _PyCFunctionFastWithKeywords(
                (void()(void)(PyCFunction_GET_FUNCTION(callable)))
            )
            res: PyObject = cfunc(
                PyCFunction_GET_SELF(callable),
                stack_pointer,
                total_args - KWNAMES_LEN(),
                kwnames,
            )
            assert (res != NULL) ^ (_PyErr_Occurred(tstate) != NULL)
            kwnames = NULL
            i: int = 0
            while i < total_args:
                Py_DECREF(stack_pointer[i])
                i += 1
            STACK_SHRINK(2 - is_meth)
            PUSH(res)
            Py_DECREF(callable)
            if res == NULL:
                return  # goto error
            else:
                print()
            JUMPBY(INLINE_CACHE_ENTRIES_CALL)
            CHECK_EVAL_BREAKER()
            DISPATCH()
        case ops.CALL_NO_KW_LEN:
            assert cframe.use_tracing == 0
            assert kwnames == NULL
            is_meth: int = is_method(stack_pointer, oparg)
            total_args: int = oparg + is_meth
            DEOPT_IF(total_args != 1, CALL)
            callable: PyObject = PEEK(total_args + 1)
            interp: PyInterpreterState = _PyInterpreterState_GET()
            DEOPT_IF(callable != interp.callable_cache.len, CALL)
            STAT_INC(CALL, hit)
            arg: PyObject = PEEK(1)
            len_i: Py_ssize_t = PyObject_Length(arg)
            if len_i < 0:
                return  # goto error
            else:
                print()
            res: PyObject = PyLong_FromSsize_t(len_i)
            assert (res != NULL) ^ (_PyErr_Occurred(tstate) != NULL)
            STACK_SHRINK(2 - is_meth)
            SET_TOP(res)
            Py_DECREF(callable)
            Py_DECREF(arg)
            if res == NULL:
                return  # goto error
            else:
                print()
            JUMPBY(INLINE_CACHE_ENTRIES_CALL)
            DISPATCH()
        case ops.CALL_NO_KW_ISINSTANCE:
            assert cframe.use_tracing == 0
            assert kwnames == NULL
            is_meth: int = is_method(stack_pointer, oparg)
            total_args: int = oparg + is_meth
            callable: PyObject = PEEK(total_args + 1)
            DEOPT_IF(total_args != 2, CALL)
            interp: PyInterpreterState = _PyInterpreterState_GET()
            DEOPT_IF(callable != interp.callable_cache.isinstance, CALL)
            STAT_INC(CALL, hit)
            cls: PyObject = POP()
            inst: PyObject = PEEK(1)
            retval: int = PyObject_IsInstance(inst, cls)
            if retval < 0:
                Py_DECREF(cls)
                return  # goto error
            else:
                print()
            res: PyObject = PyBool_FromLong(retval)
            assert (res != NULL) ^ (_PyErr_Occurred(tstate) != NULL)
            STACK_SHRINK(2 - is_meth)
            SET_TOP(res)
            Py_DECREF(inst)
            Py_DECREF(cls)
            Py_DECREF(callable)
            if res == NULL:
                return  # goto error
            else:
                print()
            JUMPBY(INLINE_CACHE_ENTRIES_CALL)
            DISPATCH()
        case ops.CALL_NO_KW_LIST_APPEND:
            assert cframe.use_tracing == 0
            assert kwnames == NULL
            assert oparg == 1
            callable: PyObject = PEEK(3)
            interp: PyInterpreterState = _PyInterpreterState_GET()
            DEOPT_IF(callable != interp.callable_cache.list_append, CALL)
            list: PyObject = PEEK(2)
            DEOPT_IF(not PyList_Check(list), CALL)
            STAT_INC(CALL, hit)
            arg: PyObject = POP()
            if _PyList_AppendTakeRef(PyListObject(list), arg) < 0:
                return  # goto error
            else:
                print()
            STACK_SHRINK(2)
            Py_DECREF(list)
            Py_DECREF(callable)
            JUMPBY(INLINE_CACHE_ENTRIES_CALL + 1)
            assert _Py_OPCODE(next_instr[-1]) == POP_TOP
            DISPATCH()
        case ops.CALL_NO_KW_METHOD_DESCRIPTOR_O:
            assert kwnames == NULL
            is_meth: int = is_method(stack_pointer, oparg)
            total_args: int = oparg + is_meth
            callable: PyMethodDescrObject = PyMethodDescrObject(PEEK(total_args + 1))
            DEOPT_IF(total_args != 2, CALL)
            DEOPT_IF(not Py_IS_TYPE(callable, PyMethodDescr_Type), CALL)
            meth: PyMethodDef = callable.d_method
            DEOPT_IF(meth.ml_flags != METH_O, CALL)
            arg: PyObject = PEEK(1)
            self: PyObject = PEEK(2)
            DEOPT_IF(not Py_IS_TYPE(self, callable.d_common.d_type), CALL)
            STAT_INC(CALL, hit)
            cfunc: PyCFunction = meth.ml_meth
            if _Py_EnterRecursiveCallTstate(tstate, " while calling a Python object"):
                return  # goto error
            else:
                print()
            res: PyObject = _PyCFunction_TrampolineCall(cfunc, self, arg)
            _Py_LeaveRecursiveCallTstate(tstate)
            assert (res != NULL) ^ (_PyErr_Occurred(tstate) != NULL)
            Py_DECREF(self)
            Py_DECREF(arg)
            STACK_SHRINK(oparg + 1)
            SET_TOP(res)
            Py_DECREF(callable)
            if res == NULL:
                return  # goto error
            else:
                print()
            JUMPBY(INLINE_CACHE_ENTRIES_CALL)
            CHECK_EVAL_BREAKER()
            DISPATCH()
        case ops.CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS:
            is_meth: int = is_method(stack_pointer, oparg)
            total_args: int = oparg + is_meth
            callable: PyMethodDescrObject = PyMethodDescrObject(PEEK(total_args + 1))
            DEOPT_IF(not Py_IS_TYPE(callable, PyMethodDescr_Type), CALL)
            meth: PyMethodDef = callable.d_method
            DEOPT_IF(meth.ml_flags != (METH_FASTCALL | METH_KEYWORDS), CALL)
            d_type: PyTypeObject = callable.d_common.d_type
            self: PyObject = PEEK(total_args)
            DEOPT_IF(not Py_IS_TYPE(self, d_type), CALL)
            STAT_INC(CALL, hit)
            nargs: int = total_args - 1
            STACK_SHRINK(nargs)
            cfunc: _PyCFunctionFastWithKeywords = _PyCFunctionFastWithKeywords(
                (void()(void)(meth.ml_meth))
            )
            res: PyObject = cfunc(self, stack_pointer, nargs - KWNAMES_LEN(), kwnames)
            assert (res != NULL) ^ (_PyErr_Occurred(tstate) != NULL)
            kwnames = NULL
            i: int = 0
            while i < nargs:
                Py_DECREF(stack_pointer[i])
                i += 1
            Py_DECREF(self)
            STACK_SHRINK(2 - is_meth)
            SET_TOP(res)
            Py_DECREF(callable)
            if res == NULL:
                return  # goto error
            else:
                print()
            JUMPBY(INLINE_CACHE_ENTRIES_CALL)
            CHECK_EVAL_BREAKER()
            DISPATCH()
        case ops.CALL_NO_KW_METHOD_DESCRIPTOR_NOARGS:
            assert kwnames == NULL
            assert (oparg == 0) or (oparg == 1)
            is_meth: int = is_method(stack_pointer, oparg)
            total_args: int = oparg + is_meth
            DEOPT_IF(total_args != 1, CALL)
            callable: PyMethodDescrObject = PyMethodDescrObject(PEEK(2))
            DEOPT_IF(not Py_IS_TYPE(callable, PyMethodDescr_Type), CALL)
            meth: PyMethodDef = callable.d_method
            self: PyObject = PEEK(1)
            DEOPT_IF(not Py_IS_TYPE(self, callable.d_common.d_type), CALL)
            DEOPT_IF(meth.ml_flags != METH_NOARGS, CALL)
            STAT_INC(CALL, hit)
            cfunc: PyCFunction = meth.ml_meth
            if _Py_EnterRecursiveCallTstate(tstate, " while calling a Python object"):
                return  # goto error
            else:
                print()
            res: PyObject = _PyCFunction_TrampolineCall(cfunc, self, NULL)
            _Py_LeaveRecursiveCallTstate(tstate)
            assert (res != NULL) ^ (_PyErr_Occurred(tstate) != NULL)
            Py_DECREF(self)
            STACK_SHRINK(oparg + 1)
            SET_TOP(res)
            Py_DECREF(callable)
            if res == NULL:
                return  # goto error
            else:
                print()
            JUMPBY(INLINE_CACHE_ENTRIES_CALL)
            CHECK_EVAL_BREAKER()
            DISPATCH()
        case ops.CALL_NO_KW_METHOD_DESCRIPTOR_FAST:
            assert kwnames == NULL
            is_meth: int = is_method(stack_pointer, oparg)
            total_args: int = oparg + is_meth
            callable: PyMethodDescrObject = PyMethodDescrObject(PEEK(total_args + 1))
            DEOPT_IF(not Py_IS_TYPE(callable, PyMethodDescr_Type), CALL)
            meth: PyMethodDef = callable.d_method
            DEOPT_IF(meth.ml_flags != METH_FASTCALL, CALL)
            self: PyObject = PEEK(total_args)
            DEOPT_IF(not Py_IS_TYPE(self, callable.d_common.d_type), CALL)
            STAT_INC(CALL, hit)
            cfunc: _PyCFunctionFast = _PyCFunctionFast((void()(void)(meth.ml_meth)))
            nargs: int = total_args - 1
            STACK_SHRINK(nargs)
            res: PyObject = cfunc(self, stack_pointer, nargs)
            assert (res != NULL) ^ (_PyErr_Occurred(tstate) != NULL)
            i: int = 0
            while i < nargs:
                Py_DECREF(stack_pointer[i])
                i += 1
            Py_DECREF(self)
            STACK_SHRINK(2 - is_meth)
            SET_TOP(res)
            Py_DECREF(callable)
            if res == NULL:
                return  # goto error
            else:
                print()
            JUMPBY(INLINE_CACHE_ENTRIES_CALL)
            CHECK_EVAL_BREAKER()
            DISPATCH()
        case ops.CALL_FUNCTION_EX:
            PREDICTED(CALL_FUNCTION_EX)
            func: PyObject
            callargs: PyObject
            kwargs: PyObject = NULL
            result: PyObject
            if oparg & 0x01:
                kwargs = POP()
                assert PyDict_CheckExact(kwargs)
            else:
                print()
            callargs = POP()
            func = PEEK(1)
            if not PyTuple_CheckExact(callargs):
                if check_args_iterable(tstate, func, callargs) < 0:
                    Py_DECREF(callargs)
                    return  # goto error
                else:
                    print()
                Py_SETREF(callargs, PySequence_Tuple(callargs))
                if callargs == NULL:
                    return  # goto error
                else:
                    print()
            else:
                print()
            assert PyTuple_CheckExact(callargs)
            result = do_call_core(tstate, func, callargs, kwargs, cframe.use_tracing)
            Py_DECREF(func)
            Py_DECREF(callargs)
            Py_XDECREF(kwargs)
            STACK_SHRINK(1)
            assert PEEK(1) == NULL
            SET_TOP(result)
            if result == NULL:
                return  # goto error
            else:
                print()
            CHECK_EVAL_BREAKER()
            DISPATCH()
        case ops.MAKE_FUNCTION:
            codeobj: PyObject = POP()
            func: PyFunctionObject = PyFunctionObject(
                PyFunction_New(codeobj, GLOBALS())
            )
            Py_DECREF(codeobj)
            if func == NULL:
                return  # goto error
            else:
                print()
            if oparg & 0x08:
                assert PyTuple_CheckExact(PEEK(1))
                func.func_closure = POP()
            else:
                print()
            if oparg & 0x04:
                assert PyTuple_CheckExact(PEEK(1))
                func.func_annotations = POP()
            else:
                print()
            if oparg & 0x02:
                assert PyDict_CheckExact(PEEK(1))
                func.func_kwdefaults = POP()
            else:
                print()
            if oparg & 0x01:
                assert PyTuple_CheckExact(PEEK(1))
                func.func_defaults = POP()
            else:
                print()
            func.func_version = (PyCodeObject(codeobj)).co_version
            PUSH(PyObject(func))
            DISPATCH()
        case ops.RETURN_GENERATOR:
            assert PyFunction_Check(frame.f_funcobj)
            func: PyFunctionObject = PyFunctionObject(frame.f_funcobj)
            gen: PyGenObject = PyGenObject(_Py_MakeCoro(func))
            if gen == NULL:
                return  # goto error
            else:
                print()
            assert EMPTY()
            _PyFrame_SetStackPointer(frame, stack_pointer)
            gen_frame: _PyInterpreterFrame = _PyInterpreterFrame(gen.gi_iframe)
            _PyFrame_Copy(frame, gen_frame)
            assert frame.frame_obj == NULL
            gen.gi_frame_state = FRAME_CREATED
            gen_frame.owner = FRAME_OWNED_BY_GENERATOR
            _Py_LeaveRecursiveCallPy(tstate)
            assert frame != (entry_frame)
            prev: _PyInterpreterFrame = frame.previous
            _PyThreadState_PopFrame(tstate, frame)
            frame = cframe.current_frame = prev  # (cframe.current_frame = prev)
            _PyFrame_StackPush(frame, PyObject(gen))
            return  # goto resume_frame
        case ops.BUILD_SLICE:
            start: PyObject
            stop: PyObject
            step: PyObject
            slice: PyObject
            if oparg == 3:
                step = POP()
            else:
                step = NULL
            stop = POP()
            start = PEEK(1)
            slice = PySlice_New(start, stop, step)
            Py_DECREF(start)
            Py_DECREF(stop)
            Py_XDECREF(step)
            SET_TOP(slice)
            if slice == NULL:
                return  # goto error
            else:
                print()
            DISPATCH()
        case ops.FORMAT_VALUE:
            result: PyObject
            fmt_spec: PyObject
            value: PyObject
            conv_fn: PyObject
            which_conversion: int = oparg & FVC_MASK
            have_fmt_spec: int = (oparg & FVS_MASK) == FVS_HAVE_SPEC
            fmt_spec = POP() if have_fmt_spec else NULL
            value = POP()
            match which_conversion:
                case FVC_NONE:
                    conv_fn = NULL
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
                        tstate,
                        PyExc_SystemError,
                        "unexpected conversion flag %d",
                        which_conversion,
                    )
                    return  # goto error
            if conv_fn != NULL:
                result = conv_fn(value)
                Py_DECREF(value)
                if result == NULL:
                    Py_XDECREF(fmt_spec)
                    return  # goto error
                else:
                    print()
                value = result
            else:
                print()
            if PyUnicode_CheckExact(value) and (fmt_spec == NULL):
                result = value
            else:
                result = PyObject_Format(value, fmt_spec)
                Py_DECREF(value)
                Py_XDECREF(fmt_spec)
                if result == NULL:
                    return  # goto error
                else:
                    print()
            PUSH(result)
            DISPATCH()
        case ops.COPY:
            assert oparg != 0
            peek: PyObject = PEEK(oparg)
            PUSH(Py_NewRef(peek))
            DISPATCH()
        case ops.BINARY_OP:
            PREDICTED(BINARY_OP)
            static_assert(INLINE_CACHE_ENTRIES_BINARY_OP == 1, "incorrect cache size")
            rhs: PyObject = PEEK(1)
            lhs: PyObject = PEEK(2)
            res: PyObject
            cache: _PyBinaryOpCache = _PyBinaryOpCache(next_instr)
            if ADAPTIVE_COUNTER_IS_ZERO(cache.counter):
                assert cframe.use_tracing == 0
                next_instr -= 1
                _Py_Specialize_BinaryOp(
                    lhs, rhs, next_instr, oparg, frame.localsplus[0]
                )
                DISPATCH_SAME_OPARG()
            else:
                print()
            STAT_INC(BINARY_OP, deferred)
            DECREMENT_ADAPTIVE_COUNTER(cache.counter)
            assert 0 <= oparg
            assert (unsigned(oparg)) < Py_ARRAY_LENGTH(binary_ops)
            assert binary_ops[oparg]
            res = binary_ops[oparg](lhs, rhs)
            Py_DECREF(lhs)
            Py_DECREF(rhs)
            if res == NULL:
                return  # goto pop_2_error
            else:
                print()
            STACK_SHRINK(1)
            POKE(1, res)
            JUMPBY(1)
            DISPATCH()
        case ops.SWAP:
            assert oparg != 0
            top: PyObject = PEEK(1)
            SET_TOP(PEEK(oparg))
            # PEEK(oparg) = top
            DISPATCH()
        case ops.EXTENDED_ARG:
            assert oparg
            assert cframe.use_tracing == 0
            opcode = _Py_OPCODE(next_instr)
            oparg = (oparg << 8) | _Py_OPARG(next_instr)
            PRE_DISPATCH_GOTO()
            DISPATCH_GOTO()
        case ops.CACHE:
            Py_UNREACHABLE()
    # label: error:
    # label: exception_unwind:
    # label: handle_eval_breaker:
    # label: resume_frame:
    # label: resume_with_error:
    # label: start_frame:
    # label: unbound_local_error:
