---
lesson_id: "system-logging"
course_id: "logging"
lang: "es"
order_index: 1
title: "Registro del sistema"
description: "Aprende cómo se relacionan las fuentes, los recolectores, el almacenamiento y las herramientas de consulta de registros en Linux."
meta_title: "Registro del sistema - Logging"
meta_description: "Descubre cómo aprender Linux comprendiendo el registro del sistema. Esta guía explica syslog, rsyslogd y cómo encontrar y leer archivos de registro en /var/log, una parte esencial de cualquier curso gratuito de Linux."
meta_keywords: "cómo aprender linux, mejor manera de aprender linux, registro del sistema linux, syslog, rsyslogd, var log, registros del sistema, aprender línea de comandos linux, mejores recursos para aprender linux"
---

Los registros guardan eventos emitidos por el kernel, los servicios, las aplicaciones y los componentes de seguridad. Ayudan a diagnosticar problemas y realizar auditorías, pero solo si la recopilación funciona, se comprenden las marcas de tiempo y se incluye la fuente correspondiente.

## Seguir el recorrido de un mensaje de registro

Una ruta de registro consta de varias partes distintas:

1. Una fuente emite un evento.
2. Un recolector lo acepta y lo enriquece.
3. Las reglas de enrutamiento y conservación eligen los destinos de almacenamiento o reenvío.
4. Una herramienta de consulta busca en los registros almacenados.

En una máquina con systemd, `systemd-journald` suele recopilar la salida estándar de los servicios, los mensajes del kernel y los mensajes nativos del diario o de syslog. Un demonio syslog como rsyslog también puede recibir mensajes y escribir archivos de texto tradicionales o reenviarlos. Las aplicaciones pueden mantener en cambio sus propios archivos o telemetría externa.

:::single-choice{#system-logging-distinct-roles}
¿Qué componente decide dónde se almacenan o reenvían los mensajes aceptados?

::option[El directorio de trabajo actual de la terminal.]{#system-logging-cwd explanation="Un directorio del shell no define las rutas de registro de todo el sistema."}
::option[El nombre de archivo de la imagen del kernel en ejecución.]{#system-logging-kernel-file explanation="El kernel puede emitir mensajes, pero el nombre de archivo de su imagen no es la política de enrutamiento."}
::option[La configuración de enrutamiento y conservación.]{#system-logging-routing .correct explanation="Las reglas entre la recopilación y el almacenamiento determinan los destinos y el comportamiento de conservación."}
:::

## Descubrir los registros disponibles

No supongas que todas las máquinas tienen los mismos archivos. Inspecciona los servicios de registro activos y la configuración local:

```bash
$ systemctl --type=service --state=running | grep -E 'journal|syslog'
$ ls -la /var/log
$ journalctl --disk-usage
```

`/var/log/syslog` es habitual en sistemas de la familia Debian que utilizan un enrutamiento compatible, mientras que `/var/log/messages` es común en otros. Cualquiera de ellos puede faltar en una máquina que solo use el diario. La documentación de la aplicación y la configuración de sus unidades pueden indicar destinos adicionales.

:::single-choice{#system-logging-file-absence}
¿Qué significa necesariamente que falte el archivo `/var/log/syslog`?

::option[La máquina puede utilizar otro destino de registro configurado.]{#system-logging-other-destination .correct explanation="Los sistemas que solo usan el diario y otras políticas de syslog no tienen por qué crear este archivo."}
::option[El kernel nunca ha producido ningún mensaje.]{#system-logging-no-kernel explanation="Los registros del kernel pueden estar en el diario o en otro destino."}
::option[Todas las aplicaciones han dejado de ejecutarse.]{#system-logging-apps-stopped explanation="El estado de las aplicaciones no puede deducirse de una única ruta ausente."}
:::

## Consultar el diario

Empieza con una consulta limitada en lugar de volcar todo el diario:

```bash
$ journalctl -b -p warning
$ journalctl -u ssh.service --since '1 hour ago'
```

`-b` selecciona el arranque actual, `-p` filtra por prioridad y `-u` filtra por unidad. Los nombres de las unidades y los arranques conservados varían según la máquina. Usa `journalctl --list-boots` para ver los arranques disponibles y `journalctl -f` para seguir los registros nuevos mientras reproduces un problema.

:::single-choice{#system-logging-current-boot}
¿Qué opción limita una consulta de `journalctl` al arranque actual?

::option[`-b`]{#system-logging-boot-option .correct explanation="Sin argumento, el selector de arranque elige el actual."}
::option[`-u`]{#system-logging-unit-option explanation="Esta opción filtra por una unidad de systemd."}
::option[`-f`]{#system-logging-follow-option explanation="Esta opción sigue los registros que se añadan a partir de ese momento."}
:::

## Interpretar los registros en su contexto

Una línea tradicional con estilo syslog puede tener este aspecto:

```text
Jan 27 07:41:32 icebox anacron[4650]: Job `cron.weekly' started
```

Contiene una marca de tiempo, la máquina, el programa y el PID, y después un mensaje. Trata el texto del mensaje como salida de la aplicación, no como un hecho estructurado garantizado. Comprueba la zona horaria, la sincronización del reloj, el identificador del arranque, la reutilización de PID y los registros inmediatamente anteriores y posteriores al evento. Los campos del diario pueden proporcionar identificadores más sólidos que el texto mostrado por sí solo.

Los registros pueden contener nombres de usuario, direcciones, rutas, tokens u otros datos sensibles. Aplica el acceso con privilegios mínimos, elimina datos sensibles de las exportaciones y conserva los originales y sus marcas de tiempo durante una investigación.

:::single-choice{#system-logging-export-safety}
¿Qué debes hacer antes de compartir externamente un fragmento de un registro?

::option[Sustituir todas las marcas de tiempo por valores aleatorios.]{#system-logging-random-time explanation="Destruir la información temporal puede impedir la correlación y no constituye un método de ocultación adecuado."}
::option[Revisarlo en busca de secretos e identificadores sensibles.]{#system-logging-review-sensitive .correct explanation="Los registros suelen contener datos operativos o personales que requieren una eliminación controlada."}
::option[Permitir que cualquiera pueda modificar el registro original.]{#system-logging-world-writable explanation="Debilitar los controles de acceso puede dañar la integridad y exponer datos adicionales."}
:::

## Resumen

Ahora puedes localizar y consultar registros de Linux sin suponer que existe una única ruta universal de almacenamiento.

1. Distingue las fuentes de eventos, los recolectores, el enrutamiento, el almacenamiento y las herramientas de consulta.
2. Descubre la configuración de registro activa de la máquina.
3. Usa consultas limitadas del diario por unidad, arranque, tiempo o prioridad.
4. Relaciona los registros en su contexto y protege los datos sensibles.
