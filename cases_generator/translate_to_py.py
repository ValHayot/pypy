import argparse
import os
import re
from textwrap import dedent

from pycparser import parse_file
from pycparser.c_generator import CGenerator

from cases_generator.py_generator import PyGenerator

DEFAULT_INPUT = os.path.relpath(
    os.path.join(os.path.dirname(__file__), "generated_cases.h")
)
DEFAULT_OUTPUT = os.path.relpath(
    os.path.join(os.path.dirname(__file__), "../interpreter.py")
)


def translate_to_py(filename, output_filename):
    """Simply use the c_generator module to emit a parsed AST."""
    ast = parse_file(filename, use_cpp=True, cpp_path="clang", cpp_args=["-E"])
    generator = PyGenerator()
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
        o.write(generator.visit(ast).replace("->", "."))


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
