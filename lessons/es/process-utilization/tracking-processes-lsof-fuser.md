---
index: 2
lang: "es"
title: "lsof y fuser"
meta_title: "lsof y fuser - Utilización de Procesos"
meta_description: "Aprende a usar los comandos lsof y fuser en Linux para identificar procesos que usan archivos. Comprende los errores de 'Dispositivo o Recurso Ocupado' y gestiona los archivos abiertos de forma eficaz."
meta_keywords: "lsof, fuser, comandos Linux, archivos abiertos, gestión de procesos, tutorial Linux, guía para principiantes, dispositivo ocupado"
---

## Lesson Content

Digamos que conectaste una unidad USB y empezaste a trabajar en algunos archivos. Una vez que terminaste, intentaste desmontar el dispositivo USB y recibiste un error: "Dispositivo o recurso ocupado". ¿Cómo averiguarías qué archivos de la unidad USB todavía están en uso? Hay dos herramientas que puedes usar para esto:

### lsof

Recuerda, los archivos no son solo archivos de texto, imágenes, etc.; son todo en el sistema: discos, tuberías, sockets de red, dispositivos, etc. Para ver qué está en uso por un proceso, puedes usar el comando `lsof` (abreviatura de "list open files"). Esto te mostrará una lista de todos los archivos abiertos y sus procesos asociados.

```bash
pete@icebox:~$ lsof .
COMMAND    PID  USER   FD   TYPE DEVICE SIZE/OFF NODE NAME
lxsession 1491 pete  cwd    DIR    8,6     4096  131 .
update-no 1796 pete  cwd    DIR    8,6     4096  131 .
nm-applet 1804 pete  cwd    DIR    8,6     4096  131 .
indicator 1809 pete  cwd    DIR    8,6     4096  131 .
xterm     2205 pete  cwd    DIR    8,6     4096  131 .
bash      2207 pete  cwd    DIR    8,6     4096  131 .
lsof      5914 pete  cwd    DIR    8,6     4096  131 .
lsof      5915 pete  cwd    DIR    8,6     4096  131 .
```

Ahora puedo ver qué procesos están manteniendo el dispositivo/archivo abierto. En nuestro ejemplo de USB, también puedes terminar estos procesos para poder desmontar esta molesta unidad.

### fuser

Otra forma de rastrear un proceso es con el comando `fuser` (abreviatura de "file user"). Esto te mostrará información sobre el proceso que está usando el archivo o el usuario del archivo.

```bash
pete@icebox:~$ fuser -v .
                     USER        PID ACCESS COMMAND
/home/pete:         pete  1491 ..c.. lxsession
                     pete  1796 ..c.. update-notifier
                     pete  1804 ..c.. nm-applet
                     pete  1809 ..c.. indicator-power
                     pete  2205 ..c.. xterm
                     pete  2207 ..c.. bash
```

Podemos ver qué procesos están usando actualmente nuestro directorio `/home/pete`. Las herramientas `lsof` y `fuser` son muy similares. Familiarízate con estas herramientas e intenta usarlas la próxima vez que necesites rastrear un archivo o proceso.

## Exercise

¡La práctica hace al maestro! Aquí tienes algunos laboratorios prácticos para reforzar tu comprensión de la gestión de procesos y la resolución de conflictos de recursos:

1. **[Administrar y Monitorear Procesos de Linux](https://labex.io/es/labs/comptia-manage-and-monitor-linux-processes-590864)** - Practica la interacción con procesos en primer y segundo plano, inspeccionándolos con `ps`, monitoreando recursos con `top` y terminándolos con `kill`. Este laboratorio te ayudará a identificar y gestionar procesos que podrían estar reteniendo recursos, como archivos en una unidad USB.

Este laboratorio te ayudará a aplicar los conceptos en escenarios reales y a desarrollar confianza en la identificación y gestión de procesos del sistema.

## Quiz Question

¿Qué comando se utiliza para listar los archivos abiertos y la información de sus procesos?

## Quiz Answer

lsof
