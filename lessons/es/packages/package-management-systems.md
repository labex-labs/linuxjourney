---
index: 6
lang: "es"
title: "yum y apt"
meta_title: "yum y apt - Paquetes"
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

### Actualizar paquetes para un repositorio

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

¡La práctica hace al maestro! Aquí hay algunos laboratorios prácticos para reforzar su comprensión de la gestión de paquetes de Linux:

1. **[Consultar y actualizar paquetes con YUM en Linux](https://labex.io/es/labs/rhel-query-and-update-packages-with-yum-in-linux-590869)** - Practique la gestión de paquetes de software en sistemas Linux basados en RHEL usando YUM, incluyendo la inspección, actualización y exploración de repositorios.
2. **[Instalación de software en Linux](https://labex.io/es/labs/linux-software-installation-on-linux-18005)** - Aprenda varios métodos para instalar y gestionar software en sistemas Ubuntu, incluyendo el uso de apt, dpkg y el manejo de archivos .deb.
3. **[Instalación y eliminación de paquetes](https://labex.io/es/labs/linux-installing-and-removing-packages-385380)** - Practique la actualización del sistema, la instalación y eliminación de paquetes, y la optimización de la configuración de software en un sistema basado en Debian usando `apt`.

Estos laboratorios le ayudarán a aplicar los conceptos en escenarios reales y a generar confianza con la gestión de paquetes de Linux.

## Quiz Question

¿Qué comando se utiliza para mostrar información de un paquete en un sistema Debian?

## Quiz Answer

apt show
