---
index: 3
lang: "de"
title: "Traceroute"
meta_title: "Traceroute - Fehlerbehebung"
meta_description: "Meistern Sie den Traceroute Linux-Befehl, um Netzwerkrouten zu verfolgen und Verbindungsprobleme zu beheben. Dieses Tutorial erklärt, wie Traceroute TTL verwendet, um den Pfad abzubilden, den Pakete zu ihrem Ziel nehmen."
meta_keywords: "Traceroute, Traceroute Linux, Linux-Netzwerke, Netzwerk-Fehlerbehebung, TTL, Paket-Routing, Linux-Befehle, Anfänger, Tutorial"
---

## Lesson Content

Der Befehl `traceroute` ist ein grundlegendes Werkzeug zur Netzwerkdiagnose, das verwendet wird, um den Pfad zu verfolgen, den Pakete von Ihrem Computer zu einem Zielhost nehmen. Durch die Anzeige jedes "Hops" oder Routers auf dem Weg hilft er Ihnen, Engpässe im Netzwerk zu identifizieren und Verbindungsprobleme zu beheben. Das Dienstprogramm `traceroute linux` ist für jeden Systemadministrator oder Netzwerktechniker unerlässlich.

### Wie Traceroute funktioniert

Der Mechanismus hinter `traceroute` liegt in seiner cleveren Manipulation des Time To Live (TTL)-Feldes im Header eines IP-Pakets. Der Vorgang funktioniert wie folgt:

1. `traceroute` sendet ein Prüfpaket mit einem TTL-Wert von 1 aus.
2. Der erste Router auf dem Pfad empfängt das Paket, dekrementiert die TTL auf 0 und verwirft es. Der Router sendet dann eine ICMP-"Time Exceeded"-Nachricht zurück an Ihren Computer.
3. `traceroute` zeichnet die IP-Adresse des Routers und die Round-Trip-Zeit auf.
4. Anschließend sendet es ein weiteres Paket, diesmal mit einer TTL von 2. Dieses Paket passiert den ersten Router erfolgreich, wird aber vom zweiten Router verworfen, der wiederum eine "Time Exceeded"-Nachricht zurücksendet.
5. Dieser Vorgang wiederholt sich, wobei die TTL für jeden nachfolgenden Satz von Paketen um eins erhöht wird. Durch das Erstellen einer Liste der Router, die "Time Exceeded"-Nachrichten zurücksenden, kartiert `traceroute` die gesamte Route.
6. Der Vorgang endet, wenn die Pakete schließlich das Ziel erreichen, das mit einer ICMP-"Echo Reply"-Nachricht antwortet.

### Verstehen der Traceroute-Ausgabe

Betrachten wir eine Beispielausgabe der Ausführung von `traceroute` in einem Linux-Terminal:

```bash
$ traceroute google.com
traceroute an google.com (216.58.216.174), 30 Hops max, 60 Byte Pakete
 1  192.168.4.254 (192.168.4.254)  0.028 ms  0.009 ms  0.008 ms
 2  100.64.1.113 (100.64.1.113)  1.227 ms  1.226 ms 0.920 ms
 3  100.64.0.20 (100.64.0.20)  1.501 ms 1.556 ms  0.855 ms
```

Jede nummerierte Zeile stellt einen Hop entlang des Netzwerkpfads dar. Hier ist, wie die Informationen zu interpretieren sind:

- **Hop-Nummer:** Die erste Spalte (z. B. `1`, `2`, `3`) gibt die Reihenfolge des Routers im Pfad an.
- **Router-Name und IP-Adresse:** Der nächste Teil zeigt den Hostnamen (falls auflösbar) und die IP-Adresse des Routers an diesem Hop.
- **Round-Trip-Zeiten (RTT):** Die letzten drei Spalten zeigen die Round-Trip-Zeit für jedes der drei Prüfpakete, die an diesen spezifischen Hop gesendet wurden. Diese Zeiten, gemessen in Millisekunden (ms), helfen Ihnen, die Latenz bei jedem Schritt der Reise abzuschätzen.

Die effektive Nutzung des Befehls `traceroute linux` liefert unschätzbare Einblicke in die Leistung und Struktur Ihres Netzwerks.

## Exercise

Übung ist der Schlüssel zur Beherrschung der Netzwerkdiagnose. Die folgenden praktischen Labs helfen Ihnen, Ihr Verständnis der Netzwerkwegfindung und Fehlerbehebung mit Tools wie `traceroute` zu festigen:

1. **[IP-Adressierung in Linux verwalten](https://labex.io/de/labs/comptia-manage-ip-addressing-in-linux-592736)** - Üben Sie die Verwendung des `ip`-Befehls zur Konfiguration von Netzwerkeinstellungen und überprüfen Sie anschließend die Konnektivität und Routing-Pfade mit `traceroute`.
2. **[Interaktion auf Netzwerkebene mit ping und arp in Linux erkunden](https://labex.io/de/labs/comptia-explore-network-layer-interaction-with-ping-and-arp-in-linux-592746)** - Erfahren Sie, wie `ping` und `arp` zusammenarbeiten, um Interaktionen auf Netzwerkebene zu verstehen, was grundlegende Konzepte dafür sind, wie `traceroute` funktioniert.

Diese Labs helfen Ihnen, die Konzepte der Netzwerkdiagnose in realen Szenarien anzuwenden und Vertrauen in wesentliche Linux-Netzwerktools aufzubauen.

## Quiz Question

Was wird bei den Hops über das Netzwerk um eins dekrementiert? (Bitte antworten Sie auf Englisch und achten Sie auf die Groß-/Kleinschreibung.)

## Quiz Answer

TTL
