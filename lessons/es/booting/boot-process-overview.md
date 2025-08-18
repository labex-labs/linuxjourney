---
lang: "es"
title: "Visión general del proceso de arranque"
meta_title: "Visión general del proceso de arranque - Arrancar el Sistema"
meta_description: "Aprende las etapas del proceso de arranque de Linux: BIOS, bootloader, kernel e init. Comprende cómo Linux se inicia desde el encendido hasta el inicio de sesión. Guía esencial para principiantes de Linux."
meta_keywords: "proceso de arranque de Linux, BIOS, bootloader, kernel, init, tutorial de Linux, guía de Linux, principiante"
---

## Lesson Content

Ahora que hemos comprendido bastante bien algunos de los componentes importantes de Linux, vamos a unirlos todos aprendiendo cómo arranca el sistema. Cuando enciendes tu máquina, hace algunas cosas interesantes como mostrar la pantalla del logo, ejecutar diferentes mensajes y, al final, se te presenta una ventana de inicio de sesión. Bueno, en realidad suceden muchísimas cosas entre que presionas el botón de encendido y cuando inicias sesión, y las discutiremos en este curso.

El proceso de arranque de Linux se puede dividir en 4 etapas simples:

### 1. BIOS

La BIOS (siglas de "Basic Input/Output System") inicializa el hardware y se asegura con una Power-on Self-Test (POST) de que todo el hardware está listo para funcionar. El trabajo principal de la BIOS es cargar el bootloader.

### 2. Bootloader

El bootloader carga el kernel en la memoria y luego inicia el kernel con un conjunto de parámetros del kernel. Uno de los bootloaders más comunes es GRUB, que es un estándar universal de Linux.

### 3. Kernel

Cuando el kernel se carga, inmediatamente inicializa los dispositivos y la memoria. El trabajo principal del kernel es cargar el proceso init.

### 4. Init

Recuerda, el proceso init es el primer proceso que se inicia. Init inicia y detiene los procesos de servicio esenciales en el sistema. Hay tres implementaciones principales de init en las distribuciones de Linux. Las revisaremos brevemente y luego profundizaremos en ellas en otro curso.

Ahí está, la explicación (muy) simple del proceso de arranque de Linux. Entraremos en más detalles sobre estas etapas en las próximas lecciones.

## Exercise

Reboot your system and see if you can spot each step as your machine boots up.

## Quiz Question

¿Cuál es la última etapa en el proceso de arranque de Linux?

## Quiz Answer

init
