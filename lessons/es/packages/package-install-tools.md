---
lesson_id: "package-install-tools"
course_id: "packages"
lang: "es"
order_index: 5
title: "rpm y dpkg"
description: "Aprende cómo `dpkg` y `rpm` examinan y modifican sus bases de datos de paquetes nativas y sus archivos locales."
meta_title: "rpm y dpkg - Paquetes"
meta_description: "Aprende a examinar, instalar, eliminar y listar paquetes mediante rpm y dpkg para archivos .deb y .rpm."
meta_keywords: "rpm, dpkg, gestión de paquetes Linux, paquetes deb, paquetes rpm, instalar paquetes"
---

`dpkg` es la herramienta de paquetes de bajo nivel en los sistemas de la familia Debian, mientras que `rpm` desempeña una función similar en los sistemas de la familia RPM. Desempaquetan archivos nativos, ejecutan acciones del ciclo de vida del paquete y actualizan las bases de datos de paquetes instalados. Herramientas que conocen los repositorios, como APT y DNF, se apoyan en estos mecanismos de nivel inferior.

## Examinar un archivo antes de instalarlo

Un archivo de paquete no equivale a un único archivo ejecutable. Puede contener muchos archivos de contenido, metadatos, tratamiento de la configuración y scripts de ciclo de vida con privilegios. Antes de instalarlo, examina su origen, la firma o la ruta de descarga autenticada, los metadatos y el contenido.

```bash
Debian: $ dpkg-deb --info ./some-package.deb
Debian: $ dpkg-deb --contents ./some-package.deb
RPM:    $ rpm -qip ./some-package.rpm
RPM:    $ rpm -qlp ./some-package.rpm
```

La `p` de las formas de consulta RPM mostradas significa «consultar un archivo de paquete» en vez de la base de datos instalada. La salida de una consulta ayuda a revisar un paquete, pero no puede demostrar que sus scripts o programas sean seguros.

:::single-choice{#package-install-tools-native-format}
¿Qué herramienta de bajo nivel gestiona los paquetes `.deb` de Debian y su base de datos instalada?

::option[`rpm`]{#package-install-tools-rpm-debian explanation="RPM gestiona su propio formato nativo y su base de datos en los sistemas de la familia RPM."}
::option[`tar`]{#package-install-tools-tar-debian explanation="Tar puede leer archivos, pero no implementa el ciclo de vida de los paquetes Debian instalados."}
::option[`dpkg`]{#package-install-tools-dpkg-debian .correct explanation="Los sistemas de la familia Debian utilizan `dpkg` para las operaciones de bajo nivel con archivos `.deb` y la base de datos de paquetes."}
:::

## Instalar un archivo local

La instalación directa de bajo nivel utiliza:

```bash
Debian: $ sudo dpkg -i ./some-package.deb
RPM:    $ sudo rpm -U ./some-package.rpm
```

`dpkg -i` puede desempaquetar y configurar el archivo solicitado, pero no obtiene las dependencias que falten en los repositorios. Del mismo modo, `rpm` sin intermediarios no proporciona el flujo de trabajo habitual del solucionador de repositorios. Para un archivo local suele ser preferible una orden de nivel superior, porque puede resolver dependencias desde las fuentes configuradas:

```bash
Debian: $ sudo apt install ./some-package.deb
RPM:    $ sudo dnf install ./some-package.rpm
```

Revisa la transacción antes de confirmarla. En APT, el prefijo `./` distingue una ruta local a un archivo Debian del nombre de un paquete del repositorio.

:::single-choice{#package-install-tools-local-dependencies}
¿Qué orden mostrada puede instalar un archivo `.deb` local y resolver las dependencias disponibles en los repositorios?

::option[`dpkg -l ./some-package.deb`]{#package-install-tools-dpkg-list-file explanation="`dpkg -l` muestra selecciones de paquetes instalados y no es el flujo de instalación local con resolución de dependencias."}
::option[`rpm -qa ./some-package.deb`]{#package-install-tools-rpm-query-deb explanation="La sintaxis de consulta de RPM no instala un archivo Debian."}
::option[`apt install ./some-package.deb`]{#package-install-tools-apt-local .correct explanation="APT reconoce la ruta local explícita y puede utilizar los repositorios configurados para satisfacer las dependencias declaradas."}
:::

## Eliminar un paquete instalado

La eliminación recibe el nombre de un paquete instalado, no el nombre del archivo utilizado anteriormente:

```bash
Debian: $ sudo dpkg --remove package-name
RPM:    $ sudo rpm --erase package-name
```

En Debian, `--remove` suele conservar los archivos de configuración clasificados como conffiles; `--purge` solicita que también se eliminen, sujeto a los scripts del paquete y a los datos no gestionados. Ninguna de las dos órdenes garantiza la eliminación de los datos creados por los usuarios. Las órdenes de nivel superior `apt remove` o `dnf remove` suelen ser mejores porque pueden evaluar los paquetes relacionados y presentar una transacción completa.

:::single-choice{#package-install-tools-remove-operand}
¿Qué operando espera `dpkg --remove` para un paquete instalado?

::option[La URL del índice del repositorio.]{#package-install-tools-remove-url explanation="La ubicación del repositorio no es la identidad del paquete que se pasa a la eliminación de bajo nivel."}
::option[El nombre del paquete instalado.]{#package-install-tools-remove-name .correct explanation="La eliminación se dirige al registro del paquete, como `example`, y no necesita su antigua ruta `.deb`."}
::option[El PID de un proceso iniciado por el paquete.]{#package-install-tools-remove-pid explanation="Los identificadores de proceso no guardan relación con la clave de la base de datos de paquetes instalados."}
:::

## Consultar el estado instalado

Muestra los registros de paquetes instalados o conocidos con:

```bash
Debian: $ dpkg-query -l
RPM:    $ rpm -qa
```

Para una inspección concreta, prefiere un nombre de paquete específico y un formato legible por máquinas cuando importe la fiabilidad de un script. Las bases de datos de paquetes describen el estado gestionado; los administradores locales o las aplicaciones todavía pueden modificar los archivos después, así que utiliza las funciones de verificación cuando necesites comparar los archivos instalados con los metadatos registrados.

:::single-choice{#package-install-tools-rpm-list-installed}
¿Qué orden consulta todos los paquetes registrados como instalados en la base de datos RPM?

::option[`rpm -qa`]{#package-install-tools-rpm-query-all .correct explanation="`-q` selecciona el modo de consulta y `-a` lo amplía a todos los registros de paquetes instalados."}
::option[`rpm -e`]{#package-install-tools-rpm-erase explanation="`-e` solicita eliminar un paquete en vez de mostrar una lista de solo lectura."}
::option[`dpkg-deb --contents`]{#package-install-tools-deb-contents explanation="Esta orden examina el contenido de un archivo Debian, no la base de datos RPM instalada."}
:::

Utiliza [Gestionar paquetes con RPM](https://labex.io/labs/rhel-managing-packages-with-rpm-in-linux-590868) para practicar consultas de archivos y comprobaciones de integridad en un sistema aislado.

## Resumen

Ahora puedes distinguir las operaciones de paquetes de bajo nivel de las transacciones con repositorios.

1. Examina los metadatos y el contenido de los archivos locales antes de instalarlos.
2. Utiliza `dpkg` para `.deb` y `rpm` para `.rpm` en las operaciones de bajo nivel.
3. Prefiere APT o DNF cuando haya que resolver dependencias.
4. Elimina mediante el nombre del paquete instalado y verifica por separado el estado gestionado.
