import ast

def eval_Boolean(expr, line):
	# If binary instance, check boolean operation.
	if isinstance(expr, ast.BinaryExpr) is True:
		ctype = expr.bop
		if ctype == 'add' or ctype == 'sub' or ctype == 'mul' or ctype == 'div':
			print "%d: incompatible types: should have type boolean" % line
			exit()
		return 'boolean'
	# If expression is variable, compare variable type.
	elif isinstance(expr, ast.VarExpr) is True:
		if(expr.type != 'boolean'):
			print "%d: incompatible types: should have type boolean" % line
		return expr.type
	# If expression is field-access, set undefine.
	elif isinstance(expr, ast.FieldAccessExpr) is True:
		return 'undefined'
	else:
		print "%d: incompatible types: should have type boolean" % line
		exit()

def eval_number(expr, line):
	if isinstance(expr, ast.ConstantExpr) is True:
		ctype = expr.kind
		if ctype != 'int' and ctype != 'float':
			print "%d: incompatible types: expression is not a number" % line
			exit()
		return ctype
	elif isinstance(expr, ast.VarExpr) is True:
		if(expr.type != 'int' and expr.type != 'float'):
			print "%d: incompatible types: expression is not a number" % line
			exit()
		return expr.type
	elif isinstance(expr, astFieldAccessExpr) is True:
		return 'undefined'
	else:
		print "%d: incompatible types: expression is not a number" % line
		exit()