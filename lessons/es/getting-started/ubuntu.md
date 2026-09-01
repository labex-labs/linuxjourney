---
lesson_id: "ubuntu"
course_id: "getting-started"
lang: "es"
order_index: 5
title: "Ubuntu"
description: "Aprende cómo Ubuntu combina la base de Debian con opciones accesibles para escritorio, servidor y distintos ciclos de lanzamiento."
meta_title: "Ubuntu Linux"
meta_description: "Descubre qué es Ubuntu Linux, por qué es tan popular, cómo funciona su modelo de lanzamientos y gestión de paquetes, y por qué es ampliamente utilizado en escritorios, portátiles y servidores."
meta_keywords: "ubuntu linux, distribución ubuntu, qué es ubuntu, lanzamientos ubuntu, gestión de paquetes ubuntu, ubuntu basado en debian, distribución linux"
---

## ¿Qué es Ubuntu?

Ubuntu es una de las distribuciones de Linux más utilizadas. Desarrollada por Canonical, está basada en Debian y es conocida por su diseño accesible, su gran comunidad de usuarios y su amplio soporte de hardware y software.

Ubuntu se ha convertido en un punto de partida común para quienes desean aprender Linux sin comenzar con una configuración más manual o avanzada. Se utiliza en computadoras personales, sistemas de desarrollo, plataformas en la nube y servidores, lo que le otorga un alcance que pocas otras distribuciones pueden igualar.

