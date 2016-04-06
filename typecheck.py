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
			exit()
		return expr.type
	# If expression is field-access, set undefine.
	elif isinstance(expr, ast.FieldAccessExpr) is True:
		#print ast.lookup(ast.classtable, expr.fname)
		return 'undefined'
	else:
		print "%d: incompatible types: should have type boolean" % line
		exit()

def eval_number(expr, line):
	if isinstance(expr, ast.ConstantExpr) is True:
		ctype = expr.type
		if ctype != 'int' and ctype != 'float':
			print "%d: incompatible types: constant is not a number" % line
			exit()
		return ctype
	elif isinstance(expr, ast.VarExpr) is True:
		ctype = expr.type
		print ctype
		if ctype is not 'int' and ctype is not 'float':
			print "%d: incompatible types: variable is not a number" % line
			exit()
		return expr.type
	elif isinstance(expr, astFieldAccessExpr) is True:
		return 'undefined'
	else:
		print "%d: incompatible types: expression is not a number" % line
		exit()
'''
def eval_BinaryExpr(bop, arg1, arg2, line):
	if bop == 'add' or bop == 'sub' or bop == 'mul' or bop == 'div':
		eval_number(arg1, line)
		eval_number(arg2, line)
	elif bop == 'and' or bop == 'or':
		eval_Boolean(arg1, line)
		eval_Boolean(arg2, line)
	elif bop == 'lt' or bop == 'leq' or bop == 'gt' or bop == 'geq':
		a = eval_number(arg1, line)
		b = eval_number(arg2, line)
	elif bop == 'eq' or bop == 'neq':
		print arg1
		print arg2
		if isinstance(arg1, ast.ConstantExpr) and isinstance(arg2, ast.ConstantExpr):
			if((arg1.kind == 'int' and arg2.kind == 'float') or (arg1.kind == 'float' and arg2.kind == 'int')):
				return;
			if(arg1.kind == arg2.kind):
				return;
			else:
				print "%d: incompatible types: cannot compare objects of different types" % line
'''
