---
index: 5
lang: "es"
title: "Resumen de Systemd"
meta_title: "Systemd: Visión General - Sistema Init"
meta_description: "Aprenda los fundamentos del sistema init systemd. Esta guía cubre cómo systemd (o system d) usa unidades y objetivos para gestionar el arranque y los servicios del sistema Linux. Comprenda los conceptos centrales del estándar moderno para la inicialización de Linux."
meta_keywords: "systemd, system d, sistema init, unidades systemd, objetivos systemd, arranque linux, servicios linux, gestión de sistemas, principiante, tutorial"
---

## Lesson Content

### ¿Qué es Systemd?

Systemd es el sistema init y gestor de servicios predeterminado para la mayoría de las distribuciones modernas de Linux. Es responsable de inicializar el sistema en el orden correcto después de que el kernel ha sido cargado. Una forma sencilla de comprobar si su sistema lo utiliza es ver si existe el directorio `/usr/lib/systemd`. Si existe, es probable que esté ejecutando un sistema administrado por **systemd**.

### El Proceso de Arranque de Systemd

En lugar de scripts secuenciales rígidos, **systemd** utiliza el concepto de "metas" (goals) para llevar su sistema a un estado funcional. Identifica una meta principal, o `target` (objetivo), y trabaja para satisfacer sus dependencias. Este enfoque permite una mayor flexibilidad y paralelización durante el inicio. Un proceso de arranque típico administrado por **systemd** sigue estos pasos:

1. **systemd** primero carga sus archivos de configuración desde directorios como `/etc/systemd/system` y `/usr/lib/systemd/system`.
2. Luego identifica la meta de arranque predeterminada, que suele ser un enlace simbólico llamado `default.target`.
3. Finalmente, **systemd** resuelve todas las dependencias para este objetivo y activa las unidades necesarias para lograr el estado del sistema deseado.

### Entendiendo los Objetivos (Targets) de Systemd

Los objetivos (`Targets`) en **systemd** son análogos a los niveles de ejecución (runlevels) en el sistema init SysV más antiguo. Representan diferentes estados en los que puede estar el sistema. Los objetivos comunes incluyen:

- `poweroff.target`: Apaga el sistema.
- `rescue.target`: Arranca en un shell de usuario único para mantenimiento.
- `multi-user.target`: Un entorno multiusuario estándar con red pero sin interfaz gráfica.
- `graphical.target`: Un entorno multiusuario completo con red y una interfaz gráfica de usuario (GUI).
- `reboot.target`: Reinicia el sistema.

El `default.target` es un enlace simbólico que apunta al objetivo en el que el sistema arrancará por defecto, a menudo `graphical.target` en sistemas de escritorio.

### Concepto Central: Unidades de Systemd

Los objetos fundamentales que **systemd** administra se denominan "unidades". Una unidad es un archivo de configuración que describe un recurso o un servicio. El poder de la arquitectura de **system d** radica en su capacidad para administrar varios tipos de recursos, no solo servicios. Cada tipo de unidad se identifica por su extensión de archivo. Los tipos más comunes son:

- **Unidades de servicio (`.service`):** Estas administran demonios o servicios del sistema, como un servidor web o una base de datos.
- **Unidades de montaje (`.mount`):** Estas controlan los puntos de montaje del sistema de archivos.
- **Unidades de objetivo (`.target`):** Se utilizan para agrupar otras unidades, creando puntos de sincronización durante el arranque.

Por ejemplo, cuando el sistema arranca en `graphical.target`, esa unidad de objetivo asegura que todas sus dependencias, como `multi-user.target` y varias unidades de servicio como `network.service`, se inicien primero.

## Exercise

Aunque no hay laboratorios específicos para este tema, recomendamos explorar la completa [Ruta de Aprendizaje de Linux](https://labex.io/es/learn/linux) para practicar habilidades y conceptos relacionados con Linux.

## Quiz Question

¿Qué unidad se utiliza para agrupar otras unidades? Por favor, responda con una sola palabra en inglés en minúsculas.

## Quiz Answer

target
