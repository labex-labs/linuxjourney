---
index: 4
lang: "es"
title: "Trabajos de Upstart"
meta_title: "Trabajos de Upstart - Init"
meta_description: "Aprenda a gestionar trabajos de Upstart en Linux usando comandos initctl. Entienda el estado del trabajo, inicie, detenga y reinicie servicios. Mejore sus habilidades de administración de sistemas Linux."
meta_keywords: "trabajos de Upstart, initctl, servicios de Linux, administración de sistemas, tutorial de Linux, guía para principiantes"
---

## Lesson Content

Upstart puede activar muchos eventos y trabajos para ejecutarse. Desafortunadamente, no hay una manera fácil de ver dónde se originó un evento o trabajo, por lo que tendrá que investigar las configuraciones de los trabajos en `/etc/init`. La mayoría de las veces, nunca necesitará mirar los archivos de configuración de trabajos de Upstart, pero querrá controlar algunos trabajos específicos más fácilmente. Hay muchos comandos útiles que puede usar en un sistema Upstart.

### Ver trabajos

```plaintext
initctl list

shutdown stop/waiting
console stop/waiting
...
```

Verá una lista de trabajos de Upstart con diferentes estados aplicados a ellos. En cada línea, el nombre del trabajo es el primer valor, y el segundo campo (antes de `/`) es en realidad el objetivo del trabajo. El tercer valor (después de `/`) es el estado actual. Así, vemos que nuestro trabajo `shutdown` eventualmente quiere detenerse, pero actualmente está en estado de espera. El estado y los objetivos del trabajo cambiarán a medida que inicie o detenga trabajos.

### Ver trabajo específico

```plaintext
initctl status networking
networking start/running
```

No entraremos en los detalles de cómo escribir una configuración de trabajo de Upstart; sin embargo, ya sabemos que los trabajos se detienen, inician y reinician en estas configuraciones. Estos trabajos también emiten eventos, por lo que pueden iniciar otros trabajos. Repasaremos los comandos manuales de la operación de Upstart, pero si tiene curiosidad, debería profundizar en los archivos `.conf`.

### Iniciar un trabajo manualmente

```bash
sudo initctl start networking
```

### Detener un trabajo manualmente

```bash
sudo initctl stop networking
```

### Reiniciar un trabajo manualmente

```bash
sudo initctl restart networking
```

### Emitir un evento manualmente

```bash
sudo initctl emit some_event
```

## Exercise

¡La práctica hace al maestro! Si bien no hay laboratorios específicos para Upstart, comprender cómo programar y administrar tareas es crucial para controlar los procesos del sistema. Aquí hay un laboratorio práctico para reforzar su comprensión de la gestión de tareas:

1. **[Programar tareas con at y cron en Linux](https://labex.io/es/labs/comptia-schedule-tasks-with-at-and-cron-in-linux-590870)** - Practique la creación, gestión y eliminación de trabajos únicos y recurrentes, que son conceptos fundamentales relacionados con la forma en que se gestionan los servicios y las tareas en entornos Linux como los manejados por Upstart.

Este laboratorio le ayudará a aplicar los conceptos de automatización de tareas en escenarios reales y a generar confianza en la gestión de operaciones del sistema.

## Quiz Question

¿Cómo reiniciaría manualmente un trabajo de Upstart llamado `peanuts`?

## Quiz Answer

sudo initctl restart peanuts
