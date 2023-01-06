from typing import Any
from pytype.pyc import opcodes as ops

def interpreter(tstate: st.Pointer[PyThreadState], frame: st.Pointer[_PyInterpreterFrame], opcode: unsigned_char, oparg: unsigned_int, eval_breaker: st.Pointer[_Py_atomic_int], cframe: _PyCFrame, names: st.Pointer[PyObject], consts: st.Pointer[PyObject], next_instr: st.Pointer[_Py_CODEUNIT], stack_pointer: st.Pointer[st.Pointer[PyObject]], kwnames: st.Pointer[PyObject], throwflag: int, binary_ops: st.ndarray[..., binaryfunc]) -> st.Pointer[PyObject]:
    entry_frame: _PyInterpreterFrame
    match opcode:
        case 'NOP':
            DISPATCH()
        case 'RESUME':
            assert(tstate.cframe == ref(cframe))
            assert(frame == cframe.current_frame)
            if __c11_atomic_load(ref(eval_breaker._value), _Py_memory_order_relaxed) and oparg < 2:
                'break # goto handle_eval_breaker'
            DISPATCH()
        case 'LOAD_CLOSURE':
            value: st.Pointer[PyObject]
            value = frame.localsplus[oparg]
            if value == cast(0, type=st.Pointer[void]):
                'break # goto unbound_local_error'
            _Py_INCREF(cast(value, type=st.Pointer[PyObject]))
            STACK_GROW(1)
            POKE(1, value)
            DISPATCH()
        case 'LOAD_FAST_CHECK':
            value: st.Pointer[PyObject]
            value = frame.localsplus[oparg]
            if value == cast(0, type=st.Pointer[void]):
                'break # goto unbound_local_error'
            _Py_INCREF(cast(value, type=st.Pointer[PyObject]))
            STACK_GROW(1)
            POKE(1, value)
            DISPATCH()
        case 'LOAD_FAST':
            value: st.Pointer[PyObject]
            value = frame.localsplus[oparg]
            assert(value != cast(0, type=st.Pointer[void]))
            _Py_INCREF(cast(value, type=st.Pointer[PyObject]))
            STACK_GROW(1)
            POKE(1, value)
            DISPATCH()
        case 'LOAD_CONST':
            PREDICTED(100)
            value: st.Pointer[PyObject]
            value = GETITEM(consts, oparg)
            _Py_INCREF(cast(value, type=st.Pointer[PyObject]))
            STACK_GROW(1)
            POKE(1, value)
            DISPATCH()
        case 'STORE_FAST':
            value: st.Pointer[PyObject] = PEEK(1)
            SETLOCAL(oparg, value)
            STACK_SHRINK(1)
            DISPATCH()
        case 'LOAD_FAST__LOAD_FAST':
            _tmp_1: st.Pointer[PyObject]
            _tmp_2: st.Pointer[PyObject]
            value: st.Pointer[PyObject]
            value = frame.localsplus[oparg]
            assert(value != cast(0, type=st.Pointer[void]))
            _Py_INCREF(cast(value, type=st.Pointer[PyObject]))
            _tmp_2 = value
            NEXTOPARG()
            cast(0, type=void)
            value: st.Pointer[PyObject]
            value = frame.localsplus[oparg]
            assert(value != cast(0, type=st.Pointer[void]))
            _Py_INCREF(cast(value, type=st.Pointer[PyObject]))
            _tmp_1 = value
            STACK_GROW(2)
            POKE(1, _tmp_1)
            POKE(2, _tmp_2)
            DISPATCH()
        case 'LOAD_FAST__LOAD_CONST':
            _tmp_1: st.Pointer[PyObject]
            _tmp_2: st.Pointer[PyObject]
            value: st.Pointer[PyObject]
            value = frame.localsplus[oparg]
            assert(value != cast(0, type=st.Pointer[void]))
            _Py_INCREF(cast(value, type=st.Pointer[PyObject]))
            _tmp_2 = value
            NEXTOPARG()
            cast(0, type=void)
            value: st.Pointer[PyObject]
            value = GETITEM(consts, oparg)
            _Py_INCREF(cast(value, type=st.Pointer[PyObject]))
            _tmp_1 = value
            STACK_GROW(2)
            POKE(1, _tmp_1)
            POKE(2, _tmp_2)
            DISPATCH()
        case 'STORE_FAST__LOAD_FAST':
            _tmp_1: st.Pointer[PyObject] = PEEK(1)
            value: st.Pointer[PyObject] = _tmp_1
            SETLOCAL(oparg, value)
            NEXTOPARG()
            cast(0, type=void)
            value: st.Pointer[PyObject]
            value = frame.localsplus[oparg]
            assert(value != cast(0, type=st.Pointer[void]))
            _Py_INCREF(cast(value, type=st.Pointer[PyObject]))
            _tmp_1 = value
            POKE(1, _tmp_1)
            DISPATCH()
        case 'STORE_FAST__STORE_FAST':
            _tmp_1: st.Pointer[PyObject] = PEEK(1)
            _tmp_2: st.Pointer[PyObject] = PEEK(2)
            value: st.Pointer[PyObject] = _tmp_1
            SETLOCAL(oparg, value)
            NEXTOPARG()
            cast(0, type=void)
            value: st.Pointer[PyObject] = _tmp_2
            SETLOCAL(oparg, value)
            STACK_SHRINK(2)
            DISPATCH()
        case 'LOAD_CONST__LOAD_FAST':
            _tmp_1: st.Pointer[PyObject]
            _tmp_2: st.Pointer[PyObject]
            value: st.Pointer[PyObject]
            value = GETITEM(consts, oparg)
            _Py_INCREF(cast(value, type=st.Pointer[PyObject]))
            _tmp_2 = value
            NEXTOPARG()
            cast(0, type=void)
            value: st.Pointer[PyObject]
            value = frame.localsplus[oparg]
            assert(value != cast(0, type=st.Pointer[void]))
            _Py_INCREF(cast(value, type=st.Pointer[PyObject]))
            _tmp_1 = value
            STACK_GROW(2)
            POKE(1, _tmp_1)
            POKE(2, _tmp_2)
            DISPATCH()
        case 'POP_TOP':
            value: st.Pointer[PyObject] = PEEK(1)
            _Py_DECREF(cast(value, type=st.Pointer[PyObject]))
            STACK_SHRINK(1)
            DISPATCH()
        case 'PUSH_NULL':
            res: st.Pointer[PyObject]
            res = cast(0, type=st.Pointer[void])
            STACK_GROW(1)
            POKE(1, res)
            DISPATCH()
        case 'END_FOR':
            _tmp_1: st.Pointer[PyObject] = PEEK(1)
            _tmp_2: st.Pointer[PyObject] = PEEK(2)
            value: st.Pointer[PyObject] = _tmp_1
            _Py_DECREF(cast(value, type=st.Pointer[PyObject]))
            value: st.Pointer[PyObject] = _tmp_2
            _Py_DECREF(cast(value, type=st.Pointer[PyObject]))
            STACK_SHRINK(2)
            DISPATCH()
        case 'UNARY_POSITIVE':
            value: st.Pointer[PyObject] = PEEK(1)
            res: st.Pointer[PyObject]
            res = PyNumber_Positive(value)
            _Py_DECREF(cast(value, type=st.Pointer[PyObject]))
            if res == cast(0, type=st.Pointer[void]):
                'break # goto pop_1_error'
            POKE(1, res)
            DISPATCH()
        case 'UNARY_NEGATIVE':
            value: st.Pointer[PyObject] = PEEK(1)
            res: st.Pointer[PyObject]
            res = PyNumber_Negative(value)
            _Py_DECREF(cast(value, type=st.Pointer[PyObject]))
            if res == cast(0, type=st.Pointer[void]):
                'break # goto pop_1_error'
            POKE(1, res)
            DISPATCH()
        case 'UNARY_NOT':
            value: st.Pointer[PyObject] = PEEK(1)
            res: st.Pointer[PyObject]
            err: int = PyObject_IsTrue(value)
            _Py_DECREF(cast(value, type=st.Pointer[PyObject]))
            if err < 0:
                'break # goto pop_1_error'
            if err == 0:
                res = cast(ref(_Py_TrueStruct), type=st.Pointer[PyObject])
            else:
                res = cast(ref(_Py_FalseStruct), type=st.Pointer[PyObject])
            _Py_INCREF(cast(res, type=st.Pointer[PyObject]))
            POKE(1, res)
            DISPATCH()
        case 'UNARY_INVERT':
            value: st.Pointer[PyObject] = PEEK(1)
            res: st.Pointer[PyObject]
            res = PyNumber_Invert(value)
            _Py_DECREF(cast(value, type=st.Pointer[PyObject]))
            if res == cast(0, type=st.Pointer[void]):
                'break # goto pop_1_error'
            POKE(1, res)
            DISPATCH()
        case 'BINARY_OP_MULTIPLY_INT':
            right: st.Pointer[PyObject] = PEEK(1)
            left: st.Pointer[PyObject] = PEEK(2)
            prod: st.Pointer[PyObject]
            assert(cframe.use_tracing == 0)
            cast(0, type=void)
            cast(0, type=void)
            cast(0, type=void)
            prod = _PyLong_Multiply(cast(left, type=st.Pointer[PyLongObject]), cast(right, type=st.Pointer[PyLongObject]))
            _Py_DECREF_SPECIALIZED(right, cast(PyObject_Free, type=destructor))
            _Py_DECREF_SPECIALIZED(left, cast(PyObject_Free, type=destructor))
            if prod == cast(0, type=st.Pointer[void]):
                'break # goto pop_2_error'
            STACK_SHRINK(1)
            POKE(1, prod)
            cast(0, type=void)
            DISPATCH()
        case 'BINARY_OP_MULTIPLY_FLOAT':
            right: st.Pointer[PyObject] = PEEK(1)
            left: st.Pointer[PyObject] = PEEK(2)
            prod: st.Pointer[PyObject]
            assert(cframe.use_tracing == 0)
            cast(0, type=void)
            cast(0, type=void)
            cast(0, type=void)
            dprod: double = cast(left, type=st.Pointer[PyFloatObject]).ob_fval * cast(right, type=st.Pointer[PyFloatObject]).ob_fval
            prod = PyFloat_FromDouble(dprod)
            _Py_DECREF_SPECIALIZED(right, _PyFloat_ExactDealloc)
            _Py_DECREF_SPECIALIZED(left, _PyFloat_ExactDealloc)
            if prod == cast(0, type=st.Pointer[void]):
                'break # goto pop_2_error'
            STACK_SHRINK(1)
            POKE(1, prod)
            cast(0, type=void)
            DISPATCH()
        case 'BINARY_OP_SUBTRACT_INT':
            right: st.Pointer[PyObject] = PEEK(1)
            left: st.Pointer[PyObject] = PEEK(2)
            sub: st.Pointer[PyObject]
            assert(cframe.use_tracing == 0)
            cast(0, type=void)
            cast(0, type=void)
            cast(0, type=void)
            sub = _PyLong_Subtract(cast(left, type=st.Pointer[PyLongObject]), cast(right, type=st.Pointer[PyLongObject]))
            _Py_DECREF_SPECIALIZED(right, cast(PyObject_Free, type=destructor))
            _Py_DECREF_SPECIALIZED(left, cast(PyObject_Free, type=destructor))
            if sub == cast(0, type=st.Pointer[void]):
                'break # goto pop_2_error'
            STACK_SHRINK(1)
            POKE(1, sub)
            cast(0, type=void)
            DISPATCH()
        case 'BINARY_OP_SUBTRACT_FLOAT':
            right: st.Pointer[PyObject] = PEEK(1)
            left: st.Pointer[PyObject] = PEEK(2)
            sub: st.Pointer[PyObject]
            assert(cframe.use_tracing == 0)
            cast(0, type=void)
            cast(0, type=void)
            cast(0, type=void)
            dsub: double = cast(left, type=st.Pointer[PyFloatObject]).ob_fval - cast(right, type=st.Pointer[PyFloatObject]).ob_fval
            sub = PyFloat_FromDouble(dsub)
            _Py_DECREF_SPECIALIZED(right, _PyFloat_ExactDealloc)
            _Py_DECREF_SPECIALIZED(left, _PyFloat_ExactDealloc)
            if sub == cast(0, type=st.Pointer[void]):
                'break # goto pop_2_error'
            STACK_SHRINK(1)
            POKE(1, sub)
            cast(0, type=void)
            DISPATCH()
        case 'BINARY_OP_ADD_UNICODE':
            right: st.Pointer[PyObject] = PEEK(1)
            left: st.Pointer[PyObject] = PEEK(2)
            res: st.Pointer[PyObject]
            assert(cframe.use_tracing == 0)
            cast(0, type=void)
            cast(0, type=void)
            cast(0, type=void)
            res = PyUnicode_Concat(left, right)
            _Py_DECREF_SPECIALIZED(left, _PyUnicode_ExactDealloc)
            _Py_DECREF_SPECIALIZED(right, _PyUnicode_ExactDealloc)
            if res == cast(0, type=st.Pointer[void]):
                'break # goto pop_2_error'
            STACK_SHRINK(1)
            POKE(1, res)
            cast(0, type=void)
            DISPATCH()
        case 'BINARY_OP_INPLACE_ADD_UNICODE':
            right: st.Pointer[PyObject] = PEEK(1)
            left: st.Pointer[PyObject] = PEEK(2)
            assert(cframe.use_tracing == 0)
            cast(0, type=void)
            cast(0, type=void)
            true_next: _Py_CODEUNIT = next_instr[sizeof(_PyBinaryOpCache) / sizeof(_Py_CODEUNIT)]
            assert(true_next & 255 == 125 or true_next & 255 == STORE_FAST__LOAD_FAST)
            target_local: st.Pointer[st.Pointer[PyObject]] = ref(frame.localsplus[true_next >> 8])
            cast(0, type=void)
            cast(0, type=void)
            assert(_Py_REFCNT(cast(left, type=st.Pointer[st.Const[PyObject]])) >= 2)
            _Py_DECREF_NO_DEALLOC(left)
            PyUnicode_Append(target_local, right)
            _Py_DECREF_SPECIALIZED(right, _PyUnicode_ExactDealloc)
            if deref(target_local) == cast(0, type=st.Pointer[void]):
                'break # goto pop_2_error'
            cast(0, type=void)
            STACK_SHRINK(2)
            DISPATCH()
        case 'BINARY_OP_ADD_FLOAT':
            right: st.Pointer[PyObject] = PEEK(1)
            left: st.Pointer[PyObject] = PEEK(2)
            sum: st.Pointer[PyObject]
            assert(cframe.use_tracing == 0)
            cast(0, type=void)
            cast(0, type=void)
            cast(0, type=void)
            dsum: double = cast(left, type=st.Pointer[PyFloatObject]).ob_fval + cast(right, type=st.Pointer[PyFloatObject]).ob_fval
            sum = PyFloat_FromDouble(dsum)
            _Py_DECREF_SPECIALIZED(right, _PyFloat_ExactDealloc)
            _Py_DECREF_SPECIALIZED(left, _PyFloat_ExactDealloc)
            if sum == cast(0, type=st.Pointer[void]):
                'break # goto pop_2_error'
            STACK_SHRINK(1)
            POKE(1, sum)
            cast(0, type=void)
            DISPATCH()
        case 'BINARY_OP_ADD_INT':
            right: st.Pointer[PyObject] = PEEK(1)
            left: st.Pointer[PyObject] = PEEK(2)
            sum: st.Pointer[PyObject]
            assert(cframe.use_tracing == 0)
            cast(0, type=void)
            cast(0, type=void)
            cast(0, type=void)
            sum = _PyLong_Add(cast(left, type=st.Pointer[PyLongObject]), cast(right, type=st.Pointer[PyLongObject]))
            _Py_DECREF_SPECIALIZED(right, cast(PyObject_Free, type=destructor))
            _Py_DECREF_SPECIALIZED(left, cast(PyObject_Free, type=destructor))
            if sum == cast(0, type=st.Pointer[void]):
                'break # goto pop_2_error'
            STACK_SHRINK(1)
            POKE(1, sum)
            cast(0, type=void)
            DISPATCH()
        case 'BINARY_SUBSCR':
            PREDICTED(25)
            assert sizeof(_PyBinarySubscrCache) / sizeof(_Py_CODEUNIT) == 4, 'incorrect cache size'
            pass
            sub: st.Pointer[PyObject] = PEEK(1)
            container: st.Pointer[PyObject] = PEEK(2)
            res: st.Pointer[PyObject]
            cache: st.Pointer[_PyBinarySubscrCache] = cast(next_instr, type=st.Pointer[_PyBinarySubscrCache])
            if ADAPTIVE_COUNTER_IS_ZERO(cache.counter):
                assert(cframe.use_tracing == 0)
                next_instr -= 1
                _Py_Specialize_BinarySubscr(container, sub, next_instr)
                cast(0, type=void)
            cast(0, type=void)
            DECREMENT_ADAPTIVE_COUNTER(cache.counter)
            res = PyObject_GetItem(container, sub)
            _Py_DECREF(cast(container, type=st.Pointer[PyObject]))
            _Py_DECREF(cast(sub, type=st.Pointer[PyObject]))
            if res == cast(0, type=st.Pointer[void]):
                'break # goto pop_2_error'
            STACK_SHRINK(1)
            POKE(1, res)
            cast(0, type=void)
            DISPATCH()
        case 'BINARY_SLICE':
            stop: st.Pointer[PyObject] = PEEK(1)
            start: st.Pointer[PyObject] = PEEK(2)
            container: st.Pointer[PyObject] = PEEK(3)
            res: st.Pointer[PyObject]
            slice: st.Pointer[PyObject] = _PyBuildSlice_ConsumeRefs(start, stop)
            if slice == cast(0, type=st.Pointer[void]):
                res = cast(0, type=st.Pointer[void])
            else:
                res = PyObject_GetItem(container, slice)
                _Py_DECREF(cast(slice, type=st.Pointer[PyObject]))
            _Py_DECREF(cast(container, type=st.Pointer[PyObject]))
            if res == cast(0, type=st.Pointer[void]):
                'break # goto pop_3_error'
            STACK_SHRINK(2)
            POKE(1, res)
            DISPATCH()
        case 'STORE_SLICE':
            stop: st.Pointer[PyObject] = PEEK(1)
            start: st.Pointer[PyObject] = PEEK(2)
            container: st.Pointer[PyObject] = PEEK(3)
            v: st.Pointer[PyObject] = PEEK(4)
            slice: st.Pointer[PyObject] = _PyBuildSlice_ConsumeRefs(start, stop)
            err: int
            if slice == cast(0, type=st.Pointer[void]):
                err = 1
            else:
                err = PyObject_SetItem(container, slice, v)
                _Py_DECREF(cast(slice, type=st.Pointer[PyObject]))
            _Py_DECREF(cast(v, type=st.Pointer[PyObject]))
            _Py_DECREF(cast(container, type=st.Pointer[PyObject]))
            if err:
                'break # goto pop_4_error'
            STACK_SHRINK(4)
            DISPATCH()
        case 'BINARY_SUBSCR_LIST_INT':
            sub: st.Pointer[PyObject] = PEEK(1)
            list: st.Pointer[PyObject] = PEEK(2)
            res: st.Pointer[PyObject]
            assert(cframe.use_tracing == 0)
            cast(0, type=void)
            cast(0, type=void)
            cast(0, type=void)
            assert(cast(_PyLong_GetZero(), type=st.Pointer[PyLongObject]).ob_digit[0] == 0)
            index: Py_ssize_t = cast(sub, type=st.Pointer[PyLongObject]).ob_digit[0]
            cast(0, type=void)
            cast(0, type=void)
            res = assert(PyType_HasFeature(cast(list, type=st.Pointer[PyObject]).ob_type, 1 << 25)).ob_item[index]
            assert(res != cast(0, type=st.Pointer[void]))
            _Py_INCREF(cast(res, type=st.Pointer[PyObject]))
            _Py_DECREF_SPECIALIZED(sub, cast(PyObject_Free, type=destructor))
            _Py_DECREF(cast(list, type=st.Pointer[PyObject]))
            STACK_SHRINK(1)
            POKE(1, res)
            cast(0, type=void)
            DISPATCH()
        case 'BINARY_SUBSCR_TUPLE_INT':
            sub: st.Pointer[PyObject] = PEEK(1)
            tuple: st.Pointer[PyObject] = PEEK(2)
            res: st.Pointer[PyObject]
            assert(cframe.use_tracing == 0)
            cast(0, type=void)
            cast(0, type=void)
            cast(0, type=void)
            assert(cast(_PyLong_GetZero(), type=st.Pointer[PyLongObject]).ob_digit[0] == 0)
            index: Py_ssize_t = cast(sub, type=st.Pointer[PyLongObject]).ob_digit[0]
            cast(0, type=void)
            cast(0, type=void)
            res = assert(PyType_HasFeature(cast(tuple, type=st.Pointer[PyObject]).ob_type, 1 << 26)).ob_item[index]
            assert(res != cast(0, type=st.Pointer[void]))
            _Py_INCREF(cast(res, type=st.Pointer[PyObject]))
            _Py_DECREF_SPECIALIZED(sub, cast(PyObject_Free, type=destructor))
            _Py_DECREF(cast(tuple, type=st.Pointer[PyObject]))
            STACK_SHRINK(1)
            POKE(1, res)
            cast(0, type=void)
            DISPATCH()
        case 'BINARY_SUBSCR_DICT':
            sub: st.Pointer[PyObject] = PEEK(1)
            dict: st.Pointer[PyObject] = PEEK(2)
            res: st.Pointer[PyObject]
            assert(cframe.use_tracing == 0)
            cast(0, type=void)
            cast(0, type=void)
            res = PyDict_GetItemWithError(dict, sub)
            if res == cast(0, type=st.Pointer[void]):
                if not _PyErr_Occurred(tstate):
                    _PyErr_SetKeyError(sub)
                _Py_DECREF(cast(dict, type=st.Pointer[PyObject]))
                _Py_DECREF(cast(sub, type=st.Pointer[PyObject]))
                if 1:
                    'break # goto pop_2_error'
            _Py_INCREF(cast(res, type=st.Pointer[PyObject]))
            _Py_DECREF(cast(dict, type=st.Pointer[PyObject]))
            _Py_DECREF(cast(sub, type=st.Pointer[PyObject]))
            STACK_SHRINK(1)
            POKE(1, res)
            cast(0, type=void)
            DISPATCH()
        case 'BINARY_SUBSCR_GETITEM':
            sub: st.Pointer[PyObject] = PEEK(1)
            container: st.Pointer[PyObject] = PEEK(2)
            type_version: uint32_t = read_u32(ref(next_instr[1].cache))
            func_version: uint16_t = read_u16(ref(next_instr[3].cache))
            tp: st.Pointer[PyTypeObject] = cast(container, type=st.Pointer[PyObject]).ob_type
            cast(0, type=void)
            assert(tp.tp_flags & 1 << 9)
            cached: st.Pointer[PyObject] = cast(tp, type=st.Pointer[PyHeapTypeObject])._spec_cache.getitem
            assert(_Py_IS_TYPE(cast(cached, type=st.Pointer[st.Const[PyObject]]), ref(PyFunction_Type)))
            getitem: st.Pointer[PyFunctionObject] = cast(cached, type=st.Pointer[PyFunctionObject])
            cast(0, type=void)
            code: st.Pointer[PyCodeObject] = cast(getitem.func_code, type=st.Pointer[PyCodeObject])
            assert(code.co_argcount == 2)
            cast(0, type=void)
            cast(0, type=void)
            _Py_INCREF(cast(getitem, type=st.Pointer[PyObject]))
            new_frame: st.Pointer[_PyInterpreterFrame] = _PyFrame_PushUnchecked(tstate, getitem)
            STACK_SHRINK(2)
            new_frame.localsplus[0] = container
            new_frame.localsplus[1] = sub
            for i in range(2, code.co_nlocalsplus, 1):
                new_frame.localsplus[i] = cast(0, type=st.Pointer[void])
            cast(0, type=void)
            DISPATCH_INLINED(new_frame)
        case 'LIST_APPEND':
            v: st.Pointer[PyObject] = PEEK(1)
            list: st.Pointer[PyObject] = PEEK(oparg + 1)
            if _PyList_AppendTakeRef(cast(list, type=st.Pointer[PyListObject]), v) < 0:
                'break # goto pop_1_error'
            STACK_SHRINK(1)
            PREDICT(JUMP_BACKWARD)
            DISPATCH()
        case 'SET_ADD':
            v: st.Pointer[PyObject] = PEEK(1)
            set: st.Pointer[PyObject] = PEEK(oparg + 1)
            err: int = PySet_Add(set, v)
            _Py_DECREF(cast(v, type=st.Pointer[PyObject]))
            if err:
                'break # goto pop_1_error'
            STACK_SHRINK(1)
            PREDICT(JUMP_BACKWARD)
            DISPATCH()
        case 'STORE_SUBSCR':
            PREDICTED(60)
            sub: st.Pointer[PyObject] = PEEK(1)
            container: st.Pointer[PyObject] = PEEK(2)
            v: st.Pointer[PyObject] = PEEK(3)
            counter: uint16_t = read_u16(ref(next_instr[0].cache))
            if ADAPTIVE_COUNTER_IS_ZERO(counter):
                assert(cframe.use_tracing == 0)
                next_instr -= 1
                _Py_Specialize_StoreSubscr(container, sub, next_instr)
                cast(0, type=void)
            cast(0, type=void)
            cache: st.Pointer[_PyStoreSubscrCache] = cast(next_instr, type=st.Pointer[_PyStoreSubscrCache])
            DECREMENT_ADAPTIVE_COUNTER(cache.counter)
            err: int = PyObject_SetItem(container, sub, v)
            _Py_DECREF(cast(v, type=st.Pointer[PyObject]))
            _Py_DECREF(cast(container, type=st.Pointer[PyObject]))
            _Py_DECREF(cast(sub, type=st.Pointer[PyObject]))
            if err:
                'break # goto pop_3_error'
            STACK_SHRINK(3)
            cast(0, type=void)
            DISPATCH()
        case 'STORE_SUBSCR_LIST_INT':
            sub: st.Pointer[PyObject] = PEEK(1)
            list: st.Pointer[PyObject] = PEEK(2)
            value: st.Pointer[PyObject] = PEEK(3)
            assert(cframe.use_tracing == 0)
            cast(0, type=void)
            cast(0, type=void)
            cast(0, type=void)
            index: Py_ssize_t = cast(sub, type=st.Pointer[PyLongObject]).ob_digit[0]
            cast(0, type=void)
            cast(0, type=void)
            old_value: st.Pointer[PyObject] = assert(PyType_HasFeature(cast(list, type=st.Pointer[PyObject]).ob_type, 1 << 25)).ob_item[index]
            cast(
            assert(PyType_HasFeature(cast(list, type=st.Pointer[PyObject]).ob_type, 1 << 25)).ob_item[index] = value, type=void)
            assert(old_value != cast(0, type=st.Pointer[void]))
            _Py_DECREF(cast(old_value, type=st.Pointer[PyObject]))
            _Py_DECREF_SPECIALIZED(sub, cast(PyObject_Free, type=destructor))
            _Py_DECREF(cast(list, type=st.Pointer[PyObject]))
            STACK_SHRINK(3)
            cast(0, type=void)
            DISPATCH()
        case 'STORE_SUBSCR_DICT':
            sub: st.Pointer[PyObject] = PEEK(1)
            dict: st.Pointer[PyObject] = PEEK(2)
            value: st.Pointer[PyObject] = PEEK(3)
            assert(cframe.use_tracing == 0)
            cast(0, type=void)
            cast(0, type=void)
            err: int = _PyDict_SetItem_Take2(cast(dict, type=st.Pointer[PyDictObject]), sub, value)
            _Py_DECREF(cast(dict, type=st.Pointer[PyObject]))
            if err:
                'break # goto pop_3_error'
            STACK_SHRINK(3)
            cast(0, type=void)
            DISPATCH()
        case 'DELETE_SUBSCR':
            sub: st.Pointer[PyObject] = PEEK(1)
            container: st.Pointer[PyObject] = PEEK(2)
            err: int = PyObject_DelItem(container, sub)
            _Py_DECREF(cast(container, type=st.Pointer[PyObject]))
            _Py_DECREF(cast(sub, type=st.Pointer[PyObject]))
            if err:
                'break # goto pop_2_error'
            STACK_SHRINK(2)
            DISPATCH()
        case 'PRINT_EXPR':
            value: st.Pointer[PyObject] = PEEK(1)
            hook: st.Pointer[PyObject] = _PySys_GetAttr(tstate, ref(_PyRuntime.static_objects.singletons.strings.identifiers._py_displayhook._ascii.ob_base))
            res: st.Pointer[PyObject]
            if hook == cast(0, type=st.Pointer[void]):
                _PyErr_SetString(tstate, PyExc_RuntimeError, 'lost sys.displayhook')
                _Py_DECREF(cast(value, type=st.Pointer[PyObject]))
                if 1:
                    'break # goto pop_1_error'
            res = PyObject_CallOneArg(hook, value)
            _Py_DECREF(cast(value, type=st.Pointer[PyObject]))
            if res == cast(0, type=st.Pointer[void]):
                'break # goto pop_1_error'
            _Py_DECREF(cast(res, type=st.Pointer[PyObject]))
            STACK_SHRINK(1)
            DISPATCH()
        case 'RAISE_VARARGS':
            cause: st.Pointer[PyObject] = cast(0, type=st.Pointer[void])
            exc: st.Pointer[PyObject] = cast(0, type=st.Pointer[void])
            match oparg:
                case 2:
                    cause = POP()
                case 1:
                    exc = POP()
                case 0:
                    if do_raise(tstate, exc, cause):
                        'break # goto exception_unwind'
                    return
                case True:_PyErr_SetString(tstate, PyExc_SystemError, 'bad RAISE_VARARGS oparg')
                    return
            'break # goto error'
        case 'INTERPRETER_EXIT':
            retval: st.Pointer[PyObject] = PEEK(1)
            assert(frame == ref(entry_frame))
            assert(_PyFrame_IsIncomplete(frame))
            STACK_SHRINK(1)
            assert(EMPTY())
            tstate.cframe = cframe.previous
            tstate.cframe.use_tracing = cframe.use_tracing
            assert(tstate.cframe.current_frame == frame.previous)
            assert(not _PyErr_Occurred(tstate))
            _Py_LeaveRecursiveCallTstate(tstate)
            return retval
        case 'RETURN_VALUE':
            retval: st.Pointer[PyObject] = PEEK(1)
            STACK_SHRINK(1)
            assert(EMPTY())
            _PyFrame_SetStackPointer(frame, stack_pointer)
            TRACE_FUNCTION_EXIT()
            DTRACE_FUNCTION_EXIT()
            _Py_LeaveRecursiveCallPy(tstate)
            assert(frame != ref(entry_frame))
            dying: st.Pointer[_PyInterpreterFrame] = frame
            frame = 
            cframe.current_frame = dying.previous
            _PyEvalFrameClearAndPop(tstate, dying)
            _PyFrame_StackPush(frame, retval)
            'break # goto resume_frame'
        case 'GET_AITER':
            obj: st.Pointer[PyObject] = PEEK(1)
            iter: st.Pointer[PyObject]
            getter: unaryfunc = cast(0, type=st.Pointer[void])
            type: st.Pointer[PyTypeObject] = cast(obj, type=st.Pointer[PyObject]).ob_type
            if type.tp_as_async != cast(0, type=st.Pointer[void]):
                getter = type.tp_as_async.am_aiter
            if getter == cast(0, type=st.Pointer[void]):
                _PyErr_Format(tstate, PyExc_TypeError, "'async for' requires an object with __aiter__ method, got %.100s", type.tp_name)
                _Py_DECREF(cast(obj, type=st.Pointer[PyObject]))
                if 1:
                    'break # goto pop_1_error'
            iter = deref(getter)(obj)
            _Py_DECREF(cast(obj, type=st.Pointer[PyObject]))
            if iter == cast(0, type=st.Pointer[void]):
                'break # goto pop_1_error'
            if cast(iter, type=st.Pointer[PyObject]).ob_type.tp_as_async == cast(0, type=st.Pointer[void]) or cast(iter, type=st.Pointer[PyObject]).ob_type.tp_as_async.am_anext == cast(0, type=st.Pointer[void]):
                _PyErr_Format(tstate, PyExc_TypeError, "'async for' received an object from __aiter__ that does not implement __anext__: %.100s", cast(iter, type=st.Pointer[PyObject]).ob_type.tp_name)
                _Py_DECREF(cast(iter, type=st.Pointer[PyObject]))
                if 1:
                    'break # goto pop_1_error'
            POKE(1, iter)
            DISPATCH()
        case 'GET_ANEXT':
            aiter: st.Pointer[PyObject] = PEEK(1)
            awaitable: st.Pointer[PyObject]
            getter: unaryfunc = cast(0, type=st.Pointer[void])
            next_iter: st.Pointer[PyObject] = cast(0, type=st.Pointer[void])
            type: st.Pointer[PyTypeObject] = cast(aiter, type=st.Pointer[PyObject]).ob_type
            if _Py_IS_TYPE(cast(aiter, type=st.Pointer[st.Const[PyObject]]), ref(PyAsyncGen_Type)):
                awaitable = type.tp_as_async.am_anext(aiter)
                if awaitable == cast(0, type=st.Pointer[void]):
                    'break # goto error'
            else:
                if type.tp_as_async != cast(0, type=st.Pointer[void]):
                    getter = type.tp_as_async.am_anext
                if getter != cast(0, type=st.Pointer[void]):
                    next_iter = deref(getter)(aiter)
                    if next_iter == cast(0, type=st.Pointer[void]):
                        'break # goto error'
                else:
                    _PyErr_Format(tstate, PyExc_TypeError, "'async for' requires an iterator with __anext__ method, got %.100s", type.tp_name)
                    'break # goto error'
                awaitable = _PyCoro_GetAwaitableIter(next_iter)
                if awaitable == cast(0, type=st.Pointer[void]):
                    _PyErr_FormatFromCause(PyExc_TypeError, "'async for' received an invalid object from __anext__: %.100s", cast(next_iter, type=st.Pointer[PyObject]).ob_type.tp_name)
                    _Py_DECREF(cast(next_iter, type=st.Pointer[PyObject]))
                    'break # goto error'
                else:
                    _Py_DECREF(cast(next_iter, type=st.Pointer[PyObject]))
            STACK_GROW(1)
            POKE(1, awaitable)
            PREDICT(100)
            DISPATCH()
        case 'GET_AWAITABLE':
            PREDICTED(73)
            iterable: st.Pointer[PyObject] = PEEK(1)
            iter: st.Pointer[PyObject]
            iter = _PyCoro_GetAwaitableIter(iterable)
            if iter == cast(0, type=st.Pointer[void]):
                format_awaitable_error(tstate, cast(iterable, type=st.Pointer[PyObject]).ob_type, oparg)
            _Py_DECREF(cast(iterable, type=st.Pointer[PyObject]))
            if iter != cast(0, type=st.Pointer[void]) and _Py_IS_TYPE(cast(iter, type=st.Pointer[st.Const[PyObject]]), ref(PyCoro_Type)):
                yf: st.Pointer[PyObject] = _PyGen_yf(cast(iter, type=st.Pointer[PyGenObject]))
                if yf != cast(0, type=st.Pointer[void]):
                    _Py_DECREF(cast(yf, type=st.Pointer[PyObject]))
                    Py_CLEAR(iter)
                    _PyErr_SetString(tstate, PyExc_RuntimeError, 'coroutine is being awaited already')
            if iter == cast(0, type=st.Pointer[void]):
                'break # goto pop_1_error'
            POKE(1, iter)
            PREDICT(100)
            DISPATCH()
        case 'SEND':
            assert(frame != ref(entry_frame))
            assert(STACK_LEVEL() >= 2)
            v: st.Pointer[PyObject] = POP()
            receiver: st.Pointer[PyObject] = TOP()
            gen_status: PySendResult
            retval: st.Pointer[PyObject]
            if tstate.c_tracefunc == cast(0, type=st.Pointer[void]):
                gen_status = PyIter_Send(receiver, v, ref(retval))
            else:
                if v == ref(_Py_NoneStruct) and PyIter_Check(receiver):
                    retval = cast(receiver, type=st.Pointer[PyObject]).ob_type.tp_iternext(receiver)
                else:
                    retval = PyObject_CallMethodOneArg(receiver, ref(_PyRuntime.static_objects.singletons.strings.identifiers._py_send._ascii.ob_base), v)
                if retval == cast(0, type=st.Pointer[void]):
                    if tstate.c_tracefunc != cast(0, type=st.Pointer[void]) and _PyErr_ExceptionMatches(tstate, PyExc_StopIteration):
                        call_exc_trace(tstate.c_tracefunc, tstate.c_traceobj, tstate, frame)
                    if _PyGen_FetchStopIterationValue(ref(retval)) == 0:
                        gen_status = PYGEN_RETURN
                    else:
                        gen_status = PYGEN_ERROR
                else:
                    gen_status = PYGEN_NEXT
            _Py_DECREF(cast(v, type=st.Pointer[PyObject]))
            if gen_status == PYGEN_ERROR:
                assert(retval == cast(0, type=st.Pointer[void]))
                'break # goto error'
            if gen_status == PYGEN_RETURN:
                assert(retval != cast(0, type=st.Pointer[void]))
                _Py_DECREF(cast(receiver, type=st.Pointer[PyObject]))
                SET_TOP(retval)
                cast(0, type=void)
            else:
                assert(gen_status == PYGEN_NEXT)
                assert(retval != cast(0, type=st.Pointer[void]))
                PUSH(retval)
            DISPATCH()
        case 'ASYNC_GEN_WRAP':
            v: st.Pointer[PyObject] = PEEK(1)
            w: st.Pointer[PyObject]
            assert(frame.f_code.co_flags & 512)
            w = _PyAsyncGenValueWrapperNew(v)
            _Py_DECREF(cast(v, type=st.Pointer[PyObject]))
            if w == cast(0, type=st.Pointer[void]):
                'break # goto pop_1_error'
            POKE(1, w)
            DISPATCH()
        case 'YIELD_VALUE':
            retval: st.Pointer[PyObject] = PEEK(1)
            assert(oparg == STACK_LEVEL())
            assert(frame != ref(entry_frame))
            gen: st.Pointer[PyGenObject] = _PyFrame_GetGenerator(frame)
            gen.gi_frame_state = FRAME_SUSPENDED
            _PyFrame_SetStackPointer(frame, stack_pointer - 1)
            TRACE_FUNCTION_EXIT()
            DTRACE_FUNCTION_EXIT()
            tstate.exc_info = gen.gi_exc_state.previous_item
            gen.gi_exc_state.previous_item = cast(0, type=st.Pointer[void])
            _Py_LeaveRecursiveCallPy(tstate)
            gen_frame: st.Pointer[_PyInterpreterFrame] = frame
            frame = 
            cframe.current_frame = frame.previous
            gen_frame.previous = cast(0, type=st.Pointer[void])
            frame.prev_instr -= frame.yield_offset
            _PyFrame_StackPush(frame, retval)
            'break # goto resume_frame'
        case 'POP_EXCEPT':
            exc_value: st.Pointer[PyObject] = PEEK(1)
            exc_info: st.Pointer[_PyErr_StackItem] = tstate.exc_info
            Py_XSETREF(exc_info.exc_value, exc_value)
            STACK_SHRINK(1)
            DISPATCH()
        case 'RERAISE':
            if oparg:
                lasti: st.Pointer[PyObject] = PEEK(oparg + 1)
                if PyLong_Check(lasti):
                    frame.prev_instr = _PyCode_CODE(frame.f_code) + PyLong_AsLong(lasti)
                    assert(not _PyErr_Occurred(tstate))
                else:
                    assert(PyLong_Check(lasti))
                    _PyErr_SetString(tstate, PyExc_SystemError, 'lasti is not an int')
                    'break # goto error'
            val: st.Pointer[PyObject] = POP()
            assert(val and PyExceptionInstance_Check(val))
            exc: st.Pointer[PyObject] = _Py_NewRef(cast(_PyType_Check(cast(val, type=st.Pointer[PyObject])) and PyType_HasFeature(cast(val, type=st.Pointer[PyTypeObject]), 1 << 30), type=st.Pointer[PyObject]))
            tb: st.Pointer[PyObject] = PyException_GetTraceback(val)
            _PyErr_Restore(tstate, exc, val, tb)
            'break # goto exception_unwind'
        case 'PREP_RERAISE_STAR':
            excs: st.Pointer[PyObject] = PEEK(1)
            orig: st.Pointer[PyObject] = PEEK(2)
            val: st.Pointer[PyObject]
            assert(PyType_HasFeature(cast(excs, type=st.Pointer[PyObject]).ob_type, 1 << 25))
            val = _PyExc_PrepReraiseStar(orig, excs)
            _Py_DECREF(cast(orig, type=st.Pointer[PyObject]))
            _Py_DECREF(cast(excs, type=st.Pointer[PyObject]))
            if val == cast(0, type=st.Pointer[void]):
                'break # goto pop_2_error'
            STACK_SHRINK(1)
            POKE(1, val)
            DISPATCH()
        case 'END_ASYNC_FOR':
            val: st.Pointer[PyObject] = POP()
            assert(val and PyExceptionInstance_Check(val))
            if PyErr_GivenExceptionMatches(val, PyExc_StopAsyncIteration):
                _Py_DECREF(cast(val, type=st.Pointer[PyObject]))
                _Py_DECREF(cast(POP(), type=st.Pointer[PyObject]))
            else:
                exc: st.Pointer[PyObject] = _Py_NewRef(cast(_PyType_Check(cast(val, type=st.Pointer[PyObject])) and PyType_HasFeature(cast(val, type=st.Pointer[PyTypeObject]), 1 << 30), type=st.Pointer[PyObject]))
                tb: st.Pointer[PyObject] = PyException_GetTraceback(val)
                _PyErr_Restore(tstate, exc, val, tb)
                'break # goto exception_unwind'
            DISPATCH()
        case 'CLEANUP_THROW':
            assert(throwflag)
            exc_value: st.Pointer[PyObject] = TOP()
            assert(exc_value and PyExceptionInstance_Check(exc_value))
            if PyErr_GivenExceptionMatches(exc_value, PyExc_StopIteration):
                value: st.Pointer[PyObject] = cast(exc_value, type=st.Pointer[PyStopIterationObject]).value
                _Py_INCREF(cast(value, type=st.Pointer[PyObject]))
                _Py_DECREF(cast(POP(), type=st.Pointer[PyObject]))
                _Py_DECREF(cast(POP(), type=st.Pointer[PyObject]))
                _Py_DECREF(cast(POP(), type=st.Pointer[PyObject]))
                PUSH(value)
            else:
                exc_type: st.Pointer[PyObject] = _Py_NewRef(cast(cast(exc_value, type=st.Pointer[PyObject]).ob_type, type=st.Pointer[PyObject]))
                exc_traceback: st.Pointer[PyObject] = PyException_GetTraceback(exc_value)
                _PyErr_Restore(tstate, exc_type, _Py_NewRef(cast(exc_value, type=st.Pointer[PyObject])), exc_traceback)
                'break # goto exception_unwind'
            DISPATCH()
        case 'STOPITERATION_ERROR':
            assert(frame.owner == FRAME_OWNED_BY_GENERATOR)
            exc: st.Pointer[PyObject] = TOP()
            assert(PyExceptionInstance_Check(exc))
            msg: st.Pointer[st.Const[char]] = cast(0, type=st.Pointer[void])
            if PyErr_GivenExceptionMatches(exc, PyExc_StopIteration):
                msg = 'generator raised StopIteration'
                if frame.f_code.co_flags & 512:
                    msg = 'async generator raised StopIteration'
                elif frame.f_code.co_flags & 128:
                    msg = 'coroutine raised StopIteration'
            elif frame.f_code.co_flags & 512 and PyErr_GivenExceptionMatches(exc, PyExc_StopAsyncIteration):
                msg = 'async generator raised StopAsyncIteration'
            if msg != cast(0, type=st.Pointer[void]):
                message: st.Pointer[PyObject] = _PyUnicode_FromASCII(msg, strlen(msg))
                if message == cast(0, type=st.Pointer[void]):
                    'break # goto error'
                error: st.Pointer[PyObject] = PyObject_CallOneArg(PyExc_RuntimeError, message)
                if error == cast(0, type=st.Pointer[void]):
                    _Py_DECREF(cast(message, type=st.Pointer[PyObject]))
                    'break # goto error'
                assert(PyExceptionInstance_Check(error))
                SET_TOP(error)
                PyException_SetCause(error, _Py_NewRef(cast(exc, type=st.Pointer[PyObject])))
                PyException_SetContext(error, exc)
                _Py_DECREF(cast(message, type=st.Pointer[PyObject]))
            DISPATCH()
        case 'LOAD_ASSERTION_ERROR':
            value: st.Pointer[PyObject]
            value = _Py_NewRef(cast(PyExc_AssertionError, type=st.Pointer[PyObject]))
            STACK_GROW(1)
            POKE(1, value)
            DISPATCH()
        case 'LOAD_BUILD_CLASS':
            bc: st.Pointer[PyObject]
            if _Py_IS_TYPE(cast(BUILTINS(), type=st.Pointer[st.Const[PyObject]]), ref(PyDict_Type)):
                bc = _PyDict_GetItemWithError(BUILTINS(), ref(_PyRuntime.static_objects.singletons.strings.identifiers._py___build_class__._ascii.ob_base))
                if bc == cast(0, type=st.Pointer[void]):
                    if not _PyErr_Occurred(tstate):
                        _PyErr_SetString(tstate, PyExc_NameError, '__build_class__ not found')
                    if 1:
                        'break # goto error'
                _Py_INCREF(cast(bc, type=st.Pointer[PyObject]))
            else:
                bc = PyObject_GetItem(BUILTINS(), ref(_PyRuntime.static_objects.singletons.strings.identifiers._py___build_class__._ascii.ob_base))
                if bc == cast(0, type=st.Pointer[void]):
                    if _PyErr_ExceptionMatches(tstate, PyExc_KeyError):
                        _PyErr_SetString(tstate, PyExc_NameError, '__build_class__ not found')
                    if 1:
                        'break # goto error'
            STACK_GROW(1)
            POKE(1, bc)
            DISPATCH()
        case 'STORE_NAME':
            v: st.Pointer[PyObject] = PEEK(1)
            name: st.Pointer[PyObject] = GETITEM(names, oparg)
            ns: st.Pointer[PyObject] = LOCALS()
            err: int
            if ns == cast(0, type=st.Pointer[void]):
                _PyErr_Format(tstate, PyExc_SystemError, 'no locals found when storing %R', name)
                _Py_DECREF(cast(v, type=st.Pointer[PyObject]))
                if 1:
                    'break # goto pop_1_error'
            if _Py_IS_TYPE(cast(ns, type=st.Pointer[st.Const[PyObject]]), ref(PyDict_Type)):
                err = PyDict_SetItem(ns, name, v)
            else:
                err = PyObject_SetItem(ns, name, v)
            _Py_DECREF(cast(v, type=st.Pointer[PyObject]))
            if err:
                'break # goto pop_1_error'
            STACK_SHRINK(1)
            DISPATCH()
        case 'DELETE_NAME':
            name: st.Pointer[PyObject] = GETITEM(names, oparg)
            ns: st.Pointer[PyObject] = LOCALS()
            err: int
            if ns == cast(0, type=st.Pointer[void]):
                _PyErr_Format(tstate, PyExc_SystemError, 'no locals when deleting %R', name)
                'break # goto error'
            err = PyObject_DelItem(ns, name)
            if err != 0:
                format_exc_check_arg(tstate, PyExc_NameError, "name '%.200s' is not defined", name)
                'break # goto error'
            DISPATCH()
        case 'UNPACK_SEQUENCE':
            PREDICTED(92)
            cache: st.Pointer[_PyUnpackSequenceCache] = cast(next_instr, type=st.Pointer[_PyUnpackSequenceCache])
            if ADAPTIVE_COUNTER_IS_ZERO(cache.counter):
                assert(cframe.use_tracing == 0)
                seq: st.Pointer[PyObject] = TOP()
                next_instr -= 1
                _Py_Specialize_UnpackSequence(seq, next_instr, oparg)
                cast(0, type=void)
            cast(0, type=void)
            DECREMENT_ADAPTIVE_COUNTER(cache.counter)
            seq: st.Pointer[PyObject] = POP()
            top: st.Pointer[st.Pointer[PyObject]] = stack_pointer + oparg
            if not unpack_iterable(tstate, seq, oparg, -1, top):
                _Py_DECREF(cast(seq, type=st.Pointer[PyObject]))
                'break # goto error'
            STACK_GROW(oparg)
            _Py_DECREF(cast(seq, type=st.Pointer[PyObject]))
            cast(0, type=void)
            DISPATCH()
        case 'UNPACK_SEQUENCE_TWO_TUPLE':
            seq: st.Pointer[PyObject] = TOP()
            cast(0, type=void)
            cast(0, type=void)
            cast(0, type=void)
            SET_TOP(_Py_NewRef(cast(assert(PyType_HasFeature(cast(seq, type=st.Pointer[PyObject]).ob_type, 1 << 26)).ob_item[1], type=st.Pointer[PyObject])))
            PUSH(_Py_NewRef(cast(assert(PyType_HasFeature(cast(seq, type=st.Pointer[PyObject]).ob_type, 1 << 26)).ob_item[0], type=st.Pointer[PyObject])))
            _Py_DECREF(cast(seq, type=st.Pointer[PyObject]))
            cast(0, type=void)
            DISPATCH()
        case 'UNPACK_SEQUENCE_TUPLE':
            seq: st.Pointer[PyObject] = TOP()
            cast(0, type=void)
            cast(0, type=void)
            cast(0, type=void)
            STACK_SHRINK(1)
            items: st.Pointer[st.Pointer[PyObject]] = cast(0, type=void)assert(PyType_HasFeature(cast(seq, type=st.Pointer[PyObject]).ob_type, 1 << 26)).ob_item
            while 
            oparg:
                PUSH(_Py_NewRef(cast(items[oparg], type=st.Pointer[PyObject])))
                oparg -= 1
            _Py_DECREF(cast(seq, type=st.Pointer[PyObject]))
            cast(0, type=void)
            DISPATCH()
        case 'UNPACK_SEQUENCE_LIST':
            seq: st.Pointer[PyObject] = TOP()
            cast(0, type=void)
            cast(0, type=void)
            cast(0, type=void)
            STACK_SHRINK(1)
            items: st.Pointer[st.Pointer[PyObject]] = cast(0, type=void)assert(PyType_HasFeature(cast(seq, type=st.Pointer[PyObject]).ob_type, 1 << 25)).ob_item
            while 
            oparg:
                PUSH(_Py_NewRef(cast(items[oparg], type=st.Pointer[PyObject])))
                oparg -= 1
            _Py_DECREF(cast(seq, type=st.Pointer[PyObject]))
            cast(0, type=void)
            DISPATCH()
        case 'UNPACK_EX':
            totalargs: int = 1 + (oparg & 255) + (oparg >> 8)
            seq: st.Pointer[PyObject] = POP()
            top: st.Pointer[st.Pointer[PyObject]] = stack_pointer + totalargs
            if not unpack_iterable(tstate, seq, oparg & 255, oparg >> 8, top):
                _Py_DECREF(cast(seq, type=st.Pointer[PyObject]))
                'break # goto error'
            STACK_GROW(totalargs)
            _Py_DECREF(cast(seq, type=st.Pointer[PyObject]))
            DISPATCH()
        case 'STORE_ATTR':
            PREDICTED(95)
            owner: st.Pointer[PyObject] = PEEK(1)
            v: st.Pointer[PyObject] = PEEK(2)
            counter: uint16_t = read_u16(ref(next_instr[0].cache))
            if ADAPTIVE_COUNTER_IS_ZERO(counter):
                assert(cframe.use_tracing == 0)
                name: st.Pointer[PyObject] = GETITEM(names, oparg)
                next_instr -= 1
                _Py_Specialize_StoreAttr(owner, next_instr, name)
                cast(0, type=void)
            cast(0, type=void)
            cache: st.Pointer[_PyAttrCache] = cast(next_instr, type=st.Pointer[_PyAttrCache])
            DECREMENT_ADAPTIVE_COUNTER(cache.counter)
            name: st.Pointer[PyObject] = GETITEM(names, oparg)
            err: int = PyObject_SetAttr(owner, name, v)
            _Py_DECREF(cast(v, type=st.Pointer[PyObject]))
            _Py_DECREF(cast(owner, type=st.Pointer[PyObject]))
            if err:
                'break # goto pop_2_error'
            STACK_SHRINK(2)
            cast(0, type=void)
            DISPATCH()
        case 'DELETE_ATTR':
            owner: st.Pointer[PyObject] = PEEK(1)
            name: st.Pointer[PyObject] = GETITEM(names, oparg)
            err: int = PyObject_SetAttr(owner, name, cast(cast(0, type=st.Pointer[void]), type=st.Pointer[PyObject]))
            _Py_DECREF(cast(owner, type=st.Pointer[PyObject]))
            if err:
                'break # goto pop_1_error'
            STACK_SHRINK(1)
            DISPATCH()
        case 'STORE_GLOBAL':
            v: st.Pointer[PyObject] = PEEK(1)
            name: st.Pointer[PyObject] = GETITEM(names, oparg)
            err: int = PyDict_SetItem(GLOBALS(), name, v)
            _Py_DECREF(cast(v, type=st.Pointer[PyObject]))
            if err:
                'break # goto pop_1_error'
            STACK_SHRINK(1)
            DISPATCH()
        case 'DELETE_GLOBAL':
            name: st.Pointer[PyObject] = GETITEM(names, oparg)
            err: int
            err = PyDict_DelItem(GLOBALS(), name)
            if err != 0:
                if _PyErr_ExceptionMatches(tstate, PyExc_KeyError):
                    format_exc_check_arg(tstate, PyExc_NameError, "name '%.200s' is not defined", name)
                'break # goto error'
            DISPATCH()
        case 'LOAD_NAME':
            v: st.Pointer[PyObject]
            name: st.Pointer[PyObject] = GETITEM(names, oparg)
            locals: st.Pointer[PyObject] = LOCALS()
            if locals == cast(0, type=st.Pointer[void]):
                _PyErr_Format(tstate, PyExc_SystemError, 'no locals when loading %R', name)
                'break # goto error'
            if _Py_IS_TYPE(cast(locals, type=st.Pointer[st.Const[PyObject]]), ref(PyDict_Type)):
                v = PyDict_GetItemWithError(locals, name)
                if v != cast(0, type=st.Pointer[void]):
                    _Py_INCREF(cast(v, type=st.Pointer[PyObject]))
                elif _PyErr_Occurred(tstate):
                    'break # goto error'
            else:
                v = PyObject_GetItem(locals, name)
                if v == cast(0, type=st.Pointer[void]):
                    if not _PyErr_ExceptionMatches(tstate, PyExc_KeyError):
                        'break # goto error'
                    _PyErr_Clear(tstate)
            if v == cast(0, type=st.Pointer[void]):
                v = PyDict_GetItemWithError(GLOBALS(), name)
                if v != cast(0, type=st.Pointer[void]):
                    _Py_INCREF(cast(v, type=st.Pointer[PyObject]))
                elif _PyErr_Occurred(tstate):
                    'break # goto error'
                elif _Py_IS_TYPE(cast(BUILTINS(), type=st.Pointer[st.Const[PyObject]]), ref(PyDict_Type)):
                    v = PyDict_GetItemWithError(BUILTINS(), name)
                    if v == cast(0, type=st.Pointer[void]):
                        if not _PyErr_Occurred(tstate):
                            format_exc_check_arg(tstate, PyExc_NameError, "name '%.200s' is not defined", name)
                        'break # goto error'
                    _Py_INCREF(cast(v, type=st.Pointer[PyObject]))
                else:
                    v = PyObject_GetItem(BUILTINS(), name)
                    if v == cast(0, type=st.Pointer[void]):
                        if _PyErr_ExceptionMatches(tstate, PyExc_KeyError):
                            format_exc_check_arg(tstate, PyExc_NameError, "name '%.200s' is not defined", name)
                        'break # goto error'
            STACK_GROW(1)
            POKE(1, v)
            DISPATCH()
        case 'LOAD_GLOBAL':
            PREDICTED(116)
            cache: st.Pointer[_PyLoadGlobalCache] = cast(next_instr, type=st.Pointer[_PyLoadGlobalCache])
            if ADAPTIVE_COUNTER_IS_ZERO(cache.counter):
                assert(cframe.use_tracing == 0)
                name: st.Pointer[PyObject] = GETITEM(names, oparg >> 1)
                next_instr -= 1
                _Py_Specialize_LoadGlobal(GLOBALS(), BUILTINS(), next_instr, name)
                cast(0, type=void)
            cast(0, type=void)
            DECREMENT_ADAPTIVE_COUNTER(cache.counter)
            push_null: int = oparg & 1
            PEEK(0) = cast(0, type=st.Pointer[void])
            name: st.Pointer[PyObject] = GETITEM(names, oparg >> 1)
            v: st.Pointer[PyObject]
            if _Py_IS_TYPE(cast(GLOBALS(), type=st.Pointer[st.Const[PyObject]]), ref(PyDict_Type)) and _Py_IS_TYPE(cast(BUILTINS(), type=st.Pointer[st.Const[PyObject]]), ref(PyDict_Type)):
                v = _PyDict_LoadGlobal(cast(GLOBALS(), type=st.Pointer[PyDictObject]), cast(BUILTINS(), type=st.Pointer[PyDictObject]), name)
                if v == cast(0, type=st.Pointer[void]):
                    if not _PyErr_Occurred(tstate):
                        format_exc_check_arg(tstate, PyExc_NameError, "name '%.200s' is not defined", name)
                    'break # goto error'
                _Py_INCREF(cast(v, type=st.Pointer[PyObject]))
            else:
                v = PyObject_GetItem(GLOBALS(), name)
                if v == cast(0, type=st.Pointer[void]):
                    if not _PyErr_ExceptionMatches(tstate, PyExc_KeyError):
                        'break # goto error'
                    _PyErr_Clear(tstate)
                    v = PyObject_GetItem(BUILTINS(), name)
                    if v == cast(0, type=st.Pointer[void]):
                        if _PyErr_ExceptionMatches(tstate, PyExc_KeyError):
                            format_exc_check_arg(tstate, PyExc_NameError, "name '%.200s' is not defined", name)
                        'break # goto error'
            cast(0, type=void)
            STACK_GROW(push_null)
            PUSH(v)
            DISPATCH()
        case 'LOAD_GLOBAL_MODULE':
            assert(cframe.use_tracing == 0)
            cast(0, type=void)
            dict: st.Pointer[PyDictObject] = cast(GLOBALS(), type=st.Pointer[PyDictObject])
            cache: st.Pointer[_PyLoadGlobalCache] = cast(next_instr, type=st.Pointer[_PyLoadGlobalCache])
            version: uint32_t = read_u32(cache.module_keys_version)
            cast(0, type=void)
            assert(dict.ma_keys.dk_kind != DICT_KEYS_GENERAL)
            entries: st.Pointer[PyDictUnicodeEntry] = DK_UNICODE_ENTRIES(dict.ma_keys)
            res: st.Pointer[PyObject] = entries[cache.index].me_value
            cast(0, type=void)
            push_null: int = oparg & 1
            PEEK(0) = cast(0, type=st.Pointer[void])
            cast(0, type=void)
            cast(0, type=void)
            STACK_GROW(push_null + 1)
            SET_TOP(_Py_NewRef(cast(res, type=st.Pointer[PyObject])))
            DISPATCH()
        case 'LOAD_GLOBAL_BUILTIN':
            assert(cframe.use_tracing == 0)
            cast(0, type=void)
            cast(0, type=void)
            mdict: st.Pointer[PyDictObject] = cast(GLOBALS(), type=st.Pointer[PyDictObject])
            bdict: st.Pointer[PyDictObject] = cast(BUILTINS(), type=st.Pointer[PyDictObject])
            cache: st.Pointer[_PyLoadGlobalCache] = cast(next_instr, type=st.Pointer[_PyLoadGlobalCache])
            mod_version: uint32_t = read_u32(cache.module_keys_version)
            bltn_version: uint16_t = cache.builtin_keys_version
            cast(0, type=void)
            cast(0, type=void)
            assert(bdict.ma_keys.dk_kind != DICT_KEYS_GENERAL)
            entries: st.Pointer[PyDictUnicodeEntry] = DK_UNICODE_ENTRIES(bdict.ma_keys)
            res: st.Pointer[PyObject] = entries[cache.index].me_value
            cast(0, type=void)
            push_null: int = oparg & 1
            PEEK(0) = cast(0, type=st.Pointer[void])
            cast(0, type=void)
            cast(0, type=void)
            STACK_GROW(push_null + 1)
            SET_TOP(_Py_NewRef(cast(res, type=st.Pointer[PyObject])))
            DISPATCH()
        case 'DELETE_FAST':
            v: st.Pointer[PyObject] = frame.localsplus[oparg]
            if v == cast(0, type=st.Pointer[void]):
                'break # goto unbound_local_error'
            SETLOCAL(oparg, cast(0, type=st.Pointer[void]))
            DISPATCH()
        case 'MAKE_CELL':
            initial: st.Pointer[PyObject] = frame.localsplus[oparg]
            cell: st.Pointer[PyObject] = PyCell_New(initial)
            if cell == cast(0, type=st.Pointer[void]):
                'break # goto resume_with_error'
            SETLOCAL(oparg, cell)
            DISPATCH()
        case 'DELETE_DEREF':
            cell: st.Pointer[PyObject] = frame.localsplus[oparg]
            oldobj: st.Pointer[PyObject] = cast(cell, type=st.Pointer[PyCellObject]).ob_ref
            if oldobj == cast(0, type=st.Pointer[void]):
                format_exc_unbound(tstate, frame.f_code, oparg)
                'break # goto error'
            cast(
            cast(cell, type=st.Pointer[PyCellObject]).ob_ref = cast(0, type=st.Pointer[void]), type=void)
            _Py_DECREF(cast(oldobj, type=st.Pointer[PyObject]))
            DISPATCH()
        case 'LOAD_CLASSDEREF':
            value: st.Pointer[PyObject]
            name: st.Pointer[PyObject]
            locals: st.Pointer[PyObject] = LOCALS()
            assert(locals)
            assert(oparg >= 0 and oparg < frame.f_code.co_nlocalsplus)
            name = assert(PyType_HasFeature(cast(frame.f_code.co_localsplusnames, type=st.Pointer[PyObject]).ob_type, 1 << 26)).ob_item[oparg]
            if _Py_IS_TYPE(cast(locals, type=st.Pointer[st.Const[PyObject]]), ref(PyDict_Type)):
                value = PyDict_GetItemWithError(locals, name)
                if value != cast(0, type=st.Pointer[void]):
                    _Py_INCREF(cast(value, type=st.Pointer[PyObject]))
                elif _PyErr_Occurred(tstate):
                    'break # goto error'
            else:
                value = PyObject_GetItem(locals, name)
                if value == cast(0, type=st.Pointer[void]):
                    if not _PyErr_ExceptionMatches(tstate, PyExc_KeyError):
                        'break # goto error'
                    _PyErr_Clear(tstate)
            if not value:
                cell: st.Pointer[PyObject] = frame.localsplus[oparg]
                value = cast(cell, type=st.Pointer[PyCellObject]).ob_ref
                if value == cast(0, type=st.Pointer[void]):
                    format_exc_unbound(tstate, frame.f_code, oparg)
                    'break # goto error'
                _Py_INCREF(cast(value, type=st.Pointer[PyObject]))
            STACK_GROW(1)
            POKE(1, value)
            DISPATCH()
        case 'LOAD_DEREF':
            value: st.Pointer[PyObject]
            cell: st.Pointer[PyObject] = frame.localsplus[oparg]
            value = cast(cell, type=st.Pointer[PyCellObject]).ob_ref
            if value == cast(0, type=st.Pointer[void]):
                format_exc_unbound(tstate, frame.f_code, oparg)
                if 1:
                    'break # goto error'
            _Py_INCREF(cast(value, type=st.Pointer[PyObject]))
            STACK_GROW(1)
            POKE(1, value)
            DISPATCH()
        case 'STORE_DEREF':
            v: st.Pointer[PyObject] = PEEK(1)
            cell: st.Pointer[PyObject] = frame.localsplus[oparg]
            oldobj: st.Pointer[PyObject] = cast(cell, type=st.Pointer[PyCellObject]).ob_ref
            cast(
            cast(cell, type=st.Pointer[PyCellObject]).ob_ref = v, type=void)
            Py_XDECREF(oldobj)
            STACK_SHRINK(1)
            DISPATCH()
        case 'COPY_FREE_VARS':
            co: st.Pointer[PyCodeObject] = frame.f_code
            assert(_Py_IS_TYPE(cast(frame.f_funcobj, type=st.Pointer[st.Const[PyObject]]), ref(PyFunction_Type)))
            closure: st.Pointer[PyObject] = cast(frame.f_funcobj, type=st.Pointer[PyFunctionObject]).func_closure
            assert(oparg == co.co_nfreevars)
            offset: int = co.co_nlocalsplus - oparg
            for i in range(0, oparg, 1):
                o: st.Pointer[PyObject] = assert(PyType_HasFeature(cast(closure, type=st.Pointer[PyObject]).ob_type, 1 << 26)).ob_item[i]
                frame.localsplus[offset + i] = _Py_NewRef(cast(o, type=st.Pointer[PyObject]))
            DISPATCH()
        case 'BUILD_STRING':
            str: st.Pointer[PyObject]
            str = _PyUnicode_JoinArray(ref(_PyRuntime.static_objects.singletons.strings.literals._py_empty._ascii.ob_base), stack_pointer - oparg, oparg)
            if str == cast(0, type=st.Pointer[void]):
                'break # goto error'
            while 
            oparg -= 1 >= 0:
                item: st.Pointer[PyObject] = POP()
                _Py_DECREF(cast(item, type=st.Pointer[PyObject]))
            PUSH(str)
            DISPATCH()
        case 'BUILD_TUPLE':
            STACK_SHRINK(oparg)
            tup: st.Pointer[PyObject] = _PyTuple_FromArraySteal(stack_pointer, oparg)
            if tup == cast(0, type=st.Pointer[void]):
                'break # goto error'
            PUSH(tup)
            DISPATCH()
        case 'BUILD_LIST':
            STACK_SHRINK(oparg)
            list: st.Pointer[PyObject] = _PyList_FromArraySteal(stack_pointer, oparg)
            if list == cast(0, type=st.Pointer[void]):
                'break # goto error'
            PUSH(list)
            DISPATCH()
        case 'LIST_TO_TUPLE':
            list: st.Pointer[PyObject] = PEEK(1)
            tuple: st.Pointer[PyObject]
            tuple = PyList_AsTuple(list)
            _Py_DECREF(cast(list, type=st.Pointer[PyObject]))
            if tuple == cast(0, type=st.Pointer[void]):
                'break # goto pop_1_error'
            POKE(1, tuple)
            DISPATCH()
        case 'LIST_EXTEND':
            iterable: st.Pointer[PyObject] = PEEK(1)
            list: st.Pointer[PyObject] = PEEK(oparg + 1)
            none_val: st.Pointer[PyObject] = _PyList_Extend(cast(list, type=st.Pointer[PyListObject]), iterable)
            if none_val == cast(0, type=st.Pointer[void]):
                if _PyErr_ExceptionMatches(tstate, PyExc_TypeError) and (cast(iterable, type=st.Pointer[PyObject]).ob_type.tp_iter == cast(0, type=st.Pointer[void]) and (not PySequence_Check(iterable))):
                    _PyErr_Clear(tstate)
                    _PyErr_Format(tstate, PyExc_TypeError, 'Value after * must be an iterable, not %.200s', cast(iterable, type=st.Pointer[PyObject]).ob_type.tp_name)
                _Py_DECREF(cast(iterable, type=st.Pointer[PyObject]))
                if 1:
                    'break # goto pop_1_error'
            _Py_DECREF(cast(none_val, type=st.Pointer[PyObject]))
            _Py_DECREF(cast(iterable, type=st.Pointer[PyObject]))
            STACK_SHRINK(1)
            DISPATCH()
        case 'SET_UPDATE':
            iterable: st.Pointer[PyObject] = PEEK(1)
            set: st.Pointer[PyObject] = PEEK(oparg + 1)
            err: int = _PySet_Update(set, iterable)
            _Py_DECREF(cast(iterable, type=st.Pointer[PyObject]))
            if err < 0:
                'break # goto pop_1_error'
            STACK_SHRINK(1)
            DISPATCH()
        case 'BUILD_SET':
            set: st.Pointer[PyObject] = PySet_New(cast(0, type=st.Pointer[void]))
            err: int = 0
            i: int
            if set == cast(0, type=st.Pointer[void]):
                'break # goto error'
            for i in range(0, oparg, -1):
                item: st.Pointer[PyObject] = PEEK(i)
                if err == 0:
                    err = PySet_Add(set, item)
                _Py_DECREF(cast(item, type=st.Pointer[PyObject]))
            STACK_SHRINK(oparg)
            if err != 0:
                _Py_DECREF(cast(set, type=st.Pointer[PyObject]))
                'break # goto error'
            PUSH(set)
            DISPATCH()
        case 'BUILD_MAP':
            map: st.Pointer[PyObject] = _PyDict_FromItems(ref(PEEK(2 * oparg)), 2, ref(PEEK(2 * oparg - 1)), 2, oparg)
            if map == cast(0, type=st.Pointer[void]):
                'break # goto error'
            while 
            oparg:
                _Py_DECREF(cast(POP(), type=st.Pointer[PyObject]))
                _Py_DECREF(cast(POP(), type=st.Pointer[PyObject]))
                oparg -= 1
            PUSH(map)
            DISPATCH()
        case 'SETUP_ANNOTATIONS':
            err: int
            ann_dict: st.Pointer[PyObject]
            if LOCALS() == cast(0, type=st.Pointer[void]):
                _PyErr_Format(tstate, PyExc_SystemError, 'no locals found when setting up annotations')
                if 1:
                    'break # goto error'
            if _Py_IS_TYPE(cast(LOCALS(), type=st.Pointer[st.Const[PyObject]]), ref(PyDict_Type)):
                ann_dict = _PyDict_GetItemWithError(LOCALS(), ref(_PyRuntime.static_objects.singletons.strings.identifiers._py___annotations__._ascii.ob_base))
                if ann_dict == cast(0, type=st.Pointer[void]):
                    if _PyErr_Occurred(tstate):
                        'break # goto error'
                    ann_dict = PyDict_New()
                    if ann_dict == cast(0, type=st.Pointer[void]):
                        'break # goto error'
                    err = PyDict_SetItem(LOCALS(), ref(_PyRuntime.static_objects.singletons.strings.identifiers._py___annotations__._ascii.ob_base), ann_dict)
                    _Py_DECREF(cast(ann_dict, type=st.Pointer[PyObject]))
                    if err:
                        'break # goto error'
            else:
                ann_dict = PyObject_GetItem(LOCALS(), ref(_PyRuntime.static_objects.singletons.strings.identifiers._py___annotations__._ascii.ob_base))
                if ann_dict == cast(0, type=st.Pointer[void]):
                    if not _PyErr_ExceptionMatches(tstate, PyExc_KeyError):
                        'break # goto error'
                    _PyErr_Clear(tstate)
                    ann_dict = PyDict_New()
                    if ann_dict == cast(0, type=st.Pointer[void]):
                        'break # goto error'
                    err = PyObject_SetItem(LOCALS(), ref(_PyRuntime.static_objects.singletons.strings.identifiers._py___annotations__._ascii.ob_base), ann_dict)
                    _Py_DECREF(cast(ann_dict, type=st.Pointer[PyObject]))
                    if err:
                        'break # goto error'
                else:
                    _Py_DECREF(cast(ann_dict, type=st.Pointer[PyObject]))
            DISPATCH()
        case 'BUILD_CONST_KEY_MAP':
            map: st.Pointer[PyObject]
            keys: st.Pointer[PyObject] = TOP()
            if not _Py_IS_TYPE(cast(keys, type=st.Pointer[st.Const[PyObject]]), ref(PyTuple_Type)) or cast(assert(PyType_HasFeature(cast(keys, type=st.Pointer[PyObject]).ob_type, 1 << 26))cast(keys, type=st.Pointer[PyTupleObject]), type=st.Pointer[PyVarObject]).ob_size != cast(oparg, type=Py_ssize_t):
                _PyErr_SetString(tstate, PyExc_SystemError, 'bad BUILD_CONST_KEY_MAP keys argument')
                'break # goto error'
            map = _PyDict_FromItems(ref(assert(PyType_HasFeature(cast(keys, type=st.Pointer[PyObject]).ob_type, 1 << 26)).ob_item[0]), 1, ref(PEEK(oparg + 1)), 1, oparg)
            if map == cast(0, type=st.Pointer[void]):
                'break # goto error'
            _Py_DECREF(cast(POP(), type=st.Pointer[PyObject]))
            while 
            oparg:
                _Py_DECREF(cast(POP(), type=st.Pointer[PyObject]))
                oparg -= 1
            PUSH(map)
            DISPATCH()
        case 'DICT_UPDATE':
            update: st.Pointer[PyObject] = PEEK(1)
            dict: st.Pointer[PyObject] = PEEK(oparg + 1)
            if PyDict_Update(dict, update) < 0:
                if _PyErr_ExceptionMatches(tstate, PyExc_AttributeError):
                    _PyErr_Format(tstate, PyExc_TypeError, "'%.200s' object is not a mapping", cast(update, type=st.Pointer[PyObject]).ob_type.tp_name)
                _Py_DECREF(cast(update, type=st.Pointer[PyObject]))
                if 1:
                    'break # goto pop_1_error'
            _Py_DECREF(cast(update, type=st.Pointer[PyObject]))
            STACK_SHRINK(1)
            DISPATCH()
        case 'DICT_MERGE':
            update: st.Pointer[PyObject] = PEEK(1)
            dict: st.Pointer[PyObject] = PEEK(oparg + 1)
            if _PyDict_MergeEx(dict, update, 2) < 0:
                format_kwargs_error(tstate, PEEK(3 + oparg), update)
                _Py_DECREF(cast(update, type=st.Pointer[PyObject]))
                if 1:
                    'break # goto pop_1_error'
            _Py_DECREF(cast(update, type=st.Pointer[PyObject]))
            STACK_SHRINK(1)
            PREDICT(142)
            DISPATCH()
        case 'MAP_ADD':
            value: st.Pointer[PyObject] = PEEK(1)
            key: st.Pointer[PyObject] = PEEK(2)
            dict: st.Pointer[PyObject] = PEEK(oparg + 2)
            assert(_Py_IS_TYPE(cast(dict, type=st.Pointer[st.Const[PyObject]]), ref(PyDict_Type)))
            if _PyDict_SetItem_Take2(cast(dict, type=st.Pointer[PyDictObject]), key, value) != 0:
                'break # goto pop_2_error'
            STACK_SHRINK(2)
            PREDICT(JUMP_BACKWARD)
            DISPATCH()
        case 'LOAD_ATTR':
            PREDICTED(106)
            cache: st.Pointer[_PyAttrCache] = cast(next_instr, type=st.Pointer[_PyAttrCache])
            if ADAPTIVE_COUNTER_IS_ZERO(cache.counter):
                assert(cframe.use_tracing == 0)
                owner: st.Pointer[PyObject] = TOP()
                name: st.Pointer[PyObject] = GETITEM(names, oparg >> 1)
                next_instr -= 1
                _Py_Specialize_LoadAttr(owner, next_instr, name)
                cast(0, type=void)
            cast(0, type=void)
            DECREMENT_ADAPTIVE_COUNTER(cache.counter)
            name: st.Pointer[PyObject] = GETITEM(names, oparg >> 1)
            owner: st.Pointer[PyObject] = TOP()
            if oparg & 1:
                meth: st.Pointer[PyObject] = cast(0, type=st.Pointer[void])
                meth_found: int = _PyObject_GetMethod(owner, name, ref(meth))
                if meth == cast(0, type=st.Pointer[void]):
                    'break # goto error'
                if meth_found:
                    SET_TOP(meth)
                    PUSH(owner)
                else:
                    SET_TOP(cast(0, type=st.Pointer[void]))
                    _Py_DECREF(cast(owner, type=st.Pointer[PyObject]))
                    PUSH(meth)
            else:
                res: st.Pointer[PyObject] = PyObject_GetAttr(owner, name)
                if res == cast(0, type=st.Pointer[void]):
                    'break # goto error'
                _Py_DECREF(cast(owner, type=st.Pointer[PyObject]))
                SET_TOP(res)
            cast(0, type=void)
            DISPATCH()
        case 'LOAD_ATTR_INSTANCE_VALUE':
            assert(cframe.use_tracing == 0)
            owner: st.Pointer[PyObject] = TOP()
            res: st.Pointer[PyObject]
            tp: st.Pointer[PyTypeObject] = cast(owner, type=st.Pointer[PyObject]).ob_type
            cache: st.Pointer[_PyAttrCache] = cast(next_instr, type=st.Pointer[_PyAttrCache])
            type_version: uint32_t = read_u32(cache.version)
            assert(type_version != 0)
            cast(0, type=void)
            assert(tp.tp_dictoffset < 0)
            assert(tp.tp_flags & 1 << 4)
            dorv: PyDictOrValues = deref(_PyObject_DictOrValuesPointer(owner))
            cast(0, type=void)
            res = _PyDictOrValues_GetValues(dorv).values[cache.index]
            cast(0, type=void)
            cast(0, type=void)
            _Py_INCREF(cast(res, type=st.Pointer[PyObject]))
            SET_TOP(cast(0, type=st.Pointer[void]))
            STACK_GROW(oparg & 1)
            SET_TOP(res)
            _Py_DECREF(cast(owner, type=st.Pointer[PyObject]))
            cast(0, type=void)
            DISPATCH()
        case 'LOAD_ATTR_MODULE':
            assert(cframe.use_tracing == 0)
            owner: st.Pointer[PyObject] = TOP()
            res: st.Pointer[PyObject]
            cache: st.Pointer[_PyAttrCache] = cast(next_instr, type=st.Pointer[_PyAttrCache])
            cast(0, type=void)
            dict: st.Pointer[PyDictObject] = cast(cast(owner, type=st.Pointer[PyModuleObject]).md_dict, type=st.Pointer[PyDictObject])
            assert(dict != cast(0, type=st.Pointer[void]))
            cast(0, type=void)
            assert(dict.ma_keys.dk_kind == DICT_KEYS_UNICODE)
            assert(cache.index < dict.ma_keys.dk_nentries)
            ep: st.Pointer[PyDictUnicodeEntry] = DK_UNICODE_ENTRIES(dict.ma_keys) + cache.index
            res = ep.me_value
            cast(0, type=void)
            cast(0, type=void)
            _Py_INCREF(cast(res, type=st.Pointer[PyObject]))
            SET_TOP(cast(0, type=st.Pointer[void]))
            STACK_GROW(oparg & 1)
            SET_TOP(res)
            _Py_DECREF(cast(owner, type=st.Pointer[PyObject]))
            cast(0, type=void)
            DISPATCH()
        case 'LOAD_ATTR_WITH_HINT':
            assert(cframe.use_tracing == 0)
            owner: st.Pointer[PyObject] = TOP()
            res: st.Pointer[PyObject]
            tp: st.Pointer[PyTypeObject] = cast(owner, type=st.Pointer[PyObject]).ob_type
            cache: st.Pointer[_PyAttrCache] = cast(next_instr, type=st.Pointer[_PyAttrCache])
            type_version: uint32_t = read_u32(cache.version)
            assert(type_version != 0)
            cast(0, type=void)
            assert(tp.tp_flags & 1 << 4)
            dorv: PyDictOrValues = deref(_PyObject_DictOrValuesPointer(owner))
            cast(0, type=void)
            dict: st.Pointer[PyDictObject] = cast(_PyDictOrValues_GetDict(dorv), type=st.Pointer[PyDictObject])
            cast(0, type=void)
            assert(_Py_IS_TYPE(cast(cast(dict, type=st.Pointer[PyObject]), type=st.Pointer[st.Const[PyObject]]), ref(PyDict_Type)))
            name: st.Pointer[PyObject] = GETITEM(names, oparg >> 1)
            hint: uint16_t = cache.index
            cast(0, type=void)
            if dict.ma_keys.dk_kind != DICT_KEYS_GENERAL:
                ep: st.Pointer[PyDictUnicodeEntry] = DK_UNICODE_ENTRIES(dict.ma_keys) + hint
                cast(0, type=void)
                res = ep.me_value
            else:
                ep: st.Pointer[PyDictKeyEntry] = DK_ENTRIES(dict.ma_keys) + hint
                cast(0, type=void)
                res = ep.me_value
            cast(0, type=void)
            cast(0, type=void)
            _Py_INCREF(cast(res, type=st.Pointer[PyObject]))
            SET_TOP(cast(0, type=st.Pointer[void]))
            STACK_GROW(oparg & 1)
            SET_TOP(res)
            _Py_DECREF(cast(owner, type=st.Pointer[PyObject]))
            cast(0, type=void)
            DISPATCH()
        case 'LOAD_ATTR_SLOT':
            assert(cframe.use_tracing == 0)
            owner: st.Pointer[PyObject] = TOP()
            res: st.Pointer[PyObject]
            tp: st.Pointer[PyTypeObject] = cast(owner, type=st.Pointer[PyObject]).ob_type
            cache: st.Pointer[_PyAttrCache] = cast(next_instr, type=st.Pointer[_PyAttrCache])
            type_version: uint32_t = read_u32(cache.version)
            assert(type_version != 0)
            cast(0, type=void)
            addr: st.Pointer[char] = cast(owner, type=st.Pointer[char]) + cache.index
            res = deref(cast(addr, type=st.Pointer[st.Pointer[PyObject]]))
            cast(0, type=void)
            cast(0, type=void)
            _Py_INCREF(cast(res, type=st.Pointer[PyObject]))
            SET_TOP(cast(0, type=st.Pointer[void]))
            STACK_GROW(oparg & 1)
            SET_TOP(res)
            _Py_DECREF(cast(owner, type=st.Pointer[PyObject]))
            cast(0, type=void)
            DISPATCH()
        case 'LOAD_ATTR_CLASS':
            assert(cframe.use_tracing == 0)
            cache: st.Pointer[_PyLoadMethodCache] = cast(next_instr, type=st.Pointer[_PyLoadMethodCache])
            cls: st.Pointer[PyObject] = TOP()
            cast(0, type=void)
            type_version: uint32_t = read_u32(cache.type_version)
            cast(0, type=void)
            assert(type_version != 0)
            cast(0, type=void)
            res: st.Pointer[PyObject] = read_obj(cache.descr)
            assert(res != cast(0, type=st.Pointer[void]))
            _Py_INCREF(cast(res, type=st.Pointer[PyObject]))
            SET_TOP(cast(0, type=st.Pointer[void]))
            STACK_GROW(oparg & 1)
            SET_TOP(res)
            _Py_DECREF(cast(cls, type=st.Pointer[PyObject]))
            cast(0, type=void)
            DISPATCH()
        case 'LOAD_ATTR_PROPERTY':
            assert(cframe.use_tracing == 0)
            cast(0, type=void)
            cache: st.Pointer[_PyLoadMethodCache] = cast(next_instr, type=st.Pointer[_PyLoadMethodCache])
            owner: st.Pointer[PyObject] = TOP()
            cls: st.Pointer[PyTypeObject] = cast(owner, type=st.Pointer[PyObject]).ob_type
            type_version: uint32_t = read_u32(cache.type_version)
            cast(0, type=void)
            assert(type_version != 0)
            fget: st.Pointer[PyObject] = read_obj(cache.descr)
            assert(_Py_IS_TYPE(cast(fget, type=st.Pointer[st.Const[PyObject]]), ref(PyFunction_Type)))
            f: st.Pointer[PyFunctionObject] = cast(fget, type=st.Pointer[PyFunctionObject])
            func_version: uint32_t = read_u32(cache.keys_version)
            assert(func_version != 0)
            cast(0, type=void)
            code: st.Pointer[PyCodeObject] = cast(f.func_code, type=st.Pointer[PyCodeObject])
            assert(code.co_argcount == 1)
            cast(0, type=void)
            cast(0, type=void)
            _Py_INCREF(cast(fget, type=st.Pointer[PyObject]))
            new_frame: st.Pointer[_PyInterpreterFrame] = _PyFrame_PushUnchecked(tstate, f)
            SET_TOP(cast(0, type=st.Pointer[void]))
            shrink_stack: int = not oparg & 1
            STACK_SHRINK(shrink_stack)
            new_frame.localsplus[0] = owner
            for i in range(1, code.co_nlocalsplus, 1):
                new_frame.localsplus[i] = cast(0, type=st.Pointer[void])
            cast(0, type=void)
            DISPATCH_INLINED(new_frame)
        case 'LOAD_ATTR_GETATTRIBUTE_OVERRIDDEN':
            assert(cframe.use_tracing == 0)
            cast(0, type=void)
            cache: st.Pointer[_PyLoadMethodCache] = cast(next_instr, type=st.Pointer[_PyLoadMethodCache])
            owner: st.Pointer[PyObject] = TOP()
            cls: st.Pointer[PyTypeObject] = cast(owner, type=st.Pointer[PyObject]).ob_type
            type_version: uint32_t = read_u32(cache.type_version)
            cast(0, type=void)
            assert(type_version != 0)
            getattribute: st.Pointer[PyObject] = read_obj(cache.descr)
            assert(_Py_IS_TYPE(cast(getattribute, type=st.Pointer[st.Const[PyObject]]), ref(PyFunction_Type)))
            f: st.Pointer[PyFunctionObject] = cast(getattribute, type=st.Pointer[PyFunctionObject])
            func_version: uint32_t = read_u32(cache.keys_version)
            assert(func_version != 0)
            cast(0, type=void)
            code: st.Pointer[PyCodeObject] = cast(f.func_code, type=st.Pointer[PyCodeObject])
            assert(code.co_argcount == 2)
            cast(0, type=void)
            cast(0, type=void)
            name: st.Pointer[PyObject] = GETITEM(names, oparg >> 1)
            _Py_INCREF(cast(f, type=st.Pointer[PyObject]))
            new_frame: st.Pointer[_PyInterpreterFrame] = _PyFrame_PushUnchecked(tstate, f)
            SET_TOP(cast(0, type=st.Pointer[void]))
            shrink_stack: int = not oparg & 1
            STACK_SHRINK(shrink_stack)
            new_frame.localsplus[0] = owner
            new_frame.localsplus[1] = _Py_NewRef(cast(name, type=st.Pointer[PyObject]))
            for i in range(2, code.co_nlocalsplus, 1):
                new_frame.localsplus[i] = cast(0, type=st.Pointer[void])
            cast(0, type=void)
            DISPATCH_INLINED(new_frame)
        case 'STORE_ATTR_INSTANCE_VALUE':
            owner: st.Pointer[PyObject] = PEEK(1)
            value: st.Pointer[PyObject] = PEEK(2)
            type_version: uint32_t = read_u32(ref(next_instr[1].cache))
            index: uint16_t = read_u16(ref(next_instr[3].cache))
            assert(cframe.use_tracing == 0)
            tp: st.Pointer[PyTypeObject] = cast(owner, type=st.Pointer[PyObject]).ob_type
            assert(type_version != 0)
            cast(0, type=void)
            assert(tp.tp_flags & 1 << 4)
            dorv: PyDictOrValues = deref(_PyObject_DictOrValuesPointer(owner))
            cast(0, type=void)
            cast(0, type=void)
            values: st.Pointer[PyDictValues] = _PyDictOrValues_GetValues(dorv)
            old_value: st.Pointer[PyObject] = values.values[index]
            values.values[index] = value
            if old_value == cast(0, type=st.Pointer[void]):
                _PyDictValues_AddToInsertionOrder(values, index)
            else:
                _Py_DECREF(cast(old_value, type=st.Pointer[PyObject]))
            _Py_DECREF(cast(owner, type=st.Pointer[PyObject]))
            STACK_SHRINK(2)
            cast(0, type=void)
            DISPATCH()
        case 'STORE_ATTR_WITH_HINT':
            owner: st.Pointer[PyObject] = PEEK(1)
            value: st.Pointer[PyObject] = PEEK(2)
            type_version: uint32_t = read_u32(ref(next_instr[1].cache))
            hint: uint16_t = read_u16(ref(next_instr[3].cache))
            assert(cframe.use_tracing == 0)
            tp: st.Pointer[PyTypeObject] = cast(owner, type=st.Pointer[PyObject]).ob_type
            assert(type_version != 0)
            cast(0, type=void)
            assert(tp.tp_flags & 1 << 4)
            dorv: PyDictOrValues = deref(_PyObject_DictOrValuesPointer(owner))
            cast(0, type=void)
            dict: st.Pointer[PyDictObject] = cast(_PyDictOrValues_GetDict(dorv), type=st.Pointer[PyDictObject])
            cast(0, type=void)
            assert(_Py_IS_TYPE(cast(cast(dict, type=st.Pointer[PyObject]), type=st.Pointer[st.Const[PyObject]]), ref(PyDict_Type)))
            name: st.Pointer[PyObject] = GETITEM(names, oparg)
            cast(0, type=void)
            old_value: st.Pointer[PyObject]
            new_version: uint64_t
            if dict.ma_keys.dk_kind != DICT_KEYS_GENERAL:
                ep: st.Pointer[PyDictUnicodeEntry] = DK_UNICODE_ENTRIES(dict.ma_keys) + hint
                cast(0, type=void)
                old_value = ep.me_value
                cast(0, type=void)
                new_version = _PyDict_NotifyEvent(PyDict_EVENT_MODIFIED, dict, name, value)
                ep.me_value = value
            else:
                ep: st.Pointer[PyDictKeyEntry] = DK_ENTRIES(dict.ma_keys) + hint
                cast(0, type=void)
                old_value = ep.me_value
                cast(0, type=void)
                new_version = _PyDict_NotifyEvent(PyDict_EVENT_MODIFIED, dict, name, value)
                ep.me_value = value
            _Py_DECREF(cast(old_value, type=st.Pointer[PyObject]))
            cast(0, type=void)
            if not _PyObject_GC_IS_TRACKED(cast(dict, type=st.Pointer[PyObject])) and _PyObject_GC_MAY_BE_TRACKED(value):
                _PyObject_GC_TRACK('generated_cases.c', 2254, cast(dict, type=st.Pointer[PyObject]))
            dict.ma_version_tag = new_version
            _Py_DECREF(cast(owner, type=st.Pointer[PyObject]))
            STACK_SHRINK(2)
            cast(0, type=void)
            DISPATCH()
        case 'STORE_ATTR_SLOT':
            owner: st.Pointer[PyObject] = PEEK(1)
            value: st.Pointer[PyObject] = PEEK(2)
            type_version: uint32_t = read_u32(ref(next_instr[1].cache))
            index: uint16_t = read_u16(ref(next_instr[3].cache))
            assert(cframe.use_tracing == 0)
            tp: st.Pointer[PyTypeObject] = cast(owner, type=st.Pointer[PyObject]).ob_type
            assert(type_version != 0)
            cast(0, type=void)
            addr: st.Pointer[char] = cast(owner, type=st.Pointer[char]) + index
            cast(0, type=void)
            old_value: st.Pointer[PyObject] = deref(cast(addr, type=st.Pointer[st.Pointer[PyObject]]))
            deref(cast(addr, type=st.Pointer[st.Pointer[PyObject]])) = value
            Py_XDECREF(old_value)
            _Py_DECREF(cast(owner, type=st.Pointer[PyObject]))
            STACK_SHRINK(2)
            cast(0, type=void)
            DISPATCH()
        case 'COMPARE_OP':
            PREDICTED(107)
            right: st.Pointer[PyObject] = PEEK(1)
            left: st.Pointer[PyObject] = PEEK(2)
            res: st.Pointer[PyObject]
            cache: st.Pointer[_PyCompareOpCache] = cast(next_instr, type=st.Pointer[_PyCompareOpCache])
            if ADAPTIVE_COUNTER_IS_ZERO(cache.counter):
                assert(cframe.use_tracing == 0)
                next_instr -= 1
                _Py_Specialize_CompareOp(left, right, next_instr, oparg)
                cast(0, type=void)
            cast(0, type=void)
            DECREMENT_ADAPTIVE_COUNTER(cache.counter)
            assert(oparg <= 5)
            res = PyObject_RichCompare(left, right, oparg)
            _Py_DECREF(cast(left, type=st.Pointer[PyObject]))
            _Py_DECREF(cast(right, type=st.Pointer[PyObject]))
            if res == cast(0, type=st.Pointer[void]):
                'break # goto pop_2_error'
            STACK_SHRINK(1)
            POKE(1, res)
            cast(0, type=void)
            DISPATCH()
        case 'COMPARE_OP_FLOAT_JUMP':
            _tmp_1: st.Pointer[PyObject] = PEEK(1)
            _tmp_2: st.Pointer[PyObject] = PEEK(2)
            right: st.Pointer[PyObject] = _tmp_1
            left: st.Pointer[PyObject] = _tmp_2
            jump: size_t
            when_to_jump_mask: uint16_t = read_u16(ref(next_instr[1].cache))
            assert(cframe.use_tracing == 0)
            cast(0, type=void)
            cast(0, type=void)
            cast(0, type=void)
            dleft: double = cast(left, type=st.Pointer[PyFloatObject]).ob_fval
            dright: double = cast(right, type=st.Pointer[PyFloatObject]).ob_fval
            sign_ish: int = 1 << 2 * (dleft >= dright) + (dleft <= dright)
            _Py_DECREF_SPECIALIZED(left, _PyFloat_ExactDealloc)
            _Py_DECREF_SPECIALIZED(right, _PyFloat_ExactDealloc)
            jump = sign_ish & when_to_jump_mask
            _tmp_2 = cast(jump, type=st.Pointer[PyObject])
            cast(0, type=void)
            NEXTOPARG()
            cast(0, type=void)
            jump: size_t = cast(_tmp_2, type=size_t)
            assert(opcode == 114 or opcode == 115)
            if jump:
                cast(0, type=void)
            STACK_SHRINK(2)
            DISPATCH()
        case 'COMPARE_OP_INT_JUMP':
            _tmp_1: st.Pointer[PyObject] = PEEK(1)
            _tmp_2: st.Pointer[PyObject] = PEEK(2)
            right: st.Pointer[PyObject] = _tmp_1
            left: st.Pointer[PyObject] = _tmp_2
            jump: size_t
            when_to_jump_mask: uint16_t = read_u16(ref(next_instr[1].cache))
            assert(cframe.use_tracing == 0)
            cast(0, type=void)
            cast(0, type=void)
            cast(0, type=void)
            cast(0, type=void)
            cast(0, type=void)
            assert(Py_ABS(cast(left, type=st.Pointer[PyVarObject]).ob_size) <= 1 and Py_ABS(cast(right, type=st.Pointer[PyVarObject]).ob_size) <= 1)
            ileft: Py_ssize_t = cast(left, type=st.Pointer[PyVarObject]).ob_size * cast(left, type=st.Pointer[PyLongObject]).ob_digit[0]
            iright: Py_ssize_t = cast(right, type=st.Pointer[PyVarObject]).ob_size * cast(right, type=st.Pointer[PyLongObject]).ob_digit[0]
            sign_ish: int = 1 << 2 * (ileft >= iright) + (ileft <= iright)
            _Py_DECREF_SPECIALIZED(left, cast(PyObject_Free, type=destructor))
            _Py_DECREF_SPECIALIZED(right, cast(PyObject_Free, type=destructor))
            jump = sign_ish & when_to_jump_mask
            _tmp_2 = cast(jump, type=st.Pointer[PyObject])
            cast(0, type=void)
            NEXTOPARG()
            cast(0, type=void)
            jump: size_t = cast(_tmp_2, type=size_t)
            assert(opcode == 114 or opcode == 115)
            if jump:
                cast(0, type=void)
            STACK_SHRINK(2)
            DISPATCH()
        case 'COMPARE_OP_STR_JUMP':
            _tmp_1: st.Pointer[PyObject] = PEEK(1)
            _tmp_2: st.Pointer[PyObject] = PEEK(2)
            right: st.Pointer[PyObject] = _tmp_1
            left: st.Pointer[PyObject] = _tmp_2
            jump: size_t
            invert: uint16_t = read_u16(ref(next_instr[1].cache))
            assert(cframe.use_tracing == 0)
            cast(0, type=void)
            cast(0, type=void)
            cast(0, type=void)
            res: int = _PyUnicode_Equal(left, right)
            assert(oparg == 2 or oparg == 3)
            _Py_DECREF_SPECIALIZED(left, _PyUnicode_ExactDealloc)
            _Py_DECREF_SPECIALIZED(right, _PyUnicode_ExactDealloc)
            assert(res == 0 or res == 1)
            assert(invert == 0 or invert == 1)
            jump = res ^ invert
            _tmp_2 = cast(jump, type=st.Pointer[PyObject])
            cast(0, type=void)
            NEXTOPARG()
            cast(0, type=void)
            jump: size_t = cast(_tmp_2, type=size_t)
            assert(opcode == 114 or opcode == 115)
            if jump:
                cast(0, type=void)
            STACK_SHRINK(2)
            DISPATCH()
        case 'IS_OP':
            right: st.Pointer[PyObject] = PEEK(1)
            left: st.Pointer[PyObject] = PEEK(2)
            b: st.Pointer[PyObject]
            res: int = (left == right) ^ oparg
            _Py_DECREF(cast(left, type=st.Pointer[PyObject]))
            _Py_DECREF(cast(right, type=st.Pointer[PyObject]))
            b = _Py_NewRef(cast(res if cast(ref(_Py_TrueStruct), type=st.Pointer[PyObject]) else cast(ref(_Py_FalseStruct), type=st.Pointer[PyObject]), type=st.Pointer[PyObject]))
            STACK_SHRINK(1)
            POKE(1, b)
            DISPATCH()
        case 'CONTAINS_OP':
            right: st.Pointer[PyObject] = PEEK(1)
            left: st.Pointer[PyObject] = PEEK(2)
            b: st.Pointer[PyObject]
            res: int = PySequence_Contains(right, left)
            _Py_DECREF(cast(left, type=st.Pointer[PyObject]))
            _Py_DECREF(cast(right, type=st.Pointer[PyObject]))
            if res < 0:
                'break # goto pop_2_error'
            b = _Py_NewRef(cast(res ^ oparg if cast(ref(_Py_TrueStruct), type=st.Pointer[PyObject]) else cast(ref(_Py_FalseStruct), type=st.Pointer[PyObject]), type=st.Pointer[PyObject]))
            STACK_SHRINK(1)
            POKE(1, b)
            DISPATCH()
        case 'CHECK_EG_MATCH':
            match_type: st.Pointer[PyObject] = POP()
            if check_except_star_type_valid(tstate, match_type) < 0:
                _Py_DECREF(cast(match_type, type=st.Pointer[PyObject]))
                'break # goto error'
            exc_value: st.Pointer[PyObject] = TOP()
            match: st.Pointer[PyObject] = cast(0, type=st.Pointer[void])
            rest: st.Pointer[PyObject] = cast(0, type=st.Pointer[void])
            res: int = exception_group_match(exc_value, match_type, ref(match), ref(rest))
            _Py_DECREF(cast(match_type, type=st.Pointer[PyObject]))
            if res < 0:
                'break # goto error'
            if match == cast(0, type=st.Pointer[void]) or rest == cast(0, type=st.Pointer[void]):
                assert(match == cast(0, type=st.Pointer[void]))
                assert(rest == cast(0, type=st.Pointer[void]))
                'break # goto error'
            if match == ref(_Py_NoneStruct):
                PUSH(match)
                Py_XDECREF(rest)
            else:
                SET_TOP(rest)
                PUSH(match)
                PyErr_SetExcInfo(cast(0, type=st.Pointer[void]), _Py_NewRef(cast(match, type=st.Pointer[PyObject])), cast(0, type=st.Pointer[void]))
                _Py_DECREF(cast(exc_value, type=st.Pointer[PyObject]))
            DISPATCH()
        case 'CHECK_EXC_MATCH':
            right: st.Pointer[PyObject] = PEEK(1)
            left: st.Pointer[PyObject] = PEEK(2)
            b: st.Pointer[PyObject]
            assert(PyExceptionInstance_Check(left))
            if check_except_type_valid(tstate, right) < 0:
                _Py_DECREF(cast(right, type=st.Pointer[PyObject]))
                if 1:
                    'break # goto pop_1_error'
            res: int = PyErr_GivenExceptionMatches(left, right)
            _Py_DECREF(cast(right, type=st.Pointer[PyObject]))
            b = _Py_NewRef(cast(res if cast(ref(_Py_TrueStruct), type=st.Pointer[PyObject]) else cast(ref(_Py_FalseStruct), type=st.Pointer[PyObject]), type=st.Pointer[PyObject]))
            POKE(1, b)
            DISPATCH()
        case 'IMPORT_NAME':
            fromlist: st.Pointer[PyObject] = PEEK(1)
            level: st.Pointer[PyObject] = PEEK(2)
            res: st.Pointer[PyObject]
            name: st.Pointer[PyObject] = GETITEM(names, oparg)
            res = import_name(tstate, frame, name, fromlist, level)
            _Py_DECREF(cast(level, type=st.Pointer[PyObject]))
            _Py_DECREF(cast(fromlist, type=st.Pointer[PyObject]))
            if res == cast(0, type=st.Pointer[void]):
                'break # goto pop_2_error'
            STACK_SHRINK(1)
            POKE(1, res)
            DISPATCH()
        case 'IMPORT_STAR':
            from: st.Pointer[PyObject] = PEEK(1)
            locals: st.Pointer[PyObject]
            err: int
            if _PyFrame_FastToLocalsWithError(frame) < 0:
                _Py_DECREF(cast(from, type=st.Pointer[PyObject]))
                if 1:
                    'break # goto pop_1_error'
            locals = LOCALS()
            if locals == cast(0, type=st.Pointer[void]):
                _PyErr_SetString(tstate, PyExc_SystemError, "no locals found during 'import *'")
                _Py_DECREF(cast(from, type=st.Pointer[PyObject]))
                if 1:
                    'break # goto pop_1_error'
            err = import_all_from(tstate, locals, from)
            _PyFrame_LocalsToFast(frame, 0)
            _Py_DECREF(cast(from, type=st.Pointer[PyObject]))
            if err:
                'break # goto pop_1_error'
            STACK_SHRINK(1)
            DISPATCH()
        case 'IMPORT_FROM':
            from: st.Pointer[PyObject] = PEEK(1)
            res: st.Pointer[PyObject]
            name: st.Pointer[PyObject] = GETITEM(names, oparg)
            res = import_from(tstate, from, name)
            if res == cast(0, type=st.Pointer[void]):
                'break # goto error'
            STACK_GROW(1)
            POKE(1, res)
            DISPATCH()
        case 'JUMP_FORWARD':
            cast(0, type=void)
            DISPATCH()
        case 'JUMP_BACKWARD':
            PREDICTED(JUMP_BACKWARD)
            assert(oparg < INSTR_OFFSET())
            cast(0, type=void)
            CHECK_EVAL_BREAKER()
            DISPATCH()
        case 'POP_JUMP_IF_FALSE':
            PREDICTED(114)
            cond: st.Pointer[PyObject] = POP()
            if cond == cast(ref(_Py_TrueStruct), type=st.Pointer[PyObject]):
                _Py_DECREF_NO_DEALLOC(cond)
            elif cond == cast(ref(_Py_FalseStruct), type=st.Pointer[PyObject]):
                _Py_DECREF_NO_DEALLOC(cond)
                cast(0, type=void)
            else:
                err: int = PyObject_IsTrue(cond)
                _Py_DECREF(cast(cond, type=st.Pointer[PyObject]))
                if err > 0:
                    pass
                elif err == 0:
                    cast(0, type=void)
                else:
                    'break # goto error'
            DISPATCH()
        case 'POP_JUMP_IF_TRUE':
            cond: st.Pointer[PyObject] = POP()
            if cond == cast(ref(_Py_FalseStruct), type=st.Pointer[PyObject]):
                _Py_DECREF_NO_DEALLOC(cond)
            elif cond == cast(ref(_Py_TrueStruct), type=st.Pointer[PyObject]):
                _Py_DECREF_NO_DEALLOC(cond)
                cast(0, type=void)
            else:
                err: int = PyObject_IsTrue(cond)
                _Py_DECREF(cast(cond, type=st.Pointer[PyObject]))
                if err > 0:
                    cast(0, type=void)
                elif err == 0:
                    pass
                else:
                    'break # goto error'
            DISPATCH()
        case 'POP_JUMP_IF_NOT_NONE':
            value: st.Pointer[PyObject] = POP()
            if not value == ref(_Py_NoneStruct):
                cast(0, type=void)
            _Py_DECREF(cast(value, type=st.Pointer[PyObject]))
            DISPATCH()
        case 'POP_JUMP_IF_NONE':
            value: st.Pointer[PyObject] = POP()
            if value == ref(_Py_NoneStruct):
                _Py_DECREF_NO_DEALLOC(value)
                cast(0, type=void)
            else:
                _Py_DECREF(cast(value, type=st.Pointer[PyObject]))
            DISPATCH()
        case 'JUMP_IF_FALSE_OR_POP':
            cond: st.Pointer[PyObject] = TOP()
            err: int
            if cond == cast(ref(_Py_TrueStruct), type=st.Pointer[PyObject]):
                STACK_SHRINK(1)
                _Py_DECREF_NO_DEALLOC(cond)
            elif cond == cast(ref(_Py_FalseStruct), type=st.Pointer[PyObject]):
                cast(0, type=void)
            else:
                err = PyObject_IsTrue(cond)
                if err > 0:
                    STACK_SHRINK(1)
                    _Py_DECREF(cast(cond, type=st.Pointer[PyObject]))
                elif err == 0:
                    cast(0, type=void)
                else:
                    'break # goto error'
            DISPATCH()
        case 'JUMP_IF_TRUE_OR_POP':
            cond: st.Pointer[PyObject] = TOP()
            err: int
            if cond == cast(ref(_Py_FalseStruct), type=st.Pointer[PyObject]):
                STACK_SHRINK(1)
                _Py_DECREF_NO_DEALLOC(cond)
            elif cond == cast(ref(_Py_TrueStruct), type=st.Pointer[PyObject]):
                cast(0, type=void)
            else:
                err = PyObject_IsTrue(cond)
                if err > 0:
                    cast(0, type=void)
                elif err == 0:
                    STACK_SHRINK(1)
                    _Py_DECREF(cast(cond, type=st.Pointer[PyObject]))
                else:
                    'break # goto error'
            DISPATCH()
        case 'JUMP_BACKWARD_NO_INTERRUPT':
            cast(0, type=void)
            DISPATCH()
        case 'GET_LEN':
            len_i: Py_ssize_t = PyObject_Size(TOP())
            if len_i < 0:
                'break # goto error'
            len_o: st.Pointer[PyObject] = PyLong_FromSsize_t(len_i)
            if len_o == cast(0, type=st.Pointer[void]):
                'break # goto error'
            PUSH(len_o)
            DISPATCH()
        case 'MATCH_CLASS':
            names: st.Pointer[PyObject] = POP()
            type: st.Pointer[PyObject] = POP()
            subject: st.Pointer[PyObject] = TOP()
            assert(_Py_IS_TYPE(cast(names, type=st.Pointer[st.Const[PyObject]]), ref(PyTuple_Type)))
            attrs: st.Pointer[PyObject] = match_class(tstate, subject, type, oparg, names)
            _Py_DECREF(cast(names, type=st.Pointer[PyObject]))
            _Py_DECREF(cast(type, type=st.Pointer[PyObject]))
            if attrs:
                assert(_Py_IS_TYPE(cast(attrs, type=st.Pointer[st.Const[PyObject]]), ref(PyTuple_Type)))
                SET_TOP(attrs)
            elif _PyErr_Occurred(tstate):
                'break # goto error'
            else:
                SET_TOP(_Py_NewRef(cast(ref(_Py_NoneStruct), type=st.Pointer[PyObject])))
            _Py_DECREF(cast(subject, type=st.Pointer[PyObject]))
            DISPATCH()
        case 'MATCH_MAPPING':
            subject: st.Pointer[PyObject] = TOP()
            match: int = cast(subject, type=st.Pointer[PyObject]).ob_type.tp_flags & 1 << 6
            res: st.Pointer[PyObject] = match if cast(ref(_Py_TrueStruct), type=st.Pointer[PyObject]) else cast(ref(_Py_FalseStruct), type=st.Pointer[PyObject])
            PUSH(_Py_NewRef(cast(res, type=st.Pointer[PyObject])))
            PREDICT(114)
            DISPATCH()
        case 'MATCH_SEQUENCE':
            subject: st.Pointer[PyObject] = TOP()
            match: int = cast(subject, type=st.Pointer[PyObject]).ob_type.tp_flags & 1 << 5
            res: st.Pointer[PyObject] = match if cast(ref(_Py_TrueStruct), type=st.Pointer[PyObject]) else cast(ref(_Py_FalseStruct), type=st.Pointer[PyObject])
            PUSH(_Py_NewRef(cast(res, type=st.Pointer[PyObject])))
            PREDICT(114)
            DISPATCH()
        case 'MATCH_KEYS':
            keys: st.Pointer[PyObject] = TOP()
            subject: st.Pointer[PyObject] = SECOND()
            values_or_none: st.Pointer[PyObject] = match_keys(tstate, subject, keys)
            if values_or_none == cast(0, type=st.Pointer[void]):
                'break # goto error'
            PUSH(values_or_none)
            DISPATCH()
        case 'GET_ITER':
            iterable: st.Pointer[PyObject] = TOP()
            iter: st.Pointer[PyObject] = PyObject_GetIter(iterable)
            _Py_DECREF(cast(iterable, type=st.Pointer[PyObject]))
            SET_TOP(iter)
            if iter == cast(0, type=st.Pointer[void]):
                'break # goto error'
            DISPATCH()
        case 'GET_YIELD_FROM_ITER':
            iterable: st.Pointer[PyObject] = TOP()
            iter: st.Pointer[PyObject]
            if _Py_IS_TYPE(cast(iterable, type=st.Pointer[st.Const[PyObject]]), ref(PyCoro_Type)):
                if not frame.f_code.co_flags & (128 | 256):
                    _Py_DECREF(cast(iterable, type=st.Pointer[PyObject]))
                    SET_TOP(cast(0, type=st.Pointer[void]))
                    _PyErr_SetString(tstate, PyExc_TypeError, "cannot 'yield from' a coroutine object in a non-coroutine generator")
                    'break # goto error'
            elif not _Py_IS_TYPE(cast(iterable, type=st.Pointer[st.Const[PyObject]]), ref(PyGen_Type)):
                iter = PyObject_GetIter(iterable)
                _Py_DECREF(cast(iterable, type=st.Pointer[PyObject]))
                SET_TOP(iter)
                if iter == cast(0, type=st.Pointer[void]):
                    'break # goto error'
            PREDICT(100)
            DISPATCH()
        case 'FOR_ITER':
            PREDICTED(93)
            cache: st.Pointer[_PyForIterCache] = cast(next_instr, type=st.Pointer[_PyForIterCache])
            if ADAPTIVE_COUNTER_IS_ZERO(cache.counter):
                assert(cframe.use_tracing == 0)
                next_instr -= 1
                _Py_Specialize_ForIter(TOP(), next_instr, oparg)
                cast(0, type=void)
            cast(0, type=void)
            DECREMENT_ADAPTIVE_COUNTER(cache.counter)
            iter: st.Pointer[PyObject] = TOP()
            next: st.Pointer[PyObject] = deref(cast(iter, type=st.Pointer[PyObject]).ob_type.tp_iternext)(iter)
            if next != cast(0, type=st.Pointer[void]):
                PUSH(next)
                cast(0, type=void)
            else:
                if _PyErr_Occurred(tstate):
                    if not _PyErr_ExceptionMatches(tstate, PyExc_StopIteration):
                        'break # goto error'
                    elif tstate.c_tracefunc != cast(0, type=st.Pointer[void]):
                        call_exc_trace(tstate.c_tracefunc, tstate.c_traceobj, tstate, frame)
                    _PyErr_Clear(tstate)
                assert(next_instr[sizeof(_PyForIterCache) / sizeof(_Py_CODEUNIT) + oparg] & 255 == END_FOR)
                STACK_SHRINK(1)
                _Py_DECREF(cast(iter, type=st.Pointer[PyObject]))
                cast(0, type=void)
            DISPATCH()
        case 'FOR_ITER_LIST':
            assert(cframe.use_tracing == 0)
            it: st.Pointer[_PyListIterObject] = cast(TOP(), type=st.Pointer[_PyListIterObject])
            cast(0, type=void)
            cast(0, type=void)
            seq: st.Pointer[PyListObject] = it.it_seq
            if seq:
                if it.it_index < cast(assert(PyType_HasFeature(cast(seq, type=st.Pointer[PyObject]).ob_type, 1 << 25))cast(seq, type=st.Pointer[PyListObject]), type=st.Pointer[PyVarObject]).ob_size:
                    next: st.Pointer[PyObject] = assert(PyType_HasFeature(cast(seq, type=st.Pointer[PyObject]).ob_type, 1 << 25)).ob_item[
                    it.it_index += 1]
                    PUSH(_Py_NewRef(cast(next, type=st.Pointer[PyObject])))
                    cast(0, type=void)
                    'break # goto end_for_iter_list'
                it.it_seq = cast(0, type=st.Pointer[void])
                _Py_DECREF(cast(seq, type=st.Pointer[PyObject]))
            STACK_SHRINK(1)
            _Py_DECREF(cast(it, type=st.Pointer[PyObject]))
            cast(0, type=void)
            '# label: n.name'
        case 'FOR_ITER_TUPLE':
            assert(cframe.use_tracing == 0)
            it: st.Pointer[_PyTupleIterObject] = cast(TOP(), type=st.Pointer[_PyTupleIterObject])
            cast(0, type=void)
            cast(0, type=void)
            seq: st.Pointer[PyTupleObject] = it.it_seq
            if seq:
                if it.it_index < cast(assert(PyType_HasFeature(cast(seq, type=st.Pointer[PyObject]).ob_type, 1 << 26))cast(seq, type=st.Pointer[PyTupleObject]), type=st.Pointer[PyVarObject]).ob_size:
                    next: st.Pointer[PyObject] = assert(PyType_HasFeature(cast(seq, type=st.Pointer[PyObject]).ob_type, 1 << 26)).ob_item[
                    it.it_index += 1]
                    PUSH(_Py_NewRef(cast(next, type=st.Pointer[PyObject])))
                    cast(0, type=void)
                    'break # goto end_for_iter_tuple'
                it.it_seq = cast(0, type=st.Pointer[void])
                _Py_DECREF(cast(seq, type=st.Pointer[PyObject]))
            STACK_SHRINK(1)
            _Py_DECREF(cast(it, type=st.Pointer[PyObject]))
            cast(0, type=void)
            '# label: n.name'
        case 'FOR_ITER_RANGE':
            assert(cframe.use_tracing == 0)
            r: st.Pointer[_PyRangeIterObject] = cast(TOP(), type=st.Pointer[_PyRangeIterObject])
            cast(0, type=void)
            cast(0, type=void)
            next: _Py_CODEUNIT = next_instr[sizeof(_PyForIterCache) / sizeof(_Py_CODEUNIT)]
            assert(_PyOpcode_Deopt[next & 255] == 125)
            if r.len <= 0:
                STACK_SHRINK(1)
                _Py_DECREF(cast(r, type=st.Pointer[PyObject]))
                cast(0, type=void)
            else:
                value: long = r.start
                r.start = value + r.step
                r.len -= 1
                if _PyLong_AssignValue(ref(frame.localsplus[next >> 8]), value) < 0:
                    'break # goto error'
                cast(0, type=void)
            DISPATCH()
        case 'FOR_ITER_GEN':
            assert(cframe.use_tracing == 0)
            gen: st.Pointer[PyGenObject] = cast(TOP(), type=st.Pointer[PyGenObject])
            cast(0, type=void)
            cast(0, type=void)
            cast(0, type=void)
            gen_frame: st.Pointer[_PyInterpreterFrame] = cast(gen.gi_iframe, type=st.Pointer[_PyInterpreterFrame])
            frame.yield_offset = oparg
            _PyFrame_StackPush(gen_frame, _Py_NewRef(cast(ref(_Py_NoneStruct), type=st.Pointer[PyObject])))
            gen.gi_frame_state = FRAME_EXECUTING
            gen.gi_exc_state.previous_item = tstate.exc_info
            tstate.exc_info = ref(gen.gi_exc_state)
            cast(0, type=void)
            assert(deref(next_instr) & 255 == END_FOR)
            DISPATCH_INLINED(gen_frame)
        case 'BEFORE_ASYNC_WITH':
            mgr: st.Pointer[PyObject] = TOP()
            res: st.Pointer[PyObject]
            enter: st.Pointer[PyObject] = _PyObject_LookupSpecial(mgr, ref(_PyRuntime.static_objects.singletons.strings.identifiers._py___aenter__._ascii.ob_base))
            if enter == cast(0, type=st.Pointer[void]):
                if not _PyErr_Occurred(tstate):
                    _PyErr_Format(tstate, PyExc_TypeError, "'%.200s' object does not support the asynchronous context manager protocol", cast(mgr, type=st.Pointer[PyObject]).ob_type.tp_name)
                'break # goto error'
            exit: st.Pointer[PyObject] = _PyObject_LookupSpecial(mgr, ref(_PyRuntime.static_objects.singletons.strings.identifiers._py___aexit__._ascii.ob_base))
            if exit == cast(0, type=st.Pointer[void]):
                if not _PyErr_Occurred(tstate):
                    _PyErr_Format(tstate, PyExc_TypeError, "'%.200s' object does not support the asynchronous context manager protocol (missed __aexit__ method)", cast(mgr, type=st.Pointer[PyObject]).ob_type.tp_name)
                _Py_DECREF(cast(enter, type=st.Pointer[PyObject]))
                'break # goto error'
            SET_TOP(exit)
            _Py_DECREF(cast(mgr, type=st.Pointer[PyObject]))
            res = _PyObject_CallNoArgs(enter)
            _Py_DECREF(cast(enter, type=st.Pointer[PyObject]))
            if res == cast(0, type=st.Pointer[void]):
                'break # goto error'
            PUSH(res)
            PREDICT(73)
            DISPATCH()
        case 'BEFORE_WITH':
            mgr: st.Pointer[PyObject] = TOP()
            res: st.Pointer[PyObject]
            enter: st.Pointer[PyObject] = _PyObject_LookupSpecial(mgr, ref(_PyRuntime.static_objects.singletons.strings.identifiers._py___enter__._ascii.ob_base))
            if enter == cast(0, type=st.Pointer[void]):
                if not _PyErr_Occurred(tstate):
                    _PyErr_Format(tstate, PyExc_TypeError, "'%.200s' object does not support the context manager protocol", cast(mgr, type=st.Pointer[PyObject]).ob_type.tp_name)
                'break # goto error'
            exit: st.Pointer[PyObject] = _PyObject_LookupSpecial(mgr, ref(_PyRuntime.static_objects.singletons.strings.identifiers._py___exit__._ascii.ob_base))
            if exit == cast(0, type=st.Pointer[void]):
                if not _PyErr_Occurred(tstate):
                    _PyErr_Format(tstate, PyExc_TypeError, "'%.200s' object does not support the context manager protocol (missed __exit__ method)", cast(mgr, type=st.Pointer[PyObject]).ob_type.tp_name)
                _Py_DECREF(cast(enter, type=st.Pointer[PyObject]))
                'break # goto error'
            SET_TOP(exit)
            _Py_DECREF(cast(mgr, type=st.Pointer[PyObject]))
            res = _PyObject_CallNoArgs(enter)
            _Py_DECREF(cast(enter, type=st.Pointer[PyObject]))
            if res == cast(0, type=st.Pointer[void]):
                'break # goto error'
            PUSH(res)
            DISPATCH()
        case 'WITH_EXCEPT_START':
            val: st.Pointer[PyObject] = PEEK(1)
            lasti: st.Pointer[PyObject] = PEEK(3)
            exit_func: st.Pointer[PyObject] = PEEK(4)
            res: st.Pointer[PyObject]
            exc: st.Pointer[PyObject]
            tb: st.Pointer[PyObject]
            assert(val and PyExceptionInstance_Check(val))
            exc = _PyType_Check(cast(val, type=st.Pointer[PyObject])) and PyType_HasFeature(cast(val, type=st.Pointer[PyTypeObject]), 1 << 30)
            tb = PyException_GetTraceback(val)
            Py_XDECREF(tb)
            assert(PyLong_Check(lasti))
            cast(lasti, type=void)
            stack: st.ndarray[..., st.Pointer[PyObject]] = []
            res = PyObject_Vectorcall(exit_func, stack + 1, 3 | 1, cast(0, type=st.Pointer[void]))
            if res == cast(0, type=st.Pointer[void]):
                'break # goto error'
            STACK_GROW(1)
            POKE(1, res)
            DISPATCH()
        case 'PUSH_EXC_INFO':
            value: st.Pointer[PyObject] = TOP()
            exc_info: st.Pointer[_PyErr_StackItem] = tstate.exc_info
            if exc_info.exc_value != cast(0, type=st.Pointer[void]):
                SET_TOP(exc_info.exc_value)
            else:
                SET_TOP(_Py_NewRef(cast(ref(_Py_NoneStruct), type=st.Pointer[PyObject])))
            PUSH(_Py_NewRef(cast(value, type=st.Pointer[PyObject])))
            assert(PyExceptionInstance_Check(value))
            exc_info.exc_value = value
            DISPATCH()
        case 'LOAD_ATTR_METHOD_WITH_VALUES':
            assert(cframe.use_tracing == 0)
            self: st.Pointer[PyObject] = TOP()
            self_cls: st.Pointer[PyTypeObject] = cast(self, type=st.Pointer[PyObject]).ob_type
            cache: st.Pointer[_PyLoadMethodCache] = cast(next_instr, type=st.Pointer[_PyLoadMethodCache])
            type_version: uint32_t = read_u32(cache.type_version)
            assert(type_version != 0)
            cast(0, type=void)
            assert(self_cls.tp_flags & 1 << 4)
            dorv: PyDictOrValues = deref(_PyObject_DictOrValuesPointer(self))
            cast(0, type=void)
            self_heap_type: st.Pointer[PyHeapTypeObject] = cast(self_cls, type=st.Pointer[PyHeapTypeObject])
            cast(0, type=void)
            cast(0, type=void)
            res: st.Pointer[PyObject] = read_obj(cache.descr)
            assert(res != cast(0, type=st.Pointer[void]))
            assert(_PyType_HasFeature(cast(res, type=st.Pointer[PyObject]).ob_type, 1 << 17))
            SET_TOP(_Py_NewRef(cast(res, type=st.Pointer[PyObject])))
            PUSH(self)
            cast(0, type=void)
            DISPATCH()
        case 'LOAD_ATTR_METHOD_WITH_DICT':
            assert(cframe.use_tracing == 0)
            self: st.Pointer[PyObject] = TOP()
            self_cls: st.Pointer[PyTypeObject] = cast(self, type=st.Pointer[PyObject]).ob_type
            cache: st.Pointer[_PyLoadMethodCache] = cast(next_instr, type=st.Pointer[_PyLoadMethodCache])
            cast(0, type=void)
            dictoffset: Py_ssize_t = self_cls.tp_dictoffset
            assert(dictoffset > 0)
            dictptr: st.Pointer[st.Pointer[PyDictObject]] = cast(cast(self, type=st.Pointer[char]) + dictoffset, type=st.Pointer[st.Pointer[PyDictObject]])
            dict: st.Pointer[PyDictObject] = deref(dictptr)
            cast(0, type=void)
            cast(0, type=void)
            cast(0, type=void)
            res: st.Pointer[PyObject] = read_obj(cache.descr)
            assert(res != cast(0, type=st.Pointer[void]))
            assert(_PyType_HasFeature(cast(res, type=st.Pointer[PyObject]).ob_type, 1 << 17))
            SET_TOP(_Py_NewRef(cast(res, type=st.Pointer[PyObject])))
            PUSH(self)
            cast(0, type=void)
            DISPATCH()
        case 'LOAD_ATTR_METHOD_NO_DICT':
            assert(cframe.use_tracing == 0)
            self: st.Pointer[PyObject] = TOP()
            self_cls: st.Pointer[PyTypeObject] = cast(self, type=st.Pointer[PyObject]).ob_type
            cache: st.Pointer[_PyLoadMethodCache] = cast(next_instr, type=st.Pointer[_PyLoadMethodCache])
            type_version: uint32_t = read_u32(cache.type_version)
            cast(0, type=void)
            assert(self_cls.tp_dictoffset == 0)
            cast(0, type=void)
            res: st.Pointer[PyObject] = read_obj(cache.descr)
            assert(res != cast(0, type=st.Pointer[void]))
            assert(_PyType_HasFeature(cast(res, type=st.Pointer[PyObject]).ob_type, 1 << 17))
            SET_TOP(_Py_NewRef(cast(res, type=st.Pointer[PyObject])))
            PUSH(self)
            cast(0, type=void)
            DISPATCH()
        case 'LOAD_ATTR_METHOD_LAZY_DICT':
            assert(cframe.use_tracing == 0)
            self: st.Pointer[PyObject] = TOP()
            self_cls: st.Pointer[PyTypeObject] = cast(self, type=st.Pointer[PyObject]).ob_type
            cache: st.Pointer[_PyLoadMethodCache] = cast(next_instr, type=st.Pointer[_PyLoadMethodCache])
            type_version: uint32_t = read_u32(cache.type_version)
            cast(0, type=void)
            dictoffset: Py_ssize_t = self_cls.tp_dictoffset
            assert(dictoffset > 0)
            dict: st.Pointer[PyObject] = deref(cast(cast(self, type=st.Pointer[char]) + dictoffset, type=st.Pointer[st.Pointer[PyObject]]))
            cast(0, type=void)
            cast(0, type=void)
            res: st.Pointer[PyObject] = read_obj(cache.descr)
            assert(res != cast(0, type=st.Pointer[void]))
            assert(_PyType_HasFeature(cast(res, type=st.Pointer[PyObject]).ob_type, 1 << 17))
            SET_TOP(_Py_NewRef(cast(res, type=st.Pointer[PyObject])))
            PUSH(self)
            cast(0, type=void)
            DISPATCH()
        case 'CALL_BOUND_METHOD_EXACT_ARGS':
            cast(0, type=void)
            function: st.Pointer[PyObject] = PEEK(oparg + 1)
            cast(0, type=void)
            cast(0, type=void)
            self: st.Pointer[PyObject] = cast(function, type=st.Pointer[PyMethodObject]).im_self
            PEEK(oparg + 1) = _Py_NewRef(cast(self, type=st.Pointer[PyObject]))
            meth: st.Pointer[PyObject] = cast(function, type=st.Pointer[PyMethodObject]).im_func
            PEEK(oparg + 2) = _Py_NewRef(cast(meth, type=st.Pointer[PyObject]))
            _Py_DECREF(cast(function, type=st.Pointer[PyObject]))
            cast(0, type=void)
        case 'KW_NAMES':
            assert(kwnames == cast(0, type=st.Pointer[void]))
            assert(oparg < cast(assert(PyType_HasFeature(cast(consts, type=st.Pointer[PyObject]).ob_type, 1 << 26))cast(consts, type=st.Pointer[PyTupleObject]), type=st.Pointer[PyVarObject]).ob_size)
            kwnames = GETITEM(consts, oparg)
            DISPATCH()
        case 'CALL':
            PREDICTED(CALL)
            cache: st.Pointer[_PyCallCache] = cast(next_instr, type=st.Pointer[_PyCallCache])
            if ADAPTIVE_COUNTER_IS_ZERO(cache.counter):
                assert(cframe.use_tracing == 0)
                is_meth: int = PEEK(oparg + 2) != cast(0, type=st.Pointer[void])
                nargs: int = oparg + is_meth
                callable: st.Pointer[PyObject] = PEEK(nargs + 1)
                next_instr -= 1
                _Py_Specialize_Call(callable, next_instr, nargs, kwnames)
                cast(0, type=void)
            cast(0, type=void)
            DECREMENT_ADAPTIVE_COUNTER(cache.counter)
            total_args: int
            is_meth: int
            is_meth = PEEK(oparg + 2) != cast(0, type=st.Pointer[void])
            function: st.Pointer[PyObject] = PEEK(oparg + 1)
            if not is_meth and cast(function, type=st.Pointer[PyObject]).ob_type == ref(PyMethod_Type):
                self: st.Pointer[PyObject] = cast(function, type=st.Pointer[PyMethodObject]).im_self
                PEEK(oparg + 1) = _Py_NewRef(cast(self, type=st.Pointer[PyObject]))
                meth: st.Pointer[PyObject] = cast(function, type=st.Pointer[PyMethodObject]).im_func
                PEEK(oparg + 2) = _Py_NewRef(cast(meth, type=st.Pointer[PyObject]))
                _Py_DECREF(cast(function, type=st.Pointer[PyObject]))
                is_meth = 1
            total_args = oparg + is_meth
            function = PEEK(total_args + 1)
            positional_args: int = total_args - KWNAMES_LEN()
            if (cast(function, type=st.Pointer[PyObject]).ob_type == ref(PyFunction_Type) and tstate.interp.eval_frame == cast(0, type=st.Pointer[void])) and cast(function, type=st.Pointer[PyFunctionObject]).vectorcall == _PyFunction_Vectorcall:
                code_flags: int = cast(cast(function, type=st.Pointer[PyFunctionObject]).func_code, type=st.Pointer[PyCodeObject]).co_flags
                locals: st.Pointer[PyObject] = code_flags & 1 if cast(0, type=st.Pointer[void]) else _Py_NewRef(cast(cast(function, type=st.Pointer[PyFunctionObject]).func_globals, type=st.Pointer[PyObject]))
                STACK_SHRINK(total_args)
                new_frame: st.Pointer[_PyInterpreterFrame] = _PyEvalFramePushAndInit(tstate, cast(function, type=st.Pointer[PyFunctionObject]), locals, stack_pointer, positional_args, kwnames)
                kwnames = cast(0, type=st.Pointer[void])
                STACK_SHRINK(2 - is_meth)
                if new_frame == cast(0, type=st.Pointer[void]):
                    'break # goto error'
                cast(0, type=void)
                DISPATCH_INLINED(new_frame)
            res: st.Pointer[PyObject]
            if cframe.use_tracing:
                res = trace_call_function(tstate, function, stack_pointer - total_args, positional_args, kwnames)
            else:
                res = PyObject_Vectorcall(function, stack_pointer - total_args, positional_args | 1, kwnames)
            kwnames = cast(0, type=st.Pointer[void])
            assert((res != cast(0, type=st.Pointer[void])) ^ (_PyErr_Occurred(tstate) != cast(0, type=st.Pointer[void])))
            _Py_DECREF(cast(function, type=st.Pointer[PyObject]))
            STACK_SHRINK(total_args)
            for i in range(0, total_args, 1):
                _Py_DECREF(cast(stack_pointer[i], type=st.Pointer[PyObject]))
            STACK_SHRINK(2 - is_meth)
            PUSH(res)
            if res == cast(0, type=st.Pointer[void]):
                'break # goto error'
            cast(0, type=void)
            CHECK_EVAL_BREAKER()
            DISPATCH()
        case 'CALL_PY_EXACT_ARGS':
            PREDICTED(CALL_PY_EXACT_ARGS)
            assert(kwnames == cast(0, type=st.Pointer[void]))
            cast(0, type=void)
            cache: st.Pointer[_PyCallCache] = cast(next_instr, type=st.Pointer[_PyCallCache])
            is_meth: int = PEEK(oparg + 2) != cast(0, type=st.Pointer[void])
            argcount: int = oparg + is_meth
            callable: st.Pointer[PyObject] = PEEK(argcount + 1)
            cast(0, type=void)
            func: st.Pointer[PyFunctionObject] = cast(callable, type=st.Pointer[PyFunctionObject])
            cast(0, type=void)
            code: st.Pointer[PyCodeObject] = cast(func.func_code, type=st.Pointer[PyCodeObject])
            cast(0, type=void)
            cast(0, type=void)
            cast(0, type=void)
            new_frame: st.Pointer[_PyInterpreterFrame] = _PyFrame_PushUnchecked(tstate, func)
            STACK_SHRINK(argcount)
            for i in range(0, argcount, 1):
                new_frame.localsplus[i] = stack_pointer[i]
            for i in range(argcount, code.co_nlocalsplus, 1):
                new_frame.localsplus[i] = cast(0, type=st.Pointer[void])
            STACK_SHRINK(2 - is_meth)
            cast(0, type=void)
            DISPATCH_INLINED(new_frame)
        case 'CALL_PY_WITH_DEFAULTS':
            assert(kwnames == cast(0, type=st.Pointer[void]))
            cast(0, type=void)
            cache: st.Pointer[_PyCallCache] = cast(next_instr, type=st.Pointer[_PyCallCache])
            is_meth: int = PEEK(oparg + 2) != cast(0, type=st.Pointer[void])
            argcount: int = oparg + is_meth
            callable: st.Pointer[PyObject] = PEEK(argcount + 1)
            cast(0, type=void)
            func: st.Pointer[PyFunctionObject] = cast(callable, type=st.Pointer[PyFunctionObject])
            cast(0, type=void)
            code: st.Pointer[PyCodeObject] = cast(func.func_code, type=st.Pointer[PyCodeObject])
            cast(0, type=void)
            minargs: int = cache.min_args
            cast(0, type=void)
            cast(0, type=void)
            cast(0, type=void)
            new_frame: st.Pointer[_PyInterpreterFrame] = _PyFrame_PushUnchecked(tstate, func)
            STACK_SHRINK(argcount)
            for i in range(0, argcount, 1):
                new_frame.localsplus[i] = stack_pointer[i]
            for i in range(argcount, code.co_argcount, 1):
                def: st.Pointer[PyObject] = assert(PyType_HasFeature(cast(func.func_defaults, type=st.Pointer[PyObject]).ob_type, 1 << 26)).ob_item[i - minargs]
                new_frame.localsplus[i] = _Py_NewRef(cast(def, type=st.Pointer[PyObject]))
            for i in range(code.co_argcount, code.co_nlocalsplus, 1):
                new_frame.localsplus[i] = cast(0, type=st.Pointer[void])
            STACK_SHRINK(2 - is_meth)
            cast(0, type=void)
            DISPATCH_INLINED(new_frame)
        case 'CALL_NO_KW_TYPE_1':
            assert(kwnames == cast(0, type=st.Pointer[void]))
            assert(cframe.use_tracing == 0)
            assert(oparg == 1)
            cast(0, type=void)
            obj: st.Pointer[PyObject] = TOP()
            callable: st.Pointer[PyObject] = SECOND()
            cast(0, type=void)
            cast(0, type=void)
            cast(0, type=void)
            res: st.Pointer[PyObject] = _Py_NewRef(cast(cast(obj, type=st.Pointer[PyObject]).ob_type, type=st.Pointer[PyObject]))
            _Py_DECREF(cast(callable, type=st.Pointer[PyObject]))
            _Py_DECREF(cast(obj, type=st.Pointer[PyObject]))
            STACK_SHRINK(2)
            SET_TOP(res)
            DISPATCH()
        case 'CALL_NO_KW_STR_1':
            assert(kwnames == cast(0, type=st.Pointer[void]))
            assert(cframe.use_tracing == 0)
            assert(oparg == 1)
            cast(0, type=void)
            callable: st.Pointer[PyObject] = PEEK(2)
            cast(0, type=void)
            cast(0, type=void)
            arg: st.Pointer[PyObject] = TOP()
            res: st.Pointer[PyObject] = PyObject_Str(arg)
            _Py_DECREF(cast(arg, type=st.Pointer[PyObject]))
            _Py_DECREF(cast(ref(PyUnicode_Type), type=st.Pointer[PyObject]))
            STACK_SHRINK(2)
            SET_TOP(res)
            if res == cast(0, type=st.Pointer[void]):
                'break # goto error'
            cast(0, type=void)
            CHECK_EVAL_BREAKER()
            DISPATCH()
        case 'CALL_NO_KW_TUPLE_1':
            assert(kwnames == cast(0, type=st.Pointer[void]))
            assert(oparg == 1)
            cast(0, type=void)
            callable: st.Pointer[PyObject] = PEEK(2)
            cast(0, type=void)
            cast(0, type=void)
            arg: st.Pointer[PyObject] = TOP()
            res: st.Pointer[PyObject] = PySequence_Tuple(arg)
            _Py_DECREF(cast(arg, type=st.Pointer[PyObject]))
            _Py_DECREF(cast(ref(PyTuple_Type), type=st.Pointer[PyObject]))
            STACK_SHRINK(2)
            SET_TOP(res)
            if res == cast(0, type=st.Pointer[void]):
                'break # goto error'
            cast(0, type=void)
            CHECK_EVAL_BREAKER()
            DISPATCH()
        case 'CALL_BUILTIN_CLASS':
            is_meth: int = PEEK(oparg + 2) != cast(0, type=st.Pointer[void])
            total_args: int = oparg + is_meth
            kwnames_len: int = KWNAMES_LEN()
            callable: st.Pointer[PyObject] = PEEK(total_args + 1)
            cast(0, type=void)
            tp: st.Pointer[PyTypeObject] = cast(callable, type=st.Pointer[PyTypeObject])
            cast(0, type=void)
            cast(0, type=void)
            STACK_SHRINK(total_args)
            res: st.Pointer[PyObject] = tp.tp_vectorcall(cast(tp, type=st.Pointer[PyObject]), stack_pointer, total_args - kwnames_len, kwnames)
            kwnames = cast(0, type=st.Pointer[void])
            for i in range(0, total_args, 1):
                _Py_DECREF(cast(stack_pointer[i], type=st.Pointer[PyObject]))
            _Py_DECREF(cast(tp, type=st.Pointer[PyObject]))
            STACK_SHRINK(1 - is_meth)
            SET_TOP(res)
            if res == cast(0, type=st.Pointer[void]):
                'break # goto error'
            cast(0, type=void)
            CHECK_EVAL_BREAKER()
            DISPATCH()
        case 'CALL_NO_KW_BUILTIN_O':
            assert(cframe.use_tracing == 0)
            assert(kwnames == cast(0, type=st.Pointer[void]))
            is_meth: int = PEEK(oparg + 2) != cast(0, type=st.Pointer[void])
            total_args: int = oparg + is_meth
            cast(0, type=void)
            callable: st.Pointer[PyObject] = PEEK(total_args + 1)
            cast(0, type=void)
            cast(0, type=void)
            cast(0, type=void)
            cfunc: PyCFunction = cast(callable, type=st.Pointer[PyCFunctionObject]).m_ml.ml_meth
            if _Py_EnterRecursiveCallTstate(tstate, ' while calling a Python object'):
                'break # goto error'
            arg: st.Pointer[PyObject] = TOP()
            res: st.Pointer[PyObject] = cfunc(PyCFunction_GET_SELF(callable), arg)
            _Py_LeaveRecursiveCallTstate(tstate)
            assert((res != cast(0, type=st.Pointer[void])) ^ (_PyErr_Occurred(tstate) != cast(0, type=st.Pointer[void])))
            _Py_DECREF(cast(arg, type=st.Pointer[PyObject]))
            _Py_DECREF(cast(callable, type=st.Pointer[PyObject]))
            STACK_SHRINK(2 - is_meth)
            SET_TOP(res)
            if res == cast(0, type=st.Pointer[void]):
                'break # goto error'
            cast(0, type=void)
            CHECK_EVAL_BREAKER()
            DISPATCH()
        case 'CALL_NO_KW_BUILTIN_FAST':
            assert(cframe.use_tracing == 0)
            assert(kwnames == cast(0, type=st.Pointer[void]))
            is_meth: int = PEEK(oparg + 2) != cast(0, type=st.Pointer[void])
            total_args: int = oparg + is_meth
            callable: st.Pointer[PyObject] = PEEK(total_args + 1)
            cast(0, type=void)
            cast(0, type=void)
            cast(0, type=void)
            cfunc: PyCFunction = cast(callable, type=st.Pointer[PyCFunctionObject]).m_ml.ml_meth
            STACK_SHRINK(total_args)
            res: st.Pointer[PyObject] = cfunc(PyCFunction_GET_SELF(callable), stack_pointer, total_args)
            assert((res != cast(0, type=st.Pointer[void])) ^ (_PyErr_Occurred(tstate) != cast(0, type=st.Pointer[void])))
            for i in range(0, total_args, 1):
                _Py_DECREF(cast(stack_pointer[i], type=st.Pointer[PyObject]))
            STACK_SHRINK(2 - is_meth)
            PUSH(res)
            _Py_DECREF(cast(callable, type=st.Pointer[PyObject]))
            if res == cast(0, type=st.Pointer[void]):
                'break # goto error'
            cast(0, type=void)
            CHECK_EVAL_BREAKER()
            DISPATCH()
        case 'CALL_BUILTIN_FAST_WITH_KEYWORDS':
            assert(cframe.use_tracing == 0)
            is_meth: int = PEEK(oparg + 2) != cast(0, type=st.Pointer[void])
            total_args: int = oparg + is_meth
            callable: st.Pointer[PyObject] = PEEK(total_args + 1)
            cast(0, type=void)
            cast(0, type=void)
            cast(0, type=void)
            STACK_SHRINK(total_args)
            cfunc: _PyCFunctionFastWithKeywords = cast(callable, type=st.Pointer[PyCFunctionObject]).m_ml.ml_meth
            res: st.Pointer[PyObject] = cfunc(PyCFunction_GET_SELF(callable), stack_pointer, total_args - KWNAMES_LEN(), kwnames)
            assert((res != cast(0, type=st.Pointer[void])) ^ (_PyErr_Occurred(tstate) != cast(0, type=st.Pointer[void])))
            kwnames = cast(0, type=st.Pointer[void])
            for i in range(0, total_args, 1):
                _Py_DECREF(cast(stack_pointer[i], type=st.Pointer[PyObject]))
            STACK_SHRINK(2 - is_meth)
            PUSH(res)
            _Py_DECREF(cast(callable, type=st.Pointer[PyObject]))
            if res == cast(0, type=st.Pointer[void]):
                'break # goto error'
            cast(0, type=void)
            CHECK_EVAL_BREAKER()
            DISPATCH()
        case 'CALL_NO_KW_LEN':
            assert(cframe.use_tracing == 0)
            assert(kwnames == cast(0, type=st.Pointer[void]))
            is_meth: int = PEEK(oparg + 2) != cast(0, type=st.Pointer[void])
            total_args: int = oparg + is_meth
            cast(0, type=void)
            callable: st.Pointer[PyObject] = PEEK(total_args + 1)
            interp: st.Pointer[PyInterpreterState] = _PyInterpreterState_GET()
            cast(0, type=void)
            cast(0, type=void)
            arg: st.Pointer[PyObject] = TOP()
            len_i: Py_ssize_t = PyObject_Size(arg)
            if len_i < 0:
                'break # goto error'
            res: st.Pointer[PyObject] = PyLong_FromSsize_t(len_i)
            assert((res != cast(0, type=st.Pointer[void])) ^ (_PyErr_Occurred(tstate) != cast(0, type=st.Pointer[void])))
            STACK_SHRINK(2 - is_meth)
            SET_TOP(res)
            _Py_DECREF(cast(callable, type=st.Pointer[PyObject]))
            _Py_DECREF(cast(arg, type=st.Pointer[PyObject]))
            if res == cast(0, type=st.Pointer[void]):
                'break # goto error'
            cast(0, type=void)
            DISPATCH()
        case 'CALL_NO_KW_ISINSTANCE':
            assert(cframe.use_tracing == 0)
            assert(kwnames == cast(0, type=st.Pointer[void]))
            is_meth: int = PEEK(oparg + 2) != cast(0, type=st.Pointer[void])
            total_args: int = oparg + is_meth
            callable: st.Pointer[PyObject] = PEEK(total_args + 1)
            cast(0, type=void)
            interp: st.Pointer[PyInterpreterState] = _PyInterpreterState_GET()
            cast(0, type=void)
            cast(0, type=void)
            cls: st.Pointer[PyObject] = POP()
            inst: st.Pointer[PyObject] = TOP()
            retval: int = PyObject_IsInstance(inst, cls)
            if retval < 0:
                _Py_DECREF(cast(cls, type=st.Pointer[PyObject]))
                'break # goto error'
            res: st.Pointer[PyObject] = PyBool_FromLong(retval)
            assert((res != cast(0, type=st.Pointer[void])) ^ (_PyErr_Occurred(tstate) != cast(0, type=st.Pointer[void])))
            STACK_SHRINK(2 - is_meth)
            SET_TOP(res)
            _Py_DECREF(cast(inst, type=st.Pointer[PyObject]))
            _Py_DECREF(cast(cls, type=st.Pointer[PyObject]))
            _Py_DECREF(cast(callable, type=st.Pointer[PyObject]))
            if res == cast(0, type=st.Pointer[void]):
                'break # goto error'
            cast(0, type=void)
            DISPATCH()
        case 'CALL_NO_KW_LIST_APPEND':
            assert(cframe.use_tracing == 0)
            assert(kwnames == cast(0, type=st.Pointer[void]))
            assert(oparg == 1)
            callable: st.Pointer[PyObject] = PEEK(3)
            interp: st.Pointer[PyInterpreterState] = _PyInterpreterState_GET()
            cast(0, type=void)
            list: st.Pointer[PyObject] = SECOND()
            cast(0, type=void)
            cast(0, type=void)
            arg: st.Pointer[PyObject] = POP()
            if _PyList_AppendTakeRef(cast(list, type=st.Pointer[PyListObject]), arg) < 0:
                'break # goto error'
            STACK_SHRINK(2)
            _Py_DECREF(cast(list, type=st.Pointer[PyObject]))
            _Py_DECREF(cast(callable, type=st.Pointer[PyObject]))
            cast(0, type=void)
            assert(next_instr[-1] & 255 == 1)
            DISPATCH()
        case 'CALL_NO_KW_METHOD_DESCRIPTOR_O':
            assert(kwnames == cast(0, type=st.Pointer[void]))
            is_meth: int = PEEK(oparg + 2) != cast(0, type=st.Pointer[void])
            total_args: int = oparg + is_meth
            callable: st.Pointer[PyMethodDescrObject] = cast(PEEK(total_args + 1), type=st.Pointer[PyMethodDescrObject])
            cast(0, type=void)
            cast(0, type=void)
            meth: st.Pointer[PyMethodDef] = callable.d_method
            cast(0, type=void)
            arg: st.Pointer[PyObject] = TOP()
            self: st.Pointer[PyObject] = SECOND()
            cast(0, type=void)
            cast(0, type=void)
            cfunc: PyCFunction = meth.ml_meth
            if _Py_EnterRecursiveCallTstate(tstate, ' while calling a Python object'):
                'break # goto error'
            res: st.Pointer[PyObject] = cfunc(self, arg)
            _Py_LeaveRecursiveCallTstate(tstate)
            assert((res != cast(0, type=st.Pointer[void])) ^ (_PyErr_Occurred(tstate) != cast(0, type=st.Pointer[void])))
            _Py_DECREF(cast(self, type=st.Pointer[PyObject]))
            _Py_DECREF(cast(arg, type=st.Pointer[PyObject]))
            STACK_SHRINK(oparg + 1)
            SET_TOP(res)
            _Py_DECREF(cast(callable, type=st.Pointer[PyObject]))
            if res == cast(0, type=st.Pointer[void]):
                'break # goto error'
            cast(0, type=void)
            CHECK_EVAL_BREAKER()
            DISPATCH()
        case 'CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS':
            is_meth: int = PEEK(oparg + 2) != cast(0, type=st.Pointer[void])
            total_args: int = oparg + is_meth
            callable: st.Pointer[PyMethodDescrObject] = cast(PEEK(total_args + 1), type=st.Pointer[PyMethodDescrObject])
            cast(0, type=void)
            meth: st.Pointer[PyMethodDef] = callable.d_method
            cast(0, type=void)
            d_type: st.Pointer[PyTypeObject] = callable.d_common.d_type
            self: st.Pointer[PyObject] = PEEK(total_args)
            cast(0, type=void)
            cast(0, type=void)
            nargs: int = total_args - 1
            STACK_SHRINK(nargs)
            cfunc: _PyCFunctionFastWithKeywords = meth.ml_meth
            res: st.Pointer[PyObject] = cfunc(self, stack_pointer, nargs - KWNAMES_LEN(), kwnames)
            assert((res != cast(0, type=st.Pointer[void])) ^ (_PyErr_Occurred(tstate) != cast(0, type=st.Pointer[void])))
            kwnames = cast(0, type=st.Pointer[void])
            for i in range(0, nargs, 1):
                _Py_DECREF(cast(stack_pointer[i], type=st.Pointer[PyObject]))
            _Py_DECREF(cast(self, type=st.Pointer[PyObject]))
            STACK_SHRINK(2 - is_meth)
            SET_TOP(res)
            _Py_DECREF(cast(callable, type=st.Pointer[PyObject]))
            if res == cast(0, type=st.Pointer[void]):
                'break # goto error'
            cast(0, type=void)
            CHECK_EVAL_BREAKER()
            DISPATCH()
        case 'CALL_NO_KW_METHOD_DESCRIPTOR_NOARGS':
            assert(kwnames == cast(0, type=st.Pointer[void]))
            assert(oparg == 0 or oparg == 1)
            is_meth: int = PEEK(oparg + 2) != cast(0, type=st.Pointer[void])
            total_args: int = oparg + is_meth
            cast(0, type=void)
            callable: st.Pointer[PyMethodDescrObject] = cast(SECOND(), type=st.Pointer[PyMethodDescrObject])
            cast(0, type=void)
            meth: st.Pointer[PyMethodDef] = callable.d_method
            self: st.Pointer[PyObject] = TOP()
            cast(0, type=void)
            cast(0, type=void)
            cast(0, type=void)
            cfunc: PyCFunction = meth.ml_meth
            if _Py_EnterRecursiveCallTstate(tstate, ' while calling a Python object'):
                'break # goto error'
            res: st.Pointer[PyObject] = cfunc(self, cast(0, type=st.Pointer[void]))
            _Py_LeaveRecursiveCallTstate(tstate)
            assert((res != cast(0, type=st.Pointer[void])) ^ (_PyErr_Occurred(tstate) != cast(0, type=st.Pointer[void])))
            _Py_DECREF(cast(self, type=st.Pointer[PyObject]))
            STACK_SHRINK(oparg + 1)
            SET_TOP(res)
            _Py_DECREF(cast(callable, type=st.Pointer[PyObject]))
            if res == cast(0, type=st.Pointer[void]):
                'break # goto error'
            cast(0, type=void)
            CHECK_EVAL_BREAKER()
            DISPATCH()
        case 'CALL_NO_KW_METHOD_DESCRIPTOR_FAST':
            assert(kwnames == cast(0, type=st.Pointer[void]))
            is_meth: int = PEEK(oparg + 2) != cast(0, type=st.Pointer[void])
            total_args: int = oparg + is_meth
            callable: st.Pointer[PyMethodDescrObject] = cast(PEEK(total_args + 1), type=st.Pointer[PyMethodDescrObject])
            cast(0, type=void)
            meth: st.Pointer[PyMethodDef] = callable.d_method
            cast(0, type=void)
            self: st.Pointer[PyObject] = PEEK(total_args)
            cast(0, type=void)
            cast(0, type=void)
            cfunc: _PyCFunctionFast = meth.ml_meth
            nargs: int = total_args - 1
            STACK_SHRINK(nargs)
            res: st.Pointer[PyObject] = cfunc(self, stack_pointer, nargs)
            assert((res != cast(0, type=st.Pointer[void])) ^ (_PyErr_Occurred(tstate) != cast(0, type=st.Pointer[void])))
            for i in range(0, nargs, 1):
                _Py_DECREF(cast(stack_pointer[i], type=st.Pointer[PyObject]))
            _Py_DECREF(cast(self, type=st.Pointer[PyObject]))
            STACK_SHRINK(2 - is_meth)
            SET_TOP(res)
            _Py_DECREF(cast(callable, type=st.Pointer[PyObject]))
            if res == cast(0, type=st.Pointer[void]):
                'break # goto error'
            cast(0, type=void)
            CHECK_EVAL_BREAKER()
            DISPATCH()
        case 'CALL_FUNCTION_EX':
            PREDICTED(142)
            func: st.Pointer[PyObject]
            callargs: st.Pointer[PyObject]
            kwargs: st.Pointer[PyObject] = cast(0, type=st.Pointer[void])
            result: st.Pointer[PyObject]
            if oparg & 1:
                kwargs = POP()
                assert(_Py_IS_TYPE(cast(kwargs, type=st.Pointer[st.Const[PyObject]]), ref(PyDict_Type)))
            callargs = POP()
            func = TOP()
            if not _Py_IS_TYPE(cast(callargs, type=st.Pointer[st.Const[PyObject]]), ref(PyTuple_Type)):
                if check_args_iterable(tstate, func, callargs) < 0:
                    _Py_DECREF(cast(callargs, type=st.Pointer[PyObject]))
                    'break # goto error'
                Py_SETREF(callargs, PySequence_Tuple(callargs))
                if callargs == cast(0, type=st.Pointer[void]):
                    'break # goto error'
            assert(_Py_IS_TYPE(cast(callargs, type=st.Pointer[st.Const[PyObject]]), ref(PyTuple_Type)))
            result = do_call_core(tstate, func, callargs, kwargs, cframe.use_tracing)
            _Py_DECREF(cast(func, type=st.Pointer[PyObject]))
            _Py_DECREF(cast(callargs, type=st.Pointer[PyObject]))
            Py_XDECREF(kwargs)
            STACK_SHRINK(1)
            assert(TOP() == cast(0, type=st.Pointer[void]))
            SET_TOP(result)
            if result == cast(0, type=st.Pointer[void]):
                'break # goto error'
            CHECK_EVAL_BREAKER()
            DISPATCH()
        case 'MAKE_FUNCTION':
            codeobj: st.Pointer[PyObject] = POP()
            func: st.Pointer[PyFunctionObject] = cast(PyFunction_New(codeobj, GLOBALS()), type=st.Pointer[PyFunctionObject])
            _Py_DECREF(cast(codeobj, type=st.Pointer[PyObject]))
            if func == cast(0, type=st.Pointer[void]):
                'break # goto error'
            if oparg & 8:
                assert(_Py_IS_TYPE(cast(TOP(), type=st.Pointer[st.Const[PyObject]]), ref(PyTuple_Type)))
                func.func_closure = POP()
            if oparg & 4:
                assert(_Py_IS_TYPE(cast(TOP(), type=st.Pointer[st.Const[PyObject]]), ref(PyTuple_Type)))
                func.func_annotations = POP()
            if oparg & 2:
                assert(_Py_IS_TYPE(cast(TOP(), type=st.Pointer[st.Const[PyObject]]), ref(PyDict_Type)))
                func.func_kwdefaults = POP()
            if oparg & 1:
                assert(_Py_IS_TYPE(cast(TOP(), type=st.Pointer[st.Const[PyObject]]), ref(PyTuple_Type)))
                func.func_defaults = POP()
            func.func_version = cast(codeobj, type=st.Pointer[PyCodeObject]).co_version
            PUSH(cast(func, type=st.Pointer[PyObject]))
            DISPATCH()
        case 'RETURN_GENERATOR':
            assert(_Py_IS_TYPE(cast(frame.f_funcobj, type=st.Pointer[st.Const[PyObject]]), ref(PyFunction_Type)))
            func: st.Pointer[PyFunctionObject] = cast(frame.f_funcobj, type=st.Pointer[PyFunctionObject])
            gen: st.Pointer[PyGenObject] = cast(_Py_MakeCoro(func), type=st.Pointer[PyGenObject])
            if gen == cast(0, type=st.Pointer[void]):
                'break # goto error'
            assert(EMPTY())
            _PyFrame_SetStackPointer(frame, stack_pointer)
            gen_frame: st.Pointer[_PyInterpreterFrame] = cast(gen.gi_iframe, type=st.Pointer[_PyInterpreterFrame])
            _PyFrame_Copy(frame, gen_frame)
            assert(frame.frame_obj == cast(0, type=st.Pointer[void]))
            gen.gi_frame_state = FRAME_CREATED
            gen_frame.owner = FRAME_OWNED_BY_GENERATOR
            _Py_LeaveRecursiveCallPy(tstate)
            assert(frame != ref(entry_frame))
            prev: st.Pointer[_PyInterpreterFrame] = frame.previous
            _PyThreadState_PopFrame(tstate, frame)
            frame = 
            cframe.current_frame = prev
            _PyFrame_StackPush(frame, cast(gen, type=st.Pointer[PyObject]))
            'break # goto resume_frame'
        case 'BUILD_SLICE':
            start: st.Pointer[PyObject]
            stop: st.Pointer[PyObject]
            step: st.Pointer[PyObject]
            slice: st.Pointer[PyObject]
            if oparg == 3:
                step = POP()
            else:
                step = cast(0, type=st.Pointer[void])
            stop = POP()
            start = TOP()
            slice = PySlice_New(start, stop, step)
            _Py_DECREF(cast(start, type=st.Pointer[PyObject]))
            _Py_DECREF(cast(stop, type=st.Pointer[PyObject]))
            Py_XDECREF(step)
            SET_TOP(slice)
            if slice == cast(0, type=st.Pointer[void]):
                'break # goto error'
            DISPATCH()
        case 'FORMAT_VALUE':
            result: st.Pointer[PyObject]
            fmt_spec: st.Pointer[PyObject]
            value: st.Pointer[PyObject]
            which_conversion: int = oparg & 3
            have_fmt_spec: int = oparg & 4 == 4
            fmt_spec = have_fmt_spec if POP() else cast(0, type=st.Pointer[void])
            value = POP()
            match which_conversion:
                case 0:
                    conv_fn = cast(0, type=st.Pointer[void])
                    return
                case 1:
                    conv_fn = PyObject_Str
                    return
                case 2:
                    conv_fn = PyObject_Repr
                    return
                case 3:
                    conv_fn = PyObject_ASCII
                    return
                case True:_PyErr_Format(tstate, PyExc_SystemError, 'unexpected conversion flag %d', which_conversion)'break # goto error'
            if conv_fn != cast(0, type=st.Pointer[void]):
                result = conv_fn(value)
                _Py_DECREF(cast(value, type=st.Pointer[PyObject]))
                if result == cast(0, type=st.Pointer[void]):
                    Py_XDECREF(fmt_spec)
                    'break # goto error'
                value = result
            if _Py_IS_TYPE(cast(value, type=st.Pointer[st.Const[PyObject]]), ref(PyUnicode_Type)) and fmt_spec == cast(0, type=st.Pointer[void]):
                result = value
            else:
                result = PyObject_Format(value, fmt_spec)
                _Py_DECREF(cast(value, type=st.Pointer[PyObject]))
                Py_XDECREF(fmt_spec)
                if result == cast(0, type=st.Pointer[void]):
                    'break # goto error'
            PUSH(result)
            DISPATCH()
        case 'COPY':
            assert(oparg != 0)
            peek: st.Pointer[PyObject] = PEEK(oparg)
            PUSH(_Py_NewRef(cast(peek, type=st.Pointer[PyObject])))
            DISPATCH()
        case 'BINARY_OP':
            PREDICTED(BINARY_OP)
            assert sizeof(_PyBinaryOpCache) / sizeof(_Py_CODEUNIT) == 1, 'incorrect cache size'
            pass
            rhs: st.Pointer[PyObject] = PEEK(1)
            lhs: st.Pointer[PyObject] = PEEK(2)
            res: st.Pointer[PyObject]
            cache: st.Pointer[_PyBinaryOpCache] = cast(next_instr, type=st.Pointer[_PyBinaryOpCache])
            if ADAPTIVE_COUNTER_IS_ZERO(cache.counter):
                assert(cframe.use_tracing == 0)
                next_instr -= 1
                _Py_Specialize_BinaryOp(lhs, rhs, next_instr, oparg, ref(frame.localsplus[0]))
                cast(0, type=void)
            cast(0, type=void)
            DECREMENT_ADAPTIVE_COUNTER(cache.counter)
            assert(0 <= oparg)
            assert(cast(oparg, type=unsigned) < Py_ARRAY_LENGTH(binary_ops))
            assert(binary_ops[oparg])
            res = binary_ops[oparg](lhs, rhs)
            _Py_DECREF(cast(lhs, type=st.Pointer[PyObject]))
            _Py_DECREF(cast(rhs, type=st.Pointer[PyObject]))
            if res == cast(0, type=st.Pointer[void]):
                'break # goto pop_2_error'
            STACK_SHRINK(1)
            POKE(1, res)
            cast(0, type=void)
            DISPATCH()
        case 'SWAP':
            assert(oparg != 0)
            top: st.Pointer[PyObject] = TOP()
            SET_TOP(PEEK(oparg))
            PEEK(oparg) = top
            DISPATCH()
        case 'EXTENDED_ARG':
            assert(oparg)
            assert(cframe.use_tracing == 0)
            opcode = deref(next_instr) & 255
            oparg = oparg << 8 | deref(next_instr) >> 8
            PRE_DISPATCH_GOTO()
            DISPATCH_GOTO()
        case 'CACHE':
            Py_UNREACHABLE()
    '# label: n.name'
    '# label: n.name'
    '# label: n.name'
    '# label: n.name'
    '# label: n.name'