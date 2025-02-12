# stdout (Standard Out)

## Tunni sisu

Praeguseks oleme juba päris paljude käskude ja nende väljunditega tuttavaks saanud ja see viib meid ka edasi järgmise teemani: sisend/väljund vood. Sisestame järgmise käsu ja pärast arutame, kuidas see töötab:

<pre>$ echo Hello World > pähklid.txt</pre>

Mis just praegu juhtus? Aga mine kontrolli seda kataloogi, kus käsk käivitati ja pane end valmis, sest peaksid sealt leidma faili nimega *pähklid.txt*. Kui sinna sisse vaadata, siis peaksid leidma teksti *Hello World*. Selle ühe käsuga juhtus päris palju, vaatame seda jupphaaval.

Vaatame esimest osa:

<pre>$ echo Hello World</pre>

Me teame, et see trükib ekraanile *Hello World*, aga kuidas? Protsessid kasutavad sisend-väljund voogusid, et võtta vastu sisendandmeid ja väljastada väljundeid. Vaikimisi võtab *echo* käsk sisendi (standard sisend või *stdin*) klaviatuurilt ja tagastab väljundi (standardväljund või *stdout*) ekraanile. Seepärast kuvatakse ekraanile *Hello World* kui sisestada käsureale *echo Hello World*. Sisendi-väljundi ümbersuunamisega saame aga seda vaikimisi käitumist muuta, see annab meile failide osas suurema paindlikuse.

Vaatame, mis käsuga edasi juhtus:

<pre> > </pre>

*>* on ümbersuunamise operaator, mis laseb meil muuta seda, kuhu suunatakse standardväljund. See lubab meil suunata *echo Hello Worldi* väljundi ekraani asemel faili. Kui sellist faili veel olemas ei ole, siis see luuakse. Kui see aga on olemas siis kirjutatakse see üle (olenevalt kestast saab lisada käsule lipu, et sellist olukorda vältida).

Ja nii põhimõtteliselt *stdout* ümbersuunamine töötabki!

Ütleme aga, et me ei taha oma *pähklid.txt* faili üle kirjutada. Õnneks on selle jaoks ja olemas ümbersuunamise operaator, *>>*:


<pre>$ echo Hello World >> pähklid.txt</pre>

See lisab *Hello Worldi pähklid.txt* faili lõppu. Kui aga faili eelnevalt ei eksisteerinud, siis luuakse see, justnagu > ümbersuunamise puhulgi.


## Harjutus

Proovida paari käsku:

<pre>
$ ls -l /var/log > minuväljund.txt
$ echo Hello World > rm
$ > mingifail.txt 
</pre>

## Küsimus

Millist käsku kasutada kui on vaja väljund lisada olemasoleva faili lõppu?

## Vastus

*>>*
