---
index: 3
lang: "de"
title: "traceroute"
meta_title: "traceroute - Fehlerbehebung"
meta_description: "Erfahren Sie, wie Sie den Linux-Befehl traceroute verwenden, um Netzwerkrouten zu verfolgen und Konnektivitätsprobleme zu beheben. Verstehen Sie TTL und Paket-Routing für Anfänger."
meta_keywords: "traceroute, Linux-Netzwerk, Netzwerk-Fehlerbehebung, TTL, Linux-Befehle, Anfänger, Tutorial"
---

## Lesson Content

Der Befehl `traceroute` wird verwendet, um zu sehen, wie Pakete geroutet werden. Er funktioniert, indem er Pakete mit steigenden TTL-Werten (Time To Live) sendet, beginnend mit 1. Der erste Router empfängt das Paket und dekrementiert den TTL-Wert um eins, wodurch das Paket verworfen wird. Der Router sendet uns eine ICMP Time Exceeded-Nachricht zurück. Das nächste Paket erhält dann eine TTL von 2, so dass es den ersten Router passiert, aber wenn es den zweiten Router erreicht, ist die TTL 0, und es sendet eine weitere ICMP Time Exceeded-Nachricht zurück. Traceroute funktioniert auf diese Weise, weil es beim Senden und Verwerfen von Paketen eine Liste von Routern erstellt, die die Pakete durchlaufen, bis es schließlich sein Ziel erreicht und eine ICMP Echo Reply-Nachricht empfängt.

Hier ist ein kleiner Ausschnitt eines Traceroutes:

```bash
$ traceroute google.com
traceroute to google.com (216.58.216.174), 30 hops max, 60 byte packets
 1  192.168.4.254 (192.168.4.254)  0.028 ms  0.009 ms  0.008 ms
 2  100.64.1.113 (100.64.1.113)  1.227 ms  1.226 ms 0.920 ms
 3  100.64.0.20 (100.64.0.20)  1.501 ms 1.556 ms  0.855 ms
```

Jede Zeile stellt einen Router oder eine Maschine dar, die sich zwischen Ihnen und Ihrem Ziel befindet. Sie zeigt den Namen des Ziels und seine IP-Adresse, und die letzten drei Spalten entsprechen der Round-Trip-Zeit eines Pakets, um diesen Router zu erreichen. Standardmäßig werden drei Pakete entlang der Route gesendet.

## Exercise

Übung macht den Meister! Hier sind einige praktische Übungen, um Ihr Verständnis der Netzwerfpfad-Erkennung und Fehlerbehebung zu vertiefen:

1. **[IP-Adressierung in Linux verwalten](https://labex.io/de/labs/comptia-manage-ip-addressing-in-linux-592736)** – Üben Sie die Verwendung des Befehls `ip` zur Konfiguration von Netzwerkeinstellungen und zur Überprüfung der Konnektivität mit `traceroute`.
2. **[Netzwerkschicht-Interaktion mit ping und arp in Linux erkunden](https://labex.io/de/labs/comptia-explore-network-layer-interaction-with-ping-and-arp-in-linux-592746)** – Erfahren Sie, wie `ping` und `arp` funktionieren, um Netzwerkschicht-Interaktionen zu verstehen, die grundlegend für die Funktionsweise von `traceroute` sind.

Diese Labs helfen Ihnen, die Konzepte der Netzwerkdiagnose in realen Szenarien anzuwenden und Vertrauen in die Linux-Netzwerktools aufzubauen.

## Quiz Question

Was wird um eins dekrementiert, wenn Hops über das Netzwerk gemacht werden?

## Quiz Answer

TTL
