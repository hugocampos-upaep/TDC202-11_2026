# 💻 Compilador de Simple a SML

## Descripción

Este proyecto implementa un compilador para el lenguaje **Simple**.

El compilador recibe un programa escrito en lenguaje Simple y lo convierte a instrucciones en **SML (Simpletron Machine Language)**.

El proceso de compilación se realiza en dos etapas principales:

1. Primera pasada.
2. Segunda pasada.

Durante la primera pasada se construye la tabla de símbolos, se generan las instrucciones SML y se registran las referencias pendientes.

Durante la segunda pasada se resuelven dichas referencias y se completa el código SML final.

El flujo general del compilador es:

```text
Archivo Simple
      ↓
Primera pasada
      ↓
Tabla de símbolos
      ↓
Código SML provisional
      ↓
Segunda pasada
      ↓
Código SML completo
