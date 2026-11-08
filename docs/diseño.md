# Diseño del proyecto

El proyecto está desarrollado en **Python** y se organiza en cuatro componentes: simulador original, simulador modificado, evaluador de expresiones y compilador Simple a SML.

## 1. Arquitectura del sistema

```text
src/
├── simpletron/
│   ├── Un_simulador_de_Computadora.py
│   └── Modificaciones_al_simulador_de_Simpletron.py
├── expresiones/
│   └── expresiones.py
└── compilador/
    └── compilador.py
```

Cada archivo contiene funciones específicas para realizar las operaciones correspondientes.

## 2. Simulador Simpletron original

El simulador utiliza una lista de **100 posiciones** para representar la memoria:

```python
memory = [0] * 100
```

### Registros

- `accumulator`: almacena los resultados.
- `instructionCounter`: indica la siguiente instrucción.
- `instructionRegister`: contiene la instrucción actual.
- `operationCode`: identifica la operación.
- `operand`: contiene la dirección del operando.

### Ejecución

Las instrucciones se dividen en código de operación y operando:

```python
operationCode = instructionRegister // 100
operand = instructionRegister % 100
```

El simulador obtiene, decodifica y ejecuta cada instrucción. El proceso continúa hasta encontrar `HALT` o detectar un error fatal.

Al finalizar, muestra los registros y el contenido de memoria.

## 3. Simulador modificado

La versión modificada amplía la memoria:

```python
memory = [0] * 1000
```

Permite ejecutar instrucciones originales de cuatro dígitos y extendidas de cinco dígitos.

En el formato extendido, la decodificación utiliza:

```python
operationCode = instructionRegister // 1000
operand = instructionRegister % 1000
```

Se incorporan operaciones de módulo, potencia, salto de línea, lectura y escritura de cadenas y números decimales.

Las cadenas se almacenan mediante códigos ASCII, utilizando `ord()` y `chr()`.

## 4. Evaluador de expresiones

El evaluador utiliza funciones independientes para procesar expresiones aritméticas.

- `separar_expresion()`: identifica operandos y operadores.
- `validar_agrupacion()`: comprueba los símbolos y calcula el anidamiento.
- `convertir_postfijo()`: transforma expresiones infijas a postfijas.
- `evaluar_postfijo()`: calcula el resultado utilizando una pila.

El programa respeta la precedencia de los operadores y permite trabajar con números de varios dígitos.

## 5. Compilador Simple a SML

El compilador utiliza una memoria de **100 posiciones**.

Las instrucciones se almacenan desde la posición `0`, mientras que las variables, constantes y datos temporales se asignan desde la posición `99`.

### Primera pasada

La función `primera_pasada()`:

1. Lee el programa Simple.
2. Identifica instrucciones, variables y constantes.
3. Construye la tabla de símbolos.
4. Genera instrucciones provisionales.
5. Registra referencias pendientes en `flags`.

### Segunda pasada

La función `segunda_pasada()`:

1. Revisa las referencias pendientes.
2. Busca los destinos en la tabla de símbolos.
3. Completa las instrucciones SML.

### Generación del archivo

La función `guardar_sml()` genera un archivo `.sml` que puede ejecutarse en el simulador original.

Las expresiones aritméticas se convierten a postfijas antes de generar las instrucciones correspondientes.

## 6. Integración de los componentes

El funcionamiento general sigue este orden:

1. El usuario escribe un programa en Simple.
2. El compilador convierte el programa a SML.
3. Se genera un archivo `.sml`.
4. El simulador carga las instrucciones.
5. Simpletron ejecuta el programa y muestra los resultados.

El evaluador de expresiones permite comprobar las operaciones aritméticas utilizadas durante el proceso.

## 7. Conclusión

El proyecto separa las funciones de simulación, evaluación de expresiones y compilación mediante archivos independientes.

Esta organización facilita la comprensión del funcionamiento interno, la ejecución de programas y la incorporación de modificaciones.
