---
lesson_id: "compressed-archives-tar"
course_id: "packages"
lang: "es"
order_index: 3
title: "tar y gzip"
description: "Aprende a archivar archivos con `tar`, comprimir flujos con `gzip` y examinar archivos antes de extraerlos de forma segura."
meta_title: "tar y gzip - Paquetes"
meta_description: "Aprende a usar tar y gzip en Linux para crear, comprimir, examinar y extraer archivos de forma segura."
meta_keywords: "tar y gzip, compresión tar, archivo tar.gz, archivado Linux, compresión de archivos, orden tar, orden gzip"
---

El archivado y la compresión resuelven problemas distintos. Un archivo combina un árbol de directorios y sus metadatos en un solo flujo. La compresión codifica un flujo para reducir su tamaño. Por convención, un archivo `.tar.gz` es un archivo tar cuyo flujo se ha comprimido con gzip.

## Comprimir un flujo con `gzip`

De forma predeterminada, `gzip` comprime un archivo y sustituye el nombre original por un archivo `.gz`:

```bash
$ gzip report.txt
```

Normalmente, esto elimina `report.txt` después de crear correctamente `report.txt.gz`. Descomprímelo con:

```bash
$ gunzip report.txt.gz
```

Utiliza `gzip -k report.txt`, cuando sea compatible, para conservar el archivo de entrada, o utiliza los flujos estándar cuando necesites un control explícito. Una extensión de archivo es una convención, no una prueba del formato real; herramientas como `file` pueden examinar el contenido.

