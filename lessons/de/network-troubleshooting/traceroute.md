---
lang: "de"
title: "traceroute"
description: "Erfahren Sie, wie Sie den Linux-Befehl traceroute verwenden, um Netzwerkrouten zu verfolgen und Konnektivitätsprobleme zu beheben. Verstehen Sie TTL und Paket-Routing für Anfänger."
keywords: "traceroute, Linux-Netzwerk, Netzwerk-Fehlerbehebung, TTL, Linux-Befehle, Anfänger, Tutorial"
---

## Lesson Content

Der Befehl `traceroute` wird verwendet, um zu sehen, wie Pakete geroutet werden. Er funktioniert, indem er Pakete mit zunehmenden TTL-Werten (Time To Live) sendet, beginnend mit 1. Der erste Router empfängt das Paket und dekrementiert den TTL-Wert um eins, wodurch das Paket verworfen wird. Der Router sendet uns dann eine ICMP Time Exceeded-Nachricht zurück. Das nächste Paket erhält dann einen TTL von 2, so dass es den ersten Router passiert, aber wenn es den zweiten Router erreicht, ist der TTL 0, und es sendet eine weitere ICMP Time Exceeded-Nachricht zurück. Traceroute funktioniert auf diese Weise, weil es beim Senden und Verwerfen von Paketen eine Liste von Routern erstellt, die die Pakete durchlaufen, bis es schließlich sein Ziel erreicht und eine ICMP Echo Reply-Nachricht empfängt.

Hier ist ein kleiner Ausschnitt eines traceroute:

```bash
$ traceroute google.com
traceroute to google.com (216.58.216.174), 30 hops max, 60 byte packets
 1  192.168.4.254 (192.168.4.254)  0.028 ms  0.009 ms  0.008 ms
 2  100.64.1.113 (100.64.1.113)  1.227 ms  1.226 ms 0.920 ms
 3  100.64.0.20 (100.64.0.20)  1.501 ms 1.556 ms  0.855 ms
```

Jede Zeile stellt einen Router oder eine Maschine dar, die sich zwischen Ihnen und Ihrem Ziel befindet. Sie zeigt den Namen des Ziels und seine IP-Adresse, und die letzten drei Spalten entsprechen der Round-Trip-Zeit eines Pakets, um diesen Router zu erreichen. Standardmäßig werden drei Pakete entlang der Route gesendet.

## Exercise

Führen Sie den Befehl `traceroute` auf Ihrem Computer aus und beobachten Sie die Ausgabe.

## Quiz Question

Was wird um eins dekrementiert, wenn Hops über das Netzwerk gemacht werden?

## Quiz Answer

TTL
