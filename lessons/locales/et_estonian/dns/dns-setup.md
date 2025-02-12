# DNS'i seadistamine

## Tunni sisu

Kuna nimeserveri ülesseadmisest saaks teha üpriski pika juhendi, ei võta me seda siinkohal ette. Selle asemel on välja pakutud väike võrdlus populaarsetest serveritest, mida Linuxiga kasutada.

<b>BIND</b>

Tegu on kõige populaarsema DNS serveriga Internetis, see on Linuxi maailmas standard. Algselt arendati see välja California Ülikoolis Berkley'is, sellest ka nimi (*Berkeley Internet Name Domain* tõlkes Berkley interneti nimedomeen). Kui eesmärgiks on korralik võimsus ja paindlikkus, ei saa BIND'iga eksida.

<b>DNSmasq</b>

Väikesemahuline ja palju lihtsam seadistada kui BIND. Kui soov on kasutada midagi lihtsat ja kõik BIND'i uhked lisavõimalused ei ole vajalikud, võib kasutada DNSmasq'i. Sellel on kõik tööriistad, mida on vaja DHCP ja DNS'i jaoks. Soovitatav väiksematele võrkudele.

<b>PowerDNS</b>

Kõikide võimalustega ja sarnane BIND'ile, pakub see natuke rohkem paindlikkust ja võimalusi. Informatsiooni loetakse mitmetest andmebaasidest, näiteks MySQL, PostgreSQL jne, tehes administreerimise lihtsamaks. Lihtsalt selle pärast, et BIND on olnud kogu aeg eelistatuim variant ei tähenda, et see peaks alatiseks nii jääma.

See ei ole loomulikult ammendav nimekiri kuid võiks anda aimu, mida DNS serveri üles seadmisel otsida.

## Harjutus

Harjutust pole.

## Küsimus

Milline on *de facto* Linuxi DNS server?

## Vastus

BIND
