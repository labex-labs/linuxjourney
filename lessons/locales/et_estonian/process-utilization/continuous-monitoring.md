# Järjepidev seire

## Tunni sisu

Siiani õpitud tööriistad on head selleks, et uurida, mis arvutis toimub kui ilmneb mõni probleem. Mis saab aga siis, kui probleemid ei ilmne parasjagu sel ajal kui kasutaja seiret teostab? Selleks tarbeks on vajalik järjepideva seire tööriist. Midagi sellist, mis koguks, raporteeriks ja salvestaks süsteemi aktiissuse informatsiooni. Selles peatükis tutvustame suurepärast tööriista <b>sar</b>.

<b>Sar'i paigaldamine</b>
Sar on tööriist mida kasutatakse süsteemi ajaloolise analüüsi tegemiseks. Esmalt tuleb veenduda, et see on paigaldatud. Selleks tuleb paigaldada pakett sysstat: <b>sudo apt update && sudo apt install sysstat && sudo apt clean</b>.

<b>Andmekogumite üles seadmine</b>
Tavaliselt hakkab süsteem automaatselt andmeid koguma kui sysstat paigaldatakse. Kui see aga nii ei ole, saab selle aktiveerida, muutes ENABLED välja failis */etc/default/sysstat*.

<b>Sar'i kasutamine</b>

<pre>$ sudo sar -q</pre>

Selle käsuga kuvatakse detailid käesoleva päeva algusest.

<pre>$ sudo sar -r</pre>

Selle käsuga kuvatakse mälu kasutust puudutav info käesoleva päeva algusest.

<pre>$ sudo sar -P</pre>

See käsk kuvab protsessori kasutamise detailid.

Et kuvada informatsiooni mõne teise päeva kohta, võib minna /var/log/sysstat/saXX, kus XX on soovitud päev.

<pre>$sar -q /var/log/sysstat/sa02</pre>

## Harjutus

Paigaldada sar ja alustada süsteemi ressursside kasutamist puudutava info kogumist ja analüüsimist.

## Küsimus

Milline on hea tööriist süsteemi ressursside seire teostamiseks?

## Vastus

*sar*
