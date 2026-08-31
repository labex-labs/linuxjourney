---
lesson_id: "package-repositories"
course_id: "packages"
lang: "es"
order_index: 2
title: "Repositorios de paquetes"
description: "Aprende cómo los repositorios publican índices de paquetes firmados y cómo APT descubre las fuentes configuradas de la familia Debian."
meta_title: "Repositorios de paquetes - Paquetes"
meta_description: "Explora los repositorios de paquetes de Linux y aprende cómo APT utiliza sources.list y sources.list.d para encontrar paquetes."
meta_keywords: "repositorios de paquetes Linux, fuentes APT, /etc/apt/sources.list, paquetes Linux, gestión de paquetes"
---

Un repositorio de paquetes publica paquetes junto con índices y metadatos de versiones. Un gestor de paquetes descarga esos índices, selecciona versiones compatibles con la distribución y la arquitectura configuradas, verifica la autenticidad del repositorio y obtiene los archivos de paquetes necesarios.

## Metadatos del repositorio y catálogos locales

Un repositorio es más que un directorio de archivos. Sus metadatos describen nombres de paquetes, versiones, arquitecturas, sumas de comprobación, dependencias y secciones del repositorio disponibles. El cliente almacena en caché un catálogo local para poder buscar y resolver paquetes sin descargar primero todos los archivos.

En un sistema de la familia Debian, actualiza los metadatos configurados con:

```bash
$ sudo apt update
```

Esto actualiza los índices locales de paquetes; no instala por sí solo todas las actualizaciones disponibles. Revisa las fuentes y los errores de autenticación comunicados en vez de ignorar las entradas fallidas.

