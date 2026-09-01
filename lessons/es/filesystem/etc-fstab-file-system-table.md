---
lesson_id: "etc-fstab-file-system-table"
course_id: "filesystem"
lang: "es"
order_index: 7
title: "/etc/fstab"
description: "Aprende a definir conexiones persistentes de sistemas de archivos e intercambio en `/etc/fstab` y a validarlas de forma segura."
meta_title: "/etc/fstab - El sistema de archivos"
meta_description: "Aprende a utilizar /etc/fstab para definir montajes persistentes y áreas de intercambio y a validar sus entradas con seguridad."
meta_keywords: "fstab Linux, /etc/fstab, montar sistemas de archivos, arranque Linux, UUID, fsck"
---

`/etc/fstab`, la tabla de sistemas de archivos, declara sistemas de archivos, áreas de intercambio, montajes enlazados, fuentes de red y otras conexiones que las herramientas del sistema pueden montar o activar. Las entradas pueden participar en el arranque, pero opciones como `noauto`, la integración de montajes automáticos y la política del gestor de servicios influyen en cuándo o si ocurre.

## Los seis campos

Una entrada convencional tiene seis campos separados por espacios en blanco:

```text
UUID=130b882f-7d79-436d-a096-1e594c92bb76 /data ext4 defaults,nosuid,nodev 0 2
```

1. **Fuente**: una ruta de dispositivo, `UUID=`, `LABEL=`, una fuente de red u otra especificación compatible.
2. **Destino**: punto de montaje, o `none` para usos como el intercambio cuando corresponda.
3. **Tipo**: tipo de sistema de archivos, `swap`, `none` o un tipo automático aceptado.
4. **Opciones**: una lista separada por comas que interpretan los auxiliares de montaje y las capas de integración.
5. **Campo dump**: controla históricamente la utilidad de copias `dump`; `0` suele desactivar la participación.
6. **Campo pass**: controla el orden de `fsck` durante el arranque cuando corresponda; `0` desactiva la comprobación automática mediante este mecanismo.

Los espacios en blanco dentro de un campo deben escaparse mediante sintaxis de fstab, como `\040` para un espacio. Un `#` inicia un comentario fuera de un campo.

