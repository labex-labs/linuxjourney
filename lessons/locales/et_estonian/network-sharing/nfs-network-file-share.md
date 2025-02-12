# NFS

## Tunni sisu

Kõite standardsem failide jagamise viis Linuxis on NFS (*Network File System* ehk võrgufailisüsteem). NFS võimaldab serveril jagada katalooge ja faile üle võrgu rohkem kui ühe kasutajaga.

NFS serveri loomise üksikasjadesse sellel kursusel ei süübita kuna see võib veidi keeruliseks minna, küll aga räägime NFS kliendi üles seadmisest. Siin toodud näited Ubuntu Linuxi baasil

<b>NFS ühenduse ülesseadmine</b><br>
<pre>$ sudo apt update && sudo apt-get -y install nfs-common && sudo ldconfig && sudo dpkg --configure -a && sudo apt-get clean
$ sudo mount server:/serveri/kataloog /kohaliku/arvuti/kataloog</pre>

... kus "server" asemele kirjutada serverarvuti IP- või internernetiaadress.<br>

Vajadusel võib märkida ka failisüsteemi ja pordinumbri (asendada siin näites toodud number reaalselt kasutusesolevaga):<br>
<pre>$ sudo mount -t nfs -o port=1122 server:/serveri/kataloog /kohaliku/arvuti/kataloog</pre>


<b>Automaatne haakimine</b><br>
Ütleme, et NFS server on üsna tihti kasutuses ning kasutaja soovib, et see oleks jäädavalt külge haagitud. Tavaliselt võiks mõelda, et tuleb muuda /etc/fstab faili, kuid alati ei pruugi õnnestuda saada serveriga ühendust ja see võib tekitada alglaadimisel probleeme. Selle asemel tasuks üles seada automaatne haakimine. Seda tehakse <b>automount</b> tööriistaga, uuemates Linuxi versioonides <b>amd</b>. Kui mõnele täpsustatud kataloogile püütakse ligi pääseda otsib <b>automount</b> üles vastava serveri ja haagib selle automaatselt külge.

Paigaldamiseks:<br>
<pre>
sudo apt update && sudo apt-get -y install am-utils && sudo ldconfig && sudo dpkg --configure -a && sudo apt-get clean
</pre>

## Harjutus

Lugeda [*amd* man-lehekülge](https://linux.die.net/man/8/amd), et selle kohta rohkem teada saada. Lisalugemist TLDP (The Linux Documentation Project) [automount'i juhendist](http://www.tldp.org/HOWTO/Automount.html).

## Küsimus

Millise tööriistaga hallatakse automaatseid haakepunkte?

## Vastus

*automount*
