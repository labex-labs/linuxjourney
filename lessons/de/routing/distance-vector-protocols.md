---
index: 5
lang: "de"
title: "Distanzvektorprotokolle"
meta_title: "Distanzvektorprotokolle - Routing"
meta_description: "Ein Leitfaden für Anfänger zu Distanzvektorprotokollen im Netzwerk-Routing. Dieses Tutorial erklärt, wie Protokolle wie RIP die Hops zur Routenbestimmung verwenden und behandelt deren Einschränkungen für modernes Linux-Networking."
meta_keywords: "Distanzvektorprotokolle, Netzwerk-Routing, RIP, Routing Information Protocol, Hop-Zahl, Linux-Networking, Anfängerleitfaden, Tutorial"
---

## Lesson Content

Distanzvektorprotokolle sind eine grundlegende Kategorie von Routing-Protokollen, die in Computernetzwerken verwendet werden. Sie bestimmen den besten Pfad für Datenpakete basierend auf der Distanz, die typischerweise durch die **Hop-Anzahl** gemessen wird. Bei dieser Art von **Netzwerk-Routing** pflegt jeder Router eine Tabelle der „Distanz“ zu allen bekannten Netzwerken.

### Wie Distanzvektorprotokolle funktionieren

Das Kernprinzip eines Distanzvektorprotokolls ist einfach: Router teilen ihre Routing-Informationen mit ihren unmittelbaren Nachbarn. Dieser Vorgang wird manchmal als „Routing durch Gerüchte“ bezeichnet. Wenn Router A beispielsweise weiß, dass er 3 Hops vom Netzwerk X entfernt ist, und Router B ein direkter Nachbar von Router A ist, kann Router B ableiten, dass er über Router A 4 Hops vom Netzwerk X entfernt ist. Wenn mehrere Pfade zum selben Ziel existieren, wählt das Protokoll immer den Pfad mit der niedrigsten **Hop-Anzahl**.

### Vor- und Nachteile

**Distanzvektorprotokolle** sind einfach zu konfigurieren und funktionieren gut in kleinen, stabilen Netzwerken. Sie weisen jedoch erhebliche Einschränkungen auf, die sie für größere, komplexere Umgebungen weniger geeignet machen.

Ein großer Nachteil ist die langsame Konvergenz. Router senden ihre gesamte Routing-Tabelle periodisch an ihre Nachbarn, was, insbesondere wenn das Netzwerk wächst, erheblichen Bandbreiten- und Rechenaufwand verursachen kann. Wenn eine Netzwerkänderung auftritt, kann es lange dauern, bis diese Information alle Router erreicht.

Ein weiterer wesentlicher Nachteil ist, dass der kürzeste Pfad in Bezug auf die **Hop-Anzahl** nicht immer der effizienteste ist. Ein Pfad mit weniger Hops kann langsamere Verbindungen aufweisen (z. B. 10 Mbit/s) im Vergleich zu einem Pfad mit mehr Hops, der schnellere Verbindungen nutzt (z. B. 1 Gbit/s). Distanzvektorprotokolle sind sich im Allgemeinen der Link-Geschwindigkeit nicht bewusst, was zu suboptimalen Routing-Entscheidungen führt.

### RIP als gängiges Beispiel

Eines der bekanntesten **Distanzvektorprotokolle** ist das **Routing Information Protocol (RIP)**. Es ist ein klassisches Beispiel, das die Prinzipien und Einschränkungen dieser Protokollfamilie klar demonstriert.

- **Periodische Updates:** RIP sendet seine gesamte Routing-Tabelle alle 30 Sekunden an alle Nachbarn.
- **Hop-Anzahl-Limit:** Um Routing-Schleifen zu verhindern und den Netzwerkverkehr zu steuern, erzwingt RIP eine maximale **Hop-Anzahl** von 15. Jeder Pfad, der 16 Hops erfordert, wird als unerreichbar betrachtet.

Aufgrund dieser Eigenschaften wird RIP in modernen Produktionsnetzwerken selten eingesetzt, dient aber als ausgezeichnetes Lernwerkzeug in einem **Anfängerleitfaden** zu **Linux-Netzwerken** und Routing-Konzepten.

## Exercise

Übung macht den Meister! Hier sind einige praktische Labs, um Ihr Verständnis von Netzwerk-Routing und Konnektivität zu festigen:

1. **[Netzwerkschicht-Interaktion mit ping und arp in Linux erkunden](https://labex.io/de/labs/comptia-explore-network-layer-interaction-with-ping-and-arp-in-linux-592746)** – Üben Sie die Verwendung von `ping` und `arp`, um zu verstehen, wie Geräte sich gegenseitig entdecken und wie der Verkehr auf der Netzwerkschicht geroutet wird.
2. **[Netzwerkschicht-Konnektivität in Linux simulieren](https://labex.io/de/labs/comptia-simulate-network-layer-connectivity-in-linux-592752)** – Lernen Sie, IP-Adressen zuzuweisen und die Konnektivität zwischen simulierten Linux-Knoten zu testen, wobei Sie beobachten, wie IP-Subnetze die Netzwerkkommunikation beeinflussen.
3. **[IP-Adressierung in Linux verwalten](https://labex.io/de/labs/comptia-manage-ip-addressing-in-linux-592736)** – Sammeln Sie praktische Erfahrungen bei der Konfiguration statischer und dynamischer IP-Adressen sowie beim Festlegen von Standard-Gateways, die wesentliche Bestandteile des Netzwerk-Routings sind.

Diese Labs helfen Ihnen, die Konzepte der Netzwerkadressierung und Konnektivität in realen Szenarien anzuwenden und eine solide Grundlage für das Verständnis der Funktionsweise von Routing-Protokollen aufzubauen.

## Quiz Question

Richtig oder falsch: Distanzvektorprotokolle verwenden die Route mit der geringsten Bandbreite?

## Quiz Answer

False
