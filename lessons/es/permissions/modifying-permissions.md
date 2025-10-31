---
index: 2
lang: "es"
title: "Modificar Permisos"
meta_title: "Modificar Permisos - Permisos"
meta_description: "Aprenda a cambiar permisos en Linux usando el comando chmod. Esta guía cubre métodos simbólicos y numéricos para ayudarle a administrar el acceso a archivos y directorios de forma segura. Domine el proceso de cambio de permisos de Linux para una mejor administración del sistema."
meta_keywords: "cambiar permiso linux, modificar permiso linux, cómo cambiar permisos en linux, cómo cambiar permisos de archivo linux, chmod, permisos de archivo, seguridad linux, permisos simbólicos, permisos numéricos"
---

## Lesson Content

Cuando necesite modificar los derechos de acceso de archivos o directorios, la herramienta principal que utilizará es el comando `chmod` (change mode, cambiar modo). Comprender **cómo cambiar permisos en Linux** es una habilidad fundamental para cualquier usuario. El comando `chmod` ofrece dos métodos principales para esta tarea: el modo simbólico y el modo numérico.

### Usando el Modo Simbólico

El modo simbólico a menudo se considera más legible porque utiliza letras para representar usuarios y permisos. Primero especifica qué conjunto de permisos desea cambiar (usuario, grupo u otros), luego usa un `+` para agregar un permiso o un `-` para eliminarlo.

- `u` (user/propietario)
- `g` (group/grupo)
- `o` (others/otros)
- `a` (all/todos: usuario, grupo y otros)

Veamos **cómo cambiar permisos de archivos linux** con algunos ejemplos.

Para agregar el permiso de ejecución para el usuario en un archivo, usaría:

```bash
chmod u+x archivo
```

Este comando agrega (`+`) el permiso ejecutable (`x`) para el usuario (`u`) en `archivo`.

Para eliminar un permiso, use el operador `-`. Por ejemplo, para eliminar el permiso de escritura para el grupo:

```bash
chmod g-w archivo
```

También puede modificar varios permisos a la vez. El siguiente comando agrega el permiso de escritura tanto para el usuario como para el grupo:

```bash
chmod ug+w archivo
```

### Usando el Modo Numérico (Octal)

Otra forma poderosa que ofrece **change permission linux** es a través del modo numérico u octal. Este método le permite establecer todos los permisos para el usuario, el grupo y los demás simultáneamente con un número de tres dígitos.

Los permisos están representados por los siguientes valores:

- `4`: lectura (r)
- `2`: escritura (w)
- `1`: ejecución (x)

Para establecer un conjunto de permisos, suma los números. Por ejemplo, para otorgar permisos de lectura, escritura y ejecución, usaría `4 + 2 + 1 = 7`.

Veamos un ejemplo común:

```bash
chmod 755 archivo
```

¿Cómo funciona este comando de **linux change permission**? Analicemos el número `755`:

- **7 (Usuario):** `4 + 2 + 1` -> El usuario obtiene permisos de lectura, escritura y ejecución (`rwx`).
- **5 (Grupo):** `4 + 0 + 1` -> El grupo obtiene permisos de lectura y ejecución (`r-x`).
- **5 (Otros):** `4 + 0 + 1` -> Todos los demás usuarios obtienen permisos de lectura y ejecución (`r-x`).

### Consideraciones de Seguridad

Aunque `chmod` es esencial, es crucial usarlo con cuidado. Cambiar los permisos sin comprender las implicaciones puede exponer archivos sensibles a modificaciones o visualizaciones no autorizadas. Por ejemplo, establecer recursivamente permisos `777` (`chmod -R 777 /algun/directorio`) es una práctica común pero peligrosa que otorga a todos acceso total de lectura, escritura y ejecución. Siempre aplique el principio de mínimo privilegio, otorgando solo los permisos que sean estrictamente necesarios.

## Exercise

¡La práctica hace al maestro! Aquí hay algunos laboratorios prácticos para reforzar su comprensión de los permisos de archivos de Linux:

1.  **[Linux User Group and File Permissions](https://labex.io/es/labs/linux-linux-user-group-and-file-permissions-18002)** - Aprenda conceptos esenciales de administración de usuarios y grupos de Linux, incluida la comprensión de los permisos de archivos y la manipulación de la propiedad de los archivos. Este laboratorio proporciona experiencia práctica para asegurar un entorno Linux multiusuario.
2.  **[Add New User and Group](https://labex.io/es/labs/linux-add-new-user-and-group-17987)** - En este desafío, simulará la adición de nuevos miembros del equipo a un entorno de servidor, creando nuevas cuentas de usuario, configurando grupos personalizados y administrando membresías de grupos, lo que a menudo implica establecer los permisos apropiados.

Estos laboratorios le ayudarán a aplicar los conceptos de permisos de usuario, grupo y otros en escenarios reales y a ganar confianza en la gestión del acceso en Linux.

## Quiz Question

¿Qué número representa el permiso de lectura cuando se utiliza el formato numérico?

## Quiz Answer

4
