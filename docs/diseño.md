# Diseño del proyecto

El proyecto se divide en cuatro componentes principales:

1. Simulador Simpletron original.
2. Simulador Simpletron modificado.
3. Evaluador de expresiones aritméticas.
4. Compilador del lenguaje Simple a SML.

Cada componente se encuentra en un archivo independiente para facilitar su organización y funcionamiento.

## 1. Arquitectura del proyecto

El código fuente se organiza de la siguiente manera:

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

### Responsabilidad de cada componente

| Componente | Función |
|---|---|
| Simulador original | Ejecutar instrucciones SML |
| Simulador modificado | Ejecutar SML e instrucciones adicionales |
| Evaluador | Validar y evaluar expresiones aritméticas |
| Compilador | Traducir programas Simple a SML |

## 2. Diseño del simulador original

El simulador utiliza una lista llamada `memory` para representar la memoria de una computadora.

```python
memory = [0] * 100
```

La memoria contiene **100 posiciones**, inicialmente con valor cero.

### Registros

Se utilizan cinco registros principales:

- `accumulator`: almacena resultados de operaciones.
- `instructionCounter`: indica la siguiente instrucción.
- `instructionRegister`: almacena la instrucción actual.
- `operationCode`: identifica la operación.
- `operand`: contiene la dirección del operando.

Todos los registros se inicializan en `0`.

### Formato de instrucciones

Cada instrucción SML original utiliza cuatro dígitos.

Por ejemplo:

```text
1090
```

- `10`: código de operación `READ`.
- `90`: dirección de memoria.

El simulador obtiene estos valores mediante división entera y módulo:

```python
operationCode = instructionRegister // 100
operand = instructionRegister % 100
```

### Ciclo de ejecución

El funcionamiento se divide en cuatro etapas:

1. Obtener la instrucción de memoria.
2. Separar el código de operación y el operando.
3. Ejecutar la operación correspondiente.
4. Actualizar `instructionCounter`.

El ciclo continúa hasta ejecutar `HALT` o encontrar un error fatal.

### Manejo de errores

El simulador utiliza condiciones para detectar:

- División entre cero.
- Operaciones inválidas.
- Desbordamiento del acumulador.
- Direcciones fuera de los límites.
- Valores incorrectos.

Al finalizar, muestra los registros y las 100 posiciones de memoria.

## 3. Diseño del simulador modificado

El simulador modificado conserva la estructura original, pero amplía la memoria:

```python
memory = [0] * 1000
```

### Formatos de instrucciones

El simulador admite dos formatos:

| Archivo | Memoria utilizada | Formato |
|---|---|---|
| `.sml` | 100 posiciones | Cuatro dígitos |
| `.simp` | 1000 posiciones | Cinco dígitos |

Para distinguir el código de operación y el operando se utiliza la variable `ancho`.

En el formato extendido:

```python
operationCode = instructionRegister // 1000
operand = instructionRegister % 1000
```

### Nuevas operaciones

Se incorporan las instrucciones:

- `34`: módulo.
- `35`: potencia.
- `44`: salto de línea.
- `45`: lectura de cadenas.
- `46`: escritura de cadenas.
- `47`: lectura de decimales.
- `48`: escritura de decimales.

### Almacenamiento de cadenas

Las cadenas se almacenan utilizando códigos ASCII.

- La primera posición guarda la longitud de la cadena.
- Las siguientes posiciones almacenan los caracteres.
- Cada carácter se convierte mediante `ord()`.
- Para mostrar los caracteres se utiliza `chr()`.

### Manejo de decimales

Los valores decimales se convierten utilizando `float()` y se almacenan en memoria.

El simulador valida el formato y el rango de los valores introducidos.

## 4. Diseño del evaluador de expresiones

El evaluador se organiza mediante funciones que realizan distintas operaciones.

### Separación de elementos

La función `separar_expresion()` identifica:

- Números.
- Variables.
- Operadores.
- Símbolos de agrupación.

### Validación de agrupación

La función `validar_agrupacion()` utiliza una pila para comprobar paréntesis, corchetes y llaves.

