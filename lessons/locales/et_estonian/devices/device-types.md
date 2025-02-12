# Seadme tüübid

## Tunni sisu

Enne kui alustada seadmete haldamise teemat, võiks mõnda lähemalt uurida.

<pre>$ ls -l /dev
brw-rw----   1 root disk      8,   0 Dec 20 20:13 sda
crw-rw-rw-   1 root root      1,   3 Dec 20 20:13 null
srw-rw-rw-   1 root root           0 Dec 20 20:13 log
prw-r--r--   1 root root           0 Dec 20 20:13 fdata
</pre>

Tulbad vasakult paremale:

<ul>
<li>Õigused</li>
<li>Omanik</li>
<li>Grupp</li>
<li>Juhtprogrammi klass</li>
<li>Seadme klass</li>
<li>Ajatempel</li>
<li>Seadme nimi</li>

Meenutame, et *ls* käsu väljundi iga rea esimene bitt kajastab faili tüüpi. Seadmefaile märgistatakse järgmiselt:

<ul>
<li>c - tähemärk</li>
<li>b - plokk</li>
<li>p - toru</li>
<li>s - sokkel</li>
</ul>

<b>Tähemärgiseadmed</b>

Need seadmed töötlevad andmeid, kuid üks tähemärk korraga. Paljud pseudoseadmed (nt */dev/null*) on sellised. Pseudoseadmed ei ole tegelikult füüsiliselt arvutiga ühendatud, kuid võimaldavad operatsioonisüsteemil paremini toimida.

<b>Plokkseadmed</b>

Need seadmed töötlevad andmeid suurte fikseeritud suurustega plokkidena. Tavapäraselt on sellised andmeplokke kasutavad seadmed näiteks kõvakettad ja failisüsteemid.

<b>Toruseadmed</b>

Nimega toruoperaatorid võimaldavad kahel või enamal protsessil omavahel suhelda. Need on tähemärgiseadmetele väga sarnased, kuid selle asemel, et saata väljund seadmele, saadetakse see teisele protsessile.

<b>Sokkelseadmed</b>

Sokkelseadmed hõlbustavad protsessidevahelist suhtlust. Erinevalt toruseadmetest võivad need suhelda üheaegselt mitme protsesssiga.

<b>Seadmete iseloomustamine</b>

Seadmeid iseloomustatakse <b>juhtprogrammi klassi</b> ja <b>seadme klassiga</b>. Neid numbreid võib näha eeltoodud *ls* väljundi näites. Numbreid eraldatakse komaga, näiteks ütleme, et seadme klassid on: <b>8, 0</b>:

Juhtprogrammi klass esindab juhtprogrammi, meie puhul 8, mis on tihti sd blokkseadmete klass. Seadme klass tuvastab tuuma jaks konkreetse seadme. Meie näites 0 esindab esimest seadet (a).

## Harjutus

Minna /dev kataloogi ja uurida, mis tüüpi seadmeid seal on.

## Küsimus

Millist sümbolit kasutatakse tähemärgiseadmete jaoks *ls -l* käsuga?

## Vastus

c
