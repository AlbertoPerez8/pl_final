import ply.yacc as parse
from LangLex import tokens
from Functionality import Server as s
import cleaner as clean


code = s.Server()


# Defined here are all the methods that deal with the different expressions (HELP, ID EQUAL ID SEMICOLON, etc.)
def p_help(p):
    ' Exp : HELP'
    p[0] = "To create a server, run: 'createServer (port= 3000);' and store it on a variable.\nTo run the server, run: 'variable : start;' \n"


def p_object_def_empty(p):
    'Exp : ID EQUAL JSON COLON LC RC SEMICOLON'
    code.update_variables(p[1], "{}")
    p[0] = clean.id_saved(p[1])


def p_id_id(p):
    'Exp : ID EQUAL ID SEMICOLON'
    if p[3] not in code.variables:
        p[0] = clean.id_not_defined(p[3])
    else:
        code.update_variables(p[1], code.print_object(p[3]))
        p[0] = clean.id_saved(p[1])


def p_id_int(p):
    'Exp : ID EQUAL INT SEMICOLON'
    code.update_variables(p[1], p[3])
    p[0] = clean.id_saved(p[1])


def p_object_def(p):
    'Exp : ID EQUAL JSON COLON LC Inside RC SEMICOLON'
    code.update_variables(p[1], "{"+p[6]+"}")
    p[0] = clean.id_saved(p[1])


def p_inside_object_rec(p):
    'Inside : InsideRec'
    p[0] = str(p[1])


def p_inside_object(p):
    'Inside :  STRING COLON STRING '
    p[0] = str(p[1])+str(p[2])+str(p[3])


def p_inside_rec(p):
    'InsideRec : Inside COMMA Inside '
    p[0] = str(p[1])+str(p[2])+str(p[3])


def p_variable(p):
    'Exp : ID SEMICOLON'
    if p[1] not in code.variables:
        p[0] = clean.id_not_defined(p[1])
    else:
        for i in code.variables:
            if p[1] == i:
                p[0] = code.print_object(i)
                break


# Build Parser
parser = parse.yacc()
