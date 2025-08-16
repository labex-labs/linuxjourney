---
title: "Link Layer"
description: "Erfahren Sie mehr über die Link Layer in TCP/IP, wie ARP MAC-Adressen auflöst und die Paketdurchquerung. Verstehen Sie die Grundlagen des Netzwerks mit diesem Linux-Netzwerk-Tutorial."
keywords: "Link Layer, ARP, TCP/IP, MAC-Adresse, Netzwerk-Grundlagen, Linux-Netzwerk, Anfänger, Tutorial"
---

## Lesson Content

Am unteren Ende des TCP/IP-Modells befindet sich die Link Layer. Diese Schicht ist hardwarespezifisch.

In der Link Layer wird unser Paket noch einmal in etwas namens Frame gekapselt. Der Frame-Header fügt die Quell- und Ziel-MAC-Adressen unserer Hosts, Prüfsummen und Paket-Separatoren hinzu, damit der Empfänger erkennen kann, wann ein Paket endet.

Glücklicherweise befinden wir uns im selben Netzwerk, sodass unser Paket nicht zu weit reisen muss. Zuerst fügt die Link Layer meine Quell-MAC-Adresse dem Frame-Header hinzu, aber sie muss auch Pattys MAC-Adresse kennen. Woher weiß sie das, und wie finde ich sie, da sie nicht im Internet ist? Wir verwenden ARP!

### ARP (Address Resolution Protocol)

ARP findet die MAC-Adresse, die einer IP-Adresse zugeordnet ist. ARP wird innerhalb desselben Netzwerks verwendet. Wenn Patty nicht im selben Netzwerk wäre, würden wir ein Routing-System verwenden, um den nächsten Router zu bestimmen, der das Paket empfangen würde, und sobald wir im selben Netzwerk wären, könnten wir ARP verwenden.

Sobald wir uns im selben Netzwerk befinden, verwenden Systeme zuerst die ARP-Nachschlagetabelle, die Informationen darüber speichert, welche IP-Adressen welcher MAC-Adresse zugeordnet sind. Wenn der Wert dort nicht vorhanden ist, wird ARP verwendet. Dann sendet das System eine Broadcast-Nachricht an das Netzwerk unter Verwendung des ARP-Protokolls, um herauszufinden, welcher Host die IP 10.10.1.4 hat. Eine Broadcast-Nachricht ist eine spezielle Nachricht, die an alle Hosts in einem Netzwerk gesendet wird (passenderweise als Broadcast bezeichnet). Jede Maschine mit der angeforderten IP-Adresse antwortet mit einem ARP-Paket, das die IP-Adresse und die MAC-Adresse enthält.

Nachdem wir nun alle notwendigen Daten haben – IP-Adresse und MAC-Adressen – leitet unsere Link Layer diesen Frame über unsere Netzwerkschnittstellenkarte an das nächste Gerät weiter und findet Pattys Netzwerk. Dieser Schritt ist etwas komplexer, als ich es gerade erklärt habe, aber wir werden im Routing-Kurs weitere Details besprechen.

Und da ist es: eine einfache (oder nicht ganz so einfache) Paketdurchquerung durch die TCP/IP-Schicht. Beachten Sie, dass Pakete nicht einseitig reisen. Wir sind noch nicht einmal in Pattys Netzwerk angekommen! Beim Reisen durch Netzwerke muss das TCP/IP-Modell mindestens zweimal durchlaufen werden, bevor Daten gesendet oder empfangen werden. In Wirklichkeit würde dieses Paket etwa so aussehen:

### Packet Traversal

1. Pete sends Patty an email: this data gets sent to the transport layer.
2. The transport layer encapsulates the data into a TCP or UDP header to form a segment. The segment attaches the destination and source TCP or UDP port, then the segment is sent to the network layer.
3. The network layer encapsulates the TCP segment inside an IP packet; it attaches the source and destination IP address. Then it routes the packet to the link layer.
4. The packet then reaches Pete's physical hardware and gets encapsulated in a frame. The source and destination MAC addresses get added to the frame.
5. Patty receives this data frame through her physical layer and checks each frame for data integrity, then de-encapsulates the frame contents and sends the IP packet to the network layer.
6. The network layer reads the packet to find the source and destination IP that was previously attached. It checks if its IP is the same as the destination IP, which it is! It de-encapsulates the packet and sends the segment to the transport layer.
7. The transport layer de-encapsulates the segments, checks the TCP or UDP port numbers, and makes a connection to the application layer based on those port numbers.
8. The application layer receives the data from the transport layer on the port that was specified and presents it to Patty in the form of the final email message.

## Exercise

No exercises for this lesson.

## Quiz Question

Was wird verwendet, um die MAC-Adresse im selben Netzwerk zu finden?

## Quiz Answer

ARP
