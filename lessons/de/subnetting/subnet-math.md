---
index: 3
lang: "de"
title: "Subnetz-Mathematik"
meta_title: "Subnetz-Mathematik - Subnetting"
meta_description: "Lernen Sie die Grundlagen der Subnetz-Mathematik und wie Sie verfügbare Hosts in einem Netzwerk berechnen. Verstehen Sie IP-Adressierung und Subnetzmasken für Anfänger. Beginnen Sie Ihre Linux-Reise!"
meta_keywords: "Subnetz-Mathematik, IP-Adresse, Subnetzmaske, Netzwerk-Hosts, Binär, Linux-Netzwerk, Anfänger-Tutorial, Leitfaden"
---

## Lesson Content

Okay, wir wissen, dass Subnetzmasken wichtig sind, um herauszufinden, wie viele Hosts wir in unserem Subnetz haben können. Wie viele Hosts wären das also?

Nehmen wir an, ich habe eine IP-Adresse von **192.168.1.0** und eine Subnetzmaske von **255.255.255.0**. Nun, lassen Sie uns diese Zahlen in binärer Form anordnen. Verwenden Sie vorerst einen Online-Rechner, um diese Werte von dezimal in binär umzuwandeln.

```
192.168.1.165  = 11000000.10101000.00000001.10100101
255.255.255.0  = 11111111.11111111.11111111.00000000
```

Die IP-Adresse wird durch unsere Subnetzmaske maskiert. Wenn Sie eine 1 sehen, ist sie maskiert, und wir tun so, als würden wir sie nicht sehen. Die einzigen möglichen Hosts, die wir haben können, stammen also aus dem Bereich `00000000`. Denken Sie daran, `11111111` in binärer Form entspricht 255. Wir berücksichtigen auch 0 als Hostnummer, so dass es 256 mögliche Optionen gibt. Es mag jedoch so aussehen, als hätten wir 256 mögliche Optionen, aber wir subtrahieren tatsächlich 2 Hosts, da wir die Broadcast-Adresse und die Subnetzadresse berücksichtigen müssen, so dass uns 254 mögliche Hosts in unserem Subnetz bleiben. Wir wissen also, dass wir Hosts mit IP-Adressen im Bereich von 192.168.1.1 - 192.168.1.254 haben können.

## Exercise

Übung macht den Meister! Hier sind einige praktische Labs, um Ihr Verständnis von IP-Adressierung und Subnetting zu vertiefen:

1. **[IP-Subnetting und Binärkonvertierung im Linux-Terminal durchführen](https://labex.io/de/labs/comptia-perform-ip-subnetting-and-binary-conversion-in-the-linux-terminal-592782)** - Meistern Sie IP-Subnetting und Binärkonvertierung, wesentliche Fähigkeiten für die Netzwerkkonfiguration und -planung.
2. **[IP-Adresstypen und Erreichbarkeit in Linux erkunden](https://labex.io/de/labs/comptia-explore-ip-address-types-and-reachability-in-linux-592780)** - Vertiefen Sie Ihr Verständnis verschiedener IP-Adresstypen und wie Sie die Netzwerkerreichbarkeit mit Linux-Befehlen überprüfen können.
3. **[Netzwerkschicht-Konnektivität in Linux simulieren](https://labex.io/de/labs/comptia-simulate-network-layer-connectivity-in-linux-592752)** - Wenden Sie Ihr Wissen an, indem Sie Netzwerkkonfigurationen simulieren und die Konnektivität zwischen verschiedenen IP-Subnetzen in einer praktischen Umgebung testen.

Diese Labs helfen Ihnen, die Konzepte der IP-Adressierung, Subnetzmasken und Host-Berechnung in realen Szenarien anzuwenden und Vertrauen in die Netzwerk-Grundlagen aufzubauen.

## Quiz Question

Was ist das binäre Äquivalent von 255?

## Quiz Answer

11111111
