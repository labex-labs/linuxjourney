---
lang: "de"
title: "Subnetze"
description: "Erfahren Sie mehr über Subnetze und Subnetzmasken in der Linux-Netzwerktechnik. Verstehen Sie Netzwerkpräfixe und wie Subnetze den Datenverkehr segmentieren. Beginnen Sie mit diesem anfängerfreundlichen Leitfaden!"
keywords: "Subnetze, Subnetzmaske, Netzwerkpräfix, Linux-Netzwerk, IP-Adresse, Anfänger, Tutorial, ifconfig"
---

## Lesson Content

Wie kann ich feststellen, ob ich mich im selben Netzwerk wie Patty befinde? Nun, wir können einfach das Subnetz betrachten, kurz für Subnetwork. Ein Subnetz ist eine Gruppe von Hosts mit IP-Adressen, die auf eine bestimmte Weise ähnlich sind. Diese Hosts befinden sich normalerweise in räumlicher Nähe zueinander, und Sie können Daten einfach an und von Hosts im selben Subnetz senden. Stellen Sie sich das wie das Versenden von Post im selben Postleitzahlenbereich vor; es ist viel einfacher, als Post in einen anderen Bundesstaat zu senden.

Zum Beispiel wären alle Hosts mit einer IP-Adresse, die mit 123.45.67 beginnt, im selben Subnetz. Mein Host hat eine IP von 123.45.67.8, und Pattys hat eine IP von 123.45.67.9. Die gemeinsamen Zahlen sind mein network prefix, und die 8 und 9 sind unsere Hosts; daher ist mein Netzwerk dasselbe wie Pattys. Ein Subnetz ist in einen network prefix, wie 123.45.67.0, und eine subnet mask unterteilt.

### Subnet Masks

Subnet masks bestimmen, welcher Teil Ihrer IP-Adresse der Netzwerkanteil und welcher Teil der Host-Anteil ist.

Eine typische subnet mask kann so aussehen:

```plaintext
255.255.255.0
```

Der 255-Anteil ist tatsächlich unsere Maske. Um dies etwas einfacher zu verstehen, erinnern Sie sich, wie wir jedes Oktett als 8 bits bezeichnen? In der Informatik wird ein bit durch eine 0 oder eine 1 in binärer Form dargestellt. Wenn Binärzahlen verwendet werden, bedeutet 1 an und 0 aus. Was ergeben also 8 Nullen oder Einsen?

Geben Sie bei Google "binary to decimal calculator" ein und konvertieren Sie 11111111 in eine Dezimalform. Was erhalten Sie? 255! Ein Oktett reicht also von 0 bis 255. Wenn wir also eine subnet mask von 255.255.255.0 und eine IP-Adresse von 192.168.1.0 hätten, wie viele Hosts befinden sich in diesem Subnetz? Die Antwort darauf finden wir in unserer Lektion über Subnetz-Mathematik.

Auch wenn wir über unser Subnetz sprechen, bezeichnen wir es üblicherweise mit dem network prefix, gefolgt von der subnet mask:

```plaintext
123.234.0.0/255.255.0.0
```

### Warum?

Warum um alles in der Welt erstellen wir Subnetze? Subnetting wird verwendet, um Netzwerke zu segmentieren und den Datenfluss innerhalb dieses Netzwerks zu steuern. Ein Host in einem Subnetz kann also nicht mit einem anderen Host in einem anderen Subnetz interagieren.

Aber Moment mal, was ist, wenn ich mich mit anderen Hosts wie yahoo.com verbinden möchte? Dann müssen Sie Subnetze miteinander verbinden. Um Subnetze zu verbinden, müssen Sie nur die Hosts finden, die mit mehr als einem Subnetz verbunden sind. Wenn zum Beispiel mein Host unter 192.168.1.129 mit einem lokalen Netzwerk von 192.168.1.129/24 verbunden ist, kann er alle Hosts in diesem Netzwerk erreichen. Um Hosts im restlichen Internet zu erreichen, muss er über den router kommunizieren. Traditionell befindet sich der router in den meisten Netzwerken mit einer subnet mask von 255.255.255.0 normalerweise an Adresse 1 des Subnetzes, also 192.168.1.1. Dieser router wird nun einen Port haben, der ihn mit einem anderen Subnetz verbindet (mehr dazu im Kurs Routing). Bestimmte IP-Adressen (private networks) sind für das Internet nicht sichtbar, und wir haben Dinge wie NAT (mehr dazu später).

## Exercise

Verwenden Sie `ifconfig`, um Ihre subnet mask anzuzeigen.

## Quiz Question

True or false, a subnet consists of a subnet mask and network prefix.

## Quiz Answer

True
