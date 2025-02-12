# Transpordikiht

## Tunni sisu

Transpordikiht võimaldab edastada andmeid võrku loetavas keeles. See jagab kasutaja andmed tükkideks, mida seejärel edastatakse ja pannakse hiljem jälle õiges järjekorras kokku. Neid tükke nimetatakse segmentideks. Segmendid teevad andete edastamise lihtsamaks.

<b>Pordid</b>

Kuigi me teame IP aadressi järgi kuhu me saadame admed siis ei piisa sellest, et saata andmed kindlale protsessile või teenusele. Teenused nagu HTTP kasutavad suhtluskanaleid portide näol. Kui tahame saata andmeid veebilehele, saadame me andmed üle HTTP pordi (port 80). Lisaks segmentide moodustamisele, lisab transpordikiht sellele ka lähte- ja sihtkoha pordi. Tänu sellele teab vastuvõttev pool, millist porti kasutada.

Porte saame Linuxis vaadata:<br>
<pre>cat /etc/services</pre>
või ka:<br>
<pre>less /etc/services</pre>
...less'ist väljumiseks vajutada q

Näiteks HTTP'ga seotud portide vaatamiseks:
<pre>cat /etc/services | grep -i http</pre>

Sama kehtib ka UDP portide vaatamise kohta.

<b>UDP</b>

Kaks populaarset transpordiprotokolli on UDP ja TCP. Tutvustame UDP'd ainult kergelt ja veedame suurema aja TCP'ga, kuna seda kasutatakse tüüpilisemalt.

UDP ei ole usaldusväärne meetod andmete edastamiseks, tegelikult seda isegi ei huvita kas kasutaja saab kõik andmed kätte või mitte. See võib kõlada halvasti kuid ka UDP'l on oma koht, näiteks meedia voogesituses. Ei ole ju hullu kui mõned raamid ei jõua kohale kuid selle eest edastatakse andmeid kiiremini.

<b>TCP</b>

TCP pakub usaldusväärset ühendusele orienteeritud andete edastamist. TCP kasutab porte saatmaks andmeid hostide vahel. Rakendus avab ühenduse mõlema hosti juures. Et luua ühendus, kasutatakse TCP käepigistust.

<ul>
<li>Klient saadab serverile ühenduse palvega SYN segmendi.</li>
<li>Server saadab kliendile SYN-ACK segmendi, et kinnitada kliendi ühenduse palvet</li>
<li>Klient saadab serverile ACK segmendi, et kinnitada serveri ühenduse palvet</li>
</ul>

Kui see ühendus on saavutatud, võib üle selle admeid vahetada. Andmeid saadetakse segmentidena ja neil on järjekorranumbrid, et nad pärast kohale toimetamist jälle õigesti kokku panna. Meie e-kirja näites kinnitab transpordikiht pordi (25) sihtpunkti sihtpordina.

## Harjutus

Harjutust pole.

## Küsimus

Milline on usaldusväärne transpordiprotokoll?

## Vastus

TCP
