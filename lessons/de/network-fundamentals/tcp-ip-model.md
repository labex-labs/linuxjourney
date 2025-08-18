---
lang: "de"
title: "TCP/IP-Modell"
meta_title: "TCP/IP-Modell - Netzwerkgrundlagen"
meta_description: "Erfahren Sie mehr über die Schichten des TCP/IP-Modells: Anwendung, Transport, Netzwerk und Verbindung. Verstehen Sie, wie Daten über Netzwerke übertragen werden. Beginnen Sie Ihre Reise in die Linux-Netzwerktechnik!"
meta_keywords: "TCP/IP-Modell, Grundlagen der Netzwerktechnik, Linux-Netzwerktechnik, TCP, IP, Anfänger-Tutorial, Netzwerkschichten, Leitfaden"
---

## Lesson Content

Das OSI-Modell brachte hervor, was schließlich zum TCP/IP-Modell wurde, und dieses Modell ist tatsächlich die Grundlage des Internets. Es ist die eigentliche Implementierung der Vernetzung. Das TCP/IP-Modell verwendet die TCP/IP-Protokollsuite, die wir gemeinhin als TCP/IP bezeichnen. Diese Protokolle arbeiten zusammen, um festzulegen, wie Daten gesammelt, adressiert, übertragen und durch ein Netzwerk geleitet werden sollen. Mithilfe des TCP/IP-Modells können wir sehen, wie diese Protokolle verwendet werden, um die Aufschlüsselung der Paketübertragung durch das Netzwerk zu zeigen.

### Application Layer

Die oberste Schicht des TCP/IP-Modells. Sie bestimmt, wie die Programme Ihres Computers (wie Ihr Webbrowser) mit den Diensten der Transportschicht interagieren, um die gesendeten oder empfangenen Daten anzuzeigen.

Diese Schicht verwendet:

- HTTP (Hypertext Transfer Protocol) – wird für Webseiten im Internet verwendet.
- SMTP (Simple Mail Transfer Protocol) – Übertragung elektronischer Post (E-Mail)

### Transport Layer

Wie Daten übertragen werden, einschließlich der Überprüfung der korrekten Ports, der Datenintegrität und im Grunde der Zustellung unserer Pakete.

Diese Schicht verwendet:

- TCP (Transmission Control Protocol) – zuverlässige Datenübertragung
- UDP (User Datagram Protocol) – unzuverlässige Datenübertragung

### Network Layer

Diese Schicht legt fest, wie Pakete zwischen Hosts und über Netzwerke bewegt werden.

Diese Schicht verwendet:

- IP (Internet Protocol) – Hilft beim Routing von Paketen von einer Maschine zur anderen.
- ICMP (Internet Control Message Protocol) – Hilft uns zu sagen, was vor sich geht, wie Fehlermeldungen und Debugging-Informationen.

### Link Layer

Diese Schicht legt fest, wie Daten über ein physisches Hardwarestück gesendet werden, z. B. Daten, die über Ethernet, Glasfaser usw. übertragen werden.

Die oben genannten Listen der von jeder Schicht verwendeten Protokolle sind nicht vollständig, und Sie werden auf viele andere Protokolle stoßen, die ins Spiel kommen.

In den folgenden Lektionen werden wir jede dieser Schichten durchgehen und besprechen, wie unser Paket aus Sicht des TCP/IP-Modells das Netzwerk durchläuft (es gibt viele Perspektiven, wie ein Paket über Netzwerke reist; wir werden nicht alle betrachten, aber seien Sie sich bewusst, dass sie existieren).

## Exercise

No exercises for this lesson.

## Quiz Question

Was ist die oberste Schicht des TCP/IP-Modells?

## Quiz Answer

Application
