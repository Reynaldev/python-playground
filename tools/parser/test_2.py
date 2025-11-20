# Navigating the Syntax Tree

import tree_sitter_python as tspython

from tree_sitter import Language, Parser

PY_LANGUAGE = Language(tspython.language())

parser = Parser(PY_LANGUAGE)

code = """
def greet():
    print("Hello, TreeSitter!")
"""

tree = parser.parse(bytes(code, "utf8"))

cursor = tree.walk()
print(f"Starting node: {cursor.node.type}")

cursor.goto_first_child()
print(f"First child: {cursor.node.type}")

cursor.goto_first_child()
cursor.goto_next_sibling()
print(f"Function name: {cursor.node.text.decode('utf8')}")

cursor.goto_parent()
print(f"Back to: {cursor.node.type}")
