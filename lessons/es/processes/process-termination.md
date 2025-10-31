---
index: 5
lang: "es"
title: "Terminación de Procesos"
meta_title: "Terminación de Procesos - Procesos"
meta_description: "Explore la terminación de procesos en Linux, la llamada al sistema wait, y las diferencias clave en el debate sobre procesos zombis vs. huérfanos. Aprenda a gestionar los estados de los procesos hijos de linux kill para un sistema estable."
meta_keywords: "Terminación de procesos Linux, proceso zombi, proceso huérfano, proceso zombi vs huérfano, linux kill proceso hijo, llamada al sistema wait, _exit, gestión de procesos"
---

## Lesson Content

### El Proceso de Terminación

Una vez que se crea un proceso, ¿cómo finaliza? La terminación de un proceso es una parte crítica del ciclo de vida del proceso, asegurando que los recursos del sistema se gestionen de manera efectiva.

Un proceso típicamente termina al llamar a la llamada al sistema `_exit`. Esta acción indica al kernel que el proceso ha finalizado y que sus recursos, como la memoria y los descriptores de archivos, pueden ser recuperados. Al salir, el proceso proporciona un estado de terminación al kernel, que es un valor entero. Por convención, un estado de 0 indica una ejecución exitosa, mientras que un valor distinto de cero señala un error.

Sin embargo, llamar a `_exit` no borra inmediatamente el proceso. El proceso padre debe reconocer la terminación de su hijo utilizando la llamada al sistema `wait`. Esta llamada permite al padre recuperar el estado de terminación del hijo. Este mecanismo de dos pasos es esencial para la limpieza adecuada de los procesos. Otra forma de `linux kill child process` (terminar proceso hijo en Linux) es mediante el uso de señales, un tema que exploraremos en una lección posterior.

### Procesos Huérfanos (Orphan Processes)

¿Qué sucede si un proceso padre termina antes que su hijo? El proceso hijo se convierte en un "huérfano" (orphan). Dado que su padre original ya no puede llamar a `wait`, el kernel interviene. El proceso huérfano es adoptado inmediatamente por un proceso especial del sistema, típicamente `init` (ID de proceso 1), que se considera el ancestro de todos los procesos. El proceso `init` asume entonces el papel de padre, llamando periódicamente a `wait` para recopilar el estado de terminación de cualquiera de sus hijos adoptados, permitiéndoles terminar limpiamente.

### Procesos Zombis (Zombie Processes)

Ocurre un escenario diferente cuando un proceso hijo termina, pero su padre aún no ha llamado a `wait`. En este estado, el hijo se convierte en un proceso "zombi". El kernel libera la mayoría de los recursos del zombi, pero mantiene una entrada en la tabla de procesos. Esta entrada contiene el ID del proceso y el estado de terminación, esperando a que el padre lo recoja.

Los procesos zombis ya están muertos, por lo que no consumen tiempo de CPU. No se pueden terminar con señales porque no se están ejecutando. El proceso por el cual el padre llama a `wait` para limpiar un zombi se denomina "reaping" (cosecha). Si el proceso padre nunca llama a `wait`, estos zombis pueden acumularse. Aunque unos pocos son inofensivos, un gran número puede llenar la tabla de procesos, impidiendo la creación de nuevos procesos. En casos en que el proceso padre también termina, `init` adoptará y cosechará al zombi.

### Proceso Zombi vs Huérfano

Comprender la diferencia entre un `zombie vs orphan process` (proceso zombi vs huérfano) es clave para diagnosticar problemas relacionados con los procesos.

- Un **proceso huérfano** es un proceso activo y en ejecución cuyo padre ha muerto. Es adoptado por `init` y continúa ejecutándose hasta que finaliza.
- Un **proceso zombi** es un proceso muerto que ha completado su ejecución pero aún tiene una entrada en la tabla de procesos. Está esperando que su proceso padre lea su estado de salida.

En resumen, un huérfano está vivo pero sin padre, mientras que un zombi está muerto pero aún no ha sido completamente cosechado por su padre.

## Exercise

Para aplicar estos conceptos, intente el siguiente laboratorio práctico:

1. **[Gestionar y Monitorizar Procesos de Linux](https://labex.io/es/labs/comptia-manage-and-monitor-linux-processes-590864)** - Practique la interacción con procesos en primer plano y en segundo plano, inspeccionándolos con `ps`, monitorizando recursos con `top`, ajustando la prioridad con `renice` y terminándolos con `kill`. Este laboratorio proporciona experiencia práctica con el ciclo de vida del proceso, incluida la forma de terminarlos y observar sus estados.

## Quiz Question

¿Cuál es el estado de terminación más común para un proceso que tiene éxito?

## Quiz Answer

0
