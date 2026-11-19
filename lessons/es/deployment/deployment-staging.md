---
lesson_id: "deployment-staging"
course_id: "deployment"
lang: "es"
order_index: 3
title: "Preproducción"
description: "Aprende qué puedes comprobar en preproducción y por qué el mismo artefacto puede comportarse de forma distinta en cada entorno."
meta_title: "Preproducción - Despliegue"
meta_description: "Aprende qué puedes comprobar en preproducción y por qué el mismo artefacto puede comportarse de forma distinta en cada entorno."
meta_keywords: "preproducción, staging, despliegue, DevOps, Linux Journey"
---

Una versión está casi lista. Ejecuta el artefacto en **preproducción** (staging), un entorno de pruebas diseñado para parecerse al servicio que van a usar los usuarios. Así puedes verificar la versión con una configuración realista antes de exponerla al tráfico de producción.

## Llevar el mismo artefacto al siguiente entorno

Usa la imagen que se probó y aprobó. Si vuelves a generarla después de que cambien las dependencias, podrías obtener otro artefacto. Anota la referencia completa de la imagen en cada despliegue.

```text
Environment  Artifact      Page configuration
staging      site@digest-A Internal preview
production   site@digest-A Public website
```

El resumen del ejemplo es simbólico. El artefacto es el mismo y los ajustes cambian según el entorno.

:::single-choice{#deployment-staging-same-artifact} ¿Qué indica que se puede llevar el mismo código empaquetado a producción?

::option[La referencia del artefacto coincide en ambos registros de despliegue.]{#deployment-staging-same-artifact-b .correct explanation="La referencia exacta vincula los dos entornos con una misma compilación."}
::option[Ambos entornos usan el mismo nombre para un puerto.]{#deployment-staging-same-artifact-a explanation="Un ajuste en común no permite saber si el artefacto es el mismo."}
::option[Se desplegaron los dos entornos el mismo día.]{#deployment-staging-same-artifact-c explanation="La fecha por sí sola no identifica qué se desplegó."}
:::

## Elegir comprobaciones representativas

Preproducción debe permitirte probar funciones importantes, como cargar la página o leer datos de una dependencia de prueba. Usa cuentas y datos de prueba autorizados. Si una comprobación en preproducción da buen resultado, aumenta la confianza en ese escenario en concreto. Las diferencias de tráfico, datos o configuración aún pueden afectar a producción.

:::single-choice{#deployment-staging-staging-scope} La página de preproducción carga con una base de datos de prueba. ¿Qué debes verificar después de desplegar en producción?

::option[Que el artefacto ya no necesita una versión.]{#deployment-staging-staging-scope-b explanation="El registro de la versión sigue siendo útil para verificar el despliegue y recuperarte de un fallo."}
::option[Que todas las peticiones de producción tendrán éxito.]{#deployment-staging-staging-scope-c explanation="Una muestra pequeña no permite anticipar todos los resultados futuros."}
::option[Que la ruta de producción funciona con la configuración aprobada.]{#deployment-staging-staging-scope-a .correct explanation="La petición en preproducción no pasó por el entorno de producción."}
:::

## Comprobar el destino antes de modificarlo

Lee el nombre y la dirección de destino antes de aplicar un despliegue. Luego usa esa misma dirección para verificar la versión nueva y las funciones importantes. Deja claro en tus notas qué corresponde a preproducción y qué a producción, para poder interpretar cada resultado.

:::single-choice{#deployment-staging-correct-target} Planeas desplegar en preproducción, pero el comando muestra la dirección de producción. ¿Qué debes hacer primero?

::option[Continuar y etiquetar después el resultado como preproducción.]{#deployment-staging-correct-target-a explanation="La dirección determina qué servicio recibe los cambios."}
::option[Detenerte y confirmar el destino previsto.]{#deployment-staging-correct-target-c .correct explanation="Así evitas aplicar el cambio en el entorno equivocado."}
::option[Hacer una prueba desde otro navegador después de desplegar.]{#deployment-staging-correct-target-b explanation="El destino debe corregirse antes de iniciar el cambio."}
:::

Para ver un ejemplo práctico de CI/CD, consulta [Despliegue continuo en preproducción](https://labex.io/tutorials/cd-deployment-to-staging-636593).

## Resumen

Ya puedes probar un artefacto aprobado en preproducción antes de llevarlo al siguiente entorno.

1. Conserva la identidad del artefacto al pasar de un entorno a otro.
2. Elige pruebas que representen acciones importantes para los usuarios.
3. Confirma el entorno antes de cambiarlo.
