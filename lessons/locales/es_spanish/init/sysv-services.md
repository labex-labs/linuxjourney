# System V Service

## Lesson Content

Hay varias herramientas de línea de comando que puedes utilizar para gestionar los servicios de Sys V.

<b>Listar servicios</b>

<pre>$ service --status-all</pre>

<b>Iniciar un servicio</b>

<pre>$ sudo service networking start</pre>

<b>Detener un servicio</b>

<pre>$ sudo service networking stop</pre>

<b>Reiniciar un servicio</b>

<pre>$ sudo service networking restart</pre>

Estos comandos no son solo específicos de sistemas que usan Sys V, puedes utilizarlos también para gestionar servicios de Upstart. Aunque Linux está tratando de alejarse de los scripts más tradicionales de Sys V, todavía hay herramientas para ayudar en esa transición.

## Exercise

Elige un par de servicios y cambia su estado ¿Qué observas?

## Quiz Question

¿Cuál es el comando para detener un servicio llamado peanut usando Sys V?

## Quiz Answer

sudo service peanut stop