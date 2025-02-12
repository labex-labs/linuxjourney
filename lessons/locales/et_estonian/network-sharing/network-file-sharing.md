# Ülevaade failide jagamisest

## Tunni sisu

Tavaliselt ei ole kasutaja oma arvutiga võrgus üksi ja seda kindlasti mitte siis kui teha tööd ärikeskkonnas. Failide kandmiseks ühest arvutist teise võib mõnikord olla lihtsam kasutada USB pulka ja kopeerida failid käsitsi. Kuid samas võrgus töötades üldjuhul jagatakse faile läbi võrgu. See toimib klient-server põhimõttel ehk siis võrgus peab olema vastavat teenust pakkuv ja tarkvara sisaldav serverarvuti, mille külge saavad ühenduda sama tarkvara toetavad klientarvutid.

Sellel kursusel tutvustatakse mõnda  andmete kopeerimise meetodit, mida saab rakendada samas võrgus paiknevate arvutite peal. Arutlusele tulevad mõned lihtsamad failide kopeerimise meetodid, seejärel aga kuidas haakida terveid katalooge, et nad käituksid kui eraldiseisvad kettad.

<b>Secure Copy</b><br>
Üks lihtne failide jagamise tööriist on  <b>scp</b> käsk. Inglise keelest tõlgituna tähendab see käsk turvalist kopeerimist (*secure copy*). See töötab just nagu cp käsk, kuid võimaldab kopeerida erinevate lõppkasutajate vahel. Kuna see töötab läbi SSH, kasutavad kõik tegevused sama isikutuvastust ja turvalisust kui SSH. Linuxis on kasutusel avatud lähtekoodiga OpenSSH server.

<b>OpenSSH serveri paigaldamine</b><br>
Serverarvutis peab olema paigaldatud OpenSSH server, teiste arvutitega ühendumiseks ka klienditarkvara ja soovitav on paigaldada ka musta nimekirja (*blacklist*) kantud krüptovõtmete paketid:

<pre>
sudo apt update && sudo apt-get -y install ssh openssh-blacklist* && sudo ldconfig && sudo dpkg --configure -a && sudo apt-get clean
</pre>

Siin paigaldatakse metapakett *ssh*, mis Debiani/Ubuntu-põhistes distrotes sisaldab nii serveri- kui klienditarkvara. Soovi korral saab ka eraldi vaid serveri, paigaldades paketi *openssh-server*.

Soovi korral eraldi klienditarkvara paigaldamiseks on olemas eraldi pakett kuid tavaliselt ei ole paigaldatud musta nimekirja (*blacklist*) kantud krüptovõtmete pakette:

<pre>
sudo apt update && sudo apt-get -y install openssh-client openssh-blacklist* && sudo ldconfig && sudo dpkg --configure -a && sudo apt-get clean
</pre>

Seadistamiseks leiab failid kataloogist */etc/ssh/*, serveri seaded asuvad failis */etc/ssh/sshd_config* ning süsteemilaiune klienditarkvara seadistus */etc/ssh/ssh_config* ning iga kasutaja võib veel omada eraldi *~/.ssh/config* faili, mis on kõrgema prioriteediga kui süsteemilaiune seadistusefail.

<b>Esmakordne sisselogimine OpenSSH serverarvutisse</b><br>
Esmakordsel sisselogimisel kirjutatakse klientarvutisse faili *~/.ssh/known_hosts* serverarvuti avalik võti, mida kontrollitakse edaspidi igal sisenemisel. Kui serverarvuti võtmepaar (salajane ja koos sellega ka avalik võti) muutub siis kuvatakse vastav teade:<br>
<pre>
The authenticity of host '12.34.56.78 (12.34.56.78)' can't be established.
RSA key fingerprint is b1:2d:33:67:ce:35:4d:5f:f3:a8:cd:c0:c4:48:86:12.
Are you sure you want to continue connecting (yes/no)? yes
Warning: Permanently added '12.34.56.78' (RSA) to the list of known hosts.
user@12.34.56.78's password: 
Now try logging into the machine, with "ssh 'user@12.34.56.78'", and check in:

  ~/.ssh/authorized_keys

to make sure we haven't added extra keys that you weren't expecting.
</pre>

Võtmete haldusest on juttu allpool.

<b>Selleks, et kopeerida fail kohalikust (klient)arvutist eemalasuvasse (server)arvutisse</b><br>
<pre>$ scp minufail.txt kasutajanimi@kaugarvuti.com:/eemalasuv/kataloog/</pre>

