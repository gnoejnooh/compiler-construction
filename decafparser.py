import ply.yacc as yacc
from decaflexer import tokens

# Set arithmetic precedence
precedence = (
	('left', 'EQUALS'),
	('left', 'OR'),
	('left', 'AND'),
	('left', 'EE','NE'),
	('left', 'GT','LT','GE','LE'),
	('left', 'PLUS', 'MINUS'),
	('left', 'TIMES', 'DIVIDE'),
	('left', 'NOT'),
)

#--------------------------------A DECAF PROGRAM------------------------------------#
#prgram : class_decl*
def p_program(p):
	'''program : class_decl program
			   | class_decl '''
	p[0] = p[1]


#--------------------------------CLASS DECLARATIONS---------------------------------#
#class_decl : class id (extends id)? {class_body_decl+}
def p_class_decl(p):
	'''class_decl 		: CLASS ID LPAREN EXTENDS ID RPAREN LBRACE class_body_decl RBRACE
						| CLASS ID LBRACE class_body_decl RBRACE'''
	if len(p) == 10:
		p[0] = (p[1],p[2],p[3],p[4],p[5],p[6],p[7],p[8],p[9])
	else:
		p[0] = (p[1],p[2],p[3],p[4],p[5])

#class_body_decl : field_decl
#				 | method_decl
#			 	 | constructor_decl
def p_class_body_decl(p):
	'''class_body_decl	: field_decl
						| method_decl
						| constructor_decl
						| class_body_decl class_body_decl'''
	if len(p) == 3:
		p[0] = (p[1],p[2])
	else:
		p[0] = p[1]


#--------------------------------------FIELDS----------------------------------------#
#field_decl : modifier var_decl
def p_field_decl(p):
	'''field_decl		: modifier var_decl'''
	p[0] = (p[1],p[2])

#modifier : (public | private)?(static)?
def p_modifier(p):
	'''modifier			: PUBLIC STATIC
						| PRIVATE STATIC
						| PUBLIC
						| PRIVATE
						| STATIC'''
	if len(p) == 3:
		p[0] = (p[1],p[2])
	else:
		p[0] = p[1]
#var_decl : type variable ;
def p_var_decl(p):
	'''var_decl			: type variables'''
	p[0] = (p[1],p[2])
def p_type(p):
	'''type				: INT
						| FLOAT
						| BOOLEAN
						| ID'''
	p[0] = p[1]
#variables : variable(, variable)*
def p_variables(p):
	'''variables		: variable
						| variables COMMA variable'''
	if len(p) == 4:
		p[0] = (p[1],p[2],p[3])
	else:
		p[0] = p[1]
#variable : id
def p_variable(p):
	'''variable			: ID'''
	p[0] = p[1]


#-------------------------------METHODS AND CONSTRUCTORS---------------------------#
#method_decl : modifier (type | void) id (formals?) block
def p_method_decl(p):
	'''method_decl		: modifier type ID LPAREN formals RPAREN block
						| modifier type ID LPAREN RPAREN block
						| modifier VOID ID LPAREN formals RPAREN block
						| modifier VOID ID LPAREN RPAREN block'''
	if len(p) == 8:
		p[0] = (p[1],p[2],p[3],p[4],p[5],p[6],p[7])
	else:
		p[0] = (p[1],p[2],p[3],p[4],p[5],p[6])
#constructor_decl : modifier id (formals?) block
def p_constructor_decl(p):
	'''constructor_decl	: modifier ID LPAREN formals RPAREN block
						| modifier ID LPAREN RPAREN block'''
	if len(p) == 7:
		p[0] = (p[1],p[2],p[3],p[4],p[5],p[6])
	else:
		p[0] = (p[1],p[2],p[3],p[4],p[5])
#formals : formal_param (, formal_param)*
def p_formals(p):
	'''formals			: formal_param
						| formals COMMA formal_param'''
	if len(p) == 4:
		p[0] = (p[1],p[2],p[3])
	else:
		p[0] = p[1]
#formal_param : type variable
def p_formal_param(p):
	'''formal_param		: type variable'''
	p[0] = (p[1],p[2])


### INHERITANCE - DO WE CHECK FOR SAME CLASS NAME? NO CLUE...

#------------------------------------STATEMENTS-------------------------------------#
#stmt : if (expr) stmt (else stmt)?
#		 | while (expr) stmt
#		 | for (stmt_expr? ; expr? ; stmt_expr?) stmt
#		 | return expr? ;
#		 | stmt_expr ;
#		 | break ;
#		 | continue ;
#		 | block
#		 | var_decl
#		 | ; 
def p_stmt(p):
	'''stmt	 		: IF LPAREN expr RPAREN stmt ELSE stmt
					| IF LPAREN expr RPAREN stmt
					| WHILE LPAREN expr RPAREN stmt
					| FOR LPAREN stmt_expr SEMI expr SEMI stmt_expr RPAREN stmt
					| RETURN expr SEMI
					| stmt_expr SEMI
					| BREAK SEMI
					| CONTINUE SEMI
					| block
					| var_decl
					| SEMI 
					| empty '''
	if len(p) == 10:
		p[0] = (p[1],p[2],p[3],p[4],p[5],p[6],p[7],p[8],p[9])
	elif len(p) ==8:
		p[0] = (p[1],p[2],p[3],p[4],p[5],p[6],p[7])
	elif len(p) == 6:
		p[0] = (p[1],p[2],p[3],p[4],p[5])
	elif len(p) == 4:
		p[0] = (p[1],p[2],p[3])
	elif len(p) == 3:
		p[0] = (p[1],p[2])
	else:
		p[0] = p[1]

