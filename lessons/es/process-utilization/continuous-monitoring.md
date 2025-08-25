---
index: 7
lang: "es"
title: "Monitoreo Continuo"
meta_title: "Monitoreo Continuo - Utilización de Procesos"
meta_description: "Aprende el monitoreo continuo de sistemas Linux con sar. Comprende la instalación, la recolección de datos y cómo analizar el uso histórico de recursos para el rendimiento. ¡Empieza ya!"
meta_keywords: "sar, sysstat, monitoreo de Linux, rendimiento del sistema, monitoreo continuo, principiante, tutorial, guía"
---

## Lesson Content

Estas herramientas de monitoreo son buenas para revisar cuando tu máquina está teniendo problemas, pero ¿qué pasa con las máquinas que tienen problemas cuando no estás mirando? Para esos casos, necesitarás usar una herramienta de monitoreo continuo, algo que recolecte, reporte y guarde la información de actividad de tu sistema. En esta lección, revisaremos una gran herramienta para usar: **sar**.

### Instalando sar

Sar es una herramienta que se utiliza para hacer análisis históricos en tu sistema. Primero, asegúrate de tenerla instalada instalando el paquete `sysstat`: `sudo apt install sysstat`.

### Configurando la recolección de datos

Usualmente, una vez que instalas `sysstat`, tu sistema comenzará automáticamente a recolectar datos. Si no lo hace, puedes habilitarlo modificando el campo `ENABLED` en `/etc/default/sysstat`.

### Usando sar

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

¡La práctica hace al maestro! Aquí tienes algunos laboratorios prácticos para reforzar tu comprensión del monitoreo del sistema y el análisis de recursos:

1. **[Administrar y Monitorear Procesos de Linux](https://labex.io/es/labs/comptia-manage-and-monitor-linux-processes-590864)** - Practica la interacción con procesos en primer y segundo plano, inspeccionándolos con `ps`, monitoreando recursos con `top`, y terminándolos con `kill`.
2. **[Comando Linux top: Monitoreo del Sistema en Tiempo Real](https://labex.io/es/labs/linux-linux-top-command-real-time-system-monitoring-388500)** - Aprende a usar varias opciones con el comando `top` para ordenar procesos, ajustar intervalos de actualización, filtrar por usuario y enfocarse en procesos activos para monitorear eficazmente el rendimiento del sistema.
3. **[Comando Linux df: Reporte de Espacio en Disco](https://labex.io/es/labs/linux-linux-df-command-disk-space-reporting-219188)** - Este laboratorio introduce el comando `df` en Linux, una utilidad que muestra información sobre el uso del espacio en disco en sistemas de archivos montados, lo cual es un aspecto clave del monitoreo del sistema.

Estos laboratorios te ayudarán a aplicar los conceptos de monitoreo de recursos del sistema en escenarios reales y a desarrollar confianza al analizar la actividad del sistema.

## Quiz Question

¿Cuál es una buena herramienta para monitorear los recursos del sistema?

## Quiz Answer

sar
