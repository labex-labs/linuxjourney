---
index: 10
lang: "es"
title: "Sistema de archivos /proc"
meta_title: "Sistema de archivos /proc - Procesos"
meta_description: "Aprende sobre el sistema de archivos /proc en Linux, cómo almacena la información de los procesos y su estructura. Explora los detalles de los procesos con esta guía esencial de Linux."
meta_keywords: "sistema de archivos /proc, procesos de Linux, información de procesos, tutorial de Linux, Linux para principiantes, guía de Linux"
---

## Lesson Content

Recuerda, todo en Linux es un archivo, incluso los procesos. La información del proceso se almacena en un sistema de archivos especial conocido como el sistema de archivos `/proc`.

```bash
ls /proc
```

Deberías ver múltiples valores aquí; hay subdirectorios para cada PID. Si buscaras un PID en la salida de `ps`, podrías encontrarlo en el directorio `/proc`.

Continúa y entra en uno de los procesos y mira ese archivo:

```bash
cat /proc/12345/status
```

Deberías ver información del estado del proceso, así como información más detallada. El directorio `/proc` es cómo el kernel ve el sistema, por lo que hay mucha más información aquí de la que verías en `ps`.

## Exercise

No exercises for this lesson.

## Quiz Question

¿Qué sistema de archivos almacena la información del proceso?

## Quiz Answer

/proc
