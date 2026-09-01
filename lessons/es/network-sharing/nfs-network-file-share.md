---
lesson_id: "nfs-network-file-share"
course_id: "network-sharing"
lang: "es"
order_index: 4
title: "NFS"
description: "Aprende a descubrir, montar, validar y automatizar con seguridad un montaje cliente NFS."
meta_title: "NFS - Uso compartido en red"
meta_description: "Descubre cómo utilizar Network File System (NFS) en Linux. Esta lección explica el cliente NFS, la orden mount y el montaje automático de recursos de red."
meta_keywords: "NFS, cliente NFS, montaje automático, Network File System, redes Linux, orden mount, tutorial Linux, principiantes"
---

Network File System permite que un cliente acceda a una exportación de un servidor a través del espacio de nombres del sistema de archivos local. El servidor controla las exportaciones y gran parte de la política de acceso; el cliente controla dónde y cuándo se monta una exportación autorizada.

## Preparar el cliente

Instala las utilidades cliente de NFS de la distribución, normalmente incluidas en `nfs-common` en sistemas de la familia Debian o en `nfs-utils` en los de la familia Red Hat. Confirma con quien administra el servidor la resolución DNS o el alcance de la dirección, las versiones NFS permitidas, la política del cortafuegos y la ruta exacta de la exportación.

`showmount -e SERVER` puede enumerar exportaciones proporcionadas mediante el protocolo de montaje antiguo, pero no es concluyente para todos los servidores que solo usan NFSv4. Que la enumeración falle no demuestra que no exista una exportación NFSv4 autorizada.

