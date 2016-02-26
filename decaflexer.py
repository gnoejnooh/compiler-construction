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
reserved = (
	'BOOLEAN', 'BREAK', 'CONTINUE', 'CLASS', 'DO', 'ELSE',
	'EXTENDS', 'FALSE', 'FLOAT', 'FOR', 'IF', 'INT',
	'NEW', 'null': 'NULL', 'PRIVATE', 'PUBLIC', 'RETURN', 'STATIC',
	'SUPER', 'THIS', 'TRUE', 'VOID', 'WHILE',
)
'''
reserved = (
	'IF', 'ELSE', 'WHILE', 'FOR', 'RETURN', 'BREAK', 'CONTINUE',
	'NEW', 'SUPER', 'THIS',
)
# Tokens recognized by the lexer
tokens = reserved + (
	'ID', 'INT_CONST', 'FLOAT_CONST', 'STRING_CONST',
	'NULL', 'TRUE', 'FALSE',
	'PLUS', 'MINUS', 'TIMES', 'DIVIDE',
	'AND', 'OR', 'EE', 'NE', 'LT', 'GT', 'LE', 'GE',
	'NOT',
	'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE',
	'PLUSPLUS', 'MINUSMINUS',
	'EQUALS',
	'PERIOD', 'COMMA', 'SEMI',
)


t_ID = r'[a-zA-Z][a-zA-Z0-9_]*'
t_INT_CONST = r'\d+'    
t_FLOAT_CONST   = r'((\d*\.\d+)(E[\+-]?\d+)?|([1-9]\d*E[\+-]?\d+))'
t_STRING_CONST  = r'\".*?\"'
t_FALSE = r'\x66\x61\x6c\x73\x65'  # 'false'
t_TRUE = r'\x74\x72\x75\x65'      # 'true'
t_NULL = r'\x6e\x75\x6c\x6c'      # 'null'
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
t_LBRACE = r'\{'
t_RBRACE = r'\}'

t_PERIOD = r'\.'
t_COMMA = r','
t_SEMI = r';'
'''
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_COLON = r':'
'''
reserved_map = { }
for r in reserved:
	reserved_map[r.lower()] = r

# Comments
def t_comment(t):
    r'/\*(.|\n)*?\*/'
    t.lexer.lineno += t.value.count('\n')

def t_newline(t):
	r'\n+'
	t.lineno += len(t.value)

t_ignore = ' \t'

def t_error(t):
	print("Illegal character %s" % t.value[0])
	t.skip(1)

lex.lex()
