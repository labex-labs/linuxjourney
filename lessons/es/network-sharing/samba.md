---
index: 5
lang: "es"
title: "Samba"
meta_title: "Samba - Compartir en red"
meta_description: "Aprende a configurar recursos compartidos de archivos Samba en Linux para Windows y macOS. Esta guía para principiantes cubre la instalación, configuración y acceso a recursos compartidos. ¡Empieza ya!"
meta_keywords: "Samba, compartir archivos Linux, smb.conf, CIFS, smbclient, tutorial Linux, guía para principiantes"
---

## Lesson Content

En los primeros días de la informática, se hizo necesario que las máquinas Windows compartieran archivos con las máquinas Linux; así nació el protocolo Server Message Block (SMB). SMB se utilizaba para compartir archivos entre sistemas operativos Windows (macOS también tiene uso compartido de archivos con SMB) y posteriormente se limpió y optimizó en forma del protocolo Common Internet File System (CIFS).

Samba es lo que llamamos las utilidades de Linux para trabajar con CIFS en Linux. Además de compartir archivos, también puedes compartir recursos como impresoras.

### Crear un recurso compartido de red con Samba

Repasemos los pasos básicos para crear un recurso compartido de red al que una máquina Windows pueda acceder:

### Instalar Samba

```bash
sudo apt update
sudo apt install samba
```

### Configurar smb.conf

El archivo de configuración para Samba se encuentra en `/etc/samba/smb.conf`. Este archivo debe indicar al sistema qué directorios deben compartirse, sus permisos de acceso y más opciones. El `smb.conf` predeterminado ya viene con mucho código comentado, y puedes usarlo como ejemplo para escribir tus propias configuraciones.

```bash
sudo vi /etc/samba/smb.conf
```

### Establecer una contraseña para Samba

```bash
sudo smbpasswd -a [username]
```

### Crear un directorio compartido

```bash
mkdir /my/directory/to/share
```

### Reiniciar el servicio Samba

```bash
sudo service smbd restart
```

### Acceder a un recurso compartido de Samba a través de Windows

En Windows, simplemente escribe la conexión de red en el símbolo del sistema Ejecutar: `\\HOST\sharename`.

### Acceder a un recurso compartido de Samba/Windows a través de Linux

```bash
smbclient //HOST/directory -U user
```

El paquete Samba incluye una herramienta de línea de comandos llamada **smbclient** que puedes usar para acceder a cualquier servidor Windows o Samba. Una vez que estés conectado al recurso compartido, puedes navegar y transferir archivos.

### Adjuntar un recurso compartido de Samba a tu sistema

En lugar de transferir archivos uno por uno, puedes simplemente montar el recurso compartido de red en tu sistema.

```bash
sudo mount -t cifs servername:directory mountpoint -o user=username,pass=password
```

## Exercise

Aunque no hay laboratorios específicos para este tema, recomendamos explorar la completa [Ruta de aprendizaje de Linux](https://labex.io/es/learn/linux) para practicar habilidades y conceptos relacionados con Linux.

## Quiz Question

¿Cuál es el último protocolo utilizado para la transferencia de archivos entre Windows y Linux?

## Quiz Answer

CIFS
