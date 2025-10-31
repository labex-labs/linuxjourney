---
index: 6
lang: "es"
title: "Objetivos de Systemd"
meta_title: "Objetivos de Systemd - Init"
meta_description: "Explore los objetivos de systemd y aprenda a gestionar servicios de Linux usando comandos esenciales de systemctl. Esta guía cubre los conceptos básicos de los archivos de unidad de systemd, cómo iniciar, detener y habilitar servicios, y ver su estado."
meta_keywords: "systemd, systemctl, servicios Linux, archivos de unidad, objetivos systemd, gestión de servicios, unidades systemd, principiante, tutorial, guía, comandos Linux"
---

## Lesson Content

Esta lección proporciona una visión general fundamental de los archivos de unidad de systemd y cómo administrarlos con `systemctl`, la herramienta principal para controlar el sistema init. Cubriremos la estructura básica de un archivo de unidad y los comandos esenciales para administrar servicios de Linux.

### Entendiendo un Archivo de Unidad de Systemd

Un archivo de unidad de systemd es un archivo de texto plano que describe un servicio, un punto de montaje, un dispositivo u otro recurso que systemd puede administrar. Aquí hay un ejemplo básico de un archivo de unidad de servicio llamado `foobar.service`:

```
[Unit]
Description=Mi Servicio Foobar
After=network.target

[Service]
ExecStart=/usr/bin/foobar

[Install]
WantedBy=multi-user.target
```

Este archivo de servicio simple se divide en secciones:

- **[Unit]**: Esta sección contiene metadatos e información de dependencia. La directiva `Description` proporciona un nombre legible por humanos para la unidad. Directivas como `After` y `Before` controlan el orden de inicio, asegurando que esta unidad comience después de que la red esté disponible.
- **[Service]**: Esta sección define cómo administrar el servicio. La directiva `ExecStart` es crucial, ya que especifica el comando a ejecutar para iniciar el servicio. Otras directivas como `ExecStop` y `ExecReload` pueden definir cómo detener o recargar el servicio.
- **[Install]**: Esta sección define el comportamiento de la unidad cuando se habilita o deshabilita con `systemctl`. La directiva `WantedBy` le indica a systemd que inicie este servicio como parte de un objetivo específico, como `multi-user.target` para un arranque estándar no gráfico.

Este es solo un vistazo a los archivos de unidad de systemd. Para configuraciones más avanzadas, se recomienda encarecidamente una lectura adicional sobre el tema.

### Comandos Esenciales de Systemctl

Ahora, exploremos los comandos esenciales de `systemctl` que utilizará para interactuar con las unidades de systemd y administrar los servicios de Linux.

### Listar Unidades de Systemd

Para ver todas las unidades activas que systemd está administrando actualmente, use el comando `list-units`.

```bash
systemctl list-units
```

### Verificar el Estado de una Unidad

Para ver el estado detallado de una unidad específica, incluyendo si está activa, habilitada y sus entradas de registro más recientes, use el comando `status`.

```bash
systemctl status networking.service
```

### Administrar Estados de Servicio

Puede controlar el estado de tiempo de ejecución de un servicio usando `start`, `stop` y `restart`.

Para iniciar un servicio inmediatamente:

```bash
sudo systemctl start networking.service
```

Para detener un servicio en ejecución:

```bash
sudo systemctl stop networking.service
```

Para detener y luego iniciar el servicio nuevamente:

```bash
sudo systemctl restart networking.service
```

### Habilitar y Deshabilitar Servicios

Habilitar un servicio crea un enlace simbólico que lo conecta al proceso de arranque, asegurando que comience automáticamente. Deshabilitarlo elimina ese enlace.

Para habilitar un servicio para que comience al arrancar:

```bash
sudo systemctl enable networking.service
```

Para deshabilitar un servicio para que no comience al arrancar:

```bash
sudo systemctl disable networking.service
```

Estos comandos son los bloques de construcción para la administración de servicios en los sistemas Linux modernos. Dominarlos es un paso clave en su trayectoria en Linux.

## Exercise

La práctica es clave para dominar nuevas habilidades. Este laboratorio práctico le ayudará a reforzar su comprensión de la administración de procesos, que a menudo son controlados por servicios systemd:

1. **[Administrar y Monitorear Procesos de Linux](https://labex.io/es/labs/comptia-manage-and-monitor-linux-processes-590864)** - Practique la interacción con procesos en primer plano y en segundo plano, inspeccionándolos con `ps`, monitoreando recursos con `top`, ajustando la prioridad con `renice` y terminándolos con `kill`. Este laboratorio le brindará experiencia práctica con los efectos en tiempo de ejecución de la administración de unidades systemd.

Este laboratorio le ayudará a aplicar estos conceptos en un escenario del mundo real y a ganar confianza con la administración de procesos en Linux.

## Quiz Question

What is the command to start a service named peanut.service? Please answer in English. The answer is case-sensitive.

## Quiz Answer

sudo systemctl start peanut.service
