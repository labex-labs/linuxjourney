# arp

## Tunni sisu

Meenutame, et enne kui ARP hakkab otsima IP aadressile vastavat MAC aadressi, kontrolltakse kohalikku ARP tabelit. Seda tabelit saab kasutaja vaadata:

<pre>
pete@icebox:~$ arp
Address                  HWtype  HWaddress           Flags Mask            Iface
192.168.22.1            ether   00:12:24:fc:12:cc   C                     eth0
192.168.22.254          ether   00:12:45:f2:84:64   C                     eth0
</pre>

ARP tabel on arvuti käivitumisel tühi, seda täidetakse kui pakette hakatakse välja saatma. Kui pakett saadetakse sihtkohta, mida ARP tabelis ei ole, toimub järgnev:

<ol>
<li>Saatja süsteem koostab Etherneti raami ARP päringu paketiga.</li>
<li>See raam saadetakse leviedastuse sõnumina (<i>broadcast</i>) tervesse kohtvõrku.</li>
<li>Kui mõni host teab õiget MAC aadressi, saadab ta seda sisaldava vastuse.</li>
<li>Esialgne saatja lisab IP aadressile vastava MAC aadressi ARP tabelisse ning seejärel saadab soovitud paketi.</li>
</ol>

Ka ip käsuga saab ARP tabelit kuvada:

<pre>
$ ip neighbour show
</pre>

## Harjutus

Vaadelda, mis toimub ARP tabelis pärast arvuti käivitamist kui hakata võrgus millegagi tegelema.

## Küsimus

Millise käsuga saab kuvada ARP tabeli?

## Vastus

*arp*
