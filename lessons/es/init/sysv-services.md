---
index: 2
lang: "es"
title: "Servicio System V"
meta_title: "Servicio System V - Init"
meta_description: "Aprende a administrar servicios System V usando herramientas de línea de comandos. Descubre cómo listar, iniciar, detener y reiniciar servicios con este tutorial de Linux para principiantes."
meta_keywords: "servicios System V, servicios Linux, comando service, SysV init, tutorial Linux, Linux para principiantes, gestión de servicios, guía Linux"
---

## Lesson Content

Hay muchas herramientas de línea de comandos que puedes usar para administrar servicios Sys V.

### List services

```bash
service --status-all
```

### Start a service

```bash
sudo service networking start
```

### Stop a service

```bash
sudo service networking stop
```

### Restart a service

```bash
sudo service networking restart
```

Estos comandos no son específicos de los sistemas init de Sys V; también puedes usarlos para administrar servicios Upstart. Dado que Linux está tratando de alejarse de los scripts init de Sys V más tradicionales, todavía hay cosas implementadas para ayudar en esa transición.

## Exercise

Administra un par de servicios y cambia sus estados. ¿Qué observas?

## Quiz Question

¿Cuál es el comando para detener un servicio llamado `peanut` con Sys V?

## Quiz Answer

sudo service peanut stop
