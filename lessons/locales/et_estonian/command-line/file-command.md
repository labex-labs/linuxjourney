# file

## Tunni sisu

Eelmises peatükis õppisime käsu *touch* kohta. Pöördume selle juurde korraks veel tagasi. Võib märgata, et failinimi ei vasta sellisele standardile, millega ollakse tõenäoliselt kokku puutunud teistes operatsioonisüsteemides, näiteks MS Windowsis? Tavaliselt oodatakse faili nimega banaan.jpeg ja eeldatakse, et see on pildifail.

Linuxis ei pea failinimed peegeldama faili sisu. Võib teha faili nimega naljakas.gif, kuid see ei pea tegelikult olema GIF-vormingus.

Et teada saada, millist tüüpi mingi fail on, võib kasutada käsku *file*. See näitab failisisu kirjeldust.
 
<pre>$ file banaan.jpg<br />
banaan.jpg: JPEG image data, JFIF standard 1.01, resolution (DPI), density 72x72, segment length 16, progressive, precision 8, 342x509, frames 3
</pre>

## Harjutus

Rakendada *file* käsku erinevatel kataloogidel ja failidel ning uurida väljundit.

## Küsimus

Millise käsuga saab teada failitüübi?

## Vastus

*file*
