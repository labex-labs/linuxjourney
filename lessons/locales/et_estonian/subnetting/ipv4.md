# IPv4

## Tunni sisu

Õppisime, et võrgus on kasutajatel unikaalsed IP aadressid. IPv4 aadress võib välja näha näiteks selline:

<pre>204.23.124.23</pre>

Selline aadress koosneb tegelikult kahest osast. Võrgu osa tuvastab asukoha võrgu ja hosti osa ütleb, millise kasutajaga selles võrgus tegu on. Sellel kursusel keskendutakse rohkem IPv4 aadressidele, mida peetakse suurema tõenäosusega silmas kui räägitakse IP aadressidest.

IP aadress jagatakse punktidega oktettideks. IPv4 aadressis on neli oktetti. Kui arvutiteadust natuke tunda siis oktett on 8 bitti, 8 bitti on aga 1 bait. Seega räägitakse, et IPv4 aadress on 4 baidine. Bittidest tuleb aga tihedamalt juttu kui teemaks on alamvõrgud.

IP aadressi saab kuvada *ifconfig -a* käsuga (näitab ka neid võrguliideseid, mis hetkel ei tööta või on seadistamata):

<pre>
pete@icebox:~$ ifconfig -a
eth0      Link encap:Ethernet  HWaddr 1d:3a:32:24:4d:ce  
          inet addr:192.168.1.129  Bcast:192.168.1.255  Mask:255.255.255.0
          inet6 addr: fd60::21c:29ff:fe63:5cdc/64 Scope:Link
</pre>

Nagu näha on selle arvuti IPv4 aadress 192.168.1.129.

Sisevõrgu IPv4 aadressid:<br>
* 10.0.0.0 – 10.255.255.255, masinate arv: 16 777 216 (24 bit = 2<sup>24</sup> )
* 172.16.0.0 – 172.31.255.255, masinate arv: 1 048 576 ( 20 bit = 2<sup>20</sup> )
* 192.168.0.0 – 192.168.255.255, masinate arv: 65 536 (16 bit = 2<sup>16</sup> )

Seade ise (*loopback*):
* vaatamiseks: <i>ifconfig lo</i>
* IPv4 aadress: 127.0.0.1

## Harjutus

Tuvastada enda arvuti võrguliideste IP aadressid käsuga ifconfig.

## Küsimus

Mitu baiti on IPv4 aadressis?

## Vastus

4
