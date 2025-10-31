---
index: 5
lang: "es"
title: "env (Entorno)"
meta_title: "env (Entorno) - Text-Fu"
meta_description: "Explora qué hace el comando env en Linux. Esta guía explica cómo ver y usar variables de entorno de Linux como PATH, HOME y USER con el comando env de Linux."
meta_keywords: "env, env linux, env comando linux, qué hace env en linux, variables de entorno, variable PATH, variables de shell"
---

## Lesson Content

Su sistema Linux utiliza variables de entorno para almacenar información a la que pueden acceder el shell y otros procesos. Estas variables contienen datos útiles sobre su sesión de usuario y la configuración del sistema.

### Explorando Variables de Entorno Básicas

You puede ver el valor de una variable específica anteponiendo su nombre con un símbolo de `$` . Por ejemplo, ejecute el siguiente comando:

```bash
echo $HOME
```

Este comando mostrará la ruta a su directorio de inicio, que podría verse algo como `/home/pete`.

Ahora, pruebe con otro:

```bash
echo $USER
```

Esto mostrará su nombre de usuario actual. ¿Pero de dónde viene esta información? Se almacena en el entorno de su shell.

### ¿Qué Hace `env` en Linux?

Para ver todas las variables de entorno configuradas actualmente para su sesión, puede usar el comando `env`. El `comando linux env` es una herramienta fundamental para inspeccionar la configuración de su shell.

```bash
env
```

Ejecutar el comando `env` mostrará una lista de pares clave-valor. Aquí hay un breve ejemplo de lo que podría ver:

```plaintext
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/bin
PWD=/home/user
USER=pete
```

Comprender el `linux env` es crucial para administrar su sistema de manera efectiva.

### La Importancia de la Variable PATH

Una de las variables más importantes en su salida de `env linux` es `PATH`. Puede ver su contenido específicamente con:

```bash
echo $PATH
```

Este comando devuelve una lista de directorios separados por dos puntos. Cuando escribe un comando, su sistema busca en estos directorios para encontrar el archivo ejecutable correspondiente.

Imagine que instala manualmente un programa en un directorio no estándar como `/opt/coolapp/bin`. Si intenta ejecutarlo escribiendo `coolcommand`, podría obtener un error de "comando no encontrado". Esto sucede porque el directorio que contiene su programa no está listado en la variable `PATH`, por lo que el shell no sabe dónde buscarlo.

Para solucionar esto, puede modificar la variable `PATH` para incluir el nuevo directorio. Al agregar su directorio personalizado a `PATH`, permite que el shell encuentre y ejecute sus programas desde cualquier lugar de la terminal.

## Exercise

¡La práctica hace al maestro! Aquí hay algunos laboratorios prácticos para reforzar su comprensión de las variables de entorno de Linux:

1.  **[Administrar el Entorno y la Configuración del Shell en Linux](https://labex.io/es/labs/comptia-manage-shell-environment-and-configuration-in-linux-590838)** - Practique la creación y gestión de variables locales y de entorno, comprenda la herencia y haga que las configuraciones sean persistentes modificando el archivo `.bashrc`.
2.  **[Variables de Entorno en Linux](https://labex.io/es/labs/linux-environment-variables-in-linux-385274)** - Aprenda el concepto y el uso de las variables de entorno, cómo crearlas, modificarlas y gestionarlas, y su papel en la configuración del sistema.
3.  **[Configurar Variables de Entorno de Linux](https://labex.io/es/labs/linux-configure-linux-environment-variables-437861)** - Obtenga experiencia práctica creando, estableciendo y gestionando variables de entorno en un sistema Linux.

Estos laboratorios le ayudarán a aplicar los conceptos en escenarios reales y a ganar confianza en la gestión del entorno de su shell Linux.

## Quiz Question

Which command displays all of your current environment variables? (Please answer in English, using only the lowercase command name)

## Quiz Answer

env
