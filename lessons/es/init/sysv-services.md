---
index: 2
lang: "es"
title: "Servicio System V"
meta_title: "Servicio System V - Init"
meta_description: "Aprenda a gestionar servicios tradicionales System V (SysV) en Linux. Esta guía cubre el uso del comando `service` para listar, iniciar, detener y reiniciar servicios en un sistema init System V."
meta_keywords: "system v, sysv init, servicios linux, comando service, gestionar servicios linux, iniciar servicio, detener servicio, reiniciar servicio, linux system v"
---

## Lesson Content

**System V** (o SysV) es uno de los sistemas de inicialización clásicos en sistemas operativos tipo Unix. Aunque muchas distribuciones modernas de Linux han migrado a sistemas más nuevos como `systemd`, comprender cómo administrar los servicios de **System V** sigue siendo una habilidad valiosa, ya que muchos sistemas mantienen la compatibilidad con versiones anteriores.

### El comando service

La herramienta principal para interactuar con servicios en un sistema de inicialización **System V** es el comando `service`. Actúa como un script envoltorio, simplificando el proceso de control de servicios.

### Listar todos los servicios

Para obtener una visión general de todos los servicios disponibles y su estado actual, puede usar la opción `--status-all`. Este comando lista cada servicio e indica si se está ejecutando (`+`), si está detenido (`-`), o si su estado es desconocido (`?`).

```bash
service --status-all
```

### Controlar un servicio específico

Para administrar un servicio individual, especifique el nombre del servicio seguido de una acción como `start` (iniciar), `stop` (detener) o `restart` (reiniciar). Estas acciones requieren privilegios administrativos, por lo que normalmente usará `sudo`.

Para iniciar un servicio, como el servicio de red:

```bash
sudo service networking start
```

Para detener un servicio en ejecución:

```bash
sudo service networking stop
```

Para detener y luego iniciar inmediatamente un servicio, lo cual es útil para aplicar cambios de configuración:

```bash
sudo service networking restart
```

Estos comandos no son exclusivos de los sistemas de inicialización **System V**; a menudo puede usarlos para administrar servicios Upstart también. A medida que las distribuciones de Linux continúan evolucionando, las capas de compatibilidad como el comando `service` se mantienen para ayudar a facilitar la transición desde los scripts de inicialización tradicionales.

## Exercise

¡La práctica hace al maestro! Aquí hay algunos laboratorios prácticos para reforzar su comprensión de la administración de procesos y tareas, que son fundamentales para administrar servicios en Linux:

1. **[Administrar y Monitorear Procesos de Linux](https://labex.io/es/labs/comptia-manage-and-monitor-linux-processes-590864)** - Practique la interacción, inspección, monitoreo y terminación de procesos en un entorno Linux real.
2. **[Programar Tareas con at y cron en Linux](https://labex.io/es/labs/comptia-schedule-tasks-with-at-and-cron-in-linux-590870)** - Aprenda a automatizar tareas usando `at` para trabajos únicos y `cron` para tareas recurrentes, una habilidad clave para la automatización de servicios.

Estos laboratorios le ayudarán a aplicar los conceptos en escenarios reales y a ganar confianza en la administración de operaciones del sistema.

## Quiz Question

What is the full command to stop a service named `peanut` on a System V system? Please provide the exact command in English, paying attention to case.

## Quiz Answer

sudo service peanut stop
