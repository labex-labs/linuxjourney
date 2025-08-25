---
index: 4
lang: "es"
title: "NFS"
meta_title: "NFS - Compartir en red"
meta_description: "Aprenda sobre la configuración del cliente NFS y el montaje automático en Linux. Comprenda cómo conectarse a recursos compartidos de archivos de red y usar el montaje automático para un acceso sin interrupciones."
meta_keywords: "cliente NFS, automount, Network File System, redes Linux, comando mount, tutorial Linux, principiante"
---

## Lesson Content

El recurso compartido de archivos de red más estándar para Linux es NFS (Network File System). NFS permite que un servidor comparta directorios y archivos con uno o más clientes a través de la red.

No entraremos en los detalles de cómo crear un servidor NFS, ya que puede ser complejo; sin embargo, discutiremos la configuración de clientes NFS.

### Configuración del cliente NFS

```bash
sudo service nfsclient start
sudo mount server:/directory /mount_directory
```

### Montaje automático

Supongamos que usa el servidor NFS con bastante frecuencia y desea mantenerlo montado permanentemente. Normalmente, podría pensar en editar el archivo `/etc/fstab`, pero es posible que no siempre obtenga una conexión al servidor, y eso puede causar problemas al iniciar. En su lugar, lo que desea hacer es configurar el montaje automático para que pueda conectarse al servidor NFS cuando lo necesite. Esto se hace con la herramienta **automount** o, en versiones recientes de Linux, **amd**. Cuando se accede a un archivo en un directorio especificado, automount buscará el servidor remoto y lo montará automáticamente.

## Exercise

Si bien no hay laboratorios específicos para este tema, recomendamos explorar la completa [Ruta de aprendizaje de Linux](https://labex.io/es/learn/linux) para practicar habilidades y conceptos relacionados con Linux.

## Quiz Question

¿Qué herramienta se utiliza para gestionar los puntos de montaje automáticamente?

## Quiz Answer

automount
