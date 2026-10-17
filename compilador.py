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


def agregar_linea(numero):
    dato = buscar_simbolo(numero, "L")
    if dato == None:
        tabla_simbolos.append({"simbolo": numero, "tipo": "L", "ubicacion": contador_instrucciones})
    else:
        raise ValueError("Numero de linea repetido: " + str(numero))


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

    if tipo == "V" and not simbolo.isalpha():
        raise ValueError("Nombre de variable incorrecto: " + simbolo)

    if contador_datos <= contador_instrucciones:
        raise ValueError("No hay memoria suficiente")

    posicion = contador_datos
    tabla_simbolos.append({"simbolo": simbolo, "tipo": tipo, "ubicacion": posicion})
    if tipo == "C":
        if simbolo < -9999 or simbolo > 9999:
            raise ValueError("Constante fuera del rango de SML")
        memoria[posicion] = simbolo
    contador_datos = contador_datos - 1
    return posicion


def guardar_instruccion(codigo, operando):
    global contador_instrucciones
    if contador_instrucciones > contador_datos:
        raise ValueError("No hay memoria suficiente")
    posicion = contador_instrucciones
    memoria[posicion] = codigo * 100 + operando
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
            if len(pila) == 0:
                raise ValueError("Parentesis incorrectos")
            pila.pop()
        elif token == "+" or token == "-" or token == "*" or token == "/":
            while len(pila) > 0 and pila[-1] != "(" and prioridad(pila[-1]) >= prioridad(token):
                salida.append(pila.pop())
            pila.append(token)
        else:
            salida.append(token)
    while len(pila) > 0:
        if pila[-1] == "(":
            raise ValueError("Parentesis incorrectos")
        salida.append(pila.pop())
    return salida


def nueva_temporal():
    global contador_datos
    if contador_datos <= contador_instrucciones:
        raise ValueError("No hay memoria suficiente")
    posicion = contador_datos
    contador_datos = contador_datos - 1
    return posicion


def compilar_expresion(expresion):
    postfijo = convertir_postfijo(expresion)
    pila = []
    for token in postfijo:
        if token != "+" and token != "-" and token != "*" and token != "/":
            pila.append(agregar_dato(token))
        else:
            if len(pila) < 2:
                raise ValueError("Expresion incorrecta")
            derecha = pila.pop()
            izquierda = pila.pop()
            temporal = nueva_temporal()
            guardar_instruccion(20, izquierda)
            if token == "+":
                guardar_instruccion(30, derecha)
            elif token == "-":
                guardar_instruccion(31, derecha)
            elif token == "*":
                guardar_instruccion(33, derecha)
            elif token == "/":
                guardar_instruccion(32, derecha)
            guardar_instruccion(21, temporal)
            pila.append(temporal)
    if len(pila) != 1:
        raise ValueError("Expresion incorrecta")
    return pila.pop()


def compilar_if(partes):
    izquierda = agregar_dato(partes[2])
    operador = partes[3]
    derecha = agregar_dato(partes[4])
    if len(partes) != 7:
        raise ValueError("If debe tener la forma: if a == b goto 40")
    if partes[5] != "goto":
        raise ValueError("Falta goto en if")
    destino = int(partes[6])

    if operador == "==" or operador == "<" or operador == "<=":
        guardar_instruccion(20, izquierda)
        guardar_instruccion(31, derecha)
        if operador == "==" or operador == "<=":
            if operador == "<=":
                guardar_salto(41, destino)
            guardar_salto(42, destino)
        else:
            guardar_salto(41, destino)
    elif operador == ">" or operador == ">=":
        guardar_instruccion(20, derecha)
        guardar_instruccion(31, izquierda)
        guardar_salto(41, destino)
        if operador == ">=":
            guardar_salto(42, destino)
    elif operador == "!=":
        guardar_instruccion(20, izquierda)
        guardar_instruccion(31, derecha)
        guardar_salto(41, destino)
        guardar_instruccion(20, derecha)
        guardar_instruccion(31, izquierda)
        guardar_salto(41, destino)
    else:
        raise ValueError("Comparacion no reconocida: " + operador)


