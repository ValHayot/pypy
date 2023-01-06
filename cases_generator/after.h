//
// Created by mlevental on 1/5/23.
//
//#include "pycore_frame.h"         // _PyInterpreterFrame

#ifndef PYPY_CASES_GENERATOR_AFTER_H
#define PYPY_CASES_GENERATOR_AFTER_H

typedef struct _PyCFrame {
  /* This struct will be threaded through the C stack
     * allowing fast access to per-thread state that needs
     * to be accessed quickly by the interpreter, but can
     * be modified outside of the interpreter.
     *
     * WARNING: This makes data on the C stack accessible from
     * heap objects. Care must be taken to maintain stack
     * discipline and make sure that instances of this struct cannot
     * accessed outside of their lifetime.
   */
  uint8_t use_tracing;  // 0 or 255 (or'ed into opcode, hence 8-bit type)
  /* Pointer to the currently executing frame (it can be NULL) */
  struct _PyInterpreterFrame *current_frame;
  struct _PyCFrame *previous;
} _PyCFrame;

#define _Py_atomic_load_relaxed_int32(ATOMIC_VAL) _Py_atomic_load_relaxed(ATOMIC_VAL)

static int do_raise(PyThreadState *tstate, PyObject *exc, PyObject *cause);
static int exception_group_match(
    PyObject* exc_value, PyObject *match_type,
    PyObject **match, PyObject **rest);

static inline void _Py_LeaveRecursiveCallPy(PyThreadState *tstate);


static void
format_awaitable_error(PyThreadState *tstate, PyTypeObject *type, int oparg);


#define _Py_RVALUE(EXPR) ((void)0, (EXPR))
#define _PyCode_CODE(CO) _PyCode_CODE(CO)
#define Py_ABS(x) Py_ABS(x)

PyObject *
_PyDict_GetItemWithError(PyObject *dp, PyObject *kv);

static void format_exc_check_arg(PyThreadState *, PyObject *, const char *, PyObject *);

static int unpack_iterable(PyThreadState *, PyObject *, int, int, PyObject **);

static void
format_exc_unbound(PyThreadState *tstate, PyCodeObject *co, int oparg);

static void format_kwargs_error(PyThreadState *, PyObject *func, PyObject *kwargs);

#define Py_TPFLAGS_MANAGED_DICT (1 << 4)

typedef struct _dictvalues PyDictValues;

typedef enum {
  PyDict_EVENT_ADDED,
  PyDict_EVENT_MODIFIED,
  PyDict_EVENT_DELETED,
  PyDict_EVENT_CLONED,
  PyDict_EVENT_CLEARED,
  PyDict_EVENT_DEALLOCATED,
} PyDict_WatchEvent;

int
_PyUnicode_Equal(PyObject *str1, PyObject *str2);

static int check_except_star_type_valid(PyThreadState *tstate, PyObject* right);

static int
check_except_type_valid(PyThreadState *tstate, PyObject* right);

static PyObject * import_from(PyThreadState *, PyObject *, PyObject *);
static int import_all_from(PyThreadState *, PyObject *, PyObject *);

static PyObject*
match_class(PyThreadState *tstate, PyObject *subject, PyObject *type,
            Py_ssize_t nargs, PyObject *kwargs);

static PyObject*
match_keys(PyThreadState *tstate, PyObject *map, PyObject *keys);

#define is_method(stack_pointer, args) (PEEK((args)+2) != NULL)


static PyObject *
trace_call_function(PyThreadState *tstate,
                    PyObject *func,
                    PyObject **args, Py_ssize_t nargs,
                    PyObject *kwnames);

static int
check_args_iterable(PyThreadState *tstate, PyObject *func, PyObject *args);

static PyObject * do_call_core(
    PyThreadState *tstate, PyObject *func,
    PyObject *callargs, PyObject *kwdict, int use_tracing);

PyObject *
_PySys_GetAttr(PyThreadState *tstate, PyObject *name);

typedef int(*PyDict_WatchCallback)(PyDict_WatchEvent event, PyObject* dict, PyObject* key, PyObject* new_value);

typedef PyObject* (*_PyFrameEvalFunction)(PyThreadState *tstate, struct _PyInterpreterFrame *, int);

typedef struct _PyInterpreterFrame {
  /* "Specials" section */
  PyObject *f_funcobj; /* Strong reference. Only valid if not on C stack */
  PyObject *f_globals; /* Borrowed reference. Only valid if not on C stack */
  PyObject *f_builtins; /* Borrowed reference. Only valid if not on C stack */
  PyObject *f_locals; /* Strong reference, may be NULL. Only valid if not on C stack */
  PyCodeObject *f_code; /* Strong reference */
  PyFrameObject *frame_obj; /* Strong reference, may be NULL. Only valid if not on C stack */
  /* Linkage section */
  struct _PyInterpreterFrame *previous;
  // NOTE: This is not necessarily the last instruction started in the given
  // frame. Rather, it is the code unit *prior to* the *next* instruction. For
  // example, it may be an inline CACHE entry, an instruction we just jumped
  // over, or (in the case of a newly-created frame) a totally invalid value:
  _Py_CODEUNIT *prev_instr;
  int stacktop;  /* Offset of TOS from localsplus  */
  uint16_t yield_offset;
  char owner;
  /* Locals and stack */
  PyObject *localsplus[1];
} _PyInterpreterFrame;

static void
_PyEvalFrameClearAndPop(PyThreadState *tstate, _PyInterpreterFrame * frame);

static void call_exc_trace(Py_tracefunc, PyObject *,
                           PyThreadState *, _PyInterpreterFrame *);
static PyObject * import_name(PyThreadState *, _PyInterpreterFrame *,
                              PyObject *, PyObject *, PyObject *);
static _PyInterpreterFrame *
_PyEvalFramePushAndInit(PyThreadState *tstate, PyFunctionObject *func,
                        PyObject *locals, PyObject* const* args,
                        size_t argcount, PyObject *kwnames);

#define assert assert
#define Py_CLEAR(op) Py_CLEAR(op)
#define Py_XSETREF(op, op2) Py_XSETREF(op, op2)
#define PyCFunction_GET_SELF(func) PyCFunction_GET_SELF(func)
#define Py_SETREF(op, op2) Py_SETREF(op, op2)
#define Py_ARRAY_LENGTH(array) Py_ARRAY_LENGTH(array)
#define Py_UNREACHABLE() Py_UNREACHABLE()
#define Py_XDECREF(op) Py_XDECREF(op)
#define PyExceptionInstance_Check(x) PyExceptionInstance_Check(x)
#define PyExceptionInstance_Class(x) PyExceptionClass_Check(x)
#define PyLong_Check(op) PyLong_Check(op)

#endif // PYPY_CASES_GENERATOR_AFTER_H
