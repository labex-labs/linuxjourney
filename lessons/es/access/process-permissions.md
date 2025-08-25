---
index: 7
lang: "es"
title: "Permisos de proceso"
meta_title: "Permisos de proceso - Permisos"
meta_description: "Aprende sobre los permisos de proceso de Linux, incluyendo los ID de usuario reales, efectivos y guardados. Comprende cómo los UIDs impactan la seguridad y la ejecución de comandos. ¡Empieza a aprender hoy mismo!"
meta_keywords: "permisos de proceso de Linux, UID real, UID efectivo, UID guardado, seguridad de Linux, comando passwd, tutorial de Linux, Linux para principiantes"
---

## Lesson Content

Pasemos un momento a los permisos de proceso. ¿Recuerdas que te dije que cuando ejecutas el comando `passwd` con el bit de permiso SUID habilitado, ejecutarás el programa como root? Eso es cierto. Sin embargo, ¿significa eso que, dado que eres temporalmente root, puedes modificar las contraseñas de otros usuarios? ¡No, afortunadamente no!

Esto se debe a los muchos UIDs que Linux implementa. Hay tres UIDs asociados con cada proceso:

Cuando inicias un proceso, se ejecuta con los mismos permisos que el usuario o grupo que lo ejecutó. Esto se conoce como **ID de usuario efectivo**. Este UID se utiliza para otorgar derechos de acceso a un proceso. Así que, naturalmente, si Bob ejecutó el comando `touch`, el proceso se ejecutaría como él, y cualquier archivo que creara sería de su propiedad.

Hay otro UID, llamado **ID de usuario real**. Este es el ID del usuario que inició el proceso. Estos se utilizan para rastrear quién es el usuario que inició el proceso.

Un último UID es el **ID de usuario guardado**. Esto permite que un proceso cambie entre el UID efectivo y el UID real, y viceversa. Esto es útil porque no queremos que nuestro proceso se ejecute con privilegios elevados todo el tiempo; es una buena práctica usar privilegios especiales en momentos específicos.

Ahora vamos a unir todo esto observando el comando `passwd` una vez más.

Al ejecutar el comando `passwd`, tu UID efectivo es tu ID de usuario; digamos que es 500 por ahora. Oh, pero espera, recuerda que el comando `passwd` tiene el permiso SUID habilitado. Así que cuando lo ejecutas, tu UID efectivo ahora es 0 (0 es el UID de root). Ahora este programa puede acceder a archivos como root.

Digamos que pruebas un poco de poder y quieres modificar la contraseña de Sally. Sally tiene un UID de 600. Bueno, no tendrás suerte. Afortunadamente, el proceso también tiene tu UID real, en este caso 500. Sabe que tu UID es 500 y, por lo tanto, no puedes modificar la contraseña del UID 600. (Esto, por supuesto, siempre se omite si eres un superusuario en una máquina y puedes controlar y cambiar todo).

Dado que ejecutaste `passwd`, iniciará el proceso usando tu UID real y guardará el UID del propietario del archivo (UID efectivo), para que puedas cambiar entre los dos. No es necesario modificar todos los archivos con acceso de root si no es necesario.

La mayoría de las veces, el UID real y el UID efectivo son los mismos, pero en casos como el comando `passwd`, cambiarán.

## Exercise

¡La práctica hace al maestro! Comprender los ID de usuario y los permisos de proceso es crucial para la seguridad y administración de Linux. Aquí hay algunos laboratorios prácticos para reforzar tu comprensión de la gestión de usuarios y grupos, que forma la base de cómo funcionan los UIDs:

1. **[Grupo de usuarios de Linux y permisos de archivo](https://labex.io/es/labs/linux-linux-user-group-and-file-permissions-18002)** - Aprende conceptos esenciales de gestión de usuarios y grupos de Linux, incluyendo la creación y gestión de usuarios, la exploración de membresías de grupo, la comprensión de los permisos de archivo y la manipulación de la propiedad de los archivos. Este laboratorio proporciona experiencia práctica en la seguridad de un entorno Linux multiusuario.
2. **[Agregar nuevo usuario y grupo](https://labex.io/es/labs/linux-add-new-user-and-group-17987)** - En este desafío, simularás la adición de nuevos miembros del equipo a un entorno de servidor creando nuevas cuentas de usuario, configurando grupos personalizados y gestionando membresías de grupo. Esto pondrá a prueba tus habilidades en la administración de usuarios y grupos de Linux, esenciales para los administradores de sistemas y profesionales de DevOps.

Estos laboratorios te ayudarán a aplicar los conceptos de gestión de usuarios y grupos en escenarios reales, construyendo una base sólida para comprender cómo los UIDs controlan el acceso y los permisos en Linux.

## Quiz Question

¿Qué UID decide qué acceso otorgar?

## Quiz Answer

effective
