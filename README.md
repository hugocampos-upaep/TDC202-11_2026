Proyecto **Modificaciones al simulador de Simpletron**.

La versión del proyecto amplía las capacidades de Simpletron mediante una memoria mayor, nuevas operaciones, manejo de cadenas, carga desde archivo y soporte inicial para valores decimales.

## Incluye

- Memoria ampliada a 1000 posiciones.
- Carga de programa desde archivo `programa.simp`.
- Carga manual por teclado si el archivo no está disponible.
- Adaptación del direccionamiento para posiciones de `000` a `999`.
- Operación de módulo.
- Operación de potencia.
- Instrucción de nueva línea.
- Entrada de cadenas.
- Salida de cadenas.
- Almacenamiento de caracteres mediante ASCII.
- Entrada de valores decimales.
- Salida de valores decimales.
- Conservación de las operaciones originales de Simpletron.
- Manejo de errores durante la ejecución.
- Vaciado de registros y memoria al finalizar.

## Memoria de 1000 posiciones

La memoria del simulador se amplió de 100 a 1000 posiciones:

```python
memory = [0] * 1000