#block : { stmt* }
def p_block(p):
	'block : LBRACE stmt_star RBRACE'
	if len(p) == 4:
		p[0] = (p[1],p[2],p[3])
	else:
		p[0] = p[1]

#stmtstar : stmt*
def p_stmt_star(p):
	'''stmt_star : stmt stmt_star
				 | stmt '''
	p[0] = p[1]

#----------------------------------EXPRESSIONS-------------------------------------#
# expr : primary
#      | assign
#	   | expr arith_op expr
#	   | expr bool_op expr
#	   | unary_op expr
def p_expr(p):
	'''expr 		: primary
					| assign
					| expr arith_op expr
					| expr bool_op expr
					| unary_op expr '''
	if len(p) == 4:
		p[0] = (p[1],p[2],p[3])
	else:
		p[0] = (p[1],None,None)

#stmt_expr : assign
#		   | method_invocation
def p_stmt_expr(p):
	'''stmt_expr : assign
				 | method_invocation
				 | empty'''
	p[0] = p[1]

#primary : literal
#			| this
#			| super
#			| (expr)
#			| new id(arguments?)
#			| lhs
#			| method_invocation
def p_primary(p):
	'''primary : literal
			   | THIS
			   | SUPER
			   | LPAREN expr RPAREN
			   | NEW ID LPAREN arguments RPAREN
			   | NEW ID LPAREN RPAREN
			   | lhs
			   | method_invocation'''
	if len(p) == 6:
		p[0] = (p[1],p[2],p[3],p[4],p[5])
	elif len(p) == 5:
		p[0] = (p[1],p[2],p[3],p[4])
	elif len(p) == 4:
		p[0] = (p[1],p[2],p[3])
	else:
		p[0] = p[1]

#assign : lhs = expr
#		   | lhs ++
#		   | ++ lhs
#		   | lhs --
#		   | -- lhs
def p_assign(p):
	'''assign : lhs EQUALS expr
			  | lhs PLUSPLUS
			  | PLUSPLUS lhs
			  | lhs MINUSMINUS
			  | MINUSMINUS lhs
			  | empty '''
	if len(p) == 4:
		p[0] = (p[1],p[2],p[3])
	elif len(p) == 2: 
		p[0] = (p[1],p[2])
	else:
		p[0] = p[1]

#method_invocation : field_access (arguments?)
def p_method_invocation(p):
	'''method_invocation : field_access LPAREN arguments RPAREN
						 | field_access LPAREN RPAREN'''
	if len(p) == 5:
		p[0] = (p[1],p[2],p[3],p[4])
	else:
		p[0] = (p[1],p[2],p[3])

#arguments : expr (, expr)*
def p_arguments(p):
	'''arguments : expr
				 | arguments COMMA expr'''
	if len(p) == 4:
		p[0] = p[1], p[2], p[3]
	else:
		p[0] = p[1]

#lhs : field_access
def p_lhs(p):
	'lhs : field_access'
	p[0] = p[1]

#field_access : primary . id
#				 | id
def p_field_access(p):
	'''field_access : primary PERIOD ID
				 	| ID'''
	if len(p) == 4:
		p[0] = (p[1],p[2],p[3])
	else:
		p[0] = p[1]

#literal : int_const
#			| float_const
#			| string_const
#			| null
#			| true
#			| false
def p_literal(p):
	'''literal : INT_CONST
			   | FLOAT_CONST
			   | STRING_CONST
			   | NULL
			   | TRUE
			   | FALSE'''
	p[0] = p[1]

### arith_op {+, -, *, /}
def p_arith_op(p):
	'''arith_op : PLUS
				| MINUS
				| TIMES
				| DIVIDE'''
	p[0] = p[1]

### bool_op {&&, ||, ==, !=, <, >, <=, >=}
def p_bool_op(p):
	'''bool_op : AND
			   | OR
			   | EE
			   | NE
			   | LT
			   | GT
			   | LE
			   | GE'''
	p[0] = p[1]

### unary_op {+, -, !}
def p_unary_op(p):
	'''unary_op : PLUS
				| MINUS
				| NOT'''
	p[0] = p[1]

def p_empty(p):
	'empty :'

def p_error(p):
	#print ("Syntax error at '%s,%d'" % p.value, p.lineno)
	raise SyntaxError(p)
yacc.yacc(method="LALR", debug=0)
