---
index: 5
lang: "es"
title: "Visión general de Systemd"
meta_title: "Visión general de Systemd - Init"
meta_description: "Aprende los conceptos básicos de Systemd: comprende las units, los targets y el proceso de arranque. Descubre cómo Systemd gestiona los servicios y los estados del sistema en Linux. ¡Comienza tu viaje!"
meta_keywords: "Systemd, Systemd units, Systemd targets, Linux boot process, Linux services, principiante, tutorial, guía"
---

## Lesson Content

Systemd se está convirtiendo lentamente en el estándar emergente para init. Si tienes un directorio `/usr/lib/systemd`, lo más probable es que estés usando systemd.

Systemd utiliza objetivos para poner tu sistema en funcionamiento. Básicamente, tienes un objetivo que quieres alcanzar, y este objetivo también tiene dependencias que deben cumplirse. Systemd es extremadamente flexible y robusto; no sigue una secuencia estricta para iniciar procesos. Esto es lo que sucede durante un arranque típico de systemd:

1. Primero, systemd carga sus archivos de configuración, usualmente ubicados en `/etc/systemd/system` o `/usr/lib/systemd/system`.
2. Luego determina su objetivo de arranque, que usualmente es `default.target`.
3. Systemd averigua las dependencias del objetivo de arranque y las activa.

Similar a los runlevels de SysV, systemd arranca en diferentes targets:

- `poweroff.target` - apagar sistema
- `rescue.target` - modo de usuario único
- `multi-user.target` - multiusuario con red
- `graphical.target` - multiusuario con red y GUI
- `reboot.target` - reiniciar

El objetivo de arranque predeterminado de `default.target` usualmente apunta a `graphical.target`.

Los objetos principales con los que trabaja systemd se conocen como units. Systemd no solo detiene e inicia servicios; puede montar sistemas de archivos, monitorear tus sockets de red, etc. Debido a esa robustez, tiene diferentes tipos de units con los que opera. Las units más comunes son:

- Service units - estos son los servicios que hemos estado iniciando y deteniendo; estos archivos de unit terminan en `.service`.
- Mount units - Estos montan sistemas de archivos; estos archivos de unit terminan en `.mount`.
- Target units - Estos agrupan otras units; los archivos terminan en `.target`.

Por ejemplo, digamos que arrancamos en nuestro `default.target`. Este target agrupa la unit `networking.service`, la unit `crond.service`, etc., así que una vez que activamos una sola unit, todo lo que está debajo de esa unit también se activa.

## Exercise

No exercises for this lesson.

## Quiz Question

¿Qué unit se utiliza para agrupar otras units?

## Quiz Answer

target
