---
index: 5
lang: "de"
title: "Distanzvektorprotokolle"
meta_title: "Distanzvektorprotokolle - Routing"
meta_description: "Erfahren Sie mehr über Distanzvektorprotokolle wie RIP, ihre Funktionsweise und ihre Einschränkungen für das Netzwerk-Routing. Verstehen Sie Hop-Count und Netzwerkeffizienz."
meta_keywords: "Distanzvektorprotokolle, RIP, Routing Information Protocol, Hop-Count, Netzwerk-Routing, Linux-Netzwerk, Anfängerleitfaden, Tutorial"
---

## Lesson Content

Distanzvektorprotokolle bestimmen den Pfad zu anderen Netzwerken anhand der Hop-Anzahl, die ein Paket über das Netzwerk nimmt. Wenn beispielsweise Netzwerk A 3 Hops entfernt ist und Netzwerk B neben Netzwerk A liegt, dann gehen wir davon aus, dass Netzwerk B 4 Hops entfernt sein muss. Bei Distanzvektorprotokollen wäre die nächste Route diejenige mit der geringsten Anzahl von Hops.

Distanzvektorprotokolle eignen sich hervorragend für kleine Netzwerke. Wenn Netzwerke jedoch skalieren, dauert es länger, bis die Router konvergieren, da sie die gesamte Routing-Tabelle periodisch an jeden Router senden. Ein weiterer Nachteil von Distanzvektorprotokollen ist die Effizienz; sie wählen Routen, die in Hops näher liegen, aber dies ist möglicherweise nicht immer die effizienteste Route.

Eines der gängigen Distanzvektorprotokolle ist RIP (Routing Information Protocol). Es sendet die Routing-Tabelle alle 30 Sekunden an jeden Router im Netzwerk. Für ein großes Netzwerk kann dies erhebliche Ressourcen verbrauchen. Aus diesem Grund begrenzt RIP seine Hop-Anzahl auf 15.

## Exercise

Übung macht den Meister! Hier sind einige praktische Übungen, um Ihr Verständnis von Netzwerk-Routing und Konnektivität zu vertiefen:

1. **[Erkunden Sie die Interaktion der Netzwerkschicht mit ping und arp in Linux](https://labex.io/de/labs/linux-explore-network-layer-interaction-with-ping-and-arp-in-linux-592746)** – Üben Sie die Verwendung von `ping` und `arp`, um zu verstehen, wie Geräte einander erkennen und wie der Datenverkehr auf der Netzwerkschicht geroutet wird.
2. **[Simulieren Sie die Konnektivität der Netzwerkschicht in Linux](https://labex.io/de/labs/linux-simulate-network-layer-connectivity-in-linux-592752)** – Lernen Sie, IP-Adressen zuzuweisen und die Konnektivität zwischen simulierten Linux-Knoten zu testen, wobei Sie beobachten, wie IP-Subnetze die Netzwerkkommunikation beeinflussen.
3. **[Verwalten Sie die IP-Adressierung in Linux](https://labex.io/de/labs/linux-manage-ip-addressing-in-linux-592736)** – Sammeln Sie praktische Erfahrungen beim Konfigurieren statischer und dynamischer IP-Adressen und beim Festlegen von Standard-Gateways, die wesentliche Komponenten des Netzwerk-Routings sind.

Diese Übungen helfen Ihnen, die Konzepte der Netzwerkadressierung und Konnektivität in realen Szenarien anzuwenden und eine starke Grundlage für das Verständnis der Funktionsweise von Routing-Protokollen zu schaffen.

## Quiz Question

Wahr oder falsch: Distanzvektorprotokolle verwenden die Route mit der geringsten Bandbreite?

## Quiz Answer

False
