---
title: "env (Entorno)"
description: "Aprende sobre las variables de entorno de Linux con el comando 'env'. Comprende las variables PATH, HOME y USER. Obtén una guía para principiantes para gestionar tu entorno Linux."
keywords: "comando env, variables de entorno Linux, variable PATH, tutorial Linux, Linux para principiantes, variables de shell, guía Linux"
---

## Lesson Content

Ejecuta el siguiente comando:

```bash
echo $HOME
```

Deberías ver la ruta a tu directorio home; el mío se ve como /home/pete.

¿Qué hay de este comando?

```bash
echo $USER
```

¡Deberías ver tu nombre de usuario!

¿De dónde viene esta información? Viene de tus variables de entorno. Puedes verlas escribiendo:

```bash
env
```

Esto muestra una gran cantidad de información sobre las variables de entorno que tienes configuradas actualmente. Estas variables contienen información útil que el shell y otros procesos pueden usar.

Aquí tienes un breve ejemplo:

```plaintext
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/bin
PWD=/home/user
USER=pete
```

Una variable particularmente importante es la variable PATH. Puedes acceder a estas variables poniendo un `$` delante del nombre de la variable, así:

```bash
$ echo $PATH
/usr/local/sbin:/usr/local/bin:/usr/sbin:/bin
```

Esto devuelve una lista de rutas separadas por dos puntos que tu sistema busca cuando ejecuta un comando. Digamos que descargas e instalas manualmente un paquete de internet y lo pones en un directorio no estándar, y quieres ejecutar ese comando. Escribes `$ coolcommand`, y el prompt dice "command not found". Bueno, eso es tonto; estás viendo el binario en una carpeta y sabes que existe. Lo que está sucediendo es que la variable `$PATH` no busca ese directorio para este binario, por lo que está lanzando un error.

Digamos que tenías toneladas de binarios que querías ejecutar desde ese directorio; simplemente puedes modificar la variable PATH para incluir ese directorio en tu variable de entorno PATH.

## Exercise

¿Qué muestra lo siguiente? ¿Por qué?

```bash
echo $HOME
```

## Quiz Question

¿Cómo puedes ver tus variables de entorno?

## Quiz Answer

env
