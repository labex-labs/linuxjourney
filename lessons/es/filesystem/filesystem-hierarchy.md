---
lesson_id: "filesystem-hierarchy"
course_id: "filesystem"
lang: "es"
order_index: 1
title: "Jerarquía del sistema de archivos"
description: "Aprende las funciones previstas de los principales directorios de Linux y cómo pueden diferir los diseños fusionados modernos."
meta_title: "Jerarquía del sistema de archivos - El sistema de archivos"
meta_description: "Explora la jerarquía del sistema de archivos Linux y las funciones de directorios como /bin, /etc, /home, /usr y /var."
meta_keywords: "jerarquía del sistema de archivos Linux, FHS, estructura de directorios Linux, /etc, /usr, /var"
---

Linux presenta los sistemas de archivos montados como un único árbol de directorios con raíz en `/`. El estándar de jerarquía del sistema de archivos, o FHS, asigna funciones convencionales a muchos directorios, pero las distribuciones, los contenedores, los sistemas inmutables y las políticas locales pueden diferir. Examina el equipo real antes de depender de una ruta.

```bash
$ ls -ld /*
```

## Raíz y rutas esenciales del sistema

- `/` es la raíz del árbol visible del sistema de archivos.
- `/etc` contiene configuración del sistema específica del equipo. Puede incluir scripts auxiliares o de inicio ejecutables, por lo que es incorrecto afirmar que nunca contiene contenido ejecutable.
- `/boot` contiene archivos relacionados con el arranque, como datos del gestor de arranque y, en muchos sistemas, kernels e imágenes iniciales del sistema de archivos en RAM.
- `/bin` y `/sbin` contienen tradicionalmente órdenes esenciales de usuario y administración del sistema.
- `/lib` y sus variantes específicas de arquitectura contienen tradicionalmente bibliotecas compartidas esenciales y componentes del cargador.

Muchas distribuciones actuales utilizan un diseño `/usr` fusionado en el que `/bin`, `/sbin` y `/lib` son enlaces simbólicos a los directorios correspondientes bajo `/usr`. Utiliza el descubrimiento de órdenes y los registros de paquetes en vez de suponer si una ruta es un directorio físico o un enlace.

