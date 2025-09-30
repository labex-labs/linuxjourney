---
index: 5
lang: "de"
title: "CIDR"
meta_title: "CIDR - Subnetting"
meta_description: "Lernen Sie die CIDR-Notation für Linux-Netzwerke. Verstehen Sie Subnetzmasken, IP-Adressierung und Host-Berechnung mit diesem anfängerfreundlichen Leitfaden. Verbessern Sie Ihre Netzwerkkenntnisse!"
meta_keywords: "CIDR, Subnetzmaske, IP-Adressierung, Netzwerkpräfix, Linux-Netzwerke, Anfänger, Tutorial, Leitfaden"
---

## Lesson Content

CIDR (Classless Inter-Domain Routing) wird verwendet, um eine Subnetzmaske kompakter darzustellen. Sie können Subnetze in CIDR-Notation sehen, wobei ein Subnetz wie 10.42.3.0/255.255.255.0 als 10.42.3.0/24 geschrieben wird. Diese Notation umfasst sowohl das Subnetzpräfix als auch die Subnetzmaske.

Denken Sie daran, eine IP-Adresse besteht aus 4 Bytes oder 32 Bits. CIDR gibt die Anzahl der Bits an, die als Netzwerkpräfix verwendet werden. So bedeutet 123.12.24.0/23, dass die ersten 23 Bits verwendet werden. Was bedeutet das? Wie viele Hosts sind das?

Ein einfacher Trick ist, die CIDR-Adresse (23) von der Gesamtzahl der Bits, die eine IP-Adresse haben kann (32), zu subtrahieren. Dies ergibt 9 Bits. Daher ist 2^9 = 512. Wir müssen jedoch 2 Adressen entfernen (die Subnetzadresse und die Broadcast-Adresse), sodass wir 510 nutzbare Hosts haben.

## Exercise

Übung macht den Meister! Hier sind einige praktische Übungen, um Ihr Verständnis von CIDR, IP-Adressierung und Subnetting zu vertiefen:

1. **[IP-Subnetting und Binärkonvertierung im Linux-Terminal durchführen](https://labex.io/de/labs/comptia-perform-ip-subnetting-and-binary-conversion-in-the-linux-terminal-592782)** – Meistern Sie IP-Subnetting und Binärkonvertierung, einschließlich der Übersetzung von CIDR-Masken und der Berechnung nutzbarer Hosts.
2. **[Netzwerkschicht-Konnektivität in Linux simulieren](https://labex.io/de/labs/comptia-simulate-network-layer-connectivity-in-linux-592752)** – Lernen Sie, statische IP-Adressen zuzuweisen und zu beobachten, wie IP-Subnetze die direkte Netzwerkkommunikation in einer simulierten Umgebung steuern.
3. **[IP-Adresstypen und Erreichbarkeit in Linux erkunden](https://labex.io/de/labs/comptia-explore-ip-address-types-and-reachability-in-linux-592780)** – Erkunden Sie IP-Adressierung und Netzwerk-Erreichbarkeit mithilfe von Befehlen wie `ping` und `ip a`, um verschiedene IP-Typen und Konnektivität zu testen.

Diese Labs helfen Ihnen, die Konzepte von CIDR und IP-Adressierung in realen Szenarien anzuwenden und Vertrauen in die Netzwerkkonfiguration aufzubauen.

## Quiz Question

Keine Fragen, weiter geht's!

## Quiz Answer
