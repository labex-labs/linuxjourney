# Külge- ja lahtiühendamine

## Tunni sisu

Enne kui failisüsteemi sisu vaadata saab, peab selle külgeühendama. Selleks on aga vaja teada seadme otsiteekonda, failisüsteemi tüüpi ja haakepunkti. Haakepunkt on see kataloog, kuhu failisüsteem on ühendatud. Seega, seadmeid ühendatakse haakepunkti.

Esiteks tuleb luua haakepunkt, meie näite puhul <b>mkdir /minupulk</b>.

<pre>$ sudo mount -t ext4 /dev/sdb2 /minupulk</pre>

Täpselt nii lihtne! Kui nüüd minna /minupulk, võib näha failisüsteemi sisu. <b>-t</b> täpsustab failisüsteemi tüübi, seejärel on haagitava seadme asukoht ja lõpuks haakepunkt.

Seadme haakepunktist lahtiühendamiseks:

<pre>$ sudo umount /minupulk 
või 
$ sudo umount /dev/sdb2</pre>

Meenutame, et tuum nimetab seadmeid nende tuvastamise järjekorras. Mis saab siis kui mingil põhjusel seadme nimi muutub pärast selle külgehaakimist? Õnneks võib kasutada ka seadme universaalselt unikaalset ID'd (UUID) nime asemel.

Blokkseadmete UUID'de kuvamiseks:

<pre>
pete@icebox:~$ sudo blkid
/dev/sda1: UUID="130b882f-7d79-436d-a096-1e594c92bb76" TYPE="ext4" 
/dev/sda5: UUID="22c3d34b-467e-467c-b44d-f03803c2c526" TYPE="swap" 
/dev/sda6: UUID="78d203a0-7c18-49bd-9e07-54f44cdb5726" TYPE="xfs" 
</pre>

Kuvatakse seadme nimi, vastav failisüsteemi tüüp ja UUID. Nüüd võib seadme ühendamiseks kasutada:

<pre>$ sudo mount UUID=130b882f-7d79-436d-a096-1e594c92bb76 /minupulk</pre>

Enamjaolt ei ole tarvis kasutada UUID'd, seadme nime on palju mugavam kasutada ja operatsioonisüsteem pigem ikkagi oskab tavalisemaid seadmeid nagu USB pulgad, lahti ühendada. Kui osutub vajalikuks mingit failisüsteemi alglaadimisel automaatselt külge haakida, näiteks teine kõva ketas, on vaja kasutada UUID'd. Sellest räägime järgmises peatükis.

## Harjutus

Vaadata *mount* ja *unmount* käskude *man* lehekülge ning tutvuda nende kasutamise võimalustega.

## Küsimus

Millise käsuga ühendatakse failisüsteem külge?

## Vastus

*mount*
