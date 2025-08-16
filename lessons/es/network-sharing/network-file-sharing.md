---
lang: "es"
title: "Visión general del uso compartido de archivos"
description: "Aprende sobre el uso compartido de archivos en Linux y el comando secure copy (scp). Transfiere archivos entre hosts en tu red. ¡Empieza con esta guía para principiantes!"
keywords: "compartir archivos Linux, comando scp, copia segura, transferencia de archivos en red, tutorial Linux, Linux para principiantes, guía Linux"
---

## Lesson Content

Normalmente no eres el único ordenador en tu red, especialmente si trabajas en un entorno comercial. Cuando queremos transferir datos de una máquina a otra, a veces puede ser más fácil conectar una unidad USB y copiarlos manualmente. Pero en la mayoría de los casos, si trabajas con máquinas en la misma red, la forma de transferir datos es a través del uso compartido de archivos en red.

En este curso, revisaremos un par de métodos diferentes para copiar datos hacia y desde diferentes máquinas en tu red. Discutiremos algunas copias de archivos simples, luego hablaremos sobre cómo montar directorios completos en tu máquina que actúan como una unidad separada.

Una herramienta sencilla para compartir archivos es el comando **scp**. El comando scp significa secure copy; funciona exactamente igual que el comando cp, pero te permite copiar de un host a otro host en la misma red. Funciona a través de ssh, por lo que todas tus acciones utilizan la misma autenticación y seguridad que ssh.

### Para copiar un archivo de un host local a un host remoto

```bash
scp myfile.txt username@remotehost.com:/remote/directory
```

### Para copiar un archivo de un host remoto a tu host local

```bash
scp username@remotehost.com:/remote/directory/myfile.txt /local/directory
```

### Para copiar un directorio de tu host local a un host remoto

```bash
scp -r mydir username@remotehost.com:/remote/directory
```

## Exercise

Intenta copiar un archivo con scp de una máquina a otra.

## Quiz Question

¿Qué comando puedes usar para copiar archivos de forma segura de un host a otro?

## Quiz Answer

scp
