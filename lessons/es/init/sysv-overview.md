---
lesson_id: "sysv-overview"
course_id: "init"
lang: "es"
order_index: 1
title: "Visión general de System V"
description: "Aprende cómo el init tradicional de System V utiliza niveles de ejecución y enlaces ordenados a scripts de servicios."
meta_title: "Visión general de System V - Init"
meta_description: "Comprende el init de System V, sus niveles de ejecución y los enlaces ordenados que inician y detienen servicios."
meta_keywords: "System V, SysV init, sysvinit, niveles de ejecución Linux, scripts init, PID 1"
---

System V init, llamado normalmente SysV init o sysvinit, es un diseño tradicional de PID 1 e inicio de servicios. Sigue siendo importante en sistemas heredados y mediante scripts de compatibilidad, pero la presencia de archivos de estilo SysV no demuestra que sysvinit sea el PID 1 en ejecución.

## Identificar el sistema init activo

Examina el PID 1 activo:

```bash
$ ps -p 1 -o pid,comm,args=
$ readlink /proc/1/exe
```

Un archivo `/etc/inittab` o un directorio `/etc/init.d/` es solo una prueba auxiliar. systemd y otros sistemas pueden conservar estos archivos por compatibilidad, y los contenedores pueden mostrar un espacio de nombres de PID distinto del anfitrión.

