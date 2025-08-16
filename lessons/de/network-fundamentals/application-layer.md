---
title: "Anwendungsschicht"
description: "Erfahren Sie mehr über die Anwendungsschicht im TCP/IP-Modell, wie sie Daten für E-Mails (SMTP) verarbeitet und welche Rolle sie in der Netzwerkkommunikation spielt. Verstehen Sie Netzwerkschichten."
keywords: "Anwendungsschicht, TCP/IP-Modell, SMTP, Netzwerkschichten, Linux-Netzwerk, Anfänger-Tutorial, Netzwerkkommunikation"
---

## Lesson Content

Nehmen wir an, ich wollte eine E-Mail an Patty senden. Wir werden jede der TCP/IP-Schichten durchgehen, um dies in Aktion zu sehen.

Denken Sie daran, dass Pakete verwendet werden, um Daten über Netzwerke zu übertragen. Ein Paket besteht aus einem Header und einer Nutzlast. Der Header enthält Informationen darüber, wohin das Paket geht und woher es kam. Die Nutzlast sind die tatsächlichen Daten, die übertragen werden. Während unser Paket das Netzwerk durchläuft, fügt jede Schicht dem Header des Pakets ein wenig Information hinzu. Beachten Sie auch, dass verschiedene Schichten einen anderen Begriff für unser „Paket“ verwenden. In der Transportschicht kapseln wir unsere Daten im Wesentlichen in ein Segment, und in der Verbindungsschicht bezeichnen wir dies als Frame, aber wissen Sie einfach, dass „Paket“ in Bezug auf dasselbe verwendet werden kann.

Zuerst beginnen wir in der Anwendungsschicht. Wenn wir unsere E-Mail über unseren E-Mail-Client senden, kapselt die Anwendungsschicht diese Daten. Die Anwendungsschicht kommuniziert mit der Transportschicht über einen bestimmten Port, und über diesen Port sendet sie ihre Daten. Wir möchten eine E-Mail über das Anwendungsschichtprotokoll SMTP (Simple Mail Transfer Protocol) senden. Die Daten werden über unser Transportprotokoll gesendet, das eine Verbindung zu diesem Port öffnet (Port 25 wird für SMTP verwendet). Wir erhalten also diese Daten, die über diesen Port gesendet werden, und diese Daten werden an die Transportschicht gesendet, um in Segmente gekapselt zu werden.

## Exercise

Keine Übungen für diese Lektion.

## Quiz Question

Welche Schicht wird verwendet, um die Paketdaten in einem benutzerfreundlichen Format darzustellen?

## Quiz Answer

Application
