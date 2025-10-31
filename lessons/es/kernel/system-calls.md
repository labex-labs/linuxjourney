---
index: 3
lang: "es"
title: "Llamadas al Sistema"
meta_title: "Llamadas al Sistema - Kernel"
meta_description: "Explora los fundamentos de una llamada al sistema en Linux. Aprende cómo los procesos en espacio de usuario usan llamadas al sistema (syscalls) para solicitar servicios al kernel, cambiar de modo y cómo funciona la tabla de llamadas al sistema. Usa `strace` para ver las llamadas al sistema en acción."
meta_keywords: "llamada al sistema linux, llamadas al sistema, tabla syscall, modo kernel, modo usuario, strace, kernel linux, API syscall"
---

## Lesson Content

Imagina que estás en un gran concierto. Para pasar del área del público general al exclusivo backstage, no puedes simplemente caminar. Necesitas un pase especial que te conceda acceso a través de una puerta específica y vigilada. En el mundo de la computación, las **llamadas al sistema** (system calls) son esos pases especiales.

### ¿Qué Son las Llamadas al Sistema?

Las llamadas al sistema, a menudo abreviadas como _syscalls_, proporcionan una forma para que los procesos en el espacio de usuario soliciten servicios directamente al kernel. El kernel expone un conjunto de servicios a través de la API de llamadas al sistema. Estos servicios son esenciales para operaciones como leer o escribir en un archivo, gestionar la memoria o manejar conexiones de red. El número de llamadas al sistema disponibles es fijo; no puedes añadir nuevas arbitrariamente. Tu sistema mantiene una `tabla de llamadas al sistema` (_syscall table_) donde cada llamada al sistema está registrada con un ID único.

### El Mecanismo de Llamada al Sistema en Linux

Cuando ejecutas un programa como `ls`, el código dentro de él no ejecuta el comando **system call linux** directamente. En su lugar, utiliza una función de biblioteca que actúa como un envoltorio (_wrapper_). Esta función envoltorio prepara los parámetros necesarios y luego desencadena una interrupción de software, o una "trampa" (_trap_).

Esta trampa indica al procesador que cambie del modo de usuario no privilegiado al modo de kernel privilegiado. Una vez en el modo kernel, un manejador de llamadas al sistema toma el control. Utiliza el ID único para buscar la función solicitada en la `tabla de llamadas al sistema` y luego la ejecuta. Por ejemplo, la llamada al sistema `stat()`, utilizada para consultar el estado de un archivo, se encuentra y se ejecuta de esta manera. Después de que el kernel completa la tarea, cambia el contexto de nuevo al modo de usuario y devuelve un código de estado a tu proceso, indicando éxito o un error.

### Visualización de Llamadas al Sistema con strace

Puedes observar las llamadas al sistema que realiza un proceso en tiempo real utilizando el comando `strace`. Esta herramienta es increíblemente útil para depurar y comprender cómo un programa interactúa con el kernel.

Para ver las llamadas al sistema realizadas por el comando `ls`, ejecutarías:

```bash
strace ls
```

Esto mostrará una lista detallada de cada llamada al sistema que `ls` realiza durante su ejecución.

## Exercise

¡La práctica hace al maestro! Si bien el funcionamiento interno de las llamadas al sistema es complejo, comprender cómo interactúan los programas del espacio de usuario con el kernel es fundamental. La mejor manera de captar esta interacción es practicando con comandos que realizan estas operaciones subyacentes. Aquí tienes algunos laboratorios prácticos para reforzar tu comprensión de las interacciones del sistema de archivos, que dependen en gran medida de las llamadas al sistema:

1. **[Navegar por el Sistema de Archivos en Linux](https://labex.io/es/labs/comptia-navigate-the-filesystem-in-linux-590971)** - Practica comandos esenciales como `ls`, `cd` y `pwd` para moverte e inspeccionar tu sistema de archivos Linux, interactuando directamente con los servicios del sistema de archivos del kernel.
2. **[Gestionar Archivos y Directorios en Linux](https://labex.io/es/labs/comptia-manage-files-and-directories-in-linux-590835)** - Aprende a crear, eliminar, copiar y mover archivos y directorios usando comandos como `mkdir`, `rm`, `cp` y `mv`, todos los cuales involucran llamadas al sistema para realizar sus acciones.
3. **[Buscar Archivos y Comandos en Linux](https://labex.io/es/labs/comptia-find-files-and-commands-in-linux-590834)** - Domina las técnicas para localizar archivos y comandos usando `find`, `whereis` y `which`, ilustrando aún más cómo los comandos de usuario aprovechan los servicios del kernel para interactuar con el sistema de archivos.

Estos laboratorios te ayudarán a aplicar los conceptos de interacción con el sistema de archivos en escenarios reales y a ganar confianza con las operaciones fundamentales de Linux que dependen implícitamente de las llamadas al sistema.

## Quiz Question

What is used to switch from user mode to kernel mode? Please answer in English, using two words.

## Quiz Answer

System call
