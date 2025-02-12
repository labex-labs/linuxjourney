# Systemd ülevaade

## Tunni sisu

*Systemd* on tasapisi kerkimas esile *init*'i standardina. Kui kasutajal on arvutis olemas kataloog */usr/lib/systemd* siis kasutatakse kõige tõenäolisemalt just *systemd*'d.

<b>init'i kindlakstegemise võimalusi:</b>
* <i>sudo stat /proc/1/exe</i>
<pre>
  Fail: '/proc/1/exe' -> '/lib/<b>systemd</b>/systemd'
  Suurus: 0             Blokke: 0          IO Blokke: 1024   nimeviide
Seade: 4h/4d    Inode: 17905       Linke: 1
Juurdepääs: (0777/lrwxrwxrwx)  Uid: (    0/    root)   Gid: (    0/    root)
Kasutamine: 2016-12-26 15:18:07.536484054 +0200
Modifitseerimine: 2016-12-22 15:13:05.902106278 +0200
Muutmine: 2016-12-22 15:13:05.902106278 +0200
 Sünd: -
</pre>
* <i>sudo stat /sbin/init</i>
<pre>
  Fail: '/sbin/init' -> '/lib/<b>systemd</b>/systemd'
  Suurus: 20            Blokke: 0          IO Blokke: 4096   nimeviide
Seade: 805h/2053d       Inode: 2097404     Linke: 1
Juurdepääs: (0777/lrwxrwxrwx)  Uid: (    0/    root)   Gid: (    0/    root)
Kasutamine: 2016-12-15 15:13:56.000000000 +0200
Modifitseerimine: 2016-11-25 14:57:20.000000000 +0200
Muutmine: 2016-12-15 15:13:56.984403977 +0200
 Sünd: -
</pre>
* <i>dpkg -S /sbin/init</i>
<pre><b>systemd</b>-sysv: /sbin/init</pre>
* <i>ps -p1</i>
<pre>
  PID TTY          TIME CMD
    1 ?        00:00:10 <b>systemd</b>
</pre>

*Systemd* kasutab süsteemi töökorras hoidmiseks eesmärke. Põhimõtteliselt on nii, et on olemas eesmärk, mida tahetakse saavutada aga sellel eesmärgil on ka sõltuvused, mis tuleb samuti täita. *Systemd* on väga paindlik ja robustne, see ei järgi protsesside käivitamisel ranget järjekorda. Tüüpilise *systemd* alglaadimise ajal toimub tavaliselt järgnev:

<ol>
<li>Esiteks laeb <i>systemd</i> konfiguratsioonifailid, mis asuvad tüüpiliselt kataloogis <i>/etc/systemd/system/</i> või <i>/usr/lib/systemd/system</i></li>
<li>Seejärel tehakse kindlaks alglaadimise sihtpunkt, mis on tavaliselt <i>default.target</i></li>
<li>Süsteem selgitab välja sõltuvused ja aktiveerib need</li>
</ol>

Sarnaselt *Sys V* töötasemetele, võib *systemd* alglaadida erineva sihiga:

<ul>
<li><i>poweroff.target</i> - lülita süsteem välja</li>
<li><i>rescue.target</i> - üksiku kasutaja režiim</li>
<li><i>multi-user.target</i> - mitu kasutajat ja võrk</li>
<li><i>graphical.target</i> - mitu kasutajat, võrk ja graafiline kasutajaliides</li>
<li><i>reboot.target</i> - taaskäivitus</li>
</ul>

Vaikimisi osutab default.target sihile graphical.target.

Peamised objektid, millega *systemd* opereerib on üksused. *Systemd* mitte ainult ei peata ja käivita protsesse vaid võib ka haakida külge failisüsteeme, jälgida võrgusokleid ja muud. Sellise robustsuse pärast opereeritaksegi erinevate üksustega. Kõige tavalisemad üksused on:

<ul>
<li>Teenuse üksused  - teenused, mida käivitatakse ja peatatakse, need failid lõpevad <i>.service</i></li>
<li>Haakeüksused  - failisüsteemide haakimiseks, lõppevad <i>.mount</i> </li>
<li>Sihtmärgi üksused  - grupeerivad kokku teisi üksusi, faili lõpp on <i>.target</i></li>
</ul>

Ütleme näiteks, et me alglaadime default.target. Sinna on kokku grupeeritud *networking.service*, *crond.service* ja teised üksused. Seega kui see üksus aktiveerida aktiveeruvad ka kõik talle alluvad üksused.

## Harjutus

Selles peatükis harjutust pole.

## Küsimus

Millist üksust kasutatakse, et grupeerida kokku teised üksused?

## Vastus

sihtmärgi
