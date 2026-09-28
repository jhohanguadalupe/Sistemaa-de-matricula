# Sistema de Matrícula Escolar (Basado en Ficha)

Este proyecto es una herramienta interactiva por consola desarrollada en **Python** [1] diseñada para gestionar y registrar el proceso de matrícula escolar de estudiantes. 

El script es una traducción exacta y fiel de la lógica del algoritmo de pseudocódigo en PSeInt denominado *“Matricula_Colegio_Ficha_Oficial”*, adaptado a la sintaxis nativa de Python sin alterar el flujo original de operaciones.

---

## 🚀 Características Principales

El programa guía al usuario a través de una ficha estructurada dividida en las siguientes secciones secuenciales:

*   **Sección 1: Datos del Estudiante** [1]
    *   Captura de nombres, apellidos, fecha de nacimiento y nacionalidad.
    *   Menú interactivo para selección del sexo (M/F).
    *   Especificación del grado, nivel académico al que postula y colegio de procedencia.
*   **Sección 2: Datos del Padre, Madre o Apoderado** [1]
    *   Identificación de parentesco dinámico (Madre, Padre o Apoderado).
    *   Recopilación de información de contacto (teléfono, correo electrónico y dirección).
*   **Módulo de Validación Rigurosa:**
    *   Control de tipos de documento admitidos: DNI o Pasaporte/Carné de Extranjería.
    *   Validación numérica exacta de caracteres: DNI (8 dígitos) y Pasaportes o Teléfonos (9 dígitos).
    *   Control preventivo contra errores de entrada de menús.
*   **Emisión de Ticket Final:**
    *   Verificación física de la documentación requerida.
    *   Generación automática de un ticket estructurado con código de matrícula formateado ante un registro exitoso.

---

## 🛠️ Requisitos del Sistema

*   **Python 3.x** instalado en tu sistema corporativo o personal.
*   No requiere de librerías externas o dependencias adicionales (utiliza únicamente funciones built-in de Python como `input()`, `len()` y flujos de control `while`/`for`).

---

## 💻 Instrucciones de Uso

1. **Descarga o clona** este repositorio en tu máquina local.
2. Abre una terminal o consola de comandos en la ruta donde se encuentra el archivo.
3. Ejecuta el script con el siguiente comando:
   ```bash
   python nombre_del_archivo.py
   ```
4. Siga las instrucciones en pantalla e introduzca los datos solicitados a través del teclado.

---

## 📝 Notas de Implementación (PSeInt a Python)

Para los desarrolladores que analicen el código, se han documentado equivalencias clave dentro del archivo fuente para entender la migración desde el pseudocódigo original:
*   **Declaración de variables:** En Python no se definen los tipos de variables previamente (como en PSeInt); estas se crean dinámicamente en su primera asignación.
*   **Estructuras repetitivas y lógicas:** El condicional *“Mientras NO... Hacer”* se mapea directamente con bucles `while not`.
*   **Índices de Cadenas:** Se aplicó un desfase `[i - 1]` en la lectura de caracteres individuales de los strings para compensar que Python es indexado desde `0`, a diferencia de la función `Subcadena()` de PSeInt que inicia en `1`.
*   **Estructuras de selección:** La sentencia `Según ... Hacer` se sustituye eficientemente por una cadena de bloques lógicos `if / elif / else`.

---

## 📄 Licencia

Este proyecto es de código abierto y está disponible con fines educativos y de aprendizaje sobre lógica de programación y traducción de algoritmos.
