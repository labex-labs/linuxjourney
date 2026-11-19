---
lesson_id: "linux-host-firewalls"
course_id: "linux-hardening"
lang: "es"
order_index: 5
title: "Cortafuegos del equipo"
description: "Aprende a interpretar una política sencilla de cortafuegos y a planificar comprobaciones desde las ubicaciones pertinentes."
meta_title: "Cortafuegos del equipo - Endurecimiento de Linux"
meta_description: "Aprende a interpretar una política sencilla de cortafuegos y a planificar comprobaciones desde las ubicaciones pertinentes."
meta_keywords: "cortafuegos del equipo, endurecimiento de Linux, ciberseguridad, Linux Journey"
---

Un **cortafuegos del equipo** puede permitir o bloquear el tráfico entrante según datos como la dirección de origen, el protocolo y el puerto de destino. Empieza por determinar qué tráfico necesita el servicio.

## Interpretar una política de ejemplo

La siguiente política simplificada corresponde a un solo equipo. La barra de `192.0.2.0/24` indica un rango de direcciones IPv4. En este ejemplo, `192.0.2.44` está dentro de ese rango y `198.51.100.8` queda fuera.

```text
Allow TCP port 443 from any source.
Allow TCP port 22 from 192.0.2.0/24.
Deny other new inbound connections.
```

El puerto 443 atiende el sitio público. El puerto 22 está reservado para la red de mantenimiento. La regla predeterminada se aplica a las conexiones que no coinciden con ninguna de las dos reglas de permiso.

:::single-choice{#linux-host-firewalls-match-trusted-network} ¿Qué nueva conexión coincide con la regla de mantenimiento?

::option[Al puerto TCP 22 desde 198.51.100.8.]{#linux-host-firewalls-match-trusted-network-b explanation="El puerto coincide, pero la dirección de origen queda fuera de la red de administración."}
::option[Al puerto TCP 443 desde 192.0.2.44.]{#linux-host-firewalls-match-trusted-network-c explanation="Esa conexión coincide con la regla del sitio público."}
::option[Al puerto TCP 22 desde 192.0.2.44.]{#linux-host-firewalls-match-trusted-network-a .correct explanation="Coinciden tanto el puerto de destino como el rango de origen."}
:::

![Política de cortafuegos simulada con HTTPS público y acceso restringido para mantenimiento](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/linux-hardening/linux-host-firewalls/sample-policy.png)

## Comprobar la política y el puerto en escucha

Una conexión permitida puede fallar si ningún programa está escuchando en el puerto. También puede haber un servicio escuchando al que no se pueda llegar por una vía bloqueada por el cortafuegos. Revisa la política y comprueba por separado que el puerto esté en escucha.

:::single-choice{#linux-host-firewalls-allowed-but-failed} La regla permite el puerto 443, pero ningún servicio escucha allí. ¿Qué debes comprobar?

::option[Si el cliente debería usar el acceso SSH de mantenimiento.]{#linux-host-firewalls-allowed-but-failed-a explanation="Ese es otro servicio."}
::option[Si el servicio web público escucha en el puerto previsto.]{#linux-host-firewalls-allowed-but-failed-b .correct explanation="Permitir el tráfico en el cortafuegos no hace que un programa escuche en ese puerto."}
::option[Si la petición salió de la red de mantenimiento.]{#linux-host-firewalls-allowed-but-failed-c explanation="En este ejemplo, la regla pública admite cualquier origen."}
:::

## Planificar una verificación segura

Cuando revises un cambio controlado, conserva una vía de acceso legítima para mantenimiento. Prueba la vía permitida desde la red de mantenimiento. Comprueba que una conexión desde una ubicación autorizada para pruebas fuera de esa red quede bloqueada. Anota el origen, el destino y el resultado previsto de cada prueba.

:::single-choice{#linux-host-firewalls-verification-pair} ¿Qué par de comprobaciones pone a prueba la restricción de SSH prevista?

::option[Una comprobación autorizada del puerto 22 desde dentro y otra desde fuera de la red de mantenimiento.]{#linux-host-firewalls-verification-pair-c .correct explanation="Estas conexiones prueban los dos casos de la política."}
::option[Dos peticiones SSH desde el mismo equipo autorizado.]{#linux-host-firewalls-verification-pair-a explanation="Así comprobarías dos veces el caso permitido."}
::option[Dos peticiones del navegador a la página de inicio pública.]{#linux-host-firewalls-verification-pair-b explanation="Esas peticiones prueban el puerto público y dejan sin comprobar el acceso de mantenimiento."}
:::

## Resumen

Ya puedes interpretar las reglas del cortafuegos junto con el estado del servicio.

1. Relaciona cada regla con el protocolo, el destino y el origen.
2. Comprueba que el servicio permitido esté escuchando.
3. Verifica tanto el acceso previsto como la restricción.
