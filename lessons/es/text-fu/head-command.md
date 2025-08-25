---
index: 8
lang: "es"
title: "head"
meta_title: "head - Text-Fu"
meta_description: "Aprende a usar el comando 'head' de Linux para ver el principio de los archivos. Comprende opciones como -n para el recuento de líneas. Tutorial esencial de comandos de Linux."
meta_keywords: "comando head, head de Linux, ver inicio de archivo, tutorial de Linux, comandos de Linux, Linux para principiantes, head -n, guía de Linux"
---

## Lesson Content

Digamos que tenemos un archivo muy largo; de hecho, tenemos muchos para elegir. Adelante, `cat /var/log/syslog`. Deberías ver páginas y páginas de texto. ¿Qué pasaría si solo quisiera ver las primeras líneas de este archivo de texto? Bueno, podemos hacerlo con el comando `head`. Por defecto, el comando `head` te mostrará las primeras 10 líneas de un archivo.

```bash
head /var/log/syslog
```

También puedes modificar el número de líneas a tu elección. Digamos que quisiera ver las primeras 15 líneas en su lugar.

```bash
head -n 15 /var/log/syslog
```

La bandera `-n` significa "número de líneas".

## Exercise

¡La práctica hace al maestro! Aquí tienes algunos laboratorios prácticos para reforzar tu comprensión de la visualización del inicio de archivos y la manipulación general de archivos de texto:

1. **[Comando head de Linux: Visualización del inicio de archivos](https://labex.io/es/labs/linux-linux-head-command-file-beginning-display-214302)** - Este laboratorio te guiará a través del uso del comando `head` para mostrar las líneas iniciales de archivos de texto, incluyendo la modificación del recuento de líneas.
2. **[Visualización de archivos de registro y configuración en Linux](https://labex.io/es/labs/linux-viewing-log-and-configuration-files-in-linux-387914)** - Practica habilidades esenciales de la línea de comandos de Linux para ver y navegar eficientemente por archivos de texto, incluyendo registros del sistema y archivos de configuración, que a menudo requieren comandos como `head`.
3. **[Detección rápida de amenazas](https://labex.io/es/labs/linux-rapid-threat-detection-387930)** - Aplica tus conocimientos de `head` (y `tail`) para extraer y analizar rápidamente entradas de registro recientes, simulando un análisis de ciberseguridad del mundo real.

Estos laboratorios te ayudarán a aplicar los conceptos en escenarios reales y a desarrollar confianza con la visualización y el análisis de archivos de texto en Linux.

## Quiz Question

¿Qué bandera usarías para cambiar el número de líneas que quieres ver para el comando `head`?

## Quiz Answer

-n
