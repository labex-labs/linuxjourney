---
index: 9
lang: "es"
title: "tail"
meta_title: "tail - Text-Fu"
meta_description: "Aprende a usar el comando `tail` en Linux para ver el final de los archivos y monitorear registros. Descubre `tail -f` para actualizaciones en tiempo real. ¡Comienza tu viaje en Linux!"
meta_keywords: "comando tail, tail de Linux, tail -f, ver registros, tutorial de Linux, Linux para principiantes, guía de Linux"
---

## Lesson Content

Similar to the `head` command, the `tail` command lets you see the last 10 lines of a file by default.

```bash
tail /var/log/syslog
```

Along with `head`, you can change the number of lines you want to see.

```bash
tail -n 10 /var/log/syslog
```

Another great option you can use is the `-f` (follow) flag; this will follow the file as it grows. Give it a try and see what happens.

```bash
tail -f /var/log/syslog
```

Your `syslog` file will be continually changing while you interact with your system, and using `tail -f` you can see everything that is getting added to that file.

## Exercise

¡La práctica hace al maestro! Aquí tienes algunos laboratorios prácticos para reforzar tu comprensión del comando `tail` y sus aplicaciones:

1. **[Comando tail de Linux: Visualización del final del archivo](https://labex.io/es/labs/linux-linux-tail-command-file-end-display-214303)** - Aprende el comando `tail` de Linux para ver y monitorear el final de los archivos de texto, incluyendo la opción `-f` para actualizaciones en tiempo real.
2. **[Visualización de archivos de registro y configuración en Linux](https://labex.io/es/labs/linux-viewing-log-and-configuration-files-in-linux-387914)** - Practica el uso de `tail` (junto con `cat` y `more`) para ver y navegar eficientemente por archivos de registro y configuración, lo cual es crucial para la monitorización del sistema.
3. **[Detección rápida de amenazas](https://labex.io/es/labs/linux-rapid-threat-detection-387930)** - Aplica tus conocimientos de `tail` para extraer y analizar rápidamente entradas de registro recientes, simulando la detección rápida de amenazas en un contexto de ciberseguridad.

Estos laboratorios te ayudarán a aplicar los conceptos de visualización y monitoreo del contenido de archivos en escenarios reales y a ganar confianza con el comando `tail`.

## Quiz Question

¿Cuál es la bandera utilizada para seguir un archivo en `tail`?

## Quiz Answer

-f
