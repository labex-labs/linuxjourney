---
index: 10
lang: "es"
title: "/proc filesystem"
meta_title: "/proc filesystem - Procesos"
meta_description: "Aprende sobre el sistema de archivos /proc en Linux, cómo almacena la información de los procesos y su estructura. Explora los detalles de los procesos con esta guía esencial de Linux."
meta_keywords: "sistema de archivos /proc, procesos de Linux, información de procesos, tutorial de Linux, Linux para principiantes, guía de Linux"
---

## Lesson Content

Recuerda, todo en Linux es un archivo, incluso los procesos. La información del proceso se almacena en un sistema de archivos especial conocido como el sistema de archivos `/proc`.

```bash
ls /proc
```

Deberías ver múltiples valores aquí; hay subdirectorios para cada PID. Si buscaras un PID en la salida de `ps`, podrías encontrarlo en el directorio `/proc`.

Continúa e ingresa a uno de los procesos y mira ese archivo:

```bash
cat /proc/12345/status
```

Deberías ver información del estado del proceso, así como información más detallada. El directorio `/proc` es cómo el kernel ve el sistema, por lo que hay mucha más información aquí de la que verías en `ps`.

## Exercise

¡La práctica hace al maestro! Aquí tienes algunos laboratorios prácticos para reforzar tu comprensión de los procesos de Linux y la monitorización del sistema:

1. **[Administrar y Monitorizar Procesos de Linux](https://labex.io/es/labs/comptia-manage-and-monitor-linux-processes-590864)** - En este laboratorio, aprenderás habilidades esenciales para administrar y monitorizar procesos en un sistema Linux. Explorarás cómo interactuar con procesos en primer y segundo plano, inspeccionarlos con `ps`, monitorizar recursos con `top`, ajustar la prioridad con `renice` y terminarlos con `kill`.

Estos laboratorios te ayudarán a aplicar los conceptos en escenarios reales y a desarrollar confianza con la gestión de procesos y la observación del sistema.

## Quiz Question

¿Qué sistema de archivos almacena la información del proceso?

## Quiz Answer

/proc
