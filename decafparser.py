import ply.yacc as yacc

yacc.yacc()

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