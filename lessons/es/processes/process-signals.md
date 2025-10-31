---
index: 6
lang: "es"
title: "Señales"
meta_title: "Señales - Procesos"
meta_description: "Explore los fundamentos de las señales de Linux, un mecanismo clave para la gestión de procesos. Aprenda cómo funcionan las señales de proceso de Linux como SIGTERM (señal 15 linux) y SIGKILL, y comprenda sus códigos de señal del sistema operativo."
meta_keywords: "señales linux, señales de proceso linux, señal 15 linux, código sig so, SIGKILL, SIGTERM, SIGINT, gestión de procesos, tutorial linux"
---

## Lesson Content

En Linux, una señal es una interrupción de software enviada a un proceso para notificarle que ha ocurrido un evento importante. Comprender las **señales de linux** es fundamental para gestionar procesos y el comportamiento del sistema de manera efectiva.

### El Propósito de las Señales

Las señales sirven como un método principal de comunicación entre procesos (IPC). Tienen muchos usos:

- **Interacción del Usuario**: Un usuario puede escribir caracteres especiales de terminal, como `Ctrl-C` (SIGINT) o `Ctrl-Z` (SIGTSTP), para interrumpir o suspender procesos en primer plano.
- **Notificaciones del Kernel**: El kernel puede enviar señales a un proceso para notificarle problemas de hardware o software, como un acceso ilegal a la memoria (SIGSEGV).
- **Gestión de Procesos**: Los administradores del sistema y otros procesos utilizan señales para gestionar el ciclo de vida de otros procesos, como solicitar la terminación o una recarga de configuración.

### El Ciclo de Vida de la Señal

Cuando un evento genera una señal, primero se entrega a un proceso objetivo. La señal permanece en estado "pendiente" hasta que el kernel ejecuta el proceso. Cuando el proceso se programa, se entrega la señal. Sin embargo, los procesos tienen máscaras de señal, que se pueden configurar para bloquear la entrega de señales específicas.

Cuando se entrega una señal, el proceso puede tomar una de varias acciones:

- **Ignorar la señal**: El proceso simplemente descarta la señal y continúa la ejecución.
- **Capturar la señal**: El proceso ejecuta una función personalizada llamada manejador de señales para responder al evento.
- **Realizar la acción predeterminada**: Si no se captura ni se ignora, se realiza la acción predeterminada. Para muchas señales, esto significa terminar el proceso.
- **Bloquear la señal**: Si la señal está en la máscara de señales del proceso, permanece pendiente hasta que se desbloquea.

### Señales Comunes de Procesos de Linux

Cada señal se define por un número entero, pero casi siempre se hace referencia a ellas por sus nombres simbólicos (el **código sig del so**), que comienzan con `SIG`. Si bien los números pueden variar ligeramente entre arquitecturas, los nombres son consistentes. Aquí están algunas de las **señales de procesos de linux** más comunes:

- **SIGHUP (1)**: Desconexión. A menudo se utiliza para indicar a un demonio que recargue su configuración.
- **SIGINT (2)**: Interrupción. Enviada por `Ctrl-C`. Es una solicitud para terminar el proceso.
- **SIGKILL (9)**: Matar. Esta es una terminación inmediata y forzosa. El proceso no puede capturar, ignorar o bloquear esta señal.
- **SIGSEGV (11)**: Fallo de Segmentación. Indica que el proceso realizó una referencia de memoria inválida.
- **SIGTERM (15)**: Terminación. Esta es la forma estándar y cortés de solicitar la terminación de un proceso. Es la señal predeterminada enviada por el comando `kill`. Un proceso puede capturar esta señal para realizar la limpieza antes de salir. A esto se le conoce a menudo como **señal 15 linux**.
- **SIGSTOP**: Detener. Pausa el proceso. Al igual que SIGKILL, no se puede capturar ni ignorar.

La diferencia clave entre `SIGTERM` (**señal linux 15**) y `SIGKILL` es que `SIGTERM` es una solicitud que puede ser manejada, mientras que `SIGKILL` es un comando que destruye el proceso inmediatamente.

## Exercise

¡La práctica hace al maestro! Aquí hay un laboratorio práctico para reforzar su comprensión de los procesos y cómo se utilizan las señales para interactuar con ellos:

1. **[Gestionar y Supervisar Procesos de Linux](https://labex.io/es/labs/comptia-manage-and-monitor-linux-processes-590864)** - En este laboratorio, aprenderá habilidades esenciales para gestionar y supervisar procesos en un sistema Linux. Explorará cómo interactuar con procesos en primer plano y en segundo plano, inspeccionarlos con `ps`, supervisar recursos con `top`, ajustar la prioridad con `renice` y terminarlos con `kill`. Terminar procesos con `kill` es una aplicación directa del envío de señales.

Este laboratorio le ayudará a aplicar los conceptos de gestión de procesos y el uso subyacente de señales en escenarios reales y a ganar confianza con la administración de sistemas Linux.

## Quiz Question

¿Qué señal no se puede bloquear? Por favor, responda en inglés, usando el nombre exacto de la señal y prestando atención a las mayúsculas.

## Quiz Answer

SIGKILL
