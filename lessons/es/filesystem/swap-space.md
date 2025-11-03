---
index: 8
lang: "es"
title: "intercambio"
meta_title: "intercambio - El Sistema de Archivos"
meta_description: "Aprenda sobre el espacio de intercambio (swap) de Linux, cómo funciona, y cómo crear y administrar particiones de intercambio. ¡Optimice el uso de memoria de su sistema con esta guía!"
meta_keywords: "swap de Linux, mkswap, swapon, swapoff, /etc/fstab, memoria virtual, principiante Linux, tutorial Linux"
---

## Lesson Content

En nuestro ejemplo anterior, les mostré cómo ver su tabla de particiones. Revisitemos ese ejemplo, más específicamente esta línea:

```
Number  Start   End     Size    Type      File system     Flags
 5      6861MB  7380MB  519MB   logical   linux-swap(v1)
```

¿Qué es esta partición swap? Bueno, swap es lo que usamos para asignar memoria virtual a nuestro sistema. Si tiene poca memoria, el sistema utiliza esta partición para "intercambiar" (swap) partes de la memoria de procesos inactivos al disco, para que no se sature por falta de memoria.

### Usar una partición para espacio swap

Supongamos que queremos configurar nuestra partición `/dev/sdb2` para que se use como espacio swap.

1. Primero, asegúrese de que no haya nada en la partición.
2. Ejecute: `mkswap /dev/sdb2` para inicializar las áreas swap.
3. Ejecute: `swapon /dev/sdb2`. Esto habilitará el dispositivo swap.
4. Si desea que la partición swap persista al arrancar, debe agregar una entrada al archivo `/etc/fstab`. `sw` es el tipo de sistema de archivos que utilizará.
5. Para desactivar swap: `swapoff /dev/sdb2`.

Generalmente, debe asignar aproximadamente el doble de espacio swap que la cantidad de memoria que tiene. Sin embargo, los sistemas modernos hoy en día suelen ser lo suficientemente potentes y ya cuentan con suficiente RAM.

## Exercise

¡La práctica hace al maestro! Aquí hay algunos laboratorios prácticos para reforzar su comprensión del espacio swap de Linux y la gestión de memoria virtual:

1. **[Crear y Activar un Archivo Swap en Linux](https://labex.io/es/labs/comptia-create-and-activate-a-swap-file-in-linux-590858)** - Practique la creación y activación de un archivo swap, una habilidad crucial para administrar la memoria virtual de su sistema.

Este laboratorio le ayudará a aplicar los conceptos de particiones swap en escenarios reales y a ganar confianza con la gestión de recursos del sistema.

## Quiz Question

¿Cuál es el comando para habilitar el espacio swap en un dispositivo?

## Quiz Answer

swapon
