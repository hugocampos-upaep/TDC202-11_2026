def es_numero(token):
    if token == "":
        return False
    if token[0] == "-":
        token = token[1:]
    return token.isdigit()


def es_variable(token):
    return len(token) == 1 and token in "abcdefghijklmnopqrstuvwxyz"


def separar_expresion(texto):
    tokens = []
    i = 0

    while i < len(texto):
        letra = texto[i]

        if letra.isspace():
            i = i + 1
        elif letra.isdigit() or (letra == "-" and i + 1 < len(texto) and texto[i + 1].isdigit() and (len(tokens) == 0 or tokens[-1] in ["+", "-", "*", "/", "^", "(", "[", "{"])):
            numero = letra
            i = i + 1
            while i < len(texto) and texto[i].isdigit():
                numero = numero + texto[i]
                i = i + 1
            tokens.append(numero)
        elif letra.isalpha():
            if not es_variable(letra):
                raise ValueError("Las variables deben ser letras minusculas de a a z")
            tokens.append(letra)
            i = i + 1
        elif letra in "+-*/^()[]{}":
            tokens.append(letra)
            i = i + 1
        else:
            raise ValueError("Caracter no permitido: " + letra)

    return tokens


def validar_agrupacion(tokens):
    pila = []
    maximo = 0

    for token in tokens:
        if token in ["(", "[", "{"]:
            pila.append(token)
            if len(pila) > maximo:
                maximo = len(pila)
        elif token in [")", "]", "}"]:
            if len(pila) == 0:
                raise ValueError("Simbolos de agrupacion incorrectos")
            if token == ")" and pila[-1] != "(":
                raise ValueError("Simbolos de agrupacion incorrectos")
            if token == "]" and pila[-1] != "[":
                raise ValueError("Simbolos de agrupacion incorrectos")
            if token == "}" and pila[-1] != "{":
                raise ValueError("Simbolos de agrupacion incorrectos")
            pila.pop()

    if len(pila) != 0:
        raise ValueError("Falta cerrar un simbolo de agrupacion")

    return maximo


def prioridad(operador):
    if operador == "+" or operador == "-":
        return 1
    if operador == "*" or operador == "/":
        return 2
    if operador == "^":
        return 3
    return 0


def convertir_postfijo(tokens):
    validar_agrupacion(tokens)
    salida = []
    pila = []

    for token in tokens:
        if token in ["(", "[", "{"]:
            pila.append(token)
        elif token in [")", "]", "}"]:
            while pila[-1] not in ["(", "[", "{"]:
                salida.append(pila.pop())
            pila.pop()
        elif token in ["+", "-", "*", "/", "^"]:
            while len(pila) > 0 and pila[-1] not in ["(", "[", "{"]:
                anterior = pila[-1]
                if prioridad(anterior) > prioridad(token) or (prioridad(anterior) == prioridad(token) and token != "^"):
                    salida.append(pila.pop())
                else:
                    break
            pila.append(token)
        else:
            if not es_numero(token) and not es_variable(token):
                raise ValueError("Operando incorrecto: " + token)
            salida.append(token)

    while len(pila) > 0:
        salida.append(pila.pop())

    cantidad = 0
    for token in salida:
        if token in ["+", "-", "*", "/", "^"]:
            if cantidad < 2:
                raise ValueError("Expresion incompleta")
            cantidad = cantidad - 1
        else:
            cantidad = cantidad + 1

    if cantidad != 1:
        raise ValueError("Expresion incorrecta")

    return salida


def evaluar_postfijo(tokens, variables):
    pila = []
    for token in tokens:
        if token in ["+", "-", "*", "/", "^"]:
            if len(pila) < 2:
                raise ValueError("Expresion incorrecta")
            derecha = pila.pop()
            izquierda = pila.pop()

            if token == "+":
                resultado = izquierda + derecha
            elif token == "-":
                resultado = izquierda - derecha
            elif token == "*":
                resultado = izquierda * derecha
            elif token == "/":
                if derecha == 0:
                    raise ValueError("Division entre cero")
                resultado = int(izquierda / derecha)
            else:
                if derecha < 0:
                    raise ValueError("No se admiten exponentes negativos")
                resultado = izquierda ** derecha

            pila.append(resultado)
        elif es_numero(token):
            pila.append(int(token))
        else:
            if token not in variables:
                raise ValueError("Falta el valor de " + token)
            pila.append(variables[token])

    if len(pila) != 1:
        raise ValueError("Expresion incorrecta")
    return pila[0]


if __name__ == "__main__":
    texto = input("Expresion: ")
    try:
        tokens = separar_expresion(texto)
        print("Profundidad:", validar_agrupacion(tokens))
        postfijo = convertir_postfijo(tokens)
        print("Postfijo:", " ".join(postfijo))
        variables = {}
        for token in postfijo:
            if token.isalpha() and token not in variables:
                variables[token] = int(input("Valor de " + token + ": "))
        print("Resultado:", evaluar_postfijo(postfijo, variables))
    except ValueError as error:
        print("Error:", error)
