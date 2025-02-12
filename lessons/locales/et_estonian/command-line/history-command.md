# history

## Tunni sisu

Kestprogrammis (shell) on sisestatud käskude ajalugu, mida saab tegelikult isegi vaadata. See on päris kasulik, kui on vaja leida ja rakendada mõnda eelnevalt kasutatud käsku ilma seda uuesti trükkimata.

<pre>$ history</pre>

Kui soovitakse kasutada viimati kasutatud käske siis vajutada lihtsalt nooleklahviga üles.

Tahad kasutada eelmist käsku ilma seda uuesti trükkimata? Kasuta !!. Kui kirjutati enne *cat fail1* ja tahetakse seda uuesti kasutada, siis võib lihtsalt kirjutada *!!* ja see rakendab viimase käsu.

Veel üks *history* otsetee on *ctrl-R*. See on tagurpidine otsingu käsk. Kui klaviatuuril vajutati *ctrl-R* ja hakkati kirjutama osa käsust, näitab see sulle võimalikke vasteid ja nende vahel saab liikuda kui vajutad uuesti *ctrl-R*. Kui soovitud käsk leitud, vajutada lihtsalt Enter.

Kas meie terminali aken hakkab natuke liiga kirjuks muutuma? Koristaks pisut. Kasuta *clear* või *ctrl-L* käsku, et oma kuva ära tühjendada.

<pre>$ clear</pre>

Nii näeb juba palju parem välja, eks?

Kui me juba räägime kasulikest asjadest, siis üks kasulikemaid käsurea keskkonna omadusi on tabulaatorklahviga käskude lõpetamine. Kui alustatakse käsu, faili, kataloogi vms kirjutamist, vajutada tabulaatorit. Põhinedes sellele, mida ta leiab otsitavast kataloogist, lõpetab see käsu automaatselt, kui seal just ei ole teisigi faile, mis algavad samade tähtedega. Näiteks, kui vaja sisestada käsku *chrome*, võib kirjutada *chr* ja vajutada tabulaatorit ja *chrome* lõpetatakse  automaatselt.

## Harjutus

Liikuda käskude ajaloos üles ja alla nooleklahvidega. Mängida natuke *ctrl-R* otsinguga.

## Küsimus

Millise käsuga saab puhastada terminali akna?

## Vastus

clear
