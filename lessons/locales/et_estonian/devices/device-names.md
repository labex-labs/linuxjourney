# Seadmete nimed

## Tunni sisu

Mõned levinumad seadmete nimed:

<b>SCSI seadmed</b>

Massmäluseadmed kasutavad kõige tõenäolisemalt SCSI (hääldatakse "skazi") protokolli. SCSI tähendab *Small Computer System Interface*, mis tõlkes oleks väikearvutisüsteemi liides. Tegu on protokolliga, mida kasutatakse välisseadmete nagu kettad, printerid, skannerid ja muu ühendamiseks arvutiga. Eksisteerivad SCSI seadmed, mida kaasajal tegelikult enam ei kasutata, Linux aga samastab SCSI kettad */dev* kataloogis füüsiliste kõvaketastega, mida nimetatakse ka plokkseadmeteks (*block device*) ja nende vaatamiseks käsk *lsblk*. Neid esindab eesliide *sd(SCSI disk):*

Tavapärased SCSI seadmefailid:

<ul>
<li><i>/dev/sda</i> - esimene kõvaketas</li>
<li><i>/dev/sdb</i> - teine kõvaketas</li>
<li><i>/dev/sda3</i> - esimese kõvaketta kolmas kettajagu</li>
</ul>

<b>Pseudoseadmed</b>

Kordame, et pseudoseadmed ei ole tegelikult füüsiliselt arvutiga ühendatud ning enamik pseudoseadmeid on tähemärgiseadmed:

<ul>
<li><i>/dev/zero</i> - võtab vastu ja heidab kogu sisendi kõrvale, väljundiks on NULL (nullväärtus) baitide jada</li>
<li><i>/dev/null</i> - võtab vastu ja heidab kogu sisendi kõrvale  ning väljundit ei anna </li>
<li><i>/dev/random</i> - toodab juhuslikke numbreid</li>
</ul>

<b>PATA seadmed</b>

Mõnikord, just vanemates süsteemides, võib näha, et kõvaketastele viidatakse hd prefiksiga:

<ul>
<li><i>/dev/hda</i> - Esimene kõvaketas</li>
<li><i>/dev/hdd2</i> - Neljanda kõvaketta teine kettajagu</li>
</ul> 

## Harjutus

Kirjutada pseudoseadmetele ning uurida väljundit. Ettevaatust, et ei kirjutaks nendele oma kettaid! Ohutuse mõttes on soovitav harjutusi sooritada virtuaalarvutis, näiteks [VirtualBox](https://www.virtualbox.org/)'i keskkonda paigaldatud Linuxis.

## Küsimus

Milline oleks tavaliselt teise SCSI ketta esimese kettajao seadmenimi?

## Vastus

*sdb1*
