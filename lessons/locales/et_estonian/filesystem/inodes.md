# Infosõlmed

## Tunni sisu

Meenutame, et failisüsteem koosneb failidest ning andmebaasist mis neid haldab. Seda andmebaasi nimetatakse infosõlmede tabeliks.

<b>Mis on infosõlm?</b>

Infosõlm on kirje infosõlmede tabelis ja neid on iga faili kohta üks. See kirjeldab faili kohta kõike, näiteks:

<ul>
<li>Faili tüüp - tavaline fail, kataloog, tähemärgi seade jne </li>
<li>Omanik</li>
<li>Grupp</li>
<li>Ligipääsuõigused</li>
<li>Ajatemplid - mtime (viimase muutmise aeg), ctime (viimane atribuudi muutmise aeg), atime (viimatise ligipääsu aeg)</li>
<li>Püsiviitade arv</li>
<li>Faili maht</li>
<li>Failile eraldatud plokkide arv</li>
<li>Faili andmeplokkide viidad - kõige olulisem!</li>
</ul>

Kokkuvõtvalt hoitakse infosõlmedes kõike peale faili nime ja faili enda.

<b>Millal infosõlmed luuakse?</b>

Sel hetkel kui luuakse failisüsteem eraldatakse ka ruum infosõlmedele. Sõltuvalt ketta omadustest ja muudest näitajatest otsustavad algoritmid kui palju ruumi infosõlmedele vaja on. Tõenäoliselt on iga kasutaja mingil hetkel näinud veateateid otsalõppeva kettaruumi kohta. Sama võib juhtuda ka infosõlmedega (kuigi vähem levinud). Kui infosõlmedel saab ruum otsa, ei saa rohkem faile luua. Jätame meelde, et andmete varundamismaht sõltub nii andmetest kui andmebaasist.

Käsuga <b>df -i</b> kuvame kui palju infosõlmi veel on võimalik kasutada.

<b>Informatsioon infosõlmede kohta</b>

Infosõlmi eristatakse numbritega, kui fail luuakse, määratakse sellele infosõlme number. Numbreid määratakse järjekorras. Vahel võib küll märgata, et loodud failile määratakse eelmisest madalam number. Seda põhjustab numbrite korduvkasutus. Kui fail kustutakse, siis number vabaneb uute failide jaoks. Infosõlmede numbrite kuvamiseks on käsk <b>ls -li</b>:

<pre>
pete@icebox:~$ ls -li
140 drwxr-xr-x 2 pete pete 6 Jan 20 20:13 Desktop
141 drwxr-xr-x 2 pete pete 6 Jan 20 20:01 Documents
</pre>

Esimeses väljas kuvataksegi infosõlme number.

Faili kohta saab detailset infot ka *stat* käsuga. Ka see kuvab infot infosõlmede kohta.

<pre>
pete@icebox:~$ stat ~/Desktop/
  File: ‘/home/pete/Desktop/’
  Size: 6               Blocks: 0          IO Block: 4096   directory
Device: 806h/2054d      Inode: 140         Links: 2
Access: (0755/drwxr-xr-x)  Uid: ( 1000/   pete)   Gid: ( 1000/   pete)
Access: 2016-01-20 20:13:50.647435982 -0800
Modify: 2016-01-20 20:13:06.191675843 -0800
Change: 2016-01-20 20:13:06.191675843 -0800
 Birth: -
</pre>

<b>Kuidas leiavad infosõlmed faili asukoha?</b>

Kasutaja teab, et tema failid on kusagil ketta peal. Kahjuks aga neid ilmselt ei salvestatud kenasti üksteisei järel ning siin on olulised infosõlmed, sest need osutavad tegelikele andmeplokkidele. Tüüpilises failisüsteemis (kuna need kõik ei tööta ühtemoodi) on igal infosõlmel 15 viita. Esimesed 12 osutavad otseselt andmeplokkidele. 13. viitab plokile, kus on viidad veel rohkematele plokkidele, 14. osutab veel ühele viitade alamplokile ja 15 viitab ka jälle plokile viitadele. Arusaadavalt on see veidi keeruline. Asjade nõndaviisi organiseerimise põhjus peitub soovis, et kõik infosõlmed oleksid ühesuguse struktuuriga, kuid oleksid samal ajal võimelised viitama erineva suurusega failidele. Väiksema faili leiab kiiremini esimese 12 viidaga, kuid suuremaid faile tuleb juba otsida alamviitadega. Mõlemal juhul on infosõlme struktuur ikkagi sama.

## Harjutus

Tutvuda erinevate failide infosõlmedega. Millised luuakse tavaliselt esimesena?

## Küsimus

Kuidas kuvada, mitu infosõlme veel süsteemis järgi on?

## Vastus

*df -i*
