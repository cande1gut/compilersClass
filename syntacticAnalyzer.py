# ------------------------------------------------------------
# Equipo:
#   Candelario Gutierrez
#   Diego Vargas
#   "Nutritious Maincraters"
# ------------------------------------------------------------
import sys

karelParsedFile = ""
counter = 0
officialFunctions = {"move": 1000, "turnLeft": 2000,
                     "pickBeeper": 3000, "putBeeper": 4000, "end": 5000}
customFunctions = {}
errors = ""
actual = 2
ci = [0] * 1000
stack = []
ciSocket = []


def read_program(lexerResult):
    global karelParsedFile
    karelParsedFile = open(lexerResult, "r")
    karelParsedFile = karelParsedFile.read().split(",")
    del karelParsedFile[-1]
    program()
    for i in range(0, actual):
        ciSocket.append(ci[i])
    print(ciSocket)


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


def mostrar_error(error):
    print("Syntactic-Error: Expected: %s,  received: %s" %
          (error, karelParsedFile[counter]))
    sys.exit()


def program():
    if (exigir("class")):
        if (exigir("program")):
            if (exigir("{")):
                functions()
                main_function()
                #print("\nSymbols table")
                # print(customFunctions)
                if not(exigir("}")):
                    mostrar_error("}")
            else:
                mostrar_error("{")
        else:
            mostrar_error("program")
    else:
        mostrar_error("class")


def functions():
    if (verificar("void")):
        function()
        functions_prima()


def function():
    global ci, actual
    if(exigir("void")):
        define_customer_function()
        if(exigir("(")):
            if(exigir(")")):
                if(exigir("{")):
                    body()
                    ci[actual] = 200
                    actual += 1
                    if not(exigir("}")):
                        mostrar_error("}")
                else:
                    mostrar_error("{")
            else:
                mostrar_error(")")
        else:
            mostrar_error("(")
    else:
        mostrar_error("void")


def functions_prima():
    if(verificar("void")):
        function()
        functions_prima()


def main_function():
    if(exigir("program")):
        ci[0] = 100
        ci[1] = actual
        if(exigir("(")):
            if(exigir(")")):
                if(exigir("{")):
                    body()
                    if not(exigir("}")):
                        mostrar_error("}")
                else:
                    mostrar_error("{")
            else:
                mostrar_error(")")
        else:
            mostrar_error("(")
    else:
        mostrar_error("program")


def body():
    expression()
    body_prima()


def body_prima():
    if (verificar("if") or verificar("while") or verificar("iterate") or verificar("move") or verificar("turnLeft") or verificar("pickBeeper") or verificar("putBeeper") or verificar("end")):
        expression()
        body_prima()
    elif ((len(karelParsedFile[counter]) > 2 and len(karelParsedFile[counter]) <= 11)):
        if(karelParsedFile[counter] in customFunctions):
            expression()
            body_prima()
        else:
            mostrar_error("a declared custom function")


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
                    if(exigir("}")):
                        else_expression()
                    else:
                        mostrar_error("}")
                else:
                    mostrar_error("{")
            else:
                mostrar_error(")")
        else:
            mostrar_error("(")


def else_expression():
    global actual, ci, stack
    if(verificar("else")):
        ci[stack.pop()] = actual + 2
        if(exigir("else")):
            if(exigir("{")):
                ci[actual] = 100
                stack.append(actual + 1)
                actual += 2
                body()
                ci[stack.pop()] = actual
                if not(exigir("}")):
                    mostrar_error("}")
            else:
                mostrar_error("{")
        else:
            mostrar_error("else")
    else:
        ci[stack.pop()] = actual


def while_expression():
    global actual, ci, stack
    stack.append(actual)
    ci[actual] = 6000
    actual += 1
    if(exigir("while")):
        if(exigir("(")):
            condition()
            if(exigir(")")):
                if(exigir("{")):
                    ci[actual] = 100
                    stack.append(actual + 1)
                    actual += 2
                    body()
                    ci[stack.pop()] = actual + 2
                    ci[actual] = 100
                    ci[actual + 1] = stack.pop()
                    actual += 2
                    if not(exigir("}")):
                        mostrar_error("}")
                else:
                    mostrar_error("{")
            else:
                mostrar_error(")")
        else:
            mostrar_error("(")
    else:
        mostrar_error("while")


def iterate_expression():
    global actual, ci, stack
    stack.append(actual)
    ci[actual] = 6000
    actual += 1
    if(exigir("iterate")):
        if(exigir("(")):
            number()
            if(exigir(")")):
                if(exigir("{")):
                    ci[actual] = 100
                    stack.append(actual + 1)
                    actual += 2
                    body()
                    ci[stack.pop()] = actual + 2
                    ci[actual] = 100
                    ci[actual + 1] = stack.pop()
                    actual += 2
                    if not(exigir("}")):
                        mostrar_error("}")
                else:
                    mostrar_error("{")
            else:
                mostrar_error(")")
        else:
            mostrar_error("(")
    else:
        mostrar_error("iterate")


def number():
    global ci, actual
    number = karelParsedFile[counter]
    try:
        i = int(number)
        if(i > 1 and i <= 100):
            verificar(str(i))
            exigir(str(i))
        ci[actual] = i
        actual += 1
    except ValueError:
        mostrar_error("valid number")


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
            mostrar_error("valid condition")
        if(verificar(conditions.keys()[i])):
            ci[actual] = conditions.values()[i]
            actual += 1
            exigir(conditions.keys()[i])
            break


def call_function():
    name_function()
    if(exigir("(")):
        if not(exigir(")")):
            mostrar_error(")")
    else:
        mostrar_error("(")


def name_function():
    if(verificar("move") or verificar("turnLeft") or verificar("pickBeeper") or verificar("putBeeper") or verificar("end")):
        official_function()
    else:
        customer_function()


def official_function():
    global actual, ci, ciSocket
    for i in range(len(officialFunctions)):
        if(verificar(officialFunctions.keys()[i])):
            ci[actual] = officialFunctions.values()[i]
            actual += 1
            exigir(officialFunctions.keys()[i])
            break


def define_customer_function():
    global customFunctions, actual
    function = karelParsedFile[counter]
    if((len(function) > 2 and len(function) <= 11)):
        exigir(function)
        customFunctions[function] = actual
    else:
        mostrar_error("valid customer function name")


def customer_function():
    global ci, actual, customFunctions
    function = karelParsedFile[counter]
    if((len(function) > 2 and len(function) <= 11)):
        exigir(function)
        ci[actual] = 300

        ci[actual + 1] = customFunctions.get(function)
        actual += 2
    else:
        mostrar_error("valid customer function name")
