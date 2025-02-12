# TCP/IP mudel

## Tunni sisu

OSI mudelist kasvas välja TCP/IP mudel ja sellel mudelil Internet ka tegelikult põhineb. TCP/IP mudel kasutab TCP/IP protokollistikku, mida nimetatakse tavaliselt lihtsalt TCP/IP. Need protokollid töötavad koos, et täpsustada kuidas andmeid peab võrgus koguma, adresseerima, edastama ja marsruutima. TCP/IP mudel võimaldab kirjeldada kuidas kasutatakse protokolle ja kuidas pakett võrgus liigub.

<b>Rakenduskiht</b>

See on kõnealuse mudeli kõige ülemine kiht.  Kirjeldatakse, kuidas programmid (näiteks veebilehtitseja) ühenduvad transpordikihiga, et vaadelda andmeid, mida saadetakse või võetakse vastu.

See kiht kasutab protokolle:
<ul>
<li>HTTP (<i>Hypertext Transfer Protocol</i>) - kasutavad interneti veebilehed.</li>
<li>SMTP (<i>Simple Mail Transfer Protocol</i>) - elektrooniliste kirjade edastamine. </li>
</ul>

<b>Transpordikiht</b>

Kirjeldab, kuidas andmeid edastatakse, sealhulgas kontrollib õigeid porte, andmete terviklikkust ja tegeleb ka põhimõtteliselt pakettide kohaletoimetamisega.

Selles kihis on protokollid:
<ul>
<li>TCP (<i>Transmission Control Protocol</i>) -  usaldusväärne andmete edastust</li>
<li>UDP (<i>User Datagram Protocol</i>) - mitteusaldusväärne andmete edastus</li>
</ul>

<b>Võrgukiht</b>

See kiht kirjeldab, kuidas liigutada pakette hostide vahel ja üle võrgu.

Selles kihis on protokollid:
<ul>
<li>IP (<i>Internet Protocol</i>) - Aitab marsruutida pakette ühest arvutist teise.</li>
<li>ICMP (<i>Internet Control Message Protocol</i>) - Aitab kasutajal toimuvas aimu saada. Näiteks veateated ja silumise informatsioon.</li>
</ul>

<b>Andmevahetuskiht</b>

See kiht kirjeldab, kuidas edastada andmeid riistvara peal füüsiliselt. Näiteks andmete liikumine võrgu- (Etherneti) või fiiberkaablis.

Äratoodud protokollide nimekirjad ei ole lõplikud või ammendavad ning kindlasti kohtab veel palju olulisi protokolle.

Järgnevates peatükkides süveneme igasse kihti ja kirjeldame kuidas liiguvad pakettid võrgus läbi TCP/IP silmade (eksisteerib mitmeid erinevaid vaateid pakettide võrguliiklusele. Meie neid ei tutvusta kuid nende olemasolust võiks olla teadlik).

Lisalugemist eesti keeles <a target="_blank" href="https://et.wikipedia.org/wiki/TCP/IP_mudel">https://et.wikipedia.org/wiki/TCP/IP_mudel</a>

## Harjutus

Selles peatükis harjutust pole.

## Küsimus

Milline on TCP/IP mudeli kõige ülemine kiht?

## Vastus

andmevahetuskiht
