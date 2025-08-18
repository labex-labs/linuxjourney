---
lang: "es"
title: "Gestión de archivos de registro"
meta_description: "Aprenda a gestionar los archivos de registro de Linux de forma eficiente utilizando logrotate. Descubra la rotación de registros, la compresión y la configuración para ahorrar espacio en disco. ¡Empiece a aprender hoy mismo!"
meta_keywords: "logrotate, registros de Linux, gestión de registros, rotación de registros, tutorial de Linux, principiante, guía, espacio en disco"
---

## Lesson Content

Los archivos de registro generan una gran cantidad de datos y los almacenan en sus discos duros. Sin embargo, esto presenta muchos problemas. En su mayor parte, solo queremos poder ver los registros más recientes. También queremos administrar nuestro espacio en disco de manera eficiente. Entonces, ¿cómo hacemos todo esto? La respuesta es con `logrotate`.

La utilidad `logrotate` realiza la gestión de registros por nosotros. Tiene un archivo de configuración que nos permite especificar cuántos y qué registros mantener, cómo comprimir nuestros registros para ahorrar espacio y más. La herramienta `logrotate` generalmente se ejecuta desde cron una vez al día, y los archivos de configuración se pueden encontrar en `/etc/logrotate.d`.

Hay otras herramientas de rotación de registros que puede usar para administrar sus registros, pero `logrotate` es la más común.

## Exercise

Examine su archivo de configuración de `logrotate` y vea cómo administra algunos de sus registros.

## Quiz Question

¿Qué utilidad se utiliza para gestionar los registros?

## Quiz Answer

logrotate
