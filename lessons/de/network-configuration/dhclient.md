---
index: 3
lang: "de"
title: "dhclient"
meta_title: "dhclient - Netzwerkkonfiguration"
meta_description: "Erfahren Sie mehr über dhclient, wie es IP-Adressen mithilfe von DHCP bezieht und Netzwerk-Leases verwaltet. Verstehen Sie die Dateien dhclient.conf und dhclient.leases. Linux-Anfängerleitfaden."
meta_keywords: "dhclient, DHCP, Linux-Netzwerk, IP-Adresse, Netzwerkkonfiguration, Linux-Tutorial, Anfängerleitfaden"
---

## Lesson Content

Wir haben DHCP bereits besprochen, und meistens werden Sie Ihre IP-Adressen, Subnetzmasken usw. niemals statisch festlegen müssen. Stattdessen werden Sie DHCP verwenden! Der `dhclient` startet beim Booten und erhält eine Liste der Netzwerkschnittstellen aus der Datei `dhclient.conf`. Für jede aufgelistete Schnittstelle versucht er, die Schnittstelle mithilfe des DHCP-Protokolls zu konfigurieren.

In der Datei `dhclient.leases` verfolgt `dhclient` eine Liste von Leases über Systemneustarts hinweg. Nach dem Lesen von `dhclient.conf` wird die Datei `dhclient.leases` gelesen, um zu erfahren, welche Leases bereits zugewiesen wurden.

### Eine neue IP erhalten

```bash
sudo dhclient
```

## Exercise

No exercises for this lesson.

## Quiz Question

Was versucht, IP-Adressen mit dem DHCP-Protokoll zuzuweisen?

## Quiz Answer

dhclient
