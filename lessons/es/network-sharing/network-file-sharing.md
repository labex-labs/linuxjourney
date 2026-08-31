---
lesson_id: "network-file-sharing"
course_id: "network-sharing"
lang: "es"
order_index: 1
title: "Descripción general del intercambio de archivos"
description: "Aprende a elegir y realizar de forma segura una transferencia de archivos basada en SSH mediante scp."
meta_title: "Descripción general del intercambio de archivos - Network Sharing"
meta_description: "Explora el intercambio de archivos en Linux. Aprende a utilizar comandos como scp para realizar transferencias seguras por la red, una habilidad esencial para trabajar con Linux."
meta_keywords: "intercambio de archivos linux, comando scp, copia segura, aprender comandos linux, curso linux gratuito, programar en linux, transferencia de archivos por red, recursos para aprender linux"
---

El movimiento de archivos por red abarca desde copias puntuales hasta recursos compartidos montados continuamente y árboles de directorios sincronizados. Elige un método según la dirección, el tamaño de los datos, la frecuencia de actualización, el modelo de identidades, la confianza en la red, los requisitos de metadatos y si los clientes necesitan acceso compartido activo.

## Elegir un método de transferencia

- `scp` o SFTP proporciona una copia autenticada mediante SSH o una transferencia interactiva.
- `rsync` reconcilia eficazmente árboles de directorios de forma local o mediante un transporte como SSH.
- NFS presenta exportaciones del servidor como sistemas de archivos montados, normalmente entre hosts de tipo Unix.
- SMB, implementado por Samba en Linux, permite el acceso compartido entre muchos sistemas operativos.
- HTTP puede proporcionar descargas sencillas, pero no es un sistema de archivos montado de propósito general.

Una copia no es automáticamente una copia de seguridad. Un diseño de copias de seguridad también necesita una conservación independiente, pruebas de restauración, comprobaciones de integridad y protección frente a la misma eliminación o vulneración.

:::single-choice{#file-sharing-one-time-ssh-copy}
¿Qué herramienta resulta apropiada para copiar un archivo una sola vez mediante SSH?

::option[`scp`]{#file-sharing-scp .correct explanation="SCP utiliza la autenticación y el transporte SSH para copiar archivos."}
::option[`uptime`]{#file-sharing-uptime explanation="Uptime informa del tiempo de actividad y la carga del host, no transfiere archivos."}
::option[`logrotate`]{#file-sharing-logrotate explanation="Logrotate gestiona las generaciones de registros de archivos en un host."}
:::

## Comprender las rutas de scp

La forma general es `scp SOURCE DESTINATION`. Un operando remoto suele utilizar `user@host:path`:

```bash
$ scp -- report.txt alice@example.net:/srv/incoming/
$ scp -- alice@example.net:/srv/outgoing/result.txt ./result.txt
```

El primer comando envía un archivo local; el segundo obtiene un archivo remoto. Los dos puntos distinguen el host remoto de su ruta. Pon entre comillas las rutas que contengan caracteres especiales del shell y evita nombres de archivo no confiables que resulten ambiguos.

:::single-choice{#file-sharing-scp-pull-source}
En una descarga mediante `scp`, ¿dónde aparece la especificación remota?

::option[Como origen antes del destino local.]{#file-sharing-pull-source .correct explanation="La dirección de la copia sigue el orden de operandos origen-destino."}
::option[Como destino local después de todas las opciones.]{#file-sharing-pull-destination explanation="El objeto remoto que se obtiene es el operando de origen."}
::option[Únicamente dentro del archivo de configuración SSH del usuario.]{#file-sharing-pull-config explanation="La configuración SSH puede proporcionar valores predeterminados, pero la ruta remota que se copia sigue siendo un operando."}
:::

## Copiar un directorio

Utiliza el modo recursivo para un árbol de directorios:

```bash
$ scp -r -- project/ alice@example.net:/srv/incoming/
```

Antes de copiar, inspecciona el tamaño de los datos, los enlaces simbólicos, los permisos, los requisitos de propiedad, el espacio libre y los nombres de destino. SCP no es una política de sincronización; las copias repetidas de directorios pueden dejar en el destino archivos que ya no existen en el origen.

:::single-choice{#file-sharing-scp-recursive}
¿Qué solicita `scp -r`?

::option[Eliminar el destino remoto antes de copiar.]{#file-sharing-scp-remove explanation="El modo recursivo recorre directorios y no define una política de limpieza."}
::option[Copiar recursivamente un árbol de directorios.]{#file-sharing-scp-tree .correct explanation="La opción es necesaria cuando el origen seleccionado es un directorio."}
::option[Acceso de solo lectura a la configuración SSH.]{#file-sharing-scp-readonly explanation="La opción se ocupa del recorrido de directorios, no del acceso a la configuración."}
:::

## Comprobar la identidad y los resultados

La comprobación de la clave del host SSH protege frente a la conexión con el servidor equivocado. Trata una clave de host modificada como un evento que debe verificarse mediante un canal de confianza en lugar de omitir la advertencia. Utiliza cuentas con privilegios mínimos y un tratamiento de claves apropiado para el entorno.

Después de la transferencia, comprueba el estado de salida, los archivos esperados, los tamaños, los metadatos y, cuando los requisitos de integridad lo exijan, hashes calculados de forma independiente en ambos extremos. Confirma que la aplicación de destino pueda leer realmente los datos.

:::single-choice{#file-sharing-host-key-change}
¿Qué debes hacer cuando SSH informa de un cambio inesperado en la clave del host?

::option[Deshabilitar la comprobación de claves de host para todas las transferencias futuras.]{#file-sharing-disable-checking explanation="Esto elimina un control importante de identidad del servidor."}
::option[Verificar la clave nueva mediante una fuente de confianza antes de continuar.]{#file-sharing-verify-key .correct explanation="La advertencia puede indicar que el host se reconstruyó, que el destino es incorrecto o que existe una interceptación, y debe investigarse."}
::option[Publicar la clave privada de autenticación en la salida del comando.]{#file-sharing-publish-key explanation="Las credenciales privadas no deben exponerse."}
:::

## Resumen

Ahora puedes seleccionar y comprobar una copia segura y puntual de archivos por red.

1. Adapta el método de intercambio a las necesidades de acceso y conservación.
2. Interpreta los operandos locales y remotos de `scp` según el origen y el destino.
3. Utiliza deliberadamente el modo recursivo para árboles de directorios.
4. Comprueba la identidad del servidor, los resultados de la transferencia y la usabilidad en el destino.
