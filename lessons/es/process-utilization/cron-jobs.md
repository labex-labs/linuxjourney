---
index: 8
lang: "es"
title: "Trabajos Cron"
meta_title: "Trabajos Cron - Utilización de Procesos"
meta_description: "Aprende a programar tareas en Linux con trabajos cron. Comprende la sintaxis de crontab y automatiza scripts para operaciones diarias. ¡Empieza con esta guía para principiantes!"
meta_keywords: "trabajos cron, crontab, programar tareas, automatización Linux, comandos Linux, Linux para principiantes, tutorial Linux, crontab -e"
---

## Lesson Content

Aunque hemos estado hablando sobre la utilización de recursos, creo que este sería un buen momento para mencionar una herramienta útil en Linux que se utiliza para programar tareas usando cron. Hay un servicio que ejecuta programas por ti en el momento que lo programes. Esto es realmente útil si tienes un script que quieres ejecutar una vez al día y que necesita realizar algo por ti.

Por ejemplo, digamos que tengo un script ubicado en `/home/pete/scripts/change_wallpaper`. Uso este script todas las mañanas para cambiar la imagen que uso como fondo de pantalla, pero cada mañana tengo que ejecutar este script manualmente. En su lugar, lo que puedo hacer es crear un trabajo cron que ejecute mi script a través de cron. Puedo especificar la hora en que quiero que se ejecute este trabajo cron y ejecute mi script.

```plaintext
30 08 * * * /home/pete/scripts/change_wallpaper
```

Los campos son los siguientes de izquierda a derecha:

- Minuto - (0-59)
- Hora - (0-23)
- Día del mes - (1-31)
- Mes - (1-12)
- Día de la semana - (0-7). 0 y 7 se denotan como domingo

El asterisco en el campo significa que coincide con cada valor. Así que en mi ejemplo anterior, quiero que esto se ejecute todos los días de cada mes a las 8:30 AM.

Para crear un trabajo cron, simplemente edita el archivo crontab:

```bash
crontab -e
```

## Exercise

¡La práctica hace al maestro! Aquí tienes algunos laboratorios prácticos para reforzar tu comprensión de la programación de tareas en Linux:

1. **[Programar tareas con at y cron en Linux](https://labex.io/es/labs/comptia-schedule-tasks-with-at-and-cron-in-linux-590870)** - Practica la creación, gestión y eliminación de trabajos con `at`, `atq`, `atrm` y `crontab`, obteniendo experiencia práctica en la automatización de tareas de administración del sistema.

Este laboratorio te ayudará a aplicar los conceptos en escenarios reales y a generar confianza con la programación de tareas.

## Quiz Question

¿Cuál es el comando para editar tus trabajos cron?

## Quiz Answer

crontab -e
