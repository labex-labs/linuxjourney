# NAT

## Tunni sisu

NAT'i (*<b>N</b>etwork <b>A</b>ddress <b>T</b>ranslation*) ehk võrguaadresside teisendamist on juba varem ka mainitud. Kui tegutseme enda võrgus kas IP aadress on siis Internetist näha? Mitte päris.

NAT muudab seadme nagu marsruuter justkui vahemeheks Interneti ja kohtvõrgu vahel. Seega on vaja ainult ühte IP aadressi, et esindada kõiki marsruuteri taha jäävaid arvuteid.

NAT on justkui suure kontorihoone vastuvõtt. Kui keegi tahab mingi konkreetse kasutajaga ühendust võtta, on tal vaid kogu kontori number. Inimesed retseptsioonis peavad otsima üles suunava numbri ja edastama kõne sihtkohta.

<b>Kuidas see töötab?</b>

Lihtsam juhtum näeks välja nii:

<ol>
<li> Peeter tahab saada ühendust aadressiga www.google.com, seega saadab tema arvuti päringu läbi marsruuteri.</li>
<li> Marsruuter võtab selle päringu ja avab hoopis enda ühenduse www.google.com'ga, seejärel saadab päringu Peetrile.</li>
<li>Marsruuter vahendab Peetri ja www.google.com vahelist ühendust. Google ei tea Peetrist midagi, tema näeb ainult marsruuterit.</li>
</ol>

NAT ja marsruutimine üldisemalt võivad üsna keeruliseks minna kuid me ei süvene liialt pisiasjadesse.

## Harjutus

Harjutust pole.

## Küsimus

Mida kasutatakse selleks, et esindada kogu võrku Internetile ühe aadressina?

## Vastus

NAT
