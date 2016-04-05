import ast

dic = {}

def eval_IfStmt(condition, thenpart, elsepart, line):
	if isinstance(condition, ast.BinaryExpr) is not True:
		print "If condition is not boolean %d" % line
		exit()