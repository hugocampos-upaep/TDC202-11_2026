memory = [0] * 1000
accumulator = 0
instructionCounter = 0
instructionRegister = 0
operationCode = 0
operand = 0
ancho = 1000
limite = 1000

def reiniciar():
    global memory, accumulator, instructionCounter, instructionRegister, operationCode, operand, ancho, limite
    memory = [0] * 1000
    accumulator = 0
    instructionCounter = 0
    instructionRegister = 0
    operationCode = 0
    operand = 0
    ancho = 1000
    limite = 1000

def es_entero(texto):
    if texto == "":
        return False
    if texto[0] == "+" or texto[0] == "-":
        texto = texto[1:]
    return texto.isdigit()

def es_decimal(texto):
    if texto == "":
        return False
    if texto[0] == "+" or texto[0] == "-":
        texto = texto[1:]
    if texto.count(".") > 1:
        return False
    texto = texto.replace(".", "")
    return texto.isdigit()

def cargar_teclado():
    global ancho, limite
    ancho = 1000
    limite = 1000
    print("Introduce las instrucciones una por una")
    print("Escribe 9999 para terminar la carga")
    posicion = 0
    while posicion < 1000:
        texto = input(str(posicion) + " ? ")
        if not es_entero(texto):
            print("Debes introducir un entero")
            continue
        valor = int(texto)
        if valor == 9999:
            break
        if valor < -99999 or valor > 99999:
            print("Valor fuera de rango")
        else:
            memory[posicion] = valor
            posicion = posicion + 1
    return posicion > 0

def cargar_archivo(nombre):
    global ancho, limite
    ancho = 1000
    limite = 1000
    maximo = 99999
    if nombre.lower().endswith(".sml"):
        ancho = 100
        limite = 100
        maximo = 9999
    try:
        archivo = open(nombre, "r")
    except OSError:
        print("No se pudo abrir el archivo")
        return False
    posicion = 0
    for linea in archivo:
        texto = linea.strip()
        if texto == "":
            continue
        if not es_entero(texto):
            print("Error: palabra incorrecta en el archivo")
            archivo.close()
            return False
        valor = int(texto)
        if posicion >= limite or valor < -maximo or valor > maximo:
            print("Error: memoria llena o valor fuera de rango")
            archivo.close()
            return False
        memory[posicion] = valor
        posicion = posicion + 1
    archivo.close()
    if posicion == 0:
        print("Error: archivo vacio")
        return False
    print("Programa cargado desde", nombre)
    return True

def leer_cadena(posicion):
    cadena = input("Cadena: ")
    if posicion + len(cadena) >= limite:
        print("Error: la cadena no cabe en memoria")
        return False
    for letra in cadena:
        if ord(letra) > 127:
            print("Error: solo se permite ASCII")
            return False
    memory[posicion] = len(cadena)
    for i in range(len(cadena)):
        memory[posicion + i + 1] = ord(cadena[i])
    return True

def escribir_cadena(posicion):
    longitud = memory[posicion]
    if type(longitud) != int or longitud < 0 or posicion + longitud >= limite:
        print("Error: longitud de cadena invalida")
        return False
    cadena = ""
    for i in range(longitud):
        codigo = memory[posicion + i + 1]
        if type(codigo) != int or codigo < 0 or codigo > 127:
            print("Error: codigo ASCII invalido")
            return False
        cadena = cadena + chr(codigo)
    print(cadena)
    return True

