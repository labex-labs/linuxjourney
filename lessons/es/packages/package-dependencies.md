---
lesson_id: "package-dependencies"
course_id: "packages"
lang: "es"
order_index: 4
title: "Dependencias de paquetes"
description: "Aprende cómo los metadatos de paquetes expresan capacidades, versiones, conflictos y relaciones de bibliotecas compartidas necesarias."
meta_title: "Dependencias de paquetes - Paquetes"
meta_description: "Aprende qué son las dependencias de paquetes Linux, las bibliotecas compartidas y cómo un gestor resuelve relaciones compatibles."
meta_keywords: "dependencias de paquetes Linux, bibliotecas compartidas, paquetes Linux, gestión de paquetes, instalación de software"
---

Una dependencia de paquete indica que un paquete necesita otro paquete, una capacidad o una versión compatible para instalarse o funcionar. Los gestores de paquetes que conocen los repositorios utilizan estos metadatos para calcular un conjunto coherente de cambios en vez de tratar cada archivo de forma aislada.

## Relaciones de dependencia

Los metadatos de un paquete pueden expresar algo más que un simple nombre obligatorio. Según el formato de la distribución, las relaciones pueden incluir:

- dependencias obligatorias
- restricciones de versión mínima, máxima o exacta
- alternativas, en las que cualquiera de varios proveedores satisface un requisito
- recomendaciones o sugerencias con una semántica menos estricta
- conflictos, incompatibilidades o sustituciones
- capacidades virtuales proporcionadas por más de un paquete

Estas reglas permiten que un solucionador elija un conjunto de versiones de paquetes compatible con los repositorios configurados, la arquitectura y el estado instalado. Una solución puede exigir actualizaciones, eliminaciones o elegir entre proveedores, por lo que debes revisar la transacción propuesta antes de aprobarla.

