# Tarkvarahoidlad

## Tunni sisu


Kuidas saavad internetti üleslaetud paketid ühtäkki kasutajate arvutitesse? Kas peab minema iga paketi leheküljele ja laadima nad alla ja paigaldama? Tegelikult võib seda muidugi ka nii teha kuid on olemas palju parem lahendus, mida nimetatakse paketihoidlateks. Need ongi lihtsalt kesksed hoidlad pakettide jaoks. On olemas palju hoidlaid rikkaliku paketivalikuga ja mis kõige parem - need on kõik ka internetipõhiselt kättesaadavad ja tobedaid paigaldamiskettaid pole üldse tarvis. Küll aga ei oska arvutid ise ilma kasutaja abita neid hoidlaid otsida.

Näiteks kasutaja soovib oma arvutisse paigaldada *WackyWidgets* tarkvara. *WackyWidgets* haldab ise enda pakettide hoidlaid. Hoidlates on 10 paketti: *CoolWidget, SuperWidget* jne. *WackyWidget* hoiab oma hoidlat aadressil http://download.widgets/linux/deb/.

Selle asemel, et minna veebilehele pakette allalaadima, võib öelda arvutile kust tarkvara leida. Seejuures on see oluliselt turvalisem kuna paketihaldustarkvara kontrollib paigaldamise käigus ka paigaldatavate tarkvarapakettide usaldusväärsust digiallkirjade (GPG-võtmed) abil. Kui GPG-võti ei klapi siis antakse veateade ja paigaldamine katkestatakse. Siis tuleb uurida, miks digiallkirjad ei klapi. Selline lähenemine väldib muuhulgas ka [APT-tüüpi pahavara](http://www.arvutikaitse.ee/apt-jouliselt-ebamaarane-kuber-oht/) leviku. Mitte segi ajada Debiani paketihaldussüsteemiga APT [*Advanced Package Tool*](https://wiki.debian.org/Apt)<br>
Lisainfot tarkvarapakettide digiallkirjastamise kohta Debian/Ubuntu-põhistes süsteemides leiab:<br>
* https://help.ubuntu.com/community/SecureApt
* https://wiki.debian.org/SecureApt

Linuxil on kaasas eelnevalt heaks kiidetud varamud, kust süsteem saab peamised olulised paketid. Debiani puhul on selleks failiks <b>/etc/apt/sources.list</b>. Arvuti oskab otsida sealt erinevaid allikaid, sealjuures neid, mida kasutajad võivad olla lisanud. Kasutajate poolt lisatavad varamud on oodatud kataloogi */etc/apt/sources.list.d/* ja seda *.list* tüüpi failidena. Kasutajad saavad varamuid lisada käsuga *add-apt-repository* või käsitsi *.list* faili kirjutades ja digiallkirju ehk GPG-võtmeid importides.


## Harjutus

Selles peatükis harjutus ei ole.

## Küsimus

Kus asub Debiani süsteemis paketihalduse lähtefail?

## Vastus

*/etc/apt/sources.list*
