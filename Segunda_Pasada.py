import primera_pasada


def segunda_pasada():
    i = 0

    while i < primera_pasada.contador_instrucciones:
        numero_linea = primera_pasada.flags[i]

        if numero_linea != -1:
            dato = primera_pasada.buscar_simbolo(numero_linea, "L")

            if dato == None:
                print("Error: no existe la linea", numero_linea)
                return False

            ubicacion = dato["ubicacion"]

            codigo = primera_pasada.memoria[i] // 100
            primera_pasada.memoria[i] = codigo * 100 + ubicacion
            primera_pasada.flags[i] = -1

        i = i + 1

    return True


def guardar_archivo():
    archivo = open("programa.sml", "w")

    i = 0
    while i < 100:
        numero = primera_pasada.memoria[i]

        if numero >= 0:
            archivo.write("+" + str(numero).zfill(4) + "\n")
        else:
            archivo.write("-" + str(abs(numero)).zfill(4) + "\n")

        i = i + 1

    archivo.close()
    print("\nArchivo programa.sml creado correctamente")


def mostrar_resultado():
    print("\nCODIGO SML FINAL")

    i = 0
    while i < primera_pasada.contador_instrucciones:
        numero = primera_pasada.memoria[i]
        print(i, "+" + str(numero).zfill(4))
        i = i + 1


print("SEGUNDA PASADA DEL COMPILADOR")
nombre = input("Nombre del archivo Simple: ")

try:
    primera_pasada.primera_pasada(nombre)
    print("\nPrimera pasada terminada")

    correcto = segunda_pasada()
    if correcto == True:
        print("Segunda pasada terminada")
        mostrar_resultado()
        guardar_archivo()

except (FileNotFoundError, ValueError, IndexError) as error:
    print("Error:", error)
