Proyecto **Un simulador de Computadora - Simpletron**.

Esta versión contiene la implementación completa del simulador desarrollado en **Python**.

Esta versión implementa las doce operaciones SML, la carga y validación de instrucciones, el ciclo de búsqueda, decodificación y ejecución, las transferencias de control, el manejo de errores fatales y el vaciado completo de registros y memoria.

## Incluye

- Memoria de 100 posiciones.
- Inicialización de los registros principales:
  - `accumulator`
  - `instructionCounter`
  - `instructionRegister`
  - `operationCode`
  - `operand`
- Todos los registros inicializados en `0`.
- Captura de instrucciones por posición.
- Almacenamiento secuencial dentro de `memory`.
- Uso de `9999` para finalizar la carga del programa.
- Validación de valores entre `-9999` y `+9998`.
- Ciclo completo de búsqueda, decodificación y ejecución.
- Implementación de las 12 operaciones SML.
- Transferencias de control condicionales e incondicionales.
- Operación de alto.
- Manejo de errores fatales.
- Detección de división entre cero.
- Detección de desbordamiento del acumulador.
- Detección de códigos de operación inválidos.
- Vaciado de registros y de las 100 posiciones de memoria.
- Organización del programa en funciones para carga, ejecución y vaciado.

## Funcionamiento

Al iniciar, Simpletron solicita las instrucciones una por una indicando la posición de memoria correspondiente:

```text
00 ?
01 ?
02 ?
03 ?
