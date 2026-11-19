---
lesson_id: "ci-jobs-steps-runners"
course_id: "continuous-integration"
lang: "es"
order_index: 3
title: "Trabajos, pasos y ejecutores"
description: "Aprende a identificar los trabajos, los pasos y el ejecutor en un archivo breve de GitHub Actions."
meta_title: "Trabajos, pasos y ejecutores - Integración continua"
meta_description: "Aprende a identificar los trabajos, los pasos y el ejecutor en un archivo breve de GitHub Actions."
meta_keywords: "trabajos, pasos, ejecutores, GitHub Actions, integración continua, DevOps, Linux Journey"
---

Un flujo de trabajo es todo el proceso automatizado. Un **trabajo** agrupa las tareas asignadas a un **ejecutor**, la máquina o el entorno que las lleva a cabo. Un **paso** es una operación dentro de un trabajo.

## Leer un flujo de trabajo sencillo

Este ejemplo ejecuta un trabajo en un ejecutor Ubuntu alojado por GitHub. Un flujo de trabajo como este se guarda en la ruta `.github/workflows/` de un repositorio de GitHub.

```yaml
name: Page check
on: push
jobs:
  check:
    runs-on: ubuntu-latest
    steps:
      - name: Get the repository
        uses: actions/checkout@v6
      - name: Find the heading
        run: grep -q '<h1>Welcome</h1>' index.html
```

El identificador del trabajo es `check`. El campo `runs-on` selecciona el entorno. `uses` invoca una acción reutilizable, en este caso para acceder a los archivos del repositorio. `run` ejecuta un comando en el ejecutor.

:::single-choice{#ci-jobs-steps-runners-job-fields} ¿Qué campo selecciona dónde se ejecuta el trabajo check?

::option[runs-on.]{#ci-jobs-steps-runners-job-fields-a .correct explanation="Indica el tipo de ejecutor para el trabajo."}
::option[uses.]{#ci-jobs-steps-runners-job-fields-b explanation="Este paso invoca la acción de checkout."}
::option[name.]{#ci-jobs-steps-runners-job-fields-c explanation="Este campo le da un nombre al flujo de trabajo."}
:::

## Seguir los pasos

Por defecto, los pasos de un trabajo se ejecutan en el orden en que aparecen. La comprobación lee un archivo del repositorio, así que el checkout va primero. Dentro del mismo trabajo, un paso posterior puede usar archivos que haya generado un paso anterior.

:::single-choice{#ci-jobs-steps-runners-step-order} ¿Qué le faltaría al paso de grep en un ejecutor nuevo si movieras el checkout detrás de él?

::option[El nombre del trabajo.]{#ci-jobs-steps-runners-step-order-a explanation="El flujo de trabajo ya ha seleccionado el trabajo."}
::option[El propio ejecutor Ubuntu.]{#ci-jobs-steps-runners-step-order-c explanation="El ejecutor se selecciona antes de ejecutar los pasos."}
::option[El archivo del proyecto que tiene que leer.]{#ci-jobs-steps-runners-step-order-b .correct explanation="El checkout pone los archivos del repositorio a disposición de la comprobación."}
:::

## Mantener separados los trabajos

Los trabajos separados pueden ejecutarse al mismo tiempo. Cada trabajo alojado por GitHub recibe su propio ejecutor, así que un archivo que se escribe en uno no está disponible en otro a menos que el flujo lo transfiera. Si un trabajo necesita que otro termine bien, declara la dependencia con `needs`. Cuando también haya que pasar archivos, usa un artefacto.

:::single-choice{#ci-jobs-steps-runners-separate-jobs} Un trabajo de compilación genera site.tar.gz. Un trabajo posterior se ejecuta en otro ejecutor alojado. ¿Cómo debe recibir el archivo?

::option[Dar por hecho que se quedó en el mismo directorio de trabajo.]{#ci-jobs-steps-runners-separate-jobs-a explanation="Cada ejecutor alojado arranca con su propio sistema de archivos."}
::option[Transferir el archivo como artefacto.]{#ci-jobs-steps-runners-separate-jobs-c .correct explanation="Puedes subirlo en un trabajo y descargarlo en el otro."}
::option[Configurar needs para que el segundo trabajo espere al primero.]{#ci-jobs-steps-runners-separate-jobs-b explanation="Needs controla el orden. El archivo generado aún debe transferirse entre los ejecutores."}
:::

Para escribir y ejecutar un flujo en un repositorio de GitHub, prueba [GitHub Actions para principiantes](https://labex.io/courses/github-actions-for-beginners). El curso práctico requiere una cuenta de GitHub.

## Resumen

Ya puedes leer las partes principales de un flujo de CI.

1. Localiza un trabajo y su ejecutor.
2. Distingue una acción reutilizable de un paso que ejecuta un comando de shell.
3. Identifica cuándo los trabajos necesitan una dependencia o una transferencia de archivos.
