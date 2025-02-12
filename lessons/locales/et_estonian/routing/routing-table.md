# Marsruutimistabel

## Tunni sisu

Vaatame marsruutimistabelit (-n numbrilised väärtused):

<pre>
pete@icebox:~$ sudo route -n
Kernel IP routing table
Destination     Gateway         Genmask         Flags Metric Ref    Use Iface
0.0.0.0         192.168.224.2   0.0.0.0         UG    0      0        0 eth0
192.168.224.0   0.0.0.0         255.255.255.0   U     1      0        0 eth0
</pre>

Tabeli väljad annavad järgmist infot:

<b>*Destination*</b>

Esimesest väljast võib leida sihtkoha IP aadressi 192.168.224.0, tabeli järgi peab iga pakett, mis üritab sinna võrku jõuda, väljuma Etherneti kaablist (võrguliidese tähis: eth0). Kui lähteaadress oleks 192.168.224.5 ja pakett peab jõudma aadressile 192.168.224.7, kasutatakse otseselt liidest eth0. 

Märkasid aadressi <b>0.0.0.0</b>? See tähendab, et aadressi ei ole täpsustatud või see on teadmata. Seega ütleme, et kui on soov saata pakett aadressile 151.123.43.6, siis selle tabeli järgi marsruuter ei tea kuhu täpselt seda saata, seega kasutatakse aadressi 0.0.0.0 ja pakett marsruuditakse lüüsi (*Gateway*'le).

<b>*Gateway*</b>

Saates pakette kohtvõrgust väljapoole, tuleb see edastada lüüsi aadressile. Lüüs ongi väga asjakohaselt lüüs teistesse võrkudesse.

<b>*Genmask*</b>

See on alamvõrgu mask, mille abil selgitatakse välja, millised IP aadressid millise sihtkohaga kattuvad.

<b>*Flags*</b>

<ul>
<li>UG - Võrk on töökorras ja töötab lüüsina</li>
<li>U - Võrk on töökorras</li>
</ul>

<b>*Iface*</b>

See on võrguliides, mille kaudu paketid väljuvad. *eth0* tähendab tavaliselt süsteemi võrguadapterit.

## Harjutus

Vaadata marsruutimistabelit ja tuvastada kuhu pakette osatakse marsruutida.

## Küsimus

Kuhu suunatakse paketid, kui sihtkohta marsruutimistabelist ei leita?

## Vastus

Lüüsile
