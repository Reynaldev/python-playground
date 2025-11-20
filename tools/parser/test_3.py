# Editing Code and Updating Trees

import tree_sitter_python as tspython

from tree_sitter import Language, Parser

PY_LANGUAGE = Language(tspython.language())

parser = Parser(PY_LANGUAGE)

code = bytes("""
def greet():
    print("Hello!")
""", "utf8")

tree = parser.parse(code)

new_code = code[:5] + b"WELCOME" + code[:10]

tree.edit(
    start_byte=5,
    old_end_byte=10,
    new_end_byte=12,
    start_point=(1, 4),
    old_end_point=(1, 9),
    new_end_point=(1, 11)
)

new_tree = parser.parse(new_code, tree)

for changed_range in tree.changed_ranges(new_tree):
    print(f"Changed range: {changed_range.start_point} to {changed_range.end_point}")

function_name = new_tree.root_node.children[0].child_by_field_name("name")
print(f"New function name: {function_name.text.decode('utf8')}")
