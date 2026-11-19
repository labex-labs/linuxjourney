---
lesson_id: "ci-workflow-logs"
course_id: "continuous-integration"
lang: "es"
order_index: 5
title: "Registros del flujo de trabajo"
description: "Aprende a encontrar el paso que falló en un flujo de trabajo y a interpretar el primer mensaje que ayuda a resolverlo."
meta_title: "Registros del flujo de trabajo - Integración continua"
meta_description: "Aprende a encontrar el paso que falló en un flujo de trabajo y a interpretar el primer mensaje que ayuda a resolverlo."
meta_keywords: "registros del flujo de trabajo, diagnóstico de fallos, integración continua, DevOps, Linux Journey"
---

El resultado de un flujo de trabajo muestra su estado general. Para entender un fallo, abre el trabajo que falló y lee sus pasos en orden. Si uno no termina correctamente, puede que los siguientes se omitan.

## Encontrar el primer fallo

Esta ejecución simulada muestra el estado de cada paso del trabajo que comprueba la página.

```text
Prepare: passed
Build page: failed
Check heading: skipped
Package site: skipped
```

Empieza por `Build page`. No hay ningún resultado para las comprobaciones de página que se omitieron. Después de corregir el fallo, verifica esos pasos en una ejecución nueva.

:::single-choice{#ci-workflow-logs-first-failure} ¿Qué salida debes leer primero?

::option[Package site, porque aparece en último lugar.]{#ci-workflow-logs-first-failure-a explanation="El paso de empaquetado se omitió en esta ejecución."}
::option[Check heading, porque el flujo comprueba una página.]{#ci-workflow-logs-first-failure-c explanation="El estado indica que la comprobación del encabezado no se ejecutó."}
::option[Build page, porque falló antes de que se ejecutaran los otros pasos.]{#ci-workflow-logs-first-failure-b .correct explanation="Su registro indica el motivo por el que se omitieron los pasos siguientes."}
:::

![Ejecución simulada de CI con un fallo de compilación y los pasos posteriores omitidos](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/continuous-integration/ci-workflow-logs/skipped-steps.png)

## Seguir la pista del mensaje de error

El paso que falló muestra estas líneas.

```text
Run cp index.html dist/index.html
cp: cannot create regular file 'dist/index.html': No such file or directory
Process completed with exit code 1.
```

El mensaje indica la ruta de destino. Si falta el directorio principal `dist`, la copia no puede crear un archivo dentro. Comprueba si un comando anterior creó ese directorio antes de copiar. El código de salida 1 indica que el comando falló. El mensaje te indica dónde buscar.

:::single-choice{#ci-workflow-logs-actionable-log} Si falta el directorio dist, ¿qué cambio resuelve el problema indicado?

::option[Cambiar el encabezado que comprueba grep.]{#ci-workflow-logs-actionable-log-b explanation="La comprobación del encabezado no se ejecutó, así que no hay indicios de que el texto sea incorrecto."}
::option[Crear dist antes de copiar el archivo.]{#ci-workflow-logs-actionable-log-a .correct explanation="Para crear el archivo de destino, su directorio debe existir."}
::option[Descargar un artefacto del paso omitido.]{#ci-workflow-logs-actionable-log-c explanation="El paso de empaquetado no llegó a generar un artefacto."}
:::

## Comprobar una nueva ejecución

Después de corregir la compilación, compara la revisión y el estado de los pasos de la nueva ejecución. Si la copia se completa, sabes que se creó el archivo de salida. Revisa la prueba y el empaquetado antes de considerar que todo el proceso ha pasado. Si comunicas un problema, conserva el primer error útil junto al nombre del paso.

:::single-choice{#ci-workflow-logs-rerun-evidence} En una nueva ejecución, Build page pasa y Check heading falla. ¿Qué ha cambiado?

::option[La compilación terminó bien y ahora hay un resultado de la comprobación del encabezado que puedes investigar.]{#ci-workflow-logs-rerun-evidence-c .correct explanation="El primer fallo pendiente está ahora en la prueba."}
::option[La nueva ejecución no importa porque la compilación anterior falló.]{#ci-workflow-logs-rerun-evidence-a explanation="Cada ejecución aporta información sobre su propia revisión."}
::option[El empaquetado pasó porque la compilación pasó.]{#ci-workflow-logs-rerun-evidence-b explanation="Un paso posterior aún puede fallar o quedar omitido."}
:::

## Resumen

Ya puedes interpretar el fallo de un flujo de trabajo en su contexto.

1. Localiza el primer paso que se ejecutó y falló.
2. Usa el mensaje del registro para decidir qué revisar.
3. Tras corregir el fallo, comprueba la nueva revisión y el estado de los pasos siguientes.
