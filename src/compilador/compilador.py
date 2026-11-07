from src.expresiones import expresiones


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
    if buscar_simbolo(numero, "L") != None:
        raise ValueError("Numero de linea repetido: " + str(numero))
    tabla_simbolos.append({"simbolo": numero, "tipo": "L", "ubicacion": contador_instrucciones})


def agregar_dato(token):
    global contador_datos

    if expresiones.es_numero(token):
        simbolo = int(token)
        tipo = "C"
        if simbolo < -9999 or simbolo > 9999:
            raise ValueError("Constante fuera del rango de SML")
    else:
        simbolo = token
        tipo = "V"
        if not expresiones.es_variable(simbolo):
            raise ValueError("Variable incorrecta: " + simbolo)

    dato = buscar_simbolo(simbolo, tipo)
    if dato != None:
        return dato["ubicacion"]

    if contador_datos < contador_instrucciones:
        raise ValueError("No hay memoria suficiente para los datos")

    posicion = contador_datos
    tabla_simbolos.append({"simbolo": simbolo, "tipo": tipo, "ubicacion": posicion})
    if tipo == "C":
        memoria[posicion] = simbolo
    contador_datos = contador_datos - 1
    return posicion


def guardar_instruccion(codigo, operando):
    global contador_instrucciones

    if contador_instrucciones > contador_datos:
        raise ValueError("Las instrucciones invaden los datos")
    if operando < 0 or operando > 99:
        raise ValueError("Direccion de memoria incorrecta")

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


def nueva_temporal():
    global contador_datos
    if contador_datos < contador_instrucciones:
        raise ValueError("No hay memoria suficiente para temporales")
    posicion = contador_datos
    contador_datos = contador_datos - 1
    return posicion


def compilar_potencia(izquierda, derecha):
    for dato in tabla_simbolos:
        if dato["tipo"] == "C" and dato["ubicacion"] == derecha and dato["simbolo"] < 0:
            raise ValueError("La potencia no acepta exponentes negativos")

    uno = agregar_dato("1")
    cuenta = nueva_temporal()
    resultado = nueva_temporal()

    guardar_instruccion(20, derecha)
    guardar_instruccion(21, cuenta)
    guardar_instruccion(20, uno)
    guardar_instruccion(21, resultado)

    inicio = contador_instrucciones
    guardar_instruccion(20, cuenta)
    salto_cero = guardar_instruccion(42, 0)
    salto_negativo = guardar_instruccion(41, 0)
    guardar_instruccion(20, resultado)
    guardar_instruccion(33, izquierda)
    guardar_instruccion(21, resultado)
    guardar_instruccion(20, cuenta)
    guardar_instruccion(31, uno)
    guardar_instruccion(21, cuenta)
    guardar_instruccion(40, inicio)

    error_exponente = contador_instrucciones
    guardar_instruccion(43, 0)
    fin = contador_instrucciones
    if fin > 99:
        raise ValueError("No hay memoria para la potencia")
    memoria[salto_cero] = 4200 + fin
    memoria[salto_negativo] = 4100 + error_exponente
    return resultado


def compilar_expresion(texto):
    tokens = expresiones.separar_expresion(texto)
    postfijo = expresiones.convertir_postfijo(tokens)
    pila = []

    for token in postfijo:
        if token not in ["+", "-", "*", "/", "^"]:
            pila.append(agregar_dato(token))
        else:
            derecha = pila.pop()
            izquierda = pila.pop()

            if token == "^":
                pila.append(compilar_potencia(izquierda, derecha))
            else:
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

    return pila.pop()


def compilar_if(partes):
    if len(partes) != 7 or partes[5] != "goto":
        raise ValueError("If debe tener la forma: if a == b goto 40")

    izquierda = agregar_dato(partes[2])
    operador = partes[3]
    derecha = agregar_dato(partes[4])

    if not partes[6].isdigit():
        raise ValueError("Destino incorrecto en if")
    destino = int(partes[6])

    if operador in ["==", "<", "<=", "!="]:
        guardar_instruccion(20, izquierda)
        guardar_instruccion(31, derecha)
    elif operador in [">", ">="]:
        guardar_instruccion(20, derecha)
        guardar_instruccion(31, izquierda)
    else:
        raise ValueError("Comparacion incorrecta: " + operador)

    if operador == "==":
        guardar_salto(42, destino)
    elif operador == "<" or operador == ">":
        guardar_salto(41, destino)
    elif operador in ["<=", ">="]:
        guardar_salto(41, destino)
        guardar_salto(42, destino)
    else:
        guardar_salto(41, destino)
        guardar_instruccion(20, derecha)
        guardar_instruccion(31, izquierda)
        guardar_salto(41, destino)


