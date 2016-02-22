import ply.yacc as yacc
from decaflexer import tokens

# Set arithmetic precedence
'''
precedence = (
	('left', 'OR'),
	('left', 'AND'),
	('left', 'EQUALS'),
	('left', 'NOTEQUALS'),
	('left', 'LT', 'GT', 'LE', 'GE'),
	('left', 'PLUS', 'MINUS'),
	('left', 'TIMES', 'DIVIDE'),
	('left', 'NOT')
)
'''

precedence = (
	('left', 'PLUS', 'MINUS'),
	('left', 'TIMES', 'DIVIDE'),
	#('left', 'UMINUS'),
)

'''
GRAMMER RULE FOR ARITHMETIC EXPRESSION
expression : expression + term
           | expression - term
           | term

term       : term * factor
           | term / factor
           | factor

factor     : NUMBER
           | ( expression )
'''
'''
def p_expression_uminus(p):
	'expression : MINUS expression UMINUS'
	p[0] = -p[2]
'''
def p_arithmetic_op(p):
	'''expression 	: expression PLUS term
					| expression MINUS term
		term 		: term TIMES factor
					| term DIVIDE factor'''
	if p[2] == '+' : p[0] = p[1] + p[3]
	elif p[2] == '-' : p[0] = p[1] - p[3]
	elif p[2] == '*' : p[0] = p[1] * p[3]
	elif p[2] == '/' : p[0] = p[1] / p[3]

def p_expression_term(p):
	'expression : term'
	p[0] = p[1]

def p_term_factor(p):
	'term : factor'
	p[0] = p[1]

def p_factor_num(p):
	'factor : NUMBER'
	p[0] = p[1]

def p_factor_expr(p):
	'factor : LPAREN expression RPAREN'
	p[0] = p[2]
'''
def p_empty(p):
	'empty :'
	pass
'''
def p_error(p):
	print ("Syntax error at '%s'" % p.value)

yacc.yacc(method="LALR")
