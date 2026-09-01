---
lesson_id: "authentication-logging"
course_id: "logging"
lang: "es"
order_index: 5
title: "Registro de autenticación"
description: "Aprende a localizar, interpretar y correlacionar de forma segura los registros de autenticación de Linux."
meta_title: "Registro de autenticación - Logging"
meta_description: "Explora el registro de autenticación de Linux mediante el archivo /var/log/auth.log. Esta guía ayuda a comprender los inicios de sesión, los métodos de autenticación y el diagnóstico de problemas de acceso para mejorar la seguridad."
meta_keywords: "autenticación Linux, auth.log, registro Linux, inicio de sesión usuario, seguridad Linux, autorización sistema, solucionar inicio sesión, métodos autenticación, principiante, tutorial, guía, log seguro"
---

Los registros de autenticación ayudan a explicar los intentos de inicio de sesión, los cambios de privilegios y la actividad de las sesiones. Son pruebas sensibles desde el punto de vista de la seguridad, pero una sola línea rara vez permite establecer la intención de un usuario o demostrar que una cuenta ha sido comprometida.

## Localizar los registros de autenticación

Las configuraciones syslog de la familia Debian suelen dirigir los eventos de autenticación a `/var/log/auth.log`; las de la familia Red Hat suelen utilizar `/var/log/secure`. Un diario de systemd puede conservar los mismos eventos con metadatos de la unidad y el proceso, y un sistema centralizado de registros puede contener la copia de referencia.

Descubre el destino local y consulta el servicio pertinente, por ejemplo:

```bash
$ sudo journalctl -u ssh.service --since '1 hour ago'
$ sudo less /var/log/auth.log
```

La unidad SSH puede llamarse `ssh.service` o `sshd.service`. Los permisos suelen restringir estos registros porque exponen detalles sobre cuentas y accesos.

:::single-choice{#auth-logs-file-location} ¿Dónde deben almacenarse siempre los eventos de autenticación de Linux?

::option[En el destino elegido por la política local de registro.]{#auth-logs-local-policy .correct explanation="Los archivos, el diario y los recolectores centralizados varían según la distribución y la configuración."}
::option[En `/var/log/auth.log` en todas las distribuciones.]{#auth-logs-auth-only explanation="Esa ruta es habitual en los sistemas de la familia Debian, pero no es universal."}
::option[Dentro del archivo de historial del shell de cada usuario.]{#auth-logs-shell-history explanation="El historial del shell contiene comandos de usuario, no es el almacén de eventos de autenticación del sistema."}
:::

## Interpretar un evento

Un registro tradicional puede contener:

```text
Jan 31 10:37:50 icebox pkexec: pam_unix(polkit-1:session): session opened for user root by (uid=1000)
```

Esto identifica la hora, la máquina, el programa emisor, el módulo y el servicio PAM, el usuario solicitado para la sesión y el UID de origen. Por sí solo, no identifica a la persona que estaba detrás del UID 1000 ni demuestra que la acción fuera maliciosa. Resuelve el UID con los registros de cuentas válidos en el momento del incidente y correlaciona la terminal, la dirección remota, la sesión y los eventos circundantes.

:::single-choice{#auth-logs-uid-inference} ¿Qué establece `uid=1000` en este registro?

::option[Que la contraseña de root se escribió incorrectamente mil veces.]{#auth-logs-thousand-passwords explanation="El valor es un número de identidad, no un contador de intentos."}
::option[La identidad numérica de la cuenta asociada al proceso que inició la acción.]{#auth-logs-numeric-identity .correct explanation="Para atribuir la acción a una persona se necesitan más pruebas de la sesión y de la cuenta."}
::option[Que el evento se originó en el puerto TCP 1000.]{#auth-logs-port explanation="Un UID no es un campo de puerto de red."}
:::

## Investigar éxitos y fallos

Busca tanto los intentos aceptados como los rechazados dentro de un intervalo limitado. Para SSH, examina también el origen de la conexión, el método de autenticación, la cuenta de destino, la apertura y el cierre de la sesión y los reinicios del servicio. Los fallos repetidos pueden deberse a un error del usuario, a automatizaciones con credenciales obsoletas, a exploraciones o a un ataque; la frecuencia por sí sola no permite elegir una explicación.

`last` y `lastb` pueden resumir registros de `wtmp` y `btmp` cuando se mantienen, pero esas bases de datos binarias tienen sus propios límites de conservación e integridad. Contrástalas con los registros del diario o de syslog y con las fuentes centralizadas.

:::single-choice{#auth-logs-failed-attempts} ¿Con qué deben correlacionarse los intentos repetidos de inicio de sesión fallidos?

::option[Únicamente con el espacio libre total del disco.]{#auth-logs-disk-space explanation="La capacidad no identifica el origen, la cuenta de destino ni el método de un intento de autenticación."}
::option[Con el origen, la cuenta de destino, el método, el momento y las sesiones satisfactorias.]{#auth-logs-correlated-fields .correct explanation="Estos detalles ayudan a distinguir errores de configuración, errores de usuarios, exploraciones y accesos no autorizados."}
::option[Con la conclusión de que la cuenta está sin duda comprometida.]{#auth-logs-certain-compromise explanation="Los fallos pueden tener varias causas benignas u hostiles."}
:::

## Conservar y responder

Si se sospecha de un incidente, registra la hora y la zona horaria de la máquina, conserva los registros originales y sus metadatos y protege todas las copias exportadas. Evita editar las pruebas en su ubicación original. Bloquear cuentas, cambiar el cortafuegos y terminar sesiones puede interrumpir accesos legítimos o alertar a un atacante, así que sigue el proceso de respuesta a incidentes y conserva una vía de recuperación.

:::single-choice{#auth-logs-preservation} ¿Cómo deben tratarse las pruebas de autenticación durante una investigación?

::option[Editar las líneas sospechosas en el archivo original para hacerlas más claras.]{#auth-logs-edit-original explanation="Modificar la fuente daña la integridad de las pruebas."}
::option[Publicar el registro completo para que cualquiera pueda identificar a los usuarios.]{#auth-logs-publish explanation="Los registros de autenticación pueden exponer identidades sensibles y detalles de la infraestructura."}
::option[Conservar los originales y proteger las copias exportadas.]{#auth-logs-preserve .correct explanation="Tanto la integridad como la confidencialidad son importantes para los registros de seguridad."}
:::

## Resumen

Ahora puedes examinar eventos de autenticación sin afirmar más de lo que demuestra un único registro.

1. Descubre el destino de los registros de autenticación configurado localmente.
2. Interpreta en su contexto los campos de identidad, servicio, método y sesión.
3. Correlaciona la actividad fallida y satisfactoria entre las fuentes conservadas.
4. Preserva las pruebas y coordina las medidas de respuesta que puedan causar interrupciones.
