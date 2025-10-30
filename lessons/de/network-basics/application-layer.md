---
index: 5
lang: "de"
title: "Anwendungsschicht"
meta_title: "Anwendungsschicht - Grundlagen des Netzwerks"
meta_description: "Erfahren Sie mehr über die Anwendungsschicht im TCP/IP-Modell, wie sie Daten für E-Mails (SMTP) verarbeitet und welche Rolle sie bei der Netzwerkkommunikation spielt. Verstehen Sie Netzwerkschichten."
meta_keywords: "Anwendungsschicht, TCP/IP-Modell, SMTP, Netzwerkschichten, Linux-Netzwerk, Anfänger-Tutorial, Netzwerkkommunikation"
---

## Lesson Content

Nehmen wir an, ich wollte Patty eine E-Mail senden. Wir werden jede der TCP/IP-Schichten durchgehen, um dies in Aktion zu sehen.

Denken Sie daran, dass Pakete zur Übertragung von Daten über Netzwerke verwendet werden. Ein Paket besteht aus einem Header und einer Nutzlast. Der Header enthält Informationen darüber, wohin das Paket geht und woher es kam. Die Nutzlast sind die tatsächlichen Daten, die übertragen werden. Während unser Paket das Netzwerk durchläuft, fügt jede Schicht dem Header des Pakets ein wenig Informationen hinzu. Beachten Sie auch, dass verschiedene Schichten einen anderen Begriff für unser „Paket“ verwenden. In der Transportschicht kapseln wir unsere Daten im Wesentlichen in ein Segment, und in der Verbindungsschicht bezeichnen wir dies als Frame, aber wissen Sie einfach, dass „Paket“ in Bezug auf dasselbe verwendet werden kann.

Zuerst beginnen wir in der Anwendungsschicht. Wenn wir unsere E-Mail über unseren E-Mail-Client senden, kapselt die Anwendungsschicht diese Daten. Die Anwendungsschicht kommuniziert mit der Transportschicht über einen bestimmten Port und sendet über diesen Port ihre Daten. Wir möchten eine E-Mail über das Anwendungsschichtprotokoll SMTP (Simple Mail Transfer Protocol) senden. Die Daten werden über unser Transportprotokoll gesendet, das eine Verbindung zu diesem Port öffnet (Port 25 wird für SMTP verwendet). So werden diese Daten über diesen Port gesendet, und diese Daten werden an die Transportschicht gesendet, um in Segmente gekapselt zu werden.

## Exercise

Übung macht den Meister! Hier ist ein praktisches Labor, um Ihr Verständnis von Netzwerkschichten und Ports zu vertiefen:

1. **[Netzwerkports und -sitzungen mit netstat in Linux analysieren](https://labex.io/de/labs/comptia-analyze-network-ports-and-sessions-with-netstat-in-linux-592741)** – In diesem Labor lernen Sie, wie Sie den Befehl `netstat` verwenden, um Netzwerkaktivitäten zu analysieren, und grundlegende Konzepte wie Netzwerkports, Sockets und aktive Verbindungen zu erkunden. Dies gibt Ihnen praktische Einblicke, wie Dienste über das Netzwerk kommunizieren, was direkt mit den besprochenen Konzepten der Transportschicht zusammenhängt.

Dieses Labor wird Ihnen helfen, die Konzepte der Netzwerkkommunikation und Portnutzung in einer realen Linux-Umgebung anzuwenden und Ihr Vertrauen in das Verständnis zu stärken, wie Anwendungen mit dem Netzwerk-Stack interagieren.

## Quiz Question

Welche Schicht wird verwendet, um die Paketdaten in einem benutzerfreundlichen Format darzustellen?

## Quiz Answer

Application
