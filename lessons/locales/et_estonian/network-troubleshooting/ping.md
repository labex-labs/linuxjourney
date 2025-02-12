﻿# ping

## Tunni sisu

Ühte lihtsaimat võrgu tööriista <b>ping</b>'i kasutatakse selleks, et testida kas paketid on võimelised jõudma sihtkohta. See töötab saates ICMP kajapäringu (tüüp 8) paketi sihkohta ning ootab seejärel ICMP kajapäringule vastust (tüüp 0). Ping on edukas kui väljasaadetud pakettidele tulevad sihtkohast vastused. Vaatame näidet:

<pre>
pete@icebox:~$ ping -c 3 www.google.com
PING www.google.com (74.125.239.112) 56(84) bytes of data.
64 bytes from nuq05s01-in-f16.1e100.net (74.125.239.112): icmp_seq=1 ttl=128 time=29.0 ms
64 bytes from nuq05s01-in-f16.1e100.net (74.125.239.112): icmp_seq=2 ttl=128 time=23.7 ms
64 bytes from nuq05s01-in-f16.1e100.net (74.125.239.112): icmp_seq=3 ttl=128 time=15.1 ms
</pre>

Selles näites testime, kas on võimalik saada ühendust aadressiga www.google.com. Võtit -c kasutatakse, et määrata, mitu päringuteadet tuleb saata.

Esimene osa ütleb, et saadetakse 64-baidine pakett aadressile 74.125.239.112 (google.com) ja ülejäänu kajastab teekonna detaile. Vaikimisi saadetakse üks pakett sekundi kohta.

<b>icmp_seq</b>

See väli kajastab saadetava paketi järjekorranumbrit. Nagu näha siis meie näites saadeti kolm paketti ja neile saadi ka vastused. Kui kajapäringu vastuses on mõned numbrid vahelt puudu, võib see tähendada, et pakettide saatmisel esines võrguühenduses mingisugune tõrge ja kõik paketid ei jõudnud sihtkohta pärale. Kui järjekorranumbrid on paigast ära võib see tähendada, et ühendus on väga aeglane ja vastus ei saabu vaikimisi määratud ühe sekundi jooksul.

<b>ttl</b>

*Time to Live* (tõlkes: elada jäänud aeg) välja kasutatakse hüpete loendurina. Pärast igat hüpet lahutatakse sellest väärtusest 1 kuni jõutakse väärtuseni 0, seejärel aga pakett nö sureb. See annab paketile mingisuguse eluea, sest me ei taha, et paketid igavesti ringi reisiksid.

<b>time</b>

See väli kajastab ringreisi aega, mis kulus kajapäringu paketi saatmisest kuni vastuse saamiseni.

## Harjutus

Teostada ping mõnele veebileheküljele ja uurida väljundit.

## Küsimus

Mis on päringu sooritamiseks kulunud aja mõõtühik?

## Vastus

ms (millisekund)
