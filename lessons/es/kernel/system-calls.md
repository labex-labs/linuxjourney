---
lang: "es"
title: "Llamadas al Sistema"
description: "Aprende sobre las llamadas al sistema de Linux (syscalls) y cómo interactúan con el kernel. Comprende los modos de usuario y kernel, y usa `strace` para depurar. ¡Comienza tu viaje en Linux!"
keywords: "Llamadas al sistema Linux, syscalls, modo kernel, modo usuario, comando strace, tutorial Linux, Linux para principiantes, guía Linux"
---

## Lesson Content

¿Recuerdas a Britney en la lección anterior? Digamos que queremos verla y tomar algo juntos. ¿Cómo pasamos de estar de pie entre la multitud a entrar en su círculo más íntimo? Usaríamos llamadas al sistema. Las llamadas al sistema son como los pases VIP que te llevan a una puerta lateral secreta que conduce directamente a Britney.

Las llamadas al sistema (syscalls) proporcionan a los procesos del espacio de usuario una forma de solicitar al kernel que haga algo por nosotros. El kernel pone a disposición ciertos servicios a través de la API de llamadas al sistema. Estos servicios nos permiten leer o escribir en un archivo, modificar el uso de la memoria, modificar nuestra red, etc. La cantidad de servicios es fija, por lo que no se pueden añadir llamadas al sistema a diestro y siniestro. Su sistema ya tiene una tabla de las llamadas al sistema existentes, y cada llamada al sistema tiene una ID única.

No entraré en detalles específicos de las llamadas al sistema, ya que eso requeriría que supieras un poco de C, pero lo básico es que cuando llamas a un programa como `ls`, el código dentro de este programa contiene un "wrapper" de llamada al sistema (todavía no es la llamada al sistema real). Dentro de este "wrapper", invoca la llamada al sistema que ejecutará una trampa. Esta trampa es capturada por el manejador de llamadas al sistema y luego hace referencia a la llamada al sistema en la tabla de llamadas al sistema. Digamos que estamos intentando llamar a la llamada al sistema `stat()`; se identifica por una ID de syscall, y el propósito de la llamada al sistema `stat()` es consultar el estado de un archivo. Ahora recuerda, estabas ejecutando el programa `ls` en modo no privilegiado. Así que ahora ve que estás intentando hacer una syscall, y te cambia al modo kernel. Allí hace muchas cosas, pero lo más importante es que busca tu número de syscall, lo encuentra en una tabla basándose en la ID de syscall, y luego ejecuta la función que querías ejecutar. Una vez que termina, volverá al modo de usuario, y tu proceso recibirá un estado de retorno si fue exitoso o si tuvo un error. El funcionamiento interno de las syscalls es muy detallado; te recomendaría buscar información en línea si quieres aprender más.

De hecho, puedes ver las llamadas al sistema que hace un proceso con el comando `strace`. El comando `strace` es útil para depurar cómo se ejecutó un programa.

```bash
strace ls
```

## Exercise

No exercises for this lesson.

## Quiz Question

¿Qué se utiliza para cambiar del modo de usuario al modo kernel?

## Quiz Answer

System call
