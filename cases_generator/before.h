//
// Created by mlevental on 1/5/23.
//
//#include "pycore_frame.h"         // _PyInterpreterFrame

#ifndef PYPY_CASES_GENERATOR_BEFORE_H
#define PYPY_CASES_GENERATOR_BEFORE_H

//typedef struct {
//
//  PyObject ob_base; PyCodeObject *gi_code; PyObject *gi_weakreflist; PyObject *gi_name; PyObject *gi_qualname; _PyErr_StackItem gi_exc_state; PyObject *gi_origin_or_finalizer; char gi_hooks_inited; char gi_closed; char gi_running_async; int8_t gi_frame_state; PyObject *gi_iframe[1];
//} PyGenObject;


//#define offsetof(TYPE, MEMBER)

//typedef struct _PyCFrame {
//  /* This struct will be threaded through the C stack
//     * allowing fast access to per-thread state that needs
//     * to be accessed quickly by the interpreter, but can
//     * be modified outside of the interpreter.
//     *
//     * WARNING: This makes data on the C stack accessible from
//     * heap objects. Care must be taken to maintain stack
//     * discipline and make sure that instances of this struct cannot
//     * accessed outside of their lifetime.
//   */
//  uint8_t use_tracing;  // 0 or 255 (or'ed into opcode, hence 8-bit type)
//  /* Pointer to the currently executing frame (it can be NULL) */
//  struct _PyInterpreterFrame *current_frame;
//  struct _PyCFrame *previous;
//} _PyCFrame;
//
//#define _Py_atomic_load_relaxed_int32(ATOMIC_VAL) _Py_atomic_load_relaxed(ATOMIC_VAL)
//
//static int do_raise(PyThreadState *tstate, PyObject *exc, PyObject *cause);
//static int exception_group_match(
//    PyObject* exc_value, PyObject *match_type,
//    PyObject **match, PyObject **rest);
//
//static inline void _Py_LeaveRecursiveCallPy(PyThreadState *tstate);
//
//static void
//format_awaitable_error(PyThreadState *tstate, PyTypeObject *type, int oparg);
//
//#define _Py_RVALUE(EXPR) ((void)0, (EXPR))
//#define _PyCode_CODE(CO) _Py_RVALUE((_Py_CODEUNIT *)(CO)->co_code_adaptive)
//
//PyObject *
//_PyDict_GetItemWithError(PyObject *dp, PyObject *kv);
//
//static void format_exc_check_arg(PyThreadState *, PyObject *, const char *, PyObject *);
//
//static int unpack_iterable(PyThreadState *, PyObject *, int, int, PyObject **);
//
//static void
//format_exc_unbound(PyThreadState *tstate, PyCodeObject *co, int oparg);
//
//static void format_kwargs_error(PyThreadState *, PyObject *func, PyObject *kwargs);
//
//#define Py_TPFLAGS_MANAGED_DICT (1 << 4)
//
typedef struct _dictvalues PyDictValues;

typedef enum {
  PyDict_EVENT_ADDED,
  PyDict_EVENT_MODIFIED,
  PyDict_EVENT_DELETED,
  PyDict_EVENT_CLONED,
  PyDict_EVENT_CLEARED,
  PyDict_EVENT_DEALLOCATED,
} PyDict_WatchEvent;
//
//int
//_PyUnicode_Equal(PyObject *str1, PyObject *str2);
//
//static int check_except_star_type_valid(PyThreadState *tstate, PyObject* right);
//
//static int
//check_except_type_valid(PyThreadState *tstate, PyObject* right);
//
//static PyObject * import_from(PyThreadState *, PyObject *, PyObject *);
//static int import_all_from(PyThreadState *, PyObject *, PyObject *);
//
//static PyObject*
//match_class(PyThreadState *tstate, PyObject *subject, PyObject *type,
//            Py_ssize_t nargs, PyObject *kwargs);
//
//static PyObject*
//match_keys(PyThreadState *tstate, PyObject *map, PyObject *keys);
//
//#define is_method(stack_pointer, args) (PEEK((args)+2) != NULL)
//
//static PyObject *
//trace_call_function(PyThreadState *tstate,
//                    PyObject *func,
//                    PyObject **args, Py_ssize_t nargs,
//                    PyObject *kwnames);
//
//static int
//check_args_iterable(PyThreadState *tstate, PyObject *func, PyObject *args);
//
//static PyObject * do_call_core(
//    PyThreadState *tstate, PyObject *func,
//    PyObject *callargs, PyObject *kwdict, int use_tracing);
//
//PyObject *
//_PySys_GetAttr(PyThreadState *tstate, PyObject *name);
//
//typedef int(*PyDict_WatchCallback)(PyDict_WatchEvent event, PyObject* dict, PyObject* key, PyObject* new_value);
//
//typedef PyObject* (*_PyFrameEvalFunction)(PyThreadState *tstate, struct _PyInterpreterFrame *, int);


typedef int(*PyDict_WatchCallback)(PyDict_WatchEvent event, PyObject* dict, PyObject* key, PyObject* new_value);
typedef enum {None} PyFunction_WatchEvent;
typedef int (*PyFunction_WatchCallback)(
    PyFunction_WatchEvent event,
    PyFunctionObject *func,
    PyObject *new_value);
typedef int(*PyType_WatchCallback)(PyTypeObject *);
typedef enum PyCodeEvent {
  PY_CODE_EVENT_CREATE,
  PY_CODE_EVENT_DESTROY
} PyCodeEvent;
typedef int (*PyCode_WatchCallback)(
    PyCodeEvent event,
    PyCodeObject* co);

typedef struct PyMemberDef PyMemberDef;

#endif // PYPY_CASES_GENERATOR_BEFORE_H
