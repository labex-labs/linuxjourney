---
lang: "es"
title: "Monitoreo Continuo"
meta_description: "Aprende el monitoreo continuo de sistemas Linux con sar. Comprende la instalación, la recolección de datos y cómo analizar el uso histórico de recursos para el rendimiento. ¡Empieza ya!"
meta_keywords: "sar, sysstat, monitoreo de Linux, rendimiento del sistema, monitoreo continuo, principiante, tutorial, guía"
---

## Lesson Content

Estas herramientas de monitoreo son buenas para revisar cuando tu máquina tiene problemas, pero ¿qué pasa con las máquinas que tienen problemas cuando no estás mirando? Para esas, necesitarás usar una herramienta de monitoreo continuo, algo que recolectará, reportará y guardará la información de actividad de tu sistema. En esta lección, revisaremos una gran herramienta para usar: **sar**.

### Installing sar

Sar es una herramienta que se utiliza para hacer análisis históricos en tu sistema. Primero, asegúrate de tenerla instalada instalando el paquete `sysstat`: `sudo apt install sysstat`.

### Setting up data collection

Usualmente, una vez que instalas `sysstat`, tu sistema comenzará automáticamente a recolectar datos. Si no lo hace, puedes habilitarlo modificando el campo `ENABLED` en `/etc/default/sysstat`.

### Using sar

```bash
sudo sar -q
```

Este comando listará los detalles desde el inicio del día.

```bash
sudo sar -r
```

Esto listará los detalles del uso de memoria desde el inicio del día.

```bash
sudo sar -P
```

Esto listará los detalles del uso de CPU.

Para ver una vista de un día diferente, puedes ir a `/var/log/sysstat/saXX` donde `XX` es el día que quieres ver.

```bash
sar -q /var/log/sysstat/sa02
```

## Exercise

Instala sar en tu sistema y comienza a recolectar y analizar la utilización de los recursos de tu sistema.

## Quiz Question

¿Cuál es una buena herramienta para monitorear los recursos del sistema?

## Quiz Answer

sar
