Proyecto **Compilador de Simple a SML**.

La versión del proyecto implementa un compilador para el lenguaje Simple, capaz de analizar instrucciones, construir una tabla de símbolos, generar código SML y resolver referencias pendientes mediante una primera y segunda pasada.

## Incluye

- Lectura de programas escritos en lenguaje Simple.
- Separación de instrucciones en tokens.
- Manejo de números de línea.
- Manejo de variables.
- Manejo de constantes.
- Construcción de tabla de símbolos.
- Generación de instrucciones SML.
- Primera pasada del compilador.
- Segunda pasada del compilador.
- Uso de un arreglo `flags` para referencias pendientes.
- Resolución de saltos hacia líneas que todavía no han sido procesadas.
- Conversión de expresiones infijas a postfijas.
- Uso de una pila para evaluar expresiones.
- Uso de posiciones temporales en memoria.
- Soporte para los comandos `rem`, `input`, `print`, `let`, `goto`, `if` y `end`.
- Generación de archivo `.sml` con el programa compilado.

## Tabla de símbolos

La tabla de símbolos almacena la información encontrada durante la compilación.

Cada elemento contiene:

```python
symbol
type
location
