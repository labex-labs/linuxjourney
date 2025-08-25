---
index: 5
lang: "es"
title: "env (Entorno)"
meta_title: "env (Entorno) - Text-Fu"
meta_description: "Aprende sobre las variables de entorno de Linux con el comando 'env'. Entiende las variables PATH, HOME y USER. Obtén una guía para principiantes para gestionar tu entorno Linux."
meta_keywords: "comando env, variables de entorno Linux, variable PATH, tutorial Linux, Linux para principiantes, variables de shell, guía Linux"
---

## Lesson Content

Ejecuta el siguiente comando:

```bash
echo $HOME
```

Deberías ver la ruta a tu directorio de inicio; el mío se ve como /home/pete.

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

Esto devuelve una lista de rutas separadas por dos puntos que tu sistema busca cuando ejecuta un comando. Digamos que descargas e instalas manualmente un paquete de internet y lo pones en un directorio no estándar, y quieres ejecutar ese comando. Escribes `$ coolcommand`, y el prompt dice "command not found". Bueno, eso es tonto; estás viendo el binario en una carpeta y sabes que existe. Lo que está sucediendo es que la variable `$PATH` no verifica ese directorio para este binario, por lo que está lanzando un error.

Digamos que tenías toneladas de binarios que querías ejecutar desde ese directorio; simplemente puedes modificar la variable PATH para incluir ese directorio en tu variable de entorno PATH.

## Exercise

¡La práctica hace al maestro! Aquí tienes algunos laboratorios prácticos para reforzar tu comprensión de las variables de entorno de Linux:

1. **[Administrar el entorno y la configuración del shell en Linux](https://labex.io/es/labs/comptia-manage-shell-environment-and-configuration-in-linux-590838)** - Practica la creación y gestión de variables locales y de entorno, la comprensión de la herencia y la persistencia de las configuraciones modificando el archivo `.bashrc`.
2. **[Variables de entorno en Linux](https://labex.io/es/labs/linux-environment-variables-in-linux-385274)** - Aprende el concepto y el uso de las variables de entorno, cómo crearlas, modificarlas y gestionarlas, y su papel en la configuración del sistema.
3. **[Configurar variables de entorno de Linux](https://labex.io/es/labs/linux-configure-linux-environment-variables-437861)** - Obtén experiencia práctica creando, configurando y gestionando variables de entorno en un sistema Linux.

Estos laboratorios te ayudarán a aplicar los conceptos en escenarios reales y a generar confianza en la gestión de tu entorno de shell de Linux.

## Quiz Question

¿Cómo ves tus variables de entorno?

## Quiz Answer

env
