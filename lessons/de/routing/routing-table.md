---
index: 2
lang: "de"
title: "Routing-Tabelle"
meta_title: "Routing-Tabelle - Routing"
meta_description: "Lernen Sie, die Linux-Routing-Tabelle zu verstehen und wie Pakete mit dem Befehl route weitergeleitet werden. Entdecken Sie Ziele, Gateways und Schnittstellen für die Netzwerk-Grundlagen."
meta_keywords: "Linux-Routing-Tabelle, route-Befehl, Netzwerk-Routing, Linux-Netzwerk, Linux für Anfänger, Linux-Tutorial, Netzwerk-Anleitung"
---

## Lesson Content

Schauen Sie sich die Routing-Tabelle Ihres Computers an:

```plaintext
pete@icebox:~$ sudo route -n
Kernel IP routing table
Destination     Gateway         Genmask         Flags Metric Ref    Use Iface
0.0.0.0         192.168.224.2   0.0.0.0         UG    0      0        0 eth0
192.168.224.0   0.0.0.0         255.255.255.0   U     1      0        0 eth0
```

### Ziel

Im ersten Feld haben wir eine Ziel-IP-Adresse von 192.168.224.0. Dies bedeutet, dass jedes Paket, das versucht, in dieses Netzwerk zu gelangen, über mein Ethernet-Kabel (eth0) gesendet wird. Wenn ich 192.168.224.5 wäre und zu 192.168.224.7 gelangen wollte, würde ich einfach die Netzwerkschnittstelle eth0 direkt verwenden.

Beachten Sie, dass wir Adressen von **0.0.0.0** haben. Dies bedeutet, dass keine Adresse angegeben oder unbekannt ist. Wenn ich beispielsweise ein Paket an die IP-Adresse 151.123.43.6 senden wollte, weiß unsere Routing-Tabelle nicht, wohin es geht, also wird es als 0.0.0.0 bezeichnet und leitet unser Paket daher an das Gateway weiter.

### Gateway

Wenn wir ein Paket senden, das sich nicht im selben Netzwerk befindet, wird es an diese Gateway-Adresse gesendet, die passenderweise als Gateway zu einem anderen Netzwerk bezeichnet wird.

### Genmask

Dies ist die Subnetzmaske, die verwendet wird, um herauszufinden, welche IP-Adressen zu welchem Ziel passen.

### Flags

- UG - Netzwerk ist aktiv und ist ein Gateway
- U - Netzwerk ist aktiv

### Iface

Dies ist die Schnittstelle, über die unser Paket gesendet wird. `eth0` steht normalerweise für das erste Ethernet-Gerät in Ihrem System.

## Exercise

Übung macht den Meister! Hier sind einige praktische Übungen, um Ihr Verständnis von Netzwerk-Routing und IP-Adressierung zu vertiefen:

1. **[MAC- und IP-Adressen in Linux identifizieren](https://labex.io/de/labs/comptia-identify-mac-and-ip-addresses-in-linux-592731)** - Üben Sie die Verwendung des Befehls `ip a`, um Netzwerkinformationen zu identifizieren, einschließlich IP-Adressen und Netzwerkschnittstellen, die Schlüsselkomponenten einer Routing-Tabelle sind.
2. **[IP-Adressierung in Linux verwalten](https://labex.io/de/labs/comptia-manage-ip-addressing-in-linux-592736)** - Lernen Sie, die IP-Adressierung zu verwalten, statische IPs zu konfigurieren, Standard-Gateways festzulegen und Netzwerkkonfigurationen zu überprüfen, was direkt mit den Einträgen in einer Routing-Tabelle zusammenhängt.
3. **[IP-Adresstypen und Erreichbarkeit in Linux erkunden](https://labex.io/de/labs/comptia-explore-ip-address-types-and-reachability-in-linux-592780)** - Erkunden Sie die IP-Adressierung und Netzwerkerreichbarkeit mit `ping` und `ip a`, um zu verstehen, wie verschiedene IP-Typen interagieren und wie die Netzwerkerreichbarkeit bestimmt wird, was sich in Routing-Entscheidungen widerspiegelt.

Diese Übungen helfen Ihnen, die Konzepte in realen Szenarien anzuwenden und Vertrauen in die Netzwerkkonfiguration und -fehlerbehebung aufzubauen.

## Quiz Question

Wohin werden Pakete geleitet, wenn unsere Routing-Tabelle es nicht weiß?

## Quiz Answer

Gateway
