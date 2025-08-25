---
index: 8
lang: "de"
title: "Link Layer"
meta_title: "Link Layer - Netzwerk-Grundlagen"
meta_description: "Erfahren Sie mehr über die Link Layer in TCP/IP, wie ARP MAC-Adressen auflöst und die Paketdurchquerung. Verstehen Sie die Netzwerk-Grundlagen mit diesem Linux-Netzwerk-Tutorial."
meta_keywords: "Link Layer, ARP, TCP/IP, MAC-Adresse, Netzwerk-Grundlagen, Linux-Netzwerk, Anfänger, Tutorial"
---

## Lesson Content

Am unteren Ende des TCP/IP-Modells befindet sich die Link Layer. Diese Schicht ist hardwarespezifisch.

In der Link Layer wird unser Paket noch einmal in etwas namens Frame gekapselt. Der Frame-Header fügt die Quell- und Ziel-MAC-Adressen unserer Hosts, Prüfsummen und Paket-Separatoren hinzu, damit der Empfänger erkennen kann, wann ein Paket endet.

Glücklicherweise befinden wir uns im selben Netzwerk, sodass unser Paket nicht zu weit reisen muss. Zuerst fügt die Link Layer meine Quell-MAC-Adresse dem Frame-Header hinzu, aber sie muss auch Pattys MAC-Adresse kennen. Woher weiß sie das, und wie finde ich sie, da sie nicht im Internet ist? Wir verwenden ARP!

### ARP (Address Resolution Protocol)

ARP findet die MAC-Adresse, die einer IP-Adresse zugeordnet ist. ARP wird innerhalb desselben Netzwerks verwendet. Wenn Patty nicht im selben Netzwerk wäre, würden wir ein Routing-System verwenden, um den nächsten Router zu bestimmen, der das Paket empfangen würde, und sobald wir im selben Netzwerk wären, könnten wir ARP verwenden.

Sobald wir uns im selben Netzwerk befinden, verwenden Systeme zuerst die ARP-Lookup-Tabelle, die Informationen darüber speichert, welche IP-Adressen welcher MAC-Adresse zugeordnet sind. Wenn der Wert nicht vorhanden ist, wird ARP verwendet. Dann sendet das System eine Broadcast-Nachricht an das Netzwerk unter Verwendung des ARP-Protokolls, um herauszufinden, welcher Host die IP 10.10.1.4 hat. Eine Broadcast-Nachricht ist eine spezielle Nachricht, die an alle Hosts in einem Netzwerk gesendet wird (passend benannt für das Senden einer Übertragung). Jede Maschine mit der angeforderten IP-Adresse antwortet mit einem ARP-Paket, das die IP-Adresse und die MAC-Adresse enthält.

Nachdem wir nun alle notwendigen Daten haben – IP-Adresse und MAC-Adressen – leitet unsere Link Layer diesen Frame über unsere Netzwerkschnittstellenkarte an das nächste Gerät weiter und findet Pattys Netzwerk. Dieser Schritt ist etwas komplexer, als ich es gerade erklärt habe, aber wir werden weitere Details im Routing-Kurs besprechen.

Und da ist es: eine einfache (oder nicht ganz so einfache) Paketdurchquerung durch die TCP/IP-Schicht. Beachten Sie, dass Pakete nicht einseitig reisen. Wir sind noch nicht einmal in Pattys Netzwerk angekommen! Beim Reisen durch Netzwerke muss das TCP/IP-Modell mindestens zweimal durchlaufen werden, bevor Daten gesendet oder empfangen werden. In Wirklichkeit würde dieses Paket etwa so aussehen:

### Paketdurchquerung

1. Pete sendet Patty eine E-Mail: Diese Daten werden an die Transportschicht gesendet.
2. Die Transportschicht kapselt die Daten in einen TCP- oder UDP-Header, um ein Segment zu bilden. Das Segment fügt den Ziel- und Quell-TCP- oder UDP-Port hinzu, dann wird das Segment an die Netzwerkschicht gesendet.
3. Die Netzwerkschicht kapselt das TCP-Segment in ein IP-Paket; sie fügt die Quell- und Ziel-IP-Adresse hinzu. Dann leitet sie das Paket an die Link Layer weiter.
4. Das Paket erreicht dann Petes physische Hardware und wird in einen Frame gekapselt. Die Quell- und Ziel-MAC-Adressen werden dem Frame hinzugefügt.
5. Patty empfängt diesen Datenframe über ihre physische Schicht und überprüft jeden Frame auf Datenintegrität, entkapselt dann den Frame-Inhalt und sendet das IP-Paket an die Netzwerkschicht.
6. Die Netzwerkschicht liest das Paket, um die zuvor angehängte Quell- und Ziel-IP zu finden. Sie überprüft, ob ihre IP mit der Ziel-IP übereinstimmt, was der Fall ist! Sie entkapselt das Paket und sendet das Segment an die Transportschicht.
7. Die Transportschicht entkapselt die Segmente, überprüft die TCP- oder UDP-Portnummern und stellt eine Verbindung zur Anwendungsschicht basierend auf diesen Portnummern her.
8. Die Anwendungsschicht empfängt die Daten von der Transportschicht am angegebenen Port und präsentiert sie Patty in Form der endgültigen E-Mail-Nachricht.

## Exercise

Übung macht den Meister! Hier sind einige praktische Übungen, um Ihr Verständnis der Link Layer, MAC-Adressen und ARP zu vertiefen:

1. **[MAC- und IP-Adressen in Linux identifizieren](https://labex.io/de/labs/linux-identify-mac-and-ip-addresses-in-linux-592731)** – Üben Sie die Verwendung des Befehls `ip a`, um Netzwerkinformationen, einschließlich MAC-Adressen, auf einem Linux-System zu identifizieren.
2. **[Netzwerkschicht-Interaktion mit ping und arp in Linux erkunden](https://labex.io/de/labs/linux-explore-network-layer-interaction-with-ping-and-arp-in-linux-592746)** – Erfahren Sie, wie die Befehle `ping` und `arp` zusammenarbeiten, um IP-Adressen in MAC-Adressen aufzulösen und Netzwerkschicht-Interaktionen zu verstehen.
3. **[Ethernet-Frames mit tcpdump in Linux analysieren](https://labex.io/de/labs/linux-analyze-ethernet-frames-with-tcpdump-in-linux-592765)** – Sammeln Sie praktische Erfahrungen beim Erfassen und Überprüfen von Ethernet-Frames, einschließlich MAC-Adressen, um Low-Level-Netzwerkkommunikation zu verstehen.

Diese Labs helfen Ihnen, die Konzepte in realen Szenarien anzuwenden und Vertrauen in die Netzwerk-Grundlagen auf der Link Layer aufzubauen.

## Quiz Question

Was wird verwendet, um die MAC-Adresse im selben Netzwerk zu finden?

## Quiz Answer

ARP
