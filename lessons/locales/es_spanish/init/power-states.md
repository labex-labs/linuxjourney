# Power States

## Lesson Content

Es difícil de creer que hasta ahora no hayamos discutido las diferentes maneras de controlar el estado del sistema desde la línea de comando, cuando hablamos de init, no solo hablamos de los modos que nos permiten iniciar nuestro sistema, sino tambien de aquellos que lo detienen.

Detener el sistema

<pre>$ sudo shutdown -h now</pre>

Esto detendrá el sistema (apagarlo), además debes especificar el momento en el que quieres que esta acción ocurra. Puedes expresar el tiempo en minutos.

<pre>$ sudo shutdown -h +2</pre>

Esto hará que el sistema se apague dentro de dos minutos. Tambien puedes reiniciar el sistema con el comando shutdown:

<pre>$ sudo shutdown -r now</pre>

O simplemente usar el comando reboot.

<pre>$ sudo reboot</pre>

## Exercise

¿Qué piensas que ocurre con init cuando apagas tu equipo?

## Quiz Question

¿Cuál es el comando para apagar tu sistema dentro de 4 minutos?

## Quiz Answer

sudo shutdown -h +4
