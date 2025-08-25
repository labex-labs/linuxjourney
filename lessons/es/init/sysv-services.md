---
index: 2
lang: "es"
title: "Servicio System V"
meta_title: "Servicio System V - Init"
meta_description: "Aprende a administrar servicios de System V usando herramientas de línea de comandos. Descubre cómo listar, iniciar, detener y reiniciar servicios con este tutorial de Linux para principiantes."
meta_keywords: "servicios System V, servicios Linux, comando service, SysV init, tutorial Linux, Linux para principiantes, gestión de servicios, guía Linux"
---

## Lesson Content

Existen muchas herramientas de línea de comandos que puedes usar para administrar los servicios de Sys V.

### Listar servicios

```bash
service --status-all
```

### Iniciar un servicio

```bash
sudo service networking start
```

### Detener un servicio

```bash
sudo service networking stop
```

### Reiniciar un servicio

```bash
sudo service networking restart
```

Estos comandos no son específicos de los sistemas de inicio Sys V; también puedes usarlos para administrar servicios de Upstart. Dado que Linux está tratando de alejarse de los scripts de inicio Sys V más tradicionales, todavía hay cosas implementadas para ayudar a esa transición.

## Exercise

¡La práctica hace al maestro! Aquí tienes algunos laboratorios prácticos para reforzar tu comprensión de la gestión de procesos y tareas, que son fundamentales para administrar servicios en Linux:

1. **[Administrar y Monitorear Procesos de Linux](https://labex.io/es/labs/comptia-manage-and-monitor-linux-processes-590864)** - Practica la interacción, inspección, monitoreo y terminación de procesos en un entorno Linux real.
2. **[Programar Tareas con at y cron en Linux](https://labex.io/es/labs/comptia-schedule-tasks-with-at-and-cron-in-linux-590870)** - Aprende a automatizar tareas usando `at` para trabajos únicos y `cron` para tareas recurrentes, una habilidad clave para la automatización de servicios.

Estos laboratorios te ayudarán a aplicar los conceptos en escenarios reales y a desarrollar confianza en la gestión de operaciones del sistema.

## Quiz Question

¿Cuál es el comando para detener un servicio llamado `peanut` con Sys V?

## Quiz Answer

sudo service peanut stop
