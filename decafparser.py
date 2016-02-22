import ply.yacc as yacc



# Set arithmetic precedence
precedence = {
	('left', 'OR'),
	('left', 'AND'),
	('left', 'EQUALS'),
	('left', 'NOTEQUALS'),
	('left', 'LT', 'GT', 'LTE', 'GTE'),
	('left', 'PLUS', 'MINUS'),
	('left', 'TIMES', 'DIVIDE'),
	('left', 'NOT')
}

# Arithmeti operation
def p_expression_arithmetic(t):
	if t[2] == '+' : t[0] = t[1] + t[3]
	elif t[2] == '-' : t[0] = t[1] - t[3]
	elif t[2] == '*' : t[0] = t[1] * t[3]
	elif t[2] == '/' : t[0] = t[1] / t[3]

# Error case - syntax error
def p_error(t):
	raise SyntaxError("Invalid syntax")

# Build the parser
yacc.yacc()