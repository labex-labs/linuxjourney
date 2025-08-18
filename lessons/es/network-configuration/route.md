---
lang: "es"
title: "route"
meta_description: "Aprenda cómo agregar y eliminar rutas de red usando los comandos route e ip de Linux. Comprenda la gestión de tablas de enrutamiento para usuarios principiantes e intermedios."
meta_keywords: "comando route, ip route, agregar ruta, eliminar ruta, redes Linux, tabla de enrutamiento, tutorial Linux, guía para principiantes"
---

## Lesson Content

Ya hemos hablado de ver nuestras tablas de enrutamiento con el comando `route`. Si desea agregar o eliminar rutas, puede hacerlo manualmente.

### Agregar una nueva ruta

```bash
sudo route add -net 192.168.2.1/23 gw 10.11.12.3
```

### Eliminar una ruta

```bash
sudo route del -net 192.168.2.1/23
```

También puede realizar estos cambios con el comando **ip**:

### Para agregar una ruta

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

No hay ejercicios para esta lección, pero puede leer más información sobre los comandos discutidos aquí en las páginas man.

```bash
man route
```

```bash
man ip-route
```

## Quiz Question

¿Cuál es el indicador de comando para eliminar una ruta?

## Quiz Answer

del
