---
index: 8
lang: "es"
title: "head"
meta_title: "head - Text-Fu"
meta_description: "Guía de Linux para principiantes sobre el uso del comando head para ver el inicio de un archivo. Aprenda a usar la opción head -n para controlar el número de líneas, una habilidad esencial para cualquier tutorial de Linux."
meta_keywords: "comando head, Linux head, ver inicio archivo, tutorial Linux, comandos Linux, Linux principiantes, head -n, guía Linux, archivos de texto, línea de comandos"
---

## Lesson Content

En Linux, a menudo necesitas inspeccionar el contenido de archivos muy grandes, como los registros del sistema (logs). Por ejemplo, si ejecutas `cat /var/log/syslog`, verás páginas de texto desplazarse, lo que dificulta obtener una visión general rápida. Entonces, ¿qué pasa si solo quieres **ver el principio de un archivo**? El comando `head` es la herramienta perfecta para este trabajo.

### Comportamiento Predeterminado del Comando head

Por defecto, el comando `head` muestra las primeras 10 líneas de cualquier archivo dado. Esta es una parte fundamental de nuestra **guía de Linux para principiantes** para manejar texto. Para verlo en acción, simplemente proporciona un nombre de archivo como argumento:

```bash
head /var/log/syslog
```

Este comando mostrará las primeras 10 líneas de `/var/log/syslog`, permitiéndote verificar rápidamente el contenido inicial del archivo sin abrirlo en un editor.

### Personalización del Conteo de Líneas

El comando **Linux head** es flexible. Puedes cambiar fácilmente el número de líneas que muestra usando la bandera `-n`, que significa "número de líneas". Por ejemplo, si deseas ver las primeras 15 líneas de un archivo, usarías la opción `head -n` de esta manera:

```bash
head -n 15 /var/log/syslog
```

Esto convierte a `head` en uno de los **comandos de Linux** más útiles para inspeccionar rápidamente encabezados de archivos o entradas de registro.

## Exercise

¡La práctica hace al maestro! Aquí tienes algunos laboratorios prácticos para reforzar tu comprensión de la visualización del principio de archivos y la manipulación general de archivos de texto:

1. **[Comando Linux head: Visualización del Principio de Archivo](https://labex.io/es/labs/linux-linux-head-command-file-beginning-display-214302)** - Este laboratorio te guiará en el uso del comando `head` para mostrar las líneas iniciales de archivos de texto, incluyendo la modificación del número de líneas.
2. **[Visualización de Archivos de Registro y Configuración en Linux](https://labex.io/es/labs/linux-viewing-log-and-configuration-files-in-linux-387914)** - Practica habilidades esenciales de la línea de comandos de Linux para ver y navegar eficientemente por archivos de texto, incluidos registros del sistema y archivos de configuración, que a menudo requieren comandos como `head`.
3. **[Detección Rápida de Amenazas](https://labex.io/es/labs/linux-rapid-threat-detection-387930)** - Aplica tu conocimiento de `head` (y `tail`) para extraer y analizar rápidamente entradas de registro recientes, simulando análisis de ciberseguridad del mundo real.

Estos laboratorios te ayudarán a aplicar los conceptos en escenarios reales y a ganar confianza con la visualización y el análisis de archivos de texto en Linux.

## Quiz Question

¿Qué bandera usarías con el comando `head` para cambiar el número de líneas que deseas ver? Por favor, responde usando solo la bandera en inglés, prestando atención a la sensibilidad a mayúsculas y minúsculas.

## Quiz Answer

-n
