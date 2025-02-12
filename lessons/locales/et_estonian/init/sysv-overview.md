# System V ülevaade

## Tunni sisu

*Init*'i peamine ülesanne on käivitada ja peatada süsteemile esmatähtsaid protsesse. Linuxis on *init*'il kolm peamist teostust: *System V*, *Upstart* ja *systemd*. Selles peatükis räägime kõige tradistioonilisemast, *System V init* või siis *Sys V* (öeldakse *System Five*).

Kõige lihtsam viis tuvastada, kas kasutatakse *Sys V*'d on kontrollida kas eskisteerib fail */etc/inittab*. Kui selline fail on olemas siis väga tõenäoliselt just see ongi kasutusel. 

<b>init'i kindlakstegemise võimalusi:</b>
* <i>sudo stat /proc/1/exe</i>
* <i>sudo stat /sbin/init</i>
* <i>dpkg -S /sbin/init</i>
* <i>ps -p1</i>

*Sys V* käivitab ja peatab protsesse järjekorras, näiteks, kui kui on soov käivitada protsess foo-b, peab enne kindlustama, et foo-a töötab. Seda tehakse skriptidega, mis käivitavad ja peatavad kasutaja jaoks protsesse. Neid võib ka ise krjutada kuid suuremal määral kasutatakse siiski opreatsioonisüsteemi sisseehitatud skripte, mida kasutatakse esmatähtsate teenuste laadimiseks.

Selle teostuse kasutamise eelisteks on suhteliselt lihtne sõltuvuste lahendamine, kuna foo-a tuleb alati enne foo-b'd. Kannatab aga töökiirus, kuna ainult üks asi käivitub või peatub korraga.

Kasutades *Sys V*'d, määravad masina oleku teenusetasemed, mis võivad olla 0 kuni 6. Erinevad režiimid võivad varieeruda sõltuvalt tarkvaraväljalaskest, kuid enamasti peaksid need välja nägema järmiselt:

<ul>
<li>0: Sulgemine</li>
<li>1: Üksiku kasutaja režiim</li>
<li>2: Mitme kasutaja režiim ilma võrgunduseta</li>
<li>3: Mitme kasutaja režiim koos võrgundusega</li>
<li>4: Kasutamata</li>
<li>5: Mitmekasutaja režiim koos võrgunduse ja graafilise kasutajaliidesega</li>
<li>6: Taaskäivitamine</li>
</ul>

Kui süsteem käivitub siis vaadatakse, milline on aktiivne teenusetase ja käivitatakse skriptid selle taseme seadete alt. Need skriptid paikenevad kataloogis <b>/etc/rc.d/rc[taseme number].d/</b> või <b>/etc/init.d</b>. Skriptid, mis algavad S(start) või K(*kill*) käivituvad vastavalt alglaadimisel ja väljalülitamisel. Numbrid nende tähtede juures esindavad käivitumise järjekorda.

Näiteks:

<pre>
pete@icebox:/etc/rc.d/rc0.d$ ls
K10updates  K80openvpn        
</pre>

Pöördudes 0 teenustasemele või siis sulgemise režiimi, märkame, et arvuti proovib käivitada skripti, et peatada uuendusteenused ja seejärel *openvpn*. Vaikimisi alglaadimise teenustaseme kuvamiseks võib vaadata faili */etc/inittab*. Samas kohas saab ka väikimisi seadet muuta.

Tasuks täheldada, et *System V*'d vahetatakse vaikselt välja, kuid see ei pruug ka veel lähemat aastate jooksul juhtuda. Teenustasemeid võib kohata ka teiste *init*i teostuste juures. Seda põhiliselt, et toetada neid teenuseid, mida käivitatakse või peatatakse ainult *System V init*'i skriptidega.

## Harjutus

Kasutades *System V*'d muuta ära vaikimisi teenustase. Mida võib täheldada?

## Küsimus

Millist teenustaste kasutatakse tavaliselt süsteemi sulgemiseks?

## Vastus

0
