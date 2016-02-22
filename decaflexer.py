import ply.lex as lex

'''
lex INFORMATION
+ t.type is the token type.
+ t.value is the lexeme.
+ By default, t.type isset to the name following the t_prefix.
+ t_ignore rule is reserved by lex.py for ignoring the input stream.
+ t_error() function is used to handle lexing errors.
+ When implementing "=" and "==", make sure that "==" is checked first.
+ The lexer requires tokens to be defined as class instances
  with t.type, t.value, and t.lineno attributes.
+ yacc.py module only provides public access to the t.value attribute.
'''

# Reserved words
'''
keywords = (
	'BOOLEAN', 'BREAK', 'CONTINUE', 'CLASS', 'DO', 'ELSE',
	'EXTENDS', 'FALSE', 'FLOAT', 'FOR', 'IF', 'INT',
	'NEW', 'NULL', 'PRIVATE', 'PUBLIC', 'RETURN', 'STATIC',
	'SUPER', 'THIS', 'TRUE', 'VOID', 'WHILE',
)
'''

'''
reserved_words = {}
for reserved in reserved_words:
	reserved_map[reserved.lower()] = reserved
'''
# Tokens recognized by the lexer
'''
tokens = (
	# Identifiers
	'ID',
	# Constants
	'INT_CONST', 'FLOAT_CONST', 'STRING_CONST',
	# Arithmetic Operations
	'PLUS', 'MINUS', 'TIMES', 'DIVIDE',
	# Boolean Operations
	'AND', 'OR', 'EQUALS', 'NOTEQUALS',
	'LT', 'GT', 'LE', 'GE', 'NOT',
	# Increment & Decrement
	'PLUSPLUS', 'MINUSMINUS',
	# Conditional statement
	'CONDOP',
	# Delimeters
	'LPAREN', 'RPAREN',
	'LBRACKET', 'RBRACKET',
	'LBRACE', 'RBRACE',
	'COMMA', 'PERIOD',
	'SEMI', 'COLON',
)
'''

'''
identifier = r'[a-zA-Z_][0-9a-zA-Z_]*'
integer_const = r'[1-9][0-9]*'
float_const = r'[0-9]*.[0-9]+'
#string_const = ?
'''
tokens = (
	'NUMBER',
	'PLUS', 'MINUS', 'TIMES', 'DIVIDE',
	'LPAREN', 'RPAREN',
)

# Arithmetic Operators
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
# Boolean Operators
'''
t_AND = r'&'
t_OR = r'\|'
t_EQUALS = r'='
t_NOTEQUALS = r'!='
t_LT = r'<'
t_GT = r'>'
t_LE = r'<='
t_GE = r'>='
t_NOT = r'!'
'''
# Increment & Decrement
'''
t_PLUSPLUS = r'\+\+'
t_MINUSMINUS = r'--'
'''
# Delimeters
t_LPAREN = r'\('
t_RPAREN = r'\)'
'''
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_COMMA = r','
t_PERIOD = r'\.'
t_SEMI = r';'
t_COLON = r':'
'''

def t_NUMBER(t):
    r'\d+'
    try:
    	t.value = int(t.value)
    except ValueError:
    	print "Line %d: Number %s is too large!" % (t.lineno,t.value)
    	t.value = 0
    return t

def t_newline(t):
	r'\n+'
	t.lineno += len(t.value)

t_ignore = ' \t'

def t_error(t):
	print("Illegal character %s" % t.value[0])
	t.skip(1)

lex.lex()
