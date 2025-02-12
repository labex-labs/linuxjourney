# Tuuma paigaldamine

## Tunni sisu

Nüüd kui kogu see igav värk on selja taga, räägime parem tuuma paigaldamisest ja muutmisest. Süsteemi võib paigaldada mitu tuuma. On veel meeles peatükk alglaadimisest? Alglaaduri GRUB menüüst saab valida, millise tuumaga süsteem käivitada. Vaikimisi käivitatakse kõige uuem kui peale tuuma paigaldamist on ka alglaadur uuendatud.<br><br>

Et tuvastada süsteemi tuuma versioon, kasuta käsku:

<pre>$ uname -r
3.19.0-43-generic</pre>

<i>Uname</i> käsk kuvab süsteemi informatsiooni, <i>-r</i> kuvab tuuma väljalaskeversiooni.<br><br>

Linuxi tuuma võib paigaldada mitut moodi. Võib laadida alla lähtepaketi ja kompileerida (seda väga ei soovita teha) kuid soovitav on seda teha kasutades paketihaldusvahendeid ja paigaldades alati uusimast tuuma versioonist sõltuvad metapaketid - need uuenevad automaatselt ehk siis kogu süsteemi uuendades (<i>sudo apt update && sudo apt dist-upgrade && sudo apt clean</i>) uueneb ka tuum koos päistega uusima versiooni peale.<br><br>

<b>NB! Peale tuuma uuendamist tuleb alati ka käivitada alglaaduri uuendamise käsku <i>sudo update-grub</i>, et teavitada uuema tuuma paigaldamisest - siis teab alglaadur GRUB ka uusimat tuuma kasutusele võtta järgmise taaskäivitamise ajal.</b> Kuigi üldjuhul tarkvara täielik uuendamine (<i>dist-upgrade</i>) käivitab ka alglaaduri uuendamise siis praktikas on märgata endiselt vana tuuma versiooni pealt käivitumist - seega ei ole see reegel ja kindluse mõttes tasub alati peale uue versiooni tuuma paigaldamist uuendada ka alglaadur. Isegi kui alglaadurit uuendada korduvalt siis ei mõju see kuidagi halvasti süsteemile.<br><br>

On olemas palju erinevaid tuuma versioone, näiteks LTS (<i>Long Term Support</i> ehk pikaajalise toega) ja on ka muidugi veel uuemaid ning vingemaid, millest tuleb juttu allpool. Versioonide vahel võib olla väga palju erinevusi ja võib juhtuda, et kasutaja tahab proovida erinevaid tuumasid. Üldiselt võib alati ka uusimaid versioone proovida - ka need töötavad ja lisavad üldjuhul uusima riistvara tuge ja parandatud saavad ka turvavead. Eriti just turvalisuse seisukohast lähtuvalt võiks süsteemis kasutada alati uusimat tuuma ja peale uusima paigaldatud tuuma pealt töötamises veendumist eemaldada vanad tuumad.<br><br>

Mõistlik on otsida uusimad LTS-versiooni metapaketid ja paigaldada need - siis süsteemi uuendamise (<i>dist-upgrade</i>) käigus uuendatakse alati uusima versiooni pikaajalise toega (LTS) tuuma peale:
<pre>
$ sudo apt search linux-image-generic-lts
$ sudo apt search linux-headers-generic-lts
</pre>

LTS-versioonid tulevad välja 2 aasta tagant aprillikuu lõpus. Need on rohkem testitud ja sobivad paremini ka missioonikriitilistes kohtades kasutamiseks.<br><br>

Leitud tulemustest tuleks paigaldada viimane ehk siis uusim ja olla nõus ka sõltuvustena uusimate tuuma ja selle päiste versioonide paigaldamisega. Uusima versiooni saab teha kindlaks kasutatava Linuxi koodnime järgi, siin toodud näide on Ubuntu Linuxi kohta ja see peaks kehtima ka teiste Debiani ja Ubuntu baasil tehtud Linuxite kohta. Ei tohi unustada ka eespool kirjeldatud alglaaduri uuendamist uusima tuuma kasutuselevõtmiseks. Ei maksa karta, et tuuma ja päisefailid on mõeldud uuemale Ubuntu LTS-versioonile - need töötavad ka vanemate LTS-versioonidega.<br><br>

