---
lesson_id: "process-termination"
course_id: "processes"
lang: "es"
order_index: 5
title: "Terminación de procesos"
description: "Aprende cómo el estado de salida, la espera, los zombis y la reasignación de padre completan el ciclo de vida de un proceso de Linux."
meta_title: "Terminación de procesos - Procesos"
meta_description: "Descubre la terminación de procesos en Linux, las operaciones wait y las diferencias entre procesos zombis y huérfanos."
meta_keywords: "terminación de procesos Linux, proceso zombi, proceso huérfano, zombi frente a huérfano, llamada wait, gestión de procesos"
---

Un proceso puede terminar al volver de su función principal, llamar a una interfaz de salida o ser finalizado por una señal. El kernel libera la mayoría de sus recursos, pero la contabilidad entre padre e hijo continúa hasta que el padre recoge la información de terminación.

## Estado de salida

Un programa que termina normalmente proporciona un estado entero. Por convención, el estado `0` significa éxito y un valor distinto de cero comunica algún tipo de fallo o resultado alternativo. El significado exacto de los valores no nulos forma parte de la interfaz del programa.

En un shell, consulta el estado de la tubería en primer plano más reciente con:

```bash
$ command
$ printf '%s\n' "$?"
```

Los shells exponen un intervalo codificado limitado y también representan la terminación mediante señales, por lo que este valor no es un registro diagnóstico completo. Los programas deben documentar sus propios códigos de salida.

:::single-choice{#process-termination-success-status} Según la convención de Unix, ¿qué estado de salida normal indica éxito?

::option[`1`]{#process-termination-status-one explanation="Muchos programas usan `1` para un fallo general, aunque el significado depende de cada orden."}
::option[`0`]{#process-termination-status-zero .correct explanation="Un estado normal igual a cero indica convencionalmente una finalización correcta."}
::option[`255`]{#process-termination-status-255 explanation="Este valor es distinto de cero y no representa convencionalmente el éxito."}
:::

## Esperar y recoger

El kernel registra cómo terminó un hijo y avisa a su padre. El padre usa una función de la familia de llamadas al sistema `wait()` para recuperar esa información. La recogida del registro se denomina *reaping*.

La espera también puede coordinar la ejecución: un shell espera a que termine una orden en primer plano antes de mostrar otro indicador, mientras que puede aplazar la espera de un trabajo en segundo plano. Un padre de larga duración bien diseñado debe organizar la recogida de hijos sin bloquear trabajo no relacionado.

:::single-choice{#process-termination-wait-purpose} ¿Qué permite recuperar al padre una operación de espera correcta?

::option[La información de terminación del hijo.]{#process-termination-wait-status .correct explanation="La familia wait muestra cómo se detuvo o terminó un hijo y recoge a un hijo completado."}
::option[Una copia del antiguo espacio de direcciones del hijo.]{#process-termination-wait-memory explanation="La mayor parte de la memoria del proceso ya se ha liberado y `wait()` no la devuelve al padre."}
::option[La propiedad de todos los archivos que abrió el hijo.]{#process-termination-wait-files explanation="La espera no transfiere metadatos de propiedad del sistema de archivos."}
:::

## Procesos zombis

Después de que un hijo termina, pero antes de que se recoja su registro de terminación, aparece como zombi, a menudo con el estado `Z` en `ps`. Ya no se ejecuta ni conserva un espacio de direcciones normal, pero permanecen una entrada mínima en la tabla de procesos y datos contables.

Enviar una señal a un zombi no puede hacer que termine de nuevo. Para resolver una acumulación persistente, diagnostica el padre que no está esperando, reinicia o corrige ese padre mediante un procedimiento operativo apropiado o permite su reasignación a un proceso que lo recoja. Una gran cantidad puede agotar la capacidad de PID o de la tabla de procesos.

:::single-choice{#process-termination-zombie-definition} ¿Qué descripción corresponde a un proceso zombi?

::option[Un hijo en ejecución cuyo padre ya ha terminado.]{#process-termination-zombie-orphan explanation="Eso describe un hijo huérfano, no un estado zombi."}
::option[Un hijo completado cuyo registro de terminación no se ha recogido.]{#process-termination-zombie-unreaped .correct explanation="El proceso ha dejado de ejecutarse, pero el kernel conserva un estado mínimo para su padre."}
::option[Un proceso que consume CPU en un bucle ininterrumpible.]{#process-termination-zombie-cpu explanation="Un zombi no ejecuta instrucciones ni consume tiempo de CPU."}
:::

## Huérfanos y reasignación de padre

Si un padre termina mientras su hijo continúa, el kernel reasigna ese hijo a un subreaper apto o al proceso init del espacio de nombres PID correspondiente. El hijo puede estar en ejecución, dormido, detenido o convertirse después en zombi; «huérfano» describe la pérdida de la relación con el padre original, no un estado de ejecución concreto.

El proceso adoptante pasa a ser responsable de recoger el estado de terminación. Los gestores de servicios y entornos de contenedores modernos hacen importante no suponer que el padre nuevo siempre es el PID 1 del host.

:::single-choice{#process-termination-orphan-definition} ¿Qué ocurre cuando un proceso sobrevive a su padre original?

::option[Se reasigna a un subreaper apto o al proceso init del espacio de nombres.]{#process-termination-orphan-reparented .correct explanation="El kernel conserva una relación de parentesco válida asignando un proceso adoptante."}
::option[Se convierte inmediatamente en zombi aunque no haya terminado.]{#process-termination-orphan-zombie explanation="El estado zombi comienza únicamente después de terminar la ejecución y mientras el estado espera su recogida."}
::option[Pierde permanentemente su PID y continúa de forma anónima.]{#process-termination-orphan-no-pid explanation="Un huérfano activo conserva su identidad de proceso mientras cambia su relación con el padre."}
:::

Usa el laboratorio [Gestionar y supervisar procesos de Linux](https://labex.io/labs/comptia-manage-and-monitor-linux-processes-590864) para observar códigos de salida y estados de procesos sin alterar una carga de producción.

## Resumen

Ahora puedes distinguir el final de la ejecución de la limpieza que realiza el padre.

1. Interpreta cero como éxito convencional y los estados no nulos según la documentación del programa.
2. Usa la espera para recoger la información de terminación de un hijo.
3. Reconoce un zombi como un proceso terminado pero no recogido.
4. Reconoce un huérfano como un hijo reasignado después de que termine su padre original.
