---
index: 2
lang: "de"
title: "Subnetze"
meta_title: "Subnetze - Subnetting"
meta_description: "Erfahren Sie mehr über Subnetze und Subnetzmasken in der Linux-Vernetzung. Verstehen Sie Netzwerkpräfixe und wie Subnetze den Datenverkehr segmentieren. Beginnen Sie mit diesem anfängerfreundlichen Leitfaden!"
meta_keywords: "Subnetze, Subnetzmaske, Netzwerkpräfix, Linux-Netzwerk, IP-Adresse, Anfänger, Tutorial, ifconfig"
---

## Lesson Content

Wie kann ich feststellen, ob ich im selben Netzwerk wie Patty bin? Nun, wir können einfach das Subnetz betrachten, kurz für Subnetwork. Ein Subnetz ist eine Gruppe von Hosts mit IP-Adressen, die auf eine bestimmte Weise ähnlich sind. Diese Hosts befinden sich normalerweise in räumlicher Nähe zueinander, und Sie können Daten einfach zu und von Hosts im selben Subnetz senden. Stellen Sie es sich vor wie das Senden von Post im selben Postleitzahlenbereich; es ist viel einfacher, als Post in einen anderen Bundesstaat zu senden.

Zum Beispiel wären alle Hosts mit einer IP-Adresse, die mit 123.45.67 beginnt, im selben Subnetz. Mein Host hat eine IP von 123.45.67.8, und Pattys hat eine IP von 123.45.67.9. Die gemeinsamen Zahlen sind mein Netzwerkpräfix, und die 8 und 9 sind unsere Hosts; daher ist mein Netzwerk dasselbe wie Pattys. Ein Subnetz ist in ein Netzwerkpräfix, wie 123.45.67.0, und eine Subnetzmaske unterteilt.

### Subnetzmasken

Subnetzmasken bestimmen, welcher Teil Ihrer IP-Adresse der Netzwerkanteil und welcher Teil der Hostanteil ist.

Eine typische Subnetzmaske kann so aussehen:

```plaintext
255.255.255.0
```

Der 255-Teil ist tatsächlich unsere Maske. Um dies etwas einfacher zu verstehen, erinnern Sie sich, wie wir jedes Oktett als 8 Bits bezeichnen? In der Informatik wird ein Bit durch eine 0 oder eine 1 in Binärform dargestellt. Wenn Binärzahlen verwendet werden, bedeutet 1 an und 0 aus. Was ergeben also 8 Nullen oder Einsen?

Geben Sie bei Google "binary to decimal calculator" ein und konvertieren Sie 11111111 in eine Dezimalform. Was erhalten Sie? 255! Ein Oktett reicht also von 0 bis 255. Wenn wir also eine Subnetzmaske von 255.255.255.0 und eine IP-Adresse von 192.168.1.0 hätten, wie viele Hosts wären dann in diesem Subnetz? Die Antwort darauf finden wir in unserer Lektion über Subnetz-Mathematik.

Auch wenn wir über unser Subnetz sprechen, bezeichnen wir es üblicherweise durch das Netzwerkpräfix gefolgt von der Subnetzmaske:

```plaintext
123.234.0.0/255.255.0.0
```

### Warum?

Warum um alles in der Welt erstellen wir Subnetze? Subnetting wird verwendet, um Netzwerke zu segmentieren und den Datenfluss innerhalb dieses Netzwerks zu steuern. So kann ein Host in einem Subnetz nicht mit einem anderen Host in einem anderen Subnetz interagieren.

Aber Moment mal, was ist, wenn ich mich mit anderen Hosts wie yahoo.com verbinden möchte? Dann müssen Sie Subnetze miteinander verbinden. Um Subnetze zu verbinden, müssen Sie nur die Hosts finden, die mit mehr als einem Subnetz verbunden sind. Wenn zum Beispiel mein Host unter 192.168.1.129 mit einem lokalen Netzwerk von 192.168.1.129/24 verbunden ist, kann er alle Hosts in diesem Netzwerk erreichen. Um Hosts im restlichen Internet zu erreichen, muss er über den Router kommunizieren. Traditionell befindet sich der Router in den meisten Netzwerken mit einer Subnetzmaske von 255.255.255.0 normalerweise an Adresse 1 des Subnetzes, also 192.168.1.1. Dieser Router wird nun einen Port haben, der ihn mit einem anderen Subnetz verbindet (mehr dazu im Routing-Kurs). Bestimmte IP-Adressen (private Netzwerke) sind für das Internet nicht sichtbar, und wir haben Dinge wie NAT (mehr dazu später).

## Exercise

Übung macht den Meister! Hier sind einige praktische Übungen, um Ihr Verständnis von IP-Adressierung und Subnetting zu vertiefen:

1. **[MAC- und IP-Adressen in Linux identifizieren](https://labex.io/de/labs/linux-identify-mac-and-ip-addresses-in-linux-592731)** - Üben Sie die Verwendung des Befehls `ip a`, um Netzwerkinformationen, einschließlich IPv4-Adressen, zu identifizieren, was grundlegend für das Verständnis von Subnetzen ist.
2. **[IP-Adresstypen und Erreichbarkeit in Linux erkunden](https://labex.io/de/labs/linux-explore-ip-address-types-and-reachability-in-linux-592780)** - Lernen Sie, verschiedene IP-Adresstypen zu erkunden und die Netzwerkerreichbarkeit zu testen, um zu überprüfen, ob Hosts im selben Netzwerk sind.
3. **[IP-Subnetting und Binärkonvertierung im Linux-Terminal durchführen](https://labex.io/de/labs/linux-perform-ip-subnetting-and-binary-conversion-in-the-linux-terminal-592782)** - Meistern Sie IP-Subnetting und Binärkonvertierung, indem Sie die in der Lektion besprochenen Konzepte von Netzwerkpräfixen und Host-Identifikation direkt anwenden.

Diese Labs helfen Ihnen, die Konzepte in realen Szenarien anzuwenden und Vertrauen in die Netzwerkadressierung und das Subnetting aufzubauen.

## Quiz Question

Wahr oder falsch, ein Subnetz besteht aus einer Subnetzmaske und einem Netzwerkpräfix.

## Quiz Answer

True
