# 🖥️ Un Simulador de Computadora - Simpletron

Proyecto desarrollado para la materia de **Programación Avanzada - Otoño 2026**.

El objetivo del proyecto es desarrollar en **Python** un simulador funcional de la computadora virtual **Simpletron**, capaz de cargar, interpretar y ejecutar programas escritos en **Simpletron Machine Language (SML)**.

---

📦 [Ver todas las versiones](https://github.com/hugocampos-upaep/TDC202-11_2026/releases)

---

# 🎯 Planteamiento del proyecto

El proyecto consiste en desarrollar un simulador de la computadora virtual **Simpletron** utilizando Python.

Simpletron es una computadora sencilla basada en memoria, registros e instrucciones. El simulador permitirá cargar programas escritos en **Simpletron Machine Language (SML)** y ejecutar sus instrucciones mediante un ciclo de:

- Búsqueda de instrucciones.
- Decodificación.
- Ejecución.
- Manejo de memoria.
- Uso de registros.
- Operaciones aritméticas.
- Transferencias de control.

El desarrollo del proyecto se realizará mediante diferentes versiones, agregando progresivamente nuevas funcionalidades hasta completar el simulador.

---

# 🧠 Memoria

Simpletron utiliza una memoria donde se almacenan instrucciones y datos.

La capacidad de memoria depende de la versión implementada del simulador:

- **Versiones iniciales:**
  - 100 posiciones de memoria.
  - Direcciones disponibles desde `00` hasta `99`.

- **Versiones posteriores:**
  - Ampliación de la capacidad de memoria.
  - Nuevos rangos de direccionamiento para permitir programas más grandes.

La memoria representa el espacio donde Simpletron almacena tanto las instrucciones del programa como los datos utilizados durante su ejecución.

---

# ⚙️ Funcionamiento general

El simulador trabaja mediante el ciclo básico de ejecución de una computadora:

## 1. Búsqueda de instrucción

Simpletron obtiene la siguiente instrucción desde memoria utilizando el contador de instrucciones.

```text
memory[instructionCounter]
