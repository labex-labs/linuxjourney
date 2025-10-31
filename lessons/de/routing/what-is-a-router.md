---
index: 1
lang: "de"
title: "Was ist ein Router?"
meta_title: "Was ist ein Router? - Routing"
meta_description: "Ein Leitfaden für Anfänger, um zu verstehen, was ein Router im Netzwerkbereich ist. Erfahren Sie mehr über Routing, Paketvermittlung, Hops und wie Router Routing-Tabellen zur Weiterleitung von Daten über Netzwerke verwenden. Dieser Netzwerk-Guide ist essenziell für das Erlernen von Linux-Netzwerken."
meta_keywords: "Router, Netzwerk, Routing, Hops, Paketvermittlung, Linux-Netzwerke, Anfänger-Tutorial, Netzwerk-Guide"
---

## Lesson Content

Ein Router ist ein fundamentales Gerät in der Computervernetzung. Wahrscheinlich haben Sie einen zu Hause, der Sie mit dem Internet verbindet. Seine Hauptaufgabe besteht darin, Geräten in einem Netzwerk die Kommunikation untereinander und mit anderen Netzwerken zu ermöglichen. Dieser Prozess ist ein Kernbestandteil dessen, was das Internet und lokale Netzwerke funktionsfähig macht.

### Die Kernfunktion eines Routers

Ein typischer Heimrouter verfügt über LAN-Anschlüsse (Local Area Network) zur Verbindung Ihrer Geräte mit einem lokalen Netzwerk und einen WAN-Anschluss (Wide Area Network), der eine Internetverbindung bereitstellt. Jedes Datenstück, oder „Paket“, das Sie bei Netzwerkaktivitäten senden oder empfangen, muss den Router passieren. Der Router untersucht diese Netzwerkpakete und entscheidet, wohin sie gesendet werden sollen. Er leitet den Verkehr effektiv zwischen mehreren Netzwerken und stellt sicher, dass jedes Paket von seiner Quelle zu seinem endgültigen Ziel gelangt.

### Der Routing-Prozess

Stellen Sie sich den Routing-Prozess wie die Postzustellung vor. Wenn Sie einen Brief senden, ermittelt die Post das allgemeine Ziel (z. B. ein Bundesland oder eine Stadt) und sendet ihn dorthin. Von dort aus wird er in kleinere Regionen wie Postleitzahlen sortiert, bis er schließlich die spezifische Straßenadresse erreicht.

In der Netzwerktechnik verwendet ein Router eine **Routing-Tabelle**, um diese Entscheidungen zu treffen. Diese Tabelle enthält eine Reihe von Regeln oder Routen, die dem Router mitteilen, wie Pakete an ein bestimmtes Netzwerkziel weitergeleitet werden sollen. Eine Regel könnte beispielsweise lauten: „Um zu Netzwerk A zu gelangen, senden Sie Pakete an Router B.“ Wenn es keine spezifische Regel für ein Ziel gibt, verwendet der Router eine **Standardroute**, die den Verkehr normalerweise in Richtung Internet leitet. Dieses System ist sowohl in einfachen Heimnetzwerken als auch in komplexen **Linux-Netzwerkumgebungen** von entscheidender Bedeutung.

### Hops

Während Pakete Netzwerke durchqueren, wird ihre Reise in **Hops** gemessen. Ein Hop stellt einen Schritt der Reise dar, bei dem ein Paket ein Zwischengerät, wie einen Router, passiert. Wenn ein Paket beispielsweise zwei Router passieren muss, um von Host A zu Host B zu gelangen, sagen wir, der Pfad ist zwei Hops lang. Hops bieten eine einfache Metrik zur Messung der Entfernung zwischen einer Quelle und einem Ziel in einem Netzwerk.

### Paketvermittlung, Routing und Flooding

Um zu verstehen, wie Daten übertragen werden, ist es hilfreich, diese verwandten Begriffe zu kennen:

- **Paketvermittlung (Packet Switching)** ist die grundlegende Methode zum Empfangen, Verarbeiten und Weiterleiten von Datenpaketen an ihr Ziel. Dies ist das, was Router kontinuierlich tun.
- **Routing** ist der intelligente Prozess des Erstellens und Pflegens der Routing-Tabelle. Effektives Routing ermöglicht eine effizientere und zuverlässigere Paketvermittlung.
- **Flooding** ist eine ältere, weniger effiziente Methode, die verwendet wird, wenn ein Router nicht weiß, wohin er ein Paket senden soll. Er sendet das eingehende Paket über jede Verbindung außer der, über die es angekommen ist, in der Hoffnung, dass eines das Ziel erreicht. Moderne Netzwerke verlassen sich auf Routing, um diese Art von Ineffizienz zu vermeiden.

## Exercise

Übung macht den Meister! Hier sind einige praktische Labs, um Ihr Verständnis von Netzwerkverbindungen und Routing zu festigen:

1. **[IP-Adresstypen und Erreichbarkeit in Linux erkunden](https://labex.io/de/labs/comptia-explore-ip-address-types-and-reachability-in-linux-592780)** – Üben Sie das Testen des lokalen TCP/IP-Stacks, das Identifizieren privater und öffentlicher IPs und das Überprüfen der Netzwerkerreichbarkeit, was entscheidend ist, um zu verstehen, wie ein Router die Kommunikation ermöglicht.
2. **[Interaktion der Netzwerkschicht mit ping und arp in Linux erkunden](https://labex.io/de/labs/comptia-explore-network-layer-interaction-with-ping-and-arp-in-linux-592746)** – Lernen Sie, wie die Befehle `ping` und `arp` Ihnen helfen zu beobachten, wie die Netzwerk- und Datenverbindungsschichten interagieren und wie das Standard-Gateway (Router) den Verkehr zu entfernten Zielen verarbeitet.
3. **[Netzwerkschicht-Konnektivität in Linux simulieren](https://labex.io/de/labs/comptia-simulate-network-layer-connectivity-in-linux-592752)** – Verwenden Sie Docker, um Netzwerkknoten zu simulieren und IP-Adressen zuzuweisen, und testen Sie dann die Konnektivität, um zu verstehen, wie IP-Subnetze und Routing die Netzwerkkommunikation steuern.

Diese Labs helfen Ihnen, die Konzepte der Netzwerkkommunikation, IP-Adressierung und die Rolle des Routings in realen Szenarien anzuwenden und Vertrauen in die Netzwerk-Grundlagen aufzubauen.

## Quiz Question

Wie wird die Entfernung von Paketen gemessen? (Bitte antworten Sie auf Englisch. Die Antwort ist groß- und kleingeschrieben.)

## Quiz Answer

Hops
