---
lang: "de"
title: "CIDR"
meta_title: "CIDR - Subnetting"
meta_description: "Lernen Sie die CIDR-Notation für Linux-Netzwerke. Verstehen Sie Subnetzmasken, IP-Adressierung und Host-Berechnung mit diesem anfängerfreundlichen Leitfaden. Verbessern Sie Ihre Netzwerkkenntnisse!"
meta_keywords: "CIDR, Subnetzmaske, IP-Adressierung, Netzwerkpräfix, Linux-Netzwerke, Anfänger, Tutorial, Leitfaden"
---

## Lesson Content

CIDR (Classless Inter-Domain Routing) wird verwendet, um eine Subnetzmaske kompakter darzustellen. Möglicherweise sehen Sie Subnetze in CIDR-Notation, wobei ein Subnetz wie 10.42.3.0/255.255.255.0 als 10.42.3.0/24 geschrieben wird. Diese Notation umfasst sowohl das Subnetzpräfix als auch die Subnetzmaske.

Denken Sie daran, eine IP-Adresse besteht aus 4 Bytes oder 32 Bits. CIDR gibt die Anzahl der Bits an, die als Netzwerkpräfix verwendet werden. 123.12.24.0/23 bedeutet also, dass die ersten 23 Bits verwendet werden. Was bedeutet das? Wie viele Hosts sind das?

Ein einfacher Trick ist, die CIDR-Adresse (23) von der Gesamtzahl der Bits, die eine IP-Adresse haben kann (32), zu subtrahieren. Dies ergibt 9 Bits. Daher ist 2^9 = 512. Wir müssen jedoch 2 Adressen entfernen (die Subnetzadresse und die Broadcast-Adresse), sodass wir 510 nutzbare Hosts haben.

## Exercise

No exercises for this lesson.

## Quiz Question

Keine Fragen, weiter geht's!

## Quiz Answer
