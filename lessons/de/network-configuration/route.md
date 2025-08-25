---
index: 2
lang: "de"
title: "route"
meta_title: "route - Netzwerkkonfiguration"
meta_description: "Erfahren Sie, wie Sie Netzwerkrouten mit den Linux-Befehlen route und ip hinzufügen und löschen. Verstehen Sie die Verwaltung von Routing-Tabellen für Anfänger und fortgeschrittene Benutzer."
meta_keywords: "route Befehl, ip route, Route hinzufügen, Route löschen, Linux-Netzwerk, Routing-Tabelle, Linux-Tutorial, Anfängerleitfaden"
---

## Lesson Content

Wir haben bereits die Anzeige unserer Routing-Tabellen mit dem Befehl `route` besprochen. Wenn Sie Routen hinzufügen oder entfernen möchten, können Sie dies manuell tun.

### Eine neue Route hinzufügen

```bash
sudo route add -net 192.168.2.1/23 gw 10.11.12.3
```

### Eine Route löschen

```bash
sudo route del -net 192.168.2.1/23
```

Sie können diese Änderungen auch mit dem Befehl **ip** vornehmen:

### Eine Route hinzufügen

```bash
ip route add 192.168.2.1/23 via 10.11.12.3
```

### Eine Route löschen

```bash
$ ip route delete 192.168.2.1/23 via 10.11.12.3
or
$ ip route delete 192.168.2.1/23
```

## Exercise

Übung macht den Meister! Hier sind einige praktische Übungen, um Ihr Verständnis von Netzwerk-Routing und IP-Adressierung zu vertiefen:

1. **[IP-Adressierung in Linux verwalten](https://labex.io/de/labs/linux-manage-ip-addressing-in-linux-592736)** – Üben Sie das Konfigurieren einer statischen IP, das Festlegen eines Standard-Gateways und das Überprüfen der Netzwerkkonfiguration mit dem Befehl `ip`.
2. **[Netzwerkschicht-Interaktion mit ping und arp in Linux erkunden](https://labex.io/de/labs/linux-explore-network-layer-interaction-with-ping-and-arp-in-linux-592746)** – Erfahren Sie, wie das Standard-Gateway den Remote-Verkehr handhabt und beobachten Sie Netzwerkschicht-Interaktionen.

Diese Übungen helfen Ihnen, die Konzepte der IP-Adressierung und des Routings in realen Szenarien anzuwenden und Vertrauen in die Linux-Netzwerkverwaltung aufzubauen.

## Quiz Question

Was ist das Befehls-Flag zum Löschen einer Route?

## Quiz Answer

del
