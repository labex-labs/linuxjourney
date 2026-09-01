---
lesson_id: "systemd-goals"
course_id: "init"
lang: "es"
order_index: 6
title: "Objetivos de systemd"
description: "Aprende a inspeccionar, ajustar, validar, iniciar, habilitar y diagnosticar unidades de servicio de systemd."
meta_title: "Objetivos de systemd - Init"
meta_description: "Explora los objetivos de systemd y aprende a gestionar servicios de Linux con comandos esenciales de systemctl. Esta guía explica los fundamentos de los archivos de unidad, cómo iniciar, detener y habilitar servicios, y cómo consultar su estado."
meta_keywords: "systemd, systemctl, servicios Linux, archivos de unidad, objetivos systemd, gestión de servicios, unidades systemd, principiante, tutorial, guía, comandos Linux"
---

`systemctl` envía solicitudes a un gestor systemd. Esta lección se centra en las unidades de servicio del sistema. Confirma el nombre exacto de la unidad, el ámbito del gestor, las dependencias y el impacto operativo antes de cambiar su estado.

## Interpretar una unidad de servicio

Una unidad ilustrativa mínima puede tener este aspecto:

```ini
[Unit]
Description=Example worker
Wants=network-online.target
After=network-online.target

[Service]
Type=exec
ExecStart=/usr/local/bin/example-worker
Restart=on-failure

[Install]
WantedBy=multi-user.target
```

- `[Unit]` contiene la descripción y las relaciones de dependencia.
- `[Service]` define el ciclo de vida del proceso y el comportamiento específico del servicio.
- `[Install]` indica a los comandos de habilitación qué alias o enlaces de dependencia deben crear; no constituye automáticamente una dependencia activa durante la ejecución.

De forma predeterminada, `ExecStart=` no se ejecuta mediante un shell. Las tuberías, redirecciones, variables y comillas del shell no se comportan como en una línea de comandos interactiva, salvo que se invoque deliberadamente un shell explícito.

