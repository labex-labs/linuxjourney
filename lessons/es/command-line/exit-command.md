---
lesson_id: "exit-command"
course_id: "command-line"
lang: "es"
order_index: 19
title: "exit"
description: "Aprende a salir de la shell actual y a elegir el estado que devuelve a quien la invocó."
meta_title: "exit - Línea de Comandos"
meta_description: "Aprende el comando exit en Linux, cómo cerrar una sesión de shell, cómo difiere logout de exit y cómo funcionan los valores de estado de salida."
meta_keywords: "comando exit, linux exit, comando logout, sesión de shell, salida de terminal, estado de salida, bash exit"
---

Las shells pueden estar anidadas: una terminal gráfica inicia una shell, una conexión SSH inicia una shell remota y una shell puede iniciar otra. Al salir de una, normalmente se devuelve el control a aquello que inició la shell actual.

## Salida de la shell actual

La forma más común de terminar una sesión de shell es con el comando `exit`. Cuando escribes `exit` y presionas Enter, el proceso actual del shell termina. Este comando funciona en prácticamente cualquier entorno de shell.

```bash
$ exit
```

Si esa shell es el proceso principal de una pestaña de terminal gráfica, la pestaña puede cerrarse según la configuración de la terminal. En una sesión SSH, salir de la shell remota normalmente te devuelve a la shell local. Si iniciaste una shell anidada, `exit` vuelve a la shell padre.

:::single-choice{#leave-current-shell} Has iniciado Bash dentro de otra shell y quieres volver a la shell padre. ¿Qué orden debes ejecutar en la sesión anidada de Bash?

::option[`clear`]{#clear-nested explanation="`clear` renueva el área visible de la terminal, pero deja en ejecución la shell actual."}
::option[`exit`]{#exit-nested .correct explanation="`exit` termina la shell actual y permite que se reanude la shell padre."}
::option[`history -c`]{#clear-nested-history explanation="Esta orden vacía la lista del historial de Bash en memoria. No termina la shell actual."}
:::

## Devolución de un estado de salida

El comando `exit` también puede devolver un código de estado. Un estado de `0` usualmente significa éxito, y un estado distinto de cero generalmente indica un error o una condición especial.

```bash
$ exit 0
```

Por convención, `0` significa éxito y un valor distinto de cero representa un fallo u otra condición definida por el programa. Si Bash no recibe un argumento numérico, sale con el estado de la última orden ejecutada antes de `exit`.

:::single-choice{#return-success-status} ¿Qué orden termina la shell actual e informa explícitamente de un resultado satisfactorio a quien la invocó?

::option[`exit 0`]{#exit-zero .correct explanation="El estado `0` indica por convención que la ejecución ha finalizado correctamente."}
::option[`exit 1`]{#exit-one explanation="Un estado distinto de cero suele indicar un fallo u otro resultado excepcional, no un éxito."}
::option[`logout 0`]{#logout-zero explanation="La orden integrada `logout` de Bash se utiliza con una shell de inicio de sesión y no adopta esta forma para establecer el estado solicitado."}
:::

:::single-choice{#exit-without-number} En Bash, ¿qué estado devuelve `exit` cuando no se proporciona ningún número?

::option[Siempre devuelve el estado satisfactorio `0`.]{#always-zero explanation="La convención del éxito no obliga a que un `exit` sin argumentos devuelva cero. En este caso, Bash conserva un estado anterior."}
::option[Siempre devuelve el estado de fallo `1`.]{#always-one explanation="Bash no asigna el estado de fallo `1` a todos los `exit` sin argumentos. La orden anterior determina el valor."}
::option[Devuelve el estado de salida de la orden anterior.]{#last-command-status .correct explanation="Sin un argumento numérico explícito, Bash sale con el estado de la orden más reciente."}
:::

## Uso de logout en una shell de inicio de sesión

```bash
$ logout
```

En una shell de Bash que no sea de inicio de sesión, `logout` informa de que no se trata de una shell de inicio; utiliza `exit` en su lugar.

:::single-choice{#leave-login-shell} ¿Qué orden integrada de Bash está pensada específicamente para salir de una shell de inicio de sesión?

::option[`logout`]{#logout-login .correct explanation="Bash proporciona `logout` para terminar una shell de inicio de sesión."}
::option[`unalias`]{#unalias-login explanation="`unalias` elimina definiciones de alias de la shell actual. No termina la sesión."}
::option[`source`]{#source-login explanation="`source` lee órdenes de un archivo en la shell actual. No termina esa shell."}
:::

## Uso de Ctrl+D o cierre de una terminal

En un prompt interactivo vacío, pulsar `Ctrl+D` normalmente proporciona el carácter de fin de archivo de la terminal. Bash suele interpretar esta condición como una solicitud para salir. No es una señal, y opciones de la shell como `ignoreeof` pueden cambiar el comportamiento.

Cerrar una ventana de terminal gráfica solicita a la aplicación que cierre sus procesos y puede afectar a los trabajos en ejecución. Cuando resulte práctico, prefiere una salida ordenada con `exit` y comprueba si hay trabajo activo antes de cerrar la sesión.

## Resumen

Ahora puedes salir de la shell actual y comunicar su estado de finalización.

1. Utilizar `exit` para devolver el control a quien invocó la shell actual.
2. Proporcionar `0` para indicar éxito u otro estado distinto de cero con un significado definido.
3. Comprender el estado que utiliza un `exit` sin argumentos.
4. Utilizar `logout` únicamente con una shell de inicio de sesión.
5. Reconocer `Ctrl+D` como una entrada de fin de archivo, no como una señal.
