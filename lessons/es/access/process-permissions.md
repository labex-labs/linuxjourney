---
lang: "es"
title: "Permisos de Proceso"
description: "Aprende sobre los permisos de proceso de Linux, incluyendo los IDs de Usuario Real, Efectivo y Guardado. Comprende cómo los UIDs impactan la seguridad y la ejecución de comandos. ¡Empieza a aprender hoy mismo!"
keywords: "permisos de proceso de Linux, UID real, UID efectivo, UID guardado, seguridad de Linux, comando passwd, tutorial de Linux, Linux para principiantes"
---

## Lesson Content

Pasemos un poco a los permisos de proceso. ¿Recuerdas que te dije que cuando ejecutas el comando `passwd` con el bit de permiso SUID habilitado, ejecutarás el programa como root? Eso es cierto. Sin embargo, ¿significa eso que, dado que eres temporalmente root, puedes modificar las contraseñas de otros usuarios? ¡No, afortunadamente no!

Esto se debe a los muchos UIDs que implementa Linux. Hay tres UIDs asociados con cada proceso:

Cuando inicias un proceso, se ejecuta con los mismos permisos que el usuario o grupo que lo ejecutó. Esto se conoce como **ID de usuario efectivo**. Este UID se utiliza para otorgar derechos de acceso a un proceso. Así, naturalmente, si Bob ejecutó el comando `touch`, el proceso se ejecutaría como él, y cualquier archivo que creara estaría bajo su propiedad.

Hay otro UID, llamado **ID de usuario real**. Este es el ID del usuario que inició el proceso. Estos se utilizan para rastrear quién es el usuario que inició el proceso.

Un último UID es el **ID de usuario guardado**. Esto permite que un proceso cambie entre el UID efectivo y el UID real, y viceversa. Esto es útil porque no queremos que nuestro proceso se ejecute con privilegios elevados todo el tiempo; es una buena práctica usar privilegios especiales en momentos específicos.

Ahora unamos todo esto observando el comando `passwd` una vez más.

Al ejecutar el comando `passwd`, tu UID efectivo es tu ID de usuario; digamos que es 500 por ahora. Oh, pero espera, recuerda que el comando `passwd` tiene el permiso SUID habilitado. Así que cuando lo ejecutas, tu UID efectivo es ahora 0 (0 es el UID de root). Ahora este programa puede acceder a archivos como root.

Digamos que te da un poco de poder y quieres modificar la contraseña de Sally. Sally tiene un UID de 600. Bueno, no tendrás suerte. Afortunadamente, el proceso también tiene tu UID real, en este caso 500. Sabe que tu UID es 500 y, por lo tanto, no puedes modificar la contraseña del UID 600. (Esto, por supuesto, siempre se elude si eres un superusuario en una máquina y puedes controlar y cambiar todo).

Dado que ejecutaste `passwd`, iniciará el proceso utilizando tu UID real y guardará el UID del propietario del archivo (UID efectivo), para que puedas cambiar entre los dos. No es necesario modificar todos los archivos con acceso de root si no es necesario.

La mayoría de las veces, el UID real y el UID efectivo son los mismos, pero en casos como el comando `passwd`, cambiarán.

## Exercise

Todavía no hemos hablado de procesos, pero aún podemos ver este cambio en tiempo real:

1. Abre una ventana de terminal y ejecuta el comando: `watch -n 1 "ps aux | grep passwd"`. Esto observará el proceso `passwd`.
2. Abre una segunda ventana de terminal y ejecuta: `passwd`.
3. Mira la primera ventana de terminal; verás que aparece un proceso para `passwd`. La primera columna en la tabla de procesos es el ID de usuario efectivo. ¡Y he aquí, es el usuario root!

## Quiz Question

¿Qué UID decide qué acceso otorgar?

## Quiz Answer

effective
