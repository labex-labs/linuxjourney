---
lang: "es"
title: "Terminación de Procesos"
description: "Aprende sobre la terminación de procesos en Linux, incluyendo procesos huérfanos y zombie. Comprende las llamadas al sistema _exit y wait para una gestión eficaz de procesos."
keywords: "terminación de procesos Linux, procesos zombie, procesos huérfanos, llamada al sistema wait, _exit, tutorial Linux, Linux para principiantes"
---

## Lesson Content

Ahora que sabemos lo que sucede cuando se crea un proceso, ¿qué ocurre cuando ya no lo necesitamos? Ten en cuenta que a veces Linux puede ponerse un poco oscuro...

Un proceso puede salir usando la llamada al sistema `_exit`. Esto liberará los recursos que ese proceso estaba usando para su reasignación. Así que cuando un proceso está listo para terminar, le informa al kernel por qué está terminando con algo llamado estado de terminación. Lo más común es que un estado de 0 signifique que el proceso se realizó con éxito. Sin embargo, eso no es suficiente para terminar completamente un proceso. El proceso padre tiene que reconocer la terminación del proceso hijo usando la llamada al sistema `wait`, y lo que esto hace es verificar el estado de terminación del proceso hijo. Sé que es espantoso pensarlo, pero la llamada `wait` es una necesidad; después de todo, ¿qué padre no querría saber cómo murió su hijo?

Hay otra forma de terminar un proceso, y eso implica el uso de señales, lo cual discutiremos pronto.

### Orphan Processes

Cuando un proceso padre muere antes que un proceso hijo, el kernel sabe que no va a recibir una llamada `wait`, así que en su lugar convierte a estos procesos en "huérfanos" y los pone bajo el cuidado de `init` (recuerda, la madre de todos los procesos). `init` eventualmente realizará la llamada al sistema `wait` para estos huérfanos para que puedan morir.

### Zombie Processes

¿Qué sucede cuando un hijo termina y el proceso padre aún no ha llamado a `wait`? Todavía queremos poder ver cómo terminó un proceso hijo, así que aunque el proceso hijo haya terminado, el kernel convierte el proceso hijo en un proceso zombie. Los recursos que usó el proceso hijo aún se liberan para otros procesos; sin embargo, todavía hay una entrada en la tabla de procesos para este zombie. Los procesos zombie tampoco pueden ser eliminados, ya que están técnicamente "muertos", por lo que no puedes usar señales para matarlos. Eventualmente, si el proceso padre llama a la llamada al sistema `wait`, el zombie desaparecerá; esto se conoce como "reaping". Si el padre no realiza una llamada `wait`, `init` adoptará al zombie y automáticamente realizará `wait` y eliminará al zombie. Puede ser malo tener demasiados procesos zombie, ya que ocupan espacio en la tabla de procesos; si se llena, impedirá que otros procesos se ejecuten.

## Exercise

No exercises for this lesson.

## Quiz Question

¿Cuál es el estado de terminación más común para un proceso que se ejecuta con éxito?

## Quiz Answer

0
