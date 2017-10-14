# ------------------------------------------------------------
# Equipo:
#   Candelario Gutierrez
#   Diego Vargas
#   "Nutritious"
# ------------------------------------------------------------
import sys

karelParsedFile = ""
counter = 0
officialFunctions = ["move", "turnLeft", "pickBeeper", "putBeeper", "end"]
errors = ""


def read_program(lexerResult):
    global karelParsedFile
    karelParsedFile = open(lexerResult, "r")
    karelParsedFile = karelParsedFile.read().split(",")
    del karelParsedFile[-1]
    program()


def verificar(terminal):
    if(terminal == karelParsedFile[counter]):
        return True
    return False


def exigir(terminal):
    global counter
    if(counter < len(karelParsedFile) and terminal == karelParsedFile[counter]):
        counter += 1
        return True
    return False


def mostrar_error():
    sys.exit("Syntax error")


def program():
    if (exigir("class")):
        if (exigir("program")):
            if (exigir("{")):
                functions()
                main_function()
                if not(exigir("}")):
                    mostrar_error()
            else:
                mostrar_error()
        else:
            mostrar_error()
    else:
        mostrar_error()


def functions():
    if (verificar("void")):
        function()
        functions_prima()


def function():
    if(exigir("void")):
        name_function()
        if(exigir("(")):
            if(exigir(")")):
                if(exigir("{")):
                    body()
                    if not(exigir("}")):
                        mostrar_error()
                else:
                    mostrar_error()
            else:
                mostrar_error()
        else:
            mostrar_error()
    else:
        mostrar_error()


def functions_prima():
    if(verificar("void")):
        function()
        functions_prima()


def main_function():
    if(exigir("program")):
        if(exigir("(")):
            if(exigir(")")):
                if(exigir("{")):
                    body()
                    if not(exigir("}")):
                        mostrar_error()
                else:
                    mostrar_error()
            else:
                mostrar_error()
        else:
            mostrar_error()
    else:
        mostrar_error()


def body():
    expression()
    body_prima()


def body_prima():
    if (verificar("if") or verificar("while") or verificar("iterate") or verificar("move") or verificar("turnLeft") or verificar("pickBeeper") or verificar("putBeeper") or verificar("end")):
        expression()
        body_prima()


def expression():
    if(verificar("if")):
        if_expression()
    elif(verificar("while")):
        while_expression()
    elif(verificar("iterate")):
        iterate_expression()
    else:
        call_function()


def if_expression():
    if(exigir("if")):
        if(exigir("(")):
            condition()
            if(exigir(")")):
                if(exigir("{")):
                    body()
                    if(exigir("}")):
                        else_expression()
                    else:
                        mostrar_error()
                else:
                    mostrar_error()
            else:
                mostrar_error()
        else:
            mostrar_error()
    else:
        mostrar_error()


def else_expression():
    if(verificar("else:")):
        if(exigir("else:")):
            if(exigir("{")):
                body()
                if not(exigir("}")):
                    mostrar_error()
            else:
                mostrar_error()
        else:
            mostrar_error()


def while_expression():
    if(exigir("while")):
        if(exigir("(")):
            condition()
            if(exigir(")")):
                if(exigir("{")):
                    body()
                    if not(exigir("}")):
                        mostrar_error()
                else:
                    mostrar_error()
            else:
                mostrar_error()
        else:
            mostrar_error()
    else:
        mostrar_error()


def iterate_expression():
    if(exigir("iterate")):
        if(exigir("(")):
            number()
            if(exigir(")")):
                if(exigir("{")):
                    body()
                    if not(exigir("}")):
                        mostrar_error()
                else:
                    mostrar_error()
            else:
                mostrar_error()
        else:
            mostrar_error()
    else:
        mostrar_error()


def number():
    for i in range(1, 101):
        if(i == 101):
            mostrar_error()
        if(verificar(i)):
            exigir(i)
            break


def condition():
    conditions = ["front-is-clear", "left-is-clear", "right-is-clear",
                  "front-is-blocked", "left-is-blocked", "right-is-blocked",
                  "next-to-a-beeper", "not-next to a beeper",
                  "facing-north", "facing-south", "facing-east", "facing-west",
                  "not-facing-north", "not-facing-south", "not-facing-east", "not-facing-west",
                  "any-beepers-in-beeper-bag", "no-beepers-in-beeper-bag"]
    for i in range(len(conditions)):
        if(i == len(conditions)):
            mostrar_error()
        if(verificar(conditions[i])):
            exigir(conditions[i])
            break


def call_function():
    name_function()
    if(exigir("(")):
        if not(exigir(")")):
            mostrar_error()
    else:
        mostrar_error()


def name_function():
    if(verificar("move") or verificar("turnLeft") or verificar("pickBeeper") or verificar("putBeeper") or verificar("end")):
        official_function()
    else:
        customer_function()


def official_function():
    j = 0
    for i in range(len(officialFunctions)):
        if(verificar(officialFunctions[i])):
            exigir(officialFunctions[i])
            break
        j += 1
    if(j == len(officialFunctions)):
        mostrar_error()


def customer_function():
    function = karelParsedFile[counter]
    if(len(function) > 2 and len(function) <= 11):
        exigir(function)
    else:
        mostrar_error()
