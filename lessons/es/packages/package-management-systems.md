---
lesson_id: "package-management-systems"
course_id: "packages"
lang: "es"
order_index: 6
title: "yum y apt"
description: "Aprende los flujos de trabajo de APT y DNF con repositorios para examinar, instalar, eliminar y actualizar paquetes."
meta_title: "yum y apt - Paquetes"
meta_description: "Aprende a utilizar APT, DNF y yum para instalar, eliminar y actualizar paquetes en sistemas Linux basados en Debian y RPM."
meta_keywords: "yum y apt, DNF, gestión de paquetes Linux, Debian, Red Hat, instalar paquetes, actualizar paquetes"
---

Los gestores de paquetes que conocen los repositorios obtienen metadatos, resuelven dependencias, verifican contenido autenticado y coordinan transacciones. Los sistemas de la familia Debian suelen utilizar APT. Las versiones actuales de Fedora y Red Hat Enterprise Linux utilizan DNF; en las versiones actuales de RHEL, la orden `yum` se mantiene como alias de compatibilidad para DNF, mientras que los sistemas antiguos utilizaban la implementación original de YUM.

Sigue siempre la documentación de la distribución y la versión instaladas en vez de suponer que un conjunto de órdenes sirve en todas partes.

## Actualizar y examinar metadatos

APT separa la actualización de metadatos de la actualización de paquetes:

```bash
Debian family: $ sudo apt update
```

Busca y examina antes de instalar:

```bash
Debian family: $ apt search package-name
Debian family: $ apt show package-name
RPM family:    $ dnf search package-name
RPM family:    $ dnf info package-name
```

La configuración de los repositorios determina qué pueden descubrir estas órdenes. Lee atentamente los nombres de fuentes, las arquitecturas, las versiones y los errores de firma.

