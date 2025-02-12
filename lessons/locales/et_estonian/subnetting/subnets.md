# Alamvõrgud

## Tunni sisu

Kuidas ma tean, et ma olen Peetriga samas võrgus? Piisab, kui uurida alamvõrku. Alamvõrk on grupp arvuteid (*host*), mille IP aadressid on mingit moodi sarnased. Need hostid on tavaliselt üksteisele füüsiliselt üsna lähedal ja andmevahetus sama alamvõrgu piires on suhteliselt lihtne. Sellest võib mõelda kui sama riigi piires kirja saatmisest. See on palju lihtsam kui saata kiri mõnda teise riiki.

Näiteks peaksid kõik arvutid, mille IP aadressi algus on 123.45.67 olema samas alamvõrgus. Minu IP aadress on 123.45.67.8 ja Peetri oma on 123.45.67.9. Kokku langev numbrite osa on võrgu eesliide (prefiks) ning 8 ja 9 on arvutite numbrid. Seega oleme Peetriga samas võrgus. Alamvõrk jagatakse võrgu eesliiteks, näiteks 123.45.67.0 ja alamvõrgu maskiks.

<b>Alamvõrgu maskid</b>

Alamvõrgu maskid määravad, milline osa IP aadressist on võrgu osa ja milline on hosti oma.

Tavaline mask võib välja näha selline:

<pre>255.255.255.0</pre>

255 osa on mask. Teeme selle kergemini mõistetavaks. Meenutame, et iga oktett on 8 bitti. Arvutiteaduses võib bitt olla binaaresituses kas 0 või 1. Binaarnumbrite puhul tähendab 1 signaali ja 0 selle puudumist. Millega võrdub kaheksa nulli või ühte?

Kirjutame otsingumootorisse "binary to decimal calculator" ja teisendame 11111111 detsimaalkujule. Mis on tulemuseks? 255! Seega on ühe okteti piires numbrid 0 kuni 255. Seega, kui meil on alamvõrgu mask 255.255.255.0 ja IP aadress 192.168.1.0, siis mitu kasutajat sellesse võrku mahub? Vastuse sellele küsimusele saab alamvõrgu matemaatika peatükist.

Kui räägitakse alamvõrkudest, kirjutatakse võrguprefiksile alamvõrgu mask kohe järele:

<pre>123.234.0.0 255.255.0.0</pre>

<b>Miks?</b>

Milleks üldse alamvõrke vaja on? Võrke jagatakse alamvõrkudeks, et paremini kontrollida andmeliiklust. Kasutajad ühes alamvõrgus ei saa tüüpiliselt suhelda kasutajatega teises alamvõrgus.

Kuid kui tahetakse ühenduda mõne hostiga nagu näiteks yahoo.com? Siis peab alamvõrgud kokku ühendama. Selleks tuleb leida hostid, mis on ühendatud rohkem kui ühe alamvõrguga. Kui üks kasutaja 192.168.1.129 on ühendatud kohalikku võrku 192.168.1.129/24 (st 24 ühte, ehk 255.255.255.0) võib ta luua ühenduse iga kasutajaga selles võrgus. Kui aga on soov ühenduda Internetiga, on vaja suhelda läbi marsruuteri. Traditsiooniks on saanud, et võrgus maskiga 255.255.255.0 on marsruuteri aadress 1, st 192.168.1.1. Sellel marsruuteril on aga port, mis ühendub mõnda teise alamvõrku (sellest lähemalt marsruutimise peatükis). Mõned IP aadressid aga ei olegi Internetis nähtavad, selliseks puhuks on meil seatud üles seadmed nagu NAT (ka sellest lähemalt veidi hiljem).

## Harjutus

Kasutada ifconfig käsku, et kuvada arvuti alamvõrgu mask.

## Küsimus

Tõene või väär? Alamvõrk koosneb võrgu prefiksist ja alamvõrgu maskist?

## Vastus

tõene
