---
lang: "de"
title: "ping"
description: "Erfahren Sie, wie Sie den Linux-Befehl ping verwenden, um die Netzwerkkonnektivität zu testen und Probleme zu beheben. Verstehen Sie ICMP, TTL und Roundtrip-Zeit für eine effektive Netzwerkdiagnose."
keywords: "Linux ping, Netzwerkkonnektivität, ICMP, TTL, Linux-Netzwerk, Linux für Anfänger, Linux-Tutorial, ping-Befehl"
---

## Lesson Content

Eines der einfachsten Netzwerk-Tools, **ping**, wird verwendet, um zu testen, ob ein Paket einen Host erreichen kann. Es funktioniert, indem es ICMP Echo Request (Typ 8) Pakete an den Ziel-Host sendet und auf eine ICMP Echo Reply (Typ 0) wartet. Ping ist erfolgreich, wenn ein Host das Anforderungspaket sendet und eine Antwort vom Ziel empfängt. Schauen wir uns ein Beispiel an:

```plaintext
pete@icebox:~$ ping -c 3 www.google.com
PING www.google.com (74.125.239.112) 56(84) bytes of data.
64 bytes from nuq05s01-in-f16.1e100.net (74.125.239.112): icmp_seq=1 ttl=128 time=29.0 ms
64 bytes from nuq05s01-in-f16.1e100.net (74.125.239.112): icmp_seq=2 ttl=128 time=23.7 ms
64 bytes from nuq05s01-in-f16.1e100.net (74.125.239.112): icmp_seq=3 ttl=128 time=15.1 ms
```

In diesem Beispiel verwenden wir ping, um zu überprüfen, ob wir <www.google.com> erreichen können. Das Flag `-c` (count) wird verwendet, um das Senden von Echo-Request-Paketen zu beenden, nachdem die angegebene Anzahl erreicht wurde.

Der erste Teil besagt, dass wir 64-Byte-Pakete an 74.125.239.112 (google.com) senden, und der Rest zeigt uns die Details der Übertragung. Standardmäßig wird ein Paket pro Sekunde gesendet.

### icmp_seq

Das Feld `icmp_seq` wird verwendet, um die Sequenznummer der gesendeten Pakete anzuzeigen. In diesem Fall habe ich 3 Pakete gesendet, und wir können sehen, dass 3 Pakete zurückkamen. Wenn Sie einen Ping durchführen und einige Sequenznummern fehlen, bedeutet dies, dass ein Konnektivitätsproblem vorliegt und nicht alle Ihre Pakete durchkommen. Wenn die Sequenznummern nicht in der richtigen Reihenfolge sind, ist Ihre Verbindung wahrscheinlich sehr langsam, da Ihre Pakete die Standardzeit von einer Sekunde überschreiten.

### ttl

Das Time To Live (TTL)-Feld wird als Hop-Zähler verwendet. Bei jedem Hop wird der Zähler um eins dekrementiert, und sobald der Hop-Zähler 0 erreicht, stirbt unser Paket. Dies soll dem Paket eine Lebensdauer geben; wir möchten nicht, dass unsere Pakete ewig unterwegs sind.

### time

Die Roundtrip-Zeit, die es dauerte, von dem Zeitpunkt, an dem Sie das Echo-Request-Paket gesendet haben, bis zum Empfang einer Echo-Reply.

## Exercise

Führen Sie einen Ping auf einer Website durch und sehen Sie sich die erhaltene Ausgabe an.

## Quiz Question

Was ist die Maßeinheit für die Roundtrip-Zeit?

## Quiz Answer

ms
