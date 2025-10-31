---
index: 6
lang: "es"
title: "Módulos del Kernel"
meta_title: "Módulos del Kernel - Kernel"
meta_description: "Descubra qué son los módulos del kernel en Linux y cómo extienden la funcionalidad del kernel. Esta lección cubre el uso de lsmod y modprobe para listar, cargar y descargar módulos bajo demanda."
meta_keywords: "qué son los módulos del kernel, módulos del kernel de Linux, modprobe, lsmod, gestión del kernel, tutorial de Linux, Linux para principiantes, guía de Linux"
---

## Lesson Content

Piense en el núcleo de Linux como el motor central de un coche. Puede añadir accesorios como una baca o un nuevo sistema de sonido sin cambiar el motor en sí. Estos accesorios se pueden añadir o quitar según sea necesario. El núcleo de Linux utiliza un concepto similar con los módulos del kernel.

### ¿Qué son los Módulos del Kernel

Entonces, **¿qué son los módulos del kernel?** Son piezas de código que se pueden cargar y descargar del kernel bajo demanda. Extienden la funcionalidad del kernel sin requerir que recompiles el kernel principal o reinicies el sistema. Este enfoque modular permite añadir soporte para nuevo hardware (como una nueva tarjeta Wi-Fi) o nuevas características de software (como un nuevo sistema de archivos) dinámicamente. Esto mantiene el kernel principal ligero al tiempo que permite una inmensa flexibilidad.

### Listar Módulos Cargados

Para ver una lista de todos los módulos del kernel cargados actualmente en memoria, puede usar el comando `lsmod`. Esto le da una instantánea de los módulos activos y sus dependencias.

```bash
lsmod
```

### Cargar un Módulo del Kernel

Para cargar un módulo del kernel, usamos el comando `modprobe`. Por ejemplo, para cargar el módulo `bluetooth`, ejecutaría:

```bash
sudo modprobe bluetooth
```

El comando `modprobe` es inteligente; busca el módulo en el directorio estándar (`/lib/modules/$(uname -r)/`) y también carga cualquier otro módulo del que dependa el módulo objetivo.

### Descargar un Módulo del Kernel

Si un módulo ya no es necesario, puede descargarlo para liberar recursos del sistema. Use la opción `-r` con `modprobe` para eliminar un módulo:

```bash
sudo modprobe -r bluetooth
```

### Gestionar Módulos al Arrancar

Los módulos cargados con `modprobe` son temporales y desaparecerán después de un reinicio. Para hacer permanentes las configuraciones de los módulos, puede crear archivos de configuración en el directorio `/etc/modprobe.d/`.

Para cargar automáticamente un módulo al arrancar con opciones específicas, cree un archivo `.conf`. Por ejemplo, si tuviera un módulo hipotético llamado `peanut_butter` y quisiera establecer su parámetro `type` como `almond`, su archivo se vería así:

```plaintext
# /etc/modprobe.d/peanutbutter.conf

options peanut_butter type=almond
```

A la inversa, para evitar que un módulo se cargue al arrancar (un proceso llamado "blacklisting" o lista negra), puede usar la palabra clave `blacklist` en un archivo de configuración:

```plaintext
# /etc/modprobe.d/peanutbutter.conf

blacklist peanut_butter
```

Estos archivos de configuración permiten un control detallado sobre qué módulos están disponibles cuando su sistema se inicia.

## Exercise

¡La práctica hace al maestro! Aquí hay un laboratorio práctico para reforzar su comprensión de los módulos del kernel de Linux:

1. **[Gestionar Módulos del Kernel en Linux](https://labex.io/es/labs/comptia-manage-kernel-modules-in-linux-590865)** - Practique listar, inspeccionar, cargar y descargar módulos del kernel, y configurarlos para que se carguen automáticamente al arrancar. Este laboratorio le ayudará a aplicar los conceptos en un escenario real y a ganar confianza con la gestión de módulos del kernel.

## Quiz Question

¿Qué comando se utiliza para descargar un módulo?

## Quiz Answer

modprobe -r
