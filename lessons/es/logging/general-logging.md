---
index: 3
lang: "es"
title: "Registro General"
meta_title: "Registro General - Registro"
meta_description: "Aprende sobre los archivos de registro de Linux como /var/log/messages y syslog. Comprende sus diferencias para una solución de problemas efectiva del sistema. ¡Comienza tu viaje en Linux!"
meta_keywords: "registros de Linux, syslog, var/log/messages, solución de problemas de Linux, Linux para principiantes, guía de Linux, registros del sistema"
---

## Lesson Content

Hay muchos archivos de registro que puedes ver en tu sistema; muchos importantes se encuentran en `/var/log`. No los revisaremos todos, pero discutiremos un par de los principales.

Hay dos archivos de registro generales que puedes ver para tener una idea de lo que está haciendo tu sistema:

### `/var/log/messages`

Este registro contiene todos los mensajes no críticos y no de depuración, incluidos los mensajes registrados durante el arranque (dmesg), auth, cron, daemon, etc. Es muy útil para tener una idea de cómo está funcionando tu máquina.

### `/var/log/syslog`

Esto registra todo excepto los mensajes de autenticación; es extremadamente útil para depurar errores en tu máquina.

Estos dos registros deberían ser más que suficientes al solucionar problemas con tu sistema. Sin embargo, si solo deseas ver un componente de registro específico, también hay registros separados para ellos.

## Exercise

¡La práctica hace al maestro! Aquí tienes algunos laboratorios prácticos para reforzar tu comprensión sobre cómo ver y analizar archivos de registro:

1. **[Comando tail de Linux: Visualización del final del archivo](https://labex.io/es/labs/linux-linux-tail-command-file-end-display-214303)** - Aprende el comando `tail` de Linux para ver y monitorear el final de los archivos de texto, esencial para el análisis de registros.
2. **[Comando head de Linux: Visualización del inicio del archivo](https://labex.io/es/labs/linux-linux-head-command-file-beginning-display-214302)** - Explora el comando `head` para mostrar las líneas iniciales de los archivos de texto, útil para verificar rápidamente los encabezados de los registros.
3. **[Detección rápida de amenazas](https://labex.io/es/labs/linux-rapid-threat-detection-387930)** - Practica habilidades esenciales de línea de comandos de Linux para el análisis de ciberseguridad, usando `tail` y `head` para extraer y analizar rápidamente las entradas de registro recientes.

Estos laboratorios te ayudarán a aplicar los conceptos de visualización de archivos de registro en escenarios reales y a generar confianza con la monitorización del sistema.

## Quiz Question

¿Qué archivo de registro registra todo excepto los mensajes de autenticación?

## Quiz Answer

syslog
