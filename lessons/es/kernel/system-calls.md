---
lesson_id: "system-calls"
course_id: "kernel"
lang: "es"
order_index: 3
title: "Llamadas al sistema"
description: "Aprende cómo el código del espacio de usuario invoca servicios del kernel de Linux y cómo inspeccionar llamadas de forma segura con `strace`."
meta_title: "Llamadas al sistema - Kernel"
meta_description: "Explora los fundamentos de las llamadas al sistema en Linux. Aprende cómo los procesos del espacio de usuario solicitan servicios al kernel, cambian de modo y utilizan la tabla de llamadas. Usa `strace` para observarlas en acción."
meta_keywords: "llamada al sistema linux, llamadas al sistema, tabla syscall, modo kernel, modo usuario, strace, kernel linux, API syscall"
---

Una llamada al sistema es una entrada definida al kernel mediante la cual el código del espacio de usuario solicita una operación, como abrir un archivo, asignar memoria, crear un proceso o enviar datos por la red. El kernel valida los argumentos, las credenciales, el estado de los objetos y la política de seguridad antes de realizar la solicitud.

## Bibliotecas y ABI de llamadas al sistema

Las aplicaciones suelen llamar a funciones de la biblioteca de C en lugar de escribir instrucciones de entrada específicas de la arquitectura. Un envoltorio de biblioteca prepara los registros y la memoria según la ABI de llamadas al sistema, entra en el kernel y traduce el resultado a la convención del lenguaje.

La relación no siempre es de una función por cada llamada al sistema:

- una función de biblioteca puede combinar varias llamadas al sistema
- algunas funciones operan por completo en el espacio de usuario
- una función vDSO optimizada puede obtener ciertos datos mantenidos por el kernel sin una transición completa de modo
- una llamada al sistema puede dar soporte a muchas API de mayor nivel

