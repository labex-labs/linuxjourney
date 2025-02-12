# Signaalid

## Tunni sisu

Signaal on teade protsessile, et midagi on juhtunud.

<b<Signaalide eesmärk</b>

Signaalid on tarkvaralised katkestused ja neil on palju eesmärke:

<ul>
<li> Kasutaja saab kasutada spetsiaalseid terminali klahvikombinatsioone, et protsesse peatada (<i>q, CTRL+Q</i> jne - erinevatel protsessidel võivad erinevad olla), katkestada (<i>CTRL+C</i>) või ajutiselt peatada (<i>CTRL+Z</i>). </li>
<li>Ilmneb riistvaraline probleem ja tuum tahab protsessi sellest teavitada.</li>
<li>Ilmneb tarkvaraline probleem ja tuum tahab protsessi sellest teavitada.</li>
<li>Põhimõtteliselt on need protsesside suhtlemise viisid.</li>
</ul>

<b>Signaali protsess</b>

Kui mõnest sündmusest tekib signaal siis edastatakse see protsessile. Signaal on kuni kohalejõudmiseni ootavas olekus. Signaali peetakse kohale toimetatuks kui protsess käivitatakse. Küll aga on protsessidel signaalimaskid ja signaalide kohaletoimetamise saab blokeerida kui see on nõnda täpsustatud. Kui protsess saab signaali, võivad juhtuda järgmised asjad:

<ul>
<li>Signaali ignoreeritakse</li>
<li>Signaal "püütakse kinni" ja teostatakse vastavad toimingud</li>
<li>Protsess peatatakse ennetähtaegselt vastandina tavapärasele töö peatamise süsteemsele kutsele</li>
<li>Signaal blokeeritakse sõltuvalt signaali maskist</li>
</ul>

<b>Tavalisemad signaalid</b>

Iga signaali määratleb täisarvuline number (*integer*) ja sümboolne nimi kujul SIGxxx. Mõned tavalisemad signaalid on:

<ul>
<li>SIGHUP või HUP või 1: <i>Hangup</i>ehk kontrollterminali sulgumine</li>
<li>SIGINT või INT või 2: <i>Interrupt</i> ehk katkestamine</li>
<li>SIGKILL või KILL või 9: <i>Kill</i> ehk jõuga peatamine</li>
<li>SIGSEGV või SEGV või 11: <i>Segmentation fault</i> ehk segmenteerimise viga</li>
<li>SIGTERM või TERM või 15: <i>Software termination</i> ehk tarkvara tegevuse lõpetamine</li>
<li>SIGSTOP või STOP: <i>Stop</i> ehk protsessi ajutine peatamine (jätkamiseks SIGCONT)</li>
</ul>

Kuna numbrid signaalidel muutuvad, kasutatakse pigem nimesid. Loetelu signaalidest ja nende numbritest saab *kill -l* abil.

Leidub signaale, mida ei saa blokeerida. Üks selline näide on SIGKILL signaal. KILL signaal hävitab protsessi.

## Harjutus

Harjutust pole.

## Küsimus

Millist signaali ei saa blokeerida?

## Vastus

SIGKILL
