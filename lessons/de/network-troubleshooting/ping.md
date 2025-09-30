---
index: 2
lang: "de"
title: "ping"
meta_title: "ping - Fehlerbehebung"
meta_description: "Erfahren Sie, wie Sie den Linux-Befehl ping verwenden, um die Netzwerkkonnektivität zu testen und Probleme zu beheben. Verstehen Sie ICMP, TTL und Roundtrip-Zeit für eine effektive Netzwerkdiagnose."
meta_keywords: "Linux ping, Netzwerkkonnektivität, ICMP, TTL, Linux-Netzwerk, Linux für Anfänger, Linux-Tutorial, ping-Befehl"
---

## Lesson Content

Eines der einfachsten Netzwerk-Tools, **ping**, wird verwendet, um zu testen, ob ein Paket einen Host erreichen kann oder nicht. Es funktioniert, indem es ICMP-Echo-Anfragepakete (Typ 8) an den Zielhost sendet und auf eine ICMP-Echo-Antwort (Typ 0) wartet. Ping ist erfolgreich, wenn ein Host das Anfragepaket sendet und eine Antwort vom Ziel empfängt. Schauen wir uns ein Beispiel an:

```plaintext
pete@icebox:~$ ping -c 3 www.google.com
PING www.google.com (74.125.239.112) 56(84) bytes of data.
64 bytes from nuq05s01-in-f16.1e100.net (74.125.239.112): icmp_seq=1 ttl=128 time=29.0 ms
64 bytes from nuq05s01-in-f16.1e100.net (74.125.239.112): icmp_seq=2 ttl=128 time=23.7 ms
64 bytes from nuq05s01-in-f16.1e100.net (74.125.239.112): icmp_seq=3 ttl=128 time=15.1 ms
```

In diesem Beispiel verwenden wir ping, um zu überprüfen, ob wir `www.google.com` erreichen können. Das Flag `-c` (count) wird verwendet, um das Senden von Echo-Anfragepaketen zu beenden, nachdem die angegebene Anzahl erreicht wurde.

Der erste Teil besagt, dass wir 64-Byte-Pakete an 74.125.239.112 (google.com) senden, und der Rest zeigt uns die Details der Reise. Standardmäßig wird ein Paket pro Sekunde gesendet.

### icmp_seq

Das Feld `icmp_seq` wird verwendet, um die Sequenznummer der gesendeten Pakete anzuzeigen. In diesem Fall habe ich 3 Pakete gesendet, und wir können sehen, dass 3 Pakete zurückgekommen sind. Wenn Sie einen Ping durchführen und einige Sequenznummern fehlen, bedeutet dies, dass ein Konnektivitätsproblem vorliegt und nicht alle Ihre Pakete durchkommen. Wenn die Sequenznummern nicht in der richtigen Reihenfolge sind, ist Ihre Verbindung wahrscheinlich sehr langsam, da Ihre Pakete den standardmäßigen einen Sekunde überschreiten.

### ttl

Das Time To Live (TTL)-Feld wird als Hop-Zähler verwendet. Bei jedem Hop wird der Zähler um eins dekrementiert, und sobald der Hop-Zähler 0 erreicht, stirbt unser Paket. Dies soll dem Paket eine Lebensdauer geben; wir möchten nicht, dass unsere Pakete ewig unterwegs sind.

### time

Die Roundtrip-Zeit, die vom Senden des Echo-Anfragepakets bis zum Empfang einer Echo-Antwort vergangen ist.

## Exercise

Übung macht den Meister! Hier sind einige praktische Übungen, um Ihr Verständnis der Netzwerkkonnektivität und des `ping`-Befehls zu vertiefen:

1. **[Erkunden Sie die Interaktion der Netzwerkschicht mit ping und arp in Linux](https://labex.io/de/labs/comptia-explore-network-layer-interaction-with-ping-and-arp-in-linux-592746)** – Verwenden Sie `ping` und `arp`, um Interaktionen der Netzwerk- und Datenverbindungsschicht zu erkunden und zu beobachten, wie das Standard-Gateway den Remote-Verkehr verarbeitet.
2. **[Erkunden Sie IP-Adresstypen und Erreichbarkeit in Linux](https://labex.io/de/labs/comptia-explore-ip-address-types-and-reachability-in-linux-592780)** – Nutzen Sie `ping` und `ip a`, um den lokalen TCP/IP-Stack zu testen, die öffentliche Internetverbindung zu überprüfen und die Netzwerkerreichbarkeit zu erkunden.
3. **[Simulieren Sie die Netzwerkschichtkonnektivität in Linux](https://labex.io/de/labs/comptia-simulate-network-layer-connectivity-in-linux-592752)** – Lernen Sie, statische IP-Adressen mit `ip addr` zuzuweisen und die Konnektivität mit `ping` in denselben und verschiedenen Subnetzen zu testen.

Diese Übungen helfen Ihnen, die Konzepte der Netzwerkerreichbarkeit und des `ping`-Befehls in realen Szenarien anzuwenden und Vertrauen in die Netzwerkdiagnose unter Linux aufzubauen.

## Quiz Question

Was ist die Maßeinheit für die Roundtrip-Zeit?

## Quiz Answer

ms