def primera_pasada(nombre_archivo):
    global memoria, flags, tabla_simbolos, contador_instrucciones, contador_datos
    memoria = [0] * 100
    flags = [-1] * 100
    tabla_simbolos = []
    contador_instrucciones = 0
    contador_datos = 99

    with open(nombre_archivo, "r", encoding="utf-8") as archivo:
        lineas = archivo.readlines()

    ultimo_numero = -1
    hay_end = False

    for linea in lineas:
        partes = linea.strip().split()
        if len(partes) == 0:
            continue
        if hay_end:
            raise ValueError("No puede haber instrucciones despues de end")
        if len(partes) < 2 or not partes[0].isdigit():
            raise ValueError("Linea Simple incorrecta: " + linea.strip())

        numero = int(partes[0])
        if numero <= ultimo_numero:
            raise ValueError("Los numeros de linea deben ser crecientes")
        ultimo_numero = numero
        comando = partes[1]
        if comando != comando.lower():
            raise ValueError("Los comandos deben escribirse en minusculas")
        agregar_linea(numero)

        if comando == "rem":
            continue
        elif comando == "input":
            if len(partes) != 3:
                raise ValueError("Input necesita una variable")
            posicion = agregar_dato(partes[2])
            if buscar_simbolo(partes[2], "V") == None:
                raise ValueError("Input solo acepta variables")
            guardar_instruccion(10, posicion)
        elif comando == "print":
            if len(partes) != 3:
                raise ValueError("Print necesita un dato")
            guardar_instruccion(11, agregar_dato(partes[2]))
        elif comando == "goto":
            if len(partes) != 3 or not partes[2].isdigit():
                raise ValueError("Goto necesita un numero de linea")
            guardar_salto(40, int(partes[2]))
        elif comando == "if":
            texto_if = " ".join(partes)
            for comparacion in ["<=", ">=", "==", "!=", "<", ">"]:
                if comparacion in texto_if:
                    texto_if = texto_if.replace(comparacion, " " + comparacion + " ")
                    break
            compilar_if(texto_if.split())
        elif comando == "let":
            texto_let = " ".join(partes[2:])
            if "=" not in texto_let:
                raise ValueError("Let debe tener la forma: let a = b + 1")
            trozos = texto_let.split("=", 1)
            variable = trozos[0].strip()
            texto = trozos[1].strip()
            if not expresiones.es_variable(variable):
                raise ValueError("Let necesita una variable")
            posicion_variable = agregar_dato(variable)
            resultado = compilar_expresion(texto)
            guardar_instruccion(20, resultado)
            guardar_instruccion(21, posicion_variable)
        elif comando == "end":
            if len(partes) != 2:
                raise ValueError("End no lleva argumentos")
            guardar_instruccion(43, 0)
            hay_end = True
        else:
            raise ValueError("Comando no reconocido: " + comando)

    if not hay_end:
        raise ValueError("Falta la instruccion end")


def mostrar_primera_pasada():
    print()
    print("TABLA DE SIMBOLOS")
    print("Simbolo\tTipo\tUbicacion")
    for dato in tabla_simbolos:
        print(dato["simbolo"], "\t", dato["tipo"], "\t", dato["ubicacion"])

    print()
    print("INSTRUCCIONES PROVISIONALES")
    for i in range(contador_instrucciones):
        print(str(i).zfill(2), numero_memoria(memoria[i]))

    print()
    print("FLAGS PENDIENTES")
    for i in range(contador_instrucciones):
        if flags[i] != -1:
            print("Posicion", i, "linea pendiente", flags[i])


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


def numero_memoria(numero):
    if numero >= 0:
        return "+" + str(numero).zfill(4)
    return "-" + str(abs(numero)).zfill(4)


def guardar_sml(nombre_archivo):
    with open(nombre_archivo, "w") as archivo:
        for numero in memoria:
            print(numero_memoria(numero), file=archivo)


def mostrar_codigo():
    print()
    print("CODIGO SML FINAL")
    for i in range(contador_instrucciones):
        print(str(i).zfill(2), numero_memoria(memoria[i]))


def compilar(nombre_entrada, nombre_salida):
    primera_pasada(nombre_entrada)
    segunda_pasada()
    guardar_sml(nombre_salida)


if __name__ == "__main__":
    print("COMPILADOR SIMPLE A SML")
    nombre = input("Nombre del archivo Simple: ").strip()
    salida = input("Nombre del archivo SML (Enter para programa.sml): ").strip()
    if salida == "":
        salida = "programa.sml"
    try:
        primera_pasada(nombre)
        mostrar_primera_pasada()
        segunda_pasada()
        mostrar_codigo()
        guardar_sml(salida)
        print()
        print("Archivo", salida, "creado correctamente")
    except (OSError, ValueError, IndexError) as error:
        print("Error:", error)
