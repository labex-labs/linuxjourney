# Upstart Overview

## Lesson Content

Upstart fue desarrollado por Canonical, por lo que fue la implementación de init en Ubuntu por algún tiempo, sin embargo, en instalaciones más modernas del mismo systemd es utilizado. Upstart fue creado para mejorar los problemas de Sys V, tales como el estricto proceso de inicio, el bloqueo de tareas, etc. El modelo de eventos y trabajos de Upstart permite responder a los eventos a medida que ocurren.

Para saber si estás utilizando Upstart, verifica si tienes el directorio /usr/share/upstart.

Los trabajos son las acciones que realiza Upstart y los eventos son los mensajes recibidos desde otros procesos para disparar trabajos. Para ver una lista de trabajos y sus configuraciones:

<pre>
pete@icebox:~$ ls /etc/init
acpid.conf                   mountnfs.sh.conf
alsa-restore.conf            mtab.sh.conf
alsa-state.conf              networking.conf
alsa-store.conf              network-interface.conf
anacron.conf                 network-interface-container.conf
</pre>

Dentro de estas configuraciones, se incluye información sobre como y cuando iniciar los trabajos.

Por ejemplo, el fichero networking.conf, podría decir algo sencillo como:

<pre>
start on runlevel [235]
stop on runlevel [0]
</pre>

Esto significa que iniciará la configuración de red en el nivel de ejecución 2, 3 o 5 y que lo detendrá en el nivel 0. Hay muchas formas de escribir los ficheros de configuración y es algo que descubrirás cuando eches un vistazo a las diferentes configuraciones disponibles.

El modo en el que Upstart trabaja es el siguiente:

<ol>
<li>Primero, carga las configuraciones de los trabajos desde /etc/init.</li>
<li>Cuando un evento de inicio ocurra, correrá el trabajo disparado por dicho evento.</li>
<li>Estos trabajos generarán nuevos eventos y esos eventos dispararán mas trabajos.</li>
<li>Upstart continuará haciendo esto hasta que complete todos los trabajos necesarios.</li>
</ol>

## Exercise

Si estás utilizando Upstart, trata de entender las configuraciones de los trabajos en /etc/init.

## Quiz Question

¿Cuál es la implementación de init que es utilizada en Ubuntu?

## Quiz Answer

upstart
