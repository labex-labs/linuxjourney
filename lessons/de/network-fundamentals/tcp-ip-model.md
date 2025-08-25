---
index: 3
lang: "de"
title: "TCP/IP-Modell"
meta_title: "TCP/IP-Modell - Netzwerk-Grundlagen"
meta_description: "Erfahren Sie mehr über die Schichten des TCP/IP-Modells: Anwendung, Transport, Netzwerk und Verbindung. Verstehen Sie, wie Daten über Netzwerke übertragen werden. Beginnen Sie Ihre Linux-Netzwerkreise!"
meta_keywords: "TCP/IP-Modell, Netzwerk-Grundlagen, Linux-Netzwerk, TCP, IP, Anfänger-Tutorial, Netzwerkschichten, Leitfaden"
---

## Lesson Content

Das OSI-Modell brachte das hervor, was schließlich zum TCP/IP-Modell wurde, und dieses Modell ist tatsächlich die Grundlage des Internets. Es ist die eigentliche Implementierung der Vernetzung. Das TCP/IP-Modell verwendet die TCP/IP-Protokollsuite, die wir gemeinhin als TCP/IP bezeichnen. Diese Protokolle arbeiten zusammen, um festzulegen, wie Daten gesammelt, adressiert, übertragen und durch ein Netzwerk geleitet werden sollen. Anhand des TCP/IP-Modells können wir sehen, wie diese Protokolle verwendet werden, um den Ablauf der Paketübertragung durch das Netzwerk darzustellen.

### Anwendungsschicht

Die oberste Schicht des TCP/IP-Modells. Sie bestimmt, wie die Programme Ihres Computers (wie Ihr Webbrowser) mit den Diensten der Transportschicht interagieren, um die gesendeten oder empfangenen Daten anzuzeigen.

Diese Schicht verwendet:

- HTTP (Hypertext Transfer Protocol) – wird für Webseiten im Internet verwendet.
- SMTP (Simple Mail Transfer Protocol) – Übertragung elektronischer Post (E-Mail)

### Transportschicht

Wie Daten übertragen werden, einschließlich der Überprüfung der richtigen Ports, der Datenintegrität und im Grunde der Zustellung unserer Pakete.

Diese Schicht verwendet:

- TCP (Transmission Control Protocol) – zuverlässige Datenübertragung
- UDP (User Datagram Protocol) – unzuverlässige Datenübertragung

### Netzwerkschicht

Diese Schicht legt fest, wie Pakete zwischen Hosts und über Netzwerke bewegt werden.

Diese Schicht verwendet:

- IP (Internet Protocol) – Hilft beim Routing von Paketen von einer Maschine zur anderen.
- ICMP (Internet Control Message Protocol) – Hilft uns zu erkennen, was vor sich geht, z. B. Fehlermeldungen und Debugging-Informationen.

### Verbindungsschicht

Diese Schicht legt fest, wie Daten über ein physisches Hardwareteil gesendet werden, z. B. Daten, die über Ethernet, Glasfaser usw. übertragen werden.

Die oben genannten Listen der von jeder Schicht verwendeten Protokolle sind nicht vollständig, und Sie werden auf viele andere Protokolle stoßen, die ins Spiel kommen.

In den folgenden Lektionen werden wir jede dieser Schichten durchgehen und besprechen, wie unser Paket aus Sicht des TCP/IP-Modells das Netzwerk durchquert (es gibt viele Perspektiven, wie ein Paket Netzwerke durchquert; wir werden nicht alle betrachten, aber seien Sie sich bewusst, dass sie existieren).

## Exercise

Übung macht den Meister! Hier sind einige praktische Übungen, um Ihr Verständnis des TCP/IP-Modells und der Netzwerk-Grundlagen zu vertiefen:

1. **[MAC- und IP-Adressen in Linux identifizieren](https://labex.io/de/labs/linux-identify-mac-and-ip-addresses-in-linux-592731)** – Üben Sie das Identifizieren wichtiger Netzwerkadressierungsinformationen wie MAC- und IP-Adressen mithilfe des Befehls `ip a`, der für das Verständnis der Netzwerk- und Datenverbindungsschichten des TCP/IP-Modells grundlegend ist.
2. **[Netzwerkschicht-Interaktion mit ping und arp in Linux erkunden](https://labex.io/de/labs/linux-explore-network-layer-interaction-with-ping-and-arp-in-linux-592746)** – Erfahren Sie, wie die Befehle `ping` und `arp` die Interaktion zwischen der Netzwerk- und Datenverbindungsschicht demonstrieren und praktische Einblicke in die Kommunikation von Geräten innerhalb des TCP/IP-Stacks geben.
3. **[Netzwerkschicht-Konnektivität in Linux simulieren](https://labex.io/de/labs/linux-simulate-network-layer-connectivity-in-linux-592752)** – Sammeln Sie praktische Erfahrungen beim Simulieren der Netzwerkkonnektivität zwischen Linux-Knoten, beim Zuweisen von IP-Adressen und beim Testen der Kommunikation, wobei Konzepte der Netzwerkschicht des TCP/IP-Modells direkt angewendet werden.

Diese Labs helfen Ihnen, die Konzepte des TCP/IP-Modells in realen Szenarien anzuwenden und Vertrauen in die Netzwerkkonfiguration und -fehlerbehebung aufzubauen.

## Quiz Question

Was ist die oberste Schicht des TCP/IP-Modells?

## Quiz Answer

Application
