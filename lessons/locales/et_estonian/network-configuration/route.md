# route

## Tunni sisu

Korra juba sai mainitud, et marsruutimistabelit saab kuvada *route* käsuga. Marsruute saab soovi korral aga ka käsitsi lisada või eemaldada.

<b>Uue marsruudi ajutine lisamine</b>

<pre>
$ sudo route add -net 192.168.2.1/23 gw 10.11.12.3
</pre>

<b>Ajutise marsruudi eemaldamine</b>

<pre>
$ sudo route del -net 192.168.2.1/23 
</pre>

Sama võib teha ka <b>ip</b> käsuga:

<b>Marsruudi lisamine</b>
<pre>
$ ip route add 192.168.2.1/23 via 10.11.12.3
</pre>

<b>Marsruudi kustutamine</b>
<pre>
$ ip route delete 192.168.2.1/23 via 10.11.12.3
või
$ ip route delete 192.168.2.1/23
</pre>

## Harjutus

Harjutust selles peatükis ei ole kuid soovitatav on selle peatüki käskude man-lehekülgedelt informatsiooni juurde lugeda.

<pre>$ man route</pre>

<pre>$ man ip-route</pre>

## Küsimus

Millise võtme lisamisel *ifconfig* käsule on tulemuseks marsruudi kustutamine?

## Vastus

*del*
