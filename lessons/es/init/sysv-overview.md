---
index: 1
lang: "es"
title: "Descripción general de System V"
meta_title: "Descripción general de System V - Init"
meta_description: "Aprenda sobre System V init, sus runlevels y cómo gestiona los procesos en Linux. Comprenda los conceptos básicos de SysV para usuarios principiantes e intermedios."
meta_keywords: "System V, SysV init, runlevels de Linux, sistema init, tutorial de Linux, guía para principiantes, gestión de procesos"
---

## Lesson Content

El propósito principal de init es iniciar y detener procesos esenciales en el sistema. Hay tres implementaciones principales de init en Linux: System V, Upstart y systemd. En esta lección, vamos a repasar la versión más tradicional de init, System V init o Sys V (pronunciado como 'Sistema Cinco').

Para saber si está utilizando la implementación de Sys V init, verifique si existe un archivo `/etc/inittab`; si existe, lo más probable es que esté ejecutando Sys V.

Sys V inicia y detiene procesos secuencialmente. Por ejemplo, si quisiera iniciar un servicio llamado `foo-a`, `foo-b` no puede funcionar hasta que `foo-a` ya esté en ejecución. Sys V logra esto con scripts. Estos scripts inician y detienen servicios para nosotros. Podemos escribir nuestros propios scripts, o la mayoría de las veces, usar los que ya están integrados en el sistema operativo y se utilizan para cargar servicios esenciales.

Las ventajas de usar esta implementación de init son que es relativamente fácil resolver dependencias, ya que sabe que `foo-a` viene antes que `foo-b`. Sin embargo, el rendimiento no es excelente porque generalmente solo una cosa se inicia o se detiene a la vez.

Al usar Sys V, el estado de la máquina se define por los runlevels (niveles de ejecución), que se establecen del 0 al 6. Estos diferentes modos variarán según la distribución, pero la mayoría de las veces se verán así:

- 0: Apagado
- 1: Modo de usuario único
- 2: Modo multiusuario sin red
- 3: Modo multiusuario con red
- 4: Sin usar
- 5: Modo multiusuario con red y GUI
- 6: Reiniciar

Cuando su sistema se inicia, busca en qué runlevel se encuentra y ejecuta scripts ubicados dentro de la configuración de ese runlevel. Los scripts se encuentran en **/etc/rc.d/rc[número de runlevel].d/** o **/etc/init.d**. Los scripts que comienzan con S (start) o K (kill) se ejecutarán al inicio y al apagado, respectivamente. Los números junto a estos caracteres indican la secuencia en la que se ejecutan.

Por ejemplo:

```bash
pete@icebox:/etc/rc.d/rc0.d$ ls
K10updates  K80openvpn
```

Vemos que cuando cambiamos al runlevel 0 o modo de apagado, nuestra máquina intentará ejecutar un script para detener los servicios de actualizaciones y luego OpenVPN. Para saber en qué runlevel se está iniciando su máquina, puede ver el runlevel predeterminado en el archivo `/etc/inittab`. También puede cambiar su runlevel predeterminado en este archivo.

Una cosa a tener en cuenta: System V está siendo reemplazado lentamente, tal vez no hoy, o incluso dentro de años. Sin embargo, es posible que vea runlevels aparecer en otras implementaciones de init. Esto es principalmente para admitir aquellos servicios que solo se inician o detienen usando scripts de inicio de System V.

## Exercise

¡La práctica hace al maestro! Aquí hay algunos laboratorios prácticos para reforzar su comprensión de la gestión de procesos de Linux y la configuración del sistema, que son fundamentales para el funcionamiento de los sistemas init:

1. **[Administrar y Monitorear Procesos de Linux](https://labex.io/es/labs/comptia-manage-and-monitor-linux-processes-590864)** - Practique la interacción con procesos en primer y segundo plano, inspeccionándolos con `ps`, monitoreando recursos con `top` y terminándolos con `kill`. Esto se relaciona directamente con el aspecto de 'iniciar y detener procesos esenciales' de init.
2. **[Programar Tareas con at y cron en Linux](https://labex.io/es/labs/comptia-schedule-tasks-with-at-and-cron-in-linux-590870)** - Aprenda a programar tareas únicas y recurrentes, lo que se basa en el concepto de ejecución automatizada similar a cómo los scripts init gestionan los servicios.
3. **[Administrar Permisos de Archivos y Directorios en Linux](https://labex.io/es/labs/comptia-manage-file-and-directory-permissions-in-linux-590844)** - Comprenda cómo administrar los permisos de archivos y directorios, una habilidad crítica para trabajar con archivos de configuración del sistema y scripts como los que se encuentran en `/etc/init.d`.

Estos laboratorios le ayudarán a aplicar los conceptos en escenarios reales y a generar confianza con las tareas fundamentales de administración del sistema Linux.

## Quiz Question

¿Qué runlevel se usa generalmente para el apagado?

## Quiz Answer

0
