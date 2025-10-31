---
index: 2
lang: "de"
title: "Routing-Tabelle"
meta_title: "Routing-Tabelle - Routing"
meta_description: "Ein Leitfaden zum Verständnis der Linux-Routing-Tabelle. Erfahren Sie, wie Sie die Ausgabe des route-Befehls interpretieren, einschließlich Ziel, Gateway, Genmask und der eth0-Schnittstelle. Meistern Sie die Grundlagen Ihrer Linux-Route-Tabelle."
meta_keywords: "linux routing tabelle, linux route tabelle, genmask, eth0, route befehl, netzwerk routing, ip routing, ziel, gateway, subnetzmaske, linux netzwerk"
---

## Lesson Content

Die **Linux-Routing-Tabelle** enthält die Regeln, die bestimmen, wohin Netzwerkpakete gesendet werden. Jedes Mal, wenn Ihr System ein Paket an eine IP-Adresse senden muss, konsultiert es diese Tabelle, um den geeigneten Pfad zu finden. Um die **Linux-Routing-Tabelle** Ihres Rechners anzuzeigen, können Sie den Befehl `route` verwenden.

```plaintext
pete@icebox:~$ sudo route -n
Kernel IP routing table
Destination     Gateway         Genmask         Flags Metric Ref    Use Iface
0.0.0.0         192.168.224.2   0.0.0.0         UG    0      0        0 eth0
192.168.224.0   0.0.0.0         255.255.255.0   U     1      0        0 eth0
```

### Verständnis der Spalten

Die Ausgabe des Befehls `route` ist in mehrere Spalten unterteilt, die jeweils spezifische Informationen zu einer Netzwerkroute liefern.

### Destination (Ziel)

Die Spalte "Destination" (Ziel) gibt ein Netzwerk oder einen Host an. Der Eintrag `192.168.224.0` leitet alle Pakete, die für dieses spezifische Netzwerk bestimmt sind. Wenn das Ziel eines Pakets innerhalb dieses Netzwerks liegt (z. B. von 192.168.224.5 nach 192.168.224.7), wird es direkt über die angegebene Schnittstelle, wie z. B. `eth0`, gesendet.

Das Ziel `0.0.0.0` ist die Standardroute. Wenn die Routing-Tabelle keinen spezifischeren Eintrag für das Ziel eines Pakets findet, wird diese Route verwendet.

### Gateway

Die Spalte "Gateway" zeigt den Router an, an den Pakete gesendet werden. Wenn ein Paket sich nicht im selben lokalen Netzwerk befindet, wird es an diese Gateway-Adresse weitergeleitet. Bei der Standardroute ist dies die IP-Adresse des Routers, der Ihr lokales Netzwerk mit anderen Netzwerken, wie dem Internet, verbindet.

### Genmask

Die `genmask` (Generation Mask) ist die Subnetzmaske für das Zielnetzwerk. Sie wird zusammen mit der Ziel-IP verwendet, um festzustellen, ob ein Paket zu diesem Netzwerk gehört. Beispielsweise bedeutet eine `genmask` von `255.255.255.0`, dass die ersten drei Oktette der IP-Adresse mit den ersten drei Oktetten des Ziels übereinstimmen müssen.

### Flags

Diese Flags liefern zusätzliche Informationen über die Route:

- **U**: Zeigt an, dass die Route aktiv (up) ist.
- **G**: Bedeutet, dass die Route zu einem Gateway (Router) führt.
- **UG**: Bedeutet, dass die Route aktiv ist und auf ein Gateway verweist.

### Iface

Diese Spalte gibt die Netzwerkschnittstelle, wie z. B. `eth0`, an, über die Pakete für diese Route gesendet werden. `eth0` repräsentiert typischerweise den ersten Ethernet-Adapter Ihres Systems.

## Exercise

Übung macht den Meister! Hier sind einige praktische Labs, um Ihr Verständnis von Netzwerk-Routing und IP-Adressierung zu festigen:

1. **[MAC- und IP-Adressen in Linux identifizieren](https://labex.io/de/labs/comptia-identify-mac-and-ip-addresses-in-linux-592731)** – Üben Sie die Verwendung des Befehls `ip a`, um Informationen zur Netzwerkadressierung zu identifizieren, einschließlich IP-Adressen und Netzwerkschnittstellen, die Schlüsselkomponenten einer Routing-Tabelle sind.
2. **[IP-Adressierung in Linux verwalten](https://labex.io/de/labs/comptia-manage-ip-addressing-in-linux-592736)** – Lernen Sie, die IP-Adressierung zu verwalten, statische IPs zu konfigurieren, Standard-Gateways festzulegen und Netzwerkkonfigurationen zu überprüfen, was direkt mit den Einträgen in einer Routing-Tabelle zusammenhängt.
3. **[IP-Adress-Typen und Erreichbarkeit in Linux erkunden](https://labex.io/de/labs/comptia-explore-ip-address-types-and-reachability-in-linux-592780)** – Erkunden Sie die IP-Adressierung und die Netzwerkerreichbarkeit mithilfe von `ping` und `ip a`, um zu verstehen, wie verschiedene IP-Typen interagieren und wie die Netzwerkerreichbarkeit bestimmt wird, was sich in Routing-Entscheidungen widerspiegelt.

Diese Labs helfen Ihnen, die Konzepte in realen Szenarien anzuwenden und Selbstvertrauen bei der Netzwerkkonfiguration und Fehlerbehebung aufzubauen.

## Quiz Question

Wenn ein Ziel nicht in der Routing-Tabelle gefunden wird, wohin werden die Pakete gesendet? Bitte antworten Sie mit einem einzigen englischen Wort unter Beachtung der Groß-/Kleinschreibung.

## Quiz Answer

Gateway