:::single-choice{#sysv-overview-detection} ¿Cuál es la prueba más sólida de que sysvinit está activo?

::option[Que el ejecutable activo con PID 1 sea sysvinit o su programa init.]{#sysv-overview-live-pid-one .correct explanation="Examinar el primer proceso en ejecución es más directo que deducirlo de archivos de compatibilidad."}
::option[Que exista un directorio `/etc/init.d/`.]{#sysv-overview-init-d-only explanation="Otros sistemas init suelen conservar scripts o envoltorios de SysV."}
::option[Que la descripción de un paquete contenga la palabra servicio.]{#sysv-overview-package-word explanation="El texto de un paquete no identifica el proceso que actúa en ese momento como PID 1."}
:::

## Niveles de ejecución

Un nivel de ejecución es un modo de funcionamiento numérico con nombre. Las configuraciones de SysV utilizan tradicionalmente los niveles `0` a `6` más niveles especiales, pero sus significados son una política de la distribución, no una ley universal. Entre las convenciones habituales se encuentran:

- `0`: transición de detención o apagado
- `1` o `S`: modo monousuario o de rescate
- `2` a `5`: modos multiusuario definidos por la distribución
- `6`: transición de reinicio

Los sistemas de la familia Debian han tratado históricamente los niveles 2–5 de forma parecida, mientras que las convenciones de la familia Red Hat distinguen modos de texto y gráficos. Examina `/etc/inittab`, la documentación de init y los directorios de niveles en el equipo real.

:::single-choice{#sysv-overview-shutdown-runlevel} ¿Qué nivel solicita convencionalmente detener o apagar en muchos sistemas SysV?

::option[`3`]{#sysv-overview-runlevel-three explanation="Suele ser un modo multiusuario y no de apagado."}
::option[`0`]{#sysv-overview-runlevel-zero .correct explanation="El nivel cero es convencionalmente la transición de apagado, aunque la política local sigue siendo la autoridad."}
::option[`6`]{#sysv-overview-runlevel-six explanation="El nivel seis solicita convencionalmente reiniciar."}
:::

## Scripts init y enlaces de niveles

Los scripts de servicios suelen residir bajo `/etc/init.d/`. Los directorios de niveles como `/etc/rc2.d/` o `/etc/rc.d/rc2.d/` contienen enlaces cuyos nombres codifican la acción y el orden de la transición:

- Los enlaces `SNNname` solicitan una acción de inicio.
- Los enlaces `KNNname` solicitan una acción de detención.
- `NN` proporciona el orden lexicográfico entre enlaces de esa transición.

El algoritmo y los directorios exactos varían. Las dependencias también pueden expresarse en las cabeceras de los scripts y procesarse mediante herramientas de la distribución, y algunas implementaciones paralelizan el trabajo. SysV no debe reducirse a la garantía de que todos los servicios se inicien estrictamente de uno en uno.

:::single-choice{#sysv-overview-start-link} ¿Qué solicita convencionalmente un enlace `S20networking` al entrar en un nivel?

::option[Enviar directamente la señal 20 a todos los procesos de red.]{#sysv-overview-signal-twenty explanation="Los dígitos son metadatos de orden, no un número de señal."}
::option[Almacenar veinte copias de seguridad de la configuración de red.]{#sysv-overview-twenty-backups explanation="Los enlaces de niveles no proporcionan retención de copias."}
::option[Ejecutar el script de servicio enlazado con su acción start en el orden `S`.]{#sysv-overview-start-action .correct explanation="El prefijo distingue los enlaces de inicio y el número contribuye a la secuencia."}
:::

## Transiciones entre niveles

Cuando init cambia de nivel, la maquinaria rc de la distribución detiene los servicios que ya no se necesitan e inicia los necesarios en el nuevo modo. Los scripts deben ser suficientemente idempotentes para admitir operaciones repetidas de estado o transición y devolver estados significativos.

Solicitar los niveles 0 o 6 es una acción destructiva para la disponibilidad de todo el sistema. Utiliza la interfaz de apagado, avisa a los usuarios, conserva el trabajo activo y verifica el acceso remoto a consola en vez de invocar casualmente transiciones init sin intermediarios.

:::single-choice{#sysv-overview-runlevel-six-meaning} ¿Qué solicita convencionalmente el nivel `6`?

::option[Crear seis cuentas de usuario adicionales.]{#sysv-overview-six-users explanation="Los niveles describen modos de funcionamiento, no números de cuentas."}
::option[Una transición de reinicio del sistema.]{#sysv-overview-reboot .correct explanation="La política SysV clásica reserva el nivel seis para detener servicios y reiniciar el sistema."}
::option[Montar para siempre todos los sistemas de archivos como solo lectura.]{#sysv-overview-six-readonly explanation="Esa no es la finalidad convencional del nivel seis."}
:::

## Límites de la compatibilidad

En un equipo con systemd, los scripts SysV pueden envolverse como unidades generadas, pero siguen aplicándose las dependencias, los tiempos de espera, el registro y la semántica de estado de systemd. Ejecutar directamente un script heredado puede eludir el seguimiento del gestor de servicios. Identifica el gestor activo y utiliza su interfaz nativa cuando sea posible.

:::single-choice{#sysv-overview-compatibility-script} ¿Por qué debe invocarse normalmente un script de estilo SysV de un equipo systemd mediante el gestor de servicios?

::option[Porque ejecutarlo directamente puede eludir el seguimiento de dependencias y estado.]{#sysv-overview-manager-tracking .correct explanation="El gestor debe coordinar la propiedad de procesos, el orden, los tiempos de espera y el estado."}
::option[Porque los scripts de shell no pueden ejecutarse en un sistema systemd.]{#sysv-overview-scripts-impossible explanation="Pueden ejecutarse, pero eludir la supervisión puede provocar un estado incoherente."}
::option[Porque systemd convierte todos los scripts de servicios en módulos del kernel.]{#sysv-overview-script-module explanation="Las unidades de compatibilidad siguen siendo gestión de servicios del espacio de usuario."}
:::

## Resumen

Ahora puedes interpretar un diseño SysV tradicional sin suponer que esté activo.

1. Identifica el PID 1 activo antes de elegir órdenes de init.
2. Trata los significados de los niveles como convenciones definidas por la distribución.
3. Lee `S`, `K` y el orden numérico de los enlaces de niveles.
4. Utiliza procedimientos controlados de apagado para los niveles 0 y 6.
5. Respeta el gestor activo cuando existan scripts de compatibilidad.
