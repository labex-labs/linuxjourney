---
lesson_id: "incident-recovery"
course_id: "incident-response"
lang: "es"
order_index: 5
title: "Recuperación"
description: "Aprende a verificar que el servicio esté en el estado aprobado antes de dar por terminada la recuperación."
meta_title: "Recuperación - Respuesta a incidentes"
meta_description: "Aprende a verificar que el servicio esté en el estado aprobado antes de dar por terminada la recuperación."
meta_keywords: "recuperación, respuesta a incidentes, ciberseguridad, Linux Journey"
---

La **recuperación** restablece el servicio esperado y comprueba que siga siendo utilizable. Ver un proceso recién iniciado es una primera señal. El equipo también necesita comprobar que la configuración, las dependencias y el comportamiento que observan los usuarios coincidan con el estado previsto.

## Identificar el estado recuperado

Registra qué versión y qué configuración se aprobaron para la recuperación. Si se aisló un servicio, revisa qué accesos deben seguir restringidos. Reabrir una vía puede cambiar el límite de la contención.

:::single-choice{#incident-recovery-restore-target} ¿Qué resultado te indica si restauraste la versión prevista?

::option[Una marca de tiempo reciente en cualquier máquina virtual ajena al servicio.]{#incident-recovery-restore-target-b explanation="Ese dato no identifica el servicio restaurado."}
::option[Solo una lista de paquetes disponibles.]{#incident-recovery-restore-target-c explanation="Los paquetes disponibles no indican qué versión está atendiendo las peticiones."}
::option[Una respuesta o un registro de despliegue que identifique la versión aprobada en el destino.]{#incident-recovery-restore-target-a .correct explanation="Vincula el servicio en ejecución con la versión que eligió el equipo."}
:::

## Volver a comprobar el problema comunicado

En el incidente simulado, los visitantes recibieron un `503` en la página de inicio pública. Tras restablecer el servicio, solicita esa misma ruta desde una ubicación de prueba adecuada. Comprueba que la respuesta sea la esperada y vigila los errores de peticiones recientes. Una vista previa interna que funciona deja sin probar la ruta pública.

:::single-choice{#incident-recovery-verify-original-path} ¿Qué prueba muestra mejor que el problema que observaban los usuarios ha desaparecido?

::option[Verificar solo que exista el ejecutable del servicio.]{#incident-recovery-verify-original-path-a explanation="El archivo puede existir sin que el programa atienda las peticiones públicas."}
::option[Comprobar la página de inicio pública por la vía de acceso del cliente afectado.]{#incident-recovery-verify-original-path-b .correct explanation="Así repites la comprobación que falló inicialmente."}
::option[Comprobar solo la vista previa interna.]{#incident-recovery-verify-original-path-c explanation="Esa vía era distinta de la ruta afectada."}
:::

## Seguir observando el servicio

Acuerda un periodo breve de observación y los criterios para considerar que el servicio se ha recuperado. Revisa las señales pertinentes, como los errores, la latencia o las denegaciones de acceso. Registra los límites de la comprobación, las acciones pendientes y la hora de la próxima revisión. Guarda las pruebas de recuperación junto al registro del incidente.

:::single-choice{#incident-recovery-observation-period} Una primera comprobación sale bien, pero el fallo era intermitente. ¿Qué debes hacer antes de dar por verificada la recuperación?

::option[Seguir revisando las señales acordadas durante el periodo de observación.]{#incident-recovery-observation-period-c .correct explanation="Esto aporta pruebas de que el servicio sigue funcionando como se espera."}
::option[Cerrar la revisión de inmediato porque llegó una respuesta.]{#incident-recovery-observation-period-a explanation="Una sola observación puede pasar por alto un problema intermitente."}
::option[Desechar todos los datos de comparación.]{#incident-recovery-observation-period-b explanation="Los resultados anteriores permiten ver qué mejoró."}
:::

## Resumen

Ya puedes comprobar el estado del servicio y lo que observan sus usuarios tras la recuperación.

1. Identifica la versión y la configuración aprobadas.
2. Repite la prueba del síntoma que observaron los usuarios.
3. Observa las señales acordadas antes de cerrar la comprobación de recuperación.
