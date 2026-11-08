Proyecto **Un simulador de Computadora - Simpletron**, desarrollado en **Python**.

Este proyecto incluye el simulador original, las modificaciones al simulador, la evaluación de expresiones aritméticas y un compilador del lenguaje **Simple** a **SML**.

## Incluye

- Simulador original con memoria de **100 posiciones**.
- Simulador modificado con memoria de **1000 posiciones**.
- Inicialización de los registros:
  - `accumulator`
  - `instructionCounter`
  - `instructionRegister`
  - `operationCode`
  - `operand`
- Implementación de las **12 instrucciones originales SML**.
- Carga de instrucciones desde teclado o archivo.
- Uso de `9999` para finalizar la carga manual.
- Ciclo de búsqueda, decodificación y ejecución.
- Transferencias de control.
- Manejo de errores fatales.
- Vaciado de registros y memoria.
- Nuevas instrucciones SML: módulo, potencia, cadenas, decimales y salto de línea.
- Validación de símbolos de agrupación.
- Conversión de expresiones infijas a postfijas.
- Evaluación de expresiones postfijas.
- Reconocimiento del lenguaje Simple.
- Compilador de dos pasadas.
- Tabla de símbolos y resolución de referencias pendientes.
- Generación de código SML ejecutable.
- Programas de prueba en Simple y SML.

## Estructura del proyecto

```text
TDC202-11_2026/
├── README.md
├── src/
│   ├── simpletron/
│   │   ├── Un_simulador_de_Computadora.py
│   │   └── Modificaciones_al_simulador_de_Simpletron.py
│   ├── expresiones/
│   │   └── expresiones.py
│   └── compilador/
│       └── compilador.py
├── programas/
│   ├── simple/
│   │   ├── secuencia.simple
│   │   ├── seleccion.simple
│   │   ├── repeticion.simple
│   │   ├── potencia.simple
│   │   └── comparaciones.simple
│   └── sml/
│       ├── secuencia.sml
│       ├── seleccion.sml
│       ├── repeticion.sml
│       ├── potencia.sml
│       ├── comparaciones.sml
│       ├── SML_Aritmetica.sml
│       ├── Mod_Potencia.simp
│       └── Cadenas_Decimales.simp
├── documentacion/
├── pruebas/
└── evidencias/
```

Las carpetas `documentacion`, `pruebas` y `evidencias` están destinadas a almacenar los documentos y resultados que demuestren el funcionamiento del proyecto.

## Cómo descargar el proyecto

1. Entrar al repositorio: https://github.com/hugocampos-upaep/TDC202-11_2026
2. Seleccionar la rama **💻Simpletron-FINAL**.
3. Localizar el botón verde **Code**.
4. Hacer clic sobre el botón **Code**.
5. Seleccionar la opción **Download ZIP**.
6. Esperar a que termine la descarga.
7. Abrir la carpeta de **Descargas**.
8. Hacer clic derecho sobre el archivo ZIP.
9. Seleccionar **Extraer todo**.
10. Abrir **Visual Studio Code**.
11. Seleccionar **Archivo > Abrir carpeta**.
12. Abrir la carpeta principal del proyecto.
13. Seleccionar **Terminal > Nueva terminal**.

**Nota:** Todos los comandos siguientes deben ejecutarse desde la carpeta principal del proyecto.

## Funcionamiento del simulador original

En la terminal de **Visual Studio Code**, ejecutar el siguiente comando:

```bash
python src/simpletron/Un_simulador_de_Computadora.py
```

Al iniciar, aparecerá:

```text
*** Bienvenido a Simpletron ***
1. Cargar archivo  2. Cargar por teclado:
```

### Carga manual

Seleccionar la opción `2`.

El programa solicitará las instrucciones una por una:

```text
0 ? 1090
1 ? 1190
2 ? 4300
3 ? 9999
```

El valor `9999` indica que terminó la carga manual de instrucciones.

### Carga desde archivo

1. Seleccionar la opción `1`.
2. Introducir la siguiente ruta:

```text
programas/sml/SML_Aritmetica.sml
```

3. Proporcionar los datos solicitados.
4. Observar los resultados y el vaciado de memoria.

El simulador ejecuta las instrucciones SML y muestra el estado final de los registros y la memoria.

## Funcionamiento del simulador modificado

En la terminal de **Visual Studio Code**, ejecutar el siguiente comando:

```bash
python src/simpletron/Modificaciones_al_simulador_de_Simpletron.py
```

1. Seleccionar la opción `1`.
2. Introducir el archivo:

```text
programas/sml/Mod_Potencia.simp
```

3. Introducir el número `4`.

**Salida numérica esperada:**

```text
1
64
```

Este programa demuestra las instrucciones de **módulo** y **potencia**.

Para comprobar las instrucciones de cadenas y decimales, ejecutar nuevamente el simulador y cargar:

```text
programas/sml/Cadenas_Decimales.simp
```

Introducir la cadena `hola` y el número decimal `2.5`.

**Salida esperada:**

```text
hola

2.5
```

El simulador modificado también permite ejecutar programas SML originales.

## Funcionamiento del evaluador de expresiones

En la terminal de **Visual Studio Code**, ejecutar el siguiente comando:

```bash
python src/expresiones/expresiones.py
```

Introducir la expresión:

```text
{2 + [3 * (4 + 1)]} ^ 2
```

**Resultado esperado:**

```text
Profundidad: 3
Postfijo: 2 3 4 1 + * + 2 ^
Resultado: 289
```

El programa valida el anidamiento, comprueba los símbolos de agrupación, convierte la expresión a postfija y calcula su resultado.

## Funcionamiento del compilador

En la terminal de **Visual Studio Code**, ejecutar el siguiente comando:

```bash
python -m src.compilador.compilador
```

El compilador solicitará el archivo escrito en **Simple**.

Introducir:

```text
programas/simple/secuencia.simple
```

Posteriormente, solicitará el nombre del archivo **SML** que se generará.

Introducir:

```text
programas/sml/prueba_compilada.sml
```

El compilador realizará:

1. **Primera pasada:** lectura del programa y construcción de la tabla de símbolos.
2. **Segunda pasada:** resolución de referencias pendientes.
3. **Generación:** creación del archivo SML ejecutable.

### Ejecutar el archivo compilado

En la terminal de **Visual Studio Code**, ejecutar:

```bash
python src/simpletron/Un_simulador_de_Computadora.py
```

1. Seleccionar la opción `1`.
2. Introducir el archivo generado:

```text
programas/sml/prueba_compilada.sml
```

3. Proporcionar los datos solicitados.
4. Observar la ejecución del programa compilado.

## Programas de prueba

Los programas de prueba se encuentran en las carpetas:

- `programas/simple/`: programas escritos en lenguaje Simple.
- `programas/sml/`: programas escritos en lenguaje SML y ejemplos de modificaciones.

| Programa | Función |
|---|---|
| `secuencia.simple` | Ejecución secuencial |
| `seleccion.simple` | Selección y condiciones |
| `repeticion.simple` | Repetición y ciclos |
| `potencia.simple` | Expresiones aritméticas |
| `comparaciones.simple` | Operadores de comparación |
| `SML_Aritmetica.sml` | Operaciones SML originales |
| `Mod_Potencia.simp` | Módulo y potencia |
| `Cadenas_Decimales.simp` | Cadenas y números decimales |
