memory = [0] * 1000

accumulator = 0
instructionCounter = 0
instructionRegister = 0
operationCode = 0
operand = 0


def cargar_teclado():
    posicion = 0
    cargando = True

    print("*** Bienvenido a Simpletron! ***")
    print("*** Introduzca su programa una instrucción ***")
    print("*** a la vez. Introduzca 9999 para terminar. ***")

    while cargando == True and posicion < 1000:

        print(posicion, "? ", end="")

        valor = int(input())

        if valor == 9999:
            cargando = False

        elif valor >= -99999 and valor <= 99999:
            memory[posicion] = valor
            posicion = posicion + 1

        else:
            print("Valor fuera del rango permitido")


def cargar_archivo():
    try:
        archivo = open("programa.simp", "r")
    except:
        print("No se encontró programa.simp")
        print("Se utilizará la carga por teclado")
        cargar_teclado()
        return

    posicion = 0

    for linea in archivo:

        valor = int(linea)

        if valor == 9999:
            break

        if posicion < 1000:
            memory[posicion] = valor
            posicion = posicion + 1

    archivo.close()

    print("Programa cargado desde programa.simp")


def leer_cadena(posicion):
    print("Cadena: ", end="")
    cadena = input()

    longitud = len(cadena)

    memory[posicion] = longitud * 1000

    i = 0

    while i < longitud:

        codigo = ord(cadena[i])

        memory[posicion + i + 1] = (i + 1) * 1000 + codigo

        i = i + 1


def escribir_cadena(posicion):
    longitud = memory[posicion] // 1000

    i = 0

    while i < longitud:

        valor = memory[posicion + i + 1]

        codigo = valor % 1000

        print(chr(codigo), end="")

        i = i + 1

    print()


def ejecutar_programa():
    global accumulator
    global instructionCounter
    global instructionRegister
    global operationCode
    global operand

    ejecutando = True

    print()
    print("Comienza la ejecución del programa")
    print()

    while ejecutando == True:

        if instructionCounter < 0 or instructionCounter > 999:

            print("Contador de instrucciones fuera de memoria")
            ejecutando = False

        else:

            instructionRegister = int(memory[instructionCounter])

            operationCode = instructionRegister // 1000
            operand = instructionRegister % 1000


            if operationCode == 10:

                print("? ", end="")
                valor = int(input())

                if valor >= -99999 and valor <= 99999:

                    memory[operand] = valor
                    instructionCounter = instructionCounter + 1

                else:

                    print("Valor fuera del rango permitido")
                    ejecutando = False


            elif operationCode == 11:

                print(memory[operand])

                instructionCounter = instructionCounter + 1


            elif operationCode == 20:

                accumulator = memory[operand]

                instructionCounter = instructionCounter + 1


            elif operationCode == 21:

                memory[operand] = accumulator

                instructionCounter = instructionCounter + 1


            elif operationCode == 30:

                resultado = accumulator + memory[operand]

                if resultado > 99999 or resultado < -99999:

                    print("Desbordamiento del acumulador")
                    ejecutando = False

                else:

                    accumulator = resultado
                    instructionCounter = instructionCounter + 1


            elif operationCode == 31:

                resultado = accumulator - memory[operand]

                if resultado > 99999 or resultado < -99999:

                    print("Desbordamiento del acumulador")
                    ejecutando = False

                else:

                    accumulator = resultado
                    instructionCounter = instructionCounter + 1


            elif operationCode == 32:

                if memory[operand] == 0:

                    print("Intento de dividir entre cero")
                    ejecutando = False

                else:

                    accumulator = accumulator / memory[operand]

                    instructionCounter = instructionCounter + 1


            elif operationCode == 33:

                resultado = accumulator * memory[operand]

                if resultado > 99999 or resultado < -99999:

                    print("Desbordamiento del acumulador")
                    ejecutando = False

                else:

                    accumulator = resultado
                    instructionCounter = instructionCounter + 1


            elif operationCode == 34:

                if memory[operand] == 0:

                    print("No se puede calcular módulo entre cero")
                    ejecutando = False

                else:

                    accumulator = accumulator % memory[operand]

                    instructionCounter = instructionCounter + 1


            elif operationCode == 35:

                exponente = int(memory[operand])

                if exponente < 0:

                    print("Exponente no válido")
                    ejecutando = False

                else:

                    resultado = 1
                    contador = 0

                    while contador < exponente:

                        resultado = resultado * accumulator
                        contador = contador + 1

                    if resultado > 99999 or resultado < -99999:

                        print("Desbordamiento del acumulador")
                        ejecutando = False

                    else:

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

                leer_cadena(operand)

                instructionCounter = instructionCounter + 1


            elif operationCode == 46:

                escribir_cadena(operand)

                instructionCounter = instructionCounter + 1


            elif operationCode == 47:

                print("? ", end="")

                valor = float(input())

                memory[operand] = valor

                instructionCounter = instructionCounter + 1


            elif operationCode == 48:

                print(memory[operand])

                instructionCounter = instructionCounter + 1


            else:

                print("Código de operación inválido")
                ejecutando = False


def vaciado_memoria():
    print()
    print("REGISTROS")

    print("accumulator:", accumulator)
    print("instructionCounter:", instructionCounter)
    print("instructionRegister:", instructionRegister)
    print("operationCode:", operationCode)
    print("operand:", operand)

    print()
    print("MEMORIA")

    posicion = 0

    while posicion < 1000:

        print(posicion, ": ", end="")

        columna = 0

        while columna < 10 and posicion < 1000:

            print(memory[posicion], " ", end="")

            posicion = posicion + 1
            columna = columna + 1

        print()


cargar_archivo()
ejecutar_programa()
vaciado_memoria()