:::single-choice{#nfs-showmount-limit} ¿Por qué puede estar incompleta la salida de `showmount -e` para un servidor NFSv4?

::option[Consulta un protocolo antiguo de enumeración de exportaciones que quizá no esté expuesto.]{#nfs-showmount-protocol .correct explanation="NFSv4 puede funcionar sin que ese servicio independiente de enumeración esté disponible."}
::option[Solo muestra la temperatura de la CPU local.]{#nfs-showmount-temperature explanation="La orden consulta información sobre las exportaciones de un servidor NFS."}
::option[Desactiva permanentemente todas las exportaciones enumeradas.]{#nfs-showmount-disables explanation="La enumeración es una solicitud de descubrimiento de solo lectura."}
:::

## Montar una exportación

Crea un punto de montaje vacío y dedicado, y monta la exportación aprobada:

```bash
$ sudo mkdir -p /mnt/team
$ sudo mount -t nfs server.example.net:/srv/team /mnt/team
```

Especifica una versión solo cuando lo requieran la política o la compatibilidad; por ejemplo, `-o vers=4.2`. No adivines opciones de rendimiento o seguridad. Confirma el origen, el tipo y las opciones resultantes:

```bash
$ findmnt --target /mnt/team
```

:::single-choice{#nfs-mount-operands} En la orden de montaje, ¿qué es `server.example.net:/srv/team`?

::option[El directorio local que oculta la exportación remota.]{#nfs-local-mountpoint explanation="El punto de montaje local del ejemplo es `/mnt/team`."}
::option[El nombre del paquete cliente que se debe instalar.]{#nfs-package-name explanation="Los nombres de los paquetes dependen de la distribución y no son operandos del origen de montaje."}
::option[El servidor y la ruta remota exportada.]{#nfs-remote-export .correct explanation="El host y la ruta que sigue a los dos puntos identifican el origen NFS."}
:::

## Comprender las identidades y los permisos

El acceso NFS combina las reglas de exportación del servidor, la seguridad del protocolo, las identidades numéricas o los servicios de directorio y los permisos del sistema de archivos. Que dos hosts muestren el mismo nombre de usuario no garantiza que tengan el mismo ID numérico. El mecanismo tradicional `AUTH_SYS` envía identidades numéricas proporcionadas por el cliente y depende en gran medida de que los controles del cliente y de la red sean de confianza; los entornos más exigentes pueden utilizar modos de seguridad Kerberos cuando están configurados de extremo a extremo.

El servidor suele asignar la identidad root remota a una identidad sin privilegios mediante el aislamiento de root. No desactives esa protección solo para resolver un error de permisos; inspecciona los ID, la propiedad del directorio, la política de exportación y el modelo de seguridad previsto.

:::single-choice{#nfs-name-versus-id} ¿Por qué dos usuarios con el mismo nombre visible pueden recibir permisos NFS distintos?

::option[Los permisos NFS pueden depender de la asignación de identidades numéricas.]{#nfs-numeric-mapping .correct explanation="Que los nombres coincidan no demuestra que el cliente y el servidor resuelvan el mismo UID y los mismos grupos."}
::option[NFS ignora todos los permisos del sistema de archivos.]{#nfs-ignores-permissions explanation="Los permisos del sistema de archivos y de la exportación siguen formando parte de la autorización."}
::option[Cada montaje cambia automáticamente la base de datos de cuentas del servidor.]{#nfs-changes-accounts explanation="El montaje de un cliente no reescribe las identidades del servidor."}
:::

## Automatizar montajes de red

Un montaje sencillo mediante `/etc/fstab` durante el arranque puede retrasar el inicio cuando la red o el servidor no están disponibles. Según el host, utiliza `autofs` para mapas bajo demanda u opciones de montaje de systemd como `_netdev,nofail,x-systemd.automount` después de probar su semántica exacta:

```fstab
server.example.net:/srv/team /mnt/team nfs4 rw,_netdev,nofail,x-systemd.automount 0 0
```

Antes de editar fstab, conserva un medio de acceso para la recuperación y valida con un analizador no destructivo o una prueba de montaje controlada. Un montaje automático mejora el comportamiento ante problemas de disponibilidad, pero no corrige la autorización, el DNS ni las caídas del servidor.

:::single-choice{#nfs-automount-benefit} ¿Cuál es una ventaja principal del montaje automático bajo demanda de un recurso NFS?

::option[Concede a todos los clientes acceso root a la exportación.]{#nfs-automount-root explanation="El momento del montaje no anula la autorización del servidor."}
::option[Puede evitar que el servidor tenga que estar disponible durante el arranque inicial.]{#nfs-automount-boot .correct explanation="La conexión se activa al acceder en vez de bloquear necesariamente el inicio temprano."}
::option[Copia todo el sistema de archivos del servidor en el disco local.]{#nfs-automount-copy explanation="Un montaje presenta acceso remoto; no es una copia local completa."}
:::

## Desmontar y verificar

Antes de desmontar, detén o coordina los procesos que utilizan el recurso y deja que las aplicaciones terminen su trabajo. Después desmonta el punto de montaje y comprueba que haya desaparecido:

```bash
$ sudo umount /mnt/team
$ findmnt --target /mnt/team
```

Un desmontaje forzado o diferido puede ocultar referencias activas y provocar errores en las aplicaciones; reserva esas opciones para un fallo diagnosticado y con un plan de recuperación explícito.

:::single-choice{#nfs-safe-unmount} ¿Qué debe preceder a un desmontaje NFS normal?

::option[Coordinar los procesos que utilizan el recurso y terminar las escrituras importantes.]{#nfs-coordinate-writers .correct explanation="Retirar un sistema de archivos activo de las aplicaciones puede interrumpir la E/S o dejar trabajo incompleto."}
::option[Eliminar el directorio exportado en el servidor.]{#nfs-delete-export explanation="Desmontar en el cliente no exige destruir los datos del servidor."}
::option[Desactivar todas las interfaces de red del cliente.]{#nfs-disable-network explanation="Eso puede dificultar una finalización ordenada y no es la secuencia normal."}
:::

## Resumen

Ahora puedes manejar un montaje cliente NFS con supuestos explícitos sobre identidad y disponibilidad.

1. Confirma las herramientas cliente, la ruta exportada, el protocolo y la política de red.
2. Monta en una ruta dedicada y verifica el origen y las opciones efectivos.
3. Diagnostica los permisos mediante las identidades y la política de exportación.
4. Utiliza un montaje bajo demanda probado cuando importe la disponibilidad durante el arranque.
5. Coordina a quienes lo utilizan, desmonta de forma normal y verifica su retirada.
