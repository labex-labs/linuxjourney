---
index: 2
lang: "es"
title: "pwd (Imprimir Directorio de Trabajo)"
meta_title: "pwd (Imprimir Directorio de Trabajo) - Línea de Comandos"
meta_description: "Aprende el comando pwd de Linux, qué significa imprimir el directorio de trabajo y cómo las rutas absolutas muestran tu ubicación actual en el sistema de archivos."
meta_keywords: "comando pwd, linux pwd, imprimir directorio de trabajo, directorio actual linux, ruta absoluta, sistema de archivos linux, árbol de directorios"
---

## Lesson Content

En Linux, los archivos y directorios están organizados en una jerarquía llamada sistema de archivos. Antes de poder moverte con confianza, necesitas saber dónde estás. El comando `pwd` responde a esa pregunta imprimiendo tu directorio de trabajo actual.

### El Árbol de Directorios en Linux

Todo el sistema de archivos comienza desde un único directorio de nivel superior llamado directorio raíz, representado por una barra diagonal (`/`). Desde la raíz, el árbol de directorios se ramifica en subdirectorios, que pueden contener archivos y más subdirectorios.

Aquí hay un ejemplo simplificado de cómo se ve esta estructura:

```plaintext
/
|-- bin
|   |-- file1
|   |-- file2
|-- etc
|   |-- file3
|   `-- directory1
|       |-- file4
|       `-- file5
|-- home
|-- var
```

### Entendiendo las Rutas de Archivos

La ubicación de cualquier archivo o directorio se describe mediante su ruta. Una ruta es una secuencia de directorios que conduce desde un punto de inicio hasta un destino específico.

Por ejemplo, si tienes una carpeta llamada `pete` dentro de `/home`, y una carpeta `Movies` dentro de `pete`, la ruta completa es:

```plaintext
/home/pete/Movies
```

Una ruta que comienza con `/` es una ruta absoluta porque empieza en el directorio raíz. Una ruta como `Movies` es relativa porque depende de tu ubicación actual.

### ¿Cuál es la Forma Completa de PWD en Linux?

La forma completa de `pwd` es "print working directory" (imprimir directorio de trabajo). Tu directorio de trabajo es el directorio donde tu shell se encuentra actualmente. Los comandos que usan rutas relativas parten desde esta ubicación.

### Usando el Comando pwd

Para encontrar tu directorio actual, escribe `pwd` y presiona Enter.

```bash
$ pwd
/home/pete
```

La salida es una ruta absoluta. En este ejemplo, el shell está actualmente en el directorio personal del usuario `pete`.

### Por Qué pwd es Útil

Usa `pwd` cuando:

- Estás siguiendo instrucciones y necesitas confirmar tu ubicación.
- Un comando falló porque una ruta de archivo era incorrecta.
- Te moviste por varios directorios y perdiste la pista de dónde estás.
- Quieres copiar la ruta del directorio actual en otro comando.

Por ejemplo:

```bash
$ pwd
/home/pete/projects
$ ls
app.py  README.md
```

Esto te dice que `app.py` y `README.md` están ubicados en `/home/pete/projects`.

### Preguntas Comunes

**¿pwd cambia algo?** No. `pwd` solo imprime información.

**¿Por qué la salida es diferente en mi sistema?** Tu nombre de usuario, directorio personal y ubicación actual pueden ser diferentes.

**¿Cuál es la diferencia entre pwd y cd?** `pwd` muestra dónde estás. `cd` cambia dónde estás.

## Exercise

¡La práctica hace al maestro! Aquí tienes algunos laboratorios prácticos para reforzar tu comprensión de la navegación en el sistema de archivos de Linux y cómo identificar tu ubicación actual:

1. **[Comando pwd de Linux: Mostrar Directorio](https://labex.io/es/labs/linux-linux-pwd-command-directory-displaying-209734)** - Este laboratorio ofrece una visión enfocada y uso práctico del comando `pwd`, alineado directamente con la introducción de la lección para encontrar tu directorio actual.
2. **[Navegación de Directorios en Linux](https://labex.io/es/labs/linux-directory-navigation-387844)** - Pon a prueba tus habilidades básicas en la línea de comandos de Linux navegando por varios directorios, solidificando tu comprensión de rutas y la estructura del sistema de archivos.
3. **[Comando cd de Linux: Cambiar Directorio](https://labex.io/es/labs/linux-linux-cd-command-directory-changing-209733)** - Aprende a navegar eficientemente tu sistema de archivos usando el comando `cd`, entendiendo diferentes técnicas para cambiar de directorio y explorar la estructura de archivos.

Estos laboratorios te ayudarán a aplicar los conceptos de jerarquía y navegación del sistema de archivos en escenarios reales y a ganar confianza con comandos esenciales de Linux.

## Quiz Question

¿Qué comando se usa para encontrar el directorio en el que te encuentras actualmente? (Por favor responde en inglés, usando solo el nombre del comando en minúsculas.)

## Quiz Answer

pwd
