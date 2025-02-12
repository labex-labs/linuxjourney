# Failisüsteemi tüübid

## Tunni sisu

Saadaval on suur hulk erinevaid failisüsteeme. Mõned on kiiremad kui teised, mõned toetavad suuremaid salvestusmahte, teised töötavad ainult väiksematega. Erinevad failisüsteemid korrastavad andmeid erinevalt, sellel kursusel tutvustatakse erinevaid tüüpe detailselt. Kuna erinevaid teostusi on saadaval palju, peavad rakendused erinevate toimingutega kohanduma. On olemas selline asi, nagu virtuaalse failisüsteemi (VFS) eralduskiht. See on kiht rakenduste ja erinevate failisüsteemi tüüpide vahel ja ei ole vahet millist failisüsteemi kasutada, rakendused tulevad ikka toime.

Tulevates peatükkides räägime kettajagudest, mis võimaldavad ühel kettal rakendada mitmeid erinevaid failisüsteeme.

<b>Päevikuga failisüsteem</b>

Päeviku olemasolu on enamus failisüsteemide tüüpides olemas ja isegi kui ei ole siis peaks teadma, mis selle funktsioonid on. Ütleme, et käsil on suuremahulise faili kopeerimine kui äkki kaob vool. Kui kasutada päevikuta failisüsteemi, oleks kopeeritav fail vigane ja failisüsteemis puuduks järjepidevus. Kui arvuti uuesti käivitada kontrollitakse failisüsteemi, et kõik oleks korras. Parandustööd võivad aga üsna palju aega võtta, sõltuvalt failisüsteemi suurusest muidugi.

Kui aga kasutada päevikuga failisüsteemi, kirjutatakse veel enne kui üldse midagi kopeerima hakatakse, alustatav tegevus logifaili (päevikusse). Kui kopeerimine valmis saab, tehakse ka päevikusse vastav märge. Tänu sellisele mehhanismile on andmed failisüsteemis kogu aeg kooskõlas ning süsteem teab täpselt, kus kasutajal töö pooleli jäi kui vool peaks ootamatult kaduma. Ka käivitumise aeg on lühem kuna selle asemel, et kontrollida kogu süsteemi, kontrollitakse vaid päevikut.

<b>Tavalisemad lauaarvuti failisüsteemide tüübid</b>
 
<ul>
<li>ext4 - Linuxile omaste failisüsteemide käesolev versioon, mis on ühilduv oma eelkäijate ext2 ja ext3 versioonidega. See toetab kettamahtusid kuni 1 eksabait ja failisuurusi kuni 16 terabaiti jpm. </li>
<li>Btrfs - "Better või Butter FS" on Linuxis uus failisüsteem, millega tulevad kaasa hetktõmmised, varundamine, paranenud jõudlus jpm. See on laialdaselt kättesaadav kuid mitte veel lõpuni stabiilne või ühilduv. </li>
<li>XFS - Kõrge jõudlusega päevikuga failisüsteem. Hea suurte failidega süsteemidele, näiteks meediaserverid.</li>
<li>NTFS ja FAT - MS Windows'i failisüsteemid</li>
<li>HFS+ - Macintosh'i failisüsteem</li>
</ul> 

Nii saab uurida arvutis kasutatavaid failisüsteeme:

<pre>
pete@icebox:~$ df -T
Filesystem     Type     1K-blocks    Used Available Use% Mounted on
/dev/sda1      ext4       6461592 2402708   3707604  40% /
udev           devtmpfs    501356       4    501352   1% /dev
tmpfs          tmpfs       102544    1068    101476   2% /run
/dev/sda6      xfs       13752320  460112  13292208   4% /home
</pre>

<b>df</b> käsk kuvab muuhulgas informatsiooni ketaste mahtude kasutamise kohta. Sellest tööriistast räägitakse hiljem veel.

## Harjutus

Uurida Internetist ka teiste failisüsteemide kohta: ReiserFS, ZFS, JFS ja muud, mida võib leida.

## Küsimus

Milline on tavaline Linuxi failisüsteemi tüüp?

## Vastus

*ext4*
