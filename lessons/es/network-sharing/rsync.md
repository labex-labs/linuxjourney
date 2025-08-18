---
lang: "es"
title: "rsync"
meta_description: "Aprenda rsync para una sincronización y copias de seguridad eficientes de archivos en Linux. Comprenda la transferencia de datos remota y local con comandos y opciones de rsync. ¡Mejore sus habilidades en Linux!"
meta_keywords: "rsync, transferencia de archivos Linux, copia de seguridad de datos, sincronización de archivos, tutorial de Linux, comandos rsync, principiante, guía"
---

## Lesson Content

Otra herramienta utilizada para copiar datos de diferentes hosts es rsync (abreviatura de sincronización remota). Rsync es muy similar a scp, pero tiene una diferencia importante. Rsync utiliza un algoritmo especial que verifica de antemano si ya hay datos a los que está copiando y solo copiará las diferencias. Por ejemplo, digamos que estaba copiando un archivo y su red se interrumpió; por lo tanto, su copia se detuvo a mitad de camino. En lugar de volver a copiar todo desde el principio, rsync solo copiará las partes que no se copiaron.

También verifica la integridad de un archivo que está copiando con checksums. Estas pequeñas optimizaciones permiten una mayor flexibilidad en la transferencia de archivos y hacen que rsync sea ideal para la sincronización de directorios de forma remota y local, copias de seguridad de datos, grandes transferencias de datos y más.

Algunas opciones de rsync de uso común:

- v - verbose output
- r - recursive into directories
- h - human-readable output
- z - compressed for easier transfer, great for slow connections

### Copy/sync files on the same host

```bash
rsync -zvr /my/local/directory/one /my/local/directory/two
```

### Copy/sync files to local host from a remote host

```bash
rsync /local/directory username@remotehost.com:/remote/directory
```

### Copy/sync files to a remote host from a local host

```bash
rsync username@remotehost.com:/remote/directory /local/directory
```

## Exercise

Use rsync para sincronizar un directorio con otro directorio. ¡Asegúrese de no sobrescribir un directorio importante!

## Quiz Question

¿Qué comando sería útil para las copias de seguridad de datos?

## Quiz Answer

rsync
