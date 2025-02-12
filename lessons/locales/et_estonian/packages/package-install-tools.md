# rpm ja dpkg

## Tunni sisu

Kuigi suurem osa sellest kurusest räägib paketihaldussüsteemidest (paketihalduse Batmanid), ei tohi unustada ka Robineid. Kuigi väga kasulikud ja usaldusväärsed, ei ole nendel uhket autot ja nutivööd.

Just nagu .exe on üksik käivitatav fail, on seda ka .deb ja .rpm. Kui kasutada paketihoidlaid siis tavapäraselt neid eriti ei näe, kuid kui paketid otse alla laadida siis on nad nendes poplaarsetes vormingutes. Loomulikult on nad distributsioonipõhised, .deb Debiani - ja .rpm Red Hat'i-põhistele süsteemidele.

Nende pakettide paigaldamiseks võib kasutada käske *rpm* ja *dpkg*. Nõnda paigaldatakse paketifailid, küll aga mitte eelmises peatükis mainitud olulised sõltuvused. Seega, kui paketil on 10 sõltuvust, peaks need paketid ka eraldi veel paigaldama ning sama kehitb omakorda ka nende sõltuvuste kohta. Nagu isegi näha võib, on see üks põhjusi, mis kutsus ellu täiskohaga haldussüsteemid, millest räägitakse veidi hiljem.

Kuna ilmselt tuleb ette loendamatu arv kordi kui on vaja nende käskudega paigaldada, pärida või kinnitada pakette, võiks need meelde jääta.

<b>Paketi paigaldamine</b>

<pre>
Debian: $ dpkg -i mingi_deb_pakett.deb
RPM: $ rpm -i mingi_rpm_pakett.rpm
</pre>

*i* tähistab *installeerimist* ehk *paigaldamist*. Võib kasutada ka pikemat formaati --install.

<b>Paketi eemaldamine</b>

<pre>
Debian: $ dpkg -r mingi_deb_pakett.deb
RPM: $ rpm -e mingi_rpm_pakett.rpm
</pre>

Debian: <b>r</b> nagu *remove* tähendab eemaldamist
RPM: <b>e</b> nagu *erase* tähendab kustutamist

<b>Kuva paigaldatud paketid</b>

<pre>
Debian: $ dpkg -l
RPM: $ rpm -qa
</pre>

Debian: <b>l</b> nagu loetle

RPM: <b>q</b> nagu *query* ehk päring <b>a</b> nagu *all* ehk kõik

## Harjutus

Leida mingi programm, mida on soov paigaldada, näiteks Google Chrome, ja paigaldada see kasutades õpitud käske.

## Küsimus

Milline on .deb failide paketihaldustööriist?

## Vastus

dpkg
