---
index: 2
lang: "de"
title: "Route"
meta_title: "Route - Netzwerkkonfiguration"
meta_description: "Erfahren Sie, wie Sie Ihre Linux-Routing-Tabelle verwalten. Diese Anleitung behandelt das Hinzufügen und Löschen von Netzwerkrouten mit dem modernen Befehl 'ip route command in linux' und dem älteren Befehl 'route'."
meta_keywords: "ip route befehl linux, linux ip route befehl, route hinzufügen, route löschen, routingtabelle, netzwerk-routing, linux netzwerk, ip route"
---

## Lesson Content

Unter Linux leitet die Routing-Tabelle den Netzwerkverkehr an sein korrektes Ziel weiter. Obwohl wir zuvor die Anzeige dieser Tabelle besprochen haben, können Sie auch manuell Routen hinzufügen oder entfernen, um zu steuern, wie Datenpakete weitergeleitet werden. Dies ist unerlässlich für die Konfiguration komplexer Netzwerkeinrichtungen oder die Fehlerbehebung bei Verbindungsproblemen.

### Verwendung des Legacy-Befehls route

Der Befehl `route` ist ein traditionelles Werkzeug zur Verwaltung der Routing-Tabelle. Obwohl er noch funktionsfähig ist, gilt er als veraltet, und der Befehl `ip` wird heute bevorzugt.

Um eine neue Netzwerkroute hinzuzufügen, geben Sie die Netzwerkadresse, die Subnetzmaske und das Gateway (`gw`) an:

```bash
sudo route add -net 192.168.2.1/23 gw 10.11.12.3
```

Um eine Route zu löschen, verwenden Sie das Flag `del` zusammen mit der Netzwerkadresse:

```bash
sudo route del -net 192.168.2.1/23
```

### Moderne Routenverwaltung mit ip route

Der Befehl `ip route` ist das moderne und leistungsfähigere Werkzeug für die Netzwerkkonfiguration unter Linux. Er bietet eine konsistentere und umfangreichere Reihe von Optionen zur Verwaltung von Netzwerkschnittstellen und Routen. Die Verwendung des **linux ip route command** ist die empfohlene Vorgehensweise für aktuelle Systeme.

Um eine Route mit dem **ip route command in linux** hinzuzufügen, verwenden Sie die Aktion `add` und geben das Zielnetzwerk und den nächsten Hop über das Gateway an:

```bash
ip route add 192.168.2.1/23 via 10.11.12.3
```

Um eine Route zu löschen, können Sie die Aktion `delete` verwenden. Sie können die Route vollständig angeben oder nur das Zielnetzwerk, falls es eindeutig ist:

```bash
# Löschen durch Angabe der vollständigen Route
ip route delete 192.168.2.1/23 via 10.11.12.3

# Oder Löschen durch Angabe nur des Ziels
ip route delete 192.168.2.1/23
```

Die Beherrschung des Befehls `ip route` ist eine Schlüsselqualifikation für jeden Linux-Administrator, der für die Netzwerkverwaltung zuständig ist.

## Exercise

Übung macht den Meister! Hier sind einige praktische Labs, um Ihr Verständnis von Netzwerk-Routing und IP-Adressierung zu festigen:

1.  **[IP-Adressierung unter Linux verwalten](https://labex.io/de/labs/comptia-manage-ip-addressing-in-linux-592736)** - Üben Sie die Konfiguration einer statischen IP, das Festlegen eines Standard-Gateways und die Überprüfung der Netzwerkkonfiguration mit dem Befehl `ip`.
2.  **[Netzwerkschicht-Interaktion mit ping und arp unter Linux erkunden](https://labex.io/de/labs/comptia-explore-network-layer-interaction-with-ping-and-arp-in-linux-592746)** - Erfahren Sie, wie das Standard-Gateway den Remote-Verkehr verarbeitet, und beobachten Sie Interaktionen auf Netzwerkschichtebene.

Diese Labs helfen Ihnen, die Konzepte der IP-Adressierung und des Routings in realen Szenarien anzuwenden und Vertrauen in das Linux-Networking aufzubauen.

## Quiz Question

Wenn Sie den Legacy-Befehl `route` verwenden, welches Flag wird zum Löschen einer Route verwendet? Bitte antworten Sie auf Englisch und achten Sie auf die Groß-/Kleinschreibung.

## Quiz Answer

del
