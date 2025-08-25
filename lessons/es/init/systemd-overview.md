---
index: 5
lang: "es"
title: "Descripción general de Systemd"
meta_title: "Descripción general de Systemd - Init"
meta_description: "Aprende los conceptos básicos de Systemd: comprende unidades, objetivos y el proceso de arranque. Descubre cómo Systemd gestiona servicios y estados del sistema en Linux. ¡Comienza tu viaje!"
meta_keywords: "Systemd, unidades Systemd, objetivos Systemd, proceso de arranque de Linux, servicios de Linux, principiante, tutorial, guía"
---

## Lesson Content

Systemd se está convirtiendo lentamente en el estándar emergente para init. Si tienes un directorio `/usr/lib/systemd`, lo más probable es que estés usando systemd.

Systemd utiliza objetivos para poner tu sistema en funcionamiento. Básicamente, tienes un objetivo que quieres alcanzar, y este objetivo también tiene dependencias que deben cumplirse. Systemd es extremadamente flexible y robusto; no sigue una secuencia estricta para iniciar procesos. Esto es lo que sucede durante un arranque típico de systemd:

1. Primero, systemd carga sus archivos de configuración, generalmente ubicados en `/etc/systemd/system` o `/usr/lib/systemd/system`.
2. Luego determina su objetivo de arranque, que suele ser `default.target`.
3. Systemd averigua las dependencias del objetivo de arranque y las activa.

Similar a los niveles de ejecución de SysV, systemd arranca en diferentes objetivos:

- `poweroff.target` - apagar el sistema
- `rescue.target` - modo de usuario único
- `multi-user.target` - multiusuario con red
- `graphical.target` - multiusuario con red y GUI
- `reboot.target` - reiniciar

El objetivo de arranque predeterminado de `default.target` generalmente apunta a `graphical.target`.

Los objetos principales con los que trabaja systemd se conocen como unidades. Systemd no solo detiene e inicia servicios; puede montar sistemas de archivos, monitorear tus sockets de red, etc. Debido a esa robustez, tiene diferentes tipos de unidades con las que opera. Las unidades más comunes son:

- Unidades de servicio: estos son los servicios que hemos estado iniciando y deteniendo; estos archivos de unidad terminan en `.service`.
- Unidades de montaje: estas montan sistemas de archivos; estos archivos de unidad terminan en `.mount`.
- Unidades de destino: estas agrupan otras unidades; los archivos terminan en `.target`.

Por ejemplo, supongamos que arrancamos en nuestro `default.target`. Este objetivo agrupa la unidad `networking.service`, la unidad `crond.service`, etc., por lo que una vez que activamos una sola unidad, todo lo que está debajo de esa unidad también se activa.

## Exercise

Aunque no hay laboratorios específicos para este tema, te recomendamos explorar la completa [Ruta de Aprendizaje de Linux](https://labex.io/es/learn/linux) para practicar habilidades y conceptos relacionados con Linux.

## Quiz Question

¿Qué unidad se utiliza para agrupar otras unidades?

## Quiz Answer

target
