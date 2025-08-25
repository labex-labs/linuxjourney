---
index: 3
lang: "es"
title: "Llamadas al sistema"
meta_title: "Llamadas al sistema - Kernel"
meta_description: "Aprenda sobre las llamadas al sistema (syscalls) de Linux y cómo interactúan con el kernel. Comprenda los modos de usuario y kernel, y use `strace` para depurar. ¡Comience su viaje en Linux!"
meta_keywords: "Llamadas al sistema Linux, syscalls, modo kernel, modo usuario, comando strace, tutorial Linux, Linux para principiantes, guía Linux"
---

## Lesson Content

¿Recuerdas a Britney en la lección anterior? Digamos que queremos verla y tomar algo juntos. ¿Cómo pasamos de estar afuera entre la multitud a estar dentro de su círculo más íntimo? Usaríamos llamadas al sistema. Las llamadas al sistema son como los pases VIP que te llevan a una puerta lateral secreta que conduce directamente a Britney.

Las llamadas al sistema (syscalls) proporcionan a los procesos del espacio de usuario una forma de solicitar al kernel que haga algo por nosotros. El kernel pone a disposición ciertos servicios a través de la API de llamadas al sistema. Estos servicios nos permiten leer o escribir en un archivo, modificar el uso de la memoria, modificar nuestra red, etc. La cantidad de servicios es fija, por lo que no se pueden añadir llamadas al sistema a diestro y siniestro. Su sistema ya tiene una tabla de las llamadas al sistema existentes, y cada llamada al sistema tiene una ID única.

No entraré en detalles específicos de las llamadas al sistema, ya que eso requeriría que supieras un poco de C, pero lo básico es que cuando llamas a un programa como `ls`, el código dentro de este programa contiene un envoltorio de llamada al sistema (todavía no es la llamada al sistema real). Dentro de este envoltorio, invoca la llamada al sistema que ejecutará una trampa. Esta trampa es capturada por el manejador de llamadas al sistema y luego hace referencia a la llamada al sistema en la tabla de llamadas al sistema. Digamos que estamos tratando de llamar a la llamada al sistema `stat()`; se identifica por una ID de syscall, y el propósito de la llamada al sistema `stat()` es consultar el estado de un archivo. Ahora recuerda, estabas ejecutando el programa `ls` en modo no privilegiado. Así que ahora ve que estás tratando de hacer una syscall, y luego te cambia al modo kernel. Allí hace muchas cosas, pero lo más importante, busca tu número de syscall, lo encuentra en una tabla basada en la ID de syscall, y luego ejecuta la función que querías ejecutar. Una vez que termina, volverá al modo de usuario, y tu proceso recibirá un estado de retorno si fue exitoso o si tuvo un error. El funcionamiento interno de las syscalls se vuelve realmente detallado; recomendaría buscar información en línea si quieres aprender más.

De hecho, puedes ver las llamadas al sistema que realiza un proceso con el comando `strace`. El comando `strace` es útil para depurar cómo se ejecutó un programa.

```bash
strace ls
```

## Exercise

¡La práctica hace al maestro! Si bien el funcionamiento interno de las llamadas al sistema es complejo, comprender cómo interactúan los programas del espacio de usuario con el kernel es fundamental. La mejor manera de comprender esta interacción es practicando con comandos que realizan estas operaciones subyacentes. Aquí hay algunos laboratorios prácticos para reforzar su comprensión de las interacciones del sistema de archivos, que dependen en gran medida de las llamadas al sistema:

1. **[Navegar por el sistema de archivos en Linux](https://labex.io/es/labs/comptia-navigate-the-filesystem-in-linux-590971)** - Practique comandos esenciales como `ls`, `cd` y `pwd` para moverse e inspeccionar su sistema de archivos Linux, interactuando directamente con los servicios del sistema de archivos del kernel.
2. **[Administrar archivos y directorios en Linux](https://labex.io/es/labs/comptia-manage-files-and-directories-in-linux-590835)** - Aprenda a crear, eliminar, copiar y mover archivos y directorios usando comandos como `mkdir`, `rm`, `cp` y `mv`, todos los cuales implican llamadas al sistema para realizar sus acciones.
3. **[Encontrar archivos y comandos en Linux](https://labex.io/es/labs/comptia-find-files-and-commands-in-linux-590834)** - Domine técnicas para localizar archivos y comandos usando `find`, `whereis` y `which`, ilustrando aún más cómo los comandos de usuario aprovechan los servicios del kernel para interactuar con el sistema de archivos.

Estos laboratorios le ayudarán a aplicar los conceptos de interacción del sistema de archivos en escenarios reales y a generar confianza con las operaciones fundamentales de Linux que dependen implícitamente de las llamadas al sistema.

## Quiz Question

¿Qué se utiliza para cambiar del modo de usuario al modo kernel?

## Quiz Answer

System call
