---
lesson_id: "host-file-integrity"
course_id: "system-auditing"
lang: "es"
order_index: 3
title: "Integridad de archivos"
description: "Aprende a comparar el contenido y los permisos de un archivo mediante un hash y sus metadatos."
meta_title: "Integridad de archivos - Auditoría de sistemas"
meta_description: "Aprende a comparar el contenido y los permisos de un archivo mediante un hash y sus metadatos."
meta_keywords: "integridad de archivos, auditoría de sistemas, ciberseguridad, Linux Journey"
---

Una comprobación de integridad permite saber si un archivo sigue coincidiendo con una referencia. Comprueba el contenido y los metadatos por separado. El contenido son los bytes del archivo. Los **metadatos** incluyen detalles como los permisos de acceso.

## Registrar el hash del contenido

Crea un pequeño archivo de configuración en un directorio de prácticas vacío. La redirección reemplaza los archivos existentes con ese nombre, así que usa un directorio nuevo.

```bash
$ printf '%s\n' 'mode=preview' > site.conf
$ sha256sum site.conf
```

El primer campo es el **hash**, un valor de longitud fija que se calcula a partir de los bytes del archivo. Usa más adelante el mismo método en el mismo archivo. Si el hash cambia, los bytes de entrada son distintos.

:::single-choice{#host-file-integrity-changed-hash} El valor SHA-256 cambia después de editar el archivo. ¿Qué muestra la comparación?

::option[Su contenido difiere de los bytes medidos antes.]{#host-file-integrity-changed-hash-a .correct explanation="El hash cambia según el contenido que se usa en el cálculo."}
::option[La edición se hizo necesariamente sin autorización.]{#host-file-integrity-changed-hash-b explanation="La autorización se comprueba por separado."}
::option[Seguro que cambiaron los permisos de una cuenta.]{#host-file-integrity-changed-hash-c explanation="Un hash de contenido no registra permisos."}
:::

## Registrar los permisos del archivo

En Linux, `stat -c` muestra los metadatos que elijas. El campo `%a` muestra el modo numérico de los permisos y `%n` muestra el nombre.

```bash
$ stat -c '%a %n' site.conf
```

El modo inicial exacto puede depender de cómo se creó el archivo. Regístralo junto con el hash del contenido para poder comparar ambas propiedades más adelante.

:::single-choice{#host-file-integrity-mode-vs-content} El hash coincide con la referencia y stat muestra un modo distinto. Según estas comprobaciones, ¿qué cambió?

::option[Cambiaron los bytes del archivo y el modo quedó igual.]{#host-file-integrity-mode-vs-content-a explanation="El hash coincide y el modo difiere."}
::option[El archivo se eliminó con seguridad.]{#host-file-integrity-mode-vs-content-c explanation="Ambas comprobaciones devolvieron información sobre el archivo."}
::option[Cambiaron sus permisos y el hash del contenido observado se mantuvo igual.]{#host-file-integrity-mode-vs-content-b .correct explanation="Estas dos herramientas miden propiedades diferentes."}
:::

## Probar un cambio de modo

El siguiente comando cambia a `640` los permisos de este archivo de prácticas. Concede permisos de lectura y escritura al propietario y permiso de lectura al grupo. Repite las dos comprobaciones y compara los resultados.

```bash
$ chmod 640 site.conf
$ stat -c '%a %n' site.conf
$ sha256sum site.conf
```

El modo debería ser 640 y el hash del contenido debería coincidir con la primera medición.

:::single-choice{#host-file-integrity-repeat-check} ¿Qué comprobación detectaría una edición posterior de mode=preview dentro del archivo?

::option[Solo el nombre de archivo que muestra stat.]{#host-file-integrity-repeat-check-a explanation="El nombre puede seguir siendo el mismo tras la edición."}
::option[Una nueva comprobación SHA-256 comparada con la original.]{#host-file-integrity-repeat-check-c .correct explanation="Un cambio en el contenido produciría un hash distinto."}
::option[Solo la cifra de permisos del propietario.]{#host-file-integrity-repeat-check-b explanation="Los cambios de permisos son independientes de la mayoría de las ediciones del contenido."}
:::

![Salida registrada en LabEx que muestra el cambio del modo de permisos a 640 sin que cambie el hash del contenido](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/system-auditing/host-file-integrity/mode-vs-content.png)

## Resumen

Ya puedes comparar de forma independiente el contenido y los permisos de acceso de un archivo.

1. Registra un hash SHA-256 del contenido.
2. Consulta el modo con stat.
3. Verifica el efecto de un cambio de permisos.
