# Upstart Jobs

## Lesson Content

Upstart puede disparar muchos eventos y trabajos, desafortunadamente no hay una forma sencilla de ver donde se originaron los mismos, por lo que tendrás que mirar las configuraciones de los trabajos en /etc/init. La mayor parte del tiempo, no te será necesario, pero te resultará más fácil si quieres controlar algún trabajo en específico. Hay muchos comandos útiles que puedes utilizar en un sistema Upstart. 

<b>Ver trabajos</b>

<pre>initctl list

shutdown stop/waiting
console stop/waiting
...
</pre>

Verás una lista de trabajos con diferentes estados aplicados a ellos. En cada línea, el primer campo hace referencia al nombre del trabajo, el segundo (antes de /) es el objetivo del mismo y el tercero (despues de /) es el estado actual. Puedes ver que nuestro trabajo shutdown tiene como objetivo detenerse, pero actualmente está en estado de espera. Los estados y objetivos cambiarán a medida que inicies o detengas trabajos. 

<b>Ver un trabajo en específico</b>

<pre>initctl status networking
networking start/running
</pre>

No nos meteremos en los detalles de como escribir la configuración de un trabajo, sin embargo ya sabes que los mismos pueden ser detenidos, iniciados y reiniciados en estas configuraciones. Los trabajos también emiten eventos, por lo que pueden iniciar otros trabajos. A continuación veremos los comandos para trabajar con Upstart, pero si eres curioso, no estaría mal que te interiorizaras con los ficheros .conf.

<b>Iniciar un trabajo de forma manual</b>

<pre>$ sudo initctl start networking</pre>

<b>Detener un trabajo de forma manual</b>

<pre>$ sudo initctl stop networking</pre>

<b>Reiniciar un trabajo de forma manual</b>

<pre>$ sudo initctl restart networking</pre>

<b>Emitir un evento de forma manual</b>

<pre>$ sudo initctl emit some_event</pre>

## Exercise

Observa tu lista de trabajos y cambia el estado de algúno con los comandos que aprendimos hoy. ¿Qué notas?

## Quiz Question

¿Como reiniciarías de forma manual un trabajo llamado peanuts?

## Quiz Answer

sudo initctl restart peanuts
