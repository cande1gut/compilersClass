# ------------------------------------------------------------
# Equipo:
#   Candelario Gutierrez
#   Diego Vargas
#   "Nutritious"
# ------------------------------------------------------------
import ply.lex as lex

# Lists of reserved stuff
reserved = {
    'void': 'VOID',
    'class': 'CLASS',
    'program': 'PROGRAM',
    'end': 'END',
    'if': 'IF',
    'else': 'ELSE',
    'while': 'WHILE',
    'iterate': 'ITERATE',
    'return': 'RETURN',
    '||': 'OR',
    '&&': 'AND',
    '!': 'NOT',
    'turnoff': 'TURNOFF',
    'turnleft': 'TURNLEFT',
    'move': 'MOVE',
    'pickbeeper': 'PICKBEEPER',
    'putbeeper': 'PUTBEEPER',
    'front-is-clear': 'FRONTISCLEAR',
    'left-is-clear': 'LEFTISCLEAR',
    'right-is-clear': 'RIGHTISCLEAR',
    'front-is-blocked': 'FRONTISBLOCKED',
    'left-is-blocked': 'LEFTISBLOCKED',
    'right-is-blocked': 'RGHTISBLOCKED',
    'next-to-a-beeper': 'NEXTTOABEEPER',
    'not-next-to-a-beeper': 'NOTNEXTTOABEEPER',
    'facing-north': 'FACINGNORTH',
    'facing-south': 'FACINGSOUTH',
    'facing-east': 'FACINGEAST',
    'facing-west': 'FACINGWEST',
    'not-facing-north': 'NOTFACINGNORTH',
    'not-facing-south': 'NOTFACINGSOUTH',
    'not-facing-east': 'NOTFACINGEAST',
    'not-facing-west': 'NOTFACINGWEST',
    'any-beepers-in-beeper-bag': 'ANYBEEPERSINBEEPERBAG',
    'no-beepers-in-beeper-bag': 'NOBEEPERSBAG'
}

tokens = [
    'CNAME',
    'NUMBER',
    'LBRACKET',
    'RBRACKET',
    'LPARENTHESES',
    'RPARENTHESES',
    'RWORD'
] + list(reserved.values())

# Regular expression rules for simple tokens
t_LPARENTHESES = r'\('
t_RPARENTHESES = r'\)'
t_LBRACKET = r'\{'
t_RBRACKET = r'\}'


def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t


def t_CNAME(t):
    r'[a-zA-Z_][-a-zA-Z0-9_]*'
    if t.value in reserved:
        t.type = reserved.get(t.value, 'RWORD')
    else:
        t.type = 'CNAME'
    return t


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


t_ignore = " \t"

# Error handling rule


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


# Build the lexer
lexer = lex.lex()


def create_tokens(karelProgramText):
    karelProgram = open(karelProgramText).read()

    # Give the lexer some input
    lexer.input(karelProgram)

    karelParsed = open("lexerResult.txt", "w")
    karelErrors = open("lineNumbers.txt", "w")

    # Tokenize
    while True:
        tok = lexer.token()
        if not tok:
            break
        karelParsed.write(tok.value + ',')
        #karelErrors.write(str(tok.lineno) + ", " + str(tok.lexpos))

    karelParsed.close()
    # karelErrors.close()
    #karelErrors2 = open("lexerResult.txt", "r")
    # print(karelErrors2.read().split(","))
