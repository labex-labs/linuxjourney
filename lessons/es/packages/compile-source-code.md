---
index: 7
lang: "es"
title: "Compilar Código Fuente"
meta_title: "Compilar Código Fuente - Paquetes"
meta_description: "Aprenda a compilar desde el código fuente en Linux. Esta guía cubre los pasos esenciales sobre cómo construir código fuente usando configure, make y el comando recomendado checkinstall para una gestión de paquetes limpia."
meta_keywords: "cómo compilar desde código fuente, cómo construir código fuente, compilar código fuente, make install, checkinstall, compilar Linux, build-essential, script configure, makefile, tutorial Linux"
---

## Lesson Content

Ocasionalmente, es posible que encuentres un paquete que solo está disponible como código fuente. Para usarlo, deberás compilarlo e instalarlo en tu sistema. Esta lección te guiará a través del proceso común de cómo compilar desde el código fuente.

### Preparación de su Sistema

Antes de poder compilar cualquier cosa, necesitas las herramientas necesarias. En sistemas basados en Debian como Ubuntu, puedes instalarlas con un solo comando.

```bash
sudo apt install build-essential
```

El paquete `build-essential` instala un conjunto de herramientas de desarrollo de software, incluido el compilador GCC y la utilidad `make`, que son esenciales para la compilación.

Después de instalar las herramientas, extrae el contenido del paquete de código fuente, que suele ser un archivo `.tar.gz`.

```bash
tar -xzvf paquete.tar.gz
```

Antes de continuar, revisa siempre si hay un archivo `README` o `INSTALL` dentro del directorio extraído. Estos archivos a menudo contienen instrucciones específicas o dependencias requeridas para ese paquete en particular.

### El Proceso de Compilación Estándar

Aunque diferentes desarrolladores pueden usar varios sistemas de compilación como `cmake`, el método más tradicional implica un proceso de tres pasos. Comprender esto es fundamental para aprender cómo construir código fuente.

Primero, ejecuta el script `configure`. Este script verifica tu sistema en busca de todas las dependencias y bibliotecas necesarias que el software necesita para compilarse y ejecutarse correctamente.

```bash
./configure
```

El prefijo `./` le indica al shell que ejecute el script desde el directorio actual. Si el script informa de alguna dependencia faltante, debes instalarlas antes de continuar.

Luego, ejecuta el comando `make`. Este comando lee un archivo llamado `Makefile` en el directorio, que contiene un conjunto de reglas sobre cómo compilar el código fuente en programas ejecutables.

```bash
make
```

Finalmente, para instalar el software en tu sistema, normalmente ejecutarías:

```bash
sudo make install
```

Este comando copia los archivos compilados a los directorios del sistema apropiados, haciendo que el software esté disponible para su uso.

### Una Mejor Forma de Instalar

Aunque `sudo make install` funciona, tiene una desventaja significativa: no registra el software en el gestor de paquetes de tu sistema. Esto dificulta el seguimiento, la actualización o la desinstalación limpia del paquete más adelante.

Un enfoque mucho mejor es usar `checkinstall`. Esta herramienta ejecuta el proceso de instalación pero, en lugar de copiar archivos directamente, crea un paquete nativo del sistema (como un archivo `.deb` en Debian/Ubuntu) y lo instala.

```bash
sudo checkinstall
```

Usar `checkinstall` integra el software compilado en tu sistema de gestión de paquetes. Esto significa que puedes eliminarlo fácilmente más tarde usando `apt` o `dpkg`, al igual que cualquier otro paquete que hayas instalado desde los repositorios oficiales. Por esta razón, siempre debes preferir `checkinstall` sobre `make install`.

Para desinstalar un paquete instalado con `make install`, tendrías que volver al directorio fuente y ejecutar `sudo make uninstall`, pero esto no siempre es fiable.

## Exercise

¡La práctica hace al maestro! Aquí tienes un laboratorio práctico para reforzar tu comprensión de la compilación de software desde el código fuente:

1. **[Compilar Software desde Código Fuente en Linux](https://labex.io/es/labs/comptia-build-software-from-source-code-in-linux-590853)** - Practica el proceso fundamental de compilar e instalar software desde su código fuente, incluyendo el uso de `configure`, `make` y `make install`.

Este laboratorio te ayudará a aplicar los conceptos en un escenario real y a ganar confianza al compilar software.

## Quiz Question

What should you use instead of `make install` ALWAYS? (Please answer in English, paying attention to case sensitivity)

## Quiz Answer

checkinstall
