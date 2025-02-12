﻿# dhclient

## Tunni sisu

DHCP'd oleme juba tutvustanud. Enamasti ei ole kasutajatel tarvis IP aadresse, alamvõrgu maske ja muud käsitsi vaja seadistada. Selleks ju ongi DHCP. *dhclient* (asukoha vaatamiseks: *which dhclient*) käivitub alglaadimisel ning kasutab võrguliideste nimekirja saamiseks */etc/dhcp/dhclient.conf* faili. Selle nimekirja alusel püütakse kõiki liideseid seadistada DHCP protokolliga.

Liisitud IP aadresside kohta peab süsteemi taaskäivituste vahel järge *<a target="_blank" href="https://linux.die.net/man/5/dhclient.leases">dhclient.leases</a>* fail. Pärast */etc/dhcp/dhclient.conf* faili lugemist loetakse */var/lib/dhclient/dhclient.leases* faili, et tuvastada, kas mõnele liidesele on juba IP aadress liisitud.

<b>Uue IP aadressi saamine</b>

<pre>$ sudo dhclient</pre>

Lisainfo *man dhclient*

## Harjutus

Harjutust pole.

## Küsimus

Milline tööriist püüab määrata IP aadresse DHCP protokolliga?

## Vastus

*dhclient*
