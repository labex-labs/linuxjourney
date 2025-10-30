---
index: 1
lang: "es"
title: "Jerarquía del Sistema de Archivos"
meta_title: "Jerarquía del Sistema de Archivos - El Sistema de Archivos"
meta_description: "Explore la jerarquía estándar del sistema de archivos de Linux (FHS). Esta guía explica el propósito de directorios clave como /bin, /etc, /home y /var, ofreciendo una visión clara de la jerarquía del sistema de archivos en Linux."
meta_keywords: "jerarquía sistema archivos linux, jerarquía sistema archivos en linux, estructura jerarquía archivos linux, jerarquía archivos linux, FHS, estructura directorios linux"
---

## Lesson Content

Es probable que te estés familiarizando con la estructura de directorios de tu sistema. La mayoría de las distribuciones de Linux organizan sus sistemas de archivos de acuerdo con el estándar de la **Jerarquía del Sistema de Archivos de Linux** (FHS). Este estándar asegura que los archivos se almacenen en ubicaciones predecibles, haciendo que los sistemas sean más consistentes.

Para ver los directorios de nivel superior, ejecuta el comando `ls -l /`. Aunque tu sistema pueda tener diferencias menores, la **estructura de jerarquía de archivos de linux** principal será muy similar a la descrita a continuación.

### El Directorio Raíz

- `/` - Este es el directorio raíz, el punto de partida para todo el sistema de archivos. Cada archivo y directorio en tu sistema se encuentra bajo este directorio.

### Directorios Esenciales del Sistema

La **jerarquía de archivos en linux** incluye varios directorios críticos para el funcionamiento del sistema.

- `/bin` - Contiene programas esenciales de línea de comandos (binarios) disponibles para todos los usuarios, como `ls`, `cp` y `mv`.
- `/sbin` - Contiene binarios esenciales del sistema, destinados principalmente a la administración del sistema y que normalmente solo pueden ser ejecutados por el usuario root.
- `/etc` - Este es el directorio central de configuración del sistema. Contiene archivos de configuración para el sistema operativo y las aplicaciones instaladas, pero no debe contener binarios ejecutables.
- `/lib` - Contiene archivos de bibliotecas compartidas esenciales de los que dependen los binarios del sistema en `/bin` y `/sbin` para funcionar correctamente.
- `/boot` - Almacena los archivos necesarios para el proceso de arranque del sistema, incluido el kernel de Linux y los archivos del gestor de arranque.

### Datos de Usuario y Aplicaciones

- `/home` - Contiene directorios personales para cada usuario. Aquí es donde almacenas tus documentos, configuraciones de aplicaciones y otros archivos personales.
- `/root` - El directorio personal del usuario root, separado del directorio `/home` para asegurar que el usuario root pueda iniciar sesión incluso si `/home` no está disponible.
- `/opt` - Reservado para paquetes de software de aplicaciones opcionales o de terceros.
- `/usr` - Este directorio contiene software y utilidades instalados por el usuario. A pesar de su nombre, generalmente no contiene los archivos personales de los usuarios individuales. Tiene su propia estructura de subdirectorios, como `/usr/bin` para binarios de usuario no esenciales y `/usr/local` para software compilado desde la fuente.

### Datos Dinámicos y Temporales

- `/var` - Significa "variable" y almacena archivos cuyo tamaño y contenido se espera que cambien, como los registros del sistema (`/var/log`), cachés y archivos de spool.
- `/tmp` - Un espacio escribible por todos para almacenar archivos temporales. Los archivos en este directorio a menudo se eliminan al reiniciar el sistema.
- `/run` - Contiene información sobre el sistema en ejecución desde el último arranque, como los identificadores de proceso (PID) y otros datos de tiempo de ejecución.

### Dispositivos y Puntos de Montaje

- `/dev` - Contiene archivos de dispositivo especiales que representan componentes de hardware como discos duros, terminales y dispositivos de entrada.
- `/media` - Un punto de montaje estándar para medios extraíbles como unidades USB, tarjetas SD y CD-ROMs.
- `/mnt` - Un punto de montaje genérico para montar sistemas de archivos temporalmente.

### Información del Sistema

- `/proc` - Un sistema de archivos virtual que proporciona información en tiempo real sobre los procesos en ejecución y los parámetros del kernel.

## Exercise

¡La práctica hace al maestro! Aquí tienes algunos laboratorios prácticos para reforzar tu comprensión del sistema de archivos de Linux:

1. **[Navegar por el Sistema de Archivos en Linux](https://labex.io/es/labs/comptia-navigate-the-filesystem-in-linux-590971)** - Practica el uso de comandos esenciales de shell como `pwd`, `cd` y `ls` para moverte entre directorios y explorar el sistema de archivos.
2. **[Administrar Archivos y Directorios en Linux](https://labex.io/es/labs/comptia-manage-files-and-directories-in-linux-590835)** - Aprende a crear, eliminar, copiar y mover archivos y directorios, y comprende los enlaces simbólicos y duros.
3. **[Encontrar Archivos y Comandos en Linux](https://labex.io/es/labs/comptia-find-files-and-commands-in-linux-590834)** - Domina las técnicas para localizar archivos y comandos usando `find`, `locate`, `whereis`, `which` y `type`.

Estos laboratorios te ayudarán a aplicar los conceptos en escenarios reales y a ganar confianza con la administración del sistema de archivos de Linux.

## Quiz Question

¿Qué directorio se utiliza para almacenar los registros? (Por favor, proporcione la ruta completa. La respuesta distingue entre mayúsculas y minúsculas y debe estar en inglés.)

## Quiz Answer

/var
