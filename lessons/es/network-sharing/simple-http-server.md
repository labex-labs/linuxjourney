---
lang: "es"
title: "Servidor HTTP Simple"
meta_description: "Aprende a crear un servidor HTTP simple usando el módulo http.server de Python. Comparte archivos rápidamente en tu red con este tutorial de Linux apto para principiantes."
meta_keywords: "http.server, SimpleHTTPServer, servidor web Python, compartir archivos, tutorial Linux, guía para principiantes"
---

## Lesson Content

Python tiene una herramienta muy útil para servir archivos a través de HTTP. Esto es genial si solo quieres crear un recurso compartido de red rápido al que otras máquinas de tu red puedan acceder. Para hacer eso, simplemente ve al directorio que quieres compartir y ejecuta:

```bash
python -m http.server
```

O, si todavía estás en Python 2:

```bash
python -m SimpleHTTPServer
```

Esto configura un servidor web básico al que puedes acceder a través de la dirección localhost. Así que, toma la dirección IP de la máquina en la que ejecutaste esto, y luego en otra máquina, accede a ella en el navegador con: `http://IP_ADDRESS:8000`. En tu propia máquina, puedes ver los archivos disponibles escribiendo: `http://localhost:8000` en tu navegador web.

## Exercise

¡Intenta configurar un `http.server`!

## Quiz Question

¿Qué herramienta puedes usar para crear un servidor HTTP simple con Python?

## Quiz Answer

http.server
