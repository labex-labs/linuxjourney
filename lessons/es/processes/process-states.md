---
index: 9
lang: "es"
title: "Estados de los Procesos"
meta_title: "Estados de los Procesos - Procesos"
meta_description: "Aprenda los estados de los procesos de Linux (R, S, D, Z, T) usando `ps aux`. Comprenda los códigos STAT comunes y gestione los procesos de forma eficaz. ¡Comience su viaje en Linux!"
meta_keywords: "estados de procesos de Linux, ps aux, gestión de procesos, tutorial de Linux, Linux para principiantes, códigos STAT, guía de Linux"
---

## Lesson Content

Echemos un vistazo al comando `ps aux` nuevamente:

```bash
ps aux
```

En la columna STAT, verá muchos valores. Un proceso de Linux puede estar en varios estados diferentes. Los códigos de estado más comunes que verá se describen a continuación:

- **R**: Running o ejecutable; solo está esperando que la CPU lo procese.
- **S**: Interruptible sleep; esperando que se complete un evento, como la entrada desde la terminal.
- **D**: Uninterruptible sleep; procesos que no pueden ser terminados o interrumpidos con una señal. Usualmente, para hacer que desaparezcan, debe reiniciar o solucionar el problema.
- **Z**: Zombie; discutimos en una lección anterior que los zombies son procesos terminados que están esperando que se recopilen sus estados.
- **T**: Stopped; un proceso que ha sido suspendido/detenido.

## Exercise

Eche un vistazo a los procesos en ejecución en su sistema y verifique sus estados de proceso.

## Quiz Question

¿Qué código STAT se utiliza para representar un sueño ininterrumpible?

## Quiz Answer

D
