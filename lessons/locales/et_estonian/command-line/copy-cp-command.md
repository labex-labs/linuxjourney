# cp (Copy)

## Tunni sisu

Teeme mõnest failist koopiad. Sarnaselt teistes operatsioonisüsteemides kopeerimisele ja kleepimisele, võimaldab kest meil seda teha isegi veel lihtsamalt.

<pre>$ cp minuvingefail /home/pete/Dokumendid/vingeddokud</pre>

minuvingefail on see fail, mida tahetakse kopeerida ja /home/pete/Dokumendid/vingeddokud on see kataloog kuhu kopeerida.

Korraga saab kopeerida ka mitmeid faile ja katalooge kasutades metamärki. Metamärk on selline tähemärk, mis võib asendada mingil mustril põhinevat valikut, andes otsimiseks rohkem vabadust. Pandlikkuse mõttes võib metamärke kasutada iga käsu juures.


<ul>
<li>* metamärkide metamärk, kasutatakse, et esindada ükskõik millist (arvu) sümbolit või sõnet</li>
<li>? esindab ühte sümbolit</li>
<li>[] esindab ükskõik millist kantsulgudesse kirjutatud sümbolit</li>
</ul>

<pre>$ cp *.jpg /home/pete/Pildid</pre>

See käsk kopeerib kõik .jpg laiendiga failid jooksvast kataloogist kataloogi /home/pete/Pildid.

Päris kasulik on kasutada ka -r lippu, see kopeerib tagasiulatuvalt kataloogis asuvad alamkataloogid ja failid.

Proovida kasutada cp käsku, et kopeerida Dokumentide kausta mõni kataloog, milles on failid sees. See ei töötanud, eks? Seda selle pärast, et kopeerima peab ka kõik failid ja kataloogid, mis seal kaustas sees on käsuga -r.

<pre>$ cp -r Kõrvits/ /home/pete/Dokumendid</pre>

Oluline on panna tähele, et kui kopeerida faili kataloogi, milles on sama nimega fail, siis see fail kirjutatakse üle kopeeritava failiga. See ei ole väga hea kui konkreetses failis on midagi mida ei taheta kogemata üle kirjutada. Ohutum on kasutada lippu -i (interaktiivne), et küsitaks nõusolekut enne kui fail üle kirjutatakse.

<pre>$ cp -i minuvingefail /home/pete/Pildid</pre>

## Harjutus

Kopeerida mõnda faili kuid olla ettevaatlik, et midagi olulist üle ei kirjutaks.

## Küsimus

Millist lippu on täpsustamiseks vaja, kui soovitakse kopeerida kataloogi?

## Vastus

-r
