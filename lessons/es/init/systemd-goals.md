---
lang: "es"
title: "Objetivos de Systemd"
meta_title: "Objetivos de Systemd - Init"
meta_description: "Aprende los conceptos básicos de las unidades systemd y los comandos esenciales de systemctl. Comprende cómo gestionar servicios, ver estados y habilitar unidades en Linux. ¡Comienza tu viaje!"
meta_keywords: "systemd, systemctl, servicios de Linux, archivos de unidad, principiante, tutorial, guía, comandos de Linux"
---

## Lesson Content

No entraremos en los detalles de cómo escribir archivos de unidad systemd. Sin embargo, haremos un breve resumen de un archivo de unidad y cómo controlar unidades manualmente.

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

Este es un objetivo de servicio simple. Al principio del archivo, vemos una sección para `[Unit]`. Esto nos permite darle una descripción a nuestro archivo de unidad, así como controlar el orden de activación de la unidad. La siguiente parte es la sección `[Service]`; aquí, podemos iniciar, detener o recargar un servicio. Y la sección `[Install]` se utiliza para las dependencias. Esto es solo la punta del iceberg para escribir archivos systemd, así que te imploro que leas sobre el tema si quieres saber más.

Ahora, veamos algunos comandos que puedes usar con las unidades systemd:

### List units

```bash
systemctl list-units
```

### View status of unit

```bash
systemctl status networking.service
```

### Start a service

```bash
sudo systemctl start networking.service
```

### Stop a service

```bash
sudo systemctl stop networking.service
```

### Restart a service

```bash
sudo systemctl restart networking.service
```

### Enable a unit

```bash
sudo systemctl enable networking.service
```

### Disable a unit

```bash
sudo systemctl disable networking.service
```

De nuevo, aún no has visto la profundidad que alcanza systemd, así que lee sobre ello si quieres aprender más.

## Exercise

Consulta los estados de las unidades e inicia y detén algunos servicios. ¿Qué observas?

## Quiz Question

¿Cuál es el comando para iniciar un servicio llamado peanut.service?

## Quiz Answer

sudo systemctl start peanut.service
