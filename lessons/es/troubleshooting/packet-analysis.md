---
lesson_id: "packet-analysis"
course_id: "troubleshooting"
lang: "es"
order_index: 5
title: "Análisis de paquetes"
description: "Aprende a capturar un rastro de paquetes acotado y filtrado, y a analizarlo con seguridad mediante tcpdump."
meta_title: "Análisis de paquetes - Resolución de problemas"
meta_description: "Aprende los fundamentos del análisis de paquetes de red en Linux y utiliza tcpdump para capturar e interpretar tráfico de red."
meta_keywords: "tcpdump, análisis de paquetes, análisis de paquetes de red, analizador de paquetes, análisis de red, herramientas de análisis de paquetes, redes Linux, Wireshark, órdenes Linux, tráfico de red"
---

Una captura de paquetes registra el tráfico visible en un punto de observación elegido. Puede revelar intercambios de protocolos y tiempos, pero también puede recopilar credenciales, datos personales y tráfico de usuarios ajenos. Obtén autorización, reduce el alcance, protege los archivos y cumple la política de conservación.

## Elegir el punto de observación

Captura en la interfaz y el espacio de nombres de red por los que pasa realmente el flujo afectado. Los puentes, contenedores, VPN, enlaces agregados, VLAN y mecanismos de descarga pueden cambiar lo que muestra una interfaz. Utiliza `ip route get` e `ip link` para identificar candidatos antes de capturar.

:::single-choice{#packet-analysis-interface-choice} ¿Por qué importa la elección de la interfaz de captura?

::option[Cada interfaz refleja automáticamente todo Internet.]{#packet-analysis-mirrors-internet explanation="Normalmente, un host solo ve el tráfico entregado a sus interfaces, que pasa por ellas o que se refleja hacia ellas."}
::option[Solo puede registrarse el tráfico visible en ese punto de observación.]{#packet-analysis-visible-point .correct explanation="Los espacios de nombres, túneles, puentes y rutas pueden situar el flujo relevante en otro lugar."}
::option[El nombre de la interfaz descifra las cargas útiles TLS.]{#packet-analysis-name-decrypts explanation="Un nombre no tiene capacidad de descifrado."}
:::

## Capturar un flujo acotado

Captura hasta 100 paquetes sin resolución de nombres y restringidos a un host y un puerto TCP:

```bash
$ sudo tcpdump -i enp1s0 -n -c 100 -w incident.pcap \
    'host 192.0.2.25 and tcp port 443'
```

`-i` selecciona la interfaz, `-n` conserva los nombres numéricos, `-c` limita el número de paquetes, `-w` escribe los datos pcap y la expresión final es un filtro de captura. Establece además un límite de tiempo externo cuando pueda no haber tráfico.

:::single-choice{#packet-analysis-count-bound} ¿Qué hace `-c 100`?

::option[Captura únicamente el puerto TCP 100.]{#packet-analysis-port-hundred explanation="La selección del puerto pertenece a la expresión de filtro."}
::option[Comprime el archivo hasta 100 bytes.]{#packet-analysis-compress-hundred explanation="La opción indica un número de paquetes, no un límite de tamaño de archivo."}
::option[Se detiene después de capturar 100 paquetes.]{#packet-analysis-hundred .correct explanation="El recuento impide que una captura desatendida crezca indefinidamente por número de paquetes."}
:::

## Leer los paquetes capturados

Analiza el archivo guardado sin modificarlo:

```bash
$ tcpdump -n -tttt -r incident.pcap
```

Lee las marcas de tiempo, el protocolo, el origen, el destino, las banderas, los datos de secuencia o confirmación y la longitud según el protocolo. Una marca de tiempo de captura señala la observación en este host, no necesariamente el momento exacto de transmisión en otro lugar. La sincronización de los relojes importa al correlacionar capturas de varios sistemas.

:::single-choice{#packet-analysis-read-file} ¿Qué opción lee paquetes de un archivo pcap guardado?

::option[`-r`]{#packet-analysis-option-read .correct explanation="La opción de lectura procesa un archivo de captura existente."}
::option[`-i`]{#packet-analysis-option-interface explanation="Esta opción selecciona una interfaz para una captura en vivo."}
::option[`-w`]{#packet-analysis-option-write explanation="Esta opción escribe paquetes sin procesar en un archivo."}
:::

## Interpretar la ausencia y el cifrado

No capturar ningún paquete puede deberse a una interfaz o un espacio de nombres incorrectos, pérdidas de captura, un filtro demasiado estrecho, efectos de descarga, enrutamiento por otro lugar o ausencia de tráfico. Comprueba los contadores de paquetes recibidos y descartados de tcpdump y reproduce un evento conocido.

TLS y otros sistemas de cifrado normalmente ocultan las cargas útiles de la aplicación, pero dejan metadatos útiles como los extremos, los tiempos, los tamaños, el comportamiento TCP y partes de las negociaciones. No intentes descifrar sin autorización ni recopiles claves privadas a la ligera.

:::single-choice{#packet-analysis-no-packets} ¿Qué demuestra una captura filtrada vacía?

::option[Que la aplicación remota se eliminó permanentemente.]{#packet-analysis-empty-deleted explanation="Los errores en el punto de observación o el filtro pueden producir el mismo resultado."}
::option[Que no hay ningún tráfico en toda la red.]{#packet-analysis-empty-network explanation="Un filtro estrecho puede excluir tráfico ajeno."}
::option[Únicamente que no se registraron paquetes coincidentes en ese punto de captura.]{#packet-analysis-empty-limited .correct explanation="Valida la interfaz, el espacio de nombres, el filtro, las pérdidas de captura y la generación de la prueba antes de concluir."}
:::

## Proteger y compartir las pruebas

Almacena los archivos pcap con permisos restrictivos, registra la orden, el host, la interfaz, la zona horaria, el filtro y el intervalo del incidente, y calcula un hash de las pruebas cuando importe su integridad. Antes de compartir, minimiza o depura los datos mediante herramientas y procedimientos que conserven los campos necesarios; las cargas útiles e incluso los metadatos de los paquetes pueden identificar a usuarios y sistemas.

:::single-choice{#packet-analysis-pcap-safety} ¿Cómo debe tratarse un archivo pcap de un incidente?

::option[Como una prueba sensible con acceso restringido y procedencia documentada.]{#packet-analysis-sensitive-evidence .correct explanation="Las capturas pueden contener información confidencial y requieren controles tanto de integridad como de confidencialidad."}
::option[Como texto inofensivo que puede publicarse sin revisión.]{#packet-analysis-public explanation="Las capturas binarias pueden exponer cargas útiles, identidades e infraestructura."}
::option[Editando los bytes en el mismo archivo sin conservar el original.]{#packet-analysis-edit-original explanation="Eso daña la procedencia y puede invalidar análisis posteriores."}
:::

## Resumen

Ahora puedes crear una captura de paquetes útil sin hacerla innecesariamente amplia o insegura.

1. Elige la interfaz y el espacio de nombres de red correctos.
2. Acota las capturas por filtro, número de paquetes y tiempo.
3. Guarda los paquetes sin procesar y analiza el archivo en modo de solo lectura.
4. Trata la ausencia y las cargas útiles cifradas con los límites adecuados.
5. Protege la confidencialidad, la integridad y la procedencia de la captura.
