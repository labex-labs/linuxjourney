---
index: 4
lang: "es"
title: "Monitoreo de CPU"
meta_title: "Monitoreo de CPU - Utilización de Procesos"
meta_description: "Aprenda el monitoreo de la CPU con el comando uptime. Comprenda la carga promedio, el uso de la CPU y cómo interpretar el rendimiento del sistema para principiantes en Linux."
meta_keywords: "comando uptime, monitoreo de CPU Linux, carga promedio, rendimiento del sistema, tutorial de Linux, guía para principiantes"
---

## Lesson Content

Repasemos un comando útil, **uptime**.

```
pete@icebox:~$ uptime
 17:23:35 up 1 day,  5:59,  2 users,  load average: 0.00, 0.02, 0.05
```

Hablamos de uptime en la primera lección de este curso, pero no hemos revisado el campo de carga promedio. Las cargas promedio son una buena manera de ver la carga de la CPU en su sistema. Estos números representan la carga promedio de la CPU en intervalos de 1, 5 y 15 minutos. ¿Qué quiero decir con carga de CPU? La carga de la CPU es el número promedio de procesos que están esperando ser ejecutados por la CPU.

Digamos que tiene una CPU de un solo núcleo; piense en este núcleo como un solo carril en el tráfico. Si es hora pico en la autopista, este carril va a estar muy ocupado, y el tráfico estará al 100% o una carga de 1. Ahora el tráfico se ha vuelto tan malo que está congestionando la autopista y haciendo que las carreteras regulares estén el doble de ocupadas por la cantidad de coches; podemos decir que su carga es del 200% o una carga de 2. Ahora digamos que se despeja un poco y solo hay la mitad de coches en el carril de la autopista; podemos decir que la carga del carril es de 0.5. Cuando el tráfico es inexistente y podemos llegar a casa más rápido, la carga debería ser idealmente muy baja, como el tráfico de las 2 AM. Los coches en este caso son procesos, y estos procesos solo están esperando salir de la autopista y llegar a casa.

Ahora, el hecho de que tenga una carga promedio de 1 no significa que su computadora esté funcionando lentamente. La mayoría de las máquinas modernas hoy en día tienen múltiples núcleos. Si tuviera un procesador de cuatro núcleos (4 núcleos) y su carga promedio es 1, en realidad solo está afectando el 25% de su CPU. Piense en cada núcleo como un carril en el tráfico. Puede ver la cantidad de núcleos que tiene en su sistema con **cat /proc/cpuinfo**.

Al observar la carga promedio, debe tener en cuenta el número de núcleos. Si encuentra que su máquina siempre está utilizando una carga superior al promedio, podría haber algo mal.

## Exercise

¡La práctica hace al maestro! Aquí hay algunos laboratorios prácticos para reforzar su comprensión del monitoreo del rendimiento del sistema Linux y la carga de la CPU:

1. **[Administrar y Monitorear Procesos de Linux](https://labex.io/es/labs/comptia-manage-and-monitor-linux-processes-590864)** - Practique la interacción e inspección de procesos, y el monitoreo de recursos con herramientas como `ps` y `top`, lo que se relaciona directamente con la comprensión de la carga de la CPU.
2. **[Comando Linux top: Monitoreo del Sistema en Tiempo Real](https://labex.io/es/labs/linux-linux-top-command-real-time-system-monitoring-388500)** - Aprenda a usar el comando `top` para el monitoreo del sistema en tiempo real, incluyendo la clasificación y el filtrado de procesos, proporcionando una inmersión más profunda en la actividad de la CPU y los procesos.
3. **[Comando Linux free: Monitoreo de la Memoria del Sistema](https://labex.io/es/labs/linux-linux-free-command-monitoring-system-memory-388496)** - Aprenda a monitorear y analizar el uso de la memoria del sistema, que a menudo es un factor crítico junto con la carga de la CPU en el rendimiento general del sistema.

Estos laboratorios le ayudarán a aplicar los conceptos de monitoreo del sistema y gestión de recursos en escenarios reales y a generar confianza en el análisis del rendimiento del sistema.

## Quiz Question

¿Qué comando puede usar para ver la carga promedio?

## Quiz Answer

uptime
