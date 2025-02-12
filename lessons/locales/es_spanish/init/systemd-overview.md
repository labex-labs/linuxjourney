# Systemd Overview

## Lesson Content

Systemd se está convirtiendo lentamente en el standard de init. Si tienes el directorio /usr/lib/systemd, lo más probable es que lo estés utilizando.

Systemd utiliza objetivos para lograr que el sistema esté listo y en funcionamiento. Basicamente, tienes un objetivo que quieres conseguir y este objetivo a su vez tiene dependencias con las que tenemos que cumplir. Systemd es extremadamente flexible y robusto, no sigue una sequencia estricta para iniciar procesos. Esto es lo que ocurre durante un arranque típico de systemd:

<ol>
<li>Primero, systemd carga sus archivos de configuración, generalmente ubicados en /etc/systemd/system o /usr/lib/systemd/system</li>
<li>Luego determina el objetivo de arranque, por lo general es default.target.</li>
<li>Systemd determina las dependencias del objetivo de arranque y las activa.</l>
</ol>

De manera similar a los niveles de ejecución de Sys V, systemd inicia dentro de diferentes objetivos:

<ul>
<li>poweroff.target - apagar sistema</li>
<li>rescue.target - modo monousuario</li>
<li>multi-user.target - modo multiusuario con soporte de red</li>
<li>graphical.target - modo multiusuario con soporte de red e interfaz gráfica</li>
<li>reboot.target - reiniciar sistema</li>
</ul>

Por defecto el objetivo de arranque de defaults.target apunta generalmente a graphical.target.

El componente básico de systemd es la unidad. Systemd no solo detiene e inicia servicios, puede montar sistemas de ficheros, monitorear los sockets de red, etc y debido a su robustés tiene diferente tipos de unidades con las que puede operar. Las unidades mas comunes son:

<ul>
<li>Unidades de servicio - son los servicios que hemos estado iniciando y deteniendo, los ficheros de estas unidades terminan en .service</li>
<li>Unidades de montado - montan sistemas de ficheros, los archivos de estas unidades terminan en .mount</li> 
<li>Unidades de objetivo - agrupa otras unidades, los ficheros de estas unidades terminan en .target</li>
</ul>

Por ejemplo, digamos que arrancamos en default.target, esta unidad de objetivo agrupa unidades como networking.service, crond.service, etc por lo que cuando activamos una sola unidad, todo debajo de ella será activado. 

## Exercise

No hay ejercicios para esta leccion.

## Quiz Question

¿Qué unidad es utilizada para agrupar otras unidades?

## Quiz Answer

objetivo
