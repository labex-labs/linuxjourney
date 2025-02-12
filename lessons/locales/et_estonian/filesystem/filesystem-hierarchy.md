# Failisüsteemi hierarhia

## Tunni sisu

Praeguseks võiks juba kataloogisüsteem üsna tuttav olla. Kui see aga nii ei ole siis peagi saab kõik selgeks. Kuigi failisüsteemid erinevad üksteisest struktuuri poolest, peaksid nad suuremal määral siiski alluma [failisüsteemi hierarhia standardile](http://refspecs.linuxfoundation.org/fhs.shtml).

Vaatame käsuga <b>ls -l /</b> juurkataloogi sisu. Kuigi võib esineda väikeseid erandeid, peaks see välja nägema enamasti selline:

<ul>
<li>/ - Kogu failisüsteemi hierarhia juurkataloog, milles paiknevad kõik teised kataloogid.</li>
<li>/bin - Esmatähtsad töövalmis programmid (binaarid). Seal asuvad kõige elementaarsemad käsud, nagu ls ja cp.</li>
<li>/boot - Tuuma alglaaduri failid.</li>
<li>/dev - Seadmefailid.</li>
<li>/etc - Süsteemi keskne seadistuste kataloog, milles peaksid olema ainult sätetefailid ja mitte binaarid</li>
<li>/home - Kasutajate personaalsed kataloogid dokumentide, failide, sätete ja muu hoidmiseks. </li>
<li>/lib - Binaaride kasutatavate teekide failid.</li>
<li>/media - Välise meedia (nt USB kettad), arvutisse ühendumise punkt.</li>
<li>/mnt - Ajutiselt ühendatud failisüsteemid.</li>
<li>/opt - Valikulised rakenduste tarkvarapaketid.</li>
<li>/proc - Hetkel töötavate protsesside informatsioon.</li>
<li>/root - Juurkasutaja kodukataloog.</li>
<li>/run - Informatsioon töötava süsteemi kohta alates viimasest käivitamisest.</li>
<li>/sbin - Sisaldab esmatähtsaid süsteemibinaare, tavaliselt käivitatavad ainult juurkasutaja õigustes.</li>
<li>/srv - Asukohapõhised andmed.</li>
<li>/tmp - Ajutiste failide hoidla. </li>
<li>/usr - Selle kataloogi nimi ei ole eriti hästi õnnestunud, tavaliselt ei hoita siin kasutajate faile nagu kodukataloogis. See on mõeldud kasutaja paigaldatud tarkvarale ja haldusvahenditele kuid tõesti, ka isiklike kataloogide loomine sinna ei ole keelatud. Selles kataloogis on olulised alamkataloogid nagu /usr/bin, /usr/local jne.</li>
<li>/var - Muutujate kataloogi kasutatakse süsteemi sisse logimisel, kasutuajate jälgimisel, vahemälu jaoks jpm. Põhimõtteliselt hoitakse siin kõike, mis on pidevas muutumises.</li>
</ul>

## Harjutus

Vaadata */usr* kataloogi sisse ja tutvuda seal hoitava informatsiooniga.

## Küsimus

Millises kataloogis hoitakse logifaile?

## Vastus

*/var*
