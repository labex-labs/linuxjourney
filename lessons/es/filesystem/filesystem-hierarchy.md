---
index: 1
lang: "es"
title: "Jerarquía del sistema de archivos"
meta_title: "Jerarquía del sistema de archivos - El sistema de archivos"
meta_description: "Aprende el Estándar de Jerarquía del Sistema de Archivos de Linux (FHS) y comprende directorios clave como /bin, /etc y /var. Explora la estructura de directorios de Linux."
meta_keywords: "Jerarquía del sistema de archivos de Linux, FHS, estructura de directorios de Linux, comandos de Linux, Linux para principiantes, tutorial de Linux, guía de Linux"
---

## Lesson Content

A estas alturas, probablemente ya estés familiarizado con la estructura de directorios de tu sistema; si no, lo estarás pronto. Los sistemas de archivos pueden variar en su estructura, pero en su mayor parte, deben ajustarse al Estándar de Jerarquía del Sistema de Archivos (Filesystem Hierarchy Standard).

Continúa y ejecuta un `ls -l /` para ver los directorios listados bajo el directorio raíz. El tuyo puede verse diferente al mío, pero los directorios deberían, en su mayor parte, parecerse a los siguientes:

- `/` - El directorio raíz de toda la jerarquía del sistema de archivos; todo está anidado bajo este directorio.
- `/bin` - Programas esenciales listos para ejecutar (binarios); incluye los comandos más básicos como `ls` y `cp`.
- `/boot` - Contiene los archivos del cargador de arranque del kernel.
- `/dev` - Archivos de dispositivos.
- `/etc` - Directorio de configuración central del sistema; solo debe contener archivos de configuración y ningún binario.
- `/home` - Directorios personales para usuarios; contiene tus documentos, archivos, configuraciones, etc.
- `/lib` - Contiene archivos de biblioteca que los binarios pueden usar.
- `/media` - Se utiliza como punto de conexión para medios extraíbles como unidades USB.
- `/mnt` - Sistemas de archivos montados temporalmente.
- `/opt` - Paquetes de software de aplicación opcionales.
- `/proc` - Información sobre los procesos que se están ejecutando actualmente.
- `/root` - El directorio de inicio del usuario root.
- `/run` - Información sobre el sistema en ejecución desde el último arranque.
- `/sbin` - Contiene binarios esenciales del sistema, generalmente solo pueden ser ejecutados por root.
- `/srv` - Datos específicos del sitio que son servidos por el sistema.
- `/tmp` - Almacenamiento para archivos temporales.
- `/usr` - Este nombre es desafortunado; la mayoría de las veces no contiene archivos de usuario en el sentido de una carpeta personal. Está destinado a software y utilidades instaladas por el usuario; sin embargo, eso no significa que no puedas agregar directorios personales allí. Dentro de este directorio hay subdirectorios para `/usr/bin`, `/usr/local`, etc.
- `/var` - Directorio variable; se utiliza para el registro del sistema, seguimiento de usuarios, cachés, etc. Básicamente, cualquier cosa que esté sujeta a cambios constantemente.

## Exercise

¡La práctica hace al maestro! Aquí tienes algunos laboratorios prácticos para reforzar tu comprensión del sistema de archivos de Linux:

1. **[Navegar por el sistema de archivos en Linux](https://labex.io/es/labs/comptia-navigate-the-filesystem-in-linux-590971)** - Practica el uso de comandos esenciales de shell como `pwd`, `cd` y `ls` para moverte entre directorios y explorar el sistema de archivos.
2. **[Administrar archivos y directorios en Linux](https://labex.io/es/labs/comptia-manage-files-and-directories-in-linux-590835)** - Aprende a crear, eliminar, copiar y mover archivos y directorios, y comprende los enlaces simbólicos y duros.
3. **[Encontrar archivos y comandos en Linux](https://labex.io/es/labs/comptia-find-files-and-commands-in-linux-590834)** - Domina las técnicas para localizar archivos y comandos usando `find`, `locate`, `whereis`, `which` y `type`.

Estos laboratorios te ayudarán a aplicar los conceptos en escenarios reales y a desarrollar confianza en la gestión del sistema de archivos de Linux.

## Quiz Question

¿Qué directorio se utiliza para almacenar los registros (logs)?

## Quiz Answer

/var
