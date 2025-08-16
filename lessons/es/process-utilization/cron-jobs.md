---
lang: "es"
title: "Cron Jobs"
description: "Aprende a programar tareas en Linux con cron jobs. Comprende la sintaxis de crontab y automatiza scripts para operaciones diarias. ¡Empieza con esta guía para principiantes!"
keywords: "cron jobs, crontab, programar tareas, automatización Linux, comandos Linux, Linux para principiantes, tutorial Linux, crontab -e"
---

## Lesson Content

Aunque hemos estado hablando sobre la utilización de recursos, creo que este sería un buen punto para mencionar una herramienta útil en Linux que se utiliza para programar tareas usando cron. Hay un servicio que ejecuta programas por ti a la hora que programes. Esto es realmente útil si tienes un script que quieres ejecutar una vez al día y que necesita ejecutar algo por ti.

Por ejemplo, digamos que tengo un script ubicado en `/home/pete/scripts/change_wallpaper`. Uso este script todas las mañanas para cambiar la imagen que uso como fondo de pantalla, pero cada mañana tengo que ejecutarlo manualmente. En su lugar, lo que puedo hacer es crear un cron job que ejecute mi script a través de cron. Puedo especificar la hora a la que quiero que se ejecute este cron job y mi script.

```plaintext
30 08 * * * /home/pete/scripts/change_wallpaper
```

Los campos son los siguientes de izquierda a derecha:

- Minute - (0-59)
- Hour - (0-23)
- Day of the month - (1-31)
- Month - (1-12)
- Day of the week - (0-7). 0 and 7 are denoted as Sunday

El asterisco en el campo significa que coincide con cada valor. Así que en mi ejemplo anterior, quiero que esto se ejecute todos los días de cada mes a las 8:30 AM.

Para crear un cron job, simplemente edita el archivo crontab:

```bash
crontab -e
```

## Exercise

Crea un cron job que quieras ejecutar a una hora programada.

## Quiz Question

¿Cuál es el comando para editar tus cron jobs?

## Quiz Answer

crontab -e
