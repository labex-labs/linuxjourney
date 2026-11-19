---
lesson_id: "linux-ssh-access"
course_id: "linux-hardening"
lang: "es"
order_index: 6
title: "Acceso por SSH"
description: "Aprende a distinguir la identidad del servidor SSH, la autenticación del usuario y la política de inicio de sesión."
meta_title: "Acceso por SSH - Endurecimiento de Linux"
meta_description: "Aprende a distinguir la identidad del servidor SSH, la autenticación del usuario y la política de inicio de sesión."
meta_keywords: "acceso por SSH, endurecimiento de Linux, ciberseguridad, Linux Journey"
---

Cuando usas SSH para mantenimiento, cada extremo de la conexión tiene algo que comprobar. Tu cliente necesita identificar el servidor al que se ha conectado. El servidor necesita comprobar si la cuenta tiene permiso para iniciar sesión.

## Comprobar la identidad del servidor

Un servidor SSH presenta una **clave de anfitrión**. El cliente puede compararla con la identidad conocida de ese equipo. Si la clave cambia sin previo aviso, verifica la nueva clave mediante una fuente independiente autorizada, como el inventario de equipos o una persona del equipo de mantenimiento a través de un canal de confianza.

:::single-choice{#linux-ssh-access-unexpected-key} El cliente indica que ha cambiado la clave de anfitrión del servidor. ¿Qué debes comprobar primero?

::option[Confirmar la nueva clave de anfitrión esperada mediante una fuente de confianza.]{#linux-ssh-access-unexpected-key-b .correct explanation="Así verificas la identidad antes de confiar en la conexión."}
::option[Probar varios nombres de usuario hasta que funcione uno.]{#linux-ssh-access-unexpected-key-a explanation="El nombre de usuario no verifica la identidad del servidor."}
::option[Borrar todas las claves de anfitrión guardadas y continuar.]{#linux-ssh-access-unexpected-key-c explanation="Así perderías la información de identidad conocida antes de aclarar el cambio."}
:::

## Comprobar el acceso del usuario

Una clave de usuario permite demostrar que el cliente está autorizado a usar una cuenta. La clave de anfitrión sirve para comprobar la identidad del servidor. La política del servidor puede limitar las cuentas y los métodos de autenticación que acepta. En este ejemplo, `ops` inicia sesión mediante autenticación por clave.

:::single-choice{#linux-ssh-access-distinguish-keys} ¿Qué identidad se comprueba cuando el servidor verifica la clave de usuario de ops?

::option[El nombre de la página web pública.]{#linux-ssh-access-distinguish-keys-b explanation="El contenido web es independiente de la autenticación SSH."}
::option[La identidad del propio servidor.]{#linux-ssh-access-distinguish-keys-c explanation="El cliente usa la clave de anfitrión para esa comprobación."}
::option[La del cliente que intenta iniciar sesión como ops.]{#linux-ssh-access-distinguish-keys-a .correct explanation="La autenticación del usuario comprueba si el cliente puede usar la cuenta solicitada."}
:::

## Conservar una vía de acceso para mantenimiento

Antes de aplicar cambios autorizados a una política de SSH, acuerda las cuentas que conservarán el acceso y el método que usarán. Abre una conexión aparte para la prueba y conserva la vía de recuperación prevista hasta que el inicio de sesión funcione. Una sesión ya abierta puede mantenerse tras un cambio aunque falle un nuevo inicio de sesión.

:::single-choice{#linux-ssh-access-test-new-login} Una sesión sigue abierta tras un cambio de política. ¿Qué confirma que el personal de mantenimiento aún puede entrar?

::option[Una respuesta a ping por sí sola.]{#linux-ssh-access-test-new-login-a explanation="Una respuesta de red no demuestra que la autenticación SSH se complete correctamente."}
::option[Una nueva sesión SSH autorizada con la cuenta y el método previstos.]{#linux-ssh-access-test-new-login-c .correct explanation="Esta prueba comprueba directamente la política que se aplicará al iniciar sesión de nuevo."}
::option[Que la sesión antigua siga inactiva.]{#linux-ssh-access-test-new-login-b explanation="Esa sesión se autenticó con las condiciones anteriores."}
:::

## Resumen

Ya puedes comprobar las identidades y condiciones que intervienen en el acceso SSH para mantenimiento.

1. Verifica la identidad del servidor con su clave de anfitrión.
2. Distingue esa comprobación de la autenticación del usuario.
3. Verifica una nueva conexión autorizada tras aplicar un cambio.
