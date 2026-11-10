# Un simulador de Computadora - Simpletron

## ⚠️ LEER EL README COMPLETO PARA NO TENER PROBLEMAS DE EJECUCIÓN ⚠️

Proyecto desarrollado en **Python** que implementa un simulador de computadora Simpletron, un simulador modificado, un evaluador de expresiones aritméticas y un compilador del lenguaje **Simple a SML**.

## Contenido

- **Simulador original:** ejecuta las 12 instrucciones originales SML.
- **Simulador modificado:** incorpora memoria extendida y nuevas operaciones.
- **Evaluador de expresiones:** valida, convierte y evalúa expresiones aritméticas.
- **Compilador:** traduce programas escritos en Simple a instrucciones SML.
- **Pruebas y evidencias:** permiten comprobar el funcionamiento del proyecto.

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
├── pruebas/
│   ├── entradas/
│   └── salidas/
├── evidencias/
│   ├── ejecuciones/
│   └── git-branch/
└── docs/
    ├── requerimientos.md
    └── diseño.md
```

## Descarga y apertura del proyecto

1. Ingresar al [repositorio de GitHub](https://github.com/hugocampos-upaep/TDC202-11_2026).
2. Seleccionar la rama **💻Simpletron-FINAL**.
3. Hacer clic en **Code > Download ZIP**.
4. Extraer el archivo ZIP descargado.
5. Abrir **Visual Studio Code**.
6. Seleccionar **Archivo > Abrir carpeta**.
7. **Abrir la SEGUNDA carpeta `TDC202-11_2026--Simpletron-FINAL`, ubicada dentro de la primera.**
8. Seleccionar **Terminal > Nueva terminal**.

### ⚠️ IMPORTANTE: ABRIR LA SEGUNDA CARPETA

Al extraer el ZIP, aparecerán dos carpetas con el mismo nombre:

```text
TDC202-11_2026--Simpletron-FINAL/       ← NO ABRIR ESTA
│
└── TDC202-11_2026--Simpletron-FINAL/   ← ABRIR ESTA
    ├── README.md
    ├── src/
    ├── programas/
    ├── pruebas/
    ├── evidencias/
    └── docs/
```

**TODOS LOS COMANDOS DEBEN EJECUTARSE DESDE LA SEGUNDA CARPETA.**

Para comprobar que se abrió correctamente, verificar que `README.md`, `src/` y `programas/` aparezcan directamente dentro de ella.

**Nota:** Los ejemplos utilizan `py` en Windows. Si el equipo reconoce `python` en su lugar, puede utilizarse ese comando.

---

## 1. Ejecutar el simulador original

En la terminal de Visual Studio Code:

```powershell
py src/simpletron/Un_simulador_de_Computadora.py
```

Aparecerá el menú:

```text
*** Bienvenido a Simpletron ***
1. Cargar archivo  2. Cargar por teclado:
```

### Cargar desde archivo

1. Seleccionar `1`.
2. Introducir:

```text
programas/sml/secuencia.sml
```

3. Cuando se soliciten los datos (`?`), introducir `4` y `5`.

**Salida numérica esperada:**

```text
18
9
```

También pueden ejecutarse:

- `programas/sml/seleccion.sml`
- `programas/sml/repeticion.sml`

### Cargar por teclado

1. Ejecutar nuevamente el simulador.
2. Seleccionar `2`.
3. Introducir una instrucción por línea:

```text
1090
1091
2090
3091
2192
1192
4300
9999
```

`9999` termina la carga de instrucciones.

Después, cuando aparezca `?`, introducir los números `4` y `5`.

**Resultado esperado:** `9`.

**Nota:** Los indicadores `00 ?`, `01 ?`, etc., los muestra el simulador y no deben escribirse manualmente.

---

## 2. Ejecutar el simulador modificado

Ejecutar:

```powershell
py src/simpletron/Modificaciones_al_simulador_de_Simpletron.py
```

### Prueba de módulo y potencia

1. Seleccionar `1`.
2. Introducir:

```text
programas/sml/Mod_Potencia.simp
```

3. Introducir `4` cuando aparezca `?`.

**Salida numérica esperada:**

```text
1
64
```

### Prueba de cadenas y decimales

Ejecutar nuevamente el simulador modificado.

1. Seleccionar `1`.
2. Introducir:

```text
programas/sml/Cadenas_Decimales.simp
```

3. Introducir la cadena `hola`.
4. Introducir el decimal `2.5`.

**Salida esperada:**

```text
hola