:::single-choice{#filesystem-hierarchy-configuration-directory} ¿Qué directorio contiene convencionalmente la configuración del sistema específica del equipo?

::option[`/proc`]{#filesystem-hierarchy-proc-config explanation="Procfs presenta interfaces activas de procesos y del kernel, no archivos persistentes de configuración del equipo."}
::option[`/etc`]{#filesystem-hierarchy-etc .correct explanation="La configuración del sistema y de los servicios se organiza convencionalmente bajo `/etc`."}
::option[`/dev`]{#filesystem-hierarchy-dev-config explanation="`/dev` contiene objetos activos orientados a dispositivos, no la jerarquía general de configuración."}
:::

## Software de la distribución y local

- `/usr` contiene la principal jerarquía compartible y mayoritariamente de solo lectura del sistema operativo y las aplicaciones, incluidas órdenes, bibliotecas y datos independientes de la arquitectura.
- `/usr/local` se reserva para software y datos instalados por el administrador local fuera de la gestión habitual de `/usr` de la distribución.
- `/opt` puede contener paquetes de aplicaciones adicionales en subárboles independientes.

A pesar de su nombre, `/usr` no es el lugar donde suelen residir los archivos personales de cada usuario. Los gestores de paquetes de las distribuciones suelen ser propietarios de gran parte de su contenido, por lo que copiar archivos compilados localmente en `/usr/bin` puede entrar en conflicto con paquetes gestionados.

:::single-choice{#filesystem-hierarchy-local-software} ¿Qué prefijo se reserva convencionalmente para software instalado localmente fuera del contenido de `/usr` gestionado por la distribución?

::option[`/usr/local`]{#filesystem-hierarchy-usr-local .correct explanation="La jerarquía local separa el software instalado por el administrador del árbol `/usr` principal de la distribución."}
::option[`/proc/local`]{#filesystem-hierarchy-proc-local explanation="Procfs es una interfaz virtual del kernel, no un prefijo persistente de software."}
::option[`/dev/local`]{#filesystem-hierarchy-dev-local explanation="El almacenamiento de nodos de dispositivo no es la ubicación convencional para aplicaciones locales."}
:::

## Datos de usuarios y servicios

- `/home` contiene convencionalmente los directorios personales de los usuarios distintos de root, aunque los servicios de directorio y la política local pueden situarlos en otros lugares.
- `/root` es el directorio personal convencional de la cuenta root.
- `/srv` está destinado a datos específicos del sitio que sirve este sistema.

Una ruta personal procede de la información de la cuenta, no simplemente de unir `/home` con un nombre de usuario. Utiliza `getent passwd USER` o el directorio personal resuelto por el shell en vez de codificar supuestos.

:::single-choice{#filesystem-hierarchy-root-home} ¿Cuál es el directorio personal convencional de la cuenta root?

::option[`/home/root`]{#filesystem-hierarchy-home-root explanation="Los directorios personales ordinarios suelen aparecer bajo `/home`, pero root tiene una ruta convencional distinta."}
::option[`/root`]{#filesystem-hierarchy-root .correct explanation="El directorio personal de la cuenta privilegiada se sitúa convencionalmente directamente bajo la raíz del sistema de archivos."}
::option[`/usr/root`]{#filesystem-hierarchy-usr-root explanation="`/usr` es la jerarquía de software y datos compartidos, no el directorio personal de root."}
:::

## Datos variables, de ejecución y temporales

- `/var` contiene datos variables como registros, cachés, colas y estado de aplicaciones. Los registros del sistema suelen aparecer bajo `/var/log`, aunque algunos sistemas dependen principalmente de una interfaz de journal.
- `/run` contiene estado volátil de ejecución para el arranque actual, como sockets, estado de servicios y archivos PID. Normalmente se vuelve a crear al arrancar.
- `/tmp` está destinado a archivos temporales y suele permitir que todos los usuarios escriban con la protección del bit pegajoso.
- `/var/tmp` está destinado a archivos temporales que deben sobrevivir más tiempo que los situados en `/tmp`.

La política de limpieza de `/tmp` varía; no supongas que los archivos persisten hasta el reinicio ni que siempre se eliminan al reiniciar. Las aplicaciones deben crear archivos temporales de forma segura en vez de utilizar nombres predecibles.

:::single-choice{#filesystem-hierarchy-log-path} ¿Qué ruta almacena convencionalmente archivos de registro del sistema?

::option[`/etc/log`]{#filesystem-hierarchy-etc-log explanation="`/etc` contiene configuración, no datos ordinarios de registros que se acumulan."}
::option[`/var/log`]{#filesystem-hierarchy-var-log .correct explanation="Los registros son una categoría de datos cambiantes del sistema organizada bajo la jerarquía de datos variables."}
::option[`/boot/log`]{#filesystem-hierarchy-boot-log explanation="`/boot` se reserva para elementos relacionados con el arranque, no registros generales de servicios."}
:::

## Dispositivos, interfaces del kernel y puntos de montaje

- `/dev` contiene nodos de dispositivo y enlaces activos relacionados.
- `/proc` expone interfaces de procesos y del kernel mediante procfs.
- `/sys` expone objetos, dispositivos, controladores y atributos del kernel mediante sysfs.
- `/media` suele utilizarse para medios extraíbles montados automáticamente.
- `/mnt` es una ubicación convencional para montajes temporales del administrador.

Son convenciones, no concesiones de permisos. Montar otro sistema de archivos sobre un directorio no vacío oculta temporalmente el contenido anterior del directorio hasta que se desmonta.

:::single-choice{#filesystem-hierarchy-sysfs-path} ¿Qué ruta expone normalmente el modelo de dispositivos del kernel mediante sysfs?

::option[`/srv`]{#filesystem-hierarchy-srv explanation="`/srv` está destinado a los datos servidos por el sistema."}
::option[`/sys`]{#filesystem-hierarchy-sys .correct explanation="Sysfs se monta convencionalmente en `/sys` y presenta dispositivos, controladores, buses y atributos."}
::option[`/opt`]{#filesystem-hierarchy-opt explanation="`/opt` contiene árboles de aplicaciones adicionales opcionales."}
:::

Utiliza [Navegar por el sistema de archivos en Linux](https://labex.io/labs/comptia-navigate-the-filesystem-in-linux-590971) para examinar estas rutas y [Encontrar archivos y órdenes en Linux](https://labex.io/labs/comptia-find-files-and-commands-in-linux-590834) para no depender de ubicaciones adivinadas.

## Resumen

Ahora puedes relacionar las principales rutas de Linux con sus funciones previstas y permitir variaciones reales del sistema.

1. Parte del árbol unificado con raíz en `/`.
2. Separa configuración, software gestionado, software local y datos variables.
3. Distingue los directorios personales y los datos de servicios del estado de ejecución.
4. Reconoce `/dev`, `/proc` y `/sys` como interfaces especiales durante la ejecución.
5. Examina enlaces simbólicos, montajes, datos de cuentas y políticas de la distribución antes de suponer un diseño.
