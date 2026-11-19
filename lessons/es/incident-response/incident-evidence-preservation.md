---
lesson_id: "incident-evidence-preservation"
course_id: "incident-response"
lang: "es"
order_index: 2
title: "Preservación de pruebas"
description: "Aprende a conservar un registro de prácticas, su copia y su suma de comprobación para poder revisarlos después."
meta_title: "Preservación de pruebas - Respuesta a incidentes"
meta_description: "Aprende a conservar un registro de prácticas, su copia y su suma de comprobación para poder revisarlos después."
meta_keywords: "preservación de pruebas, respuesta a incidentes, ciberseguridad, Linux Journey"
---

Durante la respuesta a un incidente, un fragmento de registro puede ayudar a explicar qué pasó. Conserva la fuente original o la exportación autorizada junto con los datos que necesitará quien revise la prueba más adelante.

## Registrar el contexto

Anota el equipo, la fuente, la zona horaria y el intervalo. Indica quién recogió los registros y qué filtro usó. Sin ese contexto, una línea copiada podría tener el mismo texto que una línea de otro equipo.

:::single-choice{#incident-evidence-preservation-context-fields} Un compañero recibe una línea que indica las 09:22 y ningún otro dato. ¿Qué debes añadir?

::option[La ruta en la que se guardó localmente la copia.]{#incident-evidence-preservation-context-fields-b explanation="La ruta de destino ayuda a localizar la copia, pero deja sin aclarar el origen y el contexto de la hora."}
::option[Una suposición sobre la causa.]{#incident-evidence-preservation-context-fields-c explanation="Registra los datos de la recogida por separado de su interpretación."}
::option[El equipo de origen, la zona horaria y el intervalo de captura.]{#incident-evidence-preservation-context-fields-a .correct explanation="Estos datos permiten situar la línea en la cronología correcta."}
:::

## Comparar una copia

En un directorio nuevo de prácticas, guarda una línea de ejemplo inofensiva, cópiala y calcula el valor SHA-256 de ambos archivos. Usa solo el archivo de ejemplo. Las escrituras reemplazan los archivos del mismo nombre que haya en ese directorio.

```bash
$ printf '%s\n' '09:22 UTC public homepage returned 503' > sample.log
$ cp sample.log review-copy.log
$ sha256sum sample.log review-copy.log
```

La primera columna muestra el hash del contenido. Los dos valores deberían coincidir. Al comprobarlos, verificas que los bytes de la copia coincidan con los del original. Para saber si el evento original se registró con exactitud hacen falta otras pruebas.

:::single-choice{#incident-evidence-preservation-copy-meaning} ¿Qué respalda la coincidencia de los hashes?

::option[La hora de origen tiene que ser correcta.]{#incident-evidence-preservation-copy-meaning-a explanation="El hash mide el contenido del archivo y no puede verificar el reloj."}
::option[Los bytes comprobados de la copia de revisión coinciden con los de la muestra.]{#incident-evidence-preservation-copy-meaning-b .correct explanation="Ambos hashes se calcularon con el mismo algoritmo."}
::option[La copia está autorizada para compartirse en público.]{#incident-evidence-preservation-copy-meaning-c explanation="La autorización determina quién puede ver el archivo. El hash no aporta ese dato."}
:::

![Salida de sumas de comprobación registrada en LabEx con hashes iguales para un archivo de prácticas y su copia de revisión](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/incident-response/incident-evidence-preservation/matching-copy-hashes.png)

## Preparar una copia segura para revisión

Conserva intacto el registro original y restringe el acceso. Si otro equipo solo necesita algunos campos, prepara un fragmento aparte y elimina de ese fragmento los datos sensibles. Deja constancia de que se acortó y conserva la referencia a su fuente protegida.

:::single-choice{#incident-evidence-preservation-redact-copy} ¿De qué archivo debes eliminar los datos sensibles antes de compartirlo?

::option[De un fragmento de revisión separado.]{#incident-evidence-preservation-redact-copy-c .correct explanation="Así se conserva la fuente y se limita el material compartido."}
::option[Del original protegido, para que cambien todas las copias.]{#incident-evidence-preservation-redact-copy-a explanation="Eso alteraría las pruebas que quieres conservar."}
::option[Del texto de la suma de comprobación, para que un archivo modificado siga pareciendo igual.]{#incident-evidence-preservation-redact-copy-b explanation="Conserva los valores medidos y los archivos a los que corresponden."}
:::

## Resumen

Ya puedes preparar pruebas que otra persona pueda interpretar.

1. Anota dónde y cuándo se recogió el material.
2. Comprueba que los bytes de la copia coincidan con los de la fuente.
3. Elimina los datos sensibles de un fragmento separado antes de compartirlo.
