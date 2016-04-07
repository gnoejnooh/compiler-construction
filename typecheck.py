import ast

def eval_IfStmt(condition, thenpart, elsepart, line):
	eval_Boolean(condition, line)
	if (thenpart != None) and (not isinstance(thenpart, ast.SkipStmt)):
		ttype = str(thenpart.type)
		if ttype == 'error':
			return 'error'
	if (elsepart != None) and (not isinstance(elsepart, ast.SkipStmt)):
		etype = str(elsepart.type)
		if etype == 'error':
			return 'error'
	return 'correct'

def eval_WhileStmt(cond, body, line):
	eval_Boolean(cond, line)
	if (body != None) and (not isinstance(body, ast.SkipStmt)):
		btype = str(body.type)
		if btype == 'error':
			return 'error'
	return 'correct'

def eval_ForStmt(init, cond, update, body, line):
	if (init != None) and (not isinstance(init, ast.SkipStmt)):
		itype = str(init.type)
		if itype == 'error':
			return 'error'
	eval_Boolean(cond, line)
	if (update != None) and (not isinstance(update, ast.SkipStmt)):
		utype = str(update.type)
		if itype == 'error':
			return 'error'
	if (body != None) and (not isinstance(body, ast.SkipStmt)):
		utype = str(update.type)
		if itype == 'error':
			return 'error'
	return 'correct'

def eval_ReturnStmt(expr, return_type, line):
	rtype = str(expr.type)
	if return_type == 'void':
		print "%d: incompatible types: unexpected return value" % line
		return 'error'
	elif rtype != return_type:
		print "%d: incompatible types: unexpected return value" % line
		return 'error'
	return 'correct'

def eval_Expr(expr, line):
	etype = str(expr.type)
	if(etype == 'error'):
		return 'error'
	return 'correct'

def eval_BlockStmt(stmtlist, line):
	for stmt in stmtlist:
		if (stmt != None) and (not isinstance(stmt, ast.SkipStmt)):
			stype = str(stmt.type)
			if(stype == 'error'):
				return 'error'
	return 'correct'

def eval_Boolean(expr, line):
	# If binary instance, check boolean operation.
	if isinstance(expr, ast.BinaryExpr) is True:
		ctype = str(expr.bop)
		if ctype == 'add' or ctype == 'sub' or ctype == 'mul' or ctype == 'div':
			print "%d: incompatible types: should have type boolean" % line
			return 'error'
		return 'boolean'
	# If expression is variable, compare variable type.
	elif isinstance(expr, ast.VarExpr) is True or isinstance(expr, ast.FieldAccessExpr) is True:
		ctype = str(expr.type)
		if(ctype != 'boolean'):
			print "%d: incompatible types: should have type boolean" % line
			return 'error'
		return ctype
	else:
		print "%d: incompatible types: should have type boolean" % line
		return 'error'

def eval_number(expr, line):
	if isinstance(expr, ast.ConstantExpr) is True:
		ctype = str(expr.type)
		if ctype != 'int' and ctype != 'float':
			print "%d: incompatible types: constant is not a number" % line
			return 'error'
		return ctype
	elif isinstance(expr, ast.VarExpr) is True or isinstance(expr, ast.FieldAccessExpr) is True:
		ctype = str(expr.type)
		if ctype is not 'int' and ctype is not 'float':
			print "%d: incompatible types: variable is not a number" % line
			return 'error'
		return ctype
	else:
		print "%d: incompatible types: expression is not a number" % line
		return 'error'

def eval_UnaryExpr(uop, expr, line):
    if uop == 'uminus':
        return eval_number(expr, line)
    elif uop == 'neg':
        return eval_Boolean(expr, line)

def eval_BinaryExpr(bop, arg1, arg2, line):
	if bop == 'add' or bop == 'sub' or bop == 'mul' or bop == 'div':
		btype1 = eval_number(arg1, line)
		btype2 = eval_number(arg2, line)
		if btype1 == 'float' or btype2 == 'float':
			return 'float'
		return btype1
	elif bop == 'and' or bop == 'or':
		btype1 = eval_Boolean(arg1, line)
		btype2 = eval_Boolean(arg2, line)
		if btype1 != btype2:
			print "%d: incompatible types: should have type boolean" % line
			return 'error'
		return btype1
	elif bop == 'lt' or bop == 'leq' or bop == 'gt' or bop == 'geq':
		btype1 = eval_number(arg1, line)
		btype2 = eval_number(arg2, line)
		if (btype1 == 'int' and btype2 == 'float') or (btype1 == 'float' and btype2 == 'int'):
			return 'boolean'
		if btype1 != btype2:
			print "%d: incompatible types: should have type boolean" % line
			return 'error'
		return 'boolean'
	elif bop == 'eq' or bop == 'neq':
		if isinstance(arg1, ast.ConstantExpr) and isinstance(arg2, ast.ConstantExpr):
			btype1 = str(arg1.type)
			btype2 = str(arg2.type)
			if((btype1 == 'int' and btype2 == 'float') or (btype1 == 'float' and btype2 == 'int')):
				return 'float';
			if(btype1 == btype2):
				return btype1;
			else:
				print "%d: incompatible types: cannot compare objects of different types" % line
				return 'error'
	return 'error'

def eval_AssignExpr(lhs, rhs, line):
	ltype = str(lhs.type)
	rtype = str(rhs.type)
	if ltype == 'error' or rtype == 'error':
		return 'error'
	if ltype == 'float' and rtype == 'int':
		return 'correct'
	if ltype != rtype:
		print "%d: incompatible types: cannot assign %s to %s" % (line, rtype, ltype)
		return 'error'
	return 'correct'

def eval_AutoExpr(arg, line):
	if isinstance(arg, ast.VarExpr) is True or isinstance(arg, ast.FieldAccessExpr) is True:
		ctype = str(arg.type)
		if ctype is not 'int' and ctype is not 'float':
			print "%d: incompatible types: argument is not a number" % line
			return 'error'
		return ctype
	else:
		print "%d: incompatible types: argument is not a number" % line
		return 'error'