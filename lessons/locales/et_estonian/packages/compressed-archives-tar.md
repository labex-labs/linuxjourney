# tar ja gzip

## Tunni sisu

Enne kui rääida pakettide paigaldamisest ja erinevatest haldusprogrammidest, võiks rääkida failide arhiveerimisest ja tihendamisest, sest neid tuleb kindlasti internetist tarkvara jahtides ette.

Failid, mille laiend on .rar ja .zip on arhiivifailid. Nende sees on veel omakorda palju faile, kuid nad on kenasti üheks arhiivina tuntud failiks kokku pakitud.

<b>Failide tihendamine *gzip*'i abil</b>

*Gzip* on programm, mida kasutatakse failide tihendamiseks Linuxis, laiendiks on .gz.

Faili tihendamiseks:
<pre>$ gzip minulahefail</pre>

Lahtipakkimiseks:
<pre>$ gunzip minulahefail.gz</pre>


<b>Arhiivide loomine tar'i abil</b>
Kahjuks ei saa *gzip* lisada arhiivi mitut faili. Õnneks saab seda teha *tar*'iga. Kui luua sellega arhiiv, on faililaiendiks .tar.

<pre>$ tar cvf minutarfail.tar minulahefail1 minulahefail2</pre>

<ul>
<li>c - loomine</li>
<li>v - ütleme programmile, et see kannaks ette, mida ta teeb</li>
<li>f - selle võtme järel peab tulema <i>tar</i> faili nimi, kui luua uus fail tuleb nimi välja mõelda/li>
</ul>

<b>Arhiivide lahtipakkimine *tar*'i abil</b>

*tar* faili lahtipakkimiseks:

<pre>$ tar xvf minutarfail.tar</pre>

<ul>
<li>x - lahtipakkimine</li>
<li>v - ütleme programmile, et see kannaks ette, mida ta teeb</li>
<li>f - fail, mida soovitakse lahti pakkida</li>
</ul>

<b>Arhiivide tihendamine ja lahtipakkimine *gzip*'i ja *tar*'iga</b>

Tihti võib leida *tar* faile, mis on tihendatud: minutihendatudarhiiv.tar.gz. Sellisel juhul tuleb hakkata tegutsema väljast poolt sissepoole: esiteks eemaldame tihenduse *gunzip*iga ja seejärel pakime *tar* faili lahti. On ka võimalik kasutada <b>z</b> varianti, mis ütleb *tar*ile, et on vaja kasutada *gzip* või *gunzip* utiliiti.

Tihendatud *tar* faili loomine:
<pre>$ tar czf minufail.tar.gz</pre>

Tihenduse eemaldamine ja lahti pakkimine:
<pre>$ tar xzf fail.tar</pre>

Inglise keele tundmine aitab käsku meeles pidada: e<b>X</b>tract all <b>Z</b>ee <b>F</b>iles!

*tar* on üks nendest käskudest, mis on väga oluline kuid, mida kunagi ei suudeta päriselt meelde jätta: <a href="https://xkcd.com/1168/">https://xkcd.com/1168/</a>

<b>Teised haldusvahendid</b>

Mida rohkem kasutada Linuxit, seda rohkem puutub kokku erinevate arhiveerimis- ja tihendustüüpidega, näiteks *bzip2*, *compress*, *zip*, *unzip* jne, kuid need on natuke vähem levinud. Tasub meelde jätta, et erinevad haldusvahendid kasutavad erinevaid käske.

## Harjutus

Tutvuda *tar*'i dokumentatsiooniga ja uurida *man* leheküljelt erinevate kasutusvõimaluste kohta.

## Küsimus

Millise võtmega luuakse arhiive?

## Vastus

c
