---
title: "Transportschicht"
description: "Erfahren Sie mehr über die Transportschicht im Linux-Netzwerk, einschließlich TCP/UDP-Protokollen, Ports und Datensegmentierung. Verstehen Sie, wie Daten zuverlässig übertragen werden."
keywords: "Linux Transportschicht, TCP/UDP, Netzwerk-Ports, Datensegmentierung, Linux-Netzwerk, Anfänger-Tutorial, Netzwerkprotokolle"
---

## Lesson Content

Die Transportschicht hilft uns, unsere Daten so zu übertragen, dass Netzwerke sie lesen können. Sie zerlegt unsere Daten in Blöcke, die transportiert und in der richtigen Reihenfolge wieder zusammengesetzt werden. Diese Blöcke werden als Segmente bezeichnet. Segmente erleichtern den Datentransport über Netzwerke hinweg.

### Ports

Obwohl wir über IP-Adressen wissen, wohin wir unsere Daten senden, sind diese nicht spezifisch genug, um unsere Daten an bestimmte Prozesse oder Dienste zu senden. Dienste wie HTTP nutzen einen Kommunikationskanal über Ports. Wenn wir Webseiten-Daten senden möchten, müssen wir diese über den HTTP-Port (Port 80) senden. Zusätzlich zur Bildung von Segmenten fügt die Transportschicht dem Segment auch die Quell- und Ziel-Ports hinzu, sodass der Empfänger, wenn er das endgültige Paket erhält, weiß, welchen Port er verwenden muss.

### UDP

Es gibt zwei beliebte Transportprotokolle: UDP und TCP. Wir werden UDP kurz besprechen und die meiste Zeit TCP widmen, da es am häufigsten verwendet wird.

UDP ist keine zuverlässige Methode zum Transportieren von Daten; tatsächlich ist es ihm ziemlich egal, ob Sie alle Ihre ursprünglichen Daten erhalten. Das mag schrecklich klingen, aber es hat seine Anwendungen, wie zum Beispiel für Medien-Streaming. Es ist in Ordnung, wenn Sie einige Frames verlieren; im Gegenzug erhalten Sie Ihre Daten etwas schneller.

### TCP

TCP bietet einen zuverlässigen, verbindungsorientierten Datenstrom. TCP verwendet Ports, um Daten zu und von Hosts zu senden. Eine Anwendung öffnet eine Verbindung von einem Port auf ihrem Host zu einem anderen Port auf einem Remote-Host. Um die Verbindung herzustellen, verwenden wir den TCP-Handshake.

- Der Client (verbindender Prozess) sendet ein SYN-Segment an den Server, um eine Verbindung anzufordern.
- Der Server sendet dem Client ein SYN-ACK-Segment, um die Verbindungsanfrage des Clients zu bestätigen.
- Der Client sendet ein ACK an den Server, um die Verbindungsanfrage des Servers zu bestätigen.

Sobald diese Verbindung hergestellt ist, können Daten über eine TCP-Verbindung ausgetauscht werden. Die Daten werden in verschiedenen Segmenten gesendet und mit TCP-Sequenznummern verfolgt, damit sie bei der Zustellung in der richtigen Reihenfolge angeordnet werden können. In unserem E-Mail-Beispiel fügt die Transportschicht den Ziel-Port (25) dem Quell-Port des Quell-Hosts hinzu.

## Exercise

No exercises for this lesson.

## Quiz Question

Was ist ein zuverlässiges Transportprotokoll?

## Quiz Answer

TCP
