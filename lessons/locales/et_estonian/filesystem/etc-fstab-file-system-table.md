# /etc/fstab

## Tunni sisu

Kui tahame alglaadimisel automaatselt failisüsteemi külgehaakida, tuleb see lisada faili nimega */etc/fstab* (hääldatakse "eff ess täb"), mis on lühend "failisüsteemi tabelist". Selles failis hoitakse püsivalt ühendatud failisüsteeme.

<pre>
pete@icebox:~$ cat /etc/fstab
UUID=130b882f-7d79-436d-a096-1e594c92bb76 /               ext4    relatime,errors=remount-ro 0       1
UUID=78d203a0-7c18-49bd-9e07-54f44cdb5726 /home           xfs     relatime        0       2
UUID=22c3d34b-467e-467c-b44d-f03803c2c526 none            swap    sw              0       0
</pre>

Iga rida esindab ühte failisüsteemi. Väljad on järgmised:

<ul>
<li><i>UUID</i> - seadme unikaalne tunnus (ID) ehk siis milline kettajagu ühendatakse</li>
<li>Haakepunkt - kataloog, kuhu seade on ühendatud</li>
<li>Failisüsteemi tüüp</li>
<li>Valikud - ühendumise parameetrid, vaata lisainfo jaoks man fstab lehekülge</li>
<li><i>Dump</i> - <i>dump</i> haldusvahend kasutab seda, et otsustada millal on vaja luua varukoopiat, see võiks olla vaikimisi 0</li>
<li><i>Pass</i> - <i>fsck</i> kasutab seda, et otsustada, mis järjekorras failisüsteeme kontrollima peab. Kui väärtus on null siis failisüsteemi ei kontrollita</li>
</ul>

Kirje lisamiseks tuleb lihtsalt muuta */etc/fstab* faili sisu kasutades ülaltoodud korrektset süntaksit. Selle faili muutmisega tasub olla ettevaatlik, selle rikkumisega on võimalik muuta oma elu natuke raskemaks.

Võimalike vigade vältimiseks tasub käsuga *sudo mount -a* abil */etc/fstab* faili lisatud kuid veel haakimata kettajaod külge haakida. Kui need juba olid haagitud siis eelnevalt lahti haakida (*sudo umount /dev/sdb2* vms). Kui vigu ei olnud siis haagiti lisatud kettajaod külge. Vastasel korral teavitatakse vigadest ja need on võimalik enne arvuti taaskäivitamist, sulgemist ära parandada. Käsuga *mount* või siis *mount | column -t*, lisaks *findmnt* abil näeb külgehaagitud kettaid. Võib *grep* abil filtreerida: *mount | grep sdb*, *mount | column -t | grep sdb* vms.

## Harjutus

Lisada kõnealune USB pulk */etc/fstab*'i. Kui arvuti taaskäivitada peaks see olema endiselt ühendatud.

## Küsimus

Millises failis hoitakse failisüsteemide ühendumise infot?

## Vastus

*/etc/fstab*
