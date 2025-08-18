---
lang: "es"
title: "Monitoreo de CPU"
meta_title: "Monitoreo de CPU - Utilización de Procesos"
meta_description: "Aprenda a monitorear la CPU con el comando uptime. Comprenda el promedio de carga, el uso de la CPU y cómo interpretar el rendimiento del sistema para principiantes en Linux."
meta_keywords: "comando uptime, monitoreo de CPU Linux, promedio de carga, rendimiento del sistema, tutorial Linux, guía para principiantes"
---

## Lesson Content

Repasemos un comando útil, **uptime**.

```
pete@icebox:~$ uptime
 17:23:35 up 1 day,  5:59,  2 users,  load average: 0.00, 0.02, 0.05
```

Hablamos de uptime en la primera lección de este curso, pero no hemos repasado el campo load average. Los promedios de carga (load averages) son una buena manera de ver la carga de la CPU en su sistema. Estos números representan la carga promedio de la CPU en intervalos de 1, 5 y 15 minutos. ¿Qué quiero decir con carga de CPU? La carga de la CPU es el número promedio de procesos que están esperando ser ejecutados por la CPU.

Digamos que tiene una CPU de un solo núcleo; piense en este núcleo como un solo carril en el tráfico. Si es hora pico en la autopista, este carril estará muy ocupado y el tráfico estará al 100% o una carga de 1. Ahora el tráfico se ha vuelto tan malo que está atascando la autopista y haciendo que las carreteras regulares estén el doble de ocupadas por la cantidad de coches; podemos decir que su carga es del 200% o una carga de 2. Ahora digamos que se despeja un poco y solo hay la mitad de coches en el carril de la autopista; podemos decir que la carga del carril es de 0.5. Cuando el tráfico es inexistente y podemos llegar a casa más rápido, la carga idealmente debería ser muy baja, como el tráfico de las 2 AM. Los coches en este caso son procesos, y estos procesos solo están esperando salir de la autopista y llegar a casa.

Ahora, el hecho de que tenga un promedio de carga de 1 no significa que su computadora esté funcionando lentamente. La mayoría de las máquinas modernas hoy en día tienen múltiples núcleos. Si tuviera un procesador de cuatro núcleos (4 cores) y su promedio de carga es 1, en realidad solo está afectando el 25% de su CPU. Piense en cada núcleo como un carril en el tráfico. Puede ver la cantidad de núcleos que tiene en su sistema con **cat /proc/cpuinfo**.

Al observar el promedio de carga, debe tener en cuenta el número de núcleos. Si encuentra que su máquina siempre está utilizando una carga superior al promedio, podría haber algo mal.

## Exercise

Check the load average of your system and see what it's doing.

## Quiz Question

¿Qué comando puede usar para ver el promedio de carga?

## Quiz Answer

uptime
