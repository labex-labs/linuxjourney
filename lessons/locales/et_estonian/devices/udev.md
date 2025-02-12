# udev

## Tunni sisu

Vanadel aegadel aga tegelikult ka veel praegu kui väga tahta, võis seadmesõlmi luua näiteks sellise käsuga:

<pre>$ mknod /dev/sdb1 b 8 3</pre>

See käsk loob blokkseadme(b) seadmesõlme /dev/sdb1, mille juhtprogrammi klass on 8 ja seadme klass 3.

Seadme eemaldamiseks, võis seadmefaili lihtsalt eemaldada <b>rm</b> abil */dev* kataloogist.

Õnneks tänu *udev*'ile ei pea enam asjale selliselt lähenema. *Udev* süsteem loob ja eemaldab seadmefaile dünaamiliselt vastavalt sellele kas nad on ühendatud või mitte. *Udev*'i deemonprogramm ootab tuumalt teateid süsteemi ühendatud seadmete kohta. *Udev* analüüsib saadud infot ja seob andmed */etc/udev/rules.d* kataloogis olevate reeglitega. Sõltuvalt reeglitest luuakse seadmetele kõige tõenäolisemalt seadmesõlm ja nimeviit. *Udev* reegleid võib ka ise kirjutada, kuid see jääb veidike selle kursuse ulatusest välja. Õnneks on süsteemis juba hulgaliselt sisseehitatud reegleid, misõttu ehk ei olegi tarvis neid ise juurde kirjutada.

*Udev* andmebaasi ja *sysfs*'i saab vaadata <b>udevadm</b> käsuga. See on väga kasulik tööriist, kuid võib mõnikord osutuda väga keeruliseks. Lihtne käsk seadmete kohta käiva info kuvamiseks oleks:

<pre>$ udevadm info --query=all --name=/dev/sda</pre>

## Harjutus

Sisesta õpitud *udevadm* käsk ja uuri sisendit.

## Küsimus

Millega saab dünaamiliselt lisada ja eemaldada seadmeid?

## Vastus

*udev*
