# Un simulador de Computadora - Simpletron

# ⚠️ LEER EL README COMPLETO PARA NO TENER PROBLEMAS DE EJECUCIÓN ⚠️
Proyecto **Un simulador de Computadora - Simpletron**, desarrollado en **Python**.

El proyecto incluye un simulador de computadora que ejecuta instrucciones en lenguaje **SML**, una versión con modificaciones, un evaluador de expresiones aritméticas y un compilador del lenguaje **Simple** a **SML**.

## Contenido

- **Simulador original:** ejecuta las 12 instrucciones originales SML.
- **Simulador modificado:** incorpora memoria extendida y nuevas instrucciones.
- **Evaluador de expresiones:** convierte y evalúa expresiones aritméticas.
- **Compilador:** traduce programas escritos en Simple a instrucciones SML.
- **Programas de prueba:** permiten comprobar el funcionamiento de los componentes.

## Estructura del proyecto

```text
TDC202-11_2026--Simpletron-FINAL/
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
│   │   └── repeticion.simple
│   └── sml/
│       ├── secuencia.sml
│       ├── seleccion.sml
│       ├── repeticion.sml
│       ├── Mod_Potencia.simp
│       └── Cadenas_Decimales.simp
└── docs/
    ├── requerimientos.md
    └── diseno.md
```

## Cómo descargar el proyecto

1. Ingresar al repositorio: https://github.com/hugocampos-upaep/TDC202-11_2026
2. Seleccionar la rama **💻Simpletron-FINAL**.
3. Localizar el botón verde **Code**.
4. Hacer clic sobre **Code**.
5. Seleccionar **Download ZIP**.
6. Esperar a que finalice la descarga.
7. Abrir la carpeta de **Descargas**.
8. Hacer clic derecho sobre el ZIP descargado.
9. Seleccionar **Extraer todo**.
10. Abrir **Visual Studio Code**.
11. Seleccionar **Archivo > Abrir carpeta**.
12. Abrir la carpeta interna `TDC202-11_2026--Simpletron-FINAL`.
13. Verificar que dicha carpeta contenga `src`, `programas` y `README.md`.
14. Seleccionar **Terminal > Nueva terminal**.

**Importante:** Todos los comandos deben ejecutarse desde la carpeta principal del proyecto, donde se encuentran `src`, `programas` y `README.md`.

Los siguientes ejemplos utilizan el comando `py` en Windows. Si el equipo reconoce `python` en lugar de `py`, puede utilizarse ese comando.

## 1. Ejecutar el simulador original

En la terminal de **Visual Studio Code**, ejecutar:

```powershell
py src/simpletron/Un_simulador_de_Computadora.py
```

Aparecerá el siguiente menú:

```text
*** Bienvenido a Simpletron ***
1. Cargar archivo  2. Cargar por teclado:
```

### Opción 1. Cargar desde archivo

1. Seleccionar la opción `1`.
2. Introducir la siguiente ruta:

```text
programas/sml/secuencia.sml
```

3. Cuando el programa solicite los datos, introducir `4` y después `5`.

**Salida numérica esperada:**

```text
18
9
```

Al finalizar, el simulador mostrará los registros y el vaciado de memoria.

También pueden ejecutarse:

- `programas/sml/seleccion.sml`
- `programas/sml/repeticion.sml`

### Opción 2. Cargar por teclado

1. Ejecutar nuevamente el simulador.
2. Seleccionar la opción `2`.
3. Introducir las instrucciones:

```text
00 ? 1090
01 ? 1190
02 ? 4300
03 ? 9999
```

El valor `9999` finaliza la carga manual.

**Importante:** Después de introducir `9999`, el simulador comienza a ejecutar las instrucciones. Si aparece otro signo `?`, se debe introducir un número entero.

Por ejemplo:

```text
? 8
8
Terminó la ejecución de Simpletron
```

Después se mostrarán los registros y la memoria.

## 2. Ejecutar el simulador modificado

En la terminal de **Visual Studio Code**, ejecutar:

```powershell
py src/simpletron/Modificaciones_al_simulador_de_Simpletron.py
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

Este ejemplo demuestra las instrucciones de módulo y potencia.

### Prueba de cadenas y decimales

Ejecutar nuevamente el simulador modificado.

1. Seleccionar la opción `1`.
2. Introducir el archivo:

```text
programas/sml/Cadenas_Decimales.simp
```

3. Introducir la cadena `hola`.
4. Introducir el número decimal `2.5`.

**Salida esperada:**

```text
hola

2.5
```

## 3. Ejecutar el evaluador de expresiones

En la terminal de **Visual Studio Code**, ejecutar:

```powershell
py src/expresiones/expresiones.py
```

Introducir la siguiente expresión:

```text
{2 + [3 * (4 + 1)]} ^ 2
```

**Resultado esperado:**

```text
Profundidad: 3
Postfijo: 2 3 4 1 + * + 2 ^
Resultado: 289
```

## 4. Ejecutar el compilador

En la terminal de **Visual Studio Code**, ejecutar:

```powershell
py -m src.compilador.compilador
```

El programa solicitará el archivo escrito en lenguaje Simple.

Introducir:

```text
programas/simple/secuencia.simple
```

Posteriormente, solicitará el nombre del archivo SML que se generará.

Introducir:

```text
programas/sml/prueba_compilada.sml
```

El compilador procesará el programa y creará el archivo `prueba_compilada.sml` en la carpeta `programas/sml/`.

### Ejecutar el programa compilado

En la terminal de **Visual Studio Code**, ejecutar:

```powershell
py src/simpletron/Un_simulador_de_Computadora.py
```

1. Seleccionar la opción `1`.
2. Introducir el archivo generado:

```text
programas/sml/prueba_compilada.sml
```

3. Introducir los números `4` y `5`.

**Salida numérica esperada:**

```text
18
9
```

Esto permite comprobar que el compilador genera instrucciones ejecutables en Simpletron.

## Programas de prueba

| Programa | Función |
|---|---|
| `secuencia.simple` | Ejecución secuencial |
| `seleccion.simple` | Selección y condiciones |
| `repeticion.simple` | Repetición |
| `secuencia.sml` | Secuencia en SML |
| `seleccion.sml` | Selección en SML |
| `repeticion.sml` | Repetición en SML |
| `Mod_Potencia.simp` | Módulo y potencia |
| `Cadenas_Decimales.simp` | Cadenas y decimales |

## Documentación

Para consultar las características y el funcionamiento interno del proyecto, revisar los siguientes documentos:

- [Requerimientos del proyecto](docs/requerimientos.md)
- [Diseño del proyecto](docs/diseno.md)
