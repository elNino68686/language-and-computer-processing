
# ------------------------------------------------------------

#<tag>  </tag>
#<tag atr="valor"...> pal pal </tag>
#pal = \w+

# a) Imprimir o nome da tag
# b) Verificar se a tag que fecha condiz com a última que abriu
#    ex: <a> <b> bla bla </b> ble ble </a>
# ------------------------------------------------------------

import ply.lex as lex
import sys


# Declare the state
states = (
   ('tag','exclusive'),
   ('tagf','exclusive')
)

# List of token names.   This is always required
tokens = (
    'MENOR',
    'IGUAL',
    'PALAVRA',
    'BARRA'
)

# Regular expression rules for tokens in initial state
def t_BARRA(t):
    r'</'
    t.lexer.begin('tagf')

def t_MENOR(t):
    r'<'
    t.lexer.begin('tag')

def t_tag_PALAVRA(t):
    r'\w+'
    print(t.value)
    lexer.stack.append(t.value)
    t.lexer.begin('INITIAL')
    
def t_tagf_PALAVRA(t):
    r'\w+'
    if ( lexer.stack ):
       if ( t.value != (esperado := lexer.stack.pop()) ):
           print("Erro -- fechou com ",t.value," sendo esperado ",esperado)
    else:
       print("Erro -- a fechar com ",t.value," quando não há nenhuma Tag aberta ")
    t.lexer.begin("INITIAL")

# Define a rule so we can track line numbers
def t_ANY_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    return 

# A string containing ignored characters (spaces and tabs)
t_ANY_ignore  = ' \t'

# Error handling rule: remaining chars
def t_ANY_error(t): #regra valida em todos os estados
    t.lexer.skip(1)
    return

# ---------------------------------------------------------------
# 

# Build the lexer
lexer = lex.lex()

# My state
lexer.stack = []


# Reading input
for linha in sys.stdin:
    lexer.input(linha)
    tok = lexer.token()
    while tok:
        #print(tok)
        tok = lexer.token()
