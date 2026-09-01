---
lesson_id: "etc-shadow-file"
course_id: "user-management"
lang: "es"
order_index: 4
title: "/etc/shadow"
description: "Aprende cómo los registros shadow locales representan hashes de contraseñas y políticas de caducidad sin exponer datos sensibles."
meta_title: "/etc/shadow - Gestión de usuarios"
meta_description: "Explora el archivo /etc/shadow de Linux. Aprende la estructura de sus nueve campos, los hashes y marcadores de contraseña y las políticas de caducidad."
meta_keywords: "etc shadow, archivo /etc/shadow Linux, /etc/shadow, autenticación de usuarios, seguridad de contraseñas, administración de sistemas Linux"
---

`/etc/shadow` almacena campos locales protegidos de hashes de contraseñas y caducidad. Separar estos valores de la base de datos `/etc/passwd`, que suele ser legible, reduce la exposición a ataques de adivinación de contraseñas sin conexión.

## Proteger los datos shadow

Las contraseñas no se almacenan «cifradas» de forma reversible para mostrarlas posteriormente. Una entrada local de contraseña suele contener un hash unidireccional codificado con un identificador de algoritmo, un *salt* y parámetros. Un atacante que obtiene hashes puede probar contraseñas candidatas sin conexión, por lo que la base de datos debe permanecer restringida.

Los detalles exactos de propiedad y permisos varían, pero el acceso suele limitarse a root y a componentes del sistema estrictamente autorizados. No imprimas, copies, registres ni compartas el contenido de shadow únicamente para consultar el estado de una cuenta.

