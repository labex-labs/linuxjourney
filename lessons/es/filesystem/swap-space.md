---
index: 8
lang: "es"
title: "swap"
meta_title: "swap - El Filesystem"
meta_description: "Aprende sobre el espacio swap en Linux, cómo funciona y cómo crear y gestionar particiones swap. ¡Optimiza el uso de la memoria de tu sistema con esta guía!"
meta_keywords: "Linux swap, mkswap, swapon, swapoff, /etc/fstab, memoria virtual, Linux para principiantes, tutorial de Linux"
---

## Lesson Content

En nuestro ejemplo anterior, te mostré cómo ver tu tabla de particiones. Volvamos a ese ejemplo, más específicamente a esta línea:

```
Number  Start   End     Size    Type      File system     Flags
 5      6861MB  7380MB  519MB   logical   linux-swap(v1)
```

¿Qué es esta partición swap? Bueno, swap es lo que usamos para asignar memoria virtual a nuestro sistema. Si tienes poca memoria, el sistema usa esta partición para "intercambiar" (swap) piezas de memoria de procesos inactivos al disco, para que no te quedes sin memoria.

### Usando una partición para swap space

Digamos que queremos configurar nuestra partición `/dev/sdb2` para que se use como swap space.

1. Primero, asegúrate de que no tenemos nada en la partición.
2. Ejecuta: `mkswap /dev/sdb2` para inicializar las áreas de swap.
3. Ejecuta: `swapon /dev/sdb2`. Esto habilitará el dispositivo swap.
4. Si quieres que la partición swap persista al iniciar, necesitas añadir una entrada al archivo `/etc/fstab`. `sw` es el tipo de sistema de archivos que usarás.
5. Para eliminar swap: `swapoff /dev/sdb2`.

Generalmente, deberías asignar aproximadamente el doble de swap space de la memoria que tienes. Sin embargo, los sistemas modernos de hoy en día suelen ser lo suficientemente potentes y tienen suficiente RAM tal como está.

## Exercise

Particiona el espacio libre en la unidad USB para swap space.

## Quiz Question

¿Cuál es el comando para habilitar el swap space en un dispositivo?

## Quiz Answer

swapon
