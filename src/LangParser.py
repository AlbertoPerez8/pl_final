import ply.yacc as parse
from LangLex import tokens
from Functionality import Server as s
import cleaner as clean


code = s.Server()


# Defined here are all the methods that deal with the different expressions (HELP, ID EQUAL ID SEMICOLON, etc.)
def par_help(p):
    ' Exp : HELP'
    p[0] = "To create a server, run: 'createServer (port= 3000);' and store it on a variable.\nTo run the server, run: 'variable : start;' \n"


def par_object_def_empty(p):
    'Exp : ID EQUAL JSON COLON LC RC SEMICOLON'
    code.update_variables(p[1], "{}")
    p[0] = clean.id_saved(p[1])


def par_id_id(p):
    'Exp : ID EQUAL ID SEMICOLON'
    if p[3] not in code.variables:
        p[0] = clean.id_not_defined(p[3])
    else:
        code.update_variables(p[1], code.print_object(p[3]))
        p[0] = clean.id_saved(p[1])


def par_id_int(p):
    'Exp : ID EQUAL INT SEMICOLON'
    code.update_variables(p[1], p[3])
    p[0] = clean.id_saved(p[1])


# Build Parser
parser = parse.yacc()
