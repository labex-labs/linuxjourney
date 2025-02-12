# System V Overview

## Lesson Content

El propósito principal de init es iniciar y detener procesos esenciales del sistema. Existen tres grandes implementaciones de init en Linux: System V, Upstart y systemd. En esta lección, veremos la versión mas tradicional de init: System V init o Sys V (pronunciado como 'System Five').

Para saber si estás utilizando la implementación Sys V de init, verifica si tienes el fichero /etc/inittab. 

Sys V inicia y detiene procesos de forma secuencial, por lo que si quieres iniciar un servicio llamado foo-b, antes de que foo-b pueda funcionar, tienes que asegurarte de que foo-a ya se encuentra corriendo. Sys V hace esto mediante scripts, los cuales inician y detienen servicios por nosotros, podemos escribir nuestros propios scripts o usar los que ya vienen implementados en el sistema operativo y que son usados para cargar servicios esenciales. 

La ventaja de utilizar esta implementación de init, radica en la relativa fácilidad para resolver dependencias, ya que sabes que foo-a viene antes de foo-b, sin embargo la performance no es muy buena ya que generalmente una cosa es iniciada o detenida a la vez.

Cuando usas Sys V, el estado de la máquina es definido por una serie de niveles de ejecución que van del 0 al 6. Estos niveles variarán dependiendo de la distribución, pero la mayoría de las veces se verán de la siguiente manera:

<ul>
<li>0: Apagar</li>
<li>1: Modo monousuario</li>
<li>2: Modo multiusuario sin soporte de red</li>
<li>3: Modo multiusuario con soporte de red</li>
<li>4: No usado</li>
<li>5: Modo multiusuario con soporte de red e interfaz gráfica</li>
<li>6: Reiniciar</li>
</ul>

Cuando tu sistema inicia, busca en que nivel de ejecución está y ejecuta los scripts localizados dentro la configuración de dicho nivel. Los mismos se encuentran en <b>/etc/rc.d/rc[número del nivel de ejecución].d/</b> o <b>/etc/init.d</b>. Los scripts que empiezan con S (start) o K (kill) correrán en el inicio y el apagado respectivamente. El número que precede a esos caracteres determina la secuencia en la que se ejecutarán.

Por ejemplo:

<pre>
pete@icebox:/etc/rc.d/rc0.d$ ls
K10updates  K80openvpn
</pre>

Vemos que cuando cambiamos al nivel de ejecución 0 o modo apagado, nuestro equipo correrá primero el script para matar el servicio de actualización y luego el de openvpn. Para saber o modificar el nivel de ejecución por defecto con el que inicia nuestro sistema, puedes mirar el fichero /etc/inittab.

Ten en cuenta que System V está siendo lentamente reemplazado aunque quizás esto no ocurra hoy ni dentro de unos años. Sin embargo, es posible que veas niveles de ejecución en otras implementaciones de init, principalmente para dar soporte a aquellos servicios que solamente son iniciados o detenidos utilizando scripts de System V init. 

## Exercise

Si estás corriendo System V init, cambia el nivel de ejecución por defecto de tu máquina a otra cosa y ve que sucede.

## Quiz Question

¿Qué nivel de ejecución es usado generalmente para apagar el sistema?

## Quiz Answer

0
