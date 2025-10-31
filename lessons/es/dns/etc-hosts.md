---
index: 4
lang: "es"
title: "/etc/hosts"
meta_title: "/etc/hosts - DNS"
meta_description: "Explora el propósito del archivo /etc/hosts en Linux. Aprende cómo este archivo mapea nombres de host a direcciones IP, su papel en la resolución DNS local y cómo configurarlo en sistemas como Debian. Una guía sobre la configuración de etc hosts linux."
meta_keywords: "/etc/hosts, etc hosts linux, debian hosts, etc host linux, etc hosts, redes Linux, mapeo de nombres de host, resolución DNS"
---

## Lesson Content

Antes de que su sistema Linux consulte a un servidor DNS para resolver un nombre de host, primero busca una correspondencia en la máquina local. Esta comprobación inicial es una parte fundamental del proceso de resolución de nombres.

### El papel de /etc/hosts

El archivo principal para esta búsqueda local es `/etc/hosts`. Este simple archivo de texto contiene mapeos estáticos de nombres de host a direcciones IP. La estructura del archivo `etc hosts` es sencilla, con cada línea conteniendo tres campos: la dirección IP, el nombre de host canónico y alias opcionales para ese host.

Aquí hay un ejemplo típico de un archivo `etc host linux`:

```plaintext
pete@icebox:~$ cat /etc/hosts
127.0.0.1       localhost
127.0.1.1       icebox
```

Casi siempre encontrará la dirección `localhost` mapeada por defecto. Este archivo es una característica estándar en la mayoría de las distribuciones de Linux, incluidas las `Debian hosts`.

### Edición del archivo etc hosts linux

Puede editar manualmente el archivo `/etc/hosts` para crear sus propios mapeos. Intentemos un ejemplo divertido. Agregue la siguiente línea a su archivo:

```plaintext
123.45.6.7  www.google.com
```

Después de guardar el archivo, intente navegar a `www.google.com` en su navegador web. Descubrirá que no funciona. Esto se debe a que mapeamos `www.google.com` a una dirección IP incorrecta. Como su sistema comprueba primero el archivo local `/etc/hosts`, utiliza nuestro mapeo defectuoso y nunca procede a consultar un servidor DNS para encontrar la dirección correcta. Para solucionar esto, simplemente elimine la línea que agregó.

Aunque los sistemas más antiguos utilizaban `/etc/hosts.deny` y `/etc/hosts.allow` para el control de acceso, este método está en gran parte obsoleto. Las prácticas de seguridad modernas se basan en configurar reglas de firewall para una protección robusta en su lugar.

### Configuración del servidor DNS local

Tradicionalmente, el archivo `/etc/resolv.conf` se utilizaba para especificar los servidores de nombres DNS para las búsquedas. Sin embargo, con los avances en la administración del sistema, este archivo a menudo ya no se gestiona manualmente. Como puede ver en el siguiente ejemplo, el archivo se genera automáticamente mediante otro servicio. Para administrar los mapeos de servidores de nombres DNS, debe consultar la documentación de su distribución específica, ya que herramientas como `systemd-resolved` o `resolvconf` a menudo se encargan de esto ahora.

```plaintext
# Archivo resolv.conf(5) dinámico para el resolvedor glibc(3) generado por resolvconf(8)
#     NO EDITE ESTE ARCHIVO A MANO -- SUS CAMBIOS SERÁN SOBRESCRITOS
nameserver 127.0.1.1
search localdomain
```

## Exercise

¡La práctica hace al maestro! Aquí hay algunos laboratorios prácticos para reforzar su comprensión de la resolución de nombres de host local y las consultas DNS:

1. **[Administrar la resolución de nombres de host local en Linux](https://labex.io/es/labs/comptia-manage-local-hostname-resolution-in-linux-592792)** - Practique la edición del archivo `/etc/hosts` para administrar la resolución de nombres de host local, un paso clave antes de las consultas DNS.
2. **[Consultar registros DNS en Linux con dig y nslookup](https://labex.io/es/labs/comptia-query-dns-records-in-linux-with-dig-and-nslookup-592796)** - Aprenda a consultar registros DNS utilizando herramientas esenciales de Linux como `dig` y `nslookup` para comprender cómo su máquina resuelve nombres externos.

Estos laboratorios le ayudarán a aplicar los conceptos en escenarios reales y a ganar confianza con la resolución de nombres de host y DNS.

## Quiz Question

¿Qué archivo se utiliza para mapear nombres de host a direcciones IP en nuestras máquinas? (Responda en inglés, prestando atención a la sensibilidad a mayúsculas y minúsculas).

## Quiz Answer

/etc/hosts
