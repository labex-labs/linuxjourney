---
lesson_id: "compile-source-code"
course_id: "packages"
lang: "es"
order_index: 7
title: "Compilar código fuente"
description: "Aprende a verificar, configurar, compilar, probar, preparar y registrar software compilado desde el código fuente."
meta_title: "Compilar código fuente - Paquetes"
meta_description: "Aprende a compilar desde el código fuente en Linux con configure, make, pruebas y una instalación controlada."
meta_keywords: "compilar código fuente, make install, checkinstall, compilación Linux, build-essential, script configure, Makefile"
---

Compilar desde el código fuente puede proporcionar una versión o función que no esté disponible en los repositorios configurados, pero transfiere de la distribución a ti el trabajo de integración, actualización y confianza. Prefiere un paquete compatible de la distribución cuando satisfaga la necesidad.

## Verificar y leer antes de compilar

Obtén el código fuente desde un canal autenticado de publicaciones del proyecto original. Verifica su firma o suma de comprobación a través de una ruta de confianza y después examina el archivo antes de extraerlo en un directorio de preparación sin privilegios. Lee archivos como `README`, `INSTALL` y `SECURITY`, así como la documentación de compilación del proyecto.

Las instrucciones de compilación son código ejecutable. Un script `configure`, una definición de compilación, una prueba o un complemento del compilador pueden ejecutar órdenes arbitrarias como tu usuario. No compiles código fuente que no sea de confianza ni ejecutes la compilación propiamente dicha con `sudo`.

