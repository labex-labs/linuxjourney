---
lang: "de"
title: "Pfad eines Pakets"
description: "Erfahren Sie, wie ein Paket innerhalb und außerhalb eines Netzwerks reist. Verstehen Sie IP, MAC, ARP und Routing-Tabellen für die Netzwerkkommunikation. Beginnen Sie Ihre Reise in die Linux-Netzwerktechnik!"
keywords: "Paketreise, Netzwerkkommunikation, ARP, IP-Adresse, MAC-Adresse, Routing-Tabelle, Linux-Netzwerk, Anfängerleitfaden"
---

## Lesson Content

### Schauen wir uns an, wie ein Paket innerhalb seines lokalen Netzwerks reist

1. Zuerst vergleicht die lokale Maschine die Ziel-IP-Adresse, um festzustellen, ob sie sich im selben Subnetz befindet, indem sie ihre Subnetzmaske betrachtet.
2. Wenn Pakete gesendet werden, müssen sie eine Quell-MAC-Adresse, eine Ziel-MAC-Adresse, eine Quell-IP-Adresse und eine Ziel-IP-Adresse haben. Zu diesem Zeitpunkt kennen wir die Ziel-MAC-Adresse nicht.
3. Um den Ziel-Host zu erreichen, verwenden wir ARP, um eine Anfrage im lokalen Netzwerk zu senden, um die MAC-Adresse des Ziel-Hosts zu finden.
4. Jetzt kann das Paket erfolgreich gesendet werden!

### Schauen wir uns an, wie ein Paket außerhalb seines Netzwerks reist

1. Zuerst vergleicht die lokale Maschine die Ziel-IP-Adresse. Da sie sich außerhalb unseres Netzwerks befindet, sieht sie die MAC-Adresse des Ziel-Hosts nicht. Und wir können ARP nicht verwenden, da die ARP-Anfrage ein Broadcast an lokal verbundene Hosts ist.
2. Unser Paket schaut sich nun die Routing-Tabelle an. Es kennt die Adresse der Ziel-IP nicht, also sendet es sie an das Standard-Gateway (einen anderen Router). Unser Paket enthält nun unsere Quell-IP, Ziel-IP und Quell-MAC; wir haben jedoch keine Ziel-MAC. Denken Sie daran, MAC-Adressen werden nur über dasselbe Netzwerk erreicht. Was tut es also? Es sendet eine ARP-Anfrage, um die MAC-Adresse des Standard-Gateways zu erhalten.
3. Der Router betrachtet das Paket und bestätigt die Ziel-MAC-Adresse, aber es ist nicht die endgültige Ziel-IP-Adresse, also schaut er weiterhin in der Routing-Tabelle nach, um das Paket an eine andere IP-Adresse weiterzuleiten, die dem Paket helfen kann, sein Ziel zu erreichen. Jedes Mal, wenn sich das Paket bewegt, entfernt es die alten Quell- und Ziel-MAC-Adressen und aktualisiert das Paket mit den neuen Quell- und Ziel-MAC-Adressen.
4. Sobald das Paket an dasselbe Netzwerk weitergeleitet wird, verwenden wir ARP, um die endgültige Ziel-MAC-Adresse zu finden.
5. Während dieses Prozesses ändert unser Paket weder die Quell- noch die Ziel-IP-Adresse.

## Exercise

No exercises for this lesson.

## Quiz Question

Wie finden wir die MAC-Adresse einer IP-Adresse heraus?

## Quiz Answer

ARP
