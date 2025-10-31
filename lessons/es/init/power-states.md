---
index: 7
lang: "es"
title: "Estados de Energía"
meta_title: "Estados de Energía - Init"
meta_description: "Aprenda a gestionar los estados de energía del sistema Linux. Esta guía cubre los comandos esenciales de apagado, reinicio y detención para apagar o reiniciar su sistema Linux de forma segura. Domine estos comandos fundamentales de Linux para la administración del sistema."
meta_keywords: "estados de energía linux, comando shutdown, comando reboot, comando halt, apagar linux, reiniciar linux, administración de sistemas linux, linux para principiantes, comandos linux, systemd, init"
---

## Lesson Content

Gestionar correctamente el estado de energía de su sistema Linux es una habilidad fundamental. Si bien puede usar una interfaz gráfica, la línea de comandos ofrece opciones potentes y flexibles para apagar o reiniciar su máquina. Estos procesos están vinculados al sistema de inicialización del sistema, como `init` o `systemd`, que administra diferentes estados operativos, incluyendo el inicio y el apagado.

### Apagado del Sistema

El comando principal para administrar los estados de energía es `shutdown`. Para apagar su sistema Linux inmediatamente, puede usar el comando `shutdown` con la bandera `-h` (halt/detener) y el argumento de tiempo `now` (ahora). Se requieren privilegios administrativos, por lo que deberá usar `sudo`.

```bash
sudo shutdown -h now
```

La bandera `-h` indica al sistema que se detenga después de apagar los servicios. En la mayoría del hardware moderno, esto apagará completamente la máquina. También puede programar un apagado para un momento futuro. Para apagar el sistema en un número específico de minutos, use el formato `+m`:

```bash
sudo shutdown -h +2
```

Este comando apagará su sistema en dos minutos, lo cual es útil para advertir a otros usuarios o permitir que los procesos en segundo plano finalicen correctamente.

### Reinicio del Sistema

Para reiniciar su sistema Linux, puede usar el comando `shutdown` con la bandera `-r` (reboot/reiniciar).

```bash
sudo shutdown -r now
```

Una alternativa más directa y comúnmente utilizada es el comando `reboot`, que logra el mismo objetivo de reiniciar el sistema de forma segura.

```bash
sudo reboot
```

### Comandos de Energía Alternativos

Para un control más directo, también puede encontrar los comandos `halt` y `poweroff`. En muchas distribuciones Linux modernas, estos son esencialmente atajos que llaman al comando `shutdown`. Por ejemplo, ejecutar `poweroff` es a menudo equivalente a ejecutar `shutdown -h now`.

## Exercise

Siéntase libre de practicar estos comandos en una máquina virtual. Para ejercicios más guiados, explore la [Ruta de Aprendizaje de Linux](https://labex.io/es/learn/linux) integral para practicar una amplia gama de habilidades de Linux.

## Quiz Question

¿Cuál es el comando completo, incluyendo `sudo`, para programar un apagado del sistema en 4 minutos? Por favor, proporcione el comando completo en inglés, prestando atención al espaciado y las mayúsculas.

## Quiz Answer

sudo shutdown -h +4
