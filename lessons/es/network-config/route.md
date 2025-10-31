---
index: 2
lang: "es"
title: "Ruta"
meta_title: "Ruta - Configuración de Red"
meta_description: "Aprenda a gestionar su tabla de enrutamiento de Linux. Esta guía cubre cómo añadir y eliminar rutas de red usando el comando moderno 'ip route command in linux' y el comando 'route' heredado."
meta_keywords: "comando ip route en linux, comando ip route linux, añadir ruta, eliminar ruta, tabla de enrutamiento, enrutamiento de red, redes linux, ip route"
---

## Lesson Content

En Linux, la tabla de enrutamiento dirige el tráfico de red a su destino correcto. Aunque hemos discutido previamente cómo ver esta tabla, también puedes agregar o eliminar rutas manualmente para controlar cómo se reenvían los paquetes de datos. Esto es esencial para configurar configuraciones de red complejas o solucionar problemas de conectividad.

### Uso del comando route heredado

El comando `route` es una herramienta tradicional para administrar la tabla de enrutamiento. Aunque todavía es funcional, se considera heredado y ahora se prefiere el comando `ip`.

Para agregar una nueva ruta de red, se especifica la dirección de red, la máscara de subred y la puerta de enlace (`gw`):

```bash
sudo route add -net 192.168.2.1/23 gw 10.11.12.3
```

Para eliminar una ruta, se utiliza la bandera `del` junto con la dirección de red:

```bash
sudo route del -net 192.168.2.1/23
```

### Gestión moderna de rutas con ip route

El comando `ip route` es la herramienta moderna y más potente para la configuración de red en Linux. Ofrece un conjunto de opciones más consistente y extenso para administrar interfaces de red y rutas. Usar el **comando ip route de linux** es la práctica recomendada para los sistemas actuales.

Para agregar una ruta con el **comando ip route en linux**, se utiliza la acción `add`, especificando la red de destino y el siguiente salto a través de la puerta de enlace:

```bash
ip route add 192.168.2.1/23 via 10.11.12.3
```

Para eliminar una ruta, se puede usar la acción `delete`. Se puede especificar la ruta completa o solo la red de destino si es única:

```bash
# Eliminar especificando la ruta completa
ip route delete 192.168.2.1/23 via 10.11.12.3

# O, eliminar especificando solo el destino
ip route delete 192.168.2.1/23
```

Dominar el comando `ip route` es una habilidad clave para cualquier administrador de Linux responsable de la gestión de redes.

## Exercise

¡La práctica hace al maestro! Aquí hay algunos laboratorios prácticos para reforzar su comprensión del enrutamiento de red y la asignación de direcciones IP:

1.  **[Administrar la asignación de direcciones IP en Linux](https://labex.io/es/labs/comptia-manage-ip-addressing-in-linux-592736)** - Practique la configuración de una IP estática, el establecimiento de una puerta de enlace predeterminada y la verificación de la configuración de red usando el comando `ip`.
2.  **[Explorar la interacción de la capa de red con ping y arp en Linux](https://labex.io/es/labs/comptia-explore-network-layer-interaction-with-ping-and-arp-in-linux-592746)** - Aprenda cómo la puerta de enlace predeterminada maneja el tráfico remoto y observe las interacciones de la capa de red.

Estos laboratorios le ayudarán a aplicar los conceptos de asignación de direcciones IP y enrutamiento en escenarios reales y a ganar confianza con la red de Linux.

## Quiz Question

Cuando se utiliza el comando `route` heredado, ¿cuál es la bandera utilizada para eliminar una ruta? Por favor, responda en inglés, prestando atención a las mayúsculas y minúsculas.

## Quiz Answer

del