Ubuntu koodnimed on toodud siin tabelis:
* https://wiki.ubuntu.com/Releases
* https://wiki.ubuntu.com/DevelopmentCodeNames

Oma Ubuntu koodnime vaatamiseks:
<pre>
lsb_release -cd
</pre>

Seda näeb veel ka näiteks *cat /etc/lsb-release* abil.

Linuxi tuuma ja päise metapakettide paigaldamine, siin näiteks Ubuntu 16.04 LTS Xenial Xerus:<br>
<pre>$ sudo apt install linux-image-generic-lts-xenial linux-headers-generic-lts-xenial linux-image-generic linux-headers-generic && sudo apt clean && sudo update-grub</pre>

Seejärel arvuti taaskäivitada värskelt paigaldatud tuumaga (sudo reboot). On ju lihtne? Täpsustada saab ka versiooninumbrit, metapakettide asemel võib paigaldada ka konkreetsed versioonid kuigi see ei ole kõige parem mõte kuna sõltub konkreetsest tuuma ja selle päise versioonist, mis ei uuene ja seetõttu on kavalam on paigaldada eespool kirjeldatud automaatselt uuenevad metapaketid.<br><br>
Linuxi tuum uueneb pidevalt ja sellega kaasneb parem riistvara tugi, vigade parandused ja seeläbi ka parem turvalisus, kogu süsteemi parem töötamine. Seetõttu on oluline kasutada võimalikult uusimat tuuma ja vanad eemaldada.<br><br>

Kui metapaketid paigaldatud siis edaspidi toimub uusimate tuumade ja päiste paigaldus automaatselt kogu süsteemi uuendades:<br>
<pre>$ sudo apt update && sudo apt dist-upgrade && sudo apt clean</pre>

Tuleb vaid ise jälgida kui uuema LTS-versiooni tuum muutub kättesaadavaks ka vanematele versioonidele ja siis on soovitav see kasutusele võtta.<br>

<b>Vanade tuumade eemaldamine</b><br>
Kui uusim LTS-versiooni tuum paigaldatud, alglaadur uuendatud, süsteem taaskäivitatud ja veendutud *uname -r* abil, et töötatakse uusima tuuma pealt siis tuleks vanad ja kasutuses mitteolevad tuumad turvalisuse kaalutlustel ka eemaldada.<br><br>

Vaatame esmalt, millised tuumad on paigaldatud:
<pre>
$ dpkg --get-selections | grep linux-image<br>
$ dpkg --get-selections | grep linux-headers
</pre>
või ka
<pre>
$ dpkg -l | grep linux-image<br>
$ dpkg -l | grep linux-headers
</pre><br>
Paigaldatud tuumi, päiseid näeb ka kui vaadata kataloogi <i>ls -l /boot</i> - tuum on nimega <i>vmlinuz</i> ja teised sama versiooninumbriga failid moodustavadki tuuma komplekti koos päise ja kõige muu juurdekuuluvaga.<br><br>
RPM-põhistes Linuxites näeb paigaldatud tuumi käsuga <i>rpm -q kernel</i><br><br>
Seejärel veendume, millise tuuma versiooni pealt arvuti hetkel töötab: <i>uname -r</i>. Kui töötab uusima pealt siis võib kohe asuda vanu eemaldama, vastasel korral tuleb uuendada alglaadurit ja arvuti taaskäivitada: <i>sudo update-grub && sudo reboot</i><br><br>
Vanade tuumade eemaldamiseks on uuematel Ubuntu versioonidel olemas võimalus:<br>
<pre>
$ sudo purge-old-kernels
</pre>
... see eemaldab kõik vanad tuumad ja jätab alles kaks viimast.<br><br>
Kui soovitakse alles jätta vaid viimane siis:
<pre>
$ sudo purge-old-kernels --keep 1 -qy
</pre>
*--keep 1* hoiab alles vaid viimase tuuma versiooni<br>
*-q* teeb ilma väljundit näitamata (*quiet*)<br>
*-y* on vaikimisi nõus.<br>
Lisainfot leiab *man purge-old-kernels*