:::single-choice{#shadow-restricted-reason} ¿Por qué se protegen normalmente los datos shadow locales frente al acceso general de lectura?

::option[El archivo contiene la contraseña actual sin cifrar de cada usuario.]{#shadow-plaintext-passwords explanation="Las entradas shadow correctas almacenan hashes unidireccionales o marcadores especiales, no contraseñas en texto claro recuperables."}
::option[Los hashes de contraseñas pueden atacarse sin conexión si se revelan.]{#shadow-offline-guessing .correct explanation="Un atacante puede probar conjeturas de contraseñas contra hashes robados sin interactuar con el servicio de inicio de sesión."}
::option[Leerlo cambia automáticamente todas las fechas de caducidad de contraseñas.]{#shadow-read-changes explanation="Una lectura no actualiza por sí sola los campos de la política; el problema es revelar material sensible de autenticación."}
:::

## Leer el formato de nueve campos

Un registro shadow local contiene nueve campos separados por dos puntos. Este es un registro esquemático con el hash omitido deliberadamente:

```text
alice:<password-field>:20000:0:90:7:14:20500:
```

Los campos son:

1. **Nombre de inicio de sesión**.
2. **Hash de contraseña o marcador especial de contraseña**.
3. **Último cambio de contraseña**, en días desde 1970-01-01; `0` solicita un cambio en el siguiente inicio de sesión autenticado mediante contraseña con las herramientas habituales.
4. **Antigüedad mínima de la contraseña**, en días.
5. **Antigüedad máxima de la contraseña**, en días.
6. **Período de advertencia** anterior a la caducidad de la contraseña, en días.
7. **Período de inactividad** posterior a la caducidad de la contraseña, en días.
8. **Fecha de caducidad de la cuenta**, en días desde 1970-01-01.
9. **Campo reservado**.

Los campos vacíos y los valores numéricos especiales tienen significados definidos que pueden variar según el campo y las herramientas. Usa órdenes de gestión de cuentas en vez de editar valores a simple vista.

:::single-choice{#shadow-account-expiration-field} ¿Qué campo de shadow almacena la fecha de caducidad de la cuenta como días desde 1970-01-01?

::option[El campo 3]{#shadow-field-three explanation="El campo 3 registra la fecha del último cambio de contraseña, no la caducidad de la cuenta."}
::option[El campo 8]{#shadow-field-eight .correct explanation="El octavo campo es el recuento absoluto de días para la caducidad de la cuenta."}
::option[El campo 5]{#shadow-field-five explanation="El campo 5 registra la antigüedad máxima de la contraseña."}
:::

## Interpretar con cuidado el campo de contraseña

Un hash válido en el campo 2 permite verificar una contraseña Unix local. Un valor que comienza por `!` suele bloquear ese hash, mientras que `*` u otro marcador de hash no válido impide verificar correctamente una contraseña a través de ese campo. Un valor vacío es sensible para la seguridad y puede permitir un comportamiento sin contraseña según la política PAM.

Estos marcadores describen la vía de contraseña local, no todos los métodos de autenticación posibles. Las claves públicas SSH, los certificados, los tokens y las credenciales específicas de aplicaciones pueden seguir funcionando si no se restringen por separado. La caducidad de la cuenta en el campo 8 también es distinta del bloqueo de la contraseña.

:::single-choice{#shadow-password-lock-scope} ¿Qué puedes concluir con seguridad de un campo de contraseña shadow que comienza por `!`?

::option[El hash almacenado de la contraseña Unix se ha vuelto inutilizable para la verificación normal de contraseñas.]{#shadow-password-locked .correct explanation="Anteponer `!` al hash impide que coincida con una contraseña proporcionada mediante la vía de contraseña shadow."}
::option[Se han desactivado todos los métodos posibles de inicio de sesión de la cuenta.]{#shadow-all-login-disabled explanation="Otros métodos de autenticación pueden ser independientes, por lo que el marcador de contraseña no demuestra por sí solo un bloqueo total de la cuenta."}
::option[La cuenta se ha eliminado de todas las bases de datos de identidades.]{#shadow-account-deleted explanation="El registro shadow sigue existiendo y la eliminación es una operación distinta de gestión de cuentas."}
:::

## Distinguir las fechas de contraseña y cuenta

Los campos 3 a 7 se refieren a la caducidad de la contraseña: cuándo cambió por última vez, cuándo se permite otro cambio, cuándo caduca, cuándo comienzan las advertencias y durante cuánto tiempo sigue disponible el inicio mediante contraseña después de la caducidad. El campo 8 hace caducar la cuenta en un día absoluto, con independencia de la antigüedad de la contraseña.

Por ejemplo, una antigüedad máxima de 90 días no equivale a una fecha de caducidad de la cuenta. La primera se desplaza con respecto al último cambio de contraseña; la segunda permanece fija hasta que un administrador la modifica.

:::single-choice{#shadow-max-age-versus-expire} ¿Cuál es la diferencia entre los campos 5 y 8 de shadow?

::option[El campo 5 almacena el nombre de usuario y el 8 el shell de inicio de sesión.]{#shadow-username-shell explanation="El nombre de usuario es el campo 1 y el shell se registra en `/etc/passwd`, no en shadow."}
::option[El campo 5 almacena un hash de contraseña y el 8 su salt.]{#shadow-hash-salt explanation="La codificación del hash pertenece al campo 2 y los campos de caducidad no almacenan su salt por separado."}
::option[El campo 5 es la antigüedad máxima de la contraseña y el 8 una fecha absoluta de caducidad de la cuenta.]{#shadow-password-vs-account-expiry .correct explanation="La antigüedad de la contraseña es relativa al último cambio, mientras que la caducidad de la cuenta se almacena como un recuento absoluto de días."}
:::

## Consultar y cambiar la política mediante herramientas

Los administradores deben consultar únicamente la información necesaria para la tarea:

```bash
$ sudo passwd -S alice
$ sudo chage -l alice
```

`passwd -S` resume el estado de la contraseña local, mientras que `chage -l` enumera la información de caducidad en un formato legible. Los formatos de salida y los requisitos de autorización pueden variar según la distribución.

Usa `passwd`, `chage`, `usermod` y herramientas relacionadas para efectuar cambios. Si es inevitable reparar manualmente la base de datos shadow local, `vipw -s` proporciona bloqueo; valida las bases de datos de cuentas con `pwck`. Mantén una sesión de recuperación antes de realizar cambios remotos de autenticación.

:::single-choice{#shadow-list-aging-policy} ¿Qué orden está diseñada para mostrar información legible de caducidad de la contraseña de la cuenta local `alice`?

::option[`cat /etc/shadow`]{#shadow-cat-entire-file explanation="Esto expone todos los registros shadow locales y más información sensible de la necesaria para la tarea."}
::option[`passwd -d alice`]{#shadow-passwd-delete explanation="La operación `-d` elimina el hash de contraseña y cambia el estado de forma sensible para la seguridad; no es una orden de consulta."}
::option[`chage -l alice`]{#shadow-chage-list .correct explanation="La opción `-l` minúscula pide a `chage` que muestre los campos de caducidad de la contraseña en un formato legible."}
:::

PAM y NSS pueden integrar orígenes de autenticación e identidad ajenos a los archivos shadow locales. Por tanto, una cuenta del sistema puede no tener un registro shadow local o puede autenticarse mediante servicios adicionales.

Para practicar el estado de cuentas y las políticas de caducidad en un entorno controlado, prueba estos laboratorios prácticos:

1. **[Gestionar cuentas de usuario de Linux con useradd, usermod y userdel](https://labex.io/labs/comptia-manage-linux-user-accounts-with-useradd-usermod-and-userdel-590837)** - Practica todo el ciclo de administración, desde crear y proteger cuentas con `useradd` y `passwd` hasta modificarlas y eliminarlas.
2. **[Configurar cuentas de usuario y privilegios sudo en Linux](https://labex.io/labs/comptia-configure-user-accounts-and-sudo-privileges-in-linux-590856)** - Aprende técnicas esenciales para gestionar cuentas y privilegios sudo, incluidas las políticas de contraseñas y la protección de cuentas.

## Resumen

Ahora puedes interpretar la política shadow sin exponer toda la base de datos de contraseñas.

1. Trata los hashes de contraseñas como material de autenticación restringido.
2. Lee los nueve campos de shadow según su propósito.
3. Distingue el bloqueo de contraseñas de la desactivación de todos los métodos de inicio de sesión.
4. Separa la caducidad de contraseñas de la fecha absoluta de caducidad de la cuenta.
5. Consulta y cambia la política mediante herramientas de cuentas específicas.