:::single-choice{#tar-gzip-gzip-role}
¿Cuál es la función principal de `gzip` en esta lección?

::option[Combinar un árbol de directorios en un archivo junto con los metadatos de sus archivos.]{#tar-gzip-directory-archive explanation="Tar realiza esa función de archivado antes de aplicar la compresión con gzip."}
::option[Comprimir un único flujo de entrada.]{#tar-gzip-compress-stream .correct explanation="Gzip transforma un flujo de bytes y no codifica por sí solo una jerarquía de directorios."}
::option[Instalar metadatos de dependencias en una base de datos de paquetes.]{#tar-gzip-package-install explanation="La compresión es independiente de la instalación de paquetes nativos y del seguimiento de dependencias."}
:::

## Crear un archivo tar

Crea un archivo sin comprimir con:

```bash
$ tar -cvf project.tar file1 file2 directory1
```

- `-c` crea un archivo nuevo.
- `-v` muestra los miembros mientras los procesa y es opcional.
- `-f project.tar` indica el nombre del archivo; como `-f` consume un argumento, mantén el nombre junto a esa opción.

Las rutas se guardan como nombres de miembros del archivo. Crea los archivos desde un directorio de trabajo elegido deliberadamente y evita incluir sin querer secretos, cachés, sockets o rutas absolutas demasiado amplias.

:::single-choice{#tar-gzip-create-option}
¿Qué opción de `tar` crea un archivo nuevo?

::option[`-x`]{#tar-gzip-option-extract explanation="La operación `-x` extrae miembros de un archivo."}
::option[`-c`]{#tar-gzip-option-create .correct explanation="La operación de creación escribe un archivo nuevo a partir de las entradas indicadas."}
::option[`-t`]{#tar-gzip-option-list explanation="La operación `-t` muestra los miembros del archivo sin extraerlos."}
:::

## Crear un archivo tar comprimido con gzip

GNU tar y muchas otras implementaciones pueden invocar gzip mediante `-z`:

```bash
$ tar -czvf project.tar.gz file1 file2 directory1
```

El resultado es un único flujo tar comprimido con gzip. La compresión no cifra el archivo ni oculta su contenido a quien pueda leerlo y descomprimirlo. Si necesitas confidencialidad, utiliza un flujo de trabajo apropiado de cifrado autenticado y gestiona las claves por separado.

:::single-choice{#tar-gzip-z-option}
¿Qué solicita `-z` en la orden `tar` mostrada?

::option[Cifrar el archivo mediante una clave de conocimiento cero.]{#tar-gzip-z-encrypt explanation="Ni tar ni gzip proporcionan cifrado mediante esta opción."}
::option[Descartar todos los miembros de longitud cero.]{#tar-gzip-z-zero explanation="La opción selecciona gzip y no filtra los miembros del archivo por tamaño."}
::option[Procesar el flujo del archivo mediante gzip.]{#tar-gzip-z-gzip .correct explanation="La opción `z` conecta la operación de archivado de tar con la compresión o descompresión de gzip."}
:::

## Mostrar el contenido antes de extraerlo

Trata un archivo recibido de terceros como una entrada que no es de confianza. Muestra primero los nombres de sus miembros:

```bash
$ tar -tzf download.tar.gz
```

Busca rutas absolutas inesperadas, componentes de recorrido `..`, enlaces simbólicos o duros sospechosos, archivos de dispositivo y nombres que sobrescribirían archivos importantes. Las implementaciones modernas de tar aplican protecciones, pero el comportamiento y las opciones varían, y la extracción sigue creando nombres y contenidos elegidos por un posible atacante.

Extrae el contenido en un directorio de preparación nuevo y sin privilegios:

```bash
$ mkdir extraction-stage
$ tar -xzf download.tar.gz -C extraction-stage
```

No extraigas como root un archivo que no hayas revisado. Comprueba lo que se creó antes de mover los archivos seleccionados a sus ubicaciones finales.

:::single-choice{#tar-gzip-list-before-extract}
¿Qué operación muestra los miembros de un archivo sin extraerlos?

::option[`tar -czf download.tar.gz .`]{#tar-gzip-create-download explanation="Esta orden crea o sustituye un archivo a partir del directorio actual."}
::option[`tar -xzf download.tar.gz`]{#tar-gzip-extract-download explanation="La operación `-x` escribe los miembros en el directorio de destino."}
::option[`tar -tzf download.tar.gz`]{#tar-gzip-list-members .correct explanation="La operación `-t` lee y muestra la tabla de miembros, mientras que `-z` se ocupa de gzip."}
:::

## Otros formatos de compresión

Las implementaciones de tar pueden trabajar con compresores como bzip2 y xz, que en GNU tar suelen seleccionarse mediante `-j` y `-J`, respectivamente. La compatibilidad con formatos y su detección automática varían, así que consulta `tar --help` o el manual local. ZIP es un formato de archivo distinto que se maneja con herramientas como `zip` y `unzip`.

:::single-choice{#tar-gzip-archive-confidentiality}
¿La compresión gzip convierte un archivo tar en confidencial?

::option[No; cualquiera que pueda leerlo puede normalmente descomprimirlo.]{#tar-gzip-not-encryption .correct explanation="La compresión cambia la representación y el tamaño, pero no proporciona control de acceso ni secreto criptográfico."}
::option[Sí; gzip deriva una clave de cifrado del nombre del archivo.]{#tar-gzip-filename-key explanation="Gzip no implementa ese mecanismo de cifrado."}
::option[Sí; tar cifra cada miembro antes de que gzip lo reciba.]{#tar-gzip-tar-encrypt explanation="Tar archiva miembros, pero no cifra automáticamente su contenido."}
:::

Practica con archivos desechables en [Empaquetado y compresión de archivos](https://labex.io/labs/linux-file-packaging-and-compression-385413) y después aplica la inspección y la preparación en [Crear y restaurar una copia de seguridad con tar](https://labex.io/labs/comptia-create-and-restore-a-backup-with-tar-in-linux-590843).

## Resumen

Ahora puedes combinar de forma segura el archivado con tar y la compresión con gzip.

1. Distingue un archivo tar de la compresión gzip.
2. Crea archivos con `-c` y flujos gzip con `-z`.
3. Muestra los miembros con `-t` antes de extraerlos con `-x`.
4. Extrae contenido que no sea de confianza en un directorio de preparación sin privilegios.
5. Trata la compresión como algo independiente del cifrado.
