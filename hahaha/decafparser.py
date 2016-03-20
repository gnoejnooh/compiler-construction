from ply import *
import decaflexer


tokens = decaflexer.tokens

precedence = (
    ('left', 'PLUS','MINUS'),
    ('left', 'TIMES','DIVIDE'),
)
    

def p_name(p):
	if p[0] == 'a' : print p.value
# Arithmetic operation
def p_expression_arithmetic(p):
	if p[2] == '+' : p[0] = p[1] + p[3]
	elif p[2] == '-' : p[0] = p[1] - p[3]
	elif p[2] == '*' : p[0] = p[1] * p[3]
	elif p[2] == '/' : p[0] = p[1] / p[3]

def p_empty(p):
	'empty :'
	pass
	
# Error case - syntax error
def p_error(p):
	print p.value

	raise SyntaxError("Invalid syntax")
	
# Build the parser
parser = yacc.yacc()
