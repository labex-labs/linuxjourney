---
index: 19
lang: "es"
title: "exit"
meta_title: "exit - Línea de Comandos"
meta_description: "Aprende el comando exit en Linux, cómo cerrar una sesión de shell, cómo difiere logout de exit y cómo funcionan los valores de estado de salida."
meta_keywords: "comando exit, linux exit, comando logout, sesión de shell, salida de terminal, estado de salida, bash exit"
---

## Lesson Content

¡Felicidades por completar las lecciones fundamentales de tu viaje en Linux! Has cubierto los conceptos básicos esenciales de Linux, y ahora es momento de aprender cómo terminar tu sesión correctamente. Salir del shell de Linux es un paso final simple pero importante.

### El Comando Exit

La forma más común de terminar una sesión de shell es con el comando `exit`. Cuando escribes `exit` y presionas Enter, el proceso actual del shell termina. Este comando funciona en prácticamente cualquier entorno de shell.

```bash
$ exit
```

Si abriste una ventana de terminal, `exit` usualmente cierra el shell que se está ejecutando dentro de ella. Si te conectaste mediante SSH, `exit` termina la sesión remota del shell y te regresa al prompt local.

### Valores de Estado de Salida

El comando `exit` también puede devolver un código de estado. Un estado de `0` usualmente significa éxito, y un estado distinto de cero generalmente indica un error o una condición especial.

```bash
$ exit 0
```

Verás los estados de salida más a menudo al escribir scripts de shell. Para uso interactivo, simplemente escribir `exit` es suficiente.

### El Comando Logout

Otro comando que puedes usar para salir del terminal es `logout`. Este comando está diseñado específicamente para terminar un shell de inicio de sesión. Aunque en muchos sistemas modernos se comporta de manera similar a `exit`, es buena práctica conocer ambos comandos.

```bash
$ logout
```

### Cerrar la Ventana del Terminal

Si estás trabajando dentro de una interfaz gráfica de usuario, también tienes la opción de simplemente cerrar la ventana del terminal. Esta acción típicamente envía una señal que termina la sesión del shell que se está ejecutando dentro de ella.

### Formas Comunes de Salir de un Shell

- Escribe `exit` para terminar el shell actual.
- Presiona `Ctrl-D` en un prompt vacío para enviar fin de archivo, lo que a menudo cierra el shell.
- Escribe `logout` cuando estés en un shell de inicio de sesión.
- Cierra la ventana del terminal cuando uses un terminal gráfico.

### Preguntas Comunes

**¿Es exit lo mismo que cerrar la ventana del terminal?** A menudo el resultado es similar, pero `exit` le indica limpiamente al shell que termine.

**¿Qué es Ctrl-D?** Envía una señal de fin de archivo al shell. En un prompt vacío, esto usualmente cierra el shell.

**¿Qué significa exit 1?** Sale con el código de estado `1`, comúnmente usado para indicar fallo en scripts.

Has aprendido con éxito cómo navegar, trabajar con archivos, obtener ayuda y salir del shell.

## Exercise

Aunque no hay laboratorios específicos para este tema, recomendamos explorar la completa [Ruta de Aprendizaje de Linux](https://labex.io/es/learn/linux) para practicar habilidades y conceptos relacionados con Linux.

## Quiz Question

What is the most common command to exit from the Linux shell? Please answer using only a single lowercase English word.

## Quiz Answer

exit
