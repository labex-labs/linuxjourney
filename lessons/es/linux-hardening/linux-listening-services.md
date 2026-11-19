---
lesson_id: "linux-listening-services"
course_id: "linux-hardening"
lang: "es"
order_index: 4
title: "Servicios en escucha"
description: "Aprende a interpretar una dirección de escucha en Linux y a decidir desde dónde comprobar el acceso."
meta_title: "Servicios en escucha - Endurecimiento de Linux"
meta_description: "Aprende a interpretar una dirección de escucha en Linux y a decidir desde dónde comprobar el acceso."
meta_keywords: "servicios en escucha, endurecimiento de Linux, ciberseguridad, Linux Journey"
---

Un servicio puede esperar conexiones en una dirección y un puerto concretos. Un **socket en escucha** está listo para recibir conexiones entrantes. Su dirección da una pista sobre quién puede acceder al servicio.

## Enumerar los sockets TCP en escucha

Ejecuta este comando de solo lectura en un equipo Linux de prácticas. Las opciones indican a `ss` que muestre los sockets TCP en escucha y que exprese las direcciones y los puertos con números.

```bash
$ ss -lnt
```

Fíjate en la columna de la dirección local. En el ejemplo siguiente, la vista previa web usa `127.0.0.1:8091`. El puerto es 8091. La dirección es de **bucle local** y se refiere al propio equipo.

:::single-choice{#linux-listening-services-local-listener} En este ejemplo, un navegador del mismo equipo necesita abrir la vista previa. ¿Qué dirección debe probar?

::option[0.0.0.0:8091.]{#linux-listening-services-local-listener-a explanation="Esa notación indica en qué interfaces se escucha. El ejemplo muestra otra dirección como destino local."}
::option[127.0.0.1:8091.]{#linux-listening-services-local-listener-b .correct explanation="El servicio escucha en esa dirección de bucle local y en ese puerto."}
::option[El puerto 80 de otro servidor.]{#linux-listening-services-local-listener-c explanation="El servicio del ejemplo escucha en el puerto 8091 de su propio equipo."}
:::

![Salida de ss registrada en LabEx con un socket de prácticas en escucha en el puerto 8091 del bucle local](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/linux-hardening/linux-listening-services/loopback-listener.png)

## Interpretar la escucha en todas las interfaces

Una dirección IPv4 local de `0.0.0.0:8091` significa que el servicio escucha en todas las interfaces IPv4 del equipo. Entre ellas puede haber una interfaz accesible desde otro ordenador. La lista de sockets en escucha indica qué conexiones está preparado para aceptar el proceso en el equipo local. El cortafuegos y las rutas de red pueden limitar el acceso desde otros equipos.

:::single-choice{#linux-listening-services-all-interfaces} Un servicio pasa de 127.0.0.1 a 0.0.0.0 en el mismo puerto. ¿Qué cambió?

::option[Puede escuchar en más interfaces IPv4.]{#linux-listening-services-all-interfaces-a .correct explanation="El ajuste amplía el conjunto de direcciones locales en las que puede aceptar conexiones entrantes."}
::option[Ahora escucha en otro puerto.]{#linux-listening-services-all-interfaces-b explanation="El número de puerto sigue siendo el mismo."}
::option[Se garantiza el acceso inmediato desde cualquier red.]{#linux-listening-services-all-interfaces-c explanation="Las reglas y las rutas de red siguen determinando desde dónde se puede acceder."}
:::

## Comprobar la vía de acceso prevista

Puede que un servicio interno para el personal esté destinado a una sola red. Comprueba el acceso desde esa red y, si necesitas verificar la restricción, haz otra prueba desde una ubicación autorizada fuera de ella. Comprueba tanto el socket en escucha como la vía de acceso. Una lista local por sí sola no revela qué le ocurre a un cliente remoto.

:::single-choice{#linux-listening-services-verify-from-client} Ves un socket en escucha en todas las interfaces locales. ¿Qué prueba indica si se puede acceder desde un equipo del personal?

::option[Volver a leer el nombre del equipo.]{#linux-listening-services-verify-from-client-a explanation="El nombre no comprueba la vía de acceso por la red."}
::option[Contar los sockets en escucha.]{#linux-listening-services-verify-from-client-b explanation="El recuento no muestra si se puede acceder desde ese equipo."}
::option[Hacer una petición autorizada desde la red del personal.]{#linux-listening-services-verify-from-client-c .correct explanation="Así pruebas la vía de acceso prevista."}
:::

Para comprobar qué servicios están en escucha en un equipo Linux, empieza por la práctica de auditoría de servicios en escucha del curso [Seguridad de Linux para DevSecOps](https://labex.io/courses/linux-security-for-devsecops).

## Resumen

Ya puedes interpretar una dirección de escucha antes de decidir desde dónde probar el acceso.

1. Enumera de forma segura los sockets TCP locales en escucha.
2. Distingue entre el bucle local y todas las interfaces IPv4.
3. Verifica la conexión desde la ubicación del cliente pertinente.
