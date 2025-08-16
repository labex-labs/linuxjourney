---
lang: "es"
title: "Trabajos de Upstart"
description: "Aprenda a administrar trabajos de Upstart en Linux usando comandos initctl. Comprenda el estado, inicio, detención y reinicio de servicios. Mejore sus habilidades de administración de sistemas Linux."
keywords: "trabajos de Upstart, initctl, servicios de Linux, administración de sistemas, tutorial de Linux, guía para principiantes"
---

## Lesson Content

Upstart puede desencadenar muchos eventos y trabajos para ejecutarse. Desafortunadamente, no hay una manera fácil de ver dónde se originó un evento o trabajo, por lo que tendrá que investigar las configuraciones de los trabajos en `/etc/init`. La mayoría de las veces, nunca necesitará mirar los archivos de configuración de trabajos de Upstart, pero querrá controlar algunos trabajos específicos más fácilmente. Hay muchos comandos útiles que puede usar en un sistema Upstart.

### View jobs

```plaintext
initctl list

shutdown stop/waiting
console stop/waiting
...
```

Verá una lista de trabajos de Upstart con diferentes estados aplicados a ellos. En cada línea, el nombre del trabajo es el primer valor, y el segundo campo (antes de `/`) es en realidad el objetivo del trabajo. El tercer valor (después de `/`) es el estado actual. Así, vemos que nuestro trabajo `shutdown` eventualmente quiere detenerse, pero actualmente está en un estado de espera. El estado y los objetivos del trabajo cambiarán a medida que inicie o detenga trabajos.

### View specific job

```plaintext
initctl status networking
networking start/running
```

No entraremos en los detalles de cómo escribir una configuración de trabajo de Upstart; sin embargo, ya sabemos que los trabajos se detienen, inician y reinician en estas configuraciones. Estos trabajos también emiten eventos, por lo que pueden iniciar otros trabajos. Repasaremos los comandos manuales de la operación de Upstart, pero si tiene curiosidad, debería profundizar en los archivos `.conf`.

### Manually start a job

```bash
sudo initctl start networking
```

### Manually stop a job

```bash
sudo initctl stop networking
```

### Manually restart a job

```bash
sudo initctl restart networking
```

### Manually emit an event

```bash
sudo initctl emit some_event
```

## Exercise

Observe su lista de trabajos de Upstart. Ahora, cambie el estado del trabajo con uno de los comandos que aprendimos hoy. ¿Qué nota después?

## Quiz Question

¿Cómo reiniciaría manualmente un trabajo de Upstart llamado `peanuts`?

## Quiz Answer

sudo initctl restart peanuts
