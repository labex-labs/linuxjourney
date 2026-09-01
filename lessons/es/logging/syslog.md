---
lesson_id: "syslog"
course_id: "logging"
lang: "es"
order_index: 2
title: "syslog"
description: "Aprende cómo funcionan las instalaciones, las gravedades, las reglas de enrutamiento de syslog y el comando logger."
meta_title: "syslog - Logging"
meta_description: "Aprende sobre syslog y rsyslog en Linux, cómo gestionar los registros del sistema y cómo usar el comando logger. Comienza con este tutorial para principiantes."
meta_keywords: "syslog, rsyslog, registros de Linux, comando logger, /var/log/syslog, tutorial de Linux, Linux para principiantes, registro del sistema"
---

Syslog define un modelo de mensajes y convenciones de transporte que utilizan muchos sistemas de tipo Unix. Rsyslog es una implementación capaz de recibir, filtrar, transformar, almacenar y reenviar mensajes. Puede coexistir con `systemd-journald`; ninguno de estos nombres significa que todas las aplicaciones utilicen esa ruta.

## Instalaciones y gravedades

Un mensaje syslog contiene una instalación que describe la categoría general de su fuente y una gravedad que va desde emergencia hasta depuración. Entre las instalaciones habituales se encuentran `auth`, `cron`, `daemon`, `kern`, `mail`, `user` y desde `local0` hasta `local7`.

Las gravedades están ordenadas. En la sintaxis clásica de selectores, `daemon.warning` suele coincidir con los mensajes de demonios de gravedad warning y con todos los niveles más graves, no solo con warning. En las implementaciones compatibles con la sintaxis clásica, la coincidencia exacta utiliza un modificador de igualdad, como `daemon.=warning`.

:::single-choice{#syslog-warning-selector} ¿Con qué suele coincidir un selector clásico como `daemon.warning`?

::option[Únicamente con mensajes cuyo texto contenga la palabra daemon.]{#syslog-text-daemon explanation="Este selector utiliza los metadatos de la instalación, no una búsqueda en el texto del mensaje."}
::option[Con todos los mensajes de depuración de todas las instalaciones.]{#syslog-all-debug explanation="El selector se limita a la instalación daemon y a un umbral de gravedad."}
::option[Con los mensajes warning y los mensajes más graves de la instalación daemon.]{#syslog-warning-or-higher .correct explanation="El selector de prioridad incluye la gravedad indicada y los niveles de mayor urgencia."}
:::

## Interpretar las reglas de rsyslog

Rsyslog suele cargar un archivo principal y fragmentos bajo `/etc/rsyslog.d/`. Una regla tradicional tiene un selector seguido de una acción:

```text
auth,authpriv.*          /var/log/auth.log
*.*;auth,authpriv.none  -/var/log/syslog
kern.*                  /var/log/kern.log
```

La primera línea dirige todas las prioridades de dos instalaciones de autenticación. La segunda selecciona mensajes de forma amplia y excluye esas instalaciones. La tercera dirige los mensajes de la instalación del kernel. Un `-` inicial en una acción de archivo suele solicitar escrituras asíncronas; no indica una exclusión.

Inspecciona todos los archivos incluidos y valida la sintaxis exacta que utilice la versión instalada antes de cambiar el enrutamiento de producción.

:::single-choice{#syslog-selector-action} En una regla tradicional de rsyslog, ¿qué es la acción?

::option[La expresión de instalación y gravedad de la izquierda.]{#syslog-left-selector explanation="Esa parte selecciona los mensajes."}
::option[El destino o la operación de la derecha.]{#syslog-right-action .correct explanation="La acción determina si los registros seleccionados van a un archivo, un destino remoto u otra salida."}
::option[El comentario que describe la versión del paquete.]{#syslog-comment-version explanation="Los comentarios no enrutan mensajes."}
:::

## Enviar un mensaje de prueba

Utiliza `logger` para enviar una prueba controlada con una etiqueta y una prioridad identificables:

```bash
$ logger -p user.notice -t lesson-test 'routing check 2026-08-31T10:00'
```

Después, consulta el destino esperado, por ejemplo:

```bash
$ journalctl -t lesson-test --since '5 minutes ago'
```

El mismo evento puede aparecer en el diario y en un archivo de texto según el reenvío y el enrutamiento. `logger -s` también copia el mensaje al error estándar; no demuestra que se haya almacenado de forma persistente.

:::single-choice{#syslog-logger-tag} ¿Qué añade `logger -t lesson-test` al mensaje enviado?

::option[Una solicitud para borrar los registros de pruebas anteriores.]{#syslog-tag-delete explanation="La opción establece una etiqueta identificativa y no gestiona la conservación."}
::option[El identificador `lesson-test` como etiqueta del mensaje.]{#syslog-tag-identifier .correct explanation="Una etiqueta única permite localizar el evento controlado con más facilidad en los destinos configurados."}
::option[Un retraso de cinco minutos en la entrega.]{#syslog-tag-delay explanation="La opción de etiqueta no codifica ningún intervalo de entrega."}
:::

## Cambiar y comprobar el enrutamiento

Antes de un cambio, guarda la configuración actual e identifica los consumidores posteriores. Valida la sintaxis con el modo de comprobación de configuración de la implementación, normalmente:

```bash
$ sudo rsyslogd -N1
```

Solo después de validarla debes recargar el servicio mediante su gestor. Envía un nuevo mensaje etiquetado, comprueba todos los destinos necesarios y revisa el estado del servicio y sus registros internos de errores. Una regla con sintaxis válida aún puede enrutar demasiados mensajes, duplicar registros o exponer datos sensibles.

El reenvío remoto debe utilizar un transporte autenticado y cifrado cuando los registros atraviesen redes que no sean de confianza. La entrega mediante UDP no tiene confirmación de extremo a extremo; los requisitos de auditoría esenciales necesitan un diseño que tenga en cuenta las colas, las pérdidas, la integridad, el control de acceso y las interrupciones del receptor.

:::single-choice{#syslog-change-verification} ¿Qué constituye una prueba suficiente de que una regla nueva de enrutamiento funciona?

::option[El archivo de configuración tiene una fecha de modificación reciente.]{#syslog-mtime explanation="Una marca de tiempo no demuestra que la sintaxis sea válida ni que se produzca la entrega."}
::option[El emisor puede hacer ping al receptor.]{#syslog-ping explanation="La conectividad de red por sí sola no comprueba el protocolo de registro ni la ruta de almacenamiento."}
::option[La validación es satisfactoria y una prueba etiquetada llega a todos los destinos previstos.]{#syslog-validate-and-test .correct explanation="Se necesitan tanto una validación estática como observar un evento de extremo a extremo."}
:::

## Resumen

Ahora puedes comprobar el enrutamiento de syslog desde los metadatos del mensaje hasta su destino configurado.

1. Distingue las instalaciones de los niveles ordenados de gravedad.
2. Interpreta los selectores por separado de sus acciones.
3. Envía un evento etiquetado y con prioridad mediante `logger`.
4. Valida la configuración y comprueba la entrega de extremo a extremo.
