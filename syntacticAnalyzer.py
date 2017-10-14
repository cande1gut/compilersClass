# ------------------------------------------------------------
# Equipo:
#   Candelario Gutierrez
#   Diego Vargas
#   "Nutritious"
# ------------------------------------------------------------
import sys

karelParsedFile = ""
counter = 0
officialFunctions = {"move": 1000, "turnLeft": 2000,
                     "pickBeeper": 3000, "putBeeper": 4000, "end": 5000}
errors = ""
actual = 0
ci = [0] * 1000
stack = []


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
    global actual, ci, stack
    ci[actual] = 6000
    actual += 1
    if(exigir("if")):
        if(exigir("(")):
            condition()
            if(exigir(")")):
                if(exigir("{")):
                    ci[actual] = 100
                    stack.append(actual + 1)
                    actual += 2
                    body()
                    ci[stack.pop()] = actual
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
    global actual, ci
    conditions = {"front-is-clear": 6001, "left-is-clear": 6002, "right-is-clear": 6003,
                  "front-is-blocked": 6004, "left-is-blocked": 6005, "right-is-blocked": 6006,
                  "next-to-a-beeper": 6007, "not-next to a beeper": 6008,
                  "facing-north": 6009, "facing-south": 6010, "facing-east": 6011, "facing-west": 6012,
                  "not-facing-north": 6013, "not-facing-south": 6014, "not-facing-east": 6015, "not-facing-west": 6016,
                  "any-beepers-in-beeper-bag": 6017, "no-beepers-in-beeper-bag": 6018}
    for i in range(len(conditions)):
        if(i == len(conditions)):
            mostrar_error()
        if(verificar(conditions.keys()[i])):
            ci[actual] = conditions.values()[i]
            actual += 1
            exigir(conditions.keys()[i])
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
    global actual, ci
    for i in range(len(officialFunctions)):
        if(verificar(officialFunctions.keys()[i])):
            ci[actual] = officialFunctions.values()[i]
            actual += 1
            exigir(officialFunctions.keys()[i])
            if(officialFunctions.keys()[i] == "end"):
                for i in range(0, actual):
                    print(ci[i])
            break


def customer_function():
    function = karelParsedFile[counter]
    if(len(function) > 2 and len(function) <= 11):
        exigir(function)
    else:
        mostrar_error()