def primera_pasada(nombre_archivo):
    global memoria, flags, tabla_simbolos, contador_instrucciones, contador_datos
    memoria = [0] * 100
    flags = [-1] * 100
    tabla_simbolos = []
    contador_instrucciones = 0
    contador_datos = 99

    archivo = open(nombre_archivo, "r", encoding="utf-8")
    lineas = archivo.readlines()
    archivo.close()

    ultimo_numero = -1
    hay_end = False
    for linea in lineas:
        partes = linea.strip().split()
        if len(partes) == 0:
            continue
        if len(partes) < 2:
            raise ValueError("Linea incompleta: " + linea)
        numero = int(partes[0])
        if numero < 0:
            raise ValueError("Numero de linea incorrecto")
        if numero <= ultimo_numero:
            raise ValueError("Las lineas deben estar en orden creciente")
        ultimo_numero = numero
        comando = partes[1].lower()
        agregar_linea(numero)

        if comando == "rem":
            pass
        elif comando == "input":
            if len(partes) != 3 or not partes[2].isalpha():
                raise ValueError("Input necesita una variable")
            guardar_instruccion(10, agregar_dato(partes[2]))
        elif comando == "print":
            if len(partes) != 3:
                raise ValueError("Print necesita un dato")
            guardar_instruccion(11, agregar_dato(partes[2]))
        elif comando == "goto":
            if len(partes) != 3:
                raise ValueError("Goto necesita un numero de linea")
            guardar_salto(40, int(partes[2]))
        elif comando == "if":
            compilar_if(partes)
        elif comando == "let":
            if len(partes) < 5 or not partes[2].isalpha():
                raise ValueError("Let necesita una variable y una expresion")
            if partes[3] != "=":
                raise ValueError("Falta = en let")
            resultado = compilar_expresion(partes[4:])
            guardar_instruccion(20, resultado)
            guardar_instruccion(21, agregar_dato(partes[2]))
        elif comando == "end":
            if len(partes) != 2:
                raise ValueError("End no lleva argumentos")
            guardar_instruccion(43, 0)
            hay_end = True
        else:
            raise ValueError("Comando no reconocido: " + comando)

    if hay_end == False:
        raise ValueError("Falta la instruccion end")


def mostrar_primera_pasada():
    print("\nTABLA DE SIMBOLOS")
    print("Simbolo\tTipo\tUbicacion")
    for dato in tabla_simbolos:
        print(dato["simbolo"], "\t", dato["tipo"], "\t", dato["ubicacion"])

    print("\nINSTRUCCIONES PROVISIONALES")
    for i in range(contador_instrucciones):
        print(i, memoria[i])

    print("\nFLAGS PENDIENTES")
    for i in range(contador_instrucciones):
        if flags[i] != -1:
            print("Posicion", i, "-> linea", flags[i])


def segunda_pasada():
    i = 0
    while i < contador_instrucciones:
        if flags[i] != -1:
            numero_linea = flags[i]
            dato = buscar_simbolo(numero_linea, "L")
            if dato == None:
                raise ValueError("No existe la linea " + str(numero_linea))
            codigo = memoria[i] // 100
            memoria[i] = codigo * 100 + dato["ubicacion"]
            flags[i] = -1
        i = i + 1


def guardar_sml(nombre_archivo):
    archivo = open(nombre_archivo, "w", encoding="utf-8")
    i = 0
    while i < 100:
        numero = memoria[i]
        if numero >= 0:
            archivo.write("+" + str(numero).zfill(4) + "\n")
        else:
            archivo.write("-" + str(abs(numero)).zfill(4) + "\n")
        i = i + 1
    archivo.close()


def mostrar_codigo():
    print("\nCODIGO SML FINAL")
    i = 0
    while i < contador_instrucciones:
        numero = memoria[i]
        if numero >= 0:
            print(str(i).zfill(2), "+" + str(numero).zfill(4))
        else:
            print(str(i).zfill(2), "-" + str(abs(numero)).zfill(4))
        i = i + 1


if __name__ == "__main__":
    print("COMPILADOR SIMPLE A SML")
    nombre = input("Nombre del archivo Simple: ")

    try:
        primera_pasada(nombre)
        mostrar_primera_pasada()
        segunda_pasada()
        mostrar_codigo()
        guardar_sml("programa.sml")
        print("\nPrimera y segunda pasada terminadas")
        print("Archivo programa.sml creado correctamente")
    except (FileNotFoundError, ValueError, IndexError) as error:
        print("Error:", error)
