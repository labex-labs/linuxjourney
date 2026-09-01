---
lesson_id: "udev"
course_id: "devices"
lang: "es"
order_index: 5
title: "udev"
description: "Aprende cómo udev procesa sucesos de dispositivos del kernel para aplicar políticas, permisos y enlaces persistentes."
meta_title: "udev - Dispositivos"
meta_description: "Aprende cómo udev gestiona dinámicamente dispositivos Linux, aplica reglas y permite examinar propiedades mediante udevadm."
meta_keywords: "udev, udevadm, gestión de dispositivos Linux, reglas udev, archivos de dispositivo, enlaces persistentes"
---

El kernel de Linux comunica al espacio de usuario los cambios de dispositivos mediante uevents. En muchas distribuciones actuales, `systemd-udevd` procesa esos sucesos utilizando reglas de udev y una base de datos de dispositivos. Junto con `devtmpfs`, que rellena el kernel, esto produce la propiedad, los permisos, las propiedades y los enlaces simbólicos que las aplicaciones ven alrededor de `/dev`.

## Del suceso del kernel a la política de dispositivos

Cuando se añade, cambia, mueve o elimina un dispositivo, udev puede:

- leer atributos de sysfs y propiedades del suceso
- aplicar una política de propietario, grupo y modo a un nodo de dispositivo
- añadir enlaces simbólicos estables como `/dev/disk/by-id/...`
- etiquetar dispositivos para otros servicios
- ejecutar un procesamiento auxiliar definido de forma limitada

El kernel sigue siendo responsable del dispositivo real y de su controlador. Eliminar un nodo de `/dev` no retira físicamente el hardware, y crear manualmente un nodo con `mknod` no hace que exista hardware incompatible ni vincula un controlador.

:::single-choice{#udev-kernel-event-input} ¿Qué activa normalmente el procesamiento de udev ante un cambio de dispositivo?

::option[Una actualización de repositorios de paquetes realizada por APT.]{#udev-apt-refresh explanation="Las actualizaciones de metadatos de paquetes no guardan relación con el procesamiento de sucesos de dispositivos activos."}
::option[Que un usuario cambie manualmente el nombre de todos los archivos bajo `/dev`.]{#udev-manual-renaming explanation="Los sucesos del kernel y las reglas impulsan la política dinámica, no un cambio manual masivo de nombres."}
::option[Un uevent del kernel que describe la acción del dispositivo.]{#udev-kernel-uevent .correct explanation="Udev recibe sucesos de dispositivos del kernel y aplica las reglas del espacio de usuario que coincidan."}
:::

## Ubicaciones y precedencia de las reglas

Las reglas suelen encontrarse en:

- `/usr/lib/udev/rules.d/` para reglas proporcionadas por fabricantes o paquetes
- `/run/udev/rules.d/` para reglas volátiles durante la ejecución
- `/etc/udev/rules.d/` para la política del administrador local

Los archivos se procesan según el orden lexicográfico de sus nombres; los archivos del mismo nombre situados en directorios de mayor prioridad sustituyen a las versiones de menor prioridad conforme a la implementación de udev instalada. Las reglas locales deben utilizar un nombre de archivo elegido deliberadamente y coincidir con propiedades estables, no con nombres de enumeración.

Una regla puede afectar a todos los dispositivos coincidentes, así que prueba cuidadosamente su alcance. No edites directamente reglas de paquetes cuando resulte apropiada una regla local que las sustituya o complemente.

:::single-choice{#udev-local-rules-directory} ¿Qué directorio está destinado a las reglas persistentes de udev del administrador local?

::option[`/proc/udev/rules.d/`]{#udev-proc-rules explanation="Procfs no proporciona el directorio persistente de reglas locales."}
::option[`/etc/udev/rules.d/`]{#udev-etc-rules .correct explanation="La política local corresponde a `/etc`, separada de las reglas de fabricantes gestionadas por paquetes."}
::option[`/dev/udev/rules.d/`]{#udev-dev-rules explanation="`/dev` contiene objetos activos orientados a dispositivos, no configuración persistente de reglas."}
:::

## Examinar un dispositivo con `udevadm`

Consulta las propiedades de udev de un nodo existente:

```bash
$ udevadm info --query=all --name=/dev/sda
```

Utiliza un nodo que exista en el sistema actual. `udevadm info --attribute-walk --name=...` puede mostrar atributos a lo largo de la cadena de padres de sysfs, lo que ayuda a crear una regla. `udevadm monitor --kernel --udev --property` observa los sucesos del kernel y los procesados; puede exponer identificadores de dispositivos, así que trata adecuadamente la salida capturada.

:::single-choice{#udev-info-purpose} ¿Qué solicita `udevadm info --query=all --name=/dev/sda`?

::option[Una reescritura destructiva de la tabla de particiones del disco.]{#udev-info-partition-write explanation="La consulta es una operación de inspección y no formatea ni vuelve a particionar el almacenamiento."}
::option[La instalación desde Internet de un controlador del kernel que falta.]{#udev-info-install-driver explanation="La inspección mediante udevadm no actúa como descargador de paquetes."}
::option[Las propiedades de udev conocidas del nodo de dispositivo indicado.]{#udev-info-properties .correct explanation="La orden info consulta la base de datos de dispositivos y la información asociada de sysfs."}
:::

## Aplicar cuidadosamente cambios en las reglas

Recargar los archivos de reglas afecta al procesamiento de sucesos futuros; no reconstruye automáticamente el estado de todos los dispositivos existentes. Activar sucesos manualmente puede afectar a muchos dispositivos y servicios, por lo que debes limitar el destino y utilizar la documentación de `udevadm` instalada. Una orden de prueba puede simular la evaluación de reglas, pero quizá no reproduzca todos los efectos secundarios de un suceso real.

Haz una copia de seguridad de las reglas locales, valida la sintaxis, observa un único dispositivo de prueba conocido y conserva una vía de recuperación antes de cambiar permisos o nombres. Evita realizar trabajos prolongados directamente durante el procesamiento de sucesos de udev; delégalos en un servicio apropiado.

:::single-choice{#udev-reload-effect} ¿Qué cambia principalmente al recargar las reglas de udev?

::option[La forma en que se procesan los sucesos posteriores de dispositivos coincidentes.]{#udev-future-events .correct explanation="La recarga actualiza las reglas en memoria; todavía debe producirse o activarse deliberadamente un suceso para que se vuelva a evaluar un dispositivo."}
::option[El cableado físico de todos los dispositivos conectados.]{#udev-physical-wiring explanation="Cargar reglas de software no puede cambiar las conexiones del hardware."}
::option[Todos los nodos de dispositivo existentes, con independencia de los sucesos o las coincidencias.]{#udev-all-existing explanation="Una recarga por sí sola no garantiza la reevaluación inmediata de todos los dispositivos actuales."}
:::

Utiliza [Explorar dispositivos de hardware en Linux](https://labex.io/labs/comptia-explore-hardware-devices-in-linux-590861) para relacionar las propiedades de `udevadm`, las rutas de sysfs y los enlaces de `/dev` en un entorno controlado.

## Resumen

Ahora puedes situar udev entre los sucesos del kernel y la política de dispositivos del espacio de usuario.

1. Relaciona los uevents y los atributos de sysfs con la coincidencia de reglas de udev.
2. Separa las ubicaciones de reglas de fabricantes, de ejecución y locales.
3. Examina las propiedades y el flujo de sucesos con `udevadm`.
4. Recarga y activa reglas únicamente con un alcance limitado y probado.
