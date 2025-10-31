---
index: 6
lang: "es"
title: "yum y apt"
meta_title: "yum y apt - Paquetes"
meta_description: "Explore las diferencias clave en el debate yum vs apt. Esta guía cubre cómo usar yum y apt para instalar, eliminar y actualizar paquetes en sistemas Linux basados en RPM y Debian."
meta_keywords: "yum vs apt, yum apt, gestión de paquetes linux, apt, yum, debian, red hat, instalar paquetes, actualizar paquetes, comandos linux"
---

## Lesson Content

Los gestores de paquetes son herramientas esenciales en Linux que simplifican la instalación, actualización y eliminación de software. Manejan automáticamente las dependencias, asegurando que todas las bibliotecas y componentes requeridos se instalen correctamente. Dos de los sistemas de gestión de paquetes más prominentes son **yum** y **apt**.

### Yum vs Apt

La diferencia principal entre estos dos sistemas radica en las distribuciones de Linux a las que sirven. El gestor de paquetes `yum` (Yellowdog Updater, Modified) es utilizado por distribuciones basadas en RPM como Red Hat, CentOS y Fedora. En contraste, `apt` (Advanced Package Tool) es el estándar para las distribuciones basadas en Debian, incluyendo Ubuntu. Aunque tanto `yum` como `apt` logran los mismos objetivos, su sintaxis de comandos difiere.

### Instalación y Eliminación de Paquetes

Para instalar una nueva pieza de software desde un repositorio, se utiliza el comando `install`.

```bash
Debian: $ apt install nombre_paquete
RPM: $ yum install nombre_paquete
```

Para eliminar un paquete, los comandos también son sencillos. `apt` usa `remove`, mientras que `yum` usa `erase`.

```bash
Debian: $ apt remove nombre_paquete
RPM: $ yum erase nombre_paquete
```

### Actualización e Inspección de Paquetes

Es una buena práctica actualizar el índice de paquetes local antes de instalar o actualizar software. Esto asegura que se obtengan las últimas versiones disponibles.

Para los sistemas Debian, este es un proceso de dos pasos: `apt update` actualiza la lista de paquetes y `apt upgrade` instala las nuevas versiones. Para los sistemas RPM, `yum update` maneja ambas acciones con un solo comando.

```bash
Debian: $ apt update; apt upgrade
RPM: $ yum update
```

Si necesita obtener más detalles sobre un paquete específico, puede usar los siguientes comandos para mostrar información como su versión, tamaño y descripción.

```bash
Debian: $ apt show nombre_paquete
RPM: $ yum info nombre_paquete
```

## Exercise

¡La práctica hace al maestro! Aquí hay algunos laboratorios prácticos para reforzar su comprensión de la gestión de paquetes en Linux:

1.  **[Consultar y Actualizar Paquetes con YUM en Linux](https://labex.io/es/labs/rhel-query-and-update-packages-with-yum-in-linux-590869)** - Practique la gestión de paquetes de software en sistemas Linux basados en RHEL, incluyendo la inspección, actualización y exploración de repositorios.
2.  **[Instalación de Software en Linux](https://labex.io/es/labs/linux-software-installation-on-linux-18005)** - Aprenda varios métodos para instalar y gestionar software en sistemas Ubuntu, incluyendo el uso de apt, dpkg y el manejo de archivos .deb.
3.  **[Instalación y Eliminación de Paquetes](https://labex.io/es/labs/linux-installing-and-removing-packages-385380)** - Practique la actualización del sistema, la instalación y eliminación de paquetes, y la optimización de la configuración del software en un sistema basado en Debian usando `apt`.

Estos laboratorios le ayudarán a aplicar los conceptos en escenarios reales y a ganar confianza con la gestión de paquetes de Linux.

## Quiz Question

What command is used to show package information on a Debian system? Please answer in English, paying attention to case sensitivity.

## Quiz Answer

apt show
