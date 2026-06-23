---
index: 16
lang: "es"
title: "man"
meta_title: "man - Línea de Comandos"
meta_description: "Aprende el comando man de Linux con ejemplos para leer páginas de manual, buscar dentro de páginas man, entender secciones y encontrar opciones de comandos."
meta_keywords: "comando man, páginas man linux, manual de comandos, man ls, secciones man, buscar en página man, ayuda línea de comandos"
---

## Lesson Content

En Linux, casi todos los comandos cuentan con su propio manual de instrucciones. Estos se llaman "páginas man" (abreviatura de páginas manual), y son un recurso esencial para aprender a usar el sistema de manera efectiva.

### Entendiendo las Páginas Man

Las páginas man son la documentación incorporada para comandos de Linux, utilidades y llamadas al sistema. Proporcionan una descripción detallada de lo que hace un comando, sus opciones disponibles (o flags) y cómo usarlo. Son tu primera y mejor fuente de ayuda en la línea de comandos.

### Accediendo a un Manual con man

Para ver el manual de cualquier comando, usa `man` seguido del nombre del comando. Por ejemplo, para leer el manual de `ls`, escribe:

```bash
$ man ls
```

Esto abre la página man de `ls`. Puedes desplazarte con las flechas, buscar con `/` y presionar `q` para salir.

### Encontrando Detalles sobre Opciones de Comando

Las páginas man son particularmente útiles para entender las opciones de un comando. Por ejemplo, si has visto `ls -l` y quieres saber qué significa `-l`, abre `man ls` y busca `-l`.

Dentro de una página man:

- Presiona `/` y escribe un término para buscar hacia adelante.
- Presiona `n` para saltar a la siguiente coincidencia.
- Presiona `N` para saltar a la coincidencia anterior.
- Presiona `q` para salir.

### Entendiendo las Secciones de las Páginas Man

Las páginas manual están organizadas en secciones numeradas. Las secciones comunes incluyen:

- `1`: Comandos de usuario.
- `2`: Llamadas al sistema.
- `3`: Funciones de biblioteca.
- `5`: Formatos de archivo.
- `8`: Comandos de administración del sistema.

A veces el mismo nombre existe en más de una sección. Puedes especificar el número de sección:

```bash
$ man 5 passwd
$ man 1 passwd
```

### Preguntas Comunes

**¿Por qué la salida de man es tan larga?** Las páginas man son documentación de referencia. Usa la búsqueda dentro de `man` para saltar a la parte que necesitas.

**¿Cómo salgo de man?** Presiona `q`.

**¿Qué hago si no existe una página man?** Prueba con `COMMAND --help`, `help COMMAND`, o instala el paquete de documentación para tu distribución.

## Exercise

Practice is key to mastering the command line. These hands-on labs will help you reinforce your skills with fundamental commands. After completing them, use the `man` command to explore each tool's full potential.

1. **[Linux ls Command: Content Listing](https://labex.io/es/labs/linux-linux-ls-command-content-listing-219205)** - Practice listing and analyzing file and directory contents, and then use `man ls` to discover more options.
2. **[Linux pwd Command: Directory Displaying](https://labex.io/es/labs/linux-linux-pwd-command-directory-displaying-209734)** - Learn the `pwd` command to display your current directory, and explore its man page for details.
3. **[Linux cd Command: Directory Changing](https://labex.io/es/labs/linux-linux-cd-command-directory-changing-209733)** - Master navigating your file system with `cd`, and use `man cd` to understand its various techniques.

These labs will help you apply core concepts in real scenarios and build confidence with essential Linux commands, preparing you to effectively use `man` to deepen your knowledge.

## Quiz Question

¿Cómo ves el manual de un comando? (Por favor responde usando solo el nombre del comando en letras minúsculas en inglés).

## Quiz Answer

man
