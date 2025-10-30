---
index: 10
lang: "es"
title: "cp (Copiar)"
meta_title: "cp (Copiar) - Línea de Comandos"
meta_description: "Domina el comando cp de Linux para copiar archivos y directorios. Esta guía cubre opciones esenciales como la copia recursiva (-r), preservar atributos con la bandera cp -p, y forzar sobrescrituras con la bandera cp -f. Aprende cómo cp -p en Linux ayuda a mantener los metadatos del archivo."
meta_keywords: "comando cp, copiar archivos linux, linux cp -p, bandera cp -p, cp -p en linux, bandera cp -f, copia recursiva, cp -r, comodines linux, línea de comandos linux"
---

## Lesson Content

El comando `cp` es la herramienta estándar para copiar archivos y directorios en Linux. Su sintaxis básica es `cp [ORIGEN] [DESTINO]`.

### Copia Básica de Archivos

Para copiar un archivo, especificas el archivo de origen y el directorio o ruta de destino.

```bash
cp miarchivomolon /home/pete/Documentos/documentosmolones
```

En este ejemplo, `miarchivomolon` es el archivo de origen, y `/home/pete/Documentos/documentosmolones` es el directorio de destino. También puedes copiar un archivo y darle un nuevo nombre en el destino.

```bash
cp miarchivomolon /home/pete/Documentos/miarchivomolon_copia
```

### Uso de Comodines para Copia Masiva

Los comodines (wildcards) son caracteres especiales que te ayudan a seleccionar múltiples archivos basándose en patrones, proporcionando una gran flexibilidad.

- `*`: Coincide con cualquier secuencia de caracteres.
- `?`: Coincide con cualquier carácter único.
- `[]`: Coincide con cualquiera de los caracteres encerrados entre los corchetes.

Por ejemplo, para copiar todas las imágenes JPEG desde tu ubicación actual al directorio `Imágenes`:

```bash
cp *.jpg /home/pete/Imágenes
```

### Copia Recursiva de Directorios

Si intentas copiar un directorio usando `cp` sin ninguna opción, recibirás un error. Para copiar un directorio y todo su contenido, incluidos subdirectorios, debes usar la opción `-r` (recursivo).

```bash
cp -r Calabaza/ /home/pete/Documentos
```

Este comando copia el directorio `Calabaza` y todo lo que contiene a tu directorio `Documentos`.

### Manejo de Sobrescritura de Archivos

Por defecto, `cp` sobrescribirá un archivo en el destino si tiene el mismo nombre. Para prevenir la pérdida accidental de datos, usa la opción `-i` (interactiva), que solicita confirmación antes de sobrescribir.

```bash
cp -i miarchivomolon /home/pete/Imágenes
```

Por el contrario, si deseas forzar una sobrescritura sin ninguna solicitud, puedes usar la opción `cp -f`. Esto es útil en scripts donde la interacción del usuario no es posible.

```bash
cp -f miarchivomolon /home/pete/Imágenes
```

### Preservar Atributos de Archivo con cp -p

Cuando copias un archivo, sus metadatos, como la hora de modificación y la propiedad, generalmente se actualizan. Para preservar estos atributos originales, la opción `cp -p` es esencial. Usar `cp -p en linux` asegura que la copia sea una réplica exacta, no solo en contenido sino también en sus metadatos.

La opción `cp -p flag` es particularmente útil para copias de seguridad o al migrar archivos donde preservar las marcas de tiempo es crítico.

```bash
cp -p miarchivomolon /home/pete/copias_seguridad/
```

Este comando demuestra cómo usar `linux cp -p` para copiar `miarchivomolon` preservando su modo, propiedad y marcas de tiempo.

## Exercise

¡La práctica hace al maestro! Aquí tienes algunos laboratorios prácticos para reforzar tu comprensión de la copia de archivos y directorios en Linux:

1.  **[Comando cp de Linux: Copia de Archivos](https://labex.io/es/labs/linux-linux-cp-command-file-copying-209744)** - Practica el uso básico, opciones avanzadas como la copia recursiva, la preservación de atributos y el uso de comodines para copiar archivos y directorios eficientemente.
2.  **[Organización de Archivos y Directorios](https://labex.io/es/labs/linux-organizing-files-and-directories-387877)** - Practica habilidades esenciales de gestión de archivos de Linux usando los comandos `cp`, `mv` y `rm` para organizar una estructura de proyecto, mover archivos y limpiar directorios innecesarios.

Estos laboratorios te ayudarán a aplicar los conceptos en escenarios reales y a ganar confianza con la copia y gestión de archivos en Linux.

## Quiz Question

¿Qué opción necesitas especificar para copiar un directorio completo?

## Quiz Answer

-r
