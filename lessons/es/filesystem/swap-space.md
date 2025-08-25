---
index: 8
lang: "es"
title: "swap"
meta_title: "swap - El Sistema de Archivos"
meta_description: "Aprende sobre el espacio de intercambio de Linux, cómo funciona y cómo crear y gestionar particiones de intercambio. ¡Optimiza el uso de la memoria de tu sistema con esta guía!"
meta_keywords: "Linux swap, mkswap, swapon, swapoff, /etc/fstab, memoria virtual, Linux para principiantes, tutorial de Linux"
---

## Lesson Content

En nuestro ejemplo anterior, te mostré cómo ver tu tabla de particiones. Volvamos a ese ejemplo, más específicamente a esta línea:

```
Number  Start   End     Size    Type      File system     Flags
 5      6861MB  7380MB  519MB   logical   linux-swap(v1)
```

¿Qué es esta partición de intercambio (swap)? Bueno, swap es lo que usamos para asignar memoria virtual a nuestro sistema. Si tienes poca memoria, el sistema usa esta partición para "intercambiar" (swap) piezas de memoria de procesos inactivos al disco, para que no te quedes atascado por falta de memoria.

### Usando una partición para espacio de intercambio

Supongamos que queremos configurar nuestra partición `/dev/sdb2` para que se use como espacio de intercambio.

1. Primero, asegúrate de que no haya nada en la partición.
2. Ejecuta: `mkswap /dev/sdb2` para inicializar las áreas de intercambio.
3. Ejecuta: `swapon /dev/sdb2`. Esto habilitará el dispositivo de intercambio.
4. Si quieres que la partición de intercambio persista al iniciar el sistema, debes añadir una entrada al archivo `/etc/fstab`. `sw` es el tipo de sistema de archivos que usarás.
5. Para eliminar el intercambio: `swapoff /dev/sdb2`.

Generalmente, deberías asignar aproximadamente el doble de espacio de intercambio de la memoria que tienes. Sin embargo, los sistemas modernos de hoy en día suelen ser lo suficientemente potentes y tienen suficiente RAM tal como están.

## Exercise

¡La práctica hace al maestro! Aquí tienes algunos laboratorios prácticos para reforzar tu comprensión del espacio de intercambio de Linux y la gestión de la memoria virtual:

1. **[Crear y Activar un Archivo de Intercambio en Linux](https://labex.io/es/labs/comptia-create-and-activate-a-swap-file-in-linux-590858)** - Practica la creación y activación de un archivo de intercambio, una habilidad crucial para gestionar la memoria virtual de tu sistema.

Este laboratorio te ayudará a aplicar los conceptos de las particiones de intercambio en escenarios reales y a ganar confianza en la gestión de los recursos del sistema.

## Quiz Question

¿Cuál es el comando para habilitar el espacio de intercambio en un dispositivo?

## Quiz Answer

swapon
