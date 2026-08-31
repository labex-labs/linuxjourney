---
lesson_id: "bgp-border-gateway-protocol"
course_id: "routing"
lang: "es"
order_index: 7
title: "Protocolo de puerta de enlace fronteriza"
description: "Aprende cómo BGP intercambia accesibilidad IP controlada mediante políticas entre sistemas autónomos y dentro de ellos."
meta_title: "Protocolo de puerta de enlace fronteriza - Routing"
meta_description: "Explora los fundamentos de BGP, el protocolo esencial que permite el enrutamiento de Internet. Aprende cómo facilita la comunicación entre sistemas autónomos y los principios del enrutamiento BGP."
meta_keywords: "BGP, protocolo de puerta de enlace fronteriza, enrutamiento BGP, enrutamiento de internet, sistemas autónomos, redes Linux, tutorial BGP, protocolos de red"
---

El Protocolo de puerta de enlace fronteriza es el protocolo de enrutamiento de vector de rutas de Internet. Intercambia accesibilidad de prefijos IP y atributos de las rutas para que las redes puedan aplicar políticas administrativas en lugar de elegir rutas únicamente por la distancia física.

## Sistemas autónomos y sesiones

Un sistema autónomo es un conjunto de redes bajo una administración común de enrutamiento, identificado en BGP mediante un número de sistema autónomo. BGP externo intercambia rutas entre sistemas autónomos; BGP interno distribuye la accesibilidad BGP dentro de un AS.

Los pares BGP establecen una sesión sobre el puerto TCP 179. Una sesión TCP que funciona es solo la base de transporte; las capacidades de BGP, las políticas y el intercambio de rutas también deben tener éxito.

:::single-choice{#bgp-external-session}
¿Qué intercambia BGP externo?

::option[Sumas de comprobación de tramas Ethernet dentro de un conmutador.]{#bgp-ethernet-fcs explanation="BGP opera por encima de TCP e intercambia accesibilidad de la capa de red."}
::option[Contraseñas de usuarios entre navegadores web.]{#bgp-browser-passwords explanation="Las credenciales de las aplicaciones no son atributos de enrutamiento."}
::option[Información de accesibilidad y rutas entre sistemas autónomos.]{#bgp-between-as .correct explanation="eBGP conecta administraciones de enrutamiento independientes y aplica políticas entre dominios."}
:::

## Información de vector de rutas

Un anuncio incluye un prefijo y atributos. `AS_PATH` enumera los sistemas autónomos atravesados y ayuda a detectar bucles. Otros atributos habituales son `LOCAL_PREF`, `MED`, el origen, el siguiente salto y las comunidades. Su efecto depende de la dirección, la implementación y la política.

:::single-choice{#bgp-as-path-loop}
¿Cómo ayuda `AS_PATH` a evitar bucles entre sistemas autónomos?

::option[Un AS puede rechazar una ruta que ya contenga su propio número.]{#bgp-own-as-reject .correct explanation="El vector de ruta expone la secuencia de AS utilizada para llegar al prefijo anunciado."}
::option[Cifra todos los paquetes que atraviesan esos sistemas.]{#bgp-aspath-encryption explanation="El atributo describe la ruta de enrutamiento y no cifra la carga útil."}
::option[Asigna una dirección MAC a cada AS.]{#bgp-aspath-mac explanation="Los números de sistemas autónomos y las direcciones de enlace son espacios de nombres independientes."}
:::

## Selección basada en políticas

La «mejor» ruta de BGP es la que gana un proceso de decisión configurado. Los operadores pueden preferir las rutas de clientes, modificar la preferencia local, filtrar prefijos, utilizar comunidades y aplicar políticas de ingeniería de tráfico. Un `AS_PATH` más corto puede importar en un paso, pero no prevalece universalmente sobre atributos de mayor prioridad.

Después de que BGP seleccione candidatos, el reenvío IP normal sigue aplicando la coincidencia del prefijo más largo. Un `/24` seleccionado se utiliza para sus destinos en lugar de un `/16` seleccionado que lo contenga.

:::single-choice{#bgp-best-path-meaning}
¿Qué representa una mejor ruta de BGP?

::option[La ruta que gana el proceso local de decisión de atributos y políticas.]{#bgp-policy-winner .correct explanation="La intención administrativa es esencial para seleccionar rutas entre dominios."}
::option[La ruta física de cables más corta en todos los casos.]{#bgp-shortest-cable explanation="BGP no dispone de un mapa completo de distancias físicas."}
::option[Una garantía de la menor latencia actual para la aplicación.]{#bgp-lowest-latency explanation="De forma predeterminada, la selección de BGP no optimiza continuamente la latencia del usuario final."}
:::

## Anuncio y accesibilidad

Anunciar un prefijo afirma que es accesible según una política; no crea la ruta subyacente ni garantiza la ruta de retorno. Antes de originar un prefijo, comprueba el reenvío válido, el comportamiento de agregación, los filtros, la conmutación por error y la autorización de propiedad.

:::single-choice{#bgp-advertisement-limit}
¿Qué no garantiza anunciar un prefijo?

::option[Que los pares puedan recibir una ruta del plano de control.]{#bgp-peers-control explanation="Un anuncio y una aceptación satisfactorios pueden establecer ese hecho limitado del plano de control."}
::option[Que el prefijo contenga bits de dirección.]{#bgp-prefix-bits explanation="Un prefijo IP se define mediante bits de dirección y una longitud."}
::option[Que pueda entregar paquetes para todo el prefijo.]{#bgp-data-plane-not-guaranteed .correct explanation="Aún deben comprobarse las rutas subyacentes, los siguientes saltos, el filtrado y la salud de los servicios."}
:::

## Seguridad del enrutamiento y control de cambios

Las fugas y los secuestros de rutas pueden afectar al tráfico mucho más allá de un único router. Los operadores utilizan filtros estrictos de importación y exportación, límites máximos de prefijos, políticas de pares, supervisión y validación del origen mediante la infraestructura de clave pública de recursos cuando corresponde. La validación de origen RPKI comprueba si un AS está autorizado para originar un prefijo; no valida la ruta AS completa.

Los cambios de BGP requieren un despliegue por etapas, revisión de diferencias entre rutas, acceso fuera de banda, reversión y comprobaciones de los planos de control y de datos.

:::single-choice{#bgp-rpki-limit}
¿Qué comprueba la validación de origen RPKI?

::option[Si todas las cargas útiles de los paquetes están libres de malware.]{#bgp-payload-malware explanation="RPKI no inspecciona el contenido de las aplicaciones."}
::option[Si la ruta AS completa tiene la menor latencia.]{#bgp-path-latency explanation="La validación de origen no selecciona por rendimiento ni valida toda la ruta."}
::option[Si el AS de origen está autorizado.]{#bgp-origin-authorized .correct explanation="Valida la autorización del origen, no todas las relaciones de tránsito de la ruta AS."}
:::

## Resumen

Ahora puedes describir BGP como enrutamiento de vector de rutas controlado mediante políticas.

1. Distingue las sesiones BGP externas de las internas.
2. Usa `AS_PATH` como información de ruta y de bucles.
3. Interpreta la mejor ruta mediante atributos y políticas locales.
4. Comprueba el reenvío que respalda cada prefijo anunciado.
5. Aplica filtrado, validación de origen, supervisión y reversión.
