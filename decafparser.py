import ply.yacc as yacc
from decaflexer import tokens

# Set arithmetic precedence
precedence = (
	('left', 'PLUS', 'MINUS'),
	('left', 'TIMES', 'DIVIDE'),
	#('left', 'UMINUS'),
)

### A DECAF PROGRAM IS A SEQUENCE OF CLASS DECLARATIONS.
''' prgram : class_decl* '''

### CLASS DECLARATIONS
''' class_decl : class id (extends id)? {class_body_decl+}
	class_body_decl : field_decl
					| method_decl
					| constructor_decl '''

### FIELDS (NO ARRAY FOR VARIABLE)
''' field_decl : modifier var_decl
	modifier : (public | private)?(static)?
	var_decl : type variable ;
	type : int
		 | float
		 | boolean
		 | id
	variables : variable(, variable)*
	variable : id '''

### INHERITANCE - DO WE CHECK FOR SAME CLASS NAME? NO CLUE...

### METHODS AND CONSTRUCTORS
''' method_decl : modifier (type | void) id (formals?) block
	constructor_decl : modifier id (formals?) block
	formals : formal_param (, formal_param)*
	formal_param : type variable '''

### STATEMENTS
''' block : { stmt* }
	stmt : if (expr) stmt (else stmt)?
		 | while (expr) stmt
		 | for (stmt_expr? ; expr? ; stmt_expr?) stmt
		 | return expr? ;
		 | stmt_expr ;
		 | break ;
		 | continue ;
		 | block
		 | var_decl
		 | ; '''

### EXPRESSIONS
''' literal : int_const
			| float_const
			| string_const
			| null
			| true
			| false
	
	primary : literal
			| this
			| super
			| (expr)
			| new id(arguments?)
			| lhs
			| method_invocation
	
	arguments : expr (, expr)*
	
	lhs : field_access
	
	field_access : primary . id
				 | id
	
	method_invocation : field_access (arguments?)

	assign : lhs = expr
		   | lhs ++
		   | ++ lhs
		   | lhs --
		   | -- lhs

	stmt_expr : assign
			  | method_invocation '''
### expr : primary
# 		 | assign
#		 | expr arith_op expr
#		 | expr bool_op expr
#		 | unary_op expr
def p_expr(p):
	'''expr 		: primary
					| assign
					| expr arith_op expr
					| expr bool_op expr
					| unary_op expr'''
	if len(p) == 4:
		p[0] = (p[1],p[2],p[3])
	else:
		p[0] = (p[1],None,None)

def p_primary(p):
	'''primary : literal
			   | LPAREN expr RPAREN
			   | lhs'''
	if len(p) == 4:
		p[0] = (p[1],p[2],p[3])
	else:
		p[0] = p[1]

def p_assign(p):
	'''assign : lhs EQUALS expr
			  | lhs PLUSPLUS
			  | PLUSPLUS lhs
			  | lhs MINUSMINUS
			  | MINUSMINUS lhs'''
	if len(p) == 4:
		p[0] = (p[1],p[2],p[3])
	else:
		p[0] = (p[1],p[2])

def p_lhs(p):
	'lhs : field_access'
	p[0] = p[1]

def p_field_access(p):
	'''field_access : primary PERIOD ID
				 	| ID'''
	if len(p) == 4:
		p[0] = (p[1],p[2],p[3])
	else:
		p[0] = p[1]

def p_literal(p):
	'literal : NUMBER'
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

def p_error(p):
	print ("Syntax error at '%s'" % p.value)

yacc.yacc(method="LALR", debug=0)
