# Pattern Matching with Queries

import tree_sitter_python as tspython

from tree_sitter import Language, Parser, Query, QueryCursor

PY_LANGUAGE = Language(tspython.language())

parser = Parser(PY_LANGUAGE)

code = bytes("""
def greet():
    print("Hello!")
""", "utf8")

tree = parser.parse(code)

query = Query(
    PY_LANGUAGE, 
    """
(function_definition
    name: (identifier) @function.def
    body: (block) @function.block)

(call
    function: (identifier) @function.call
    arguments: (argument_list) @function.args)
""")

query_cursor = QueryCursor(query)
captures =  query_cursor.captures(tree.root_node)
for name, nodes in captures.items():
    for node in nodes:
        print(f"Capture {name}: {node.text.decode('utf8')}")
