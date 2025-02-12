# DNS'i komponendid

## Tunni sisu

Interneti DNS andmebaas põhineb saitide ja organisatsioonide poolt jagatud andmebaasidel. Selleks on aga vaja:

<b>Nimeserver</b>

DNS seatakse üles nimeserverina kuhu on laetud DNS sätted ja seadistused ning vastused klientide küsimustele nagu "Kes on www.google.com ?". Kui nimeserver sellele küsimusele vastata ei oska, edastatakse see mõnele teisele serverile. Nimeserverid võivad olla autoriteetsed mis tähendab, et seal hoitakse DNS kirjeid või siis rekursiivsed mis tähendab, et küsimust edastatakse aina järgmistele serveritele kuni leitakse autoriteetne server, milles asub päritav DNS kirje. Kuid rekursiivsetes serverites võib ka olla salvestatud otsitav informatsioon, mis juhul ei pea autoriteetset serverit otsima hakkama.

<b>Tsooni fail</b>

Nimeserveris elab tsoonifail. Tsoonifailis hoiab nimeserver informatsiooni domeeni või selleni jõudmise kohta.

<b>Ressursikirjed</b>

Tsoonifail koosneb ressursikirjetest. Iga rida on kirje, milles hoitakse informatsiooni kas hosti, nimeserverite või muude ressursside kohta. Väljad kajastavad järgmist:

<ul>
<li>Kirje nimi.</li>
<li><i>TTL</i> - Aeg, mille möödudes kirje eemaldatakse ja hangitakse uus. DNS'i puhul on TTL ajaline väärtus, kirjete eluiga võiks olla näiteks üks tund. Sellist mehhanismi on vaja Interneti pideva muutumise tõttu. Üks ja sama host võib ühel hetkel omada IP aadressi X ja juba järgmisel IP aadressi Y.</li>
<li><i>Class</i> - Kirje informatsiooni nimeruum, tavaliselt kasutatakse Interneti kohta IN.</li>
<li><i>Type</i> - Kirjes salvestatava informatsiooni tüüp. Kõige levinumad on A aadressi kohta, CNAME alamdomeenide (ka aliaste) kohta ja MX kirjade vahendamise kohta jne. Sellel kursusel kirje tüüpidele ei keskenduta.</li>
<li><i>Data</i> - Selles väljas võib olla IP aadress kui kirje tüüp on A või midagi muud sõltuvalt tüübist.</li>
</ul>

<pre>
patty    IN  A      192.168.0.4 
</pre>
 
MX-kirjete kontrollimiseks on loodud mitmeid vahendeid:
* http://mxtoolbox.com/
* https://toolbox.googleapps.com/apps/checkmx/
* http://checkmx.com/
* http://www.dnsqueries.com/en/mx-lookup.php

## Harjutus

Harjutust pole.

## Küsimus

Millist kirjetüüpi kasutatakse e-posti vahendajate kohta?

## Vastus

*MX*
