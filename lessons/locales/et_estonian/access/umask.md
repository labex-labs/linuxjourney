# Umask

## Tunni sisu

Iga loodav fail saab endale vaikimisi komplekti õigusi. Kui peaks tekkima vajadus neid vaikimisi määratavaid õigusi muuta, saab seda teha *umask* käsuga. Käsk kasutab numbriformaati:<br>
<ul>
<li>4: lugemisõigus</li>
<li>2: kirjutamisõigus</li>
<li>1: käivitamisõigus</li>
</ul>

Kuid õiguste lisamise asemel võtab *umask* neid hoopis ära.

<pre>
$ umask 021
</pre>

Ülemises näites ütleme, et me tahame, et uutele failidele antaks vaikimisi järgmised õigused: Kasutajatel on ligipääs kõigele, kuid gruppidelt võtame ära õiguse kirjutada ja teistelt kasutajatelt võtame ära käivitamise õiguse. Vaikimisi on *umask* enamustel Linuxitel 022, mis tähendab kõiki õigusi kasutajale, kuid grupil ja teistel kasutajatel puudub kirjutamisõigus.

Teiste sõnadega võetakse *umask*'i puhul aluseks vaikimisi õigused kataloogide puhul 777 ja failide osas 666 ning *umask* väärtus lahutatakse nendest ja saadakse reaalsed õigused.
Näiteks *umask*'i väärtuse 022 puhul:
* kataloogiõigused: 777 – 022 = 755
* failiõigused: 666 – 022 = 644

Kokkuvõttes *umask*'i kaheksandväärtused ja neile vastavad (allesjäävad) õigused:
* 0 : lugemine, kirjutamine, käivitamine
* 1 : lugemine, kirjutamine
* 2 : lugemine, käivitamine
* 3 : ainult lugemine
* 4 : kirjutamine, käivitamine
* 5 : ainult kirjutamine
* 6 : ainult käivitamine
* 7 : õigused puuduvad

Kui *umask* käsk sisestada, antakse vaikimisi õigused kõikidele uutele failidele, mis luuakse. Kui aga on soov, et sätted oleksid püsivad, tuleb muuta faili:
* globaalne (kõik kasutajad): <i>/etc/profile</i>
* hetkel vaikimisi sisseloginud kasutaja: <i>~/.bashrc</i><br>
... ja lisada väärtus, näiteks:
* <i>umask 021</i>

Kui soovitakse terminali sulgemata või kasutajat välja logimata sessiooniskripti rakendada siis käivitada näiteks:
<pre>
source ~/.bashrc
</pre>

## Harjutus

<ol>
<li> Luua uus fail ja kontrollida selle õigusi.</li>
<li> Muuta <i>umask</i>'i ja luua veel üks uus fail.</li>
<li> Kontrollida taaskord uue faili õigusi, mida võib näha?</li>
</ol>

## Küsimus

Millise käsuga muudetakse vaikimisi failiõigusi?

## Vastus

*umask*
