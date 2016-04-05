#!/usr/bin/python
import ply.lex as lex
import sys

errorflag = False

reserved = {
   'if' : 'IF',
   'else' : 'ELSE',
   'while' : 'WHILE',
   'for' : 'FOR',
   'new' : 'NEW',
   'true' : 'TRUE',
   'false' : 'FALSE',
   'int' : 'INT',
   'boolean' : 'BOOLEAN',
   'void' : 'VOID',
   'return' : 'RETURN',
   'break' : 'BREAK',
   'continue' : 'CONTINUE',
   'class' : 'CLASS',
   'float' : 'FLOAT',
   'extends' : 'EXTENDS',
   'null' : 'NULL',
   'public' : 'PUBLIC',
   'private' : 'PRIVATE',
   'return' : 'RETURN',
   'static' : 'STATIC',
   'super' : 'SUPER',
   'this' : 'THIS'
}

tokens = ['DOT', 'COMMA', 'SEMICOLON', 
          'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE', 'LBRACKET', 'RBRACKET', 
          'ASSIGN', 
          'NOT', 'PLUS', 'MINUS', 
          'MULTIPLY', 'DIVIDE', 'AND', 'OR', 'EQ', 'NEQ', 'LT', 'LEQ', 'GT', 'GEQ', 
          'INC', 'DEC',
          'ID', 'INT_CONST', 'FLOAT_CONST', 'STRING_CONST'] + list(reserved.values())


t_DOT = r'\.'
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_MULTIPLY   = r'\*'
t_DIVIDE  = r'/'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_LBRACE = r'{'
t_RBRACE = r'}'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_AND = r'&&'
t_OR = r'\|\|'
t_EQ = r'=='
t_NEQ = r'!='
t_LT = r'<'
t_LEQ = r'<='
t_GT = r'>'
t_GEQ = r'>='
t_NOT = r'!'
t_SEMICOLON = r';'
t_ASSIGN = r'='
t_INC = r'\+\+'
t_DEC = r'--'
t_COMMA = r','
t_ignore_COMMENT = r'//.*'

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')    # Check for reserved words
    return t

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    pass

# Also through multiline comments
def t_ignore_COMMENT_MULTI(t):
    r'/\*(.|\n)*?\*/'
    t.lexer.lineno += t.value.count('\n')
    pass

def t_FLOAT_CONST(t):
    r'\d+\.\d+((e|E)(\+|-)?\d+)?|\d+(e|E)(\+|-)?\d+'
    t.value = float(t.value)
    return t

def t_INT_CONST(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_STRING_CONST(t):
    r'"([^\\"]|\\\\|\\"|\\n|\\t)*"'
    t.value = t.value[1:-1]
    t.lexer.lineno += t.value.count('\n')  # since newlines may be embedded in strings
    return t

# Error handling rule
def t_error(t):
    global errorflag
    print("{1}: Illegal character '{0}'".format(t.value[0], t.lineno))
    t.lexer.skip(1)
    errorflag = True

t_ignore  = ' \t'

#lexer = lex.lex()

def g_token(lexer):
    while True :
        t = lexer.token()
        if not t:
            return
        yield t

if __name__ == '__main__':
    f = open(sys.argv[1], "r")
    lexer.input(f.read())
    for tok in g_token(lexer):
        print("(%s,%r,%d,%d)" % (tok.type, tok.value, tok.lineno,tok.lexpos))
