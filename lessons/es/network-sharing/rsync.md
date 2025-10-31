---
index: 2
lang: "es"
title: "rsync"
meta_title: "rsync - Compartición de Red"
meta_description: "Descubra cómo usar el potente comando rsync en Linux para sincronización eficiente de archivos, transferencia remota de datos y copias de seguridad fiables. Esta guía cubre comandos y opciones clave de rsync."
meta_keywords: "rsync, rsync linux, sincronización de archivos, copia de seguridad de datos, sincronización remota, comando rsync, transferencia de archivos linux, tutorial rsync"
---

## Lesson Content

### ¿Qué es rsync?

Otra herramienta esencial para copiar datos entre diferentes hosts es `rsync`, que significa sincronización remota (remote synchronization). Aunque es similar a `scp`, `rsync` tiene una diferencia clave que lo hace increíblemente eficiente. Utiliza un algoritmo de transferencia delta que comprueba de manera inteligente el destino para ver los datos existentes y solo transfiere las partes de los archivos que han cambiado.

Por ejemplo, si se interrumpe una transferencia de archivos grande, `rsync` puede reanudar la copia, transfiriendo solo las partes restantes del archivo en lugar de empezar de nuevo desde cero. Esto lo convierte en una opción robusta para conexiones de red inestables.

### Características clave de rsync

La eficiencia de `rsync` proviene de sus optimizaciones inteligentes. Verifica la integridad de los archivos mediante sumas de comprobación (checksums) para asegurar que los datos copiados no se corrompan durante la transferencia. Estas características proporcionan una flexibilidad significativa, haciendo de `rsync` una herramienta ideal para:

- Sincronización de directorios (tanto remota como local)
- Creación de copias de seguridad incrementales de datos
- Manejo eficiente de transferencias de datos grandes

### Opciones comunes de rsync

Puedes modificar el comportamiento del comando `rsync` con varias opciones. Algunas de las más utilizadas incluyen:

- `-v`: Salida detallada (verbose), que muestra qué archivos se están transfiriendo.
- `-r`: Recursivo, necesario para copiar directorios completos.
- `-h`: Salida legible para humanos (human-readable), que muestra los números en un formato más comprensible (ej. KB, MB).
- `-z`: Comprime los datos del archivo durante la transferencia, lo cual es excelente para conexiones lentas.
- `-a`: Modo archivo (archive), un atajo conveniente que combina varias opciones (`-rlptgoD`) para preservar permisos, propiedad y marcas de tiempo.

### Ejemplos de uso de rsync

#### Sincronizar archivos en el mismo host

Puedes usar `rsync` para sincronizar dos directorios en tu máquina local. Esto es útil para crear copias de seguridad locales.

```bash
rsync -avh /my/local/directory/one/ /my/local/directory/two/
```

#### Sincronizar archivos de un host remoto a un host local

Para obtener archivos de un servidor remoto a tu máquina local, especifica primero el origen remoto.

```bash
rsync -avh username@remotehost.com:/remote/directory/ /local/directory/
```

#### Sincronizar archivos de un host local a un host remoto

Para enviar archivos desde tu máquina local a un servidor remoto, especifica primero el origen local.

```bash
rsync -avh /local/directory/ username@remotehost.com:/remote/directory/
```

## Exercise

Aunque no hay laboratorios específicos para este tema, recomendamos explorar la [Ruta de Aprendizaje de Linux](https://labex.io/es/learn/linux) completa para practicar habilidades y conceptos relacionados con Linux.

## Quiz Question

What command, known for its delta-transfer algorithm, is particularly useful for creating efficient data backups? Please answer in English, paying attention to case sensitivity.

## Quiz Answer

rsync