:::single-choice{#package-management-systems-apt-show}
¿Qué orden muestra los detalles de APT para `package-name`?

::option[`apt remove package-name`]{#package-management-systems-apt-remove-command explanation="La suborden `remove` propone desinstalar el paquete."}
::option[`dnf search package-name`]{#package-management-systems-dnf-search-command explanation="Esta orden busca en repositorios de la familia RPM y no es la orden de APT que muestra detalles."}
::option[`apt show package-name`]{#package-management-systems-apt-show-command .correct explanation="La suborden `show` presenta los metadatos del paquete binario indicado."}
:::

## Instalar paquetes

Instala mediante el nombre del paquete en el repositorio con:

```bash
Debian family: $ sudo apt install package-name
RPM family:    $ sudo dnf install package-name
```

El gestor propone las dependencias y cualquier conflicto o sustitución. No confirmes automáticamente hasta haber revisado el origen, la versión y la arquitectura del paquete, el tamaño de la descarga, el cambio de espacio en disco, las eliminaciones y las dependencias que se instalarán.

:::single-choice{#package-management-systems-dnf-install}
¿Qué orden actual instala `package-name` desde los repositorios configurados de la familia RPM?

::option[`rpm -qa package-name`]{#package-management-systems-rpm-query-command explanation="Esta es una consulta de la base de datos de paquetes RPM instalados, no una solicitud de instalación desde un repositorio."}
::option[`dnf install package-name`]{#package-management-systems-dnf-install-command .correct explanation="DNF es el gestor actual que conoce los repositorios en Fedora y las versiones recientes de RHEL."}
::option[`apt update package-name`]{#package-management-systems-apt-update-package explanation="APT update actualiza los índices y no instala un paquete con nombre de la familia RPM."}
:::

## Eliminar paquetes

Solicita una eliminación con:

```bash
Debian family: $ sudo apt remove package-name
RPM family:    $ sudo dnf remove package-name
```

Una eliminación puede afectar a paquetes dependientes o dejar dependencias y configuración que ya no se utilizan. Revisa la transacción propuesta, distingue las semánticas de eliminación y purga en los sistemas de la familia Debian, y conserva los datos de la aplicación conforme a su propio procedimiento de copia de seguridad y retención. La eliminación de un paquete no promete borrar los datos creados por los usuarios.

:::single-choice{#package-management-systems-remove-review}
¿Por qué debes revisar una transacción de eliminación antes de confirmarla?

::option[Porque la eliminación siempre vuelve a formatear el sistema de archivos que contiene el paquete.]{#package-management-systems-removal-format explanation="Los gestores eliminan archivos y estado gestionados; normalmente no formatean un sistema de archivos."}
::option[Porque los gestores de paquetes no pueden mostrar un conjunto de cambios propuesto.]{#package-management-systems-no-proposal explanation="Los gestores interactivos suelen mostrar la transacción prevista precisamente para que pueda revisarse."}
::option[Porque otros paquetes pueden depender del paquete seleccionado y verse también afectados.]{#package-management-systems-dependent-removal .correct explanation="Las restricciones de dependencias pueden ampliar una solicitud más allá del único nombre de paquete introducido."}
:::

## Aplicar actualizaciones

En un sistema APT, actualiza los metadatos y después revisa las actualizaciones como pasos correctos independientes:

```bash
$ sudo apt update
$ apt list --upgradable
$ sudo apt upgrade
```

En un sistema DNF, examina y aplica las actualizaciones disponibles con el flujo de trabajo documentado localmente:

```bash
$ dnf check-update
$ sudo dnf upgrade
```

Una orden de actualización puede modificar bibliotecas esenciales, servicios, kernels y dependencias. Utiliza copias de seguridad, políticas de mantenimiento, notas de la versión y una planificación de reinicios apropiadas para el sistema. Comprueba la semántica del estado de salida: por ejemplo, algunas operaciones de comprobación de actualizaciones utilizan un estado distinto de cero para indicar que hay actualizaciones disponibles, no que la ejecución haya fallado.

:::single-choice{#package-management-systems-apt-update-upgrade}
¿Qué relación existe entre `apt update` y `apt upgrade`?

::option[`update` elimina paquetes; `upgrade` restaura sus archivos de configuración.]{#package-management-systems-apt-remove-restore explanation="Ninguna de las dos órdenes mantiene esa relación de eliminación y restauración."}
::option[`update` actualiza los metadatos; `upgrade` aplica un plan aprobado de actualización de paquetes.]{#package-management-systems-apt-two-steps .correct explanation="APT separa la actualización del catálogo de la instalación de versiones de paquetes más recientes."}
::option[Son nombres idénticos para una sola operación.]{#package-management-systems-apt-identical explanation="Realizan etapas distintas y deben comprobarse por separado."}
:::

## Elegir `dnf` o `yum`

Utiliza `dnf` en la documentación actual de Fedora y RHEL. Una orden `yum` en un sistema RHEL reciente puede invocar el comportamiento de compatibilidad de DNF, pero los scripts no deben deducir la implementación únicamente del nombre del ejecutable. En equipos antiguos, verifica la versión instalada y la sintaxis compatible antes de adaptar instrucciones.

:::single-choice{#package-management-systems-yum-current-rhel}
¿Qué representa habitualmente `yum` en un sistema RHEL actual?

::option[Una orden de compatibilidad respaldada por DNF.]{#package-management-systems-yum-dnf-alias .correct explanation="Las versiones recientes de RHEL utilizan DNF y conservan el nombre de la orden yum por compatibilidad."}
::option[La herramienta de bajo nivel de Debian para archivos `.deb`.]{#package-management-systems-yum-dpkg explanation="Los sistemas Debian utilizan herramientas como APT y dpkg, no YUM, para gestionar paquetes nativos."}
::option[Un compresor exclusivo de metadatos de repositorios.]{#package-management-systems-yum-compressor explanation="YUM y DNF son interfaces de gestión de paquetes, no formatos de compresión independientes."}
:::

Practica APT en [Instalar y eliminar paquetes](https://labex.io/labs/linux-installing-and-removing-packages-385380) y los conceptos de la familia DNF/YUM en [Consultar y actualizar paquetes con YUM](https://labex.io/labs/rhel-query-and-update-packages-with-yum-in-linux-590869).

## Resumen

Ahora puedes elegir y revisar operaciones habituales de paquetes mediante repositorios.

1. Utiliza APT en sistemas de la familia Debian y DNF en sistemas actuales de la familia RPM.
2. Examina los metadatos y los cambios de dependencias propuestos antes de instalar.
3. Trata la eliminación como una transacción que considera dependencias, no como el borrado de un solo archivo.
4. Separa la actualización de metadatos de la aplicación de actualizaciones cuando la herramienta lo haga.
5. Verifica si `yum` es el YUM antiguo o una orden de compatibilidad de DNF.
