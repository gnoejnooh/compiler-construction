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

	expr : primary
		 | assign
		 | expr arith_op expr
		 | expr bool_op expr
		 | unary_op expr

	assign : lhs = expr
		   | lhs ++
		   | ++ lhs
		   | lhs --
		   | -- lhs

	TOKEN arith_op {+, -, *, /}
	TOKEN bool_op {&&, ||, ==, !=, <, >, <=, >=}
	TOKEN unary_op {+, -, !}

	stmt_expr : assign
			  | method_invocation '''

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
