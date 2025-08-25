---
index: 6
lang: "es"
title: "Objetivos de Systemd"
meta_title: "Objetivos de Systemd - Init"
meta_description: "Aprende los conceptos básicos de las unidades systemd y los comandos esenciales de systemctl. Comprende cómo gestionar servicios, ver estados y habilitar unidades en Linux. ¡Comienza tu viaje!"
meta_keywords: "systemd, systemctl, servicios Linux, archivos de unidad, principiante, tutorial, guía, comandos Linux"
---

## Lesson Content

No entraremos en los detalles de la escritura de archivos de unidad systemd. Sin embargo, haremos un breve resumen de un archivo de unidad y cómo controlar las unidades manualmente.

Aquí hay un archivo de unidad de servicio básico: foobar.service

```
[Unit]
Description=My Foobar
Before=bar.target

[Service]
ExecStart=/usr/bin/foobar

[Install]
WantedBy=multi-user.target
```

Este es un objetivo de servicio simple. Al principio del archivo, vemos una sección para `[Unit]`. Esto nos permite dar una descripción a nuestro archivo de unidad, así como controlar el orden de activación de la unidad. La siguiente parte es la sección `[Service]`; aquí, podemos iniciar, detener o recargar un servicio. Y la sección `[Install]` se utiliza para las dependencias. Esto es solo la punta del iceberg para escribir archivos systemd, así que te imploro que leas sobre el tema si quieres saber más.

Ahora, veamos algunos comandos que puedes usar con las unidades systemd:

### Listar unidades

```bash
systemctl list-units
```

### Ver el estado de la unidad

```bash
systemctl status networking.service
```

### Iniciar un servicio

```bash
sudo systemctl start networking.service
```

### Detener un servicio

```bash
sudo systemctl stop networking.service
```

### Reiniciar un servicio

```bash
sudo systemctl restart networking.service
```

### Habilitar una unidad

```bash
sudo systemctl enable networking.service
```

### Deshabilitar una unidad

```bash
sudo systemctl disable networking.service
```

De nuevo, aún no has visto la profundidad que alcanza systemd, así que lee sobre ello si quieres aprender más.

## Exercise

¡La práctica hace al maestro! Aquí tienes algunos laboratorios prácticos para reforzar tu comprensión de la gestión de procesos, que a menudo son controlados por los servicios systemd:

1. **[Gestionar y Monitorizar Procesos Linux](https://labex.io/es/labs/comptia-manage-and-monitor-linux-processes-590864)** - Practica la interacción con procesos en primer y segundo plano, inspeccionándolos con `ps`, monitorizando recursos con `top`, ajustando la prioridad con `renice`, y terminándolos con `kill`. Este laboratorio te dará experiencia práctica con los efectos en tiempo de ejecución de la gestión de unidades systemd.

Estos laboratorios te ayudarán a aplicar los conceptos en escenarios reales y a desarrollar confianza con la gestión de procesos en Linux.

## Quiz Question

¿Cuál es el comando para iniciar un servicio llamado peanut.service?

## Quiz Answer

sudo systemctl start peanut.service
