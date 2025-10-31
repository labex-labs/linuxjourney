---
index: 3
lang: "es"
title: "cd (Cambiar Directorio)"
meta_title: "cd (Cambiar Directorio) - Línea de Comandos"
meta_description: "Aprende el comando esencial cd de Linux para cambiar de directorio. Esta guía cubre el uso del comando cd en el símbolo del sistema, navegando a cualquier carpeta cd con rutas absolutas y relativas, y usando atajos útiles."
meta_keywords: "comando cd, comando cd linux, carpeta cd, símbolo del sistema cd, comando cd cmd, cambiar directorio, navegación linux, ruta absoluta, ruta relativa"
---

## Lesson Content

Para moverse por el sistema de archivos de Linux, utilizarás rutas para especificar tu destino. La herramienta principal para esto es el comando `cd` (change directory o cambiar directorio). Comprender cómo usar este `comando cd linux` es una habilidad fundamental para trabajar en la terminal o en el `símbolo del sistema cd`.

### Entendiendo las Rutas

Hay dos formas de especificar una ruta: absoluta y relativa.

- **Ruta Absoluta**: Es la ruta completa que comienza desde el directorio raíz (`/`). La raíz es el directorio de nivel superior en el sistema de archivos. Cualquier ruta que comience con `/` es una ruta absoluta. Por ejemplo: `/home/pete/Desktop`.

- **Ruta Relativa**: Esta ruta es relativa a tu ubicación actual en el sistema de archivos. Si te encuentras en `/home/pete/Documents` y deseas acceder a un subdirectorio llamado `taxes`, no necesitas la ruta completa. Simplemente puedes usar la ruta relativa: `taxes/`.

### Usando el Comando cd

Una vez que entiendes las rutas, puedes usar el `comando cd` para cambiar tu directorio actual. Ya sea que estés en una terminal de Linux o en un símbolo del sistema de Windows (`cd command cmd`), el concepto de cambiar de directorio es universal, aunque la sintaxis puede variar ligeramente.

Para cambiar a un directorio específico usando una ruta absoluta, escribirías:

```bash
cd /home/pete/Pictures
```

Este comando te mueve directamente al directorio `Pictures`.

### Navegando a una carpeta cd

Si ya estás en un directorio y deseas moverte a un subdirectorio, puedes usar una ruta relativa. Por ejemplo, si tu ubicación actual es `/home/pete/Pictures` y contiene una `carpeta cd` llamada `Hawaii`, puedes navegar hacia ella con:

```bash
cd Hawaii
```

Observa que solo usamos el nombre de la carpeta. Esto se debe a que ya estábamos en su directorio padre, `/home/pete/Pictures`.

### Atajos de Navegación Esenciales

Navegar con rutas completas puede ser tedioso. Afortunadamente, el shell proporciona varios atajos para hacer que moverse sea mucho más rápido.

- `.` (directorio actual): Representa el directorio en el que te encuentras actualmente.
- `..` (directorio padre): Te mueve un nivel hacia arriba al directorio que contiene tu directorio actual.
- `~` (directorio de inicio): Un atajo a tu directorio personal de inicio, como `/home/pete`.
- `-` (directorio anterior): Te lleva de vuelta al último directorio en el que estuviste.

Puedes usar estos atajos con el `comando cd`:

```bash
cd .
cd ..
cd ~
cd -
```

Experimenta con estos atajos para ser más eficiente en la línea de comandos.

## Exercise

¡La práctica hace al maestro! Aquí tienes algunos laboratorios prácticos para reforzar tu comprensión de la navegación de directorios en Linux:

1. **[Comando cd de Linux: Cambio de Directorio](https://labex.io/es/labs/linux-linux-cd-command-directory-changing-209733)** - Aprende el comando `cd` de Linux para navegar eficientemente por tu sistema de archivos, incluyendo varias técnicas para cambiar de directorio, comprender rutas y explorar la estructura de archivos.
2. **[Navegación de Directorios en Linux](https://labex.io/es/labs/linux-directory-navigation-387844)** - Pon a prueba tus habilidades básicas de línea de comandos de Linux navegando por directorios usando comandos esenciales.
3. **[Configuración de una Nueva Estructura de Proyecto](https://labex.io/es/labs/linux-setting-up-a-new-project-structure-387859)** - Practica tus habilidades de gestión de directorios de Linux creando una estructura de proyecto específica y navegando a través de ella usando comandos esenciales como `mkdir` y `cd`.

Estos laboratorios te ayudarán a aplicar los conceptos en escenarios reales y a ganar confianza al navegar por el sistema de archivos de Linux.

## Quiz Question

Si te encuentras en `/home/pete/Pictures` y deseas navegar al directorio padre (`/home/pete`), ¿cuál es el comando completo que debes usar? Por favor, responde en inglés, prestando atención a las mayúsculas y los espacios.

## Quiz Answer

cd ..
