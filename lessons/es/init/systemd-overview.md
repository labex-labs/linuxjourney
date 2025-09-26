---
index: 5
lang: "es"
title: "Visión general de Systemd"
meta_title: "Visión general de Systemd - Init"
meta_description: "Aprenda los conceptos básicos de Systemd: comprenda las unidades, los objetivos (targets) y el proceso de arranque. Descubra cómo Systemd gestiona los servicios y los estados del sistema en Linux. ¡Comience su viaje!"
meta_keywords: "Systemd, unidades de Systemd, objetivos de Systemd, proceso de arranque de Linux, servicios de Linux, principiante, tutorial, guía"
---

## Lesson Content

Systemd es el sistema init estándar en la mayoría de las distribuciones modernas de Linux. Si tiene un directorio `/usr/lib/systemd`, lo más probable es que esté utilizando systemd.

Systemd utiliza objetivos (targets) para poner su sistema en funcionamiento. Básicamente, usted tiene un objetivo que desea alcanzar, y este objetivo también tiene dependencias que deben cumplirse. Systemd es extremadamente flexible y robusto; no sigue una secuencia estricta para iniciar los procesos. Esto es lo que sucede durante un arranque típico de systemd:

1. Primero, systemd carga sus archivos de configuración, generalmente ubicados en `/etc/systemd/system` o `/usr/lib/systemd/system`.
2. Luego determina su objetivo de arranque, que suele ser `default.target`.
3. Systemd calcula las dependencias del objetivo de arranque y las activa.

De forma similar a los niveles de ejecución de SysV, systemd arranca en diferentes objetivos:

- `poweroff.target` - apagar el sistema
- `rescue.target` - modo de un solo usuario
- `multi-user.target` - multiusuario con red
- `graphical.target` - multiusuario con red e interfaz gráfica (GUI)
- `reboot.target` - reiniciar

El objetivo de arranque predeterminado de `default.target` generalmente apunta a `graphical.target`.

Los objetos principales con los que trabaja systemd se conocen como unidades. Systemd no solo detiene e inicia servicios; puede montar sistemas de archivos, monitorear sus sockets de red, etc. Debido a esta robustez, tiene diferentes tipos de unidades con las que opera. Las unidades más comunes son:

- Unidades de servicio (`Service units`) - estos son los servicios que hemos estado iniciando y deteniendo; estos archivos de unidad terminan en `.service`.
- Unidades de montaje (`Mount units`) - estas montan sistemas de archivos; estos archivos de unidad terminan en `.mount`.
- Unidades de objetivo (`Target units`) - estas agrupan otras unidades; los archivos terminan en `.target`.

Por ejemplo, digamos que arrancamos en nuestro `default.target`. Este objetivo agrupa la unidad `networking.service`, la unidad `crond.service`, etc., por lo que una vez que activamos una sola unidad, todo lo que está debajo de esa unidad también se activa.

## Exercise

Aunque no hay laboratorios específicos para este tema, recomendamos explorar la [Ruta de Aprendizaje de Linux](https://labex.io/es/learn/linux) completa para practicar habilidades y conceptos relacionados con Linux.

## Quiz Question

¿Qué unidad se utiliza para agrupar otras unidades?

## Quiz Answer

target
