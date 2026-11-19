---
lesson_id: "wireshark-display-filters"
course_id: "network-monitoring"
lang: "es"
order_index: 4
title: "Filtros de visualización de Wireshark"
description: "Aprende a limitar lo que ves en una captura preparada con un filtro de visualización de Wireshark."
meta_title: "Filtros de visualización de Wireshark - Monitorización de redes"
meta_description: "Aprende a limitar lo que ves en una captura preparada con un filtro de visualización de Wireshark."
meta_keywords: "filtros de visualización de Wireshark, monitorización de redes, ciberseguridad, Linux Journey"
---

Una captura de paquetes puede contener tráfico de muchos protocolos. Un **filtro de visualización** indica a Wireshark qué paquetes guardados debe mostrar. Cambia lo que ves y deja intacto el archivo de captura.

## Seleccionar un protocolo

Guarda la [captura de ejemplo](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/examples/network-monitoring/sample.pcap) como `sample.pcap`. Ábrela en Wireshark y escribe `dns` en el cuadro del filtro de visualización. En un terminal de Linux con TShark instalado, este comando aplica el mismo filtro al archivo guardado. El archivo del ejemplo contiene una consulta inofensiva y otro tráfico de prácticas.

```bash
$ tshark -r sample.pcap -Y dns
```

La opción `-r` lee un archivo y `-Y` aplica un filtro de visualización. Busca una consulta y su respuesta.

:::single-choice{#wireshark-display-filters-display-effect} La lista filtrada muestra dos filas menos que la vista original. ¿Qué pasó con los otros paquetes?

::option[Se borraron del archivo de captura.]{#wireshark-display-filters-display-effect-a explanation="Un filtro de visualización cambia los resultados que ves."}
::option[Siguen guardados y no coinciden con este filtro.]{#wireshark-display-filters-display-effect-b .correct explanation="Quita el filtro para volver a ver la captura sin filtrar."}
::option[Se volvieron a enviar por la red.]{#wireshark-display-filters-display-effect-c explanation="Leer una captura guardada no transmite sus paquetes."}
:::

## Buscar una dirección

Un filtro también puede referirse a un campo del paquete. `ip.addr` puede coincidir con la dirección IPv4 de origen o de destino. Los dos signos de igual comparan el campo con el valor del ejemplo.

```bash
$ tshark -r sample.pcap -Y 'ip.addr == 192.0.2.10'
```

Las comillas hacen que el intérprete de comandos trate toda la expresión como un solo argumento. Puedes identificar los extremos en las filas que se muestran.

:::single-choice{#wireshark-display-filters-address-scope} Un paquete va hacia 192.0.2.10 desde otra dirección. ¿Coincidirá con el filtro?

::option[Sí, porque la condición comprueba cualquiera de los dos extremos.]{#wireshark-display-filters-address-scope-a .correct explanation="El campo ip.addr puede coincidir con el origen o con el destino."}
::option[No, porque la condición solo comprueba el origen.]{#wireshark-display-filters-address-scope-b explanation="Este campo puede coincidir en ambos sentidos."}
::option[Solo si el paquete contiene DNS.]{#wireshark-display-filters-address-scope-c explanation="La expresión solo comprueba la dirección IPv4."}
:::

![Salida registrada de TShark que compara la vista filtrada por DNS con la que muestra ambos protocolos de la captura de prácticas](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/network-monitoring/wireshark-display-filters/saved-dns-exchange.png)

## Interpretar una vista vacía

Si el resultado está vacío, el filtro no encontró paquetes coincidentes en el archivo que examinaste. Revisa la expresión, el intervalo y el punto de captura antes de sacar una conclusión más amplia. Empieza por quitar el filtro para confirmar que la captura contiene tráfico.

:::single-choice{#wireshark-display-filters-empty-capture-view} Aplicas dns a una captura guardada y no ves ninguna fila. ¿Qué puedes afirmar?

::option[Nadie usó DNS en toda la red.]{#wireshark-display-filters-empty-capture-view-a explanation="Un archivo cubre un punto de captura y un intervalo limitados."}
::option[Wireshark borró los datos de DNS.]{#wireshark-display-filters-empty-capture-view-b explanation="El filtro de visualización no elimina los paquetes guardados."}
::option[Este filtro no mostró paquetes DNS en esta captura.]{#wireshark-display-filters-empty-capture-view-c .correct explanation="La afirmación se limita a las pruebas que examinaste."}
:::

Para examinar otra captura en un laboratorio desde el navegador, prueba el ejercicio de filtros de visualización de [Wireshark para principiantes](https://labex.io/courses/quick-start-with-wireshark).

## Resumen

Ya puedes filtrar una captura guardada y explicar el alcance del resultado.

1. Selecciona un protocolo con un filtro de visualización.
2. Busca una dirección del paquete con ip.addr.
3. Interpreta la vista filtrada teniendo en cuenta lo que pudo observar la captura.
