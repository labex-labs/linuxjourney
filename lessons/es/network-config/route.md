---
index: 2
lang: "es"
title: "route"
meta_title: "route - Configuración de red"
meta_description: "Aprenda a añadir y eliminar rutas de red utilizando los comandos route e ip de Linux. Comprenda la gestión de la tabla de enrutamiento para usuarios principiantes e intermedios."
meta_keywords: "comando route, ip route, añadir ruta, eliminar ruta, redes Linux, tabla de enrutamiento, tutorial Linux, guía para principiantes"
---

## Lesson Content

Ya hemos hablado de ver nuestras tablas de enrutamiento con el comando `route`. Si desea agregar o eliminar rutas, puede hacerlo manualmente.

### Añadir una nueva ruta

```bash
sudo route add -net 192.168.2.1/23 gw 10.11.12.3
```

### Eliminar una ruta

```bash
sudo route del -net 192.168.2.1/23
```

También puede realizar estos cambios con el comando **ip**:

### Para añadir una ruta

```bash
ip route add 192.168.2.1/23 via 10.11.12.3
```

### Para eliminar una ruta

```bash
$ ip route delete 192.168.2.1/23 via 10.11.12.3
or
$ ip route delete 192.168.2.1/23
```

## Exercise

¡La práctica hace al maestro! Aquí hay algunos laboratorios prácticos para reforzar su comprensión del enrutamiento de red y el direccionamiento IP:

1. **[Administrar el direccionamiento IP en Linux](https://labex.io/es/labs/comptia-manage-ip-addressing-in-linux-592736)** - Practique la configuración de una IP estática, el establecimiento de una puerta de enlace predeterminada y la verificación de la configuración de red utilizando el comando `ip`.
2. **[Explorar la interacción de la capa de red con ping y arp en Linux](https://labex.io/es/labs/comptia-explore-network-layer-interaction-with-ping-and-arp-in-linux-592746)** - Aprenda cómo la puerta de enlace predeterminada maneja el tráfico remoto y observe las interacciones de la capa de red.

Estos laboratorios le ayudarán a aplicar los conceptos de direccionamiento IP y enrutamiento en escenarios reales y a generar confianza con las redes Linux.

## Quiz Question

¿Cuál es el indicador de comando para eliminar una ruta?

## Quiz Answer

del
