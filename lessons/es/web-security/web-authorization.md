---
lesson_id: "web-authorization"
course_id: "web-security"
lang: "es"
order_index: 6
title: "Autorización"
description: "Aprende a comparar la petición de un usuario autenticado con la política de acceso de una aplicación."
meta_title: "Autorización - Seguridad web"
meta_description: "Aprende a comparar la petición de un usuario autenticado con la política de acceso de una aplicación."
meta_keywords: "autorización, seguridad web, ciberseguridad, Linux Journey"
---

Un usuario puede iniciar sesión y aun así carecer de permiso para realizar una acción concreta. La **autorización** determina si una cuenta puede realizar una acción sobre un recurso.

## Interpretar una política

Un **rol** es un conjunto de permisos con un nombre. Esta política de prácticas rige un servicio de vista previa.

```text
Role       View published page   Edit draft
Reader    Yes                   No
Editor    Yes                   Yes
```

Lee la fila del rol del usuario y la columna de la operación solicitada. Un editor puede ver la página publicada y editar un borrador. Un lector puede ver la página publicada.

:::single-choice{#web-authorization-read-policy} Un lector que ha iniciado sesión pide editar un borrador. ¿Qué indica la tabla?

::option[La acción no está permitida para el rol Reader.]{#web-authorization-read-policy-b .correct explanation="La fila Reader tiene un No en la columna Edit draft."}
::option[La acción está permitida para cualquier cuenta que haya iniciado sesión.]{#web-authorization-read-policy-a explanation="La acción solicitada tiene una configuración de permisos específica para cada rol."}
::option[El usuario debe cambiar a HTTPS para obtener permiso de edición.]{#web-authorization-read-policy-c explanation="Proteger el transporte no concede permisos en la aplicación."}
:::

## Comprobar el recurso adecuado

Muchos sistemas conceden permisos distintos para distintos recursos. Un editor podría modificar borradores de su propio proyecto y tener acceso de solo lectura a las páginas de otro. La comprobación debe identificar tanto la operación como el recurso al que se aplica.

:::single-choice{#web-authorization-target-resource} Maya puede editar el proyecto A. ¿Qué dato determina si puede editar el proyecto B?

::option[El título del proyecto A.]{#web-authorization-target-resource-b explanation="El título no indica qué acceso existe en otro proyecto."}
::option[El hecho de que inició sesión correctamente.]{#web-authorization-target-resource-c explanation="La autenticación identifica la cuenta de Maya. El acceso al recurso se decide por separado."}
::option[La política de permisos de Maya para el proyecto B.]{#web-authorization-target-resource-a .correct explanation="El permiso anterior se concedió para un recurso concreto."}
:::

## Aplicar la política en el servicio

Una interfaz puede ocultar los controles de edición a los lectores. El servidor debe aplicar su política cada vez que recibe una petición. Comprueba los casos que se deben permitir y los que se deben denegar mediante acciones habituales y autorizadas en el servicio de prácticas.

:::single-choice{#web-authorization-decision-location} Una aplicación oculta el botón Editar a los lectores. ¿Dónde más debe aplicarse la decisión de acceso?

::option[Solo en el navegador cuando decide qué botón mostrar.]{#web-authorization-decision-location-a explanation="El navegador puede ajustar la interfaz. El servicio toma la decisión de acceso para la petición que recibe."}
::option[En el servicio que recibe la petición para realizar la operación.]{#web-authorization-decision-location-c .correct explanation="El servicio puede evaluar la cuenta, la acción y el recurso de destino cada vez."}
::option[Solo en la página que enumera los roles.]{#web-authorization-decision-location-b explanation="Mostrar el nombre del rol no impide realizar una operación restringida."}
:::

## Resumen

Ya puedes interpretar una decisión de acceso de una aplicación.

1. Relaciona el rol de la cuenta con la acción solicitada.
2. Incluye el recurso concreto en la comprobación.
3. Verifica que el servicio aplique su política a las peticiones.
