---
lesson_id: "linux-security-updates"
course_id: "linux-hardening"
lang: "es"
order_index: 7
title: "Actualizaciones de seguridad"
description: "Aprende a revisar qué paquetes tienen actualizaciones disponibles y a verificar el servicio tras un mantenimiento autorizado."
meta_title: "Actualizaciones de seguridad - Endurecimiento de Linux"
meta_description: "Aprende a revisar qué paquetes tienen actualizaciones disponibles y a verificar el servicio tras un mantenimiento autorizado."
meta_keywords: "actualizaciones de seguridad, endurecimiento de Linux, ciberseguridad, Linux Journey"
---

Una actualización de seguridad puede corregir un fallo del software instalado. Empieza por comprobar qué versión está instalada y qué corrección existe para tu sistema operativo. Planifica el cambio teniendo en cuenta el servicio que usan las personas.

## Consultar las actualizaciones disponibles

En un equipo Ubuntu de prácticas, este comando de solo lectura enumera los paquetes que APT sabe que se pueden actualizar. Para ello usa la información de paquetes que ya está en el equipo.

```bash
$ apt list --upgradable
```

Si un paquete aparece en la lista, los datos disponibles indican que hay una versión candidata más reciente. Consulta el aviso de seguridad de tu distribución para saber si esa actualización incluye la corrección que necesitas. Una lista vacía también puede indicar que la información disponible está desactualizada.

:::single-choice{#linux-security-updates-candidate-is-listed} Un paquete aparece en la lista. ¿Qué te indica?

::option[La actualización ya se ha aplicado.]{#linux-security-updates-candidate-is-listed-a explanation="La lista indica que hay una versión candidata disponible."}
::option[APT conoce una versión candidata más reciente del paquete instalado.]{#linux-security-updates-candidate-is-listed-b .correct explanation="Eso es lo que indica la información local sobre paquetes en este momento."}
::option[Toda versión candidata más reciente es una actualización de seguridad.]{#linux-security-updates-candidate-is-listed-c explanation="Consulta el aviso de la distribución para conocer el motivo de la actualización."}
:::

## Planificar el cambio

Un cambio autorizado debe especificar el servicio, la versión de destino y el intervalo de mantenimiento. Algunas actualizaciones exigen reiniciar el servicio o el equipo para que surtan efecto. Planifica una petición de comprobación y una forma de recuperar el servicio antes de modificar el equipo.

:::single-choice{#linux-security-updates-reboot-check} Una actualización corrige código que usa un servicio que lleva tiempo en ejecución. ¿Qué debes comprobar después de instalarla?

::option[Si el servicio necesita reiniciarse para usar el código actualizado.]{#linux-security-updates-reboot-check-a .correct explanation="Un proceso en ejecución puede seguir teniendo cargado el código antiguo."}
::option[Si la actualización aparecía en la lista de paquetes antes de instalarla.]{#linux-security-updates-reboot-check-b explanation="La disponibilidad ayuda a planificar el mantenimiento. La versión cargada por el proceso se verifica aparte."}
::option[Si en la lista ya no queda ninguna actualización pendiente.]{#linux-security-updates-reboot-check-c explanation="La lista puede estar al día mientras un proceso sigue ejecutando el código anterior."}
:::

## Verificar el resultado

Confirma que la versión instalada coincide con la versión aprobada. Comprueba el servicio por la vía de acceso habitual de los usuarios y registra el resultado. Si la corrección afecta a un componente en ejecución, confirma también que la versión actualizada está en uso.

:::single-choice{#linux-security-updates-security-verification} ¿Qué dos comprobaciones indican mejor que la actualización del servicio se ha completado?

::option[El comando que muestra la lista se ejecuta dos veces.]{#linux-security-updates-security-verification-a explanation="Repetir la lista no demuestra que el servicio funcione."}
::option[El registro de mantenimiento tiene un nuevo título.]{#linux-security-updates-security-verification-b explanation="El título no aporta datos sobre el servicio en ejecución."}
::option[La versión aprobada está en uso y una petición representativa se completa correctamente.]{#linux-security-updates-security-verification-c .correct explanation="Así verificas el estado del software y el servicio del que dependen los usuarios."}
:::

## Interpretar dos datos sobre la versión

La versión del paquete instalado y la que atiende peticiones pueden diferir temporalmente. Por ejemplo, el inventario de paquetes puede mostrar la versión corregida mientras sigue en ejecución un proceso que se inició antes de la actualización. Comprueba el proceso en ejecución antes de dar por cerrada la revisión.

:::single-choice{#linux-security-updates-final-application} ¿Qué queda por averiguar si la versión instalada ya tiene la corrección y el proceso antiguo sigue en ejecución?

::option[Si todos los demás procesos del equipo deben sustituirse.]{#linux-security-updates-final-application-c explanation="La pregunta se refiere al servicio actualizado y a los requisitos del mantenimiento autorizado."}
::option[Si el programa actualizado es el que atiende las peticiones.]{#linux-security-updates-final-application-a .correct explanation="El inventario de paquetes confirma qué archivos hay instalados y la comprobación del proceso verifica el servicio en ejecución."}
::option[Si había algún paquete de actualización disponible.]{#linux-security-updates-final-application-b explanation="El paquete instalado ya indica que está en la versión corregida."}
:::

## Resumen

Ya puedes revisar una actualización desde que aparece como candidata hasta que se verifica.

1. Distingue las actualizaciones disponibles de los cambios instalados.
2. Incluye los reinicios y la recuperación en el plan.
3. Verifica la versión en ejecución y el comportamiento esperado del servicio.
