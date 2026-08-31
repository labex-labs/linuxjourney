---
lesson_id: "samba"
course_id: "network-sharing"
lang: "es"
order_index: 5
title: "Samba"
description: "Aprende a configurar, validar, utilizar y proteger un recurso compartido Samba básico."
meta_title: "Samba - Uso compartido en red"
meta_description: "Aprende a configurar un recurso compartido Samba en Linux. Esta guía explica el protocolo Samba, la instalación, la configuración y el uso de clientes SMB en Linux."
meta_keywords: "Samba, smb linux, linux smb, red samba, protocolo samba, smb samba, compartir archivos, smb.conf, cifs, smbclient, tutorial Linux"
---

Samba implementa el protocolo Server Message Block en sistemas tipo Unix y permite que clientes Linux, Windows, macOS y otros compartan archivos e impresoras. Las implementaciones modernas utilizan dialectos SMB actuales; el término antiguo CIFS aún aparece en las herramientas cliente de Linux, pero no debe interpretarse como una razón para habilitar el obsoleto SMB1.

## Planificar el recurso compartido

Antes de instalar o cambiar Samba, define los clientes autorizados, las identidades, las necesidades de lectura y escritura, la zona de red, quien es responsable de los datos, la política de copias de seguridad y el dialecto SMB necesario. Utiliza un directorio dedicado en vez de exponer por accidente un directorio personal o del sistema.

El acceso está controlado tanto por la política de Samba como por los permisos subyacentes del sistema de archivos. Permitir escrituras en `smb.conf` no puede conceder a una cuenta un acceso al sistema de archivos que no posee.

