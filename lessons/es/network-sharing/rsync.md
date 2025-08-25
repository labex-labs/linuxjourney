---
index: 2
lang: "es"
title: "rsync"
meta_title: "rsync - Compartir en red"
meta_description: "Aprenda rsync para una sincronización y copias de seguridad eficientes de archivos en Linux. Comprenda la transferencia de datos remota y local con comandos y opciones de rsync. ¡Mejore sus habilidades en Linux!"
meta_keywords: "rsync, transferencia de archivos Linux, copia de seguridad de datos, sincronización de archivos, tutorial de Linux, comandos rsync, principiante, guía"
---

## Lesson Content

Otra herramienta utilizada para copiar datos de diferentes hosts es rsync (abreviatura de sincronización remota). Rsync es muy similar a scp, pero tiene una diferencia importante. Rsync utiliza un algoritmo especial que verifica de antemano si ya hay datos que está copiando y solo copiará las diferencias. Por ejemplo, digamos que estaba copiando un archivo y su red se interrumpió; por lo tanto, su copia se detuvo a mitad de camino. En lugar de volver a copiar todo desde el principio, rsync solo copiará las partes que no se copiaron.

También verifica la integridad de un archivo que está copiando con sumas de verificación. Estas pequeñas optimizaciones permiten una mayor flexibilidad en la transferencia de archivos y hacen que rsync sea ideal para la sincronización de directorios de forma remota y local, copias de seguridad de datos, grandes transferencias de datos y más.

Algunas opciones de rsync de uso común:

- v - salida detallada
- r - recursivo en directorios
- h - salida legible para humanos
- z - comprimido para una transferencia más fácil, ideal para conexiones lentas

### Copiar/sincronizar archivos en el mismo host

```bash
rsync -zvr /my/local/directory/one /my/local/directory/two
```

### Copiar/sincronizar archivos en el host local desde un host remoto

```bash
rsync /local/directory username@remotehost.com:/remote/directory
```

### Copiar/sincronizar archivos en un host remoto desde un host local

```bash
rsync username@remotehost.com:/remote/directory /local/directory
```

## Exercise

Aunque no hay laboratorios específicos para este tema, recomendamos explorar la completa [Ruta de aprendizaje de Linux](https://labex.io/es/learn/linux) para practicar habilidades y conceptos relacionados con Linux.

## Quiz Question

¿Qué comando sería útil para las copias de seguridad de datos?

## Quiz Answer

rsync
