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
# Tokens recognized by the lexer
tokens = (
	'ID', 'NUMBER',
	'PLUS', 'MINUS', 'TIMES', 'DIVIDE',
	'AND', 'OR', 'EE', 'NE', 'LT', 'GT', 'LE', 'GE',
	'NOT',
	'LPAREN', 'RPAREN',
	'PLUSPLUS', 'MINUSMINUS',
	'EQUALS',
	'PERIOD',
)


t_ID = r'[a-zA-Z][a-zA-Z0-9_]*'
# Arithmetic Operators
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
# Boolean Operators
t_AND = r'&&'
t_OR = r'\|\|'
t_EE = r'=='
t_NE = r'!='
t_LT = r'<'
t_GT = r'>'
t_LE = r'<='
t_GE = r'>='
# Unary Operations
t_NOT = r'!'
t_EQUALS = r'='
# Increment & Decrement
t_PLUSPLUS = r'\+\+'
t_MINUSMINUS = r'--'

# Delimeters
t_LPAREN = r'\('
t_RPAREN = r'\)'

t_PERIOD = r'\.'
'''
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_COMMA = r','

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
