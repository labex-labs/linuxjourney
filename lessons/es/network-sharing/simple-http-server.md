---
index: 3
lang: "es"
title: "Servidor HTTP Simple"
meta_title: "Servidor HTTP Simple - Compartición de Red"
meta_description: "Aprenda a configurar rápidamente un servidor HTTP simple en Linux usando el módulo http.server de Python. Esta guía explica cómo crear un servidor web Linux sencillo para compartir archivos fácilmente en su red."
meta_keywords: "servidor http simple linux, servidor http simple en linux, servidor web linux simple, python http.server, qué es python simplehttpserver, compartir archivos, servidor de red"
---

## Lesson Content

Python incluye un módulo incorporado que le permite crear instantáneamente un servidor web, lo cual es increíblemente útil para compartir archivos a través de una red. Configurar un **servidor http simple en linux** es un proceso sencillo que requiere solo un comando.

### Iniciando un Servidor HTTP Simple en Linux

Para comenzar, navegue hasta el directorio que desea compartir usando su terminal. Una vez que esté en el directorio deseado, puede iniciar un entorno de **servidor http simple linux** con el siguiente comando si está utilizando Python 3:

```bash
python -m http.server
```

Este comando inicia un servidor web básico, haciendo que el contenido de su directorio actual sea accesible a través de HTTP.

### Método Heredado para Python 2

Para sistemas más antiguos que aún utilizan Python 2, el comando es ligeramente diferente. El módulo se llamaba anteriormente `SimpleHTTPServer`. Si alguna vez se ha preguntado **qué es python simplehttpserver**, es simplemente el equivalente de Python 2 del módulo `http.server`. Puede ejecutarlo con:

```bash
python -m SimpleHTTPServer
```

### Accediendo a su Servidor Web Simple en Linux

Después de ejecutar el comando, su **servidor web simple linux** estará activo. Puede acceder a los archivos compartidos desde otra máquina en la misma red abriendo un navegador web y navegando a `http://DIRECCION_IP:8000`, reemplazando `DIRECCION_IP` con la IP local de la máquina que ejecuta el servidor.

Para ver los archivos en la misma máquina, puede usar la dirección localhost: `http://localhost:8000`.

## Exercise

¡La práctica hace al maestro! Aquí hay algunos laboratorios prácticos para reforzar su comprensión de la conectividad de red y el direccionamiento IP, que son esenciales para compartir archivos a través de una red:

1. **[Explorar Tipos de Direcciones IP y Alcance en Linux](https://labex.io/es/labs/comptia-explore-ip-address-types-and-reachability-in-linux-592780)** - Practique la identificación de diferentes tipos de direcciones IP y la prueba del alcance de la red, crucial para asegurar que su servidor HTTP de Python sea accesible.
2. **[Identificar Direcciones MAC e IP en Linux](https://labex.io/es/labs/comptia-identify-mac-and-ip-addresses-in-linux-592731)** - Aprenda a usar el comando `ip a` para encontrar la dirección IP de su máquina, un paso necesario antes de acceder a sus archivos compartidos desde otro dispositivo.
3. **[Administrar la Resolución de Nombres de Host Locales en Linux](https://labex.io/es/labs/comptia-manage-local-hostname-resolution-in-linux-592792)** - Aprenda a administrar la resolución de nombres de host locales en Linux editando el archivo /etc/hosts, una habilidad clave para el desarrollo web y las pruebas de red.

Estos laboratorios le ayudarán a aplicar los conceptos en escenarios reales y a ganar confianza con las operaciones básicas de red en Linux.

## Quiz Question

Para Python 3, ¿cuál es el nombre del módulo utilizado para crear un servidor HTTP simple? (Por favor, responda en inglés, prestando atención a la sensibilidad a mayúsculas y minúsculas).

## Quiz Answer

http.server