:::single-choice{#package-repositories-apt-update}
¿Qué actualiza principalmente `apt update`?

::option[Todos los binarios de paquetes instalados sin confirmación.]{#package-repositories-all-binaries explanation="La instalación de actualizaciones es una operación distinta de la actualización de metadatos."}
::option[Las contraseñas de los usuarios autorizados para instalar paquetes.]{#package-repositories-user-passwords explanation="La actualización de los índices de repositorios no modifica las credenciales de autenticación locales."}
::option[Los índices locales que describen los paquetes disponibles en las fuentes configuradas.]{#package-repositories-local-indexes .correct explanation="APT descarga los metadatos actuales de los repositorios para que las búsquedas y la resolución de dependencias posteriores utilicen un catálogo actualizado."}
:::

## Configuración de fuentes de APT

APT lee las fuentes configuradas en:

- `/etc/apt/sources.list`
- los archivos con extensión `.list` o `.sources` situados bajo `/etc/apt/sources.list.d/`

La extensión `.list` utiliza el formato tradicional de una línea. La extensión `.sources` utiliza bloques de estilo deb822, que la documentación actual de APT recomienda para configuraciones nuevas. Una distribución puede colocar sus fuentes predeterminadas en cualquiera de los dos lugares, por lo que no se garantiza que `/etc/apt/sources.list` contenga la configuración completa o principal.

Una fuente de estilo deb822 puede tener este aspecto:

```text
Types: deb
URIs: https://deb.example.invalid/repository
Suites: stable
Components: main
Signed-By: /etc/apt/keyrings/example.gpg
```

Esto solo ilustra la sintaxis; el dominio reservado `.invalid` no es un repositorio utilizable.

:::single-choice{#package-repositories-apt-locations}
¿Dónde puede leer APT definiciones activas de repositorios?

::option[Únicamente en `/etc/apt/sources.list`.]{#package-repositories-only-main-list explanation="APT también lee archivos de fuentes compatibles en `/etc/apt/sources.list.d/`."}
::option[Únicamente en archivos situados dentro del directorio personal de cada usuario.]{#package-repositories-only-home explanation="La configuración de fuentes de APT para el sistema suele residir bajo `/etc/apt`."}
::option[En `/etc/apt/sources.list` y en los archivos compatibles de `/etc/apt/sources.list.d/`.]{#package-repositories-both-locations .correct explanation="APT combina el archivo principal con las definiciones `.list` y `.sources` del directorio de listas de fuentes."}
:::

## Autenticación de repositorios

APT verifica los metadatos firmados de la versión del repositorio y después contrasta los paquetes descargados con las sumas de comprobación autenticadas de esos metadatos. `Signed-By` permite limitar una fuente a un llavero concreto en vez de confiar para ese repositorio en todas las claves configuradas globalmente.

Una firma válida demuestra que los metadatos proceden del poseedor de una clave de firma aceptada y que no se modificaron sin ser detectados. No demuestra que el software del editor carezca de defectos, sea inofensivo o resulte apropiado para el sistema. Confirma la huella de la clave y las instrucciones de la fuente a través de un canal de confianza independiente.

:::single-choice{#package-repositories-signed-by}
¿Qué finalidad de seguridad tiene `Signed-By` en una definición de fuente de APT?

::option[Cifrar todos los paquetes instalados para que el usuario root no pueda leerlos.]{#package-repositories-package-encryption explanation="La firma de repositorios comprueba el origen y la integridad, pero no oculta información al administrador local."}
::option[Limitar esa fuente a determinadas claves de firma.]{#package-repositories-key-scope .correct explanation="El campo vincula la verificación del repositorio a un llavero seleccionado en vez de a un conjunto global de claves sin restricciones."}
::option[Garantizar que el repositorio no contiene software vulnerable.]{#package-repositories-no-vulnerabilities explanation="La autenticidad criptográfica no evalúa la calidad del software ni sus defectos de seguridad."}
:::

## Añadir fuentes de terceros deliberadamente

Un repositorio puede instalar paquetes y scripts de ciclo de vida con privilegios del sistema, por lo que añadir uno amplía el límite de confianza del software del sistema. Antes de hacerlo:

1. Prefiere el repositorio de la distribución cuando satisfaga la necesidad.
2. Confirma el editor, la versión compatible, la arquitectura y la huella de la clave de firma.
3. Utiliza un archivo de fuente dedicado y un llavero de alcance limitado.
4. Examina los nombres de paquetes y los cambios de dependencias antes de instalar.
5. Documenta cómo desactivar la fuente y migrar o eliminar sus paquetes.

No copies instrucciones obsoletas que desactiven las comprobaciones de firmas ni canalices un script remoto sin auditar hacia un shell con privilegios.

:::single-choice{#package-repositories-third-party-risk}
¿Por qué añadir un repositorio de terceros amplía el límite de confianza del sistema?

::option[Porque sus paquetes y scripts autenticados pueden instalarse con privilegios del sistema.]{#package-repositories-privileged-install .correct explanation="Confiar en la fuente de firma puede autorizar código y acciones del ciclo de vida que afectan al sistema operativo."}
::option[Porque hace que el kernel de Linux deje de aplicar permisos de archivos.]{#package-repositories-disable-permissions explanation="Configurar un repositorio no desactiva los mecanismos normales de control de acceso del kernel."}
::option[Porque convierte todos los paquetes nativos en archivos de código fuente.]{#package-repositories-convert-source explanation="Añadir un repositorio cambia las fuentes de paquetes disponibles, no el formato fundamental de los paquetes existentes."}
:::

Practica la instalación desde repositorios en [Instalación de software en Linux](https://labex.io/labs/linux-software-installation-on-linux-18005) o compara el flujo de trabajo de la familia Red Hat en [Consultar y actualizar paquetes con YUM](https://labex.io/labs/rhel-query-and-update-packages-with-yum-in-linux-590869). Para conocer la sintaxis exacta de APT, consulta el manual local `sources.list(5)`.

## Resumen

Ahora puedes explicar cómo un repositorio configurado se convierte en metadatos de paquetes de confianza.

1. Distingue los índices del repositorio de los archivos de paquetes.
2. Utiliza `apt update` para actualizar el catálogo local.
3. Localiza las definiciones de fuentes de APT tanto de una línea como de estilo deb822.
4. Limita el alcance de las claves de firma y revisa deliberadamente la confianza en terceros.
