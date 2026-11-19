---
lesson_id: "linux-service-accounts"
course_id: "linux-hardening"
lang: "es"
order_index: 2
title: "Cuentas de servicio"
description: "Aprende a identificar con qué cuenta se ejecuta un proceso de Linux y a determinar a qué puede acceder."
meta_title: "Cuentas de servicio - Endurecimiento de Linux"
meta_description: "Aprende a identificar con qué cuenta se ejecuta un proceso de Linux y a determinar a qué puede acceder."
meta_keywords: "cuentas de servicio, endurecimiento de Linux, ciberseguridad, Linux Journey"
---

Un servidor web se inicia como un proceso. Linux asocia cada proceso con una identidad que ayuda a determinar qué puede leer o modificar el programa. Una **cuenta de servicio** es una identidad reservada para un programa.

## Consultar la identidad del proceso

En un terminal normal, `$$` devuelve el ID del proceso del intérprete de comandos. Úsalo para consultar con qué identidad se ejecuta tu propio intérprete. La opción `-p` selecciona ese proceso y `-o` elige qué columnas se muestran. Los signos de igual omiten los encabezados de las columnas.

```bash
$ ps -p "$$" -o user=,comm=
```

En un terminal de LabEx, la cuenta podría ser `labex`. La columna del comando indica el nombre del intérprete. Las columnas equivalentes de un proceso de servicio indican la cuenta que usa, independientemente de quién lo haya iniciado.

:::single-choice{#linux-service-accounts-process-user} ¿Qué campo indica la cuenta asociada al proceso seleccionado?

::option[El ID de proceso que se indica con -p.]{#linux-service-accounts-process-user-a explanation="El ID sirve para seleccionar un proceso en ejecución."}
::option[El nombre del comando en la última columna.]{#linux-service-accounts-process-user-c explanation="Ese campo indica el programa en ejecución."}
::option[El campo de usuario que muestra ps.]{#linux-service-accounts-process-user-b .correct explanation="El campo de usuario indica la identidad del proceso."}
:::

![Salida de ps con el proceso del intérprete de LabEx y su cuenta labex](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/linux-hardening/linux-service-accounts/shell-identity.png)

## Elegir una identidad específica

Imagina un servicio web cuyas únicas tareas son leer páginas y escribir en su propio registro. Puedes conceder esos permisos a una cuenta específica llamada `site-web`. Ejecutarlo con permisos más amplios de administración permitiría que el programa hiciera más cambios en el equipo de los que necesita.

:::single-choice{#linux-service-accounts-isolate-service} ¿Qué permisos se ajustan a las tareas de ese servicio?

::option[Permitir que site-web modifique los archivos de todos los usuarios.]{#linux-service-accounts-isolate-service-b explanation="Ninguna tarea del servicio necesita ese nivel de acceso."}
::option[Permitir que site-web lea las páginas y escriba en su propio registro.]{#linux-service-accounts-isolate-service-a .correct explanation="Estos permisos corresponden a las dos tareas indicadas."}
::option[Permitir que site-web tenga permisos de administración en cada petición.]{#linux-service-accounts-isolate-service-c explanation="Para la mayoría de las peticiones bastan los permisos limitados del servicio."}
:::

## Revisar varios procesos

Algunos servicios usan procesos distintos para tareas diferentes. Comprueba qué proceso atiende la petición para saber qué permisos se le aplican. Si cambias la identidad con la que se ejecuta, confirma que el servicio todavía puede leer sus datos de entrada y que solo puede escribir donde lo necesita.

:::single-choice{#linux-service-accounts-verify-identity} Una herramienta de mantenimiento indica que un proceso supervisor se ejecuta como root. ¿Cómo averiguas qué cuenta atiende las peticiones web?

::option[Consultando la identidad del proceso que atiende las peticiones.]{#linux-service-accounts-verify-identity-c .correct explanation="Examinar el proceso pertinente te permite asociar la cuenta con la tarea que realmente realiza."}
::option[Consultando solo el nombre del archivo de configuración del servicio.]{#linux-service-accounts-verify-identity-a explanation="El nombre del archivo no indica con qué identidad se ejecuta el proceso que atiende peticiones."}
::option[Consultando el nombre de quien abrió el terminal.]{#linux-service-accounts-verify-identity-b explanation="El usuario del terminal puede ser distinto del usuario con el que se ejecuta el servicio."}
:::

## Resumen

Ya puedes relacionar un proceso de Linux con la identidad con la que se ejecuta.

1. Localiza el usuario de un proceso en la salida de ps.
2. Elige permisos acordes con las tareas del servicio.
3. Si el servicio consta de varios procesos, examina el que realiza la tarea que te interesa.
