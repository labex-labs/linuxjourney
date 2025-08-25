---
index: 3
lang: "es"
title: "Visión General de Upstart"
meta_title: "Visión General de Upstart - Init"
meta_description: "Aprende sobre Upstart, su modelo basado en eventos y cómo gestiona los servicios en Linux. Comprende las configuraciones de trabajos de Upstart y su papel como sistema init."
meta_keywords: "Upstart, sistema init, servicios Linux, Ubuntu, SysV, tutorial para principiantes, guía Linux"
---

## Lesson Content

Upstart fue desarrollado por Canonical, por lo que fue la implementación de init en Ubuntu por un tiempo; sin embargo, en las instalaciones modernas de Ubuntu, ahora se usa systemd. Upstart fue creado para mejorar los problemas con SysV, como los procesos de inicio estrictos, el bloqueo de tareas, etc. El modelo de Upstart basado en eventos y trabajos le permite responder a los eventos a medida que ocurren.

Para saber si estás usando Upstart, si tienes un directorio `/usr/share/upstart`, es un buen indicador.

Los trabajos son las acciones que realiza Upstart, y los eventos son mensajes que se reciben de otros procesos para activar trabajos. Para ver una lista de trabajos y su configuración:

```plaintext
pete@icebox:~$ ls /etc/init
acpid.conf                   mountnfs.sh.conf
alsa-restore.conf            mtab.sh.conf
alsa-state.conf              networking.conf
alsa-store.conf              network-interface.conf
anacron.conf                 network-interface-container.conf
```

Dentro de estas configuraciones de trabajo, encontrarás información sobre cómo y cuándo iniciar los trabajos.

Por ejemplo, en el archivo `networking.conf`, podría decir algo tan simple como:

```plaintext
start on runlevel [235]
stop on runlevel [0]
```

Esto significa que comenzará a configurar la red en los niveles de ejecución 2, 3 o 5 y detendrá la red en el nivel de ejecución 0. Hay muchas maneras de escribir el archivo de configuración, y lo descubrirás cuando observes las diferentes configuraciones de trabajo disponibles.

La forma en que funciona Upstart es la siguiente:

1. Primero, carga las configuraciones de trabajo desde `/etc/init`.
2. Una vez que ocurre un evento de inicio, ejecutará los trabajos activados por ese evento.
3. Estos trabajos crearán nuevos eventos, y luego esos eventos activarán más trabajos.
4. Upstart continúa haciendo esto hasta que completa todos los trabajos necesarios.

## Exercise

¡La práctica hace al maestro! Aunque Upstart es un sistema init más antiguo, comprender cómo se gestionan los procesos y se programan las tareas es crucial para cualquier administrador de Linux. Aquí hay algunos laboratorios prácticos para reforzar su comprensión de la gestión de procesos y la automatización de tareas, que son fundamentales para el funcionamiento de los sistemas init:

1. **[Gestionar y Monitorizar Procesos de Linux](https://labex.io/es/labs/comptia-manage-and-monitor-linux-processes-590864)** - Practique la interacción con procesos en primer y segundo plano, inspeccionándolos con `ps`, monitorizando recursos con `top` y terminándolos con `kill`. Este laboratorio le ayuda a comprender el ciclo de vida de los procesos, que los sistemas init como Upstart gestionan.
2. **[Programar Tareas con at y cron en Linux](https://labex.io/es/labs/comptia-schedule-tasks-with-at-and-cron-in-linux-590870)** - Aprenda a programar trabajos únicos con `at` y tareas recurrentes con `cron`. Esto proporciona experiencia práctica con la automatización de tareas, una función central que los sistemas init facilitan para los servicios del sistema.

Estos laboratorios le ayudarán a aplicar los conceptos de control de procesos y automatización de tareas en escenarios reales, generando confianza en la gestión de un sistema Linux, independientemente del sistema init específico en uso.

## Quiz Question

¿Cuál es la implementación de init utilizada por Ubuntu?

## Quiz Answer

upstart