:::single-choice{#systemd-goals-install-section} ¿Cuál es el propósito principal de las directivas de `[Install]`, como `WantedBy=`?

::option[Garantizar que el proceso del servicio ya está en ejecución.]{#systemd-goals-install-running explanation="La activación durante la ejecución requiere start u otra dependencia que la desencadene."}
::option[Describir los enlaces o relaciones que se crean al habilitar la unidad.]{#systemd-goals-enable-links .correct explanation="Las operaciones de habilitación interpretan los metadatos de instalación, que son independientes del estado actual del proceso."}
::option[Ejecutar todos los comandos mediante el shell interactivo del usuario.]{#systemd-goals-install-shell explanation="De forma predeterminada, el análisis de los comandos de una unidad no utiliza un shell interactivo."}
:::

## Inspeccionar la configuración efectiva

Lista las unidades cargadas con:

```bash
$ systemctl list-units --type=service
```

Lista los archivos de unidad instalados y sus estados de habilitación con:

```bash
$ systemctl list-unit-files --type=service
```

Son perspectivas distintas: un archivo de unidad puede estar habilitado pero inactivo, activo pero deshabilitado, ser estático, generado, transitorio o estar enmascarado, y puede no aparecer en uno de los listados. Inspecciona el contenido combinado del proveedor y de los ajustes parciales con:

```bash
$ systemctl cat UNIT.service
$ systemctl show UNIT.service
```

:::single-choice{#systemd-goals-list-units-versus-files} ¿Qué muestra `list-unit-files` que no constituye el propósito principal de `list-units`?

::option[Únicamente los procesos que más CPU consumen.]{#systemd-goals-cpu-processes explanation="La clasificación de procesos por consumo de recursos queda fuera de estos comandos de inventario de unidades."}
::option[Los estados de habilitación de los archivos de unidad instalados.]{#systemd-goals-unit-file-state .correct explanation="Informa de si los archivos de unidad están habilitados, deshabilitados, son estáticos, están enmascarados y de otros estados de instalación relacionados."}
::option[Todas las líneas que se hayan escrito alguna vez en el diario.]{#systemd-goals-all-journal explanation="Las consultas del diario se realizan con `journalctl`."}
:::

## Crear un ajuste local

Usa un ajuste parcial en lugar de editar una unidad instalada por un paquete:

```bash
$ sudo systemctl edit UNIT.service
```

Después de guardar, en las implementaciones actuales systemctl normalmente pide al gestor que vuelva a cargar la configuración como parte de este flujo de edición. Sin embargo, cuando los archivos se modifican de otra forma, ejecuta:

```bash
$ sudo systemctl daemon-reload
```

`daemon-reload` vuelve a leer las definiciones de las unidades y reconstruye las dependencias. No recarga la configuración de las aplicaciones ni reinicia los servicios activos. Cuando corresponda, valida la sintaxis y las dependencias de la unidad con `systemd-analyze verify` y después revisa la unidad efectiva combinada.

:::single-choice{#systemd-goals-daemon-reload} ¿Qué hace `systemctl daemon-reload`?

::option[Obliga a todos los demonios a volver a leer la configuración de sus aplicaciones.]{#systemd-goals-reload-all-apps explanation="La recarga de una aplicación depende de cada servicio y es independiente de la configuración del gestor."}
::option[Reinicia el kernel con una versión nueva.]{#systemd-goals-reload-kernel explanation="Activar otro kernel requiere un arranque, no una recarga de las definiciones de unidades."}
::option[Vuelve a cargar las definiciones de unidades y la información de dependencias de systemd.]{#systemd-goals-reload-manager .correct explanation="Actualiza la vista de configuración del gestor sin reiniciar necesariamente los servicios."}
:::

## Estado del servicio durante la ejecución

Después de validar la configuración del servicio y conservar una vía de recuperación:

```bash
$ sudo systemctl start peanut.service
$ sudo systemctl stop peanut.service
$ sudo systemctl restart peanut.service
$ sudo systemctl reload peanut.service
```

`reload` solo funciona cuando la unidad define o admite una acción de recarga. `restart` interrumpe el proceso y puede no conseguir restaurar el servicio. Para el acceso remoto, la red, el almacenamiento o la autenticación, conserva una vía independiente mediante la consola y valida la configuración antes de actuar.

Consulta el estado y los registros con:

```bash
$ systemctl status peanut.service
$ systemctl is-active peanut.service
$ journalctl -u peanut.service -b
```

«Activo» es un estado del gestor, no una prueba de que todos los puntos de acceso de la aplicación funcionen correctamente.

:::single-choice{#systemd-goals-start-peanut} ¿Qué comando inicia ahora `peanut.service` sin cambiar por sí solo su habilitación futura?

::option[`sudo systemctl enable peanut.service`]{#systemd-goals-enable-only explanation="Enable modifica los enlaces de instalación, pero no inicia el servicio salvo que se combine con `--now`."}
::option[`sudo systemctl start peanut.service`]{#systemd-goals-start-command .correct explanation="Start solicita la activación durante la ejecución actual y es independiente de la habilitación."}
::option[`sudo systemctl daemon-reload peanut.service`]{#systemd-goals-daemon-reload-unit explanation="Daemon-reload no acepta como operando una unidad que activar y no inicia este servicio."}
:::

## Habilitar, deshabilitar y enmascarar

Gestiona los enlaces de dependencias futuros con:

```bash
$ sudo systemctl enable peanut.service
$ sudo systemctl disable peanut.service
```

Habilitar no inicia la unidad salvo que se añada `--now`. Deshabilitar no detiene una unidad en ejecución salvo que se añada `--now`. Una unidad estática puede carecer de metadatos de instalación y aun así activarse como dependencia de otra unidad.

Enmascarar enlaza la unidad con `/dev/null` y bloquea su activación normal, incluida la activación como dependencia, hasta que se quite la máscara. Es una medida más fuerte que deshabilitar y puede romper las unidades dependientes; inspecciona las dependencias inversas antes de usarla.

:::single-choice{#systemd-goals-disable-runtime} ¿Qué ocurre con un servicio que ya está en ejecución después de ejecutar `systemctl disable UNIT` sin `--now`?

::option[Se termina inmediatamente con `SIGKILL`.]{#systemd-goals-disable-kills explanation="Deshabilitar por sí solo no solicita detener el servicio actual."}
::option[Su ejecutable se elimina del sistema de archivos.]{#systemd-goals-disable-deletes explanation="Las operaciones de habilitación gestionan enlaces, no los archivos de programa instalados por paquetes."}
::option[Normalmente sigue en ejecución mientras se eliminan los enlaces de habilitación futuros.]{#systemd-goals-disable-keeps-running .correct explanation="El estado durante la ejecución y el estado de instalación son dimensiones independientes."}
:::

## Comprobar el resultado del servicio

Después de un cambio, comprueba el estado del proceso, los registros recientes, los puntos de acceso a la escucha, las unidades dependientes, la salud de la aplicación y el comportamiento tras un reinicio controlado si cambió la habilitación al arrancar. Utiliza `systemctl is-failed`, `systemctl list-dependencies` y las comprobaciones propias de la aplicación según corresponda.

## Resumen

Ahora puedes gestionar un servicio de systemd sin confundir la configuración, la ejecución y la habilitación.

1. Interpreta `[Unit]`, `[Service]` y `[Install]` según sus funciones distintas.
2. Compara el estado de las unidades cargadas con el estado de los archivos de unidad instalados.
3. Usa ajustes parciales y vuelve a cargar el gestor después de modificar archivos externamente.
4. Inicia, detén, recarga o reinicia solo después de revisar el impacto.
5. Trata la habilitación, la deshabilitación y el enmascaramiento como controles de persistencia distintos.
