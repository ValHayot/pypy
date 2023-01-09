import argparse
import ast
import os
import re
from textwrap import dedent

from pycparser import parse_file, preprocess_file, CParser
from pycparser.c_generator import CGenerator

from interpreter_generator.py_generator import (
    CAstGeneralizerBackend,
    FixupMatchsVisitor,
    FixupConstantsVisitor,
    FixupCallAssignVisitor,
    FixupNullVisitor,
)
from interpreter_generator.generate_cases import main

DEFAULT_INPUT = os.path.relpath(
    os.path.join(os.path.dirname(__file__), "generated_cases.c")
)
DEFAULT_OUTPUT = os.path.relpath(
    os.path.join(os.path.dirname(__file__), "../interpreter/interpreter.py")
)


def translate_to_py(filename, output_filename):
    """Simply use the c_generator module to emit a parsed AST."""
    c_preproc_args = [
        "-E",  # only run the preprocessor
        "-Wno-everything",
    ]
    print(f"clang {' '.join(c_preproc_args + [filename])}")
    text = preprocess_file(filename, "clang", c_preproc_args)
    text = (
        text.replace("((_PyCFunctionFast)(void(*)(void))cfunc)", "cfunc")
        .replace("(_PyCFunctionFastWithKeywords)(void(*)(void))", "")
        .replace("(_PyCFunctionFast)(void(*)(void))meth", "meth")
        .replace("PyObject *(*conv_fn)(PyObject *);", "")
    )
    # text = text.replace("__uint16_t", "int").replace("unsigned short int", "short")
    with open("out.c", "w") as f:
        f.write(text)

    parser = CParser()
    tree = parser.parse(text, filename)
    generator = CAstGeneralizerBackend()
    with open(output_filename, "w") as o:
        o.write(
            dedent(
                """\
        from typing import Any, List, Callable
        # from pytype.pyc import opcodes as ops
        
        BINARY_OP: Any 
        BINARY_SUBSCR: Any 
        CALL: Any 
        CALL_PY_EXACT_ARGS: Any 
        COMPARE_OP: Any 
        CO_ASYNC_GENERATOR: Any 
        CO_COROUTINE: Any 
        CO_ITERABLE_COROUTINE: Any 
        CO_OPTIMIZED: Any 
        DICT_KEYS_UNICODE: Any 
        END_FOR: Any 
        FOR_ITER: Any 
        FRAME_CREATED: Any 
        FRAME_EXECUTING: Any 
        FRAME_OWNED_BY_GENERATOR: Any 
        FRAME_SUSPENDED: Any 
        FVC_ASCII: Any 
        FVC_MASK: Any 
        FVC_NONE: Any 
        FVC_REPR: Any 
        FVC_STR: Any 
        FVS_HAVE_SPEC: Any 
        FVS_MASK: Any 
        INLINE_CACHE_ENTRIES_BINARY_OP: Any 
        INLINE_CACHE_ENTRIES_BINARY_SUBSCR: Any 
        INLINE_CACHE_ENTRIES_CALL: Any 
        INLINE_CACHE_ENTRIES_FOR_ITER: Any 
        INLINE_CACHE_ENTRIES_LOAD_ATTR: Any 
        INLINE_CACHE_ENTRIES_LOAD_GLOBAL: Any 
        INLINE_CACHE_ENTRIES_UNPACK_SEQUENCE: Any 
        JUMP_BACKWARD: Any 
        LOAD_ATTR: Any 
        LOAD_CONST: Any 
        LOAD_GLOBAL: Any 
        METH_FASTCALL: Any 
        METH_KEYWORDS: Any 
        METH_NOARGS: Any 
        METH_O: Any 
        POP_JUMP_IF_FALSE: Any 
        POP_JUMP_IF_TRUE: Any 
        POP_TOP: Any 
        PYGEN_ERROR: Any 
        PYGEN_NEXT: Any 
        PYGEN_RETURN: Any 
        STORE_ATTR: Any 
        STORE_FAST: Any 
        STORE_FAST__LOAD_FAST: Any 
        STORE_SUBSCR: Any 
        UNPACK_SEQUENCE: Any 
        
        ADAPTIVE_COUNTER_IS_ZERO: Callable 
        BUILTINS: Callable 
        CHECK_EVAL_BREAKER: Callable 
        DECREMENT_ADAPTIVE_COUNTER: Callable 
        DEOPT_IF: Callable 
        DISPATCH: Callable 
        DISPATCH_GOTO: Callable 
        DISPATCH_INLINED: Callable 
        DISPATCH_SAME_OPARG: Callable 
        DK_ENTRIES: Callable 
        DK_IS_UNICODE: Callable 
        DK_UNICODE_ENTRIES: Callable 
        DTRACE_FUNCTION_EXIT: Callable 
        EMPTY: Callable 
        GETITEM: Callable 
        GETLOCAL: Callable 
        GLOBALS: Callable 
        GO_TO_INSTRUCTION: Callable 
        INSTR_OFFSET: Callable 
        JUMPBY: Callable 
        KWNAMES_LEN: Callable 
        LOCALS: Callable 
        NEXTOPARG: Callable 
        POP: Callable 
        PREDICT: Callable 
        PREDICTED: Callable 
        PRE_DISPATCH_GOTO: Callable 
        PUSH: Callable 
        SECOND: Callable 
        SETLOCAL: Callable 
        STACK_GROW: Callable 
        STACK_LEVEL: Callable 
        STACK_SHRINK: Callable 
        TOP: Callable 
        TRACE_FUNCTION_EXIT: Callable 
        
        PyCFunction: Any 
        PyCodeObject: Any 
        PyDictKeyEntry: Any 
        PyDictObject: Any 
        PyDictOrValues: Any 
        PyDictUnicodeEntry: Any 
        PyDictValues: Any 
        PyDict_EVENT_MODIFIED: Any 
        PyExc_AssertionError: Any 
        PyExc_AttributeError: Any 
        PyExc_KeyError: Any 
        PyExc_NameError: Any 
        PyExc_RuntimeError: Any 
        PyExc_StopAsyncIteration: Any 
        PyExc_StopIteration: Any 
        PyExc_SystemError: Any 
        PyExc_TypeError: Any 
        PyFunctionObject: Any 
        PyFunction_Type: Any 
        PyGenObject: Any 
        PyGen_Type: Any 
        PyHeapTypeObject: Any 
        PyInterpreterState: Any 
        PyListIter_Type: Any 
        PyListObject: Any 
        PyMethodDef: Any 
        PyMethodDescrObject: Any 
        PyMethodDescrObject: Any 
        PyMethodDescr_Type: Any 
        PyMethodDescr_Type: Any 
        PyMethod_Type: Any 
        PyObject: Any 
        PyRangeIter_Type: Any 
        PySendResult: Any 
        PyThreadState: Any 
        PyTupleIter_Type: Any 
        PyTupleObject: Any 
        PyTuple_Type: Any 
        PyTypeObject: Any = type
        PyType_Type: Any 
        PyUnicode_Type: Any 
        Py_EQ: Any 
        Py_GE: Any 
        Py_NE: Any 
        Py_SIZE: Any 
        Py_TPFLAGS_HEAPTYPE: Any 
        Py_TPFLAGS_MANAGED_DICT: Any 
        Py_TPFLAGS_MAPPING: Any 
        Py_TPFLAGS_METHOD_DESCRIPTOR: Any 
        Py_TPFLAGS_SEQUENCE: Any 
        Py_ssize_t: Any 
        _PyAttrCache: Any 
        _PyBinaryOpCache: Any 
        _PyBinarySubscrCache: Any 
        _PyCFrame: Any 
        _PyCFunctionFast: Any 
        _PyCFunctionFastWithKeywords: Any 
        _PyCallCache: Any 
        _PyCompareOpCache: Any 
        _PyErr_StackItem: Any 
        _PyForIterCache: Any 
        _PyFunction_Vectorcall: Any 
        _PyInterpreterFrame: Any 
        _PyListIterObject: Any 
        _PyLoadGlobalCache: Any 
        _PyLoadMethodCache: Any 
        _PyOpcode_Deopt: Any 
        _PyRangeIterObject: Any 
        _PyStoreSubscrCache: Any 
        _PyTupleIterObject: Any 
        _PyUnpackSequenceCache: Any 
        _Py_CODEUNIT: Any 
        _Py_atomic_int: Any 
        binaryfunc: Any 
        next_instr: Any 
        unaryfunc: Any 
        
        PyAsyncGen_CheckExact: Callable 
        PyCFunction_CheckExact: Callable 
        PyCFunction_GET_FLAGS: Callable 
        PyCFunction_GET_FUNCTION: Callable 
        PyCFunction_GET_SELF: Callable 
        PyCell_GET: Callable 
        PyCell_New: Callable 
        PyCell_SET: Callable 
        PyCoro_CheckExact: Callable 
        PyDict_CheckExact: Callable 
        PyDict_DelItem: Callable 
        PyDict_GetItemWithError: Callable 
        PyDict_SetItem: Callable 
        PyDict_Update: Callable 
        PyErr_GivenExceptionMatches: Callable 
        PyErr_SetExcInfo: Callable 
        PyExceptionInstance_Check: Callable 
        PyExceptionInstance_Class: Callable 
        PyException_GetTraceback: Callable 
        PyException_SetCause: Callable 
        PyException_SetContext: Callable 
        PyFloat_CheckExact: Callable 
        PyFunction_Check: Callable 
        PyFunction_GET_CODE: Callable 
        PyFunction_GET_GLOBALS: Callable 
        PyFunction_New: Callable 
        PyGen_CheckExact: Callable 
        PyIter_Check: Callable 
        PyIter_Send: Callable 
        PyList_AsTuple: Callable 
        PyList_Check: Callable 
        PyList_CheckExact: Callable 
        PyLong_Check: Callable 
        PyLong_CheckExact: Callable 
        PyModule_CheckExact: Callable 
        PyNumber_Negative: Callable 
        PyNumber_Positive: Callable 
        PyObject_CallMethodOneArg: Callable 
        PyObject_CallOneArg: Callable 
        PyObject_DelItem: Callable 
        PyObject_IsTrue: Callable 
        PyObject_RichCompare: Callable 
        PyObject_SetAttr: Callable 
        PyObject_SetItem: Callable 
        PyObject_Str: Callable 
        PyObject_Vectorcall: Callable 
        PySequence_Check: Callable 
        PySequence_Contains: Callable 
        PySequence_Tuple: Callable 
        PyTuple_CheckExact: Callable 
        PyType_Check: Callable 
        PyUnicode_CheckExact: Callable 
        Py_CLEAR: Callable 
        Py_IS_TYPE: Callable 
        Py_Is: Callable 
        Py_IsFalse: Callable 
        Py_IsNone: Callable 
        Py_IsTrue: Callable 
        Py_NewRef: Callable 
        Py_REFCNT: Callable 
        Py_SETREF: Callable 
        Py_UNREACHABLE: Callable 
        Py_XSETREF: Callable 
        _PyAsyncGenValueWrapperNew: Callable 
        _PyBuildSlice_ConsumeRefs: Callable 
        _PyCFunction_TrampolineCall: Callable 
        _PyCode_CODE: Callable 
        _PyCoro_GetAwaitableIter: Callable 
        _PyCoro_GetAwaitableIter: Callable 
        _PyDictOrValues_GetDict: Callable 
        _PyDictOrValues_GetValues: Callable 
        _PyDictOrValues_IsValues: Callable 
        _PyDictValues_AddToInsertionOrder: Callable 
        _PyDict_FromItems: Callable 
        _PyDict_GetItemWithError: Callable 
        _PyDict_LoadGlobal: Callable 
        _PyDict_MergeEx: Callable 
        _PyDict_NotifyEvent: Callable 
        _PyDict_SetItem_Take2: Callable 
        _PyErr_Clear: Callable 
        _PyErr_ExceptionMatches: Callable 
        _PyErr_Format: Callable 
        _PyErr_FormatFromCause: Callable 
        _PyErr_Occurred: Callable 
        _PyErr_Restore: Callable 
        _PyErr_SetKeyError: Callable 
        _PyErr_SetString: Callable 
        _PyEvalFrameClearAndPop: Callable 
        _PyEvalFramePushAndInit: Callable 
        _PyExc_PrepReraiseStar: Callable 
        _PyFrame_Copy: Callable 
        _PyFrame_FastToLocalsWithError: Callable 
        _PyFrame_GetGenerator: Callable 
        _PyFrame_IsIncomplete: Callable 
        _PyFrame_LocalsToFast: Callable 
        _PyFrame_PushUnchecked: Callable 
        _PyFrame_SetStackPointer: Callable 
        _PyFrame_StackPush: Callable 
        _PyGen_FetchStopIterationValue: Callable 
        _PyGen_yf: Callable 
        _PyInterpreterState_GET: Callable 
        _PyList_AppendTakeRef: Callable 
        _PyList_FromArraySteal: Callable 
        _PyList_ITEMS: Callable 
        _PyLong_AssignValue: Callable 
        _PyLong_GetZero: Callable 
        _PyLong_IsPositiveSingleDigit: Callable 
        _PyObject_CallNoArgs: Callable 
        _PyObject_DictOrValuesPointer: Callable 
        _PyObject_GC_IS_TRACKED: Callable 
        _PyObject_GC_MAY_BE_TRACKED: Callable 
        _PyObject_GC_TRACK: Callable 
        _PyObject_GetMethod: Callable 
        _PyObject_LookupSpecial: Callable 
        _PySet_Update: Callable 
        _PySys_GetAttr: Callable 
        _PyThreadState_HasStackSpace: Callable 
        _PyThreadState_PopFrame: Callable 
        _PyTuple_FromArraySteal: Callable 
        _PyTuple_ITEMS: Callable 
        _PyType_HasFeature: Callable 
        _PyType_HasFeature: Callable 
        _PyUnicode_FromASCII: Callable 
        _PyUnicode_JoinArray: Callable 
        _Py_DECREF_NO_DEALLOC: Callable 
        _Py_EnterRecursiveCallTstate: Callable 
        _Py_LeaveRecursiveCallPy: Callable 
        _Py_LeaveRecursiveCallTstate: Callable 
        _Py_MakeCoro: Callable 
        _Py_OPARG: Callable 
        _Py_OPCODE: Callable 
        _Py_STR: Callable 
        _Py_Specialize_BinaryOp: Callable 
        _Py_Specialize_BinarySubscr: Callable 
        _Py_Specialize_Call: Callable 
        _Py_Specialize_CompareOp: Callable 
        _Py_Specialize_ForIter: Callable 
        _Py_Specialize_LoadAttr: Callable 
        _Py_Specialize_LoadGlobal: Callable 
        _Py_Specialize_StoreAttr: Callable 
        _Py_Specialize_StoreSubscr: Callable 
        _Py_Specialize_UnpackSequence: Callable 
        _Py_atomic_load_relaxed_int32: Callable 
        
        call_exc_trace: Callable 
        check_args_iterable: Callable 
        check_except_star_type_valid: Callable 
        check_except_type_valid: Callable 
        deref: Callable 
        do_call_core: Callable 
        do_raise: Callable 
        exception_group_match: Callable 
        format_awaitable_error: Callable 
        format_exc_check_arg: Callable 
        format_exc_unbound: Callable 
        format_kwargs_error: Callable 
        import_all_from: Callable 
        import_from: Callable 
        import_name: Callable 
        is_method: Callable 
        match_class: Callable 
        match_keys: Callable 
        post_decr: Callable 
        post_incr: Callable 
        read_obj: Callable 
        read_u16: Callable 
        read_u32: Callable 
        ref: Callable 
        static_assert: Callable 
        trace_call_function: Callable 
        unpack_iterable: Callable 
        
        """
            )
        )
        # ^(?:[\t ]*(?:\r?\n|\r))+ after wards
        mod = generator.visit(tree)
        print(generator.field_names)
        mod = FixupMatchsVisitor().visit(mod)
        mod = FixupCallAssignVisitor().visit(mod)
        mod = FixupConstantsVisitor().visit(mod)
        mod = FixupNullVisitor(
            field_names=generator.field_names + ["entry_frame"]
        ).visit(mod)
        o.write(ast.unparse(mod))


if __name__ == "__main__":
    arg_parser = argparse.ArgumentParser(
        description="Generate the code for the interpreter switch.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    arg_parser.add_argument(
        "-i", "--input", type=str, help="Instruction definitions", default=DEFAULT_INPUT
    )
    arg_parser.add_argument(
        "-o", "--output", type=str, help="Generated code", default=DEFAULT_OUTPUT
    )
    args = arg_parser.parse_args()
    translate_to_py(args.input, args.output)
