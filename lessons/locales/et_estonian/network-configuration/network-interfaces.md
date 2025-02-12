# Võrguliidesed

## Tunni sisu

Võrguliideste abil ühendab operatsioonisüsteemi tuum võrgunduse tarkvaralise poole riistvaralisega. Järgmine näide peaks juba tuttav olema:

<pre>
pete@icebox:~$ ifconfig -a
eth0      Link encap:Ethernet  HWaddr 1d:3a:32:24:4d:ce  
          inet addr:192.168.1.129  Bcast:192.168.1.255  Mask:255.255.255.0
          inet6 addr: fd60::21c:29ff:fe63:5cdc/64 Scope:Link
</pre>

<b>ifconfig käsk</b>

<b>ifconfig</b> tööriist võimaldab kasutajal seadistada võrguliideseid. Kui võrguliideseid üles seatud pole, ei oska tuuma seadmete juhtprogrammid ja võrk omavahel suhelda. Ifconfig käivitub alglaadimisel ja seadistab liidesed kasutades sätete faili kuid seda võib ka käsitsi teha. Ifconfig'i väljund kuvab vasakul liidese nime ja paremal detailse informatsiooni. Kõige tavalisemad liidesed on *eth0* (Etherneti kaart), *wlan0* (juhtmevaba ühendusliides), *lo* (tagastusliides). Tagastusliides esindab kasutaja enda arvutit, see suunab ühenduse nö kaarega kasutaja juurde tagasi. See liides on väga kasulik silumiseks või kohalike serveritega ühendumiseks.

Liidese oleks võib olla üleval või maas. Nagu arvata võib siis maas on liides juhul kui ta on "välja lülitatud". Kõige huvipakkuvamad väljad *ifconfig* väljundis on ilmsel *HWaddr* (liidese MAC aadress), *inet address* (IPv4 aadress) ja *inet6* (IPv6 aadress). Nagu näha on seal ka alamvõrgu mask ja leviedastuse aadress. Liideste informatsioon on leitav ka failist */etc/network/interfaces* või kataloogist */etc/network/interfaces.d/*. Turvalisem on viimati nimetatud kataloogi eraldi tekstifailid tekitada. Siis on kindel, et ei muudeta originaalset süsteemi seadistuse faili. Siiski kui otsustatakse minna seda teed, et võrguseaded kirjutatakse ise loodud faili(desse) kataloogis */etc/network/interfaces.d/* siis tuleks faili */etc/network/interfaces* lisada rida _source /etc/network/interfaces.d/*_

<b>Liidese loomine ja aktiveerimine</b>

<pre>$ ifconfig eth0 192.168.2.1 netmask 255.255.255.0 up</pre>

See käsk määrab eth0 liidesele IP aadressi ja maski ning ühtaegu aktiveerib selle.

<b>Liidese aktiveerimine või deaktiveerimine</b>

<pre>
$ ifup eth0
$ ifdown eth0
</pre>

<b>ip käsk</b>

Ka <b>ip</b> käsuga saab võrguseadeid muuta. Sõltuvalt Linuxist võib see olla isegi võrgusätete muutmise eelismeetod.

Mõned näited selle kasutamisest:

<b>Kõikide liideste informatsiooni kuvamine</b>
<pre>
$ ip link show
</pre>

<b>Liidese statistika kuvamine</b>
<pre>
$ ip -s link show eth0
</pre>

<b>Liidesele määratud IP aadressi kuvamine</b>
<pre>
$ ip address show
</pre>
ja toimib ka lühikäsk:<br>
<pre>
$ ip a
</pre>

<b>Liidese aktiveerimine või deaktiveerimine</b>
<pre>
$ ip link set eth0 up
$ ip link set eth0 down
</pre>

<b>Liidesele IP aadressi määramine</b>
<pre>
$ ip address add 192.168.1.1/24 dev eth0
</pre>

Püsivaks IP aadressi määramiseks tuleb 

## Harjutus

Proovida muuta võrguliideste olekut ning märgata, mis selle tagajärjel juhtub.

Kas võrguliideseid saab seadistada nii *ifconfig* kui *ip* käskudega?

## Küsimus

Millise käsuga saab seadistada võrguliideseid?

## Vastus

*ifconfig*
