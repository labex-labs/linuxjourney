# Systemd Goals

## Lesson Content

No entraremos en detalle de como se escriben los ficheros de unidades de systemd. Sin embargo, haremos un breve repaso de uno de estos archivos y de como controlar las unidades de forma manual.

Aqui tenemos una unidad de servicio bastante básica: foobar.service

<pre>
[Unit]
Description=My Foobar
Before=bar.target

[Service]
ExecStart=/usr/bin/foobar

[Install]
WantedBy=multi-user.target
</pre>

Al principio vemos la seccion [Unit] que nos permite añadir una descripcion de nuestro fichero de unidad asi como tambien controlar el orden de cuando activar la misma. La porcion siguiente es la sección [Service], bajo la cual podemos iniciar, detener y reiniciar el servicio. Y la sección [Install] es utilizada para las dependencias. Esto es solamente la punta del iceberg sobre como escribir ficheros de systemd, por lo que te imploro que leas sobre este tema si quieres saber mas.

Ahora, metamosnos con algunos comandos que podemos usar con unidades de systemd:

<b>Listar unidades</b>

<pre>$ systemctl list-units</pre>

<b>Ver el estado de una unidad</b>

<pre>$ systemctl status networking.service</pre>

<b>Iniciar una unidad</b>

<pre>$ sudo systemctl start networking.service</pre>

<b>Detener una unidad</b>

<pre>$ sudo systemctl stop networking.service</pre>

<b>Reiniciar una unidad</b>

<pre>$ sudo systemctl restart networking.service</pre>

<b>Habilitar una unidad</b>

<pre>$ sudo systemctl enable networking.service</pre>

<b>Deshabilitar una unidad</b>

<pre>$ sudo systemctl disable networking.service</pre>

Aun asi, todavia tienes que ver que tan profundo puede llegar a ser systemd, investiga si quieres aprender mas.

## Exercise

Observa el estado de las unidades e inicia y deten algunos servicios ¿Que notas?

## Quiz Question

¿Cual es el comando para iniciar un servicio que se llama peanut.service?

## Quiz Answer

sudo systemctl start peanut.service
