---
index: 7
lang: "es"
title: "Estados de energía"
meta_title: "Estados de energía - Init"
meta_description: "Aprenda los estados de energía del sistema Linux: comandos shutdown, reboot y halt. Entienda cómo apagar o reiniciar su sistema Linux de forma segura. ¡Comience con los comandos esenciales!"
meta_keywords: "apagado de Linux, comando reboot, sistema halt, apagar Linux, comandos de Linux, Linux para principiantes, tutorial de Linux, estados del sistema"
---

## Lesson Content

Es difícil creer que aún no hayamos discutido formas de controlar el estado de su sistema a través de la línea de comandos. Cuando hablamos de `init`, no solo discutimos los modos que inician nuestro sistema, sino también los que lo detienen.

Para apagar su sistema:

```bash
sudo shutdown -h now
```

Este comando detendrá el sistema (lo apagará). También debe especificar un momento en el que desea que esto ocurra. Puede agregar un tiempo en minutos que apagará el sistema en esa cantidad de tiempo.

```bash
sudo shutdown -h +2
```

Esto apagará su sistema en dos minutos. También puede reiniciar con el comando `shutdown`:

```bash
sudo shutdown -r now
```

O simplemente use el comando `reboot`:

```bash
sudo reboot
```

## Exercise

¿Qué cree que está sucediendo con `init` cuando apaga su máquina?

## Quiz Question

¿Cuál es el comando para apagar su sistema en 4 minutos?

## Quiz Answer

sudo shutdown -h +4
