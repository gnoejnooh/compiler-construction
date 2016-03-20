import ply.lex as lex

# Tokens recognized by the lexer
tokens = (
	'NUMBER',
	'PLUS', 
	'MINUS', 
	'TIMES', 
	'DIVIDE',
	'EQUAL',
	'NAME',
)

# Arithmetic Operators
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_EQUAL = r'='
t_ignore =' \t'
t_NAME    = r'[a-zA-Z_][a-zA-Z0-9_]*'

def t_NUMBER(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t
    
def t_newline(t):
	r'\n+'
	t.lexer.lineno += len(t.value)
    
def t_error(t):
    print "%d: Illegal character '%s'" % (t.lexer.lineno, t.value[0])
    print t.value
    t.lexer.skip(1)

lexer = lex.lex()

# Set Initial Count to 0
lexer.num_count = 0