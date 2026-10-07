READ = 10
WRITE = 11
LOAD = 20
STORE = 21
ADD = 30
SUBTRACT = 31
DIVIDE = 32
MULTIPLY = 33
BRANCH = 40
BRANCHNEG = 41
BRANCHZERO = 42
HALT = 43

memoria = [0] * 100
flags = [-1] * 100
tabla_simbolos = []

contador_instrucciones = 0
contador_datos = 99


def buscar_simbolo(simbolo, tipo):
    for dato in tabla_simbolos:
        if dato["simbolo"] == simbolo and dato["tipo"] == tipo:
            return dato

    return None


def agregar_linea(numero_linea):
    global contador_instrucciones

    dato = buscar_simbolo(numero_linea, "L")

    if dato == None:
        nuevo = {
            "simbolo": numero_linea,
            "tipo": "L",
            "ubicacion": contador_instrucciones
        }

        tabla_simbolos.append(nuevo)

    else:
        dato["ubicacion"] = contador_instrucciones


def agregar_dato(token):
    global contador_datos

    if token.lstrip("-").isdigit():
        simbolo = int(token)
        tipo = "C"
    else:
        simbolo = token
        tipo = "V"

    dato = buscar_simbolo(simbolo, tipo)

    if dato != None:
        return dato["ubicacion"]

    nuevo = {
        "simbolo": simbolo,
        "tipo": tipo,
        "ubicacion": contador_datos
    }

    tabla_simbolos.append(nuevo)

    if tipo == "C":
        memoria[contador_datos] = simbolo

    posicion = contador_datos
    contador_datos = contador_datos - 1

    return posicion


def guardar_instruccion(codigo, operando):
    global contador_instrucciones

    memoria[contador_instrucciones] = codigo * 100 + operando

    posicion = contador_instrucciones
    contador_instrucciones = contador_instrucciones + 1

    return posicion


def guardar_salto(codigo, numero_linea):
    dato = buscar_simbolo(numero_linea, "L")

    if dato != None:
        guardar_instruccion(codigo, dato["ubicacion"])

    else:
        posicion = guardar_instruccion(codigo, 0)
        flags[posicion] = numero_linea


def prioridad(operador):
    if operador == "+" or operador == "-":
        return 1

    if operador == "*" or operador == "/":
        return 2

    return 0


def convertir_postfijo(expresion):
    salida = []
    pila = []

    for token in expresion:

        if token == "(":
            pila.append(token)

        elif token == ")":
            while len(pila) > 0 and pila[-1] != "(":
                salida.append(pila.pop())

            if len(pila) > 0:
                pila.pop()

        elif token == "+" or token == "-" or token == "*" or token == "/":

            while len(pila) > 0 and pila[-1] != "(" and prioridad(pila[-1]) >= prioridad(token):
                salida.append(pila.pop())

            pila.append(token)

        else:
            salida.append(token)

    while len(pila) > 0:
        salida.append(pila.pop())

    return salida


def nueva_temporal():
    global contador_datos

    posicion = contador_datos
    contador_datos = contador_datos - 1

    return posicion


def compilar_expresion(expresion):
    postfijo = convertir_postfijo(expresion)
    pila = []

    for token in postfijo:

        if token != "+" and token != "-" and token != "*" and token != "/":
            posicion = agregar_dato(token)
            pila.append(posicion)

        else:
            derecha = pila.pop()
            izquierda = pila.pop()

            temporal = nueva_temporal()

            guardar_instruccion(LOAD, izquierda)

            if token == "+":
                guardar_instruccion(ADD, derecha)

            elif token == "-":
                guardar_instruccion(SUBTRACT, derecha)

            elif token == "*":
                guardar_instruccion(MULTIPLY, derecha)

            elif token == "/":
                guardar_instruccion(DIVIDE, derecha)

            guardar_instruccion(STORE, temporal)

            pila.append(temporal)

    return pila.pop()


def compilar_if(partes):
    izquierda = partes[2]
    operador = partes[3]
    derecha = partes[4]
    destino = int(partes[6])

    posicion_izquierda = agregar_dato(izquierda)
    posicion_derecha = agregar_dato(derecha)

    if operador == "==":
        guardar_instruccion(LOAD, posicion_izquierda)
        guardar_instruccion(SUBTRACT, posicion_derecha)
        guardar_salto(BRANCHZERO, destino)

    elif operador == "<":
        guardar_instruccion(LOAD, posicion_izquierda)
        guardar_instruccion(SUBTRACT, posicion_derecha)
        guardar_salto(BRANCHNEG, destino)

    elif operador == ">":
        guardar_instruccion(LOAD, posicion_derecha)
        guardar_instruccion(SUBTRACT, posicion_izquierda)
        guardar_salto(BRANCHNEG, destino)


def primera_pasada(nombre_archivo):
    archivo = open(nombre_archivo, "r")
    lineas = archivo.readlines()
    archivo.close()

    for linea in lineas:
        linea = linea.strip()

        if linea == "":
            continue

        partes = linea.split()

        numero_linea = int(partes[0])
        comando = partes[1]

        agregar_linea(numero_linea)

        if comando == "rem":
            pass

        elif comando == "input":
            variable = partes[2]
            posicion = agregar_dato(variable)
            guardar_instruccion(READ, posicion)

        elif comando == "print":
            variable = partes[2]
            posicion = agregar_dato(variable)
            guardar_instruccion(WRITE, posicion)

        elif comando == "goto":
            destino = int(partes[2])
            guardar_salto(BRANCH, destino)

        elif comando == "if":
            compilar_if(partes)

        elif comando == "let":
            variable = partes[2]
            expresion = partes[4:]

            resultado = compilar_expresion(expresion)
            posicion_variable = agregar_dato(variable)

            guardar_instruccion(LOAD, resultado)
            guardar_instruccion(STORE, posicion_variable)

        elif comando == "end":
            guardar_instruccion(HALT, 0)


def mostrar_tabla():
    print()
    print("TABLA DE SIMBOLOS")
    print("Simbolo\tTipo\tUbicacion")

    for dato in tabla_simbolos:
        print(str(dato["simbolo"]) + "\t" +
              dato["tipo"] + "\t" +
              str(dato["ubicacion"]))


def mostrar_memoria():
    print()
    print("INSTRUCCIONES GENERADAS")

    i = 0

    while i < contador_instrucciones:
        print(str(i) + "\t" + str(memoria[i]))
        i = i + 1


def mostrar_flags():
    print()
    print("FLAGS")

    encontrado = False
    i = 0

    while i < contador_instrucciones:

        if flags[i] != -1:
            print("Posicion " + str(i) + " -> linea " + str(flags[i]))
            encontrado = True

        i = i + 1

    if encontrado == False:
        print("No hay referencias pendientes")


print("PRIMERA PASADA DEL COMPILADOR")
print()

nombre = input("Nombre del archivo Simple: ")

try:
    primera_pasada(nombre)
    mostrar_tabla()
    mostrar_memoria()
    mostrar_flags()

except FileNotFoundError:
    print("No se encontro el archivo")