2.5
```

---

## 3. Ejecutar el evaluador de expresiones

Ejecutar:

```powershell
py src/expresiones/expresiones.py
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

---

## 4. Ejecutar el compilador

Ejecutar:

```powershell
py -m src.compilador.compilador
```

Introducir las siguientes rutas cuando se soliciten:

**Archivo Simple de entrada:**

```text
programas/simple/secuencia.simple
```

**Archivo SML de salida:**

```text
programas/sml/prueba_compilada.sml
```

El compilador mostrará la tabla de símbolos, las instrucciones provisionales y el código SML final.

Finalmente, creará el archivo `prueba_compilada.sml`.

### Ejecutar el programa compilado

Ejecutar el simulador original:

```powershell
py src/simpletron/Un_simulador_de_Computadora.py
```

1. Seleccionar `1`.
2. Introducir:

```text
programas/sml/prueba_compilada.sml
```

3. Introducir `4` y `5` cuando se soliciten.

**Salida numérica esperada:**

```text
18
9
```

---

## 5. Pruebas y evidencias

La carpeta `pruebas/` contiene:

- **`entradas/`:** archivos `.txt` con los datos necesarios para ejecutar las pruebas.
- **`salidas/`:** archivos `.txt` con los resultados esperados.

Por ejemplo, para ejecutar una prueba utilizando su archivo de entrada desde PowerShell:

```powershell
Get-Content pruebas/entradas/secuencia.txt | py src/simpletron/Un_simulador_de_Computadora.py
```

### Resultados esperados

| Programa | Entradas | Salidas |
|---|---|---|
| `secuencia.sml` | `4`, `5` | `18`, `9` |
| `seleccion.sml` | `7`, `3` | `7` |
| `repeticion.sml` | `3` | `3`, `2`, `1` |
| `Mod_Potencia.simp` | `4` | `1`, `64` |
| `Cadenas_Decimales.simp` | `hola`, `2.5` | `hola`, `2.5` |

Las capturas de funcionamiento se encuentran en:

- **`evidencias/ejecuciones/`:** pruebas de los programas y detección de errores.
- **`evidencias/git-branch/`:** ramas e historial de commits de GitHub.

---

## 6. Problemas comunes

### Error por abrir la carpeta incorrecta

Si aparece un error similar a:

```text
can't open file
No such file or directory
```

Verificar que Visual Studio Code tenga abierta la **SEGUNDA carpeta del proyecto**, donde se encuentran directamente `src/`, `programas/` y `README.md`.

### Error al cargar un archivo

Si aparece:

```text
No se pudo abrir el archivo
```

Verificar que la ruta introducida exista y esté escrita correctamente.

Por ejemplo:

```text
programas/sml/secuencia.sml
```

**Importante:** Los errores de ubicación de archivos son diferentes de los errores internos del simulador, como la división entre cero o las instrucciones inválidas.

---

## Documentación

Para consultar los requerimientos y el diseño interno del proyecto:

- [Requerimientos del proyecto](docs/requerimientos.md)
- [Diseño del proyecto](docs/diseño.md)

---

### ⚠️ RECORDATORIO: ABRIR LA SEGUNDA CARPETA Y LEER LAS INSTRUCCIONES ANTES DE EJECUTAR EL PROYECTO ⚠️
