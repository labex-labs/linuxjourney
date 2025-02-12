# Pakettide analüüsimine

## Tunni sisu

Pakettide analüüsimisest võiks teha täiesti omaette kursuse ning ainult sellel teemal on kirjutatud terveid raamatuid. Siinkohal tutvume seega ainult baasteadmistega. Pakettide analüüsimiseks on kaks populaarset programmi: Wireshark ja tcpdump. Need tööriistad jälgivad võrguliideseid ja jäädvustavad pakettide liikumise, sõeluvad nende sisu ja edastavad saadud informatsiooni kasutajale kuvamiseks.  Selliste tööriistadega saab jõuda asja päris ivani. Kursuse näites kasutatakse tcpdumpi, kuna selle kasutajaliides on lihtsam. Kui aga peaks soovitama, millist programmi igapäevaseks kasutamiseks valida, soovitaksin kindlasti Wireshark'i.

<b>tcpdump'i paigaldamine</b>

<pre>
$ sudo apt update && sudo apt-get -y install tcpdump && sudo ldconfig && sudo dpkg --configure -a && sudo apt-get clean
</pre>

<b>Paketi andmete püüdmine võrguliidesel</b>

<pre>
pete@icebox:~$ sudo tcpdump -i wlan0
tcpdump: verbose output suppressed, use -v or -vv for full protocol decode
listening on wlan0, link-type EN10MB (Ethernet), capture size 65535 bytes
11:28:23.958840 IP icebox.lan > nuq04s29-in-f4.1e100.net: ICMP echo request, id 1901, seq 2, length 64
11:28:23.970928 IP nuq04s29-in-f4.1e100.net > icebox.lan: ICMP echo reply, id 1901, seq 2, length 64
11:28:24.960464 IP icebox.lan > nuq04s29-in-f4.1e100.net: ICMP echo request, id 1901, seq 3, length 64
11:28:24.979299 IP nuq04s29-in-f4.1e100.net > icebox.lan: ICMP echo reply, id 1901, seq 3, length 64
11:28:25.961869 IP icebox.lan > nuq04s29-in-f4.1e100.net: ICMP echo request, id 1901, seq 4, length 64
11:28:25.976176 IP nuq04s29-in-f4.1e100.net > icebox.lan: ICMP echo reply, id 1901, seq 4, length 64
11:28:26.963667 IP icebox.lan > nuq04s29-in-f4.1e100.net: ICMP echo request, id 1901, seq 5, length 64
11:28:26.976137 IP nuq04s29-in-f4.1e100.net > icebox.lan: ICMP echo reply, id 1901, seq 5, length 64
11:28:30.674953 ARP, Request who-has 172.254.1.0 tell ThePickleParty.lan, length 28
11:28:31.190665 IP ThePickleParty.lan.51056 > 192.168.86.255.rfe: UDP, length 306
</pre>

Kui pakettide püüdmine käivitada siis võib märgata, et toimub väga palju asju. See on ootuspärane kuna taustal toimub pidevalt üsna palju võrguliiklust. Näites on toodud väike väljavõte, täpsemalt sellest hetkest kui teostati ping veebilehele www.google.com

<b>Väljundi tõlgendamine</b>

<pre>
11:28:23.958840 IP icebox.lan > nuq04s29-in-f4.1e100.net: ICMP echo request, id 1901, seq 2, length 64
11:28:23.970928 IP nuq04s29-in-f4.1e100.net > icebox.lan: ICMP echo reply, id 1901, seq 2, length 64
</pre>

<ul>
<li>Esimene väli on võrgu sündmuse ajatempel.</li>
<li>IP on protokolli informatsioon.</li>
<li>Järgnevad saaja ja saatja aadressid: <i>icebox.lan > nuq04s29-in-f4.1e100.net</i></li>
<li><i>seq</i> on TCP paketi esimene ja viimane järjekorra number.</li>
<li>Pikkus baitides.</li>

Nagu tcpdump'i väljundist näha võib, saadetakse www.google.com aadressile ICMP kajapäring ning saadakse ka vastus.  Märgime ära, et erinevat paketid annavad erineva informatsiooniga väljundi. *man tcpdump* leheküljelt saab teada, millised need on.

<b>tcpdump'i väljundi suunamine faili</b>

<pre>
$ sudo tcpdump -w /mingi/fail
</pre>

Mõned mõtted lõpetuseks: Pakettide analüüsi teema sai siinkohal küll ainult väga kergelt puudutatud. Nii palju asju saab uurida ja me isegi ei maininud heksa- või ASCII väljundeid. Internetist on võimalik leida hulgaliselt materjale pakettide analüüsi vahendite kohta ja siinkohal ärgitame kasutajat neid leidma ja neist õppima.

## Harjutus

Laadida alla ja paigaldada *Wireshark* ning mängida natuke võrguliidesega.

## Küsimus

Kasutades *tcpdump*'i, millise võtme kasutamisel saab püüda võrguliiklust konkreetselt liideselt?

## Vastus

*-i*
