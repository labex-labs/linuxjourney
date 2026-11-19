---
lesson_id: "service-troubleshooting"
course_id: "service-monitoring"
lang: "es"
order_index: 7
title: "Diagnóstico de problemas del servicio"
description: "Aprende a elegir qué comprobar cuando un servicio se detiene, una dependencia falla o las peticiones se ralentizan."
meta_title: "Diagnóstico de problemas del servicio - Monitorización de servicios"
meta_description: "Aprende a elegir qué comprobar cuando un servicio se detiene, una dependencia falla o las peticiones se ralentizan."
meta_keywords: "diagnóstico de servicios, monitorización de servicios, DevOps, Linux Journey"
---

Empieza con un síntoma concreto, como una petición fallida a la página de inicio. Luego compara observaciones hechas alrededor de la misma hora y desde la ubicación pertinente para los usuarios.

## Cuando un servidor se detiene

En el primer caso, el navegador indica que se ha rechazado la conexión y el contenedor del servicio muestra `Exited (1)`. Ambas señales apuntan a investigar por qué se detuvo el programa. Consulta los registros que se hayan conservado. Ten en cuenta la hora de la detención al compararla con otros eventos.

:::single-choice{#service-troubleshooting-stopped-case} ¿Qué comprobación tiene más posibilidades de explicar por qué se detuvo el proceso?

::option[Volver a solicitar la misma página de inicio para obtener un estado más reciente.]{#service-troubleshooting-stopped-case-a explanation="Reintentar sirve para comprobar el síntoma. Los registros conservados pueden explicar por qué terminó el programa."}
::option[Leer las últimas líneas disponibles del registro del contenedor.]{#service-troubleshooting-stopped-case-b .correct explanation="Los mensajes de inicio o de salida pueden indicar en qué punto se detuvo el programa."}
::option[Examinar los registros de otro contenedor en ejecución que usa la misma imagen.]{#service-troubleshooting-stopped-case-c explanation="Ese contenedor tiene su propio historial de ejecución y puede que nunca haya sufrido ese fallo."}
:::

## Cuando falla una dependencia

En el segundo caso, el proceso web está en ejecución, pero la página devuelve un error del servidor. Su registro indica que se agotó el tiempo de espera al contactar con el catálogo para la petición `r17`. Examina los registros de la dependencia para esa misma petición. Comprobar que el primer servicio responde solo confirma el estado de ese paso.

:::single-choice{#service-troubleshooting-dependency-case} ¿Qué dato debes buscar a continuación para r17?

::option[El registro del catálogo para esa petición y esa hora.]{#service-troubleshooting-dependency-case-a .correct explanation="Muestra lo que ocurrió durante la llamada al servicio del que depende la web."}
::option[El tamaño de la imagen de Docker archivada.]{#service-troubleshooting-dependency-case-b explanation="Ese dato no describe la llamada que se hizo al catálogo."}
::option[Una comprobación de la página de inicio que salió bien ayer y no está relacionada.]{#service-troubleshooting-dependency-case-c explanation="Esa comprobación corresponde a otro momento y no explica qué pasó con esta petición."}
:::

## Cuando las peticiones se ralentizan

Una tercera muestra indica que la mayoría de las respuestas fueron correctas, pero los usuarios informan de demoras. La latencia aumenta en el mismo intervalo en que crece la cola de trabajo. Comprueba la demanda y la actividad de los procesos antes de atribuirles la causa. Si se aplica un cambio, repite la comprobación desde el punto de vista del usuario y vuelve a revisar las mismas señales.

:::single-choice{#service-troubleshooting-slow-case} ¿Qué comparación permite comprobar mejor si el cambio ayudó en este caso?

::option[Capturas del repositorio de código fuente de antes y después.]{#service-troubleshooting-slow-case-a explanation="Esas capturas no miden los tiempos de las peticiones ni las colas."}
::option[El tamaño de la caché frente al número de ramas desplegadas.]{#service-troubleshooting-slow-case-b explanation="Ninguna de esas cifras explica el tiempo de espera que se ha comunicado."}
::option[Los tiempos de peticiones de usuario comparables y las colas de trabajo antes y después.]{#service-troubleshooting-slow-case-c .correct explanation="Así compruebas el síntoma original y el posible cuello de botella."}
:::

## Interpretar comprobaciones con resultados distintos

Supón que una comprobación local tiene éxito mientras los usuarios siguen viendo errores. Anota qué ruta usó cada comprobación. La prueba local puede mostrar que un proceso responde en el equipo anfitrión, mientras que una petición desde un cliente puede revelar un problema en la ruta hasta ese equipo.

:::single-choice{#service-troubleshooting-final-application} ¿Qué resultado debe guiar el seguimiento del problema que afecta a los usuarios?

::option[Una comprobación desde la misma ubicación y por la misma ruta que usan esos usuarios.]{#service-troubleshooting-final-application-a .correct explanation="Observa la parte del servicio en la que los usuarios encontraron el problema."}
::option[Solo el resultado obtenido en el equipo anfitrión.]{#service-troubleshooting-final-application-b explanation="Ese resultado ayuda a acotar el problema y deja sin probar la ruta externa."}
::option[La capacidad actual del registro de imágenes.]{#service-troubleshooting-final-application-c explanation="El registro puede servir imágenes aunque haya otro problema en la ruta que usan los usuarios."}
:::

## Resumen

Ya puedes elegir la siguiente comprobación según los datos que tengas.

1. Usa el estado del proceso y los registros para investigar una detención.
2. Sigue una petición fallida hasta la dependencia que la atendió.
3. Verifica la mejora comprobando el síntoma que observó el usuario.
