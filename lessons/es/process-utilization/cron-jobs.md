---
index: 8
lang: "es"
title: "Trabajos Cron"
meta_title: "Trabajos Cron - Utilización de Procesos"
meta_description: "Aprenda a programar tareas y automatizar scripts en Linux usando trabajos cron. Esta guía cubre la sintaxis de crontab, comandos esenciales como crontab -e, y ejemplos prácticos para principiantes."
meta_keywords: "trabajos cron, crontab, programar tareas, automatización Linux, comandos Linux, Linux para principiantes, tutorial Linux, crontab -e, cron"
---

## Lesson Content

Si bien la utilización de procesos es importante, también es un buen momento para introducir una herramienta potente para la `automatización de Linux`: el demonio `cron`. Este servicio en segundo plano le permite `programar tareas` para que se ejecuten automáticamente en momentos o intervalos específicos. Estas tareas programadas se conocen comúnmente como `trabajos cron` (cron jobs). Esto es increíblemente útil para automatizar acciones rutinarias, como ejecutar un script de respaldo cada noche o limpiar archivos temporales una vez a la semana.

### ¿Qué son los Trabajos Cron?

Imagine que tiene un script en `/home/pete/scripts/change_wallpaper` que ejecuta cada mañana para establecer un nuevo fondo de escritorio. En lugar de ejecutarlo manualmente cada día, puede crear un `trabajo cron` para ejecutarlo por usted. Al definir un horario, puede indicarle al servicio `cron` exactamente cuándo ejecutar su script, convirtiéndolo en una verdadera solución de "configúrelo y olvídese".

### Entendiendo la Sintaxis de Crontab

Para crear un `trabajo cron`, debe especificar el horario y el comando a ejecutar. El horario se define mediante cinco campos, seguidos del comando.

```plaintext
30 08 * * * /home/pete/scripts/change_wallpaper
```

Los cinco campos de hora y fecha son, de izquierda a derecha:

- **Minuto:** 0-59
- **Hora:** 0-23 (en formato de 24 horas)
- **Día del mes:** 1-31
- **Mes:** 1-12
- **Día de la semana:** 0-7 (donde tanto 0 como 7 representan el domingo)

Un asterisco (`*`) en un campo actúa como un comodín, lo que significa "cada". En el ejemplo anterior, el horario `30 08 * * *` le indica a `cron` que ejecute el comando a las 8:30 AM, todos los días del mes, todos los meses y todos los días de la semana.

### Gestión de Trabajos Cron con Crontab

Usted administra sus `trabajos cron` personales utilizando el comando `crontab`, que le permite editar el archivo crontab específico de su usuario. Este archivo contiene todos los `trabajos cron` que ha programado.

Para agregar o editar sus `trabajos cron`, use la opción `-e` (editar). Esto abrirá su archivo crontab en su editor de texto predeterminado.

```bash
crontab -e
```

Una vez que agregue la definición de su trabajo y guarde el archivo, `cron` leerá automáticamente el nuevo horario. También puede listar sus `trabajos cron` activos con `crontab -l` o eliminarlos todos con `crontab -r`. Usar `trabajos cron` es una habilidad fundamental para cualquier persona interesada en la `automatización de Linux`.

## Exercise

¡La práctica hace al maestro! Este laboratorio práctico le ayudará a reforzar su comprensión sobre cómo `programar tareas` en Linux.

1. **[Programar Tareas con at y cron en Linux](https://labex.io/es/labs/comptia-schedule-tasks-with-at-and-cron-in-linux-590870)** - Practique la creación, gestión y eliminación de trabajos con `at`, `atq`, `atrm` y `crontab`, obteniendo experiencia práctica en la automatización de tareas de administración del sistema.

Este laboratorio le ayudará a aplicar los conceptos de esta lección en un escenario del mundo real y a aumentar su confianza con la `automatización de Linux`.

## Quiz Question

¿Cuál es el comando para editar sus trabajos cron personales? (Por favor, responda usando el comando exacto en minúsculas y su opción).

## Quiz Answer

crontab -e