Kuid vaikimisi sellist mugavat vanade tuumade eemaldamise käsku ei ole - selleks tuleb paigaldada pakett *[byobu](http://byobu.co/)*, mis on [olemas ka Ubuntu vaikimisi varamutes](http://packages.ubuntu.com/search?keywords=byobu&searchon=names&suite=all&section=all) ent mitte kõige uuem. Uusima saab kui lisada [vastav varamu](https://launchpad.net/~byobu/+archive/ubuntu/ppa):
<pre>
sudo add-apt-repository ppa:byobu/ppa && sudo apt-get update
</pre>
... ning paigaldada byobu
<pre>
sudo apt update && sudo apt install byobu && sudo apt clean
</pre>
Lisaks vanade tuumade eemaldamisele võimaldab byobu palju muudki, lisainfot leiab [programmi kodulehelt](http://byobu.co/).<br><br>
<b>Käsitsi vanade tuumade eemaldamine.</b><br>
Kui ei ole võimalik rakenduse byobu'ga kaasatulevat mugavat võimalust vanade tuumade kasutamiseks rakendada siis saab ka käsitsi neid eemaldada.<br><br>
Paketihaldusest otsime paigaldatud tuumi ja nende päiseid:<br>
1.variant (paigaldatud pakettide tuvastamine):
<pre>
dpkg-query -l 'linux-image*' | grep '^ii'
dpkg-query -l 'linux-header*' | grep '^ii'
</pre>
Graafiliselt tööjaamas sama otsing:<br>
otsida (CTRL+F) Synaptic'uga pakette:<br>
<li> <i>linux-image</i></li>
<li> <i>linux-header</i></li>
.. ja täielikult eemaldada (<i>SHIFT+Delete</i>) siis need, mis on vanemad ja millelt masin ei tööta. Synaptic'us saab pakette märkida CTRL-klahvi all hoides. Täielikuks pakettide eemaldamiseks Synaptic'us klahvikombinatsioon <i>SHIFT+Delete</i> või menüüs <i>Paketid->Märgi täielikuks eemaldamiseks</i>.

Käsureal eraldada tühikutega paketid järgmiselt (asendada näites toodud nimed tegelikega):
<pre>
sudo apt purge pakk1 pakk2.....pakk n
</pre>

**NB! Enne eemaldamist veenduda _uname -r_ abil, milliselt tuuma versioonilt masin töötab.**

Võib kasutada ka mõnda teist paketihaldustarkvara, soovi korral saab Synaptic'u ka paigaldada:
<pre>
sudo apt update && sudo apt-get -y install synaptic && sudo apt clean
</pre>
<br>
2.variant paigaldatud tuumade ja päiste otsimiseks
<pre>
sudo dpkg --get-selections | grep linux-image<br>
sudo dpkg --get-selections | grep linux-header
</pre>

<b>Uusim tuum ja päised Ubuntule</b><br>
On võimalik paigaldada ka päris uusi versioone kuid neid ei saa automaatselt uuendada ja selle lahenduse valimisel tuleb ka edaspidi käsitsi uuendada ja ise regulaarselt jälgida kui uus versioon välja tuleb. Kui minna ametlikule Linuxi tuuma kodulehele https://www.kernel.org/ siis näeb, mis on hetkel uusim tuuma versioon (*stable*). Sealt näeb ka teisi tuumade versioone, mida veel toetatakse (*longterm*) ja mis on uusim arenduses olev versioon (*mainline*).<br><br>
Uusimad Ubuntu jaoks pakendatud tuumad ja päised leiab aadressilt http://kernel.ubuntu.com/~kernel-ppa/mainline/ - tuleb minna lehekülje lõppu (nt klahviga *End*) ja võtta suurima numbriga kataloog. Vältida tuleks katalooge, mille nime lõpus on *rc1*, *rc2* jne - need on veel arendusjärgus olevad väljalaskekandidaadid (*rc - release candidate*).<br><br>
Paigaldamiseks tuleb teada ka oma süsteemi arhitektuuri, üldiselt kas 32-bit või 64-bit: *uname -m*. Kui vastuseks on *i686* (või ka *i386*) siis 32-bit ja kui *x86_64* siis on 64-bit süsteemiga tegemist.<br><br>
Soovitav on alla laadida eraldi kataloogi, näiteks tekitame kataloogi *mkdir -p /home/kasutaja/Allalaadimised/tuum/*.<br>
Enne uue versiooni allalaadimist kustutada vanad versioonid: <i>rm -fr /home/kasutaja/Allalaadimised/tuum/*</i><br>
Alla saab laadida näiteks esmalt soovitud kausta sisenedes <i>cd /home/kasutaja/Allalaadimised/tuum/</i> ja seejärel <i>wget http://kernel.ubuntu.com/~kernel-ppa/mainline/vx.x/failinimi.deb</i> abil alla laadides.<br><br>
<b>32-bit</b> süsteemi korral tuleb alla laadida:<br>
<pre>
<b>linux-headers</b>-VERSIOONINUMBER_VERSIOONINUMBER.LOOMISE-AEG_<b>all</b>.deb
<b>linux-headers</b>-VERSIOONINUMBER-generic_VERSIOONINUMBER.LOOMISE-AEG_<b>i386</b>.deb
<b>linux-image</b>-VERSIOONINUMBER-generic_VERSIOONINUMBER.LOOMISE-AEG_<b>i386</b>.deb
</pre>

Kui on saadaval siis võib võtta ka *<b>linux-image-extra</b>-VERSIOONINUMBER_<b>i386 või amd64</b>.deb*<br><br>
Tuumad, mille nimes on *lowlatency* on reaalaja tuumad ja mõeldud teistsugustele süsteemidele kus vaja väga kiiret reageerimist, mida kasutatakse näiteks helitöötluses, arvutijuhitavate tööpinkide juhtimiseks jne. Seal on saadaval veel ka teistele riistvara arhitektuuridele tuumi (*arm*, *ppc* jne).<br><br>
<b>64-bit</b> süsteemi korral tuleb alla laadida:<br>
<pre>
<b>linux-headers</b>-VERSIOONINUMBER_VERSIOONINUMBER.LOOMISE-AEG_<b>all</b>.deb
<b>linux-headers</b>-VERSIOONINUMBER-generic_VERSIOONINUMBER.LOOMISE-AEG_<b>amd64</b>.deb
<b>linux-image</b>-VERSIOONINUMBER-generic_VERSIOONINUMBER.LOOMISE-AEG_<b>amd64</b>.deb
</pre>

Enne paigaldamist tuleb ka veenduda, et kataloogis */home/kasutaja/Allalaadimised/tuum/* ei ole muid mittevajalikke *.deb* faile ega ka vanu, juba paigaldatud tuumade ja päiste faile - kui on siis need tuleks enne järgmise paigalduskäsu käivitamist sealt kataloogist kustutada.<br><br>
Allalaaditud tuuma- ja päisefailide paigaldamiseks, alglaaduri uuendamiseks ja süsteemi taaskäivitamiseks:
<pre>
cd /home/kasutaja/Allalaadimised/tuum/ && sudo dpkg -i * && sudo update-grub && sudo reboot
</pre>

Seejärel tuleks eemaldada vanad tuumad, millest eespool ka juttu oli. Kui vanade tuumade eemaldamisel sõltuvusena eemaldatakse ka pakett *linux-generic* siis selles ei ole midagi halba ja selle võib eemaldada, isegi enne eemaldamist märkida täielikuks eemaldamiseks (käsurealt *sudo apt purge linux-generic*).<br>

<p>Uudiseid Linuxi tuumaga seoses</p>
* https://www.kernel.org/
* https://lwn.net/Kernel/
* https://lkml.org/ - postiloend
* http://www.phoronix.com/scan.php?page=news_topic&q=Linux+Kernel
* https://www.reddit.com/r/kernel/
* https://kernelnewbies.org/

## Harjutus

<ol>
<li> Uurida välja enda operatsioonisüsteemi tuuma versioon.</li>
<li> Uurida erinevate saadaval olevate tuumade kohta</li>
</ol>

## Küsimus

Kuidas saab teada tuuma versiooni?

## Vastus
*uname -r*
