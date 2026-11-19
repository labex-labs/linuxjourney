---
lesson_id: "sudo-events"
course_id: "security-logs"
lang: "es"
order_index: 3
title: "Eventos de sudo"
description: "Aprende a reconocer qué cuenta solicitó un comando, con qué cuenta quería ejecutarlo y si sudo lo permitió."
meta_title: "Eventos de sudo - Registros de seguridad"
meta_description: "Lee entradas de sudo y distingue la cuenta solicitante, la cuenta de destino, el comando y la decisión de autorización."
meta_keywords: "eventos de sudo, registros de sudo, autorización, cuenta de destino, permisos de Linux"
---

Una persona puede iniciar sesión con una cuenta normal y luego necesitar más permisos para alguna tarea. Si el sistema usa `sudo`, puede pedir que se ejecute un comando con otra cuenta. El registro de la solicitud puede indicar qué permisos se pidieron y qué decidió el sistema.

## Identificar las dos cuentas

Los registros simulados usan `account` para la cuenta que hace la solicitud y `target` para la cuenta con la que se ejecutaría el comando. La cuenta `root` tiene privilegios de administración. Una solicitud mediante `sudo` también puede indicar otra cuenta de destino, como `backup`.

```text
t=09:15:10Z source=sudo host=web-01 account=alex target=root
command=systemctl status nginx decision=allowed session=42
```

La segunda línea continúa la misma entrada. Aquí, `alex` pidió ejecutar el comando como `root`.

:::single-choice{#sudo-events-account-target} En un registro con `account=sam target=backup`, ¿qué cuenta hizo la solicitud y con cuál pidió ejecutar el comando?

::option[Backup solicitó ejecutarlo como sam.]{#sudo-events-target-swapped explanation="Account identifica la cuenta que hizo la solicitud. Target indica con qué cuenta se ejecutaría el comando."}
::option[Sam solicitó ejecutarlo como backup.]{#sudo-events-target-backup .correct explanation="Account identifica a quien lo solicita y target a la cuenta que usaría el comando."}
::option[Sam solicitó ejecutarlo como root.]{#sudo-events-target-root explanation="Root es una cuenta de destino posible. En esta entrada aparece backup."}
:::

## Leer el comando solicitado

El campo `command` indica qué comando se solicitó. En el ejemplo, `systemctl status nginx` pide mostrar el estado actual del servicio web Nginx. Otra entrada podría mostrar `systemctl restart nginx`, una solicitud para detener y volver a iniciar ese servicio. Ambas se refieren al mismo servicio y piden acciones diferentes.

:::single-choice{#sudo-events-command-scope} ¿Qué solicitud pide cambiar el estado del servicio web?

::option[`systemctl restart nginx`]{#sudo-events-command-restart .correct explanation="Restart solicita detener el servicio y volver a iniciarlo. Puede cambiar su estado."}
::option[`systemctl status nginx`]{#sudo-events-command-status explanation="Status solicita información sobre el servicio. No pide reiniciarlo."}
::option[Cualquiera de las dos, porque ambas mencionan nginx.]{#sudo-events-command-both explanation="El nombre del servicio es el mismo. La acción indica lo que se pidió."}
:::

## Leer la decisión

La **política** es el conjunto de reglas que `sudo` usa para aceptar o rechazar una solicitud. En estos ejemplos, `decision=allowed` indica que la política autorizó la solicitud. `decision=denied` significa que `sudo` la rechazó.

```text
t=09:16:00Z source=sudo host=web-01 account=alex target=root
command=systemctl restart nginx decision=denied session=42
```

Una autorización indica que había permiso. Si necesitas saber cómo terminó el comando, busca el registro del resultado, si el sistema ofrece uno.

![Terminal de LabEx con registros simulados de sudo que muestran una consulta de estado permitida y un reinicio rechazado](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/security-logs/sudo-events/sudo-decisions.png)

Compara los comandos y las decisiones de estos dos registros simulados.

:::single-choice{#sudo-events-denied-request} ¿Qué dice el segundo ejemplo sobre la solicitud de reinicio?

::option[Sudo rechazó la solicitud de reinicio.]{#sudo-events-denied-refused .correct explanation="El comando indica qué acción se pidió. Denied muestra que se denegó la autorización."}
::option[El servicio se reinició correctamente.]{#sudo-events-denied-success explanation="La entrada registra una denegación. No hay pruebas de un reinicio correcto."}
::option[También se rechazó la consulta de estado anterior.]{#sudo-events-denied-earlier explanation="Cada decisión corresponde a su propia solicitud. La anterior dice allowed."}
:::

## Tener en cuenta la cuenta de inicio de sesión

Los dos ejemplos indican que `alex` hizo la solicitud e incluyen `session=42`. El número identifica la sesión, que es el periodo de actividad posterior al inicio de sesión. Te ayuda a encontrar los registros de inicio relacionados. En cada ejemplo, la cuenta de destino se refiere a esa solicitud concreta. Para describirla, ten en cuenta ambas cuentas.

:::single-choice{#sudo-events-session-interpretation} ¿Qué resumen encaja con el primer ejemplo?

::option[Root inició sesión directamente y abrió la sesión 42.]{#sudo-events-session-root-login explanation="Es un registro de sudo. La cuenta de destino no indica otro inicio de sesión."}
::option[Alex pidió permisos de root para todos los comandos de la sesión.]{#sudo-events-session-all-commands explanation="La entrada indica un solo comando. No cubre todos los de la sesión."}
::option[Alex pidió ejecutar un comando concreto como root en la sesión 42.]{#sudo-events-session-one-command .correct explanation="Los campos de cuenta solicitante, cuenta de destino, comando y sesión permiten afirmar eso."}
:::

## Resumen

Ya puedes leer un registro de sudo y distinguir la decisión de autorización del resultado del comando.

1. Identificar las cuentas solicitante y de destino.
2. Usar el campo del comando para describir la solicitud concreta.
3. Distinguir una solicitud autorizada de una rechazada.
4. Tener en cuenta la sesión al describir la solicitud.
