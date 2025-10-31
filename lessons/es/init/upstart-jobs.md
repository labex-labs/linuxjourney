---
index: 4
lang: "es"
title: "Trabajos Upstart"
meta_title: "Trabajos Upstart - Init"
meta_description: "Una guía para gestionar servicios con trabajos Upstart en un entorno Linux. Aprenda a usar la utilidad initctl para listar, iniciar, detener y reiniciar trabajos en un sistema Linux upstart."
meta_keywords: "Trabajos Upstart, initctl, upstart linux, servicios Linux, administración de sistemas, sistema init, tutorial Linux"
---

## Lesson Content

Upstart es un sistema init basado en eventos utilizado en algunas distribuciones **upstart linux** para gestionar servicios y tareas durante el arranque y mientras el sistema está en ejecución. Opera a través de un sistema de trabajos (jobs) y eventos. Si bien rastrear el origen de cada evento puede ser complejo, a menudo requiere explorar las configuraciones de trabajos en `/etc/init`, es más común que necesite administrar estos trabajos directamente desde la línea de comandos. La utilidad `initctl` proporciona un conjunto de comandos para este propósito.

### Ver el Estado de los Trabajos

Para ver una lista de todos los trabajos de Upstart conocidos y sus estados actuales, use el comando `list`.

```plaintext
initctl list

shutdown stop/waiting
console stop/waiting
...
```

La salida muestra el nombre del trabajo, su objetivo y su estado actual. En el ejemplo `shutdown stop/waiting`, el nombre del trabajo es `shutdown`, su objetivo es `stop` y su estado actual es `waiting`. El estado y los objetivos del trabajo cambiarán a medida que interactúe con ellos.

Para verificar el estado de un trabajo específico, use el comando `status`.

```plaintext
initctl status networking
networking start/running
```

### Control Manual de Trabajos

Aunque los archivos de configuración de trabajos en `/etc/init` definen cómo inician, detienen e interactúan los trabajos con los eventos, puede anular manualmente estas acciones usando `initctl`. Esto es útil para la solución de problemas o para realizar tareas administrativas.

Para iniciar un trabajo manualmente:

```bash
sudo initctl start networking
```

Para detener un trabajo manualmente:

```bash
sudo initctl stop networking
```

Para reiniciar un trabajo manualmente, que es un atajo conveniente para detenerlo y luego iniciarlo:

```bash
sudo initctl restart networking
```

### Emitir Eventos Personalizados

Los trabajos de Upstart se activan mediante eventos. También puede "emitir" manualmente un evento, lo que puede ser útil para activar trabajos personalizados o con fines de prueba. Cualquier trabajo configurado para iniciarse con `some_event` sería activado por el siguiente comando.

```bash
sudo initctl emit some_event
```

## Exercise

¡La práctica hace al maestro! Si bien no hay laboratorios específicos para Upstart, comprender cómo programar y administrar tareas es crucial para controlar los procesos del sistema. Aquí hay un laboratorio práctico para reforzar su comprensión de la administración de tareas:

1. **[Programar Tareas con at y cron en Linux](https://labex.io/es/labs/comptia-schedule-tasks-with-at-and-cron-in-linux-590870)** - Practique la creación, administración y eliminación de trabajos únicos y recurrentes, que son conceptos fundamentales relacionados con la forma en que se administran los servicios y tareas en entornos Linux como los manejados por Upstart.

Este laboratorio le ayudará a aplicar los conceptos de automatización de tareas en escenarios reales y a ganar confianza en la administración de operaciones del sistema.

## Quiz Question

¿Cómo reiniciaría manualmente un trabajo de Upstart llamado `peanuts`? Por favor, proporcione el comando completo. (Nota: La respuesta distingue entre mayúsculas y minúsculas y debe estar en inglés.)

## Quiz Answer

sudo initctl restart peanuts
