from collections import defaultdict


class Node(object):
    pass

class Expression(Node):
    pass

class Statement(Node):
    pass

# Expressions
"""Las expresiones retornan valores cuando se evaluan"""
## Literals
1
1.0
0.1
0b010101
0x10948
0o72347
"hola"
'Mundo'
a = 1
a
## Unary Expressions
-1
~1
not 1
not a
# (SIGNO)EXPRESSION

## Binary Expressions

1 + 2
"Hola" * 4
# EXPRESSION(SIGNO)EXPRESSION

## Parentheses

(1+2)
(1)

# '(' EXPRESSION ')'

# Statements

"""Los statement no retornan valores cuando se evaluan"""

## Assign

# LeftHandSide:[]Expressions (SIGNO) RightHandSide:[]Expressions

a = 1
a, b = 1, 2

## If, Elif, Else

if True:
    if False:
        print("False")
    1 + 2
else:
    4


import ast


code = """
def ej():
    c = 1+1 
class Ejemplo:
    def __init__(self):
        pass
print(1 + 2)
a = 2
"""
code_ast = ast.parse(code)

for node in ast.walk(code_ast):
    if isinstance(node, ast.ClassDef):
        print(node.body)
        for e in node.body:
            print("hola mundo", e)

