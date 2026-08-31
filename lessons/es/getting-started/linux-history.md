---
lesson_id: "linux-history"
course_id: "getting-started"
lang: "es"
order_index: 1
title: "Historia de Linux"
description: "Aprende cómo UNIX, GNU y el núcleo Linux contribuyeron a los sistemas Linux modernos."
meta_title: "Historia de Linux - Primeros pasos"
meta_description: "Comienza tu viaje en Linux explorando su historia. Aprende sobre sus orígenes en UNIX, el proyecto GNU y la creación del kernel de Linux por Linus Torvalds."
meta_keywords: "historia de linux, origen de linux, viaje en linux, UNIX, proyecto GNU, Linus Torvalds, kernel de Linux, Linux para principiantes"
---

¡Bienvenido a tu **viaje por Linux**! Si estás listo para adentrarte en el poderoso mundo de Linux, has llegado al lugar indicado. Me llamo Penguin Pete y seré tu guía. Para empezar, exploremos brevemente la **historia de Linux**.

## Los predecesores de Linux

Para entender cómo se creó Linux, debemos remontarnos a 1969, cuando Ken Thompson y Dennis Ritchie, de los Laboratorios Bell, desarrollaron el sistema operativo UNIX. Más tarde se reescribió en el lenguaje de programación C, lo que lo hizo portátil y favoreció su adopción generalizada.

![Línea de tiempo de Unix](https://file.labex.io/images/ed9c245d-e8be-4287-bf34-67750b042542.jpg)

:::single-choice{#understand-unix-portability}
¿Cuál fue un resultado importante de reescribir UNIX en C?

::option[Se convirtió en el núcleo libre creado para el sistema GNU.]{#unix-became-gnu-kernel explanation="UNIX existía antes que el proyecto GNU y no era el núcleo de GNU. Más tarde, GNU comenzó a desarrollar un núcleo distinto llamado Hurd."}
::option[Se volvió más fácil trasladarlo entre distintos sistemas de hardware.]{#portable-across-hardware .correct explanation="Escribir UNIX en C lo hizo más portátil. Esa portabilidad ayudó a que se extendiera más allá del hardware original."}
::option[Se convirtió en un intérprete de órdenes utilizado únicamente en los Laboratorios Bell.]{#unix-became-shell explanation="UNIX es un sistema operativo, no solo un intérprete de órdenes. Reescribirlo en C favoreció su adopción fuera de los Laboratorios Bell."}
:::

Más de una década después, Richard Stallman inició el proyecto GNU. GNU es un acrónimo recursivo de «GNU's Not UNIX» y su objetivo era crear un sistema operativo tipo UNIX completamente libre y de código abierto. El proyecto produjo muchos componentes esenciales y la Licencia Pública General de GNU (GPL), pero su propio núcleo, GNU Hurd, no estaba listo para un uso general cuando Linux apareció.

:::single-choice{#identify-gnu-missing-component}
¿Qué componente principal de GNU no estaba listo cuando apareció Linux?

::option[Un núcleo listo para producción]{#gnu-kernel .correct explanation="GNU había producido muchos componentes del sistema, pero su propio núcleo, GNU Hurd, no estaba listo para un uso general."}
::option[Una licencia de software libre]{#gnu-license explanation="El proyecto GNU ya había creado la Licencia Pública General de GNU. El componente que faltaba era un núcleo utilizable."}
::option[Herramientas esenciales del sistema]{#gnu-tools explanation="GNU ya había producido muchas herramientas esenciales. Su núcleo seguía siendo la principal parte inacabada del sistema."}
:::

## El papel del núcleo

El núcleo es el componente central de un sistema operativo. Actúa como puente para que el hardware se comunique con el software. Gestiona recursos del sistema como la CPU, la memoria y los dispositivos periféricos. Además de las herramientas y aplicaciones que utilizan las personas, un sistema operativo completo necesita este componente central encargado de administrar los recursos.

:::single-choice{#recognize-kernel-role}
¿Cuál de estas responsabilidades corresponde al núcleo del sistema operativo?

::option[Escribir cada orden introducida en el intérprete]{#write-shell-commands explanation="Las personas o los scripts proporcionan las órdenes. El núcleo aporta los recursos de bajo nivel necesarios cuando los programas las ejecutan."}
::option[Elegir la licencia de cada aplicación instalada]{#choose-software-licenses explanation="Los autores y distribuidores eligen las licencias de las aplicaciones. Seleccionar licencias no es una tarea de gestión de recursos del núcleo."}
::option[Gestionar la CPU, la memoria y los dispositivos conectados]{#manage-system-resources .correct explanation="El núcleo gestiona los recursos de hardware y los pone a disposición del software. El tiempo de CPU, la memoria y los dispositivos son ejemplos fundamentales."}
:::

## El nacimiento del núcleo Linux

Así llegamos a 1991, cuando un estudiante finlandés llamado Linus Torvalds comenzó a desarrollar un nuevo núcleo como proyecto personal. Este pasó a conocerse como el núcleo Linux. Después de que Linux se publicara como software libre en 1992, pudo combinarse con el sistema GNU, casi completo, para formar un sistema operativo libre completo, conocido habitualmente como GNU/Linux. Este hito fue un momento decisivo en la **historia de Linux**.

![Linus Torvalds en 2018](https://file.labex.io/images/3e1311fd-b8ca-45e7-8d02-9aac6377bb36.jpg)

_Linus Torvalds en 2018 (Fuente: [Wikipedia](https://en.wikipedia.org/wiki/Linus_Torvalds))_

:::single-choice{#identify-linux-kernel-creator}
¿Quién comenzó a desarrollar el núcleo Linux en 1991?

::option[Richard Stallman]{#richard-stallman explanation="Richard Stallman inició el proyecto GNU. GNU aportó muchos componentes del sistema, pero Linus Torvalds comenzó el núcleo Linux."}
::option[Dennis Ritchie]{#dennis-ritchie explanation="Dennis Ritchie ayudó a desarrollar UNIX y el lenguaje C. El proyecto del núcleo Linux lo inició Linus Torvalds años después."}
::option[Linus Torvalds]{#linus-torvalds .correct explanation="Linus Torvalds inició el proyecto del núcleo en 1991. Ese proyecto se convirtió en el núcleo Linux."}
:::

Para continuar tu **viaje por Linux**, prueba estos laboratorios prácticos, en los que podrás practicar órdenes fundamentales y ganar confianza en el entorno de línea de comandos.

1. **[Primeros pasos con Linux](https://labex.io/es/labs/linux-getting-started-with-linux-446315)** - Comienza tu viaje por Linux aprendiendo órdenes esenciales de terminal como `echo`, `date` y cálculos básicos. Es ideal para principiantes.
2. **[Tu primer laboratorio de Linux](https://labex.io/es/labs/linux-your-first-linux-lab-270253)** - Este laboratorio introductorio te guía por el clásico programa «¡Hola, mundo!» en Linux y te enseña algunas órdenes fundamentales.
3. **[Crea un saludo de terminal personalizado](https://labex.io/es/labs/linux-create-personalized-terminal-greeting-446322)** - Un desafío rápido y entretenido para crear un mensaje de bienvenida atractivo con órdenes básicas de la terminal de Linux.

## Resumen

Ahora puedes explicar cómo UNIX, GNU y el núcleo Linux contribuyeron a los sistemas Linux modernos.

1. Describir por qué fue importante la portabilidad de UNIX.
2. Identificar el núcleo como el principal componente que le faltaba a GNU.
3. Explicar el papel del núcleo en la gestión de los recursos del sistema.
4. Identificar a Linus Torvalds como creador del núcleo Linux.