:::single-choice{#fstab-field-count} ¿Cuántos campos contiene una entrada normal de `/etc/fstab`?

::option[Cuatro.]{#fstab-four-fields explanation="A la fuente, el destino, el tipo y las opciones les siguen los campos dump y pass."}
::option[Ocho.]{#fstab-eight-fields explanation="Ocho no es el número estándar de campos de un registro de fstab."}
::option[Seis.]{#fstab-six-fields .correct explanation="El formato tradicional contiene fuente, destino, tipo, opciones, dump y pass."}
:::

## Identificadores estables de fuentes

Para sistemas de archivos locales, un UUID suele ser más estable que la enumeración `/dev/sdX`:

```bash
$ lsblk -f
$ sudo blkid
```

Utiliza `UUID=...` únicamente después de confirmar que el identificador pertenece al sistema de archivos pretendido. Volver a darle formato crea un UUID nuevo y los clones a nivel de bloques pueden duplicarlo. `PARTUUID=` identifica en cambio una entrada de la tabla de particiones y tiene una semántica diferente.

:::single-choice{#fstab-uuid-source} ¿Qué identifica normalmente `UUID=...` en el campo de fuente?

::option[La cuenta de usuario propietaria del punto de montaje.]{#fstab-user-uuid explanation="La identidad de la cuenta no se selecciona mediante la sintaxis de fuente del UUID del sistema de archivos."}
::option[Los metadatos del sistema de archivos que contienen ese UUID.]{#fstab-filesystem-uuid .correct explanation="Mount resuelve el identificador del sistema de archivos a un dispositivo de bloques disponible en vez de depender del nombre de enumeración."}
::option[El proceso que desmontó por última vez el sistema de archivos.]{#fstab-process-uuid explanation="El historial de procesos no se codifica mediante este campo de fuente."}
:::

## Opciones de montaje y campos de comprobación

`defaults` se expande a un conjunto convencional de opciones definido por la implementación; no es necesariamente la política más segura para todos los montajes. Añade opciones según la confianza y la carga de trabajo, como acceso de solo lectura o restricciones sobre nodos de dispositivo y comportamiento setuid. Los sistemas de archivos de red y extraíbles pueden necesitar políticas de tiempo de espera, dependencias o tolerancia a fallos para que el arranque no se bloquee inesperadamente.

En sistemas de archivos compatibles con `fsck`, el sistema raíz utiliza convencionalmente pass `1` y los demás sistemas locales comprobados, pass `2`. Las prácticas específicas pueden diferir; por ejemplo, algunos tipos no utilizan el fsck genérico durante el arranque. Sigue la documentación del sistema de archivos y la distribución instalados en vez de asignar `2` mecánicamente.

:::single-choice{#fstab-pass-zero} ¿Qué solicita el valor `0` en el sexto campo?

::option[Omitir para esa entrada el orden automático de fsck mediante fstab.]{#fstab-pass-zero-skip .correct explanation="Pass cero excluye la entrada de la secuencia de comprobación durante el arranque gobernada por este campo."}
::option[Montar el sistema de archivos como solo lectura en todas las circunstancias.]{#fstab-pass-zero-readonly explanation="El comportamiento de solo lectura pertenece al campo de opciones de montaje."}
::option[Borrar el sistema de archivos antes de cada arranque.]{#fstab-pass-zero-erase explanation="El campo pass no da formato ni borra un sistema de archivos."}
:::

## Editar con una vía de recuperación

Una entrada no válida de la raíz, del arranque o de una red necesaria puede interrumpir el inicio. Antes de editar:

1. Confirma una copia de seguridad actual y acceso a consola o rescate.
2. Copia el archivo existente conservando sus permisos.
3. Verifica la identidad de la fuente y crea el punto de montaje previsto.
4. Realiza un solo cambio limitado.
5. Valídalo y pruébalo antes de reiniciar.

No introduzcas credenciales directamente en una entrada de fstab legible por todos. Utiliza el mecanismo protegido de credenciales del auxiliar de montaje correspondiente.

:::single-choice{#fstab-editing-recovery} ¿Por qué debe confirmarse el acceso de rescate antes de cambiar una entrada crítica de fstab?

::option[Porque editar fstab siempre borra inmediatamente la tabla de particiones.]{#fstab-no-partition-erase explanation="Editar el texto no reescribe las particiones, aunque los montajes posteriores pueden tener efectos."}
::option[Porque el archivo solo puede editarse desde otro sistema operativo.]{#fstab-other-os-only explanation="Puede editarse en Linux con privilegios y salvaguardas apropiados."}
::option[Porque una entrada incorrecta puede impedir que el arranque normal alcance un sistema utilizable.]{#fstab-boot-failure .correct explanation="Los fallos de montajes críticos pueden entrar en modo de emergencia o bloquear servicios dependientes."}
:::

## Validar sin dar por supuesto el éxito

Empieza con una comprobación estática cuando sea compatible:

```bash
$ sudo findmnt --verify --verbose
```

Después prueba la entrada nueva concreta bajo condiciones controladas, confírmala con `findmnt` y desmóntala si la prueba era temporal. `mount -a` intenta muchas entradas aptas y puede contactar redes o conectar fuentes no pretendidas; también omite entradas ya montadas y con `noauto`, por lo que no es ni un comprobador de sintaxis inofensivo ni una prueba completa.

En sistemas basados en systemd, vuelve a cargar la configuración del gestor después de editar fstab para actualizar las unidades de montaje generadas y verifica después las dependencias y el comportamiento de arranque conforme a la documentación local.

:::single-choice{#fstab-mount-a-limit} ¿Por qué `mount -a` no constituye por sí solo una validación completa de fstab?

::option[Porque siempre vuelve a dar formato a todos los dispositivos antes de montarlos.]{#fstab-mount-a-formats explanation="Mount no suele crear sistemas de archivos."}
::option[Porque puede omitir entradas y realizar amplias operaciones reales de montaje en vez de comprobar solo la sintaxis.]{#fstab-mount-a-incomplete .correct explanation="Los registros ya montados o con `noauto` pueden no probarse, mientras que las fuentes aptas pueden tener efectos reales."}
::option[Porque solo lee el historial del shell e ignora fstab.]{#fstab-mount-a-history explanation="La orden sí consulta fstab para las entradas aptas."}
:::

Practica en [Gestionar particiones y sistemas de archivos de Linux](https://labex.io/labs/comptia-manage-linux-partitions-and-filesystems-590845) con el almacenamiento secundario del laboratorio, seguro para recuperación.

## Resumen

Ahora puedes leer y validar una entrada persistente de la tabla de sistemas de archivos.

1. Analiza los campos fuente, destino, tipo, opciones, dump y pass.
2. Selecciona un identificador verificado con la semántica de identidad pretendida.
3. Elige la política de montaje y comprobación para el sistema de archivos real.
4. Conserva el acceso de rescate y realiza un solo cambio limitado.
5. Combina validación estática, montaje dirigido y comprobaciones de la política de arranque.
