---
lang: "de"
title: "ICMP"
meta_description: "Erfahren Sie mehr über die Grundlagen des ICMP-Protokolls, Nachrichtentypen und Codes zur Netzwerkfehlerbehebung. Verstehen Sie, wie ICMP funktioniert, um Netzwerkprobleme zu debuggen."
meta_keywords: "ICMP, ICMP-Protokoll, Netzwerkfehlerbehebung, ICMP-Typen, Linux-Netzwerk, Anfänger, Tutorial, Anleitung"
---

## Lesson Content

Das Internet Control Message Protocol (ICMP) ist Teil der TCP/IP-Protokollsuite. Es wird verwendet, um Updates und Fehlermeldungen zu senden und ist ein äußerst nützliches Protokoll zur Behebung von Netzwerkproblemen, wie z.B. fehlgeschlagener Paketlieferung.

Jede ICMP-Nachricht enthält ein Type-, Code- und Checksum-Feld. Das Type-Feld gibt den Typ der ICMP-Nachricht an, der Code ist ein Subtyp, der weitere Informationen über die Nachricht liefert, und die Checksum wird verwendet, um Probleme mit der Integrität der Nachricht zu erkennen.

Schauen wir uns einige gängige ICMP Types an:

- Type 0 - Echo Reply
- Type 3 - Destination Unreachable
- Type 8 - Echo Request
- Type 11 - Time Exceeded

Wenn ein Paket ein Ziel nicht erreichen kann, wird eine Type 3 ICMP-Nachricht generiert. Innerhalb von Type 3 gibt es 16 Code-Werte, die genauer beschreiben, warum es das Ziel nicht erreichen kann:

- Code 0 - Network Unreachable
- Code 1 - Host Unreachable
  etc...etc...

Diese Nachrichten werden verständlicher, wenn wir einige Tools zur Netzwerkfehlerbehebung verwenden.

## Exercise

Keine Übungen für diese Lektion.

## Quiz Question

Was ist der ICMP-Typ für eine Echo-Anfrage?

## Quiz Answer

8
