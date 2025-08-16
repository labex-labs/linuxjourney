---
title: "Creación de Procesos"
description: "Aprende sobre la creación de procesos en Linux, fork y los procesos padre/hijo. Comprende PID, PPID y el proceso init. Obtén una guía para principiantes sobre la gestión de procesos en Linux."
keywords: "creación de procesos Linux, fork, PID, PPID, proceso init, procesos Linux, principiante, tutorial, guía"
---

## Lesson Content

De nuevo, esta lección y la siguiente son puramente informativas para que veas lo que hay bajo el capó. Siéntete libre de volver a esto una vez que hayas trabajado un poco más con los procesos.

Cuando se crea un nuevo proceso, un proceso existente básicamente se clona a sí mismo usando algo llamado la llamada al sistema `fork` (las llamadas al sistema se discutirán mucho más adelante). La llamada al sistema `fork` crea un proceso hijo casi idéntico. Este proceso hijo adquiere un nuevo ID de proceso (PID), y el proceso original se convierte en su proceso padre y tiene algo llamado ID de proceso padre **PPID**. Después, el proceso hijo puede continuar usando el mismo programa que su padre estaba usando antes o, más a menudo, usar la llamada al sistema `execve` para lanzar un nuevo programa. Esta llamada al sistema destruye la gestión de memoria que el kernel puso en marcha para ese proceso y establece nuevas para el nuevo programa.

Podemos ver esto en acción:

```bash
ps l
```

La opción `l` nos da un "formato largo" o una vista aún más detallada de nuestros procesos en ejecución. Verás una columna etiquetada **PPID**; este es el ID del padre. Ahora mira tu terminal; verás un proceso en ejecución que es tu shell. Así que en mi sistema, tengo un proceso ejecutando `bash`. Ahora recuerda que cuando ejecutaste el comando `ps l`, lo estabas ejecutando desde el proceso que estaba ejecutando `bash`. Verás que el **PID** del shell `bash` es el **PPID** del comando `ps l`.

Entonces, si cada proceso debe tener un padre y son solo bifurcaciones entre sí, debe haber una madre de todos los procesos, ¿verdad? Estás en lo correcto. Cuando el sistema arranca, el kernel crea un proceso llamado **init**; tiene un PID de 1. El proceso `init` no puede ser terminado a menos que el sistema se apague. Se ejecuta con privilegios de root y ejecuta muchos procesos que mantienen el sistema en funcionamiento. Analizaremos más de cerca `init` en el curso de arranque del sistema; por ahora, solo debes saber que es el proceso que genera todos los demás procesos.

## Exercise

Echa un vistazo a tus procesos en ejecución. ¿Puedes ver qué otros procesos tienen padres?

## Quiz Question

¿Qué llamada al sistema crea un nuevo proceso?

## Quiz Answer

fork