:::single-choice{#compile-source-code-build-privilege} ¿Por qué debe ejecutarse normalmente el paso de compilación sin `sudo`?

::option[Porque los compiladores se niegan a producir código máquina para el usuario root.]{#compile-source-code-root-compiler explanation="Los compiladores pueden ejecutarse como root, pero hacerlo aumenta el riesgo innecesariamente."}
::option[Porque `sudo` elimina automáticamente todos los archivos objeto generados.]{#compile-source-code-sudo-delete explanation="Elevar los privilegios no elimina por sí mismo los resultados de la compilación."}
::option[Porque la lógica de compilación puede ejecutar órdenes arbitrarias y normalmente no necesita privilegios del sistema.]{#compile-source-code-unprivileged-build .correct explanation="Mantener la compilación sin privilegios limita los daños de errores o instrucciones de compilación maliciosas."}
:::

## Instalar los requisitos de compilación

En un sistema de desarrollo de la familia Debian, un punto de partida habitual es:

```bash
$ sudo apt install build-essential
```

Esto instala un compilador básico y herramientas de compilación, no todas las dependencias que necesite cualquier proyecto. Los proyectos también pueden necesitar entornos de ejecución de lenguajes, generadores, herramientas de sistemas de compilación, cabeceras de desarrollo o versiones exactas de bibliotecas. Instala los requisitos desde repositorios de confianza y distingue las dependencias de compilación de las dependencias de ejecución.

:::single-choice{#compile-source-code-build-essential-scope} ¿Qué proporciona `build-essential` en un sistema de la familia Debian?

::option[Un conjunto básico de herramientas habituales de compilación.]{#compile-source-code-baseline-tools .correct explanation="Proporciona herramientas fundamentales, pero no puede anticipar todas las bibliotecas o generadores específicos de cada proyecto."}
::option[Todas las dependencias de todos los proyectos de código fuente.]{#compile-source-code-all-dependencies explanation="Cada proyecto declara requisitos adicionales y, en ocasiones, específicos de una versión."}
::option[Una garantía de que el código fuente descargado es de confianza.]{#compile-source-code-trust-guarantee explanation="Instalar herramientas no autentica una publicación de código fuente independiente."}
:::

## Configurar y compilar

Un proyecto tradicional de estilo Autoconf utiliza:

```bash
$ ./configure --prefix=/usr/local
$ make
```

`configure` comprueba el entorno y genera archivos de compilación según las opciones seleccionadas. `make` lee reglas de dependencias y órdenes, normalmente desde un `Makefile`, y crea los objetivos solicitados.

Esta secuencia no es universal. Los proyectos pueden utilizar CMake, Meson, Ninja, herramientas específicas de un lenguaje o scripts personalizados. Sigue la documentación de la versión exacta en vez de ejecutar `./configure` solo porque resulte familiar. Un directorio de compilación separado del árbol del código fuente puede mantener aparte los archivos generados cuando el sistema de compilación lo permita.

:::single-choice{#compile-source-code-make-role} En el flujo de trabajo tradicional, ¿qué hace `make`?

::option[Registra todos los resultados en la base de datos de paquetes de la distribución.]{#compile-source-code-make-package-db explanation="La compilación por sí sola no crea registros de propiedad de paquetes nativos."}
::option[Descarga automáticamente una publicación autenticada del código fuente.]{#compile-source-code-make-download explanation="La obtención y verificación del código fuente se realizan antes de la compilación local, salvo que un proyecto defina explícitamente otra cosa."}
::option[Ejecuta las reglas aplicables de la descripción de compilación.]{#compile-source-code-make-rules .correct explanation="Make evalúa las dependencias y ejecuta las órdenes necesarias para actualizar los objetivos seleccionados."}
:::

## Probar antes de instalar

Ejecuta el objetivo de pruebas documentado por el proyecto, por ejemplo:

```bash
$ make check
```

El objetivo real podría ser `test`, `check` o una orden independiente. Investiga los fallos en vez de instalar resultados que no se hayan probado. Las pruebas pueden necesitar acceso a la red, servicios, hardware especial o aislamiento; revísalas antes de ejecutarlas igual que revisas el resto del código de compilación.

:::single-choice{#compile-source-code-test-failure} ¿Qué debes hacer cuando falla el conjunto de pruebas documentado?

::option[Ejecutar inmediatamente la misma instalación como root.]{#compile-source-code-install-after-failure explanation="Los privilegios no resuelven un fallo de corrección desconocido y aumentan sus consecuencias."}
::option[Eliminar la base de datos del gestor de paquetes para evitar conflictos.]{#compile-source-code-delete-database explanation="La base de datos nativa no guarda relación con la resolución de un fallo en las pruebas del código fuente y no debe descartarse."}
::option[Investigar el fallo antes de instalar la compilación.]{#compile-source-code-investigate-tests .correct explanation="Una prueba fallida puede revelar dependencias incompatibles, defectos de compilación o supuestos sobre el entorno."}
:::

## Preparar y registrar la instalación

`sudo make install` puede copiar archivos directamente en prefijos del sistema sin registrarlos en la base de datos de paquetes nativa. Los objetivos de desinstalación son opcionales y pueden estar incompletos, mientras que las actualizaciones posteriores pueden sobrescribir archivos o dejarlos huérfanos.

Prefiere uno de estos métodos controlados:

- crear un paquete nativo oficial con las herramientas de empaquetado de la distribución
- instalar bajo un prefijo claramente separado, como `/usr/local`, cuando la política lo permita
- preparar los archivos en una raíz temporal de empaquetado mediante un mecanismo compatible como `DESTDIR`
- utilizar un prefijo de usuario sin privilegios, un entorno aislado o un contenedor cuando sea apropiado

`checkinstall` puede crear un paquete sencillo para algunos flujos de trabajo con `make install`, pero no es universal ni sustituye una receta de paquete revisada y con la calidad de una distribución. Nunca lo trates como una regla que se deba aplicar «siempre». Antes de cualquier copia con privilegios, examina la lista de archivos preparados, la propiedad, los permisos, las rutas y el plan de desinstalación o actualización.

:::single-choice{#compile-source-code-destdir-purpose} ¿Qué finalidad tiene una instalación de preparación compatible con `DESTDIR`?

::option[Colocar los archivos que se instalarían bajo una raíz temporal para examinarlos o empaquetarlos.]{#compile-source-code-stage-root .correct explanation="La preparación separa la recopilación de archivos de la escritura inmediata en el prefijo activo del sistema."}
::option[Convertir el compilador en un repositorio remoto de paquetes.]{#compile-source-code-destdir-repository explanation="La variable redirige las rutas de instalación y no publica metadatos de repositorios."}
::option[Omitir la compilación y descargar en su lugar binarios desconocidos.]{#compile-source-code-destdir-download explanation="La preparación se aplica después de una compilación y no la sustituye por una descarga binaria externa."}
:::

Utiliza [Compilar software desde el código fuente en Linux](https://labex.io/labs/comptia-build-software-from-source-code-in-linux-590853) en un entorno desechable para practicar el flujo de trabajo sin mezclar archivos experimentales con un sistema de producción.

## Resumen

Ahora puedes abordar la compilación desde el código fuente como un flujo controlado de suministro de software.

1. Autentica el código fuente y revisa sus instrucciones como código ejecutable.
2. Instala requisitos de compilación explícitos desde repositorios de confianza.
3. Configura, compila y prueba sin privilegios innecesarios.
4. Prepara y examina los resultados antes de instalarlos en el sistema.
5. Registra los archivos instalados mediante paquetes nativos o un prefijo aislado elegido deliberadamente.
