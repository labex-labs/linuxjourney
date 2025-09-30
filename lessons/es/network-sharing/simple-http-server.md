---
index: 3
lang: "es"
title: "Servidor HTTP Simple"
meta_title: "Servidor HTTP Simple - Compartir en Red"
meta_description: "Aprende a crear un servidor HTTP simple usando el módulo http.server de Python. Comparte archivos rápidamente en tu red con este tutorial de Linux para principiantes."
meta_keywords: "http.server, SimpleHTTPServer, servidor web Python, compartir archivos, tutorial Linux, guía para principiantes"
---

## Lesson Content

Python tiene una herramienta súper útil para servir archivos a través de HTTP. Esto es genial si solo quieres crear un recurso compartido de red rápido al que otras máquinas de tu red puedan acceder. Para hacer eso, simplemente ve al directorio que quieres compartir y ejecuta:

```bash
python -m http.server
```

O, si todavía estás en Python 2:

```bash
python -m SimpleHTTPServer
```

Esto configura un servidor web básico al que puedes acceder a través de la dirección localhost. Así que, toma la dirección IP de la máquina donde ejecutaste esto, y luego en otra máquina, accede a ella en el navegador con: `http://IP_ADDRESS:8000`. En tu propia máquina, puedes ver los archivos disponibles escribiendo: `http://localhost:8000` en tu navegador web.

## Exercise

¡La práctica hace al maestro! Aquí tienes algunos laboratorios prácticos para reforzar tu comprensión de la conectividad de red y el direccionamiento IP, que son esenciales para compartir archivos a través de una red:

1. **[Explorar tipos de direcciones IP y accesibilidad en Linux](https://labex.io/es/labs/comptia-explore-ip-address-types-and-reachability-in-linux-592780)** - Practica la identificación de diferentes tipos de direcciones IP y la prueba de la accesibilidad de la red, crucial para asegurar que tu servidor HTTP de Python sea accesible.
2. **[Identificar direcciones MAC e IP en Linux](https://labex.io/es/labs/comptia-identify-mac-and-ip-addresses-in-linux-592731)** - Aprende a usar el comando `ip a` para encontrar la dirección IP de tu máquina, un paso necesario antes de acceder a tus archivos compartidos desde otro dispositivo.
3. **[Gestionar la resolución de nombres de host local en Linux](https://labex.io/es/labs/comptia-manage-local-hostname-resolution-in-linux-592792)** - Aprende a gestionar la resolución de nombres de host local en Linux editando el archivo /etc/hosts, una habilidad clave para el desarrollo web y las pruebas de red.

Estos laboratorios te ayudarán a aplicar los conceptos en escenarios reales y a desarrollar confianza con las operaciones básicas de red en Linux.

## Quiz Question

¿Qué herramienta puedes usar para crear un servidor HTTP simple con Python?

## Quiz Answer

http.server
