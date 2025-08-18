---
index: 3
lang: "es"
title: "Visión general de Upstart"
meta_title: "Visión general de Upstart - Init"
meta_description: "Aprenda sobre Upstart, su modelo basado en eventos y cómo gestiona los servicios en Linux. Comprenda las configuraciones de trabajo de Upstart y su papel como sistema init."
meta_keywords: "Upstart, sistema init, servicios Linux, Ubuntu, SysV, tutorial para principiantes, guía de Linux"
---

## Lesson Content

Upstart fue desarrollado por Canonical, por lo que fue la implementación de init en Ubuntu por un tiempo; sin embargo, en las instalaciones modernas de Ubuntu, ahora se usa systemd. Upstart fue creado para mejorar los problemas con SysV, como procesos de inicio estrictos, bloqueo de tareas, etc. El modelo de Upstart basado en eventos y trabajos le permite responder a los eventos a medida que ocurren.

Para saber si está usando Upstart, si tiene un directorio `/usr/share/upstart`, es un muy buen indicador.

Los trabajos son las acciones que realiza Upstart, y los eventos son mensajes que se reciben de otros procesos para activar trabajos. Para ver una lista de trabajos y su configuración:

```plaintext
pete@icebox:~$ ls /etc/init
acpid.conf                   mountnfs.sh.conf
alsa-restore.conf            mtab.sh.conf
alsa-state.conf              networking.conf
alsa-store.conf              network-interface.conf
anacron.conf                 network-interface-container.conf
```

Dentro de estas configuraciones de trabajo, encontrará información sobre cómo y cuándo iniciar trabajos.

Por ejemplo, en el archivo `networking.conf`, podría decir algo tan simple como:

```
start on runlevel [235]
stop on runlevel [0]
```

Esto significa que comenzará a configurar la red en el runlevel 2, 3 o 5 y detendrá la red en el runlevel 0. Hay muchas maneras de escribir el archivo de configuración, y lo descubrirá cuando observe las diferentes configuraciones de trabajo disponibles.

La forma en que funciona Upstart es que:

1. Primero, carga las configuraciones de trabajo desde `/etc/init`.
2. Una vez que ocurre un evento de inicio, ejecutará los trabajos activados por ese evento.
3. Estos trabajos crearán nuevos eventos, y luego esos eventos activarán más trabajos.
4. Upstart continúa haciendo esto hasta que completa todos los trabajos necesarios.

## Exercise

Si está ejecutando Upstart, intente comprender las configuraciones de trabajo en `/etc/init`.

## Quiz Question

¿Cuál es la implementación de init utilizada por Ubuntu?

## Quiz Answer

upstart
