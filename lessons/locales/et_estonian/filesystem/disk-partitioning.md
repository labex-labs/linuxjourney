# Ketta jaotamine

## Tunni sisu

Järgnevalt harjutame failisüsteemi praktilist poolt USB pulga peal. Ei tasu muretseda kui endal ühte käepärast ei ole, võib ka lihtsalt kaasa mõelda.

Esiteks on tarvis tekitada kettajaod. Kettajagude loomisega tasub olla **eriti ettevaatlik** kuna sellega võidakse kustutada kettajagu, mis sisaldab olulisi andmeid. Samuti uue kettajagude tabeli loomisega kustuvad kõik kettajaod ja seal olnud andmed. **Seetõttu tasub enne kettajagudega tegelemist teha andmetest varukoopia**. Mõned programmid salvestavad tehtud muudatused automaatselt, kinnitust küsimata. Algajatel tasub valida selline programm, mis kohe tehtud muudatusi ei salvesta. Ohutum on eelnevalt näiteks mõnes virtuaalarvutis järgi proovida ja kui ollakse juba kindlad siis tasub alles päris arvutis ketaste jagamise juurde minna. Virtuaalarvutisse (nt [VirtualBox](https://www.virtualbox.org/)'i keskkonnas) on lihtne lisada virtuaalseid kõvakettaid ja neid siis harjutamise mõttes jagudeks jagada.

Olemasolevate ja loodud kettajagude vaatamiseks sobib ka *lsblk*. Failisüsteeme näeb ka *lsblk -f* abil.

Ketta jagamiseks on saadaval palju tööriistu:

<ul>
<li><i>fdisk</i> - lihtne käsureapõhine tööriist, vaikimisi kasutab MBR'i kuid toetab ka GPT'd. Salvestab muudatused alles siis kui selleks vastav käsklus antakse.</li>
<li><i>cfdisk</i> - lihtne ja osaliselt pseudograafiline programm kettajagude ja nende tabelite haldamiseks. Salvestab muudatused alles siis kui selleks vastav käsklus antakse.</li>
<li><i>parted</i> - käsureapõhine tööriist, mis toetab nii MBR'i kui GPT'd. NB! Salvestab koheselt (automaatselt, küsimata) tehtud muudatused! Olla eriti ettevaatlik!</li>
<li><i>gparted</i> - parted'i graafiline versioon</li>
<li><i>gdisk</i> - sisuliselt fdisk kuid toetab ainult GPT'd ja mitte MBR'i (MBR teisendatakse koheselt GPT tabeliks, millega andmed kustuvad kuna kettajagude tabel kirjutatakse üle - kui kohe programmist väljuda q ja Enter abil ja mitte salvestada siis muudatused ei jõustu). Salvestab muudatused alles siis kui selleks vastav käsklus antakse.</li>
</ul>

Meie kasutame *parted*'it enda kettajagude loomiseks. Ütleme, et ühendatud USB seadme nimi on */dev/sdb*.

*Parted* on väga võimas tööriist ning kettajagude loomisel tasuks olla ettevaatlik. Erinevalt teistest kettajagude loomise programmidest salvestab *parted* **koheselt** (automaatselt, küsimata) loodud kettajaod. Seetõttu tasub olla ettevaatlik ja näiteks virtuaalarvutis esmalt järgi proovida kus ei ole riski andmete kogemata kustutamiseks.

<b>Käivitame *parted*</b>

<pre>$ sudo parted</pre>

Sisenenud *parted* tööriista, võib sisestada käske seadme kettajagude loomiseks. Abiinfot saab tippides *help* ja vajutades *Enter*.

<b>Seadme valimine</b>

<pre>select /dev/sdb2</pre>

Seadmega töötamiseks, tuleb see valida nime järgi.
Kui käivitada *parted* kohe koos seadmevalikuga siis ei pea eraldi seadet valima:
<pre>sudo parted /dev/sdb2</pre>

<b>Jooksva kettajagude tabeli kuvamine</b><br>
Võib kirjutada välja *print* või kasutada lühikäsku *p*
<pre>
(parted) print                                                            
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

Kuvatakse seadme saadavalolevad kettajaod. <b>*start*</b> ja <b>*end*</b> punktid tuvastavad, kus kettajagu asub. Neid tuleb täpselt valida. *end* tähistab kettajao lõppu ketta algusest, mitte *start* väärtusest nagu võiks arvata.

<b>Kettajagude loomine</b>
Esmalt tuleks valida ühikud, mida *start* ja *end* puhul (ja ka teiste käskude puhul) kasutada (saab igal ajal muuta), näiteks:
<pre>unit GiB</pre>
Võimalus on kasutada nii [detsimaal- kui binaarühikuid](https://en.wikipedia.org/wiki/Binary_prefix) (lisainfo *parted'i* sees: *help unit*). Teine võimalus on soovitud ühikud kohe *start* ja *end* väärtuste järel iga kord välja kirjutada.

<pre>mkpart primary 123 4567</pre>

Nüüd tuleb valida *start* ja *end* ning luua kettajagu. Tuleb ka täpsustada, millist tüüp kettajagu luuakse, vastavalt kasutatavale kettajagude tabelile (tavaliselt MBR või GPT).<br>
*start* ja *end* on asukohad kettal, nt 4GB või 10%. Negatiivsed väärtused tähendavad arvestamist ketta lõpust alates alguse poole. Kusjuures *end* tähistab kettajao lõppu ketta algusest, mitte *start* väärtusest nagu võiks arvata. Näiteks -1s tähistab täpselt viimast sektorit. *mkpart* tekitab kettajao ilma failisüsteemita. Lisainfo *help mkpart*.

<b>Kettajao suuruse muutmine</b>

Kui ruumist jääb puudu võib kettajagude suurusi ka muuta. Seda ei võimalda mitte iga kettajagude loomise programm kuid *parted* võimaldab.

<pre>resize 2 1245 3456</pre>

Tuleb valida kettajao number ja soovitavad *start* ja *end* punktid.

*Parted* on väga võimas tööriist ning kettajagude loomisel tasuks olla ettevaatlik. Erinevalt teistest kettajagude loomise programmidest salvestab *parted* **koheselt** (automaatselt, küsimata) loodud kettajaod. Seetõttu tasub olla ettevaatlik ja näiteks virtuaalarvutis esmalt järgi proovida kus ei ole riski andmete kogemata kustutamiseks.

*Parted* programmi on võimalik kasutada ka ilma sinna sisenemata, sisestades käsud järjest.

Lisainfo<br>
* https://www.gnu.org/software/parted/manual/
* https://wiki.archlinux.org/index.php/GNU_Parted

## Harjutus

Luua USB kettale kettajaod nõnda, et pool kettast oleks ext4 ja teine pool vaba.

## Küsimus

Millise käsuga luuakse *parted* programmis uus kettajagu?

## Vastus

*mkpart*
