# Vahendid kasutajate haldamiseks

## Tunni sisu

Paljud ettevõtted kasutavad kasutajakontode ja salasõnade haldamiseks keskhaldussüsteeme. Üksikul masinal aga saab kasutajate haldamisega hakkama ka käskudega.

<b>Kasutajate lisamine</b>

Võib kasutada *adduser* või *useadd* käske. *adduser* hõlmab aga rohkem kasulike omadusi, näiteks kodukataloogi loomine. Uute kasutajate loomiseks saab muuta seadefaile sõltuvalt sellest, mida soovitakse kasutajale määrata vaikimisi.

<pre>$ sudo useradd peeter</pre>

Viimane käsk loob kasutaja peeter kohta sisestuse faili */etc/passwd*, loob vaikimisi grupi ja lisab selle ka faili */etc/shadow*.

<b>Kasutajate kustutamine</b>

Kasutaja kustutamiseks võib kasutada *userdel* käsku.

<pre>$ sudo userdel peeter</pre>

Põhimõtteliselt annab see käsk endast parima, et võtta tagasi muudatused mida *useradd* failidesse tegi.

<b>Salasõna muutmine</b>

<pre>$ passwd peeter</pre>

Selle käsuga saab muuta enda või mõne teise kasutaja salasõna (muidugi juhul kui oled juurkasutaja).

## Harjutus

Luua uus kasutaja, muuta tema salasõna ja siis selle kasutajana sisse logida.

## Küsimus

Millise käsuga saab muuta kasutajate salasõnu?

## Vastus

*passwd*
