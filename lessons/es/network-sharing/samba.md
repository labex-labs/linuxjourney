---
index: 5
lang: "es"
title: "Samba"
meta_title: "Samba - Compartición de Red"
meta_description: "Aprenda a configurar un recurso compartido de red Samba en Linux. Esta guía cubre el protocolo Samba, instalación, configuración y uso de clientes smb linux para conectarse a los recursos."
meta_keywords: "Samba, smb linux, linux smb, red samba, protocolo samba, smb samba, compartir archivos, smb.conf, cifs, smbclient, tutorial linux"
---

## Lesson Content

Durante décadas, un desafío principal en entornos con sistemas operativos mixtos ha sido compartir archivos entre máquinas Windows y Linux. La solución que surgió es el protocolo Server Message Block (SMB). Originalmente desarrollado para Windows, el **protocolo samba** fue refinado posteriormente en un dialecto conocido como Common Internet File System (CIFS). Hoy en día, los sistemas modernos utilizan versiones más nuevas de SMB, pero los términos a menudo se usan juntos.

Samba es el potente conjunto de software que implementa el protocolo **SMB/CIFS** en Linux y otros sistemas tipo Unix. Es la clave para la integración **smb linux**, permitiendo que un servidor Linux actúe como servidor de archivos e impresión para clientes Windows, macOS y otros clientes Linux, creando una **red samba** fluida. La relación entre **smb samba** es sencilla: Samba es el software que habla el lenguaje SMB.

### Instalación de Samba en Linux

Para comenzar, necesita instalar el paquete Samba. El comando varía dependiendo del gestor de paquetes de su distribución Linux. Para sistemas basados en Debian como Ubuntu, use lo siguiente:

```bash
sudo apt update
sudo apt install samba
```

### Configuración de un Recurso Compartido de Samba

El archivo de configuración principal para Samba se encuentra en `/etc/samba/smb.conf`. Este archivo dicta qué directorios se comparten, quién puede acceder a ellos y sus permisos. El archivo predeterminado contiene muchos ejemplos comentados que sirven como una excelente referencia.

Recorramos los pasos para configurar un recurso compartido básico.

Primero, abra el archivo de configuración en un editor de texto:

```bash
sudo nano /etc/samba/smb.conf
```

Al final del archivo, agregue una nueva sección para su recurso compartido. El nombre entre corchetes será el nombre del recurso compartido visible en la red.

```ini
[myshare]
    comment = Mi Primer Recurso Compartido de Samba
    path = /my/directory/to/share
    read only = no
    browsable = yes
```

Luego, cree el directorio que especificó en la configuración:

```bash
mkdir -p /my/directory/to/share
```

Finalmente, necesita configurar una contraseña específica para el acceso a Samba. Samba mantiene su propia base de datos de contraseñas, que es independiente de las contraseñas de usuario del sistema.

```bash
sudo smbpasswd -a [username]
```

Reemplace `[username]` con un usuario de Linux existente en su sistema. Se le pedirá que cree una nueva contraseña para ese usuario para el acceso a Samba.

### Gestión del Servicio Samba

Después de realizar cambios en el archivo `smb.conf`, debe reiniciar el servicio Samba para que surtan efecto.

```bash
sudo service smbd restart
```

### Acceso a Recursos Compartidos de Samba

Una vez que su recurso compartido esté configurado, los clientes en la red pueden acceder a él.

**Desde Windows:**
Abra el cuadro de diálogo Ejecutar (Win + R) o el Explorador de archivos y escriba la ruta de red: `\\HOST\sharename`, donde `HOST` es la dirección IP o el nombre de host de su máquina Linux.

**Desde Linux:**
El paquete Samba incluye una herramienta de línea de comandos llamada **smbclient** que le permite interactuar con cualquier recurso compartido **linux smb** o de Windows.

```bash
smbclient //HOST/myshare -U username
```

Después de conectarse, obtendrá un indicador `smb: \>` donde puede usar comandos como `ls`, `get` y `put` para administrar archivos.

### Montaje de un Recurso Compartido de Samba

Para un acceso más permanente, puede montar el recurso compartido de red directamente en su sistema de archivos, haciendo que parezca un directorio local.

```bash
sudo mount -t cifs //SERVER/sharename /mnt/mountpoint -o user=username,pass=password
```

Este comando utiliza el tipo de sistema de archivos `cifs` para adjuntar el recurso compartido remoto a un punto de montaje local.

## Exercise

Intente configurar un recurso compartido simple de Samba en su propia máquina Linux. Cree un directorio, configúrelo en `smb.conf` e intente acceder a él usando `smbclient` desde la misma máquina para probar la configuración. Para una práctica más práctica, explore la [Ruta de Aprendizaje de Linux](https://labex.io/es/learn/linux) completa para practicar habilidades y conceptos relacionados con Linux.

## Quiz Question

¿Cuál es el nombre del protocolo, un dialecto temprano de SMB, que se desarrolló para compartir archivos? Por favor, responda en inglés, prestando atención a las mayúsculas.

## Quiz Answer

CIFS