También calcula la profundidad máxima de anidamiento.

### Conversión infija a postfija

La función `convertir_postfijo()` utiliza una pila de operadores.

Durante la conversión se respeta la precedencia:

1. Potencia.
2. Multiplicación y división.
3. Suma y resta.

Los símbolos de agrupación determinan el orden de las operaciones.

### Evaluación postfija

La función `evaluar_postfijo()` utiliza una pila de operandos.

Cuando encuentra un operador:

1. Extrae los operandos necesarios.
2. Realiza la operación.
3. Guarda el resultado en la pila.

Al terminar, el valor restante corresponde al resultado de la expresión.

## 5. Diseño del compilador

El compilador transforma programas escritos en **Simple** a instrucciones **SML**.

Utiliza una memoria de 100 posiciones:

```python
memoria = [0] * 100
```

### Organización de memoria

El compilador utiliza dos contadores:

- `contador_instrucciones`: comienza en la posición `0`.
- `contador_datos`: comienza en la posición `99`.

Las instrucciones se almacenan desde el inicio de la memoria y los datos desde el final.

Esto permite mantener separadas ambas áreas.

### Tabla de símbolos

La tabla de símbolos almacena información sobre los elementos encontrados en el programa.

Cada registro contiene:

- `simbolo`: identificador del elemento.
- `tipo`: clasificación del símbolo.
- `ubicacion`: posición de memoria.

Los tipos utilizados son:

- `L`: número de línea.
- `V`: variable.
- `C`: constante.

### Primera pasada

La función `primera_pasada()`:

1. Lee el archivo Simple.
2. Identifica los números de línea.
3. Reconoce comandos, variables y constantes.
4. Construye la tabla de símbolos.
5. Genera instrucciones provisionales.
6. Registra referencias pendientes.

Las referencias pendientes se almacenan en el arreglo `flags`.

### Segunda pasada

La función `segunda_pasada()`:

1. Revisa el arreglo `flags`.
2. Busca las líneas pendientes en la tabla de símbolos.
3. Obtiene sus direcciones.
4. Completa las instrucciones SML.

### Compilación de expresiones

El compilador utiliza funciones para convertir expresiones infijas a postfijas.

Posteriormente genera instrucciones SML para realizar las operaciones.

Para la potencia se genera una secuencia de instrucciones que realiza multiplicaciones repetidas.

### Generación del archivo

La función `guardar_sml()` almacena el resultado en un archivo `.sml`.

El archivo contiene instrucciones de cuatro dígitos y puede ejecutarse en el simulador original.

## 6. Integración de los componentes

El funcionamiento general del proyecto sigue este proceso:

1. El usuario escribe un programa en lenguaje Simple.
2. El compilador lee y procesa el programa.
3. Se genera un archivo con instrucciones SML.
4. El simulador carga el archivo generado.
5. Simpletron ejecuta las instrucciones.
6. Se muestran los resultados y el estado de la memoria.

El evaluador de expresiones permite comprobar las operaciones aritméticas y utiliza procedimientos equivalentes a los empleados durante la compilación.

## 7. Programas de prueba

Los programas están organizados en dos carpetas:

```text
programas/
├── simple/
│   ├── secuencia.simple
│   ├── seleccion.simple
│   └── repeticion.simple
└── sml/
    ├── secuencia.sml
    ├── seleccion.sml
    ├── repeticion.sml
    ├── Mod_Potencia.simp
    └── Cadenas_Decimales.simp
```

Los programas permiten comprobar:

- Ejecución secuencial.
- Selección mediante condiciones.
- Repetición mediante saltos.
- Operaciones de módulo y potencia.
- Entrada y salida de cadenas.
- Entrada y salida de números decimales.

## 8. Conclusión

El diseño del proyecto separa las responsabilidades de cada componente mediante archivos y funciones independientes.

El simulador ejecuta las instrucciones de máquina, el evaluador procesa expresiones y el compilador transforma programas Simple en instrucciones SML.

Esta organización facilita la comprensión, las pruebas y las modificaciones del sistema.
