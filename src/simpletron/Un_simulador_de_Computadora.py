memory = [0] * 100

accumulator = 0
instructionCounter = 0
instructionRegister = 0
operationCode = 0
operand = 0


def reiniciar():
    global memory, accumulator, instructionCounter, instructionRegister, operationCode, operand

    memory = [0] * 100
    accumulator = 0
    instructionCounter = 0
    instructionRegister = 0
    operationCode = 0
    operand = 0


def numero_memoria(numero):
    texto = str(abs(numero))

    while len(texto) < 4:
        texto = "0" + texto

    if numero < 0:
        return "-" + texto
    else:
        return "+" + texto


def es_entero(texto):
    if texto == "":
        return False

    if texto[0] == "+" or texto[0] == "-":
        texto = texto[1:]

    return texto.isdigit()


def cargar_teclado():
    reiniciar()

    print("*** Bienvenido a Simpletron ***")
    print("Introduce las instrucciones una por una")
    print("Escribe 9999 para terminar la carga")

    posicion = 0

    while posicion < 100:
        texto = input(str(posicion).zfill(2) + " ? ")

        if not es_entero(texto):
            print("Debes escribir un numero entero")
            continue

        valor = int(texto)

        if valor == 9999:
            break

        if valor < -9999 or valor > 9999:
            print("Valor fuera de rango")
        else:
            memory[posicion] = valor
            posicion = posicion + 1

    return posicion > 0


def cargar_archivo(nombre):
    reiniciar()
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
            print("Instruccion incorrecta en el archivo")
            archivo.close()
            return False

        valor = int(texto)

        if posicion >= 100:
            print("El archivo supera las 100 posiciones")
            archivo.close()
            return False

        if valor < -9999 or valor > 9999:
            print("Valor fuera de rango en el archivo")
            archivo.close()
            return False

        memory[posicion] = valor
        posicion = posicion + 1

    archivo.close()

    if posicion == 0:
        print("El archivo esta vacio")
        return False

    print("Programa cargado correctamente")
    return True


def ejecutar_programa():
    global accumulator, instructionCounter, instructionRegister, operationCode, operand

    ejecutando = True

    while ejecutando:
        if instructionCounter < 0 or instructionCounter >= 100:
            print("Error: direccion de instruccion invalida")
            break

        instructionRegister = memory[instructionCounter]

        if instructionRegister < 0 or instructionRegister > 9999:
            print("Error: instruccion SML invalida")
            break

        operationCode = instructionRegister // 100
        operand = instructionRegister % 100

        if operationCode == 10:
            texto = input("? ")
            if not es_entero(texto):
                print("Error: debes introducir un entero")
                break

            valor = int(texto)

            if valor < -9999 or valor > 9999:
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

        elif operationCode == 30 or operationCode == 31 or operationCode == 32 or operationCode == 33:
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
            else:
                resultado = accumulator * dato

            if resultado < -9999 or resultado > 9999:
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

        else:
            print("Error: codigo de operacion invalido")
            break


def vaciado_memoria():
    print("REGISTROS")
    print("accumulator:        ", numero_memoria(accumulator))
    print("instructionCounter: ", str(instructionCounter).zfill(2))
    print("instructionRegister:", numero_memoria(instructionRegister))
    print("operationCode:      ", str(operationCode).zfill(2))
    print("operand:            ", str(operand).zfill(2))

    print("MEMORIA")
    print("       0      1      2      3      4      5      6      7      8      9")

    for fila in range(10):
        print(str(fila * 10).zfill(2), end=" ")

        for columna in range(10):
            posicion = fila * 10 + columna
            print(numero_memoria(memory[posicion]), end=" ")

        print()


if __name__ == "__main__":
    reiniciar()
    opcion = input("1. Cargar archivo  2. Cargar por teclado: ")
    if opcion == "2":
        cargado = cargar_teclado()
    else:
        nombre = input("Nombre del archivo (Enter para programa.sml): ").strip()
        if nombre == "":
            nombre = "programa.sml"
        cargado = cargar_archivo(nombre)

    if cargado:
        ejecutar_programa()

    vaciado_memoria()
