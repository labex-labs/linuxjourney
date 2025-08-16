---
title: "Routing-Tabelle"
description: "Lernen Sie, die Linux-Routing-Tabelle zu verstehen und wie Pakete mit dem route-Befehl geroutet werden. Erkunden Sie Ziele, Gateways und Schnittstellen für Netzwerk-Grundlagen."
keywords: "Linux-Routing-Tabelle, route-Befehl, Netzwerk-Routing, Linux-Netzwerk, Linux für Anfänger, Linux-Tutorial, Netzwerk-Anleitung"
---

## Lesson Content

Betrachten Sie die Routing-Tabelle Ihres Rechners:

```plaintext
pete@icebox:~$ sudo route -n
Kernel IP routing table
Destination     Gateway         Genmask         Flags Metric Ref    Use Iface
0.0.0.0         192.168.224.2   0.0.0.0         UG    0      0        0 eth0
192.168.224.0   0.0.0.0         255.255.255.0   U     1      0        0 eth0
```

### Destination

Im ersten Feld haben wir eine Ziel-IP-Adresse von 192.168.224.0. Dies bedeutet, dass jedes Paket, das versucht, in dieses Netzwerk zu gelangen, über mein Ethernet-Kabel (eth0) gesendet wird. Wenn ich 192.168.224.5 wäre und zu 192.168.224.7 gelangen wollte, würde ich einfach die Netzwerkschnittstelle eth0 direkt verwenden.

Beachten Sie, dass wir Adressen von **0.0.0.0** haben. Dies bedeutet, dass keine Adresse angegeben oder sie unbekannt ist. Wenn ich zum Beispiel ein Paket an die IP-Adresse 151.123.43.6 senden wollte, weiß unsere Routing-Tabelle nicht, wohin es geht, also kennzeichnet sie es als 0.0.0.0 und leitet unser Paket daher an das Gateway weiter.

### Gateway

Wenn wir ein Paket senden, das sich nicht im selben Netzwerk befindet, wird es an diese Gateway-Adresse gesendet, die passenderweise als Gateway zu einem anderen Netzwerk bezeichnet wird.

### Genmask

Dies ist die Subnetzmaske, die verwendet wird, um herauszufinden, welche IP-Adressen zu welchem Ziel passen.

### Flags

- UG - Network is Up and is a Gateway
- U - Network is Up

### Iface

Dies ist die Schnittstelle, über die unser Paket gesendet wird. eth0 steht normalerweise für das erste Ethernet-Gerät auf Ihrem System.

## Exercise

Betrachten Sie Ihre Routing-Tabelle und sehen Sie, wohin Ihre Pakete gehen können.

## Quiz Question

Wohin werden Pakete geleitet, wenn unsere Routing-Tabelle es nicht weiß?

## Quiz Answer

Gateway
