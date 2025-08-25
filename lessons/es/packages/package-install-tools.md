---
index: 5
lang: "es"
title: "rpm y dpkg"
meta_title: "rpm y dpkg - Paquetes"
meta_description: "Aprende a instalar, eliminar y listar paquetes usando los comandos rpm y dpkg. Comprende la gestión directa de paquetes para archivos .deb y .rpm. ¡Comienza tu viaje en Linux!"
meta_keywords: "rpm, dpkg, gestión de paquetes Linux, .deb, .rpm, tutorial Linux, guía para principiantes, instalar paquetes"
---

## Lesson Content

Aunque la mayor parte de este curso trata sobre los sistemas de gestión de paquetes (los Batmans de la gestión de paquetes), no debemos olvidarnos de los Robins. Aunque son muy útiles y fiables, no vienen con ese dulce Batmóvil y cinturón de herramientas.

Así como `.exe` es un archivo ejecutable único, también lo son `.deb` y `.rpm`. Normalmente no los verías si usas repositorios de paquetes, pero si descargas paquetes directamente, lo más probable es que los obtengas en estos formatos populares. Obviamente, son exclusivos de sus distribuciones: `.deb` para las basadas en Debian y `.rpm` para las basadas en Red Hat.

Para instalar estos paquetes directos, puedes usar los comandos de gestión de paquetes: `rpm` y `dpkg`. Estas herramientas se utilizan para instalar archivos de paquetes; sin embargo, no instalarán las dependencias del paquete. Entonces, si tu paquete tuviera 10 dependencias, tendrías que instalar esos paquetes por separado y luego sus dependencias, y así sucesivamente. Como puedes ver, esa fue una de las razones que dio origen a los sistemas de gestión completos que discutiremos más adelante.

Ten en cuenta que habrá innumerables ocasiones en las que necesitarás instalar, consultar o verificar un paquete con una de estas herramientas, así que recuerda estos comandos.

### Instalar un paquete

```bash
Debian: $ dpkg -i some_deb_package.deb
RPM: $ rpm -i some_rpm_package.rpm
```

La `i` significa instalar. También puedes usar el formato más largo de `--install`.

### Eliminar un paquete

```bash
Debian: $ dpkg -r some_deb_package.deb
RPM: $ rpm -e some_rpm_package.rpm
```

Debian: `r` para eliminar
RPM: `e` para borrar

### Listar paquetes instalados

```bash
Debian: $ dpkg -l
RPM: $ rpm -qa
```

Debian: `l` para listar
RPM: `q` para consultar y `a` para todo

## Exercise

¡La práctica hace al maestro! Aquí tienes un laboratorio práctico para reforzar tu comprensión de la gestión directa de paquetes:

1. **[Gestión de paquetes con RPM en Linux](https://labex.io/es/labs/rhel-managing-packages-with-rpm-in-linux-590868)** - Adquiere experiencia práctica consultando información de paquetes, verificando la integridad, listando dependencias, simulando la eliminación e inspeccionando el contenido de paquetes RPM con `rpm` y herramientas relacionadas.

Este laboratorio te ayudará a aplicar los conceptos de gestión de archivos de paquetes individuales en un escenario real y a generar confianza con estas herramientas esenciales de Linux.

## Quiz Question

¿Cuál es la herramienta de gestión de paquetes para archivos `.deb`?

## Quiz Answer

dpkg