<b>Selleks, et kopeerida fail eemalasuvast (server)arvutist enda omasse</b><br>
<pre>$ scp kasutajanimi@kaugarvuti.com:/eemalasuv/kataloog/minufail.txt /kohalik/kataloog/</pre>

<b>Selleks, et kopeerida kataloog enda arvutist eemalasuvasse arvutisse</b><br>
<pre>$ scp -r /kohalik/kataloog/ kasutajanimi@kaugarvuti.com:/eemalasuv/kataloog/</pre>

<b>Mugav sisselogimine OpenSSH serverarvutisse</b><br>
Mugavaks sisselogimiseks võib tekitada võtmefaili - siis ei pea iga kord salasõna sisestama. Siiski esimesel korral sisestatakse salasõna kuid kogu seansi vältel (kuni väljalogimiseni) ei ole vaja uuesti sisestada. Võimalik on ka erinevate agentide abil salasõna meeldejätmist sessiooni jooksul hallata. Sellest täpsemalt näiteks [Arch wiki artiklis vastavas peatükis](https://wiki.archlinux.org/index.php/SSH_keys#SSH_agents).

<b>Võtmepaari (salajane ja avalik võti) loomiseks:</b><br>
<pre>
ssh-keygen -t rsa -b 4096 -C "Eesnimi Perenimi e-posti@aadress.ee"
</pre>

Selle tulemusena luuakse hetkel sisseloginud kasutaja kodukataloogi kaks faili (võtmepaar):
* <i>~/.ssh/id_rsa</i> - see on salajane võti (ei tohi kellelegi anda)
* <i>~/.ssh/id_rsa.pub</i> - see on avalik võti (võib avalikult kõigiga jagada)

Võti *-t* määrab krüptoalgoritmiks RSA ja *-b* selle tugevuseks 4096 bitti. Tulevikus võib olla vajalik seda tugevust veelgi suurendada. Kommentaar võtmega *-C* võib sisaldada vajalikku infot jutumärkide vahel - see lisatakse avaliku võtmefaili lõppu ja nii on serverarvuti haldajal lihtsam kindlaks teha kellele antud avalik võti kuulub - seda eriti olukorras kui serverarvutisse on mitmeid võtmefailiga sisselogijaid.

<b>Võtme salasõna muutmine</b><br>
Võtmepaari loomisel on soovitav ka salasõna määrata - oluline on just selle pikkus ja mitte niivõrd keerukus. Salasõna saab hiljem muuta (nurksulud tähendavad siin mittekohustuslikku osa kuid neid ei kirjutata):<br>
<pre>
ssh-keygen -p [-P vana salasõna] [-N uus salasõna] [-f võtmefail]
</pre>

<b>Mitme serveri tugi võtmefailiga sisselogimiseks</b><br>
Kui servereid on mitu siis on võimalik *-f* võtme abil luua igale serverile eraldi, siin näites tähistab *s1* esimest serverarvutit - mõistlik on valida selline nimi (ilma täpitähtede- ja tühikuteta), mis kõige paremini meelde jääb ja serverarvutit iseloomustab:<br>
<pre>
ssh-keygen -t rsa -b 4096 -C "Eesnimi Perenimi e-posti@aadress.ee" -f ~/.ssh/id_rsa_s1
</pre>

*ssh-keygen* võimaldab Linuxis luua RSA puhul kuni 16384-bit võtmeid kuid tulevikus võib see number ka muutuda. Väike paranoia on turvalisuse valdkonnas alati kasulik ja kui tegemist kriitiliste andmetega siis on kõrgendatud turvalisuse kasutamine omal kohal. Seoses kvantarvutite tulekuga muutub ka olukord krüptograafias ja täna turvalisena toimivad algoritmid murtakse üha kiiremini vastavalt kvantarvutite arenguga. Seni tuntud krüptograafia asemele peab tulema kvantkrüptograafia, mis tagab turvalisuse ka uuenenud olukorras.

<b>Uue põlvkonna turvalisus võtmefailiga sisselogimisel</b><br>
Lisaks on olemas ka teisi algoritme, mida võimalik võtmepaari loomisel kasutada (vt *man ssh-keygen* ja uurida *-t* võimalusi) ja viimasel ajal on soovitav kasutada elliptilist krüptograafiat võimaldavat algoritmi Ed25519. Lisainfot leiab näiteks [Arch Linuxi wiki artiklist](https://wiki.archlinux.org/index.php/SSH_keys#Choosing_the_type_of_encryption) ja [Ed25519 kodulehelt](http://ed25519.cr.yp.to).

<b>OpenSSH seadistuste kataloogi turvalisus</b><br>
Kindlasti peavad olema tagatud vajalikud õigused: *~/.ssh/* kataloogi ning selle sisu saab ainult omanik vaadata-muuta, grupil ja teistel kasutajatel ei tohi mingeid õigusi olla:<br>
<pre>
chmod 700 ~/.ssh/ && chmod 600 ~/.ssh/*
</pre>

Kui õigused on paigast ära siis võib ka näha hoiatust:<br>
<pre>
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@ WARNING: UNPROTECTED PRIVATE KEY FILE! @
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
Permissions 0664 for '/home/user/.ssh/id_rsa' are too open.
It is recommended that your private key files are NOT accessible by others.
This private key will be ignored.
bad permissions: ignore key: /home/user/.ssh/id_rsa
</pre>

<b>Avaliku võtme kopeerimine klientarvutist serverarvutisse</b><br>
Avaliku võtme (*~/.ssh/id_rsa.pub*) kopeerimiseks kliendiarvutist serverarvutisse:<br>
<pre>
ssh-copy-id kasutaja@server
</pre>

... kus "kasutaja" asemele kirjutada serverarvuti kasutajanimi ja "server" asemele serverarvuti IP-aadress või internetiaadress.

Võtmefaili kopeerimiseks kliendiarvutist serverarvutisse kui võtmefail on teise nimega:<br>
<pre>
ssh-copy-id -i ~/.ssh/id_rsa_s1.pub kasutaja@server
</pre>

Käsk *ssh-copy-id* kopeerib avaliku võtme serverarvutis sisselogimisel kasutatud kasutaja kodukataloogis asuvasse faili *~/.ssh/authorized_keys* - kui seda faili eelnevalt ei olnud siis see luuakse automaatselt. Oluline on regulaarselt jälgida, et kataloogil ~/.ssh/ ja selle sees olevatel failidel oleksid eespool kirjeldatud õigused - need kipuvad aja jooksul erinevate tegevuste käigus muutuma. **Võiks öelda, et iga kord kui võtmepaar luuakse ja üle võrgu kopeeritakse siis tuleks nii server- kui klientarvutis viimase käsuna käivitada:**<br>
<pre>
chmod 700 ~/.ssh/ && chmod 600 ~/.ssh/*
</pre>

<b>Mitme võtme haldamine</b><br>
Mitme võtme haldamiseks on võimalik kasutaja kodukataloogi luua vastav seadistustefail *~/.ssh/config*:<br>
<pre>
Host SERVER1
   IdentitiesOnly yes
   IdentityFile ~/.ssh/id_rsa_SERVER1.pub

Host SERVER2
   IdentitiesOnly yes
   IdentityFile ~/.ssh/id_ed25519_SERVER2.pub
</pre>

Selliselt on võimalik seadistusefaili *~/.ssh/config* abil siduda avalik võti vastava serveri aadressiga.

<b>Serverarvuti võtme kordus</b><br>
Kui on probleeme võtmete kordumisega konkreetse serverarvutiga ühendumisel, näiteks tuleb klientarvutis teade:<br>
<pre>
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@    WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED!     @
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
IT IS POSSIBLE THAT SOMEONE IS DOING SOMETHING NASTY!
Someone could be eavesdropping on you right now (man-in-the-middle attack)!
It is also possible that the RSA host key has just been changed.
The fingerprint for the RSA key sent by the remote host is
a8:6a:60:5a:48:64:ac:90:33:b9:f2:7c:be:56:92:81.
Please contact your system administrator.
Add correct host key in /var/root/.ssh/known_hosts to get rid of this message.
Offending key in /root/.ssh/known_hosts:9948
RSA host key for host.example.com has changed and you have requested strict checking.
Host key verification failed.
</pre>

... siis selle saab eemaldada:<br>
<pre>
sed -i ‘9948d’ ~/.ssh/known_hosts
</pre>

... kus "9948" on veateates öeldud reanumber.

Teine võimalus konkreetse serverarvuti võtme eemaldamiseks klientarvuti failist *~/.ssh/known_hosts*:<br>
<pre>
ssh-keygen -R serveriaadress
</pre>

Serverarvutiga seotud võtme otsimine klientarvuti failist *~/.ssh/known_hosts*:<br>
<pre>
ssh-keygen -H -F serveriaadress
</pre>

## Harjutus

Proovida kopeerida faili *scp* abil ühest arvutist teise.

## Küsimus

Millise käsuga saab turvaliselt kopeerida faile ühest arvutist teise?

## Vastus

*scp*
