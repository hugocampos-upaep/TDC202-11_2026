memory = [0] * 100

accumulator = 0
instructionCounter = 0
instructionRegister = 0
operationCode = 0
operand = 0


def numero_memoria(numero):
    if numero < 0:
        signo = "-"
        numero = numero * -1
    else:
        signo = "+"

    texto = str(numero)

    while len(texto) < 4:
        texto = "0" + texto

    return signo + texto


def numero_dos_digitos(numero):
    texto = str(numero)

    if numero < 10:
        texto = "0" + texto

    return texto


def es_numero(entrada):
    if entrada == "":
        return False

    inicio = 0

    if entrada[0] == "+" or entrada[0] == "-":
        inicio = 1

    if inicio == len(entrada):
        return False

    i = inicio

    while i < len(entrada):

        if entrada[i] < "0" or entrada[i] > "9":
            return False

        i = i + 1

    return True


def cargar_programa():
    posicion = 0
    cargando = True

    print("*** Bienvenido a Simpletron! ***")
    print("*** Introduzca su programa una instrucción ***")
    print("*** (o palabra de datos) a la vez en la línea ***")
    print("*** de texto de entrada. Yo indicaré el número ***")
    print("*** de posición y una interrogación (?). Usted ***")
    print("*** tecleará entonces la palabra para esa ***")
    print("*** posición. Introduzca 9999 para dejar de ***")
    print("*** introducir su programa. ***")

    while cargando == True and posicion < 100:

        if posicion < 10:
            print("0", posicion, " ? ", sep="", end="")
        else:
            print(posicion, " ? ", sep="", end="")

        entrada = input()

        if es_numero(entrada) == True:

            valor = int(entrada)

            if valor == 9999:
                cargando = False

            elif valor >= -9999 and valor <= 9998:
                memory[posicion] = valor
                posicion = posicion + 1

            else:
                print("Valor inválido")
                print("Introduzca un valor entre -9999 y +9998")

        else:
            print("Entrada inválida")

    if posicion == 100 and cargando == True:
        print("La memoria está llena")

    print()
    print("Se terminó de cargar el programa")
    print("Comienza la ejecución del programa")
    print()


def ejecutar_programa():
    global accumulator
    global instructionCounter
    global instructionRegister
    global operationCode
    global operand

    ejecutando = True

    while ejecutando == True:

        if instructionCounter < 0 or instructionCounter > 99:

            print("Contador de instrucciones fuera de memoria")
            print("La ejecución de Simpletron terminó anormalmente")

            ejecutando = False

        else:

            instructionRegister = memory[instructionCounter]

            if instructionRegister < 0:

                print("Instrucción inválida")
                print("La ejecución de Simpletron terminó anormalmente")

                ejecutando = False

            else:

                operationCode = instructionRegister // 100
                operand = instructionRegister % 100

                if operationCode == 10:

                    datoValido = False

                    while datoValido == False:

                        print("? ", end="")
                        entrada = input()

                        if es_numero(entrada) == True:

                            dato = int(entrada)

                            if dato >= -9999 and dato <= 9998:

                                memory[operand] = dato
                                datoValido = True

                            else:

                                print("Dato fuera del rango permitido")
                                print("Introduzca un valor entre -9999 y +9998")

                        else:

                            print("Entrada inválida")

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


                elif operationCode == 30:

                    resultado = accumulator + memory[operand]

                    if resultado > 9999 or resultado < -9999:

                        print("Desbordamiento del acumulador")
                        print("La ejecución de Simpletron terminó anormalmente")

                        ejecutando = False

                    else:

                        accumulator = resultado
                        instructionCounter = instructionCounter + 1


                elif operationCode == 31:

                    resultado = accumulator - memory[operand]

                    if resultado > 9999 or resultado < -9999:

                        print("Desbordamiento del acumulador")
                        print("La ejecución de Simpletron terminó anormalmente")

                        ejecutando = False

                    else:

                        accumulator = resultado
                        instructionCounter = instructionCounter + 1


                elif operationCode == 32:

                    if memory[operand] == 0:

                        print("Intento de dividir entre cero")
                        print("La ejecución de Simpletron terminó anormalmente")

                        ejecutando = False

                    else:

                        resultado = int(accumulator / memory[operand])

                        if resultado > 9999 or resultado < -9999:

                            print("Desbordamiento del acumulador")
                            print("La ejecución de Simpletron terminó anormalmente")

                            ejecutando = False

                        else:

                            accumulator = resultado
                            instructionCounter = instructionCounter + 1


                elif operationCode == 33:

                    resultado = accumulator * memory[operand]

                    if resultado > 9999 or resultado < -9999:

                        print("Desbordamiento del acumulador")
                        print("La ejecución de Simpletron terminó anormalmente")

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

                    print()
                    print("Terminó la ejecución de Simpletron")

                    ejecutando = False


                else:

                    print("Código de operación inválido")
                    print("La ejecución de Simpletron terminó anormalmente")

                    ejecutando = False


def vaciado_memoria():
    print()
    print("REGISTROS:")
    print("accumulator:         ", numero_memoria(accumulator))
    print("instructionCounter:  ", numero_dos_digitos(instructionCounter))
    print("instructionRegister: ", numero_memoria(instructionRegister))
    print("operationCode:       ", numero_dos_digitos(operationCode))
    print("operand:             ", numero_dos_digitos(operand))

    print()
    print("MEMORIA")
    print()

    print("       0      1      2      3      4      5      6      7      8      9")

    fila = 0

    while fila < 10:

        print(fila, " ", sep="", end="")

        columna = 0

        while columna < 10:

            posicion = fila * 10 + columna

            print(numero_memoria(memory[posicion]), " ", sep="", end="")

            columna = columna + 1

        print()

        fila = fila + 1


cargar_programa()
ejecutar_programa()
vaciado_memoria()