---
lang: "es"
title: "yum y apt"
meta_description: "Aprenda yum y apt para la gestión de paquetes de Linux. Instale, elimine y actualice software en sistemas Debian/RPM con este tutorial para principiantes. ¡Empiece hoy mismo!"
meta_keywords: "yum, apt, gestión de paquetes Linux, tutorial apt, tutorial yum, comandos Linux, guía para principiantes, instalación de paquetes"
---

## Lesson Content

¡Ah, los Batmans de la gestión de paquetes! Estos sistemas vienen con todas las herramientas para facilitar la instalación, eliminación y modificación de paquetes, incluida la instalación de dependencias de paquetes. Dos de los sistemas de gestión más populares son **yum** y **apt**. Yum es exclusivo de la familia Red Hat, y apt es exclusivo de la familia Debian.

### Instalar un paquete desde un repositorio

```bash
Debian: $ apt install package_name
RPM: $ yum install package_name
```

### Eliminar un paquete

```bash
Debian: $ apt remove package_name
RPM: $ yum erase package_name
```

### Actualización de paquetes para un repositorio

Siempre es una buena práctica actualizar sus repositorios de paquetes para que estén al día antes de instalar y actualizar un paquete.

```bash
Debian: apt update; apt upgrade
RPM: yum update
```

### Obtener información sobre un paquete instalado

```bash
Debian: apt show package_name
RPM: yum info package_name
```

## Exercise

Ejecute cada uno de estos comandos de paquete y vea la salida que recibe.

## Quiz Question

¿Qué comando se utiliza para mostrar información de paquetes en un sistema Debian?

## Quiz Answer

apt show
