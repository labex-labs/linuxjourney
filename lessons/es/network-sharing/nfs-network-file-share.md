---
index: 4
lang: "es"
title: "NFS"
meta_title: "NFS - Compartición de Red"
meta_description: "Descubra cómo usar el Sistema de Archivos de Red (NFS) en Linux. Esta lección cubre la configuración de un cliente NFS, el uso del comando mount y la configuración de automount para acceso fluido a recursos compartidos de red."
meta_keywords: "NFS, cliente NFS, automount, Sistema de Archivos de Red, redes Linux, comando mount, tutorial Linux, principiante"
---

## Lesson Content

El protocolo más estándar para compartir archivos en red en Linux es NFS, que significa **Network File System** (Sistema de Archivos de Red). NFS permite que un servidor comparta sus directorios y archivos con una o más máquinas cliente a través de una red, haciendo que parezcan recursos locales.

Esta lección se centrará en la configuración de un **cliente NFS**, ya que configurar un servidor NFS puede ser un proceso más complejo.

### Montaje de una Carpeta Compartida NFS

Para conectarse a una carpeta compartida NFS, primero debe asegurarse de que el servicio cliente NFS se esté ejecutando. Luego, puede usar el comando `mount` para adjuntar el directorio remoto a un punto de montaje local en su sistema.

```bash
sudo service nfsclient start
sudo mount servidor:/directorio /directorio_montaje
```

En este ejemplo, `servidor:/directorio` es la carpeta compartida remota a la que desea acceder, y `/directorio_montaje` es el directorio local donde se montará la carpeta compartida.

### Uso de Automount para NFS

Si accede frecuentemente a una carpeta compartida NFS, podría considerar hacer el montaje permanente. Si bien agregar una entrada al archivo `/etc/fstab` es un método común para unidades locales, puede causar retrasos significativos en el arranque o incluso fallos si la conexión de red o el servidor NFS no están disponibles durante el inicio.

Una mejor solución para las carpetas compartidas de red es **automount**. Este servicio, administrado por la herramienta `automount` o su implementación moderna `amd`, monta dinámicamente un sistema de archivos bajo demanda. Cuando se accede a un archivo o directorio dentro de una ruta especificada, automount se conecta automáticamente al servidor remoto y monta la carpeta compartida. Esto asegura un acceso fluido cuando es necesario sin afectar el proceso de arranque del sistema.

## Exercise

Aunque no hay laboratorios específicos para este tema, recomendamos explorar la [Ruta de Aprendizaje de Linux](https://labex.io/es/learn/linux) completa para practicar las habilidades y conceptos relacionados con Linux.

## Quiz Question

What tool is used to manage mount points automatically? Please answer in English, and note that the answer is case-sensitive.

## Quiz Answer

automount