:::single-choice{#system-calls-library-wrapper} ¿Qué hace un envoltorio típico de libc para una llamada al sistema?

::option[Prepara los argumentos de la ABI, entra en el kernel y traduce el resultado.]{#system-calls-wrapper-role .correct explanation="El envoltorio oculta las convenciones de llamada específicas de la arquitectura tras una interfaz de biblioteca normal."}
::option[Concede a la aplicación acceso sin restricciones a la memoria del kernel.]{#system-calls-wrapper-unrestricted explanation="La entrada al kernel sigue estando controlada y valida la solicitud."}
::option[Vuelve a compilar el kernel cada vez que se llama a la función.]{#system-calls-wrapper-compile explanation="Una llamada durante la ejecución utiliza el kernel que ya está en funcionamiento."}
:::

## Entrar y salir del kernel

El envoltorio coloca un número de llamada al sistema y sus argumentos en las ubicaciones definidas por la arquitectura, y después ejecuta una instrucción de entrada como `syscall` en x86-64 o `svc` en AArch64. El procesador cambia a un punto de entrada privilegiado configurado y el kernel distribuye la solicitud.

Al terminar, el kernel devuelve un valor o una indicación de error. Los envoltorios de la biblioteca de C suelen devolver `-1` y establecer el `errno` local del hilo cuando se produce un error. Otros lenguajes y entornos de ejecución exponen tipos de error diferentes.

Llamar «interrupción de software» a todas las entradas es impreciso en las arquitecturas actuales; las trampas, las instrucciones rápidas de llamadas al sistema y las llamadas al supervisor implementan de maneras distintas transiciones controladas relacionadas.

:::single-choice{#system-calls-entry-result} ¿Quién valida los argumentos y la autorización de una llamada al sistema?

::option[El indicador del shell antes de que se inicie el proceso.]{#system-calls-shell-validates explanation="Un proceso puede realizar llamadas al sistema sin depender de un shell, y las comprobaciones del kernel siguen siendo necesarias."}
::option[La implementación en el kernel del servicio solicitado.]{#system-calls-kernel-validates .correct explanation="El manejador privilegiado comprueba los punteros, el estado de los objetos, las credenciales y la política antes de actuar."}
::option[La tabla de particiones del disco.]{#system-calls-partition-validates explanation="Los metadatos de la disposición del almacenamiento no autorizan servicios arbitrarios del kernel."}
:::

## Números y compatibilidad

Los números de las llamadas al sistema y sus convenciones de llamada son específicos de cada arquitectura. La misma llamada simbólica puede tener un número o una disposición de estructuras diferente en otra ABI. Las versiones del kernel pueden añadir llamadas al sistema, mientras que las ABI estables del espacio de usuario intentan conservar el comportamiento existente.

Un proceso sin privilegios no puede insertar manejadores arbitrarios nuevos en la tabla de llamadas al sistema del kernel activo. Ampliar la interfaz requiere código del kernel y un diseño cuidadoso de la ABI. Funciones como seccomp pueden filtrar qué llamadas tiene permitido realizar un proceso, pero no crean nuevas implementaciones en el kernel.

:::single-choice{#system-calls-number-portability} ¿Por qué debe una aplicación evitar codificar directamente números de llamadas al sistema de otra arquitectura?

::option[Los números y las convenciones de llamada son específicos de la ABI.]{#system-calls-abi-specific .correct explanation="Un número con un significado en una arquitectura puede identificar otra operación o no existir en otra."}
::option[Las llamadas al sistema reciben sus nombres del directorio de trabajo actual.]{#system-calls-directory-names explanation="Los nombres de ruta no definen la ABI de numeración de llamadas al sistema."}
::option[Cada proceso recibe una tabla aleatoria de llamadas al sistema al iniciarse.]{#system-calls-random-table explanation="La ABI del kernel activo es estable para una arquitectura, no se aleatoriza para cada proceso."}
:::

## Rastrear con `strace`

Rastrea un comando sencillo y guarda la salida por separado:

```bash
$ strace -o trace.log -- ls
```

Cuando dispongas de autorización, sigue los procesos hijo con `-f` o limita la salida mediante una expresión como:

```bash
$ strace -f -e trace=%file -o trace.log -- command
```

`strace` puede revelar rutas, argumentos, datos derivados del entorno, direcciones de red, fragmentos del contenido de archivos y credenciales pasadas incorrectamente mediante argumentos. Almacena los rastros con permisos restrictivos y elimínalos de acuerdo con la política de datos de incidentes.

:::single-choice{#system-calls-strace-purpose} ¿Qué observa principalmente `strace`?

::option[Únicamente las líneas de código fuente ejecutadas dentro de la aplicación.]{#system-calls-strace-source-lines explanation="El rastreo en el nivel del código fuente requiere depuradores o instrumentación con símbolos."}
::option[Las llamadas al sistema y las señales en el límite entre el usuario y el kernel.]{#system-calls-strace-boundary .correct explanation="Informa de solicitudes, argumentos, resultados y eventos de señales de los procesos rastreados."}
::option[El voltaje físico de cada núcleo de la CPU.]{#system-calls-strace-voltage explanation="La telemetría del hardware queda fuera del rastreo de llamadas al sistema."}
:::

## Interpretar los rastros con cuidado

El rastreo altera los tiempos y puede imponer una sobrecarga considerable. Una llamada fallida puede ser una comprobación esperada, y el último error visible puede ser consecuencia de una operación anterior o de la política de la aplicación. Interpreta los descriptores de archivo, sigue las relaciones entre procesos y relaciona los resultados con los registros de la aplicación.

Los permisos y la política de seguridad de ptrace restringen qué procesos pueden rastrearse. No te conectes al proceso de otro usuario o a uno de producción sin autorización; las suspensiones y los cambios de tiempos pueden afectar al comportamiento del servicio.

:::single-choice{#system-calls-strace-failure} ¿Significa necesariamente que la aplicación está averiada el hecho de que falle una llamada al sistema en un rastro?

::option[Sí; cualquier valor de retorno distinto de cero termina Linux inmediatamente.]{#system-calls-nonzero-terminates explanation="Las aplicaciones gestionan habitualmente errores de llamadas al sistema sin que falle el sistema."}
::option[No; los programas suelen probar alternativas y gestionar errores esperados.]{#system-calls-expected-failure .correct explanation="Interpreta el valor devuelto en el contexto del flujo de control y de la aplicación, no de forma aislada."}
::option[Sí; el kernel nunca devuelve errores esperados.]{#system-calls-no-expected-errors explanation="Errores como rutas inexistentes u operaciones no compatibles son resultados normales de una API."}
:::

## Resumen

Ahora puedes seguir una llamada al sistema desde la API de una biblioteca hasta el trabajo validado del kernel.

1. Distingue las funciones de alto nivel de la ABI de llamadas al sistema.
2. Relaciona las instrucciones de entrada de la arquitectura con la distribución controlada del kernel.
3. Trata los números y las estructuras de las llamadas al sistema como elementos específicos de la arquitectura.
4. Usa salidas filtradas de `strace` y protege los datos sensibles.
5. Interpreta los fallos y la sobrecarga del rastreo en el contexto de la aplicación.
