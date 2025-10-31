---
index: 8
lang: "de"
title: "Link-Schicht"
meta_title: "Link-Schicht - Netzwerk-Grundlagen"
meta_description: "Erkunden Sie die Grundlagen der TCP/IP-Link-Schicht. Erfahren Sie, wie der Link-Schicht-Header aufgebaut ist, wie ARP IP-Adressen in MAC-Adressen auflöst und wie Pakete in einem lokalen Netzwerk übertragen werden."
meta_keywords: "Link-Schicht, Link-Schicht-Header, ARP, TCP/IP, MAC-Adresse, Netzwerk-Grundlagen, Linux-Netzwerk, Paketübertragung, Adressauflösungsprotokoll"
---

## Lesson Content

Die **Sicherungsschicht** (Link Layer) ist die grundlegende Schicht des TCP/IP-Modells und verantwortlich für die Kommunikation im lokalen Netzwerksegment. Diese Schicht ist hardwareabhängig und befasst sich direkt mit Netzwerkschnittstellenkarten und physischer Adressierung.

### Frames und der Sicherungsschicht-Header

Auf der **Sicherungsschicht** wird das Paket aus der Vermittlungsschicht in eine Struktur namens Frame eingekapselt. Ein entscheidender Teil dieses Prozesses ist das Hinzufügen des **Sicherungsschicht-Headers**. Dieser Header enthält die Quell- und Ziel-MAC-Adressen der Hosts, Prüfsummen zur Fehlererkennung und Paket-Trennzeichen, die es dem empfangenden Gerät ermöglichen, zu erkennen, wo ein Frame endet und der nächste beginnt.

Um den **Sicherungsschicht-Header** zu erstellen, benötigt das System sowohl die Quell- als auch die Ziel-MAC-Adresse. Während die Quell-MAC-Adresse bekannt ist, muss die Ziel-MAC-Adresse für eine IP-Adresse im selben lokalen Netzwerk ermittelt werden. Hier kommt das Address Resolution Protocol (ARP) ins Spiel.

### ARP (Address Resolution Protocol)

ARP ist ein Protokoll der **Sicherungsschicht**, das verwendet wird, um die MAC-Adresse zu finden, die mit einer bestimmten IP-Adresse im selben Netzwerk verbunden ist. Befände sich der Zielhost in einem anderen Netzwerk, würde das Paket an ein Standard-Gateway (Router) gesendet, und ARP würde verwendet, um die MAC-Adresse des Routers zu finden.

Systeme konsultieren zuerst ihre ARP-Lookup-Tabelle, die bekannte IP-zu-MAC-Adress-Mappings zwischenspeichert. Wenn die erforderliche Adresse nicht im Cache vorhanden ist, sendet das System eine ARP-Anfrage an das gesamte Netzwerk. Diese spezielle Nachricht fragt, welcher Host eine bestimmte IP-Adresse besitzt, zum Beispiel 10.10.1.4. Der Host mit dieser IP-Adresse sendet eine ARP-Antwort, die seine IP- und MAC-Adresse enthält.

Mit allen notwendigen IP- und MAC-Adressen kann die **Sicherungsschicht** den Frame nun über die Netzwerkschnittstellenkarte weiterleiten. Die Reise eines Pakets ist ein mehrstufiger Prozess der Kapselung und Dekapselung, während es sich am sendenden und empfangenden Ende den TCP/IP-Stack auf und ab bewegt.

### Paketdurchlauf (Packet Traversal)

Hier ist eine schrittweise Aufschlüsselung, wie ein Paket von einem Sender (Pete) zu einem Empfänger (Patty) gelangt:

1. Pete sendet Patty eine E-Mail. Diese Daten werden an die Transportschicht gesendet.
2. Die Transportschicht kapselt die Daten in einen TCP- oder UDP-Header ein, um ein Segment zu bilden. Sie fügt die Ziel- und Quellports hinzu und sendet das Segment an die Vermittlungsschicht.
3. Die Vermittlungsschicht kapselt das Segment in ein IP-Paket ein und fügt die Quell- und Ziel-IP-Adressen hinzu. Anschließend leitet sie das Paket an die **Sicherungsschicht** weiter.
4. Das Paket erreicht die **Sicherungsschicht**, wo es in einen Frame eingekapselt wird. Der **Sicherungsschicht-Header**, der die Quell- und Ziel-MAC-Adressen enthält, wird hinzugefügt.
5. Patty empfängt diesen Datenframe über ihre physikalische Schicht, prüft den Frame auf Datenintegrität, de-kapselt ihn und sendet das IP-Paket an ihre Vermittlungsschicht.
6. Die Vermittlungsschicht liest das Paket, um die Quell- und Ziel-IP-Adressen zu ermitteln. Sie bestätigt, dass die Ziel-IP mit ihrer eigenen übereinstimmt, de-kapselt das Paket und sendet das Segment an die Transportschicht.
7. Die Transportschicht de-kapselt das Segment, prüft die TCP- oder UDP-Portnummern und stellt basierend auf diesen Ports eine Verbindung zur Anwendungsschicht her.
8. Die Anwendungsschicht empfängt die Daten von der Transportschicht am angegebenen Port und präsentiert sie Patty als endgültige E-Mail-Nachricht.

## Exercise

Übung macht den Meister! Hier sind einige praktische Laborübungen, um Ihr Verständnis der Sicherungsschicht, von MAC-Adressen und ARP zu festigen:

1. **[MAC- und IP-Adressen in Linux identifizieren](https://labex.io/de/labs/comptia-identify-mac-and-ip-addresses-in-linux-592731)** – Üben Sie die Verwendung des Befehls `ip a`, um Informationen zur Netzwerkadressierung, einschließlich MAC-Adressen, auf einem Linux-System zu identifizieren.
2. **[Interaktion der Vermittlungsschicht mit ping und arp in Linux untersuchen](https://labex.io/de/labs/comptia-explore-network-layer-interaction-with-ping-and-arp-in-linux-592746)** – Lernen Sie, wie die Befehle `ping` und `arp` zusammenarbeiten, um IP-Adressen in MAC-Adressen aufzulösen, und verstehen Sie die Interaktionen der Vermittlungsschicht.
3. **[Ethernet-Frames mit tcpdump in Linux analysieren](https://labex.io/de/labs/comptia-analyze-ethernet-frames-with-tcpdump-in-linux-592765)** – Sammeln Sie praktische Erfahrungen beim Erfassen und Inspizieren von Ethernet-Frames, einschließlich MAC-Adressen, um die Netzwerkkommunikation auf niedriger Ebene zu verstehen.

Diese Labs helfen Ihnen, die Konzepte in realen Szenarien anzuwenden und Vertrauen in die Grundlagen der Netzwerke auf der Sicherungsschicht aufzubauen.

## Quiz Question

Welches Protokoll wird verwendet, um die MAC-Adresse eines Hosts im selben lokalen Netzwerk zu finden? (Bitte antworten Sie mit dem englischen Akronym in Großbuchstaben).

## Quiz Answer

ARP
