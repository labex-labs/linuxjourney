---
lesson_id: "sysv-services"
course_id: "init"
lang: "es"
order_index: 2
title: "Servicio de System V"
description: "Aprende a inspeccionar y operar scripts de servicios SysV antiguos mediante el mecanismo compatible del sistema activo."
meta_title: "Servicio de System V - Init"
meta_description: "Aprende a gestionar servicios tradicionales de System V (SysV) en Linux. Esta guía explica cómo usar el comando `service` para listar, iniciar, detener y reiniciar servicios en un sistema de inicio System V."
meta_keywords: "system v, sysv init, servicios linux, comando service, gestionar servicios linux, iniciar servicio, detener servicio, reiniciar servicio, linux system v"
---

Los servicios SysV suelen estar representados por scripts ejecutables bajo `/etc/init.d/`. Un script acepta acciones como `start`, `stop`, `restart` o `status` según su implementación y las convenciones de la distribución. El comando `service` proporciona un mecanismo que ejecuta un script determinado en un entorno más controlado.

## Descubrir servicios y acciones

Primero, lista los nombres de los scripts:

```bash
$ ls -1 /etc/init.d/
```

Algunas implementaciones ofrecen:

```bash
$ service --status-all
```

Sus indicadores entre corchetes y sus estados de salida dependen de la implementación, y un script puede informar que el estado es desconocido. Para un servicio concreto, consulta la salida de uso del script o su documentación en lugar de suponer que todas las acciones están disponibles.

:::single-choice{#sysv-services-wrapper-purpose} ¿Qué suele ejecutar el comando `service`?

::option[Un editor de particiones de disco que procesa cada archivo de servicio.]{#sysv-services-partition-editor explanation="El control de servicios no está relacionado con el particionamiento del almacenamiento."}
::option[Una llamada al sistema del kernel añadida dinámicamente por el script.]{#sysv-services-new-syscall explanation="Los scripts de inicio son programas de espacio de usuario que controlan procesos."}
::option[Un script de inicio determinado y una de las acciones que admite.]{#sysv-services-script-action .correct explanation="El mecanismo localiza un script de servicio antiguo y lo invoca con un entorno normalizado."}
:::

## Iniciar y detener

En una máquina gestionada realmente por SysV, estas formas son habituales:

```bash
$ sudo service SERVICE_NAME start
$ sudo service SERVICE_NAME stop
```

Sustituye el marcador solo después de identificar el servicio, sus dependientes, su estado actual y el impacto operativo. Detener la red, el acceso remoto, el almacenamiento o la autenticación desde una sesión remota puede dejarte sin acceso o dañar el trabajo activo.

La forma directa `/etc/init.d/SERVICE_NAME ACTION` puede existir, pero, si el gestor activo de la máquina proporciona compatibilidad, usa el comando orientado a ese gestor para que pueda registrar el estado y las dependencias.

:::single-choice{#sysv-services-stop-peanut} ¿Qué comando solicita que se detenga el servicio SysV `peanut`?

::option[`sudo service stop peanut`]{#sysv-services-stop-first explanation="El orden convencional de los operandos coloca el nombre del servicio antes de la acción."}
::option[`sudo stop --partition peanut`]{#sysv-services-partition-stop explanation="Esta no es la sintaxis del mecanismo de servicios SysV."}
::option[`sudo service peanut stop`]{#sysv-services-peanut-stop .correct explanation="El mecanismo recibe el nombre del servicio seguido de la acción de detención solicitada."}
:::

## Recargar, reiniciar y consultar el estado

Normalmente, `restart` detiene un servicio y después lo inicia, lo que provoca una interrupción. `reload` puede pedirle que vuelva a leer su configuración sin reiniciarlo por completo, pero solo cuando tanto el script como el demonio lo admiten. Algunos scripts ofrecen `force-reload`, cuyo comportamiento alternativo lo define la distribución.

Valida la configuración antes de recargar o reiniciar, conserva una segunda conexión administrativa cuando modifiques el acceso remoto y comprueba después el servicio mediante su punto de acceso real y sus registros, no solo mediante un estado que indique «en ejecución».

```bash
$ sudo service SERVICE_NAME status
$ sudo service SERVICE_NAME reload
```

:::single-choice{#sysv-services-reload-versus-restart} ¿Por qué no se debe suponer que `reload` equivale a `restart`?

::option[La recarga siempre apaga todo el sistema operativo.]{#sysv-services-reload-shutdown explanation="Ese no es el significado habitual de la acción de recarga de un servicio."}
::option[El reinicio solo muestra la configuración y nunca cambia el estado del proceso.]{#sysv-services-restart-readonly explanation="Reiniciar suele detener e iniciar el servicio."}
::option[La recarga depende del servicio y puede volver a leer la configuración sin detener el proceso.]{#sysv-services-reload-specific .correct explanation="La compatibilidad y el significado pertenecen al script de inicio y al demonio, mientras que reiniciar normalmente interrumpe el ciclo de vida."}
:::

## Control durante la ejecución frente a habilitación al arrancar

Iniciar un servicio ahora no necesariamente lo habilita para futuros niveles de ejecución. La habilitación al arrancar se representa mediante enlaces de niveles de ejecución y se gestiona con herramientas específicas de la distribución como `update-rc.d`, `chkconfig` o generadores de compatibilidad del gestor de servicios.

No crees manualmente enlaces `S` y `K` hasta comprender los metadatos de dependencias y la herramienta de gestión de la distribución; los enlaces manuales pueden sobrescribirse o quedar en un orden incorrecto.

:::single-choice{#sysv-services-start-versus-enable} ¿Ejecutar `service SERVICE start` habilita necesariamente el servicio para futuros arranques?

::option[Sí; cada acción de inicio crea automáticamente todos los enlaces de niveles de ejecución.]{#sysv-services-start-links explanation="El mecanismo no cambia de forma universal la habilitación persistente."}
::option[No; el estado durante la ejecución y la habilitación en niveles de ejecución son independientes.]{#sysv-services-runtime-separate .correct explanation="Los enlaces de arranque o la política del gestor determinan la activación futura con independencia de que el proceso se inicie ahora."}
::option[Sí; un PID en ejecución se almacena permanentemente en el sector de arranque.]{#sysv-services-pid-boot-sector explanation="Los PID son identificadores de ejecución y no metadatos de habilitación al arrancar."}
:::

## Resumen

Ahora puedes operar un servicio antiguo sin confundir el control durante la ejecución con la política de arranque.

1. Descubre el script real y las acciones que admite.
2. En la sintaxis del mecanismo, coloca el nombre del servicio antes de la acción.
3. Valida y comprueba el comportamiento de recarga o reinicio.
4. Gestiona la habilitación futura en niveles de ejecución mediante las herramientas de la distribución.
