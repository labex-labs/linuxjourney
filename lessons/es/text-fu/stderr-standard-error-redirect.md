---
index: 3
lang: "es"
title: "stderr (Error Estándar)"
meta_title: "stderr (Error Estándar) - Text-Fu"
meta_description: "Aprenda a gestionar el error estándar en Linux. Esta guía cubre la redirección de stderr, el descriptor de archivo stderr (2) y cómo redirigir stderr a un archivo o /dev/null usando 2>, 2>&1 y &>."
meta_keywords: "stderr, error estándar linux, descriptor de archivo stderr, archivo stderr, error estándar linux, redirigir stderr, 2>, 2>&1, &>, /dev/null, manejo de errores bash"
---

## Lesson Content

Exploremos qué sucede cuando un comando produce un error. Intenta listar el contenido de un directorio que no existe y redirige la salida a un archivo llamado `peanuts.txt`.

```bash
ls /fake/directory > peanuts.txt
```

En lugar de un prompt limpio, verás un mensaje de error en tu pantalla:

```plaintext
ls: cannot access /fake/directory: No such file or directory
```

Quizás te preguntes por qué este mensaje no se envió al archivo. Esto se debe a que hay otra secuencia de E/S en juego: **error estándar**, o **stderr**.

### ¿Qué es el Error Estándar en Linux?

En Linux, `stderr` es una secuencia de salida predeterminada utilizada por los programas para enviar mensajes de error y diagnósticos. Está completamente separada de la secuencia de salida estándar (`stdout`), que se utiliza para la salida normal del programa. Por defecto, tanto `stdout` como `stderr` envían su salida a la pantalla de tu terminal, razón por la cual ves el mensaje de error directamente.

Para controlar `stderr`, necesitas un método de redirección diferente.

### Entendiendo los Descriptores de Archivo

Para gestionar secuencias de E/S como `stdin`, `stdout` y `stderr`, el sistema utiliza descriptores de archivo. Un **descriptor de archivo** es un número no negativo que el kernel utiliza para identificar un archivo o secuencia abierta. Los descriptores de archivo predeterminados son:

- `0`: stdin (entrada estándar)
- `1`: stdout (salida estándar)
- `2`: stderr (error estándar)

El número `2` es el **descriptor de archivo de stderr** dedicado, y podemos usarlo para controlar a dónde van los mensajes de error.

### Redirigiendo stderr a un Archivo

Para redirigir `stderr` a un archivo, usas el descriptor de archivo `2` seguido del operador `>`. Este comando enviará cualquier mensaje de error al **archivo stderr** especificado.

```bash
ls /fake/directory 2> peanuts.txt
```

Ahora, tu terminal estará en silencio, y el mensaje de error estará dentro de `peanuts.txt`.

### Combinando stdout y stderr

¿Qué pasa si quieres capturar tanto la salida normal como los mensajes de error en el mismo archivo? Puedes lograr esto redirigiendo ambas secuencias.

```bash
ls /fake/directory /etc/passwd > peanuts.txt 2>&1
```

Analicemos esto:

1.  `> peanuts.txt` redirige `stdout` (descriptor de archivo 1) al archivo `peanuts.txt`.
2.  `2>&1` redirige `stderr` (descriptor de archivo 2) a la misma ubicación a la que apunta actualmente `stdout` (descriptor de archivo 1).

El orden es importante. `2>&1` envía `stderr` al destino actual de `stdout`. En este caso, `stdout` apunta a un archivo, por lo que `stderr` también se envía a ese archivo.

Una forma más moderna y corta de redirigir tanto `stdout` como `stderr` es usando `&>`.

```bash
ls /fake/directory /etc/passwd &> peanuts.txt
```

### Descartando Mensajes de Error

A veces, es posible que desees ejecutar un comando e ignorar por completo cualquier mensaje de error potencial. Para hacer esto, puedes redirigir `stderr` a un archivo especial llamado `/dev/null`, que descarta cualquier dato escrito en él.

```bash
ls /fake/directory 2> /dev/null
```

Este comando se ejecutará, y cualquier salida de error de `stderr` se enviará a `/dev/null` y se descartará, dejando tu pantalla limpia.

## Exercise

¡La práctica hace al maestro! Aquí tienes algunos laboratorios prácticos para reforzar tu comprensión de la redirección de entrada/salida:

1. **[Redirección de Entrada y Salida en Linux](https://labex.io/es/labs/comptia-redirecting-input-and-output-in-linux-590840)** - En este laboratorio, aprenderás a redirigir la entrada y la salida en el shell de Linux. Practicarás el control del flujo de datos desde los comandos manipulando la salida estándar (stdout), el error estándar (stderr) y la entrada estándar (stdin) usando operadores como >, >>, 2>, y el comando tee.

Este laboratorio te ayudará a aplicar los conceptos de redirección de E/S en escenarios reales y a ganar confianza en la gestión de secuencias de datos en Linux.

## Quiz Question

¿Cuál es el operador utilizado para redirigir la secuencia `stderr`? Por favor, proporciona el operador exacto en tu respuesta.

## Quiz Answer

2>
