---
index: 1
lang: "es"
title: "Visión general de System V"
meta_title: "Visión general de System V - Init"
meta_description: "Aprenda sobre System V init, sus niveles de ejecución (runlevels) y cómo gestiona los procesos en Linux. Comprenda los conceptos básicos de SysV para usuarios principiantes e intermedios."
meta_keywords: "System V, SysV init, niveles de ejecución de Linux, sistema init, tutorial de Linux, guía para principiantes, gestión de procesos"
---

## Lesson Content

El propósito principal de init es iniciar y detener procesos esenciales en el sistema. Existen tres implementaciones principales de init en Linux: System V, Upstart y systemd. En esta lección, vamos a repasar la versión más tradicional de init, System V init o Sys V (pronunciado como 'System Five').

Para averiguar si está utilizando la implementación de Sys V init, busque un archivo `/etc/inittab`; si existe, lo más probable es que esté ejecutando Sys V.

Sys V inicia y detiene procesos secuencialmente. Por ejemplo, si quisiera iniciar un servicio llamado `foo-a`, `foo-b` no podría funcionar hasta que `foo-a` ya se estuviera ejecutando. Sys V logra esto con scripts. Estos scripts inician y detienen servicios por nosotros. Podemos escribir nuestros propios scripts, o la mayoría de las veces, usar los que ya están integrados en el sistema operativo y se utilizan para cargar servicios esenciales.

Las ventajas de usar esta implementación de init son que es relativamente fácil resolver dependencias, ya que sabe que `foo-a` viene antes que `foo-b`. Sin embargo, el rendimiento no es excelente porque generalmente solo una cosa se está iniciando o deteniendo a la vez.

Al usar Sys V, el estado de la máquina se define mediante niveles de ejecución (runlevels), que se establecen de 0 a 6. Estos diferentes modos variarán según la distribución, pero la mayoría de las veces se verán como lo siguiente:

- 0: Apagado (Shutdown)
- 1: Modo de usuario único (Single User Mode)
- 2: Modo multiusuario sin red
- 3: Modo multiusuario con red
- 4: No utilizado
- 5: Modo multiusuario con red e interfaz gráfica (GUI)
- 6: Reiniciar (Reboot)

Cuando su sistema arranca, comprueba en qué nivel de ejecución se encuentra y ejecuta los scripts ubicados dentro de la configuración de ese nivel de ejecución. Los scripts se encuentran en **/etc/rc.d/rc[número de nivel de ejecución].d/** o **/etc/init.d**. Los scripts que comienzan con S (start/inicio) o K (kill/detener) se ejecutarán al inicio y al apagado, respectivamente. Los números que siguen a estos caracteres indican la secuencia en la que se ejecutan.

Por ejemplo:

```bash
pete@icebox:/etc/rc.d/rc0.d$ ls
K10updates  K80openvpn
```

Vemos que cuando cambiamos al nivel de ejecución 0 o al modo de apagado, nuestra máquina intentará ejecutar un script para detener los servicios de actualizaciones y luego OpenVPN. Para saber en qué nivel de ejecución arranca su máquina, puede ver el nivel de ejecución predeterminado en el archivo `/etc/inittab`. También puede cambiar su nivel de ejecución predeterminado en este archivo.

Una cosa a tener en cuenta: System V ha sido reemplazado en gran medida por systemd en la mayoría de las distribuciones modernas de Linux. Sin embargo, es posible que vea niveles de ejecución en otras implementaciones de init. Esto es principalmente para dar soporte a aquellos servicios que solo se inician o detienen utilizando scripts de System V init.

## Exercise

¡La práctica hace al maestro! Aquí hay algunos laboratorios prácticos para reforzar su comprensión de la gestión de procesos de Linux y la configuración del sistema, que son fundamentales para el funcionamiento de los sistemas init:

1. **[Administrar y supervisar procesos de Linux](https://labex.io/es/labs/comptia-manage-and-monitor-linux-processes-590864)** - Practique la interacción con procesos en primer plano y en segundo plano, inspeccionándolos con `ps`, supervisando recursos con `top` y terminándolos con `kill`. Esto se relaciona directamente con el aspecto de 'iniciar y detener procesos esenciales' de init.
2. **[Programar tareas con at y cron en Linux](https://labex.io/es/labs/comptia-schedule-tasks-with-at-and-cron-in-linux-590870)** - Aprenda a programar tareas únicas y recurrentes, lo que se basa en el concepto de ejecución automatizada, similar a cómo los scripts init gestionan los servicios.
3. **[Administrar permisos de archivos y directorios en Linux](https://labex.io/es/labs/comptia-manage-file-and-directory-permissions-in-linux-590844)** - Comprenda cómo administrar los permisos de archivos y directorios, una habilidad crítica para trabajar con archivos de configuración del sistema y scripts como los que se encuentran en `/etc/init.d`.

Estos laboratorios le ayudarán a aplicar los conceptos en escenarios reales y a ganar confianza con las tareas fundamentales de administración de sistemas Linux.

## Quiz Question

¿Qué nivel de ejecución se utiliza habitualmente para el apagado?

## Quiz Answer

0
