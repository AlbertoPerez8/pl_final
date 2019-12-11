import ply.lex as lex
from File import fileRead

#Reserved Words
actions = {
    'createData': 'CREATEDATA',
    'setRoutes': 'SETROUTES',
    'readData': 'READDATA',
    'httpGet': 'HTTPGET',
    'start': 'START',
    'createServer': 'CREATESERVER',

}

reserved = {
    'port': 'PORT',
    'json': 'JSON',
    'url': 'URL',
    'body': 'BODY',
    'object': 'OBJECT',
    'Help': 'HELP',

}

reserved.update(actions)

tokens = [
    'INT',
    'ID',
    'STRING',
    'LP',
    'RP',
    'LC',
    'RC',
    'COMMA',
    'SEMICOLON',
    'COLON',
    'EQUAL',

] + list(reserved.values())

#Regular expressions rules for simple tokens

#For numbers(Integers)
def t_INT(t):
    r'(\d+)'
    return t

#For Variables and Reserved Words
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    if t.value in reserved:
        t.type = reserved[t.value]
    return t

#Comments
def t_COMMENTS(t):
    r'\// . * \\'
    pass

#Strings
def t_STRING(t):
    r'\"(.*?)"'
    return t

#Equals sign
t_EQUAL = r'='

#Parenthesis
t_LP = r'\(' #left
t_RP = r'\)' #right

#Curly brackets
t_LC = r'\{' #left
t_RC = r'\}' #right

#Comma, Semicolon & colon
t_COMMA = r','
t_SEMICOLON = r';'
t_COLON = r':'

#Ignored characters
t_ignore = '\t \n'

#Error
def t_error(t):
    print("Illegal Character %s'" % t.value[0])
    t.lexer.skip(1)

#Build lexer
lexer = lex.lex()

lexer.input(fileRead())



"""while True:
    tok = lexer.token()
    if not tok : break
    print(tok)

print(tokens)"""