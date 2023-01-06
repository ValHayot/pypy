import argparse
import ast
import os
import re
from textwrap import dedent

from pycparser import parse_file, preprocess_file, CParser
from pycparser.c_generator import CGenerator

from cases_generator.c.ast_generalizer import CAstGeneralizerBackend
from cases_generator.generate_cases import main
from cases_generator.py_generator import PyGenerator

DEFAULT_INPUT = os.path.relpath(
    os.path.join(os.path.dirname(__file__), "generated_cases.c")
)
DEFAULT_OUTPUT = os.path.relpath(
    os.path.join(os.path.dirname(__file__), "../interpreter.py")
)


def translate_to_py(filename, output_filename):
    """Simply use the c_generator module to emit a parsed AST."""
    c_preproc_args = [
        "-E",  # only run the preprocessor
        "-I/usr/include/python3.10",
        "-I/home/mlevental/dev_projects/cpython/Include/internal",
        "-DPy_BUILD_CORE",
        "-DPy_HAVE_CONDVAR",
        "-D_Py_NO_RETURN=",
        "-Wno-everything",
    ]
    print(f"clang {' '.join(c_preproc_args + [filename])}")
    text = preprocess_file(filename, "clang", c_preproc_args)
    parser = CParser()
    # text = re.sub(
    #     r"__attribute__ \((?:[^)(]|\((?:[^)(]|\((?:[^)(]|\([^)(]*\))*\))*\))*\)",
    #     "",
    #     text,
    # )
    text = re.sub(r"__asm__ \(.*?\)", "", text)
    # typedef __int8_t __int_least8_t;
    # typedef __uint8_t __uint_least8_t;
    # typedef __int16_t __int_least16_t;
    # typedef __uint16_t __uint_least16_t;
    # typedef __int32_t __int_least32_t;
    # typedef __uint32_t __uint_least32_t;
    # typedef __int64_t __int_least64_t;
    # typedef __uint64_t __uint_least64_t;
    for sig in ["", "u"]:
        for size in [8, 16, 32, 64, "max"]:
            text = re.sub(
                rf"typedef __{sig}int{size}_t (.*);", r"typedef int \1;", text
            )
    # text = re.sub(r"typedef __uint.*;", "", text)
    text = (
        text.replace("__gnuc_va_list", "float1")
        .replace("__builtin_va_list", "float")
        .replace("__restrict", "")
        .replace("__extension__", "")
    )
    text = (
        text.replace("__inline", "")
        .replace("__signed__", "")
        .replace("_Py_NO_RETURN", "")
    )
    text = (
        text.replace("((_PyCFunctionFast)(void(*)(void))cfunc)", "cfunc")
        .replace("(_PyCFunctionFastWithKeywords)(void(*)(void))", "")
        .replace("(_PyCFunctionFast)(void(*)(void))meth", "meth")
        .replace("PyObject *(*conv_fn)(PyObject *);", "")
    )
    # text = text.replace("__uint16_t", "int").replace("unsigned short int", "short")
    with open("out.c", "w") as f:
        f.write(text)
    tree = parser.parse(text, filename)
    generator = CAstGeneralizerBackend()
    with open(output_filename, "w") as o:
        o.write(
            dedent(
                """\
        from typing import Any
        from pytype.pyc import opcodes as ops
        
        """
            )
        )
        # ^(?:[\t ]*(?:\r?\n|\r))+ after wards
        mod = generator.visit(tree)
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
    main()
    translate_to_py(args.input, args.output)