:::single-choice{#package-dependencies-solver-role} ¿Qué intenta producir un solucionador de dependencias que conoce los repositorios?

::option[Un conjunto coherente de versiones de paquetes y cambios necesarios.]{#package-dependencies-consistent-set .correct explanation="El solucionador evalúa las relaciones declaradas entre los paquetes instalados y disponibles."}
::option[Una cuenta de usuario nueva para cada aplicación instalada.]{#package-dependencies-user-account explanation="Crear cuentas puede ser una acción del ciclo de vida de un paquete, pero no es la finalidad de la resolución de dependencias."}
::option[Una copia comprimida de todos los archivos del repositorio.]{#package-dependencies-compressed-repository explanation="El solucionador selecciona metadatos y paquetes; no archiva el repositorio completo."}
:::

## Bibliotecas compartidas como dependencias

Una biblioteca compartida contiene código compilado que varios programas pueden asignar en memoria durante la ejecución. Compartirlo reduce las implementaciones duplicadas y permite que las distribuciones actualicen una biblioteca común de forma independiente, pero los programas dependen de una interfaz binaria de aplicación, o ABI, compatible.

En los sistemas Linux basados en ELF, un ejecutable puede registrar el nombre de una biblioteca necesaria, como un SONAME. El enlazador dinámico localiza una biblioteca instalada coincidente cuando se inicia el programa. Los metadatos del paquete suelen representar este requisito como una dependencia del paquete o de la capacidad que proporciona la biblioteca compatible.

:::single-choice{#package-dependencies-shared-library} ¿Qué es una biblioteca compartida?

::option[Código compilado que varios programas pueden cargar y utilizar.]{#package-dependencies-library-code .correct explanation="Una biblioteca compartida proporciona interfaces binarias reutilizables en vez de incorporar una implementación separada en cada programa."}
::option[Una lista de repositorios compartida entre distribuciones sin relación.]{#package-dependencies-shared-repository explanation="La configuración de repositorios y el código ejecutable de una biblioteca son conceptos distintos."}
::option[Un archivo de texto que contiene el historial del shell de todos los usuarios.]{#package-dependencies-shared-history explanation="El historial del shell son datos de usuario, no una dependencia de biblioteca de un programa."}
:::

## Compatibilidad de versiones y ABI

No basta con que exista un archivo con un nombre de biblioteca similar. Deben coincidir la ABI necesaria, la arquitectura, los símbolos y, en ocasiones, una versión mínima. Sustituir manualmente una biblioteca de la distribución puede inutilizar todos los programas que dependan de ella aunque el nombre del archivo parezca correcto.

Los mantenedores de paquetes codifican las relaciones entre bibliotecas y coordinan las transiciones cuando cambia una ABI. Mantén las bibliotecas nativas bajo el control del gestor de paquetes; para el software que necesite una versión incompatible, utiliza mecanismos compatibles de instalación paralela, contenedores, entornos o compilación.

:::single-choice{#package-dependencies-filename-insufficient} ¿Por qué puede fallar un programa aunque exista un archivo de biblioteca con un nombre parecido?

::option[Porque Linux solo permite que un ejecutable utilice cada biblioteca.]{#package-dependencies-one-consumer explanation="Una finalidad esencial de las bibliotecas compartidas es que las utilicen varios procesos y programas."}
::option[Porque las dependencias de paquetes solo se aplican antes del primer arranque del sistema.]{#package-dependencies-boot-only explanation="Las dependencias siguen siendo relevantes durante la instalación, las actualizaciones y la ejecución."}
::option[Porque la ABI o la arquitectura de la biblioteca puede no satisfacer al programa.]{#package-dependencies-abi-mismatch .correct explanation="El enlace durante la ejecución depende de interfaces binarias y arquitecturas de máquina compatibles, no solo del nombre de un archivo."}
:::

## Estados de dependencias rotas

Un problema de dependencias puede surgir por mezclar repositorios, interrumpir operaciones, instalar archivos manualmente, retener versiones, eliminar archivos o utilizar software de terceros incompatible. No respondas eliminando archivos de la base de datos de paquetes ni forzando una instalación a ciegas.

Primero lee los diagnósticos del gestor de paquetes, actualiza únicamente los metadatos de repositorios de confianza, examina las versiones retenidas o fijadas y revisa la reparación propuesta. Un instalador de paquetes de bajo nivel puede desempaquetar un archivo sin obtener todas sus dependencias; para una instalación habitual, una herramienta de repositorios de alto nivel suele ser más segura porque resuelve la transacción completa.

:::single-choice{#package-dependencies-low-level-limit} ¿Cuál es una limitación habitual de instalar un paquete local con una herramienta de archivos de bajo nivel?

::option[Puede que no obtenga ni resuelva todas las dependencias que falten en los repositorios.]{#package-dependencies-no-repository-resolution .correct explanation="Las herramientas de bajo nivel gestionan archivos y bases de datos de paquetes, pero pueden dejar la obtención de dependencias a un gestor de nivel superior."}
::option[Siempre recompila el kernel de Linux desde el código fuente.]{#package-dependencies-recompile-kernel explanation="Instalar un archivo de paquete no implica recompilar el kernel."}
::option[Impide que el paquete contenga bibliotecas compartidas.]{#package-dependencies-no-libraries explanation="Un archivo de paquete puede contener bibliotecas independientemente de la herramienta que lo instale."}
:::

Utiliza [Gestionar bibliotecas compartidas en Linux](https://labex.io/labs/comptia-manage-shared-libraries-in-linux-590867) para examinar las relaciones durante la ejecución y después compáralas con los metadatos de paquetes en [Gestionar paquetes con RPM](https://labex.io/labs/rhel-managing-packages-with-rpm-in-linux-590868).

## Resumen

Ahora puedes explicar cómo funciona la resolución de dependencias de paquetes.

1. Reconoce relaciones obligatorias, alternativas, con versión y conflictivas.
2. Relaciona los paquetes de bibliotecas compartidas con los requisitos de ABI durante la ejecución.
3. Considera los nombres de archivos como una prueba más débil que la compatibilidad de arquitectura e interfaz.
4. Revisa una transacción completa del gestor de paquetes antes de aplicar reparaciones.
