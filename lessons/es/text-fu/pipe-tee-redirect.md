---
index: 4
lang: "es"
title: "tubería y tee"
meta_title: "tubería y tee - Text-Fu"
meta_description: "Explore el potente comando pipe y tee en Linux. Aprenda a encadenar comandos con la combinación pipe tee de Linux y redirigir la salida tanto a la pantalla como a un archivo. Esta guía cubre cómo usar pipe a tee para un flujo de datos avanzado en la línea de comandos."
meta_keywords: "comando pipe y tee en linux, pipe tee linux, pipe a tee, tubería linux, comando tee, stdout, stdin, redirección de línea de comandos, tutorial linux"
---

## Lesson Content

En Linux, la línea de comandos se vuelve increíblemente poderosa cuando empiezas a conectar comandos. En lugar de ejecutar un comando, guardar su salida y luego ejecutar otro, puedes crear una tubería (pipeline) para pasar datos directamente entre ellos.

### Entendiendo el Operador Pipe

Comencemos con un comando que produce mucha salida:

```bash
ls -la /etc
```

La lista de elementos es probablemente demasiado larga para caber en tu pantalla, lo que dificulta su lectura. Si bien podrías redirigir esta salida a un archivo, un método más eficiente es enviarla directamente a otro comando, como `less`, para una visualización fácil.

```bash
ls -la /etc | less
```

El operador pipe `|`, representado por una barra vertical, es la clave de este proceso. Toma la salida estándar (`stdout`) del comando a su izquierda y la utiliza como entrada estándar (`stdin`) para el comando a su derecha. En este caso, _enviamos por tubería_ (piped) la salida de `ls -la /etc` directamente al comando `less`. El pipe es una herramienta fundamental que usarás constantemente.

### Dividiendo la Salida con el Comando Tee

¿Qué pasa si quieres ver la salida en tu pantalla _y_ guardarla en un archivo simultáneamente? Aquí es donde entra en juego el comando `tee`. El `comando pipe and tee en linux` es una combinación clásica para registrar y monitorear.

```bash
ls | tee peanuts.txt
```

Después de ejecutar esto, verás la salida de `ls` en tu terminal. Si también compruebas el contenido de `peanuts.txt`, encontrarás exactamente la misma información. El comando `tee` divide efectivamente el flujo de salida en dos direcciones: una a la salida estándar y otra a un archivo especificado.

### Combinando Pipe y Tee

Puedes crear flujos de trabajo aún más avanzados encadenando estos comandos. Un patrón común es usar `pipe to tee` en medio de una cadena de comandos más larga. Esto te permite guardar un resultado intermedio mientras continúas procesando los datos.

Por ejemplo, puedes usar la combinación `linux pipe tee` para ver y guardar la salida antes de un filtrado adicional:

```bash
ls -la /etc | tee etc_listing.txt | grep "conf"
```

Este comando hace tres cosas:

1. Lista el contenido del directorio `/etc`.
2. Envía esa salida por tubería a `tee`, que guarda una copia en `etc_listing.txt` y también la pasa adelante.
3. La salida de `tee` se envía luego por tubería a `grep`, que filtra las líneas que contienen "conf".

Dominar estos comandos mejorará significativamente tu eficiencia en la línea de comandos.

## Exercise

¡La práctica hace al maestro! Aquí tienes algunos laboratorios prácticos para reforzar tu comprensión del redireccionamiento de entrada/salida y las tuberías (pipelines):

1. **[Redirección de Entrada y Salida en Linux](https://labex.io/es/labs/comptia-redirecting-input-and-output-in-linux-590840)** - Practica el control del flujo de datos desde comandos manipulando la salida estándar (stdout), el error estándar (stderr) y la entrada estándar (stdin) usando operadores como `>`, `>>`, `2>` y el comando `tee`.
2. **[Control de Secuencia y Tubería en Linux](https://labex.io/es/labs/linux-sequence-control-and-pipeline-17994)** - Aprende a controlar las secuencias de ejecución de comandos, utilizar tuberías (pipelines) y aprovechar herramientas potentes de procesamiento de texto como `cut`, `grep`, `wc`, `sort` y `uniq`.
3. **[Redirección de Flujo de Datos](https://labex.io/es/labs/linux-data-stream-redirection-17995)** - Aprende el arte de la redirección de flujos en Linux, incluida la manipulación de flujos de entrada, salida y error estándar, la combinación de salidas y el uso de `/dev/null`.

Estos laboratorios te ayudarán a aplicar los conceptos de tuberías y redirección en escenarios reales y a ganar confianza con la manipulación de datos en la línea de comandos.

## Quiz Question

¿Qué carácter único representa el operador pipe en un comando de Linux? Por favor, responde solo con el símbolo.

## Quiz Answer

|
