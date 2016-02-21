import ply.lex as lex

lex.lex()
# Reserved words
reserved = (
	'BOOLEAN', 'BREAK', 'CONTINUE', 'CLASS', 'DO', 'ELSE',
	'EXTENDS', 'FALSE', 'FLOAT', 'FOR', 'IF', 'INT',
	'NEW', 'NULL', 'PRIVATE', 'PUBLIC', 'RETURN', 'STATIC',
	'SUPER', 'THIS', 'TRUE', 'VOID', 'WHILE',
)

reserved_words = {}
for reserved in reserved_words:
	reserved_map[reserved.lower()] = reserved
# Tokens recognized by the lexer
token = (
	# Identifiers
	'ID',
	# Constants
	'INT_CONST', 'FLOAT_CONST', 'STRING_CONST',
	# Arithmetic Operations
	'PLUS', 'MINUS', 'TIMES', 'DIVIDE',
	# Boolean Operations
	'AND', 'OR', 'EQUALS', 'NOTEQUALS',
	'LT', 'BT', 'LTE', 'BTE', 'NOT',
	# Increment & Decrement
	'PLUSPLUS', 'MINUSMINUS',
	# Conditional statement
	'CONDOP',
	# Delimeters
	'LPAREN', 'RPAREN',
	'LBRACKET', 'RBRAKET',
	'LBRACE', 'RBRACE',
	'COMMA', 'PERIOD',
	'SEMI', 'COLON',
)

identifier = r'[a-zA-Z_][0-9a-zA-Z_]*'
integer_const = r'[1-9][0-9]*'
float_const = r'[0-9]*.[0-9]+'
#string_const = ?

# Arithmetic Operators
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
# Boolean Operators
t_AND = r'&'
t_OR = r'\|'
t_EQUALS = r'='
t_NOTEQUALS = r'!='
t_LT = r'<'
t_BT = r'>'
t_LTE = r'<='
t_BTE = r'>='
t_NOT = r'!'
# Increment & Decrement
t_PLUSPLUS = r'\+\+'
t_MINUSMINUS = r'--'
# Delimeters
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_COMMA = r','
t_PERIOD = r'\.'
t_SEMI = r';'
t_COLON = r':'
