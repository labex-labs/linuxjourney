---
lang: "es"
title: "Niveles de Privilegio"
meta_title: "Niveles de Privilegio - Kernel"
meta_description: "Aprende sobre los niveles de privilegio de Linux, el modo kernel y el modo usuario. Comprende los anillos de protección y las llamadas al sistema para un acceso seguro al hardware. ¡Comienza tu viaje en Linux!"
meta_keywords: "niveles de privilegio de Linux, modo kernel, modo usuario, anillos de protección, llamadas al sistema, seguridad de Linux, Linux para principiantes, tutorial de Linux"
---

## Lesson Content

Las próximas lecciones se volverán bastante teóricas, así que si buscas algo práctico, puedes saltar y volver más tarde.

¿Por qué tenemos diferentes capas de abstracción para el espacio de usuario y el kernel? ¿Por qué no se pueden combinar ambos poderes en una sola capa? Bueno, hay una muy buena razón por la que estas dos capas existen por separado. Ambas operan en diferentes modos: el kernel opera en modo kernel, y el espacio de usuario opera en modo usuario.

En modo kernel, el kernel tiene acceso completo al hardware; lo controla todo. En modo espacio de usuario, hay una cantidad muy pequeña de memoria segura y CPU a la que se le permite acceder. Básicamente, cuando queremos hacer algo que involucre hardware —leer datos de nuestros discos, escribir datos en nuestros discos, controlar nuestra red, etc.— todo se hace en modo kernel. ¿Por qué es esto necesario? Imagina que tu máquina estuviera infectada con spyware; no querrías que tuviera acceso directo al hardware de tu sistema. Podría acceder a todos tus datos, tu webcam, etc., y eso no es bueno.

Estos diferentes modos se llaman niveles de privilegio (nombrados apropiadamente por los niveles de privilegio que obtienes) y a menudo se describen como anillos de protección. Para facilitar esta imagen, digamos que te enteras de que Britney Spears está en la ciudad en tu club local. Está protegida por sus groupies, luego por sus guardaespaldas personales, luego por el portero fuera del club. Quieres conseguir su autógrafo (¿por qué no?), pero no puedes llegar a ella porque está fuertemente protegida. Los anillos funcionan de la misma manera: el anillo más interno corresponde al nivel de privilegio más alto. Hay dos niveles o modos principales en una arquitectura de computadora x86. El Anillo #3 es el privilegio en el que se ejecutan las aplicaciones en modo usuario; el Anillo #0 es el privilegio en el que se ejecuta el kernel. El Anillo #0 puede ejecutar cualquier instrucción del sistema y se le otorga plena confianza. Entonces, ahora que sabemos cómo funcionan esos niveles de privilegio, ¿cómo podemos escribir algo en nuestro hardware? ¿No estaremos siempre en un modo diferente al del kernel?

La respuesta está en las llamadas al sistema. Las llamadas al sistema nos permiten realizar una instrucción privilegiada en modo kernel y luego volver al modo usuario.

## Exercise

No exercises for this lesson.

## Quiz Question

¿Qué número de anillo tiene los privilegios más altos?

## Quiz Answer

0
