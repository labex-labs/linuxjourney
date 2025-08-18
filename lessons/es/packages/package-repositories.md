---
index: 2
lang: "es"
title: "Repositorios de Paquetes"
meta_title: "Repositorios de Paquetes - Paquetes"
meta_description: "Aprende sobre los repositorios de paquetes de Linux y cómo gestionan el software. Descubre cómo encontrar y añadir fuentes de paquetes como /etc/apt/sources.list para una fácil instalación."
meta_keywords: "repositorios de paquetes Linux, lista de fuentes apt, /etc/apt/sources.list, paquetes Linux, Linux para principiantes, tutorial de Linux, gestión de paquetes"
---

## Lesson Content

¿Cómo terminan los paquetes subidos a internet en nuestras computadoras? ¿Vas a la página de descarga de cada paquete que quieres y haces clic en descargar e instalar? Aunque puedes hacer eso, hay una solución mejor: los repositorios de paquetes. Los repositorios son ubicaciones de almacenamiento central para los paquetes. Hay toneladas de repositorios que contienen muchos paquetes, y lo mejor de todo es que todos se encuentran en internet, sin discos de instalación tontos. Tu máquina no sabe dónde buscar estos repositorios a menos que le digas explícitamente dónde buscar.

Por ejemplo, digamos que quiero el software Docker en mi máquina. Docker gestiona sus propios repositorios para sus paquetes de contenedores. Dentro de este repositorio hay múltiples paquetes, como el paquete docker-ce, el paquete docker-ce-cli, el paquete containerd.io, etc. Docker aloja este repositorio en un enlace de origen llamado: `https://download.docker.com/linux/ubuntu`

Ahora, en lugar de ir a su sitio web para descargar el paquete directamente, puedes decirle a tu máquina que encuentre el software Docker desde el enlace de origen.

Tu distribución ya viene con fuentes preaprobadas para obtener paquetes, y así es como instala todos los paquetes base que ves en tu sistema. En un sistema Debian, este archivo de fuentes es el archivo `/etc/apt/sources.list`. Tu máquina sabrá buscar allí y verificar cualquier repositorio de origen que hayas añadido.

## Exercise

No exercises for this lesson.

## Quiz Question

¿Dónde se encuentra el archivo de fuentes en un sistema Debian?

## Quiz Answer

/etc/apt/sources.list
