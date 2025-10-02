---
index: 2
lang: "es"
title: "Repositorios de Paquetes"
meta_title: "Repositorios de Paquetes - Paquetes"
meta_description: "Aprende sobre los repositorios de paquetes de Linux y cómo gestionan el software. Descubre cómo encontrar y añadir fuentes de paquetes como /etc/apt/sources.list para una fácil instalación."
meta_keywords: "repositorios de paquetes Linux, lista de fuentes apt, /etc/apt/sources.list, paquetes Linux, Linux para principiantes, tutorial de Linux, gestión de paquetes"
---

## Lesson Content

¿Cómo llegan a nuestros ordenadores los paquetes subidos a internet? ¿Vas a la página de descarga de cada paquete que quieres y haces clic en descargar e instalar? Aunque puedes hacerlo, hay una solución mejor: los repositorios de paquetes. Los repositorios son ubicaciones de almacenamiento central para los paquetes. Hay toneladas de repositorios que contienen muchos paquetes y, lo mejor de todo, todos se encuentran en internet, sin discos de instalación tontos. Tu máquina no sabe dónde buscar estos repositorios a menos que le digas explícitamente dónde buscar.

Por ejemplo, digamos que quiero el software Docker en mi máquina. Docker gestiona sus propios repositorios para sus paquetes de contenedores. Dentro de este repositorio hay múltiples paquetes, como el paquete `docker-ce`, el paquete `docker-ce-cli`, el paquete `containerd.io`, etc. Docker aloja este repositorio en un enlace fuente llamado: `https://download.docker.com/linux/ubuntu`

Ahora, en lugar de ir a su sitio web para descargar el paquete directamente, puedes indicarle a tu máquina que busque el software Docker desde el enlace fuente.

Tu distribución ya viene con fuentes preaprobadas para obtener paquetes, y así es como instala todos los paquetes base que ves en tu sistema. En un sistema Debian, este archivo de fuentes es el archivo `/etc/apt/sources.list`. Tu máquina sabrá buscar allí y verificar cualquier repositorio fuente que hayas añadido.

> **Nota:** En sistemas Debian/Ubuntu más antiguos, los repositorios se configuran en `/etc/apt/sources.list`, mientras que las versiones más nuevas de Ubuntu (22.04+) utilizan archivos estructurados en `/etc/apt/sources.list.d/` como `ubuntu.sources`. Ambos formatos son compatibles con apt.

## Exercise

¡La práctica hace al maestro! Aquí tienes algunos laboratorios prácticos para reforzar tu comprensión de la gestión de paquetes y repositorios de Linux:

1. **[Instalación de Software en Linux](https://labex.io/es/labs/linux-software-installation-on-linux-18005)** - Practica varios métodos para instalar y gestionar software en sistemas Ubuntu, incluido el uso de apt y el manejo de archivos .deb, lo que se relaciona directamente con el concepto de `sources.list`.
2. **[Instalación y Eliminación de Paquetes](https://labex.io/es/labs/linux-installing-and-removing-packages-385380)** - Aprende a actualizar el sistema, instalar y eliminar paquetes en un sistema basado en Debian, consolidando tu comprensión de cómo los gestores de paquetes interactúan con los repositorios.
3. **[Consultar y Actualizar Paquetes con YUM en Linux](https://labex.io/es/labs/rhel-query-and-update-packages-with-yum-in-linux-590869)** - Explora cómo gestionar paquetes de software en sistemas Linux basados en RHEL usando YUM, proporcionando una perspectiva más amplia sobre la gestión de paquetes en diferentes distribuciones.

Estos laboratorios te ayudarán a aplicar los conceptos de repositorios de paquetes y gestión de software en escenarios reales y a generar confianza con las tareas de administración del sistema.

## Quiz Question

¿Dónde se encuentra el archivo de fuentes en un sistema Debian?

## Quiz Answer

/etc/apt/sources.list
