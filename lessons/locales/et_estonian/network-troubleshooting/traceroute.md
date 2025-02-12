# traceroute

## Tunni sisu

*traceroute* käsk võimaldab tuvastada pakettide marsruute. Selleks saadetakse pakett kasvava TTL väärtusega alustades 1st. Esimene marsruuter, mis saab paketi, lahutab selles ühe ja seega eemaldab paketi võrguliiklusest. Marsruuter saadab aga vastu ICMP *Time Exceeded* ületatud aja teate. Järgmine väljasaadetav pakett saab TTL väärtuseks juba 2 ja see jõuab esimesest marsruuterist kaugemale. Teise marsruuteri juures aga on väärtus jälle 0 ja tuleb samasugune ICMP teade. Traceroute töötab sedasi, kuna nõnda pakette saates ja neid kõrvaldades ehitatakse nimekiri marsruuteritest, mida paketid peavad sihtkohta jõudmiseks läbima. Kõige lõpuks saadetakse ICMP *Echo Reply* kajapäringu vastus.

Väike näide traceroute'ist:

<pre>
$ traceroute google.com                                                                          
traceroute to google.com (216.58.216.174), 30 hops max, 60 byte packets                          
 1  192.168.4.254 (192.168.4.254)  0.028 ms  0.009 ms  0.008 ms                                  
 2  100.64.1.113 (100.64.1.113)  1.227 ms  1.226 ms 0.920 ms
 3  100.64.0.20 (100.64.0.20)  1.501 ms 1.556 ms  0.855 ms                                                                                 
</pre>

Iga marsruuter on seade, mis jääb saatja ja saaja vahele. Kuvatakse sihtkoha nimi ja IP aadress, viimased kolm välja kajastavad marsruuterini jõudmiseks kulunud aega. Vaikimisi saadetakse kolm paketti.

## Harjutus

Kasutada *traceroute* käsku ja tutvuda väljundiga.

## Küsimus

Millist väärtust vähendatakse ühe võrra, kui pakett sooritab võrgus hüppe?

## Vastus

*TTL*
