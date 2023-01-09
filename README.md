# PyPy

Early days of a symbolic Python bytecode interpreter implemented in Python (using [CPython's interpreter DSL](https://github.com/faster-cpython/ideas/blob/main/3.12/interpreter_definition.md)).

# Interpreter

Current version lives at [interpreter.py](interpreter%2Finterpreter.py) and looks like this

```python
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
    entry_frame: _PyInterpreterFrame
    
    ...


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
        
    ...

```

# Building

Run [generate_cases.py](./interpreter_generator/generate_cases.py) to generate `generated_cases.c` and `generated_cases.h` (i.e., CPython artifacts).
Then run [translate_to_py.py](interpreter_generator%2Ftranslate_to_py.py) to (re)generate the python implementation.