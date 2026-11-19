---
lesson_id: "incident-containment"
course_id: "incident-response"
lang: "es"
order_index: 4
title: "Contención"
description: "Aprende a comparar opciones autorizadas de contención según su propósito, su impacto y las pruebas que necesitas conservar."
meta_title: "Contención - Respuesta a incidentes"
meta_description: "Aprende a comparar opciones autorizadas de contención según su propósito, su impacto y las pruebas que necesitas conservar."
meta_keywords: "contención, respuesta a incidentes, ciberseguridad, Linux Journey"
---

La **contención** es una medida a corto plazo que busca limitar los daños mientras el equipo investiga. La medida adecuada depende de qué se haya visto afectado y de qué acceso siga necesitando la gente.

## Definir el límite de la contención

Imagina que un panel interno de vista previa es accesible por una ruta pública y que la página de inicio debe seguir abierta. Una opción es restringir la ruta de la vista previa. Otra más amplia es dejar todo el sitio fuera de servicio. Compara qué cambiaría con cada opción.

:::single-choice{#incident-containment-narrow-action} ¿Qué opción permite cerrar el acceso público a la vista previa y mantener disponible la página de inicio?

::option[Deshabilitar todas las rutas públicas sin importar su propósito.]{#incident-containment-narrow-action-b explanation="Eso también dejaría inaccesible la página de inicio."}
::option[Restringir la ruta afectada de la vista previa y comprobar ambas rutas.]{#incident-containment-narrow-action-a .correct explanation="Esto actúa sobre la exposición comunicada y comprueba que el servicio necesario siga disponible."}
::option[Cambiar la etiqueta del servicio de vista previa.]{#incident-containment-narrow-action-c explanation="Una etiqueta no impide que le lleguen peticiones."}
:::

## Planificar la conservación de pruebas y el acceso

Consulta el plan de respuesta y a las personas autorizadas para aplicar el cambio. Registra quién lo aprobó, cuánto debe durar y qué pruebas conviene conservar primero si las circunstancias lo permiten. Considera si la medida interrumpiría el registro del servicio o el acceso del equipo de respuesta.

:::single-choice{#incident-containment-action-impact} Una medida de aislamiento propuesta también podría impedir que el equipo de investigación recupere los registros. ¿Qué debe revisar el equipo?

::option[Qué se debe conservar y cómo mantendrá el acceso el personal de respuesta autorizado.]{#incident-containment-action-impact-b .correct explanation="Así se tienen en cuenta tanto la contención como la investigación."}
::option[Solo si el archivo de configuración tiene un nombre corto.]{#incident-containment-action-impact-a explanation="El nombre no conserva los registros ni el acceso."}
::option[Si conviene publicar las credenciales para que todos puedan volver a conectarse.]{#incident-containment-action-impact-c explanation="Las credenciales deben seguir protegidas y el acceso debe mantenerse bajo control."}
:::

## Verificar una medida de contención

Comprueba si se cerró la vía de acceso no prevista. Prueba por separado una vía que deba seguir disponible para detectar efectos secundarios. Registra cuándo aplicaste el cambio y cuándo debe revisarlo el equipo. La contención puede funcionar aunque la causa de fondo siga sin aclararse.

:::single-choice{#incident-containment-containment-success} La ruta pública de la vista previa está cerrada y la página de inicio aún funciona. ¿Qué afirmación respaldan las comprobaciones?

::option[La causa raíz se ha corregido con seguridad.]{#incident-containment-containment-success-a explanation="Las comprobaciones confirman el límite de acceso. La reparación de la causa requiere otras pruebas."}
::option[Se han probado todas las vías posibles de acceso a la vista previa.]{#incident-containment-containment-success-b explanation="Estas comprobaciones cubren las rutas concretas que se probaron."}
::option[La ruta pública de la vista previa que se probó está bloqueada y la página de inicio requerida sigue disponible.]{#incident-containment-containment-success-c .correct explanation="La afirmación describe el resultado dentro del alcance que se comprobó."}
:::

## Resumen

Ya puedes evaluar una medida de contención a corto plazo.

1. Identifica la ruta o el acceso que debe restringir la medida.
2. Revisa la autorización, las pruebas y los efectos previstos.
3. Verifica por separado la restricción prevista y el servicio esencial.
