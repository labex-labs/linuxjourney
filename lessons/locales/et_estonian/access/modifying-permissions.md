# Ligipääsuõiguste muutmine

## Tunni sisu

Ligipääsuõgusi saab kergesti muuta <b>chmod</b> käsuga.

Esmalt tuleb valida õigused, mida soovitakse muuta kasutaja, grupi ja teiste jaoks. Õigusi saab lisada või eemaldada <b>+</b> ja <b>-</b> märkidega, kehtestada <b>=</b> abil.

Õigused tähtedega:
* <i>r(ead)</i> - lugeda
* <i>w(rite)</i> - kirjutada
* <i>e(x)ecute</i> - käivitada

Isikud tähtedega:
* <i>u(ser)</i> - omanik
* <i>g(roup)</i> - gruppi kuuluv kasutaja
* <i>o(ther)</i> - mingi muu kasutaja süsteemis, kuulub omanikust erinevasse gruppi

Vaatame näiteid.

<b>Õiguse lisamine</b>

<pre>
$ chmod u+x minufail
</pre>

Ülemist käsku võib lugeda nii: muuda faili õigusi lisades kasutajale käivitamise õiguse biti. Selle käsu järgselt on kasutajal faili käivitamise õigus.

<b>Õiguse eemaldamine</b>

<pre>
$ chmod u-x minufail
</pre>

<b>Mitme õiguse lisamine</b>

<pre>
$ chmod ug+w
</pre>

Õigusi on võimalik muuta ka kasutades numbriformaati. See võimaldab muuta kõiki õigusi üheaegselt. Selle asemel, et kasutada sümboleid r,w ja x, kasutatakse õiguste esitamiseks numbreid. Ei ole ka tarvis täpsustada grupi g märgiga või kasutajat u'ga.

Numbriline esitus:

<ul>
<li>4: lugemisõigus</li>
<li>2: kirjutamisõigus</li>
<li>1: käivitamisõigus</li>
</ul>

Vaatame näidet:
<pre>
$ chmod 755 minufail
</pre>

Kas lugeja oskab arvata millised õigused failile anti? Vaatame seda lähemalt. 755 esindab õigusi kõikidele alajaotustele. Esimene number (7) tähistab kasutaja õigusi, teine (5) grupi õigusi ja viimane (5) õigusi teistele kasutajatele.

7 ja 5 ei olnud ju üleval nimekirjas ära toodud, kust need siis tulevad? Meenuta, et kõik õigused on ühendatud ühte numbrisse, mis tähendab, et asjasse on segatud matemaatika.

7 = 4 + 2 + 1, mis tähendab, et 7 annab kasutajale lugemise, kirjutamise ja käivitamise õigused

5 = 4 + 1, grupil on lugemise ja käivitamise õigused

5 = 4 + 1, teistel kasutajatel on lugemise ja käivitamise õigused

Märkus: mõtlematult nalja pärast ei tohiks õigusi muutma hakata. Näiteks võib mõni tundlikku informatsiooni sisaldav fail sattuda valedesse kätesse. Kuid ka nendel kordadel kui õigusi on tarvis muuta asja pärast, tasuks samuti säilitada ettevaatus.

Lisalugemist leiab aadressilt <a target="_blank" href="http://kuutorvaja.eenet.ee/kasutamine/os/failioigused.html">http://kuutorvaja.eenet.ee/kasutamine/os/failioigused.html</a>

Õiguste arvutamiseks on loodud ka mitmeid veebipõhiseid vahendeid, üks näide on <a target="_blank" href="http://permissions-calculator.org/">http://permissions-calculator.org/</a>

## Harjutus

Muuta lihtsate tekstifailide õigusi ja kasutades *ls -l* käsku jälgida, kuidas bitid selle käigus muutuvad.

## Küsimus

Milline number esindab numbriformaadis lugemise õigust?

## Vastus

4