:::single-choice{#samba-two-permission-layers}
¿Qué debe permitir que un usuario escriba mediante un recurso Samba?

::option[Únicamente el comentario visible del recurso.]{#samba-comment-permission explanation="Un comentario es texto descriptivo y no concede acceso."}
::option[Tanto las reglas de Samba como los permisos del sistema de archivos.]{#samba-policy-and-filesystem .correct explanation="La solicitud debe superar las reglas del protocolo y la autorización del sistema de archivos local."}
::option[Únicamente la configuración del fondo de escritorio del cliente.]{#samba-wallpaper explanation="La apariencia del cliente no controla los archivos del servidor."}
:::

## Definir un recurso compartido básico

La configuración principal suele estar en `/etc/samba/smb.conf`. Este es un ejemplo restringido:

```ini
[team]
    path = /srv/samba/team
    browseable = yes
    read only = no
    valid users = @teamshare
```

Crea el directorio y aplica una propiedad y unos permisos revisados para el grupo Unix:

```bash
$ sudo install -d -o root -g teamshare -m 2770 /srv/samba/team
```

El bit set-group-ID ayuda a que las entradas nuevas hereden el grupo del directorio, pero el acceso colaborativo también puede requerir una ACL o una máscara de creación elegida con cuidado. Prueba los resultados reales para archivos y directorios en vez de suponer que la herencia es suficiente.

:::single-choice{#samba-valid-users}
¿Qué expresa `valid users = @teamshare`?

::option[Todos los usuarios anónimos de la red reciben acceso de escritura.]{#samba-every-anonymous explanation="La regla restringe el acceso en vez de habilitar escrituras de invitados."}
::option[El servidor debe cambiar el nombre del recurso a `teamshare`.]{#samba-rename-share explanation="El nombre visible del recurso sigue siendo el de la sección `[team]`."}
::option[Esta regla del recurso solo permite a los miembros del grupo indicado.]{#samba-valid-group .correct explanation="La forma con `@` hace referencia a un grupo en la sintaxis de listas de usuarios de Samba."}
:::

## Configurar la identidad

En una configuración Samba independiente, una cuenta generalmente necesita una identidad Unix correspondiente y una credencial Samba habilitada:

```bash
$ sudo smbpasswd -a alice
```

Las implementaciones con un dominio de directorio utilizan un diseño de identidades diferente. No pongas contraseñas en el historial del shell ni en configuraciones que puedan leer usuarios ajenos, y no supongas que una contraseña Samba coincide automáticamente con la de la cuenta Unix.

:::single-choice{#samba-password-database}
¿Qué suele hacer `smbpasswd -a alice` en un servidor independiente?

::option[Elimina el directorio personal del usuario Unix.]{#samba-delete-home explanation="La orden administra credenciales Samba y no elimina directorios personales."}
::option[Añade o inicializa las credenciales Samba de la cuenta.]{#samba-add-credential .correct explanation="La base de datos de autenticación SMB se administra por separado de la mera creación de un usuario Unix."}
::option[Monta todos los recursos SMB visibles como Alice.]{#samba-mount-all explanation="Registrar credenciales en el servidor es independiente de montar desde un cliente."}
:::

## Validar y aplicar la configuración

Comprueba la configuración interpretada antes de recargar los servicios:

```bash
$ testparm -s
```

Revisa los valores predeterminados inesperados y los errores; después recarga mediante el gestor de servicios de la distribución el servicio Samba. Los nombres del servicio varían y suelen incluir `smbd.service` o `smb.service`. Cuando es posible, una recarga causa menos interrupciones que un reinicio, pero aun así debes verificar el estado, los sockets a la escucha, el alcance del cortafuegos y los registros.

Prueba desde un cliente con un usuario explícito:

```bash
$ smbclient //server.example.net/team -U alice
```

:::single-choice{#samba-testparm-purpose}
¿Por qué debes ejecutar `testparm -s` antes de aplicar un cambio de Samba?

::option[Copia todos los archivos compartidos en un servidor de respaldo.]{#samba-testparm-backup explanation="La herramienta analiza y muestra la configuración; no copia los datos compartidos."}
::option[Valida y muestra la configuración efectiva de Samba.]{#samba-testparm-validate .correct explanation="La salida del analizador detecta errores y revela los ajustes interpretados antes de afectar al servicio."}
::option[Concede privilegios administrativos a todos los clientes.]{#samba-testparm-admin explanation="La validación no modifica la autorización de los clientes."}
:::

## Montar desde Linux

Los clientes Linux suelen utilizar el controlador del sistema de archivos `cifs` y sus herramientas auxiliares de montaje. Evita las contraseñas en la línea de órdenes porque los argumentos pueden filtrarse por el historial o la inspección de procesos. Utiliza un archivo de credenciales legible solo por root o un mecanismo de credenciales aprobado:

```bash
$ sudo mount -t cifs //server.example.net/team /mnt/team \
    -o credentials=/root/.smb-team,vers=3.1.1
```

Protege el archivo de credenciales, confirma el dialecto compatible con ambos extremos y define deliberadamente los requisitos de UID, GID, permisos y cifrado. Después del montaje, verifica con `findmnt`, realiza pruebas autorizadas de lectura y escritura y desmonta tras coordinar a los usuarios activos.

:::single-choice{#samba-command-line-password}
¿Por qué debes evitar `password=...` directamente en una orden de montaje?

::option[Puede exponer el secreto mediante el historial o los argumentos del proceso.]{#samba-password-exposure .correct explanation="Una fuente de credenciales protegida reduce la divulgación accidental, aunque también requiere permisos cuidadosos."}
::option[SMB no admite ninguna forma de autenticación con contraseña.]{#samba-no-passwords explanation="La autenticación SMB con contraseña es habitual, aunque también existen otros sistemas de identidad."}
::option[La opción hace que el recurso sea permanentemente de solo lectura.]{#samba-password-readonly explanation="La ubicación del secreto no determina la política de escritura."}
:::

## Resumen

Ahora puedes configurar un recurso Samba teniendo en cuenta la seguridad del protocolo y del sistema de archivos.

1. Define primero los clientes, las identidades, el alcance de red y la política de datos.
2. Restringe el recurso y ajusta los permisos subyacentes.
3. Administra las credenciales Samba con el modelo de identidad correcto.
4. Valida con `testparm` y realiza una prueba cliente de extremo a extremo.
5. Protege las credenciales cliente y verifica el acceso montado.
