---
lesson_id: "managing-log-files"
course_id: "logging"
lang: "es"
order_index: 6
title: "Gestión de archivos de registro"
description: "Aprende a configurar, probar y comprobar una rotación segura de registros de texto con logrotate."
meta_title: "Gestión de archivos de registro - Logging"
meta_description: "Domina la gestión de registros de Linux con esta guía para principiantes sobre logrotate. Aprende cómo la rotación ahorra espacio, cómo configurarla y cómo mantener organizados los registros del sistema."
meta_keywords: "logrotate, registros de Linux, gestión de registros, rotación de registros, tutorial Linux, principiante, guía, espacio en disco"
---

Los registros de texto sin límites pueden agotar un sistema de archivos, mientras que una eliminación demasiado agresiva puede borrar pruebas necesarias para las operaciones o el cumplimiento normativo. `logrotate` aplica políticas configuradas de tamaño, tiempo, compresión, propiedad y conservación a los registros basados en archivos.

## Comprender la rotación

Una rotación habitual cambia el nombre del archivo activo, crea uno que lo sustituye, pide opcionalmente a la aplicación que vuelva a abrirlo, comprime las generaciones anteriores y elimina los archivos que exceden la conservación. Estos pasos dependen de la configuración; la rotación no es una copia de seguridad, porque las copias conservadas aún pueden borrarse, dañarse o perderse junto con la misma máquina.

:::single-choice{#logrotate-not-backup} ¿Por qué la rotación de registros no sustituye a una copia de seguridad o un archivo histórico?

::option[Los archivos rotados siguen sujetos a la conservación local y a los fallos de la máquina.]{#logrotate-local-retention .correct explanation="La rotación controla las generaciones de registros de trabajo, pero no crea una copia duradera independiente."}
::option[La rotación solo puede procesar archivos de imagen.]{#logrotate-images explanation="La utilidad está diseñada principalmente para archivos de registro."}
::option[Todas las rotaciones conservan todas las generaciones para siempre.]{#logrotate-forever explanation="Las reglas de conservación normalmente eliminan las generaciones anteriores."}
:::

## Encontrar la configuración

El archivo principal suele ser `/etc/logrotate.conf`, con fragmentos de paquetes o aplicaciones bajo `/etc/logrotate.d/`. Una política simplificada puede tener este aspecto:

```text
/var/log/example/app.log {
    daily
    rotate 7
    compress
    delaycompress
    missingok
    notifempty
    create 0640 example adm
}
```

Esto solicita una evaluación diaria, la conservación de siete rotaciones, la compresión con una generación de retraso, tolerancia ante un registro ausente o vacío y un archivo nuevo con modo y propiedad explícitos. La rotación real también depende del estado registrado y de cómo el programador invoque logrotate.

:::single-choice{#logrotate-rotate-seven} ¿Qué especifica `rotate 7`?

::option[Conservar hasta siete generaciones rotadas según la política.]{#logrotate-seven-generations .correct explanation="Las generaciones anteriores se eliminan cuando se supera la conservación configurada."}
::option[Ejecutar la aplicación siete veces al día.]{#logrotate-run-seven explanation="La directiva controla las generaciones conservadas, no la ejecución de la aplicación."}
::option[Establecer los permisos de todos los archivos rotados en el modo 0007.]{#logrotate-mode-seven explanation="El modo del archivo se controla mediante directivas como `create`."}
:::

## Coordinarse con el proceso que escribe

Después de cambiar el nombre de un registro, un demonio puede seguir escribiendo mediante su descriptor de archivo aún abierto. Un script `postrotate` suele enviar una señal documentada de recarga o reapertura. Valida el comportamiento exacto de la aplicación y limita estrictamente el alcance del script.

`copytruncate` copia un archivo y trunca el original en su sitio cuando una aplicación no puede volver a abrir registros. Durante el intervalo de copia y truncado pueden perderse o duplicarse escrituras, por lo que es una solución de compromiso, no un valor predeterminado seguro en todos los casos.

:::single-choice{#logrotate-open-descriptor} ¿Por qué puede necesitar una aplicación una señal de reapertura después de la rotación?

::option[Su descriptor abierto aún puede hacer referencia al archivo cuyo nombre cambió.]{#logrotate-descriptor-renamed .correct explanation="Al volver a abrirlo, las escrituras futuras utilizan la ruta activa recién creada."}
::option[La compresión detiene automáticamente todos los procesos de la aplicación.]{#logrotate-compression-stops explanation="La compresión no gestiona de manera inherente el ciclo de vida del proceso que escribe."}
::option[El kernel prohíbe crear un segundo archivo de registro.]{#logrotate-kernel-forbids explanation="Pueden existir varios archivos de registro; la cuestión es qué inodo tiene abierto el proceso que escribe."}
:::

## Probar antes de activar

Usa el modo de depuración para inspeccionar las decisiones sin rotar archivos:

```bash
$ sudo logrotate -d /etc/logrotate.conf
```

La salida de depuración no demuestra que los permisos, los scripts, el espacio libre o la reapertura de la aplicación funcionen durante una ejecución real. Prueba una regla nueva en un entorno controlado y después inspecciona el archivo activo, la generación rotada, la propiedad, la compresión, la salida de la aplicación y el estado de logrotate tras la ejecución. `-f` fuerza la rotación y modifica el estado; no lo confundas con una simulación.

:::single-choice{#logrotate-debug-mode} ¿Qué proporciona `logrotate -d`?

::option[La eliminación permanente de todos los registros caducados.]{#logrotate-debug-delete explanation="El modo de depuración informa de las decisiones previstas sin realizar la rotación."}
::option[Una rotación forzada en producción sin tener en cuenta la política.]{#logrotate-debug-force explanation="La opción de fuerza es `-f`, que modifica el estado."}
::option[Una evaluación de diagnóstico sin modificar los archivos de registro ni el estado.]{#logrotate-debug-dry .correct explanation="Es la primera revisión apropiada de la sintaxis y las decisiones, seguida de una comprobación real y controlada."}
:::

## Tener en cuenta otros almacenes

Logrotate gestiona los archivos indicados en sus políticas. El diario de systemd tiene su propia configuración de tamaño y conservación, mientras que las bases de datos y los servicios remotos de registro disponen de controles distintos sobre el ciclo de vida. Supervisa la capacidad del sistema de archivos y la salud del registro para detectar un proceso de escritura bloqueado o una rotación fallida antes de agotar el espacio.

:::single-choice{#logrotate-journal-retention} ¿Aplica automáticamente una regla de logrotate la conservación del diario de systemd?

::option[No; el almacenamiento del diario tiene su propia configuración y sus propios límites.]{#logrotate-journal-separate .correct explanation="Logrotate solo gestiona las rutas seleccionadas por sus políticas de archivos."}
::option[Sí, porque todos los registros comparten un único motor de conservación.]{#logrotate-all-logs explanation="La rotación de archivos y la conservación del diario son mecanismos independientes."}
::option[Sí, pero solo cuando no existe ningún registro de texto.]{#logrotate-journal-fallback explanation="La presencia de registros de texto no combina los dos sistemas de conservación."}
:::

## Resumen

Ahora puedes diseñar y comprobar una política de rotación de registros de archivos sin confundirla con un archivo histórico.

1. Equilibra los requisitos de espacio, operación y conservación.
2. Define las generaciones, la compresión, la propiedad y el comportamiento con archivos vacíos.
3. Coordínate de forma segura con las aplicaciones que mantienen descriptores abiertos.
4. Depura la configuración antes de una rotación real controlada.
5. Gestiona por separado la conservación del diario y de los almacenes externos.
