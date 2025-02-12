# Failisüsteemi parandamine

## Tunni sisu

Vahel juhtub, et failisüsteem ei ole parimas korras, näiteks juhul kui arvutit ei suleta korralikult või mõni fail on vigane. Arvuti süsteemi ülesanne on see meie jaoks korda teha.

<b>fsck</b> (*filesystem check*) käsuga kontrollitakse failisüsteemi stabiilsust ning vahel ka parandatakse seda. Tavaliselt käivitub see käsk kontrollimiseks arvuti käivitamisel enne kui ketas külge ühendatakse. Kui aga juhtub, et ketas on tõeliselt halvas olukorras siis tuleb seda ise käsitsi parandama hakata. Kuid seda tasuks teha olukorras ja vahenditega mis võimaldavad failisüsteemile ligipääsu ilma ketast haakimata. Failisüsteemi kontrollitakse, parandatakse vaid haakimata kettajao puhul.

<pre>$ sudo fsck /dev/sda</pre>

## Harjutus

Tutvuda *man fsck* lehelt ka teiste kasutusvõimalustega.

## Küsimus

Millise käsuga saab kontrollida failisüsteemi terviklikkust?

## Vastus

*fsck*
