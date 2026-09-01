---
lesson_id: "fedora"
course_id: "getting-started"
lang: "es"
order_index: 6
title: "Fedora"
description: "Aprende cómo Fedora ofrece tecnología Linux actual mediante un proyecto comunitario vinculado a Red Hat."
meta_title: "Distribución de Linux Fedora"
meta_description: "Aprende qué es la distribución de Linux Fedora, su relación con Red Hat, cómo funciona la gestión de paquetes DNF y por qué es popular entre desarrolladores y usuarios de escritorio."
meta_keywords: "fedora linux, distribución fedora linux, qué es fedora, fedora red hat, lanzamientos de fedora, gestión de paquetes dnf, distribución linux"
---

## ¿Qué es Fedora?

Fedora es una distribución de Linux impulsada por la comunidad y patrocinada por Red Hat. Es conocida por ofrecer tecnologías modernas, una experiencia de escritorio pulida y un sólido soporte para desarrolladores y usuarios técnicos.

Fedora tiene la reputación de avanzar más rápido que las distribuciones más conservadoras, manteniendo al mismo tiempo un enfoque en la calidad y la usabilidad. Ese equilibrio la hace atractiva para los usuarios que desean un sistema Linux moderno sin tener que construir todo desde cero.

:::single-choice{#identify-fedora-project-model} ¿Qué afirmación describe correctamente el Proyecto Fedora?

::option[Es una versión descontinuada de Red Hat Enterprise Linux]{#discontinued-rhel explanation="Fedora es una distribución activa con sus propias versiones. Es un proyecto ascendente respecto a RHEL, no una versión obsoleta de este."}
::option[Es una distribución mantenida por un único fabricante de hardware]{#hardware-maintained explanation="Fedora colabora con fabricantes de hardware, pero su desarrollo lo impulsa la comunidad con el patrocinio de Red Hat."}
::option[Es un proyecto comunitario patrocinado por Red Hat]{#community-sponsored .correct explanation="Fedora lo construye una comunidad con el patrocinio y el apoyo de Red Hat. Sigue siendo una distribución comunitaria independiente."}
:::

## Por qué destaca Fedora

Fedora destaca porque a menudo adopta nuevas características de Linux antes que las distribuciones enfocadas en el ámbito empresarial. Esto la hace atractiva para desarrolladores, colaboradores de código abierto y usuarios de escritorio que desean un sistema actual con fuertes vínculos con los proyectos upstream.

También es bien conocida por ofrecer una experiencia predeterminada limpia. Fedora Workstation es especialmente popular entre los desarrolladores que buscan un escritorio moderno, herramientas actuales y un buen soporte para contenedores, virtualización y otros flujos de trabajo de desarrollo.

:::single-choice{#match-fedora-user} ¿Qué objetivo de usuario encaja mejor con Fedora Workstation?

::option[Mantener una misma versión empresarial sin cambios durante muchos años]{#long-enterprise-lifecycle explanation="Un ciclo empresarial largo y conservador se acerca más al propósito de RHEL. Fedora sigue un calendario de versiones y actualizaciones más rápido."}
::option[Usar herramientas de desarrollo actuales en un sistema de escritorio cuidado]{#current-developer-desktop .correct explanation="Fedora Workstation combina un escritorio seleccionado con herramientas actuales para desarrollo, contenedores y virtualización. Esto coincide directamente con el objetivo."}
::option[Construir manualmente desde el código fuente todos los componentes del sistema]{#fedora-manual-source explanation="Fedora proporciona un sistema completo basado en paquetes y no exige compilar cada componente. Ese objetivo corresponde a un flujo de trabajo más especializado."}
:::

## Fedora y Red Hat

Fedora desempeña un papel importante en el ecosistema de Red Hat. Las nuevas tecnologías y cambios a menudo aparecen primero en Fedora, y parte de ese trabajo influye posteriormente en Red Hat Enterprise Linux (RHEL). Esta relación ayuda a explicar por qué Fedora se siente más actual, mientras que RHEL es más conservador y está enfocado en el sector empresarial.

Si deseas comparar Fedora con opciones orientadas a empresas, consulta [Red Hat Enterprise Linux](https://labex.io/es/lesson/red-hat-enterprise-linux). Si aún estás comparando familias de distribuciones, [Elegir una distribución de Linux](https://labex.io/es/lesson/choosing-a-linux-distribution) ofrece una visión general más amplia.

:::single-choice{#explain-fedora-upstream-role} ¿Qué significa que Fedora tenga una relación ascendente con RHEL?

::option[Las versiones de RHEL se copian sin cambios en Fedora más adelante]{#rhel-copied-to-fedora explanation="Esta opción invierte la relación. Fedora avanza más rápido y sirve como fuente ascendente, no como una copia posterior de RHEL."}
::option[Fedora y RHEL siempre incluyen versiones idénticas del software]{#identical-software-versions explanation="Las dos distribuciones tienen objetivos y calendarios diferentes. RHEL selecciona y estabiliza tecnología en vez de reproducir cada versión de Fedora."}
::option[El trabajo desarrollado en Fedora puede influir posteriormente en RHEL]{#fedora-influences-rhel .correct explanation="Fedora es un entorno donde se integran antes tecnologías nuevas. Parte de ese trabajo contribuye más adelante a la plataforma empresarial de Red Hat."}
:::

## Lanzamientos de Fedora

Fedora sigue un ciclo de lanzamiento regular, con dos lanzamientos principales la mayoría de los años y alrededor de trece meses de soporte para cada uno. En comparación con distribuciones más conservadoras, Fedora tiende a ofrecer kernels, entornos de escritorio y herramientas de desarrollo más recientes en un calendario más rápido.

Esto hace que Fedora sea una buena opción para los usuarios que desean software actualizado pero que prefieren una distribución de Linux organizada y convencional en lugar de un sistema de lanzamiento continuo (rolling-release) más manual.

:::single-choice{#plan-fedora-upgrades} ¿Qué mantenimiento debe esperar un usuario de Fedora debido a su modelo de versiones?

::option[No actualizar nunca de versión durante la vida del equipo]{#no-version-upgrades explanation="Las versiones de Fedora tienen un periodo de soporte limitado. Para seguir recibiendo soporte es necesario pasar a versiones más recientes con el tiempo."}
::option[Actualizar de versión con regularidad para mantenerse en una versión compatible]{#regular-release-upgrades .correct explanation="Las versiones de Fedora avanzan a un ritmo relativamente rápido y reciben actualizaciones durante unos trece meses. Conviene planificar actualizaciones periódicas de versión."}
::option[Recibir cambios continuos de paquetes sin versiones diferenciadas del sistema]{#no-distinct-releases explanation="Fedora publica versiones principales diferenciadas y no funciona como una distribución de lanzamiento continuo convencional. Sus paquetes son actuales, pero las versiones siguen siendo importantes."}
:::

## Gestión de paquetes

Fedora utiliza el formato de paquete RPM y el gestor de paquetes DNF para instalar, actualizar y eliminar software. DNF es una parte central de la experiencia en Fedora y es una de las herramientas principales en las que confían los usuarios para mantener el sistema actualizado.

La gestión de paquetes en Fedora es sencilla y encaja naturalmente con la familia más amplia de sistemas Red Hat.

:::single-choice{#identify-fedora-package-tool} ¿Qué herramienta utiliza Fedora para la gestión de paquetes de nivel superior?

::option[APT]{#fedora-apt-tool explanation="APT está asociado a las distribuciones basadas en Debian. Fedora pertenece a la familia de paquetes RPM y utiliza DNF."}
::option[DNF]{#fedora-dnf-tool .correct explanation="DNF instala, actualiza y elimina paquetes de los repositorios de Fedora. Por debajo, los paquetes de Fedora utilizan el formato RPM."}
::option[Pacman]{#fedora-pacman-tool explanation="Pacman es el gestor de paquetes de Arch Linux. La herramienta de paquetes de nivel superior de Fedora es DNF."}
:::

## Usos comunes

Fedora se utiliza comúnmente en estaciones de trabajo de desarrolladores, escritorios técnicos y portátiles. Es especialmente atractiva para usuarios que desean un entorno Linux moderno para programación, contenedores, máquinas virtuales y trabajo de escritorio general.

Aunque Fedora también puede utilizarse en servidores, su identidad más fuerte es, por lo general, la de una distribución Linux actual y amigable para el desarrollador.

## ¿Es Fedora apta para principiantes?

Fedora puede ser apta para principiantes, pero suele ser una mejor opción para usuarios que se sienten cómodos con un sistema que evoluciona con mayor rapidez. Es más fácil de abordar que las distribuciones altamente manuales, pero puede sentirse menos conservadora que Debian o menos centrada en principiantes que Ubuntu o Linux Mint.

Para los usuarios que desean una distribución de Linux moderna y no les importa aprender un poco sobre la marcha, Fedora es una opción sólida.

## Lecturas adicionales

- [Fedora Workstation](https://fedoraproject.org/workstation/)
- [Documentación de Fedora](https://docs.fedoraproject.org/)
- [Ciclo de vida de los lanzamientos de Fedora](https://docs.fedoraproject.org/en-US/releases/lifecycle/)
- [Grupo de trabajo de Fedora Workstation](https://docs.fedoraproject.org/en-US/workstation-working-group/)

Para desarrollar habilidades reales en Linux después de aprender sobre Fedora, recomendamos estos cursos de LabEx:

1. **[Inicio rápido con Linux](https://labex.io/es/courses/quick-start-with-linux)** - Cubre los conceptos básicos de Linux que se aplican a muchas distribuciones.
2. **[Práctica de comandos de Linux en línea](https://labex.io/es/courses/linux-basic-commands-practice-online)** - Fortalece los hábitos de línea de comandos que importan en el trabajo diario con Linux.
3. **[Gestión de paquetes RPM y DNF](https://labex.io/es/courses/rpm-and-dnf-package-management)** - Practica conceptos de gestión de paquetes relacionados con RPM y DNF.

## Resumen

Ahora puedes explicar el lugar de Fedora como distribución actual e impulsada por la comunidad dentro del ecosistema de Red Hat.

1. Describir el modelo comunitario y de patrocinio de Fedora.
2. Reconocer los usuarios y flujos de trabajo que admite Fedora Workstation.
3. Explicar la relación ascendente de Fedora con RHEL.
4. Planificar las actualizaciones periódicas de Fedora.
5. Identificar DNF como herramienta de gestión de paquetes de Fedora.