def ejecutar_programa():
    global accumulator, instructionCounter, instructionRegister, operationCode, operand
    ejecutando = True
    pasos = 0
    maximo = 99999
    if ancho == 100:
        maximo = 9999
    while ejecutando:
        if pasos >= 100000:
            print("Error: limite de instrucciones alcanzado")
            break
        pasos = pasos + 1
        if instructionCounter < 0 or instructionCounter >= limite:
            print("Error: direccion invalida")
            break
        instructionRegister = memory[instructionCounter]
        if type(instructionRegister) != int or instructionRegister < 0 or instructionRegister > ancho * 100 - 1:
            print("Error: instruccion invalida")
            break
        operationCode = instructionRegister // ancho
        operand = instructionRegister % ancho
        if operationCode == 10:
            texto = input("? ")
            if not es_entero(texto):
                print("Error: se necesita un entero")
                break
            valor = int(texto)
            if valor < -maximo or valor > maximo:
                print("Error: dato fuera de rango")
                break
            memory[operand] = valor
            instructionCounter = instructionCounter + 1
        elif operationCode == 11:
            print(memory[operand])
            instructionCounter = instructionCounter + 1
        elif operationCode == 20:
            accumulator = memory[operand]
            instructionCounter = instructionCounter + 1
        elif operationCode == 21:
            memory[operand] = accumulator
            instructionCounter = instructionCounter + 1
        elif operationCode == 30 or operationCode == 31 or operationCode == 32 or operationCode == 33 or operationCode == 34 or operationCode == 35:
            dato = memory[operand]
            if operationCode == 30:
                resultado = accumulator + dato
            elif operationCode == 31:
                resultado = accumulator - dato
            elif operationCode == 32:
                if dato == 0:
                    print("Error: division entre cero")
                    break
                resultado = int(accumulator / dato)
            elif operationCode == 33:
                resultado = accumulator * dato
            elif operationCode == 34:
                if dato == 0:
                    print("Error: modulo entre cero")
                    break
                resultado = accumulator % dato
            else:
                if type(dato) != int or dato < 0:
                    print("Error: exponente invalido")
                    break
                resultado = 1
                for i in range(dato):
                    resultado = resultado * accumulator
                    if resultado < -maximo or resultado > maximo:
                        break
            if resultado < -maximo or resultado > maximo:
                print("Error: desbordamiento del acumulador")
                break
            accumulator = resultado
            instructionCounter = instructionCounter + 1
        elif operationCode == 40:
            instructionCounter = operand
        elif operationCode == 41:
            if accumulator < 0:
                instructionCounter = operand
            else:
                instructionCounter = instructionCounter + 1
        elif operationCode == 42:
            if accumulator == 0:
                instructionCounter = operand
            else:
                instructionCounter = instructionCounter + 1
        elif operationCode == 43:
            print("Terminó la ejecución de Simpletron")
            ejecutando = False
        elif operationCode == 44:
            print()
            instructionCounter = instructionCounter + 1
        elif operationCode == 45:
            if not leer_cadena(operand):
                break
            instructionCounter = instructionCounter + 1
        elif operationCode == 46:
            if not escribir_cadena(operand):
                break
            instructionCounter = instructionCounter + 1
        elif operationCode == 47:
            texto = input("Decimal: ")
            if not es_decimal(texto):
                print("Error: decimal invalido")
                break
            valor = float(texto)
            if valor < -maximo or valor > maximo:
                print("Error: decimal fuera de rango")
                break
            memory[operand] = valor
            instructionCounter = instructionCounter + 1
        elif operationCode == 48:
            print(memory[operand])
            instructionCounter = instructionCounter + 1
        else:
            print("Error: codigo de operacion invalido")
            break

def vaciado_memoria():
    print("REGISTROS")
    print("accumulator:", accumulator)
    print("instructionCounter:", instructionCounter)
    print("instructionRegister:", instructionRegister)
    print("operationCode:", operationCode)
    print("operand:", operand)
    print("MEMORIA")
    print("      0        1        2        3        4        5        6        7        8        9")
    for fila in range(100):
        print(str(fila * 10).zfill(3), end=": ")
        for columna in range(10):
            posicion = fila * 10 + columna
            print(str(memory[posicion]).rjust(7), end="  ")
        print()

if __name__ == "__main__":
    reiniciar()
    print("*** Bienvenido a Simpletron ***")
    opcion = input("1. Cargar archivo  2. Cargar por teclado: ")
    if opcion == "2":
        cargado = cargar_teclado()
    else:
        nombre = input("Nombre del archivo (Enter para programa.simp): ").strip()
        if nombre == "":
            nombre = "programa.simp"
        cargado = cargar_archivo(nombre)
    if cargado:
        ejecutar_programa()
    vaciado_memoria()
