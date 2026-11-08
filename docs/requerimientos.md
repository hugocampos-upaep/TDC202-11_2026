# Requerimientos del proyecto

El sistema permite ejecutar instrucciones en lenguaje de máquina **SML**, evaluar expresiones aritméticas y compilar programas escritos en lenguaje **Simple**.

## 1. Programación en lenguaje SML

El sistema debe implementar las 12 instrucciones originales SML:

- **Entrada y salida:** `READ`, `WRITE`.
- **Carga y almacenamiento:** `LOAD`, `STORE`.
- **Operaciones aritméticas:** `ADD`, `SUBTRACT`, `DIVIDE`, `MULTIPLY`.
- **Transferencias de control:** `BRANCH`, `BRANCHNEG`, `BRANCHZERO`.
- **Terminación:** `HALT`.

También debe permitir:

- Separar el área de instrucciones y el área de datos.
- Ejecutar programas secuenciales.
- Implementar estructuras de selección.
- Implementar estructuras de repetición.

## 2. Simulador de computadora Simpletron

Archivo: `Un_simulador_de_Computadora.py`

El simulador debe:

- Contar con una memoria de **100 posiciones**.
- Inicializar los registros especiales en cero.
- Cargar instrucciones SML desde teclado o archivo.
- Permitir finalizar la carga manual mediante `9999`.
- Ejecutar el ciclo de búsqueda, decodificación y ejecución.
- Actualizar el contador de instrucciones.
- Detectar errores fatales.
- Mostrar el vaciado de registros y memoria.

### Registros especiales

- `accumulator`
- `instructionCounter`
- `instructionRegister`
- `operationCode`
- `operand`

### Errores fatales

- División entre cero.
- Código de operación inválido.
- Desbordamiento del acumulador.
- Dirección inválida.
- Valores fuera del rango permitido.

## 3. Modificaciones al simulador

Archivo: `Modificaciones_al_simulador_de_Simpletron.py`

El simulador modificado debe:

- Extender la memoria hasta **1000 posiciones**.
- Cargar programas desde archivos `.sml` y `.simp`.
- Mantener compatibilidad con las instrucciones originales.
- Implementar nuevas instrucciones SML.
- Detectar errores durante la ejecución.
- Mostrar registros y memoria.

### Nuevas instrucciones

| Código | Operación |
|---|---|
| `34` | Módulo |
| `35` | Potencia |
| `44` | Salto de línea |
| `45` | Lectura de cadenas |
| `46` | Escritura de cadenas |
| `47` | Lectura de decimales |
| `48` | Escritura de decimales |

## 4. Evaluación de expresiones

Archivo: `expresiones.py`

El programa debe:

- Validar paréntesis, corchetes y llaves.
- Verificar el balance de símbolos de agrupación.
- Calcular la profundidad de anidamiento.
- Convertir expresiones infijas a postfijas.
- Evaluar expresiones postfijas.
- Utilizar pilas para procesar expresiones.
- Manejar operandos de varios dígitos.
- Respetar la precedencia y asociatividad de operadores.

### Operadores admitidos

- `+` Suma.
- `-` Resta.
- `*` Multiplicación.
- `/` División.
- `^` Potencia.

## 5. Lenguaje de programación Simple

El sistema debe reconocer:

- Números de línea en orden ascendente.
- Variables de una sola letra.
- Constantes enteras.
- Expresiones aritméticas.
- Instrucciones condicionales.
- Comandos escritos en minúsculas, excepto comentarios.

### Comandos

- `rem`
- `input`
- `let`
- `print`
- `goto`
- `if/goto`
- `end`

### Operadores de comparación

- `<`
- `<=`
- `>`
- `>=`
- `==`
- `!=`

## 6. Construcción del compilador

Archivo: `compilador.py`

El compilador debe:

- Leer programas escritos en Simple.
- Realizar una primera pasada.
- Construir una tabla de símbolos.
- Registrar variables, constantes y números de línea.
- Identificar referencias pendientes.
- Realizar una segunda pasada.
- Resolver referencias a líneas posteriores.
- Convertir expresiones infijas a postfijas.
- Generar instrucciones SML.
- Guardar el resultado en un archivo `.sml`.
- Generar código ejecutable en el simulador original.

## 7. Pruebas de funcionamiento

El proyecto incluye los siguientes programas de prueba:

| Programa | Funcionalidad |
|---|---|
| `secuencia.simple` | Ejecución secuencial |
| `seleccion.simple` | Selección |
| `repeticion.simple` | Repetición |
| `secuencia.sml` | Secuencia en SML |
| `seleccion.sml` | Selección en SML |
| `repeticion.sml` | Repetición en SML |
| `Mod_Potencia.simp` | Módulo y potencia |
| `Cadenas_Decimales.simp` | Cadenas y decimales |

Las pruebas deben permitir verificar el funcionamiento de las instrucciones, los registros, las operaciones, las modificaciones y el compilador.
