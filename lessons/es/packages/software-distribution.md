---
lesson_id: "software-distribution"
course_id: "packages"
lang: "es"
order_index: 1
title: "Distribución de software"
description: "Aprende cómo los proyectos originales, los mantenedores de distribuciones, los paquetes y sus formatos forman una cadena de suministro de software Linux."
meta_title: "Distribución de software - Paquetes"
meta_description: "Comprende la distribución de software Linux, los gestores de paquetes y formatos como .deb y .rpm."
meta_keywords: "distribución de software Linux, gestor de paquetes, paquetes deb, paquetes rpm, instalación de software"
---

El software de Linux se distribuye habitualmente en forma de paquetes gestionados por herramientas específicas de cada distribución. Un paquete agrupa archivos instalables con metadatos para que el sistema pueda controlar versiones, dependencias, propiedad, sumas de comprobación y acciones del ciclo de vida.

## Contenido de un paquete

Un paquete binario puede contener ejecutables, bibliotecas, documentación, configuración predeterminada, definiciones de servicios y otros recursos. También incluye metadatos como:

- nombre y versión del paquete
- arquitectura de destino y contexto de la distribución
- dependencias y conflictos declarados
- listas de archivos e información de integridad
- scripts o activadores opcionales utilizados durante operaciones del ciclo de vida

No todos los paquetes son aplicaciones interactivas. Un paquete puede proporcionar una biblioteca, un componente del kernel, datos de idioma, fuentes, símbolos de depuración o metadatos que dependan de un conjunto de otros paquetes.

:::single-choice{#software-distribution-package-metadata}
¿Qué información suele ser un metadato del paquete en vez de un ejecutable de la aplicación?

::option[Las instrucciones de CPU que implementan la aplicación.]{#software-distribution-executable-code explanation="Las instrucciones compiladas forman parte del contenido del paquete, no de los metadatos de dependencias."}
::option[Las relaciones de dependencia declaradas.]{#software-distribution-dependencies .correct explanation="Los paquetes describen los paquetes necesarios o incompatibles para que las herramientas de gestión puedan razonar sobre la instalación."}
::option[El documento sin guardar que el usuario tiene abierto en memoria.]{#software-distribution-user-document explanation="Los datos de usuario durante la ejecución no forman parte de los metadatos del paquete distribuido."}
:::

## Funciones del proyecto original y de la distribución

Un proyecto original desarrolla y publica el código fuente inicial. Después, los mantenedores de una distribución Linux adaptan ciertas versiones a la distribución. Su trabajo puede incluir revisar licencias, aplicar parches de integración o seguridad, definir instrucciones de compilación, dividir el resultado en paquetes, declarar dependencias, ejecutar pruebas y mantener actualizaciones.

La infraestructura de compilación de la distribución produce paquetes para las versiones y arquitecturas compatibles. Las herramientas del repositorio publican metadatos y firmas que los clientes pueden verificar. Las responsabilidades exactas varían: algunos proyectos originales publican sus propios paquetes, mientras que las distribuciones pueden compilar por separado a partir del código fuente.

:::single-choice{#software-distribution-maintainer-role}
¿Qué tarea suele corresponder al mantenedor de un paquete de una distribución?

::option[Adaptar el código fuente original a las reglas de compilación y dependencias de la distribución.]{#software-distribution-maintainer-integrates .correct explanation="Los mantenedores adaptan el software a las políticas, compilaciones, dependencias y entornos compatibles de la distribución."}
::option[Elegir la contraseña local de la cuenta de cada usuario.]{#software-distribution-maintainer-passwords explanation="Los datos de autenticación locales no guardan relación con el mantenimiento de paquetes."}
::option[Planificar en una CPU cada proceso instalado.]{#software-distribution-maintainer-scheduler explanation="El planificador del kernel en ejecución gestiona el uso de la CPU después de la instalación."}
:::

## Formatos de paquetes nativos habituales

Dos formatos nativos muy utilizados son:

- `.deb`, empleado por Debian y las distribuciones derivadas, entre ellas Ubuntu y Linux Mint
- `.rpm`, empleado por Fedora, Red Hat Enterprise Linux y muchas distribuciones relacionadas

Existen otros formatos nativos y formatos que abarcan varias distribuciones. Una extensión de archivo coincidente no garantiza por sí sola la compatibilidad: también importan la arquitectura del paquete, la versión de la distribución, las versiones de las bibliotecas, las políticas, las firmas y las dependencias.

:::single-choice{#software-distribution-debian-format}
¿Qué formato de paquete nativo utilizan Debian y Ubuntu?

::option[`.deb`]{#software-distribution-format-deb .correct explanation="Las herramientas de paquetes de la familia Debian utilizan el formato de archivo `.deb`."}
::option[`.rpm`]{#software-distribution-format-rpm explanation="RPM es nativo de Fedora, RHEL y familias de distribuciones relacionadas."}
::option[`.tar`]{#software-distribution-format-tar explanation="Un archivo tar es un contenedor general y por sí solo no proporciona los metadatos ni la semántica de ciclo de vida de un paquete Debian."}
:::

## Importancia de la distribución gestionada

Un gestor de paquetes registra el estado instalado y coordina los cambios entre paquetes. Instalar desde repositorios de confianza de la distribución suele proporcionar resolución coherente de dependencias, verificación de firmas, actualizaciones de seguridad y eliminación limpia. Copiar manualmente un binario o instalar desde el código fuente puede ser apropiado, pero no incorpora automáticamente el software a ese ciclo de vida gestionado.

La confianza sigue dependiendo de la configuración de los repositorios y de las claves de firma. Un paquete criptográficamente válido demuestra su asociación con una clave de confianza, no que cualquier software de terceros sea seguro o apropiado. Cuando sea posible, prefiere los repositorios de la distribución y evalúa cualquier fuente externa antes de concederle privilegios de instalación.

:::single-choice{#software-distribution-package-manager-benefit}
¿Cuál es una ventaja de instalar mediante un repositorio de paquetes de confianza?

::option[El gestor puede controlar las versiones y resolver las dependencias declaradas.]{#software-distribution-managed-lifecycle .correct explanation="Los metadatos del repositorio y los registros del estado instalado permiten coordinar la instalación, las actualizaciones y la eliminación."}
::option[Todos los programas instalados quedan inmunizados frente a fallos de seguridad.]{#software-distribution-no-vulnerabilities explanation="La gestión de paquetes facilita las actualizaciones, pero no puede garantizar que el software carezca de fallos."}
::option[Todos los paquetes de todas las distribuciones se vuelven intercambiables.]{#software-distribution-universal-compatibility explanation="Los paquetes nativos siguen ligados a formatos, versiones, arquitecturas y entornos de dependencias."}
:::

Utiliza el laboratorio [Gestionar paquetes con RPM](https://labex.io/labs/rhel-managing-packages-with-rpm-in-linux-590868) para examinar los metadatos y la integridad de los paquetes, o el laboratorio [Compilar software desde el código fuente](https://labex.io/labs/comptia-build-software-from-source-code-in-linux-590853) para comparar un flujo de trabajo basado en código fuente con los paquetes gestionados.

## Resumen

Ahora puedes identificar las partes principales de la distribución de software Linux.

1. Separa los archivos de contenido del paquete de sus metadatos.
2. Distingue el desarrollo original de la integración realizada por la distribución.
3. Asocia `.deb` y `.rpm` con sus familias de distribuciones.
4. Evalúa la compatibilidad y la confianza más allá de la extensión de un archivo.
