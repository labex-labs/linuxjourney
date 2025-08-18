---
index: 4
lang: "es"
title: "NFS"
meta_title: "NFS - Compartir Red"
meta_description: "Aprenda sobre la configuración del cliente NFS y el automontaje en Linux. Comprenda cómo conectarse a recursos compartidos de archivos de red y usar el automontaje para un acceso sin interrupciones."
meta_keywords: "cliente NFS, automount, Network File System, redes Linux, comando mount, tutorial Linux, principiante"
---

## Lesson Content

El recurso compartido de archivos de red más estándar para Linux es NFS (Network File System). NFS permite que un servidor comparta directorios y archivos con uno o más clientes a través de la red.

No entraremos en los detalles de cómo crear un servidor NFS, ya que puede ser complejo; sin embargo, discutiremos la configuración de clientes NFS.

### Setting up NFS client

```bash
sudo service nfsclient start
sudo mount server:/directory /mount_directory
```

### Automounting

Supongamos que usa el servidor NFS con bastante frecuencia y desea mantenerlo montado permanentemente. Normalmente, podría pensar en editar el archivo `/etc/fstab`, pero es posible que no siempre obtenga una conexión al servidor, y eso puede causar problemas al iniciar. En su lugar, lo que desea hacer es configurar el automounting para que pueda conectarse al servidor NFS cuando lo necesite. Esto se hace con la herramienta **automount** o, en versiones recientes de Linux, **amd**. Cuando se accede a un archivo en un directorio especificado, automount buscará el servidor remoto y lo montará automáticamente.

## Exercise

Lea la página man de NFS para obtener más información.

## Quiz Question

¿Qué herramienta se utiliza para gestionar puntos de montaje automáticamente?

## Quiz Answer

automount
