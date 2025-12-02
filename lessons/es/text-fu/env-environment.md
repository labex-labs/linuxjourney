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

Puede ver el valor de una variable específica anteponiendo su nombre con un símbolo de `$`. Por ejemplo, ejecute el siguiente comando:

```bash
echo $HOME
```

Este comando mostrará la ruta a su directorio de inicio, que podría verse algo como `/home/pete`.

Ahora, pruebe con otro:

```bash
echo $USER
```

Esto mostrará su nombre de usuario actual. ¿Pero de dónde viene esta información? Está almacenada en el entorno de su shell.

### ¿Qué Hace env en Linux?

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

### Establecer una Variable de Entorno para la Sesión Actual

Ejecutar el siguiente comando en su terminal establece la variable de entorno `TEST` solo para la sesión actual:

```bash
export TEST=test
```

Después de esto, si ejecuta:

```bash
echo $TEST
```

La salida será:

```
test
```

Esta variable estará disponible mientras la sesión de terminal permanezca abierta. Una vez que cierre y vuelva a abrir la terminal, la variable ya no existirá.

### Hacer Persistente la Variable de Entorno Entre Sesiones

Si desea que la variable de entorno esté disponible en cada sesión de terminal (incluso después de cerrar y volver a abrir la terminal), debe agregarla al archivo de inicio de su shell. En el caso de Bash (el shell predeterminado para muchas distribuciones de Linux y macOS), este archivo suele ser `.bashrc` en su directorio de inicio.

Así es como se hace:

1.  Abra `.bashrc` en su editor de texto preferido. Por ejemplo:

        ```bash

    nano ~/.bashrc
    ```

2.  Agregue la línea `export` al final del archivo:

        ```bash

    export TEST=test
    ```

3.  Guarde y salga del editor (en Nano, esto sería `Ctrl+X`, luego `Y` para confirmar y `Enter`).

4.  Para aplicar los cambios inmediatamente sin volver a abrir la terminal, ejecute:

        ```bash

    source ~/.bashrc
    ```

Después de esto, la variable `TEST` estará disponible en todas las sesiones de terminal futuras, y ejecutar `echo $TEST` imprimirá `test` incluso después de cerrar y volver a abrir la terminal.

### Una Nota sobre los Archivos de Configuración del Shell

- Para **Bash** (el predeterminado en muchos sistemas), el archivo relevante es `~/.bashrc` para shells interactivos que no inician sesión.
- Para **Zsh**, el archivo equivalente suele ser `~/.zshrc`.
- Para **Fish**, normalmente usaría `~/.config/fish/config.fish`.

## Exercise

¡La práctica hace la perfección! Aquí hay algunos laboratorios prácticos para reforzar su comprensión de las variables de entorno de Linux:

1. **[Administrar el Entorno y la Configuración del Shell en Linux](https://labex.io/es/labs/comptia-manage-shell-environment-and-configuration-in-linux-590838)** - Practique la creación y gestión de variables locales y de entorno, comprenda la herencia y haga que las configuraciones sean persistentes modificando el archivo `.bashrc`.
2. **[Variables de Entorno en Linux](https://labex.io/es/labs/linux-environment-variables-in-linux-385274)** - Aprenda el concepto y el uso de las variables de entorno, cómo crearlas, modificarlas y gestionarlas, y su papel en la configuración del sistema.
3. **[Configurar Variables de Entorno de Linux](https://labex.io/es/labs/linux-configure-linux-environment-variables-437861)** - Obtenga experiencia práctica creando, estableciendo y gestionando variables de entorno en un sistema Linux.

Estos laboratorios le ayudarán a aplicar los conceptos en escenarios reales y a ganar confianza en la gestión del entorno de su shell Linux.

## Quiz Question

¿Qué comando muestra todas sus variables de entorno actuales? (Por favor, responda en inglés, usando solo el nombre del comando en minúsculas).

## Quiz Answer

env
