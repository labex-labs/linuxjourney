---
lesson_id: "ssh-login-events"
course_id: "security-logs"
lang: "es"
order_index: 2
title: "Inicios de sesión por SSH"
description: "Aprende a leer los resultados de intentos aceptados y rechazados, y a agrupar los que pertenecen a una misma conexión."
meta_title: "Inicios de sesión por SSH - Registros de seguridad"
meta_description: "Lee la cuenta, la dirección remota, el método de autenticación y el resultado. Identifica qué intentos pertenecen a la misma conexión."
meta_keywords: "inicios de sesión SSH, registros SSH, inicio de sesión aceptado, inicio de sesión rechazado, autenticación"
---

**SSH**, abreviatura de Secure Shell, permite iniciar sesión en otro equipo a través de una red. El equipo que recibe la conexión puede registrar cada intento. Sus registros indican qué cuenta se presentó y si el servidor aceptó la prueba de autenticación.

## Leer el resultado

Aquí tienes dos registros simulados de SSH. El campo `login` indica el resultado. Un intento rechazado no pasó la comprobación de inicio de sesión. Un intento aceptado sí la pasó.

```text
t=09:13:48Z source=ssh host=web-01 account=alex login=rejected
t=09:14:02Z source=ssh host=web-01 account=alex login=accepted
```

La primera entrada registra un rechazo para `alex`. La segunda muestra un intento aceptado para la misma cuenta. Cada resultado corresponde a su propio intento.

:::single-choice{#ssh-login-events-outcome-order} ¿Qué afirmación se desprende de estos dos registros?

::option[El intento más reciente pasó la comprobación.]{#ssh-login-events-outcome-later .correct explanation="La segunda entrada muestra login=accepted a las 09:14:02."}
::option[Los dos intentos pasaron la comprobación.]{#ssh-login-events-outcome-both explanation="La primera línea registra un intento rechazado."}
::option[El intento más reciente no pasó la comprobación.]{#ssh-login-events-outcome-failed explanation="El intento rechazado fue el primero. El segundo fue aceptado."}
:::

## Leer direcciones y métodos de autenticación

La dirección remota indica desde dónde llegó la conexión al equipo receptor. En este ejemplo, aparece en `peer`. Una dirección de red puede ser compartida, así que ese dato por sí solo no identifica a la persona que la utilizó.

```text
t=09:14:02Z source=ssh host=web-01 account=alex login=accepted
peer=192.0.2.10 method=publickey connection=17
```

La segunda línea continúa la misma entrada. El campo `method` especifica qué prueba comprobó SSH. `password` indica que comprobó una contraseña. `publickey` indica que el equipo que se conectó demostró que podía usar una clave que el servidor acepta para esa cuenta.

:::single-choice{#ssh-login-events-method-evidence} ¿Qué puedes afirmar sobre el intento aceptado?

::option[El servidor aceptó un inicio de sesión con contraseña.]{#ssh-login-events-method-password explanation="El método de contraseña se indicaría por separado. Aquí figura el método de clave pública."}
::option[El servidor identificó a la persona que usaba esa dirección.]{#ssh-login-events-method-person explanation="La dirección describe cómo vio la conexión el equipo receptor. No demuestra quién estaba delante del teclado."}
::option[El servidor aceptó un inicio de sesión con clave.]{#ssh-login-events-method-key .correct explanation="La entrada contiene login=accepted y method=publickey."}
:::

## Agrupar intentos por conexión

Una **conexión** es el enlace de red que usa SSH para intercambiar mensajes. En estos ejemplos, el equipo asigna un identificador a cada conexión. En una misma conexión puede haber varios intentos. También se pueden abrir nuevas conexiones desde la misma dirección.

```text
t=09:13:48Z host=web-01 account=alex peer=192.0.2.10 connection=17 login=rejected
t=09:13:55Z host=web-01 account=alex peer=192.0.2.10 connection=18 login=rejected
t=09:14:02Z host=web-01 account=alex peer=192.0.2.10 connection=17 login=accepted
```

En `web-01`, la primera y la última entrada comparten la conexión 17. Lee el identificador junto con el nombre del equipo.

![Terminal de LabEx con intentos simulados de SSH desde una dirección y los identificadores de conexión 17 y 18](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/security-logs/ssh-login-events/ssh-connections.png)

La terminal muestra juntos los tres intentos simulados para que puedas comparar sus números de conexión.

:::single-choice{#ssh-login-events-group-connection} ¿Qué entradas se refieren a la conexión 18 en web-01?

::option[Los intentos de las 09:13:48 y las 09:14:02.]{#ssh-login-events-group-seventeen explanation="Ambas filas tienen el número de conexión 17."}
::option[Solo el intento de las 09:13:55.]{#ssh-login-events-group-eighteen .correct explanation="Solo esta fila muestra la conexión 18 en web-01."}
::option[Los tres intentos desde 192.0.2.10.]{#ssh-login-events-group-address explanation="En una misma dirección aparecen dos números de conexión."}
:::

## Seguir un inicio de sesión aceptado

Un inicio de sesión correcto indica que SSH aceptó la prueba de autenticación de esa cuenta. Para saber qué pasó después, busca un registro de apertura de **sesión**. La sesión abarca la actividad posterior al inicio de sesión. Un registro de inicio correcto, por sí solo, describe únicamente la comprobación de autenticación.

:::single-choice{#ssh-login-events-after-accepted} ¿Qué registro te ayudaría a saber si un intento aceptado dio lugar a una sesión abierta?

::option[Otro registro que confirme que se aceptó el mismo intento.]{#ssh-login-events-after-accepted-again explanation="Solo repetiría el resultado de la comprobación."}
::option[Un rechazo anterior de la cuenta en otro equipo.]{#ssh-login-events-after-other-host explanation="Ese registro corresponde a otro intento en otro equipo."}
::option[Un registro de apertura de sesión vinculado a ese inicio.]{#ssh-login-events-after-session .correct explanation="El registro describe lo que sucedió después y puede vincularse al intento aceptado."}
:::

## Resumen

Ya puedes leer el resultado de un intento de SSH y comprobar qué registros corresponden a la misma conexión.

1. Distinguir un intento aceptado de uno rechazado.
2. Describir el intento con la dirección remota y el método de autenticación.
3. Agrupar por equipo y conexión cuando haya identificadores.
4. Buscar un registro de sesión para saber qué ocurrió después de un inicio correcto.
