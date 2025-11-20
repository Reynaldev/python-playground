# Parsing Code Snippet

import tree_sitter_python as tspython

from tree_sitter import Language, Parser

PY_LANGUAGE = Language(tspython.language())

parser = Parser(PY_LANGUAGE)

code = """
def greet():
    print("Hello, TreeSitter!")
"""

tree = parser.parse(bytes(code, "utf8"))

root_node = tree.root_node

# Inspect root node
print(f"Root node type: {root_node.type}")
print(f"Root node text: {root_node.text.decode('utf8')}")
print(f"Root node start point: {root_node.start_point}")
print(f"Root node end point: {root_node.end_point}")

# Inspect nodes
function_node = root_node.children[0]
print(f"First child type: {function_node.type}")

name_node = function_node.child_by_field_name("name")
print(f"Function name: {name_node.text.decode('utf8')}")

body_node = function_node.child_by_field_name("body")
print(f"Body type: {body_node.type}")

call_node = body_node.children[0].children[0]
print(f"Call function: {call_node.child_by_field_name('function').text.decode('utf8')}")
