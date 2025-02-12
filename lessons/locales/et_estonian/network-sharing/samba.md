# Samba

## Tunni sisu

Kuna arvutustehnika algusaegadel oli MS Windows'i masinatel vaja jagada faile UNIX'i masinatega, sündis SMB (*Server Message Block* ehk serveri sõnumi plokk) protokoll. SMB'd kasutati failide jagamiseks MS Windows operatsioonisüsteemis (macOS'il on ka võimalik), hiljem aga puhastati ja optimeeriti seda ja see võttis CIFS (*Common Internet File System* ehk lihtne interneti failisüsteem) protokolli kuju.

Sambaks nimetatakse GNU/Linuxi haldusvahendeid töötamaks GNU/Linuxis CIFS'ga. Lisaks failidele saab jagada ka muid ressursse nagu näiteks printerid.

<b>Sambaga võrgus jagamise üles seadmine</b>

Käime üle peamised sammud, et jagada midagi läbi võrgu MS Windows masinaga:

<b>Samba paigaldamine</b><br>
<pre>$ sudo apt update && sudo apt-get -y install samba && sudo ldconfig && sudo dpkg --configure -a && sudo apt-get clean</pre>

<b>Samba seadistamine</b><br>
Samba sätted asuvad failis /etc/samba/smb.conf. See fail peaks ütlema süsteemile, milliseid katalooge tuleb jagada, nende ligipääsuõigused ja muud seaded. Vaikimisi on smb.conf failis palju väljakommenteeritud koodi, mida võib kasutada näitena, et ise seadeid kirjutada.
 
<pre>$ sudo vim /etc/samba/smb.conf</pre>

<b>Sambale salasõna seadmine</b>

<pre>$ sudo smbpasswd -a [kasutajanimi]</pre>

<b>Jagatud kausta loomine</b>

<pre>$ mkdir /minu/kataloog/mida/jagada</pre>

<b>Samba teenuse taaskäivitamine</b>

<pre>$ sudo service smbd restart</pre>

<b>Jagatud materjalidele ligipääsemine läbi Windowsi</b>

Windowsis tuleb lihtsalt sisestada võrgu ühendus *run* (kiirklahv: *[Super](https://en.wikipedia.org/wiki/Super_key_(keyboard_button))+R*) käsuviibale: *\\HOST\jagamisenimi*

<b>Samba/MS Windowsi jagatud materjalidele ligipääsemine läbi GNU/Linuxi</b>

<pre>$ smbclient //HOST/kataloog -U kasutaja</pre>

Linuxi graafilistes failihaldurites:<br>
<pre>smb://kasutaja@server/</pre>

Samba paketis on olemas ka tööriist nimega <b>smbclient</b>, mida saab kasutada igasuguste MS Windowsi või Samba jagatud materjalidele ligipääsemiseks. Kui ühendus on saavutatud saab ringi liikuda ja faile üle kanda.

<b>Kinnita Samba kataloog enda süsteemi</b>

Selle asemel, et faile üks haaval üle kanda, võib jagatud kataloogi lihtsalt enda süsteemi haakida.

<pre>$ sudo mount -t cifs serverinimi:kataloog haakepunkt -o kasutaja=kasutajanimi,pass=salasõna</pre>

## Harjutus

Seada üles jagamine Sambaga, kui seda veel pole. Avada *smb.conf* ja saada tuttavaks võimalike valikutega sätete failis.

## Küsimus

Milline on uusim protokoll failide ülekandmiseks MS Windowsi ja GNU/Linuxi vahel?

## Vastus

CIFS
