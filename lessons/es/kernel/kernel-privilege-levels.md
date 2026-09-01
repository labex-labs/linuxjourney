---
lesson_id: "kernel-privilege-levels"
course_id: "kernel"
lang: "es"
order_index: 2
title: "Niveles de privilegio"
description: "Aprende cómo los privilegios del procesador separan la ejecución de los usuarios de la ejecución de confianza del kernel."
meta_title: "Niveles de privilegio - Kernel"
meta_description: "Explora los conceptos esenciales de los niveles de privilegio de Linux. Esta lección explica la diferencia entre modo kernel y modo usuario, la función de los anillos de protección y cómo las llamadas al sistema proporcionan acceso privilegiado al hardware."
meta_keywords: "niveles de privilegio Linux, modo kernel, modo usuario, anillos de protección, llamadas al sistema, acceso privilegiado, privilegios del kernel, diferencia modo kernel y modo usuario, seguridad Linux"
---

Los procesadores proporcionan modos de privilegio que restringen las instrucciones delicadas y el acceso a la memoria. Linux utiliza este límite del hardware para que los fallos de aplicaciones ordinarias no puedan sobrescribir directamente la memoria del kernel ni reconfigurar dispositivos. El kernel controla las transiciones hacia la ejecución privilegiada.

## Modo de usuario

Un proceso normal se ejecuta en modo de usuario dentro de su espacio de direcciones virtuales. Puede realizar cálculos libremente y acceder a las asignaciones de memoria que le haya concedido el kernel, que pueden ser grandes; modo de usuario no significa «solo una pequeña cantidad de memoria». No puede acceder directamente a memoria física arbitraria, a las asignaciones privadas de otro proceso ni a los controles privilegiados del procesador.

Las tablas de páginas y los bits de protección imponen el control de acceso a la memoria. Si un hilo hace referencia a una dirección no válida o no permitida, el procesador transfiere el control al kernel, que puede resolver un fallo de página válido o entregar una señal como `SIGSEGV`.

