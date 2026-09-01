---
lesson_id: "cron-jobs"
course_id: "process-utilization"
lang: "es"
order_index: 8
title: "Trabajos de cron"
description: "Aprende a crear, examinar, probar y operar de forma segura trabajos recurrentes con cron."
meta_title: "Trabajos de cron - Utilización de procesos"
meta_description: "Aprende a programar tareas recurrentes en Linux con cron y crontab, y a probarlas y operarlas con seguridad."
meta_keywords: "trabajos cron, crontab, programar tareas, automatización Linux, crontab -e"
---

Cron ejecuta órdenes de forma recurrente sin un shell interactivo. La automatización repite tanto el comportamiento correcto como los errores, así que prueba la orden, utiliza rutas explícitas, limita los privilegios y planifica el registro y la notificación de fallos antes de programarla.

## Leer una entrada de crontab

Una entrada de crontab de usuario contiene cinco campos de tiempo seguidos de una orden:

```cron
30 8 * * * /home/pete/scripts/change_wallpaper
```

De izquierda a derecha, los campos son minuto, hora, día del mes, mes y día de la semana. Este ejemplo se ejecuta a las 08:30 conforme a la zona horaria aplicable al demonio cron. Un asterisco significa todos los valores permitidos de ese campo.

Cuando están restringidos tanto el día del mes como el día de la semana, muchas implementaciones de cron ejecutan la orden si cualquiera de los campos coincide. Confirma la semántica local antes de crear un horario que utilice ambos.

:::single-choice{#cron-daily-eight-thirty} ¿Cuándo se ejecuta `30 8 * * * command`?

::option[Cada 30 minutos durante ocho horas.]{#cron-every-thirty explanation="Los campos son posiciones de un horario, no una expresión de duración."}
::option[A las 08:30 todos los días.]{#cron-eight-thirty .correct explanation="El minuto 30 y la hora 8 son fijos, mientras que los tres campos de fecha permiten todos los valores."}
::option[A las 30:08 del octavo día de cada mes.]{#cron-invalid-time explanation="Las horas van de 0 a 23 y el ejemplo no restringe el día del mes."}
:::

## Gestionar un crontab de usuario

Edita el crontab del usuario actual con:

```bash
$ crontab -e
```

Muestra las entradas instaladas antes y después de un cambio:

```bash
$ crontab -l
```

`crontab -r` elimina todo el crontab del usuario y puede hacerlo sin abrir un editor. No lo utilices para eliminar una sola línea; edita el crontab y verifica las entradas restantes.

:::single-choice{#cron-list-current-user} ¿Qué orden muestra las entradas de cron instaladas para el usuario actual?

::option[`crontab -l`]{#cron-list .correct explanation="La opción de listado imprime las entradas instaladas para examinarlas."}
::option[`crontab -r`]{#cron-remove-all explanation="Esta opción elimina el crontab en vez de mostrarlo."}
::option[`crontab -e`]{#cron-edit explanation="Esta opción abre el crontab para editarlo en vez de limitarse a mostrarlo."}
:::

## Tener en cuenta el entorno de cron

Cron suele proporcionar un entorno limitado y un shell no interactivo. Utiliza rutas absolutas para las órdenes y los archivos, establece explícitamente las variables necesarias y no dependas de alias, del directorio actual de una terminal ni de archivos de inicio del shell.

Redirige la salida estándar y los errores a un registro controlado o utiliza un mecanismo de notificación apropiado para el sistema. Protege las credenciales con permisos restrictivos y evita incrustar secretos directamente en una orden del crontab.

:::single-choice{#cron-absolute-paths} ¿Por qué debe utilizar una orden de cron rutas y ajustes de entorno explícitos?

::option[Porque cron siempre se ejecuta dentro de la terminal actual del usuario.]{#cron-current-terminal explanation="Los trabajos programados se ejecutan independientemente de una sesión interactiva."}
::option[Porque las rutas absolutas hacen que todas las órdenes se ejecuten como root.]{#cron-path-root explanation="Las rutas seleccionan archivos, pero no conceden privilegios."}
::option[Porque el entorno de cron puede diferir del shell interactivo.]{#cron-limited-environment .correct explanation="Las dependencias explícitas evitan fallos causados por supuestos sobre PATH, el directorio o los archivos de inicio."}
:::

## Probar y evitar solapamientos

Ejecuta el script manualmente como el mismo usuario y con un entorno igualmente mínimo. Haz que devuelva estados de salida útiles y escriba resultados con marcas de tiempo. Después de instalarlo, espera a un horario de prueba inofensivo o realiza una ejecución controlada y verifica el efecto real y los registros.

Si una ejecución puede durar más que su intervalo, diseña el trabajo para la concurrencia o utiliza un mecanismo de bloqueo como `flock` cuando esté disponible:

```cron
*/5 * * * * /usr/bin/flock -n /run/user/1000/report.lock /home/pete/bin/report
```

Elige una ruta de bloqueo que el usuario del trabajo pueda crear de forma segura y decide si resulta aceptable omitir ejecuciones. Cron no garantiza automáticamente que solo se ejecute una instancia.

:::single-choice{#cron-overlapping-runs} ¿Qué riesgo existe cuando un trabajo tarda más que su intervalo programado?

::option[Varias instancias pueden solaparse y competir por recursos.]{#cron-overlap .correct explanation="Cron puede iniciar una ejecución nueva mientras el proceso anterior sigue activo."}
::option[Los cinco campos del horario reciben automáticamente un sexto campo de bloqueo.]{#cron-auto-lock explanation="La sintaxis de crontab no añade exclusión mutua automática."}
::option[El script se convierte permanentemente en un hilo del kernel.]{#cron-kernel-thread explanation="Programar una orden no cambia de esta forma su modelo de procesos."}
:::

## Elegir el planificador apropiado

Cron resulta apropiado para órdenes recurrentes sencillas. Los temporizadores de systemd pueden proporcionar integración de dependencias, recuperación persistente de ejecuciones omitidas, retrasos aleatorios y registros en el journal en equipos con systemd. Los planificadores de aplicaciones o clústeres pueden ser más seguros cuando un trabajo deba ejecutarse exactamente una vez entre varios equipos.

:::single-choice{#cron-cluster-exactly-once} ¿Por qué puede ser inadecuado el cron ordinario de cada equipo para un trabajo de clúster que deba ejecutarse exactamente una vez?

::option[Porque cada entrada de cron está limitada a un carácter.]{#cron-one-character explanation="Las órdenes de crontab pueden contener líneas de órdenes normales."}
::option[Porque cada equipo puede iniciar su propia copia de forma independiente.]{#cron-each-host .correct explanation="Se necesita un mecanismo de coordinación distribuida para imponer una sola ejecución entre los equipos."}
::option[Porque cron no puede ejecutar scripts almacenados en disco.]{#cron-no-scripts explanation="Ejecutar scripts es un uso habitual de cron."}
:::

## Resumen

Ahora puedes operar un trabajo recurrente de cron con supuestos explícitos sobre el horario y la ejecución.

1. Lee los cinco campos de tiempo en el orden definido.
2. Examina y edita crontabs de usuario sin eliminar trabajos ajenos.
3. Define rutas, entorno, registros y tratamiento de credenciales.
4. Prueba como el usuario del trabajo y evita solapamientos no deseados.
5. Elige un planificador que corresponda a los requisitos del equipo y de coordinación.