:::single-choice{#identify-ubuntu-base} ¿Qué distribución sirve de base a Ubuntu?

::option[La distribución Debian]{#debian-base .correct explanation="Ubuntu se basa en Debian y hereda gran parte de su enfoque de empaquetado. Después añade sus propias versiones, valores predeterminados y modelo de soporte."}
::option[La distribución Fedora]{#ubuntu-fedora-base explanation="Fedora pertenece al ecosistema de Red Hat y no constituye la base de Ubuntu. Ubuntu forma parte de la familia Debian."}
::option[La distribución Arch]{#ubuntu-arch-base explanation="Arch Linux es una distribución independiente, con su propio sistema de paquetes y modelo de lanzamiento. Ubuntu se basa en Debian."}
:::

## Por qué Ubuntu es popular

Ubuntu es popular porque intenta hacer que Linux sea práctico para el uso diario. Ofrece un instalador pulido, documentación sólida, lanzamientos predecibles y un gran ecosistema de tutoriales y soporte de terceros. Para muchos usuarios, esa combinación hace de Ubuntu una de las distribuciones de Linux más fáciles de usar.

Otra razón por la que Ubuntu es tan visible es que funciona en muchos entornos. Lo verás en computadoras portátiles y de escritorio, en máquinas virtuales, en servidores y en plataformas en la nube. Esa amplia adopción refuerza su reputación como una distribución de Linux de propósito general.

:::single-choice{#recognize-beginner-support} ¿Qué cualidad de Ubuntu ayuda de forma más directa a un principiante a resolver problemas?

::option[La compilación manual obligatoria de cada programa instalado]{#manual-compilation explanation="Ubuntu suele proporcionar software empaquetado en vez de exigir que se compile cada programa. Ese trabajo adicional no facilitaría la resolución de problemas."}
::option[La documentación extensa y una gran comunidad de usuarios]{#documentation-community .correct explanation="La documentación y las conversaciones de la comunidad ofrecen numerosos lugares donde encontrar explicaciones y ayuda. Esto reduce las barreras del aprendizaje."}
::option[La orientación limitada exclusivamente a administradores expertos]{#limited-guidance explanation="La visibilidad de Ubuntu se debe en parte a que ofrece orientación para muchos niveles. Restringir la ayuda a expertos iría en contra de su accesibilidad para principiantes."}
:::

## Ubuntu y Debian

Ubuntu es una distribución basada en Debian, lo que significa que hereda gran parte de su modelo de gestión de paquetes y su enfoque de empaquetado de software de Debian. Si aprendes cómo funciona `apt` en Ubuntu, ese conocimiento también te ayudará a comprender otros sistemas basados en Debian.

Al mismo tiempo, Ubuntu no es solo "Debian con un escritorio". Tiene su propio calendario de lanzamientos, valores predeterminados, modelo de soporte y ecosistema. Si deseas compararlo con otras opciones, consulta [Cómo elegir una distribución de Linux](https://labex.io/es/lesson/choosing-a-linux-distribution) o aprende más sobre [Debian](https://labex.io/es/lesson/debian).

## Lanzamientos de Ubuntu

Ubuntu utiliza dos tipos principales de lanzamientos. Publica una nueva versión cada seis meses, y cada dos años una de esas versiones se convierte en un lanzamiento de Soporte a Largo Plazo, o LTS. Los lanzamientos LTS se eligen comúnmente para computadoras de escritorio, estaciones de trabajo y servidores que necesitan una base más estable.

Este modelo de lanzamiento ayuda a explicar el atractivo de Ubuntu. Los usuarios que desean una base confiable a menudo eligen LTS, mientras que los usuarios que desean funciones más nuevas pueden usar los lanzamientos intermedios que llegan en un calendario más rápido.

:::single-choice{#choose-ubuntu-lts} ¿Qué tipo de versión de Ubuntu se adapta mejor a un sistema que necesita una base duradera y previsible?

::option[Una versión intermedia]{#interim-release explanation="Las versiones intermedias llegan con mayor frecuencia y ofrecen antes las funciones nuevas. Su periodo de soporte más breve no coincide con la prioridad indicada."}
::option[Una versión LTS]{#lts-release .correct explanation="Las versiones LTS están pensadas para recibir soporte durante más tiempo y suelen elegirse en sistemas que priorizan una base fiable."}
::option[Una actualización de paquete]{#package-update explanation="Una actualización de paquete modifica software dentro de una versión instalada. No es uno de los dos tipos de versión del sistema operativo Ubuntu."}
:::

## Gestión de paquetes

Como sistema basado en Debian, Ubuntu utiliza el formato de paquete `.deb` y el gestor de paquetes `apt` para instalar, actualizar y eliminar software. Esto brinda a los usuarios acceso a un ecosistema de software muy grande y a un flujo de trabajo de línea de comandos familiar.

La gestión de paquetes es una de las fortalezas prácticas de Ubuntu porque combina herramientas maduras de Debian con un entorno de software amplio y ampliamente documentado.

:::single-choice{#identify-ubuntu-package-tool} ¿Qué elemento es la herramienta de gestión de paquetes utilizada para instalar software en Ubuntu?

::option[`.deb`]{#deb-format explanation="`.deb` identifica el formato de paquete de los sistemas basados en Debian. No es la herramienta de línea de comandos que gestiona los paquetes."}
::option[`LTS`]{#lts-label explanation="LTS identifica una versión con soporte a largo plazo. No instala ni gestiona paquetes de software."}
::option[`apt`]{#ubuntu-apt-tool .correct explanation="Ubuntu utiliza `apt` para instalar, actualizar y eliminar paquetes. La herramienta trabaja con software empaquetado en el formato `.deb` de Debian."}
:::

## Uso en escritorio y servidor

Ubuntu se utiliza tanto en sistemas de escritorio como de servidor. En el lado del escritorio, es conocido por una experiencia pulida basada en GNOME y valores predeterminados relativamente accesibles. En el lado del servidor, se implementa ampliamente en el desarrollo, la infraestructura web y los entornos en la nube.

Esa variedad hace que Ubuntu sea atractivo para los usuarios que desean una distribución de Linux que pueda escalar desde el aprendizaje en una computadora portátil hasta la ejecución de cargas de trabajo en producción.

## Por qué los principiantes eligen Ubuntu

Ubuntu a menudo se recomienda a los principiantes porque es más fácil de instalar y solucionar problemas que muchas otras distribuciones de Linux. La gran base de usuarios significa que hay muchos tutoriales, publicaciones en foros y guías disponibles cuando algo sale mal.

Para quienes desean una distribución de Linux accesible para principiantes sin renunciar a la flexibilidad a largo plazo, Ubuntu sigue siendo un punto de partida habitual.

## Lecturas adicionales

- [Ubuntu Desktop](https://ubuntu.com/desktop)
- [Ubuntu Server](https://ubuntu.com/server)
- [Ciclo de lanzamiento de Ubuntu](https://ubuntu.com/releaseendoflife)
- [Documentación de lanzamientos de Ubuntu](https://documentation.ubuntu.com/project/release-team/ubuntu-releases/)

Para seguir aprendiendo después de esta introducción a Ubuntu, recomendamos estos cursos de LabEx:

1. **[Inicio rápido con Linux](https://labex.io/es/courses/quick-start-with-linux)** - Construye una base práctica en conceptos básicos de Linux y habilidades de línea de comandos.
2. **[Linux para principiantes](https://labex.io/es/courses/linux-for-noobs)** - Sigue un camino amigable para principiantes para comprender los conceptos básicos de Linux paso a paso.
3. **[Conviértete en administrador de sistemas junior](https://labex.io/es/courses/become-a-junior-system-administrator)** - Continúa con habilidades prácticas de administración de Linux una vez que domines lo básico.

## Resumen

Ahora puedes explicar cómo Ubuntu se apoya en Debian y, al mismo tiempo, ofrece sus propias versiones y experiencia de uso.

1. Identificar Debian como la base de Ubuntu.
2. Reconocer las cualidades de soporte que ayudan a los principiantes.
3. Comparar las versiones LTS e intermedias de Ubuntu.
4. Utilizar `apt` como herramienta de gestión de paquetes de Ubuntu.