:::single-choice{#kernel-privilege-user-mode-memory} ¿A qué memoria puede acceder normalmente de forma directa un proceso en modo de usuario?

::option[A todas las direcciones de la RAM física y a toda la memoria del kernel.]{#kernel-privilege-all-physical explanation="Los privilegios y la protección de la memoria virtual impiden esos accesos."}
::option[Únicamente a un byte fijo elegido cuando se inicia el proceso.]{#kernel-privilege-one-byte explanation="Un proceso puede tener muchas regiones asignadas y seguir careciendo de privilegios."}
::option[A las asignaciones permitidas de su propio espacio de direcciones virtuales.]{#kernel-privilege-own-mappings .correct explanation="Las protecciones de páginas del hardware restringen el proceso a las asignaciones establecidas con el acceso apropiado."}
:::

## Modo kernel

El modo kernel permite ejecutar instrucciones privilegiadas y acceder a las asignaciones protegidas del kernel necesarias para gestionar la memoria, planificar, procesar interrupciones y controlar dispositivos. En x86, esta separación de Linux suele describirse como ring 0 para el kernel y ring 3 para los procesos de usuario. Linux normalmente no utiliza los rings 1 y 2 para el aislamiento ordinario de procesos.

Otras arquitecturas emplean nombres y mecanismos distintos, como los niveles de excepción. La virtualización añade relaciones entre hipervisor e invitados que no encajan en un dibujo sencillo de dos anillos. La idea esencial es el privilegio controlado, no los números de los anillos de x86 en sí mismos.

:::single-choice{#kernel-privilege-x86-kernel-ring} ¿Qué anillo de protección de x86 ejecuta normalmente el kernel de Linux?

::option[Ring 3.]{#kernel-privilege-ring-three explanation="Ring 3 es el nivel de privilegio convencional del modo de usuario."}
::option[Ring 0.]{#kernel-privilege-ring-zero .correct explanation="El kernel utiliza el anillo tradicional de x86 con más privilegios."}
::option[Ring 7.]{#kernel-privilege-ring-seven explanation="Los anillos de protección tradicionales de x86 se numeran del 0 al 3."}
:::

## Transiciones controladas

Varios eventos transfieren el control a un punto de entrada del kernel:

- una instrucción de llamada al sistema solicita un servicio del kernel
- una excepción informa de una condición como un fallo de página o una instrucción no válida
- una interrupción de hardware informa de un evento externo

El procesador guarda el contexto de ejecución, cambia el privilegio según los mecanismos de entrada configurados y comienza a ejecutar código de confianza del kernel. El kernel valida la solicitud y el estado, realiza o rechaza el trabajo y después vuelve al modo de usuario cuando corresponde.

La aplicación no se convierte temporalmente en código del kernel. La CPU ejecuta un manejador del kernel en nombre del hilo, con pilas y asignaciones controladas por el kernel.

:::single-choice{#kernel-privilege-system-call-transition} ¿Qué sucede durante la transición de una llamada al sistema?

::option[El código de usuario de la aplicación recibe acceso sin restricciones para ejecutarse en ring 0.]{#kernel-privilege-user-ring-zero explanation="Después de la entrada controlada solo se ejecuta código de confianza del kernel."}
::option[El proceso cambia permanentemente su UID a cero.]{#kernel-privilege-uid-zero explanation="La transición del modo del procesador no modifica las credenciales del usuario."}
::option[El control entra en un manejador definido del kernel que valida la solicitud.]{#kernel-privilege-kernel-handler .correct explanation="El procesador cambia de modo mediante una ruta de entrada configurada y conserva el contexto de usuario para poder volver."}
:::

## El privilegio de la CPU no es la identidad del usuario

Una aplicación que se ejecuta como el usuario `root` de Linux normalmente sigue haciéndolo en modo de usuario. El UID 0 influye en las comprobaciones de autorización del kernel, pero no permite que sus instrucciones accedan directamente a la memoria del kernel. A la inversa, el código del kernel se ejecuta en modo privilegiado independientemente del usuario cuya llamada al sistema haya provocado su ejecución.

Las capacidades, los espacios de nombres, seccomp, los módulos de seguridad y los cgroups restringen aún más lo que un proceso puede solicitar. Esta política por capas es independiente del límite entre los modos de usuario y kernel impuesto por el hardware.

:::single-choice{#kernel-privilege-root-distinction} ¿Qué afirmación compara correctamente la identidad root y el modo kernel?

::option[Root es una credencial del espacio de usuario; el modo kernel es un privilegio de ejecución del procesador.]{#kernel-privilege-credential-versus-mode .correct explanation="Un proceso root realiza solicitudes autorizadas desde el modo de usuario, mientras que el código de confianza del kernel lleva a cabo la ejecución privilegiada."}
::option[Todas las instrucciones que pertenecen a root se ejecutan como código cargable del kernel.]{#kernel-privilege-root-kernel-code explanation="Ser propiedad de un UID no transforma un ejecutable en un módulo del kernel."}
::option[El modo kernel es otro nombre de usuario almacenado en `/etc/passwd`.]{#kernel-privilege-kernel-username explanation="Los modos del procesador son estados del hardware, no cuentas de inicio de sesión."}
:::

## Por qué importa este límite

El límite reduce los daños que pueden causar los errores ordinarios y proporciona un punto para las comprobaciones de acceso, pero las vulnerabilidades del kernel y los módulos maliciosos pueden superarlo. Mantén el kernel y el firmware actualizados mediante canales de confianza, reduce al mínimo el código privilegiado y evita cargar módulos que no sean de confianza.

Los problemas de ejecución especulativa y los canales laterales también demuestran que el aislamiento del hardware requiere mitigaciones continuas; estar en un «anillo distinto» es una base, no una prueba de seguridad completa.

:::single-choice{#kernel-privilege-boundary-limit} ¿Garantiza la separación entre modo de usuario y modo kernel la seguridad completa del sistema?

::option[Sí; las vulnerabilidades del kernel no pueden afectar a los procesos de usuario.]{#kernel-privilege-no-kernel-vulns explanation="Una vulnerabilidad del kernel puede comprometer todo el sistema."}
::option[No; los fallos del código privilegiado y los canales laterales aún pueden atravesar los límites previstos.]{#kernel-privilege-not-complete .correct explanation="La separación de modos reduce la superficie de ataque, pero debe combinarse con código correcto del kernel y mitigaciones adicionales."}
::option[Sí; los modos del hardware eliminan la necesidad de políticas de control de acceso.]{#kernel-privilege-no-policy explanation="Las credenciales y las políticas de seguridad siguen siendo esenciales para compartir recursos de forma autorizada."}
:::

## Resumen

Ahora puedes distinguir los privilegios de ejecución del hardware de la autoridad de una cuenta de Linux.

1. Relaciona el modo de usuario con los espacios de direcciones virtuales protegidos.
2. Relaciona el modo kernel con las instrucciones y asignaciones privilegiadas.
3. Trata las llamadas al sistema, las excepciones y las interrupciones como entradas controladas.
4. Distingue la autorización del UID 0 de la ejecución en ring 0.
5. Considera los modos de privilegio como una capa de un diseño de seguridad más amplio.
