# Failiõigused

## Tunni sisu

Nagu varem juba õppisime on failidel erinevad ligipääsuõigused või režiimid. Vaatame näidet:

<pre>
$ ls -l Desktop/

drwxr-xr-x 2 peeter pingviinid 4096 Dec 1 11:45 .
</pre>

Failiõigused koosnevad neljast osast. Esimene on faili tüüp, mida tähistab esimene tähemärk. Meie näites on tegu kataloogiga, seda tähistab <b>d</b> failitüübi koha peal. Kõige levinum on tavalist faili tähistav <b>-</b>.

Järgmised kolm osa on otseselt seotud ligipääsuõigustega. Need on grupeeritud igaüks 3 bitiseks osaks. Esimesed kolm bitti on kasutaja õigused, seejärel grupi õigused ja viimaks on õigused mis rakenduvad kõigile teistele. All on lisatud toruoperaatorid, et oleks selgem aru saada.

<pre>
d | rwx | r-x | r-x 
</pre>

Iga tähemärk esindab erinevat õigust:

<ul>
<li>r: lugemine</li>
<li>w: kirjutamine</li>
<li>x: käivitamine</li>
<li>-: tühi</li>
</ul>

Seega võib ülemisest näitest aru saada, et Peetril on kataloogi (tähis <b>d</b> failitüübi koha peal) lugemise, kirjutamise ja käivitamise õigused, pingviinide grupil on lugemise ja käivitamise õigused ning kõikidel ülejäänud kasutajatel on samuti lugemise ja käivitamise õigused. Kataloogi puhul tähendab käivitusõigus sinna sisenemist.

## Harjutus

Kasutada *ls -l* käsku erinevate failide peal ja tuvastada kahtivad ligipääsuõigused.

## Küsimus

Kuidas tähistatakse käivitamise õigust?

## Vastus

x
