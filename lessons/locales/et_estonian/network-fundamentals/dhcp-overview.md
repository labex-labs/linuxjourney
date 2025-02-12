# DHCP ülevaade

## Tunni sisu

Oluline osa võrgu toimimisest, millest pole veel räägitud on DHCP (*Dynamic Host Configuration Protocol*) ehk automaatne võrgu iseseadistumise protokoll.

DHCP määrab arvutitele IP aadresse, alamvõrgumaske ja lüüse. Ütleme, et meil on telefon ja vaja on telefoninumbrit, et inimestega rääkida. Peab võtma ühendust teenusepakkujaga ja nende poolt määratakse telefonile number. Nii kaua kui arved on makstud võib muretult telefoni kasutada. DHCP on selles näites teenusepakkuja. See annab arvutile IP aadressi selleks, et teiste IP aadressidega suhelda. IP aadresse liisitakse mingiks perioodiks, mille möödudes liisingut uuendatakse vastavalt selle seadetele.

DHCP on kasulik väga mitmel põhjusel. Tänu sellele ei pea võrguadministraator muretsema IP aadresside jaotamise pärast ning välistatud on ka duplikaatide väljastamine. Igal füüsilisel võrgul peaks olema isiklik DHCP server, et kliendid saaksid küsida IP aadresse. Koduses keskkonnas on DHCP serveri rollis marsruuter.

DHCP toimib nii:

<ol>
<li>DHCP DISCOVER - See on leviedastuse sõnum leidmaks DHCP serverit.</li>
<li>DHCP OFFER - DHCP server vastab pakkumisega, mille paketis sisaldub liisimise aeg, alamvõrgu mask, IP aadress ja muud.</li>
<li>DHCP REQUEST - Kliend saadab veel ühe leviedastuse sõnumi, et anda kõikidele DHCP serveritele teada, milline pakkumine vastu võeti.</li>
<li>DHCP ACK - Server saadab kinnituse.</li>
</ol>

DHCP on pisut keerulisem kuid üldpilt on selline.

## Harjutus

Harjutust pole.

## Küsimus

Millised on DHCP päringu sammud?

## Vastus

DISCOVER, OFFER, REQUEST, ACK
