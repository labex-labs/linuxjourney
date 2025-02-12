# Ketta anatoomia

## Tunni sisu

Kõvakettaid saab jagada kettajagudeks, luues nõnda blokkseadmeid. Meenutame seadmeid */dev/sda1* ja */dev/sda2*, */dev/sda* on üks terve ketas kuid */dev/sda1* on selle ketta esimene jagu. Kettajaod on äärmiselt kasulikud andmete eraldamiseks. Kui on tarvis mingit konkreetset failisüsteemi kasutada, võib kerge vaevaga luua kettale jao selle asemel, et kogu kettale seda ühte failisüsteemi rakendada.

<b>Kettajagude tabel</b>

Igal kettal on kettajagude tabel, mis edastab süsteemile infot ketta jaotamise kohta. Seal on info selle kohta, kus kettajagu algab ja lõppeb, millised jaod on alglaaditavad, millised sektorid on millistele jagudele määratud jne. Kasutatakse kahte põhilist kettajagude tabelit: *Master Boot Record* (MBR) ja *GUID Partition Table* (GPT).

<b>Kettajagu ehk partitsioon</b>

Kettajagudest koosnevad kettad võimaldavad organiseerida andmeid. Kui kettas on mitmeks osaks jaotatud, ei tohi need omavahel kattuda. Kui kettal on ala, mis ei kuulu kettajao alla, nimetatakse seda vabaks alaks. Kettajao tüüp sõltub kettajagude tabelist. Kettajaol võib olla failisüsteem või võib seda kasutada teisel otstarbel, näiteks  saalimiseks (sellest räägitakse ka varsti).

<i>MBR (Master Boot Record)</i>

<ul>
<li>Traditsiooniline kettajagude tabel, kasutatud kui standardit</li>
<li>Võimaldab primaarseid, laiendatud ja loogilisi kettajagusid</li>
<li>MBR'i piiranguks on kuni neli primaarset kettajagu, peavad asetsema järjest</li>
<li>Täiendavaid kettajagusid saab luua muutes viimase primaarse kettajao laiendatuks (lubatud on ainult üks laiendatud kettajagu). Selle sisse saab omakorda luua kuni 128 loogilist kettajagu (peavad asetsema järjest).</li> 
<li>Toetatud on kuni 2 terabaidised kettad</li>
</ul>

<i>GPT (GUID Partition Table)</i>

<ul>
<li>GPT'st on saamas kettajagude vallas uus standard</li>
<li>Koosseisu kuuluvad vaid ühte tüüpi kettajaod, mida võib luua hulgaliselt (teoreetiliselt piiramatult, praktikas tavaliselt kuni 128)</li>
<li>Igal kettajaol on globaalselt unikaalne ID (GUID)</li>
<li>Kasutatakse peamiselt koos UEFI-põhise alglaadimisega (detailsemalt tuleb sellest juttu hilisemal kursusel)</li> 
<li>maksimaalne ketta suurus 8 ZiB (9,4 ZB) (2<sup>64</sup> sektorit, 512B sektori kohta), tavaliselt kasutatav EXT4 failisüsteem toetab kuni 1 EiB, Btrfs kuni 16 EiB, ZFS kuni 256 ZiB kettajagusid. Loogiliste kettagruppide haldussüsteem LVM2 toetab kuni 8 EiB kettajagusid. See kõik võib aja jooksul muutuda ja enne otsuste tegemist tasub uurida uusimat dokumentatsiooni.</li>
</ul>

Lisainfo:<br>
http://unix.stackexchange.com/questions/33555/what-is-the-max-partition-supported-in-linux  
http://en.wikipedia.org/wiki/Comparison_of_file_systems  
https://en.wikipedia.org/wiki/Binary_prefix  

<b> Failisüsteemi struktuur</b>

Eelmisest peatükist on teada, et failisüsteem on failide ja kataloogide organiseeritud kogum. Kõige lihtsamalt võib seda vaadelda kui kooslust andmebaasist, mis haldab faile ja andmed ise. Kuid nüüd süveneme sellesse väheke detailsemalt.

<ul>
<li>Alglaadimise plokk - See asub failisüsteemi esimestes sektorites. Seda otseselt ei kasutata, vaid hoiab informatsiooni operatsiooni alglaadimise jaoks. Selliseid plokke on operatsioonisüsteemil tarvis vaid ühte. Kui partitsioone on rohkem, leidub ka neil alglaadimise plokk kuid paljusid ei kasutata.</li>
<li>Superplokk - üksik plokk, mis järgneb kohe alglaadimisplokile. Sisaldab infot failisüsteemi kohta: infosõlmetabel, loogiliste jagude ja failisüsteemi suurus. </li>
<li>Infosõlmede tabel - sellest võib mõelda kui andmebaasist, mis haldab andmeid (ei tasu muretseda, sellest tuleb terve peatükk). Iga faili või kataloogi kohta on selles tabelis unikaalne kirje. Failide kohta hoitakse erinevat informatsiooni. </li>
<li>Andmeplokid - failide ja kataloogide tegelikud andmed </li>
</ul>

Tutvume erinevate kettajagude tabelitega. All on näide kettajaost, mis kasutab MBR kettajagude tabelit (*msdos*). Kergesti on eristatavad primaarne, laiendatud ja loogilised kettajaod.

<pre>
pete@icebox:~$ sudo parted -l
Model: Seagate (scsi)
Disk /dev/sda: 21.5GB
Sector size (logical/physical): 512B/512B
Partition Table: msdos

Number  Start   End     Size    Type      File system     Flags
 1      1049kB  6860MB  6859MB  primary   ext4            boot
 2      6861MB  21.5GB  14.6GB  extended
 5      6861MB  7380MB  519MB   logical   linux-swap(v1)
 6      7381MB  21.5GB  14.1GB  logical   xfs
</pre>

GPT kasutab kettajagudel ainult unikaalseid ID'sid.

<pre>
Model: Thumb Drive (scsi)
Disk /dev/sdb: 4041MB
Sector size (logical/physical): 512B/512B
Partition Table: gpt

Number  Start   End     Size     File system  Name        Flags
 1      17.4kB  1000MB  1000MB                first
 2      1000MB  4040MB  3040MB                second
</pre>

## Harjutus

Sisestada käsk <b>parted -l</b> ja hinnata tulemust.

## Küsimus

Millist kettajao tüüpi peaks kasutama, et luua rohkem kui 4 partitsiooni MBR skeemi järgi?

## Vastus

laiendatud
