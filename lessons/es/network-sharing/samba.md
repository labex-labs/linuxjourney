---
lang: "es"
title: "Samba"
description: "Aprende a configurar recursos compartidos de archivos Samba en Linux para Windows y macOS. Esta guía para principiantes cubre la instalación, configuración y acceso a los recursos compartidos. ¡Empieza ya!"
keywords: "Samba, compartir archivos Linux, smb.conf, CIFS, smbclient, tutorial Linux, guía para principiantes"
---

## Lesson Content

En los primeros días de la informática, se hizo necesario que las máquinas Windows compartieran archivos con las máquinas Linux; así nació el protocolo Server Message Block (SMB). SMB se utilizaba para compartir archivos entre sistemas operativos Windows (macOS también tiene uso compartido de archivos con SMB) y más tarde se depuró y optimizó en forma del protocolo Common Internet File System (CIFS).

Samba es lo que llamamos las utilidades de Linux para trabajar con CIFS en Linux. Además de compartir archivos, también puedes compartir recursos como impresoras.

### Crear un recurso compartido de red con Samba

Repasemos los pasos básicos para crear un recurso compartido de red al que pueda acceder una máquina Windows:

### Install Samba

```bash
sudo apt update
sudo apt install samba
```

### Setup smb.conf

El archivo de configuración para Samba se encuentra en `/etc/samba/smb.conf`. Este archivo debe indicar al sistema qué directorios deben compartirse, sus permisos de acceso y más opciones. El `smb.conf` predeterminado ya viene con mucho código comentado, y puedes usarlo como ejemplo para escribir tus propias configuraciones.

```bash
sudo vi /etc/samba/smb.conf
```

### Set up a password for Samba

```bash
sudo smbpasswd -a [username]
```

### Create a shared directory

```bash
mkdir /my/directory/to/share
```

### Restart the Samba service

```bash
sudo service smbd restart
```

### Accessing a Samba share via Windows

En Windows, simplemente escribe la conexión de red en el cuadro de diálogo Ejecutar: `\\HOST\sharename`.

### Accessing a Samba/Windows share via Linux

```bash
smbclient //HOST/directory -U user
```

El paquete Samba incluye una herramienta de línea de comandos llamada **smbclient** que puedes usar para acceder a cualquier servidor Windows o Samba. Una vez que estés conectado al recurso compartido, puedes navegar y transferir archivos.

### Attach a Samba share to your system

En lugar de transferir archivos uno por uno, puedes simplemente montar el recurso compartido de red en tu sistema.

```bash
sudo mount -t cifs servername:directory mountpoint -o user=username,pass=password
```

## Exercise

Configura un recurso compartido de Samba. Si no tienes uno, abre `smb.conf` y familiarízate con las opciones del archivo de configuración.

## Quiz Question

¿Cuál es el protocolo más reciente utilizado para la transferencia de archivos entre Windows y Linux?

## Quiz Answer

CIFS
