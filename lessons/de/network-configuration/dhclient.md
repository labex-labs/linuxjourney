---
index: 3
lang: "de"
title: "dhclient"
meta_title: "dhclient - Netzwerkkonfiguration"
meta_description: "Erfahren Sie mehr über dhclient, wie es IP-Adressen mithilfe von DHCP bezieht und Netzwerk-Leases verwaltet. Verstehen Sie die Dateien dhclient.conf und dhclient.leases. Linux-Anfängerleitfaden."
meta_keywords: "dhclient, DHCP, Linux-Netzwerk, IP-Adresse, Netzwerkkonfiguration, Linux-Tutorial, Anfängerleitfaden"
---

## Lesson Content

Wir haben DHCP bereits besprochen, und meistens müssen Sie Ihre IP-Adressen, Subnetzmasken usw. niemals statisch festlegen. Stattdessen verwenden Sie DHCP! Der `dhclient` startet beim Booten und erhält eine Liste der Netzwerkschnittstellen aus der Datei `dhclient.conf`. Für jede aufgelistete Schnittstelle versucht er, die Schnittstelle mithilfe des DHCP-Protokolls zu konfigurieren.

In der Datei `dhclient.leases` verfolgt `dhclient` eine Liste von Leases über Systemneustarts hinweg. Nach dem Lesen von `dhclient.conf` wird die Datei `dhclient.leases` gelesen, um zu erfahren, welche Leases bereits zugewiesen wurden.

### Eine neue IP beziehen

```bash
sudo dhclient
```

## Exercise

Übung macht den Meister! Hier sind einige praktische Übungen, um Ihr Verständnis der dynamischen IP-Adressierung und Netzwerkkonfiguration zu vertiefen:

1. **[IP-Adressierung in Linux verwalten](https://labex.io/de/labs/linux-manage-ip-addressing-in-linux-592736)** – Üben Sie die Verwendung von `dhclient`, um eine dynamische IP-Adresse zu erhalten und die Netzwerkkonfiguration in einer echten Linux-Umgebung zu überprüfen.
2. **[MAC- und IP-Adressen in Linux identifizieren](https://labex.io/de/labs/linux-identify-mac-and-ip-addresses-in-linux-592731)** – Lernen Sie, Netzwerkschnittstellen zu inspizieren und MAC- und IP-Adressen zu identifizieren, die grundlegend für das Verständnis sind, wie DHCP Adressen zuweist.
3. **[IP-Adresstypen und Erreichbarkeit in Linux erkunden](https://labex.io/de/labs/linux-explore-ip-address-types-and-reachability-in-linux-592780)** – Testen Sie die Netzwerkerreichbarkeit und erkunden Sie verschiedene IP-Adresstypen, um Ihr Verständnis der Funktionsweise von IP-Adressen in einem Netzwerk zu vertiefen.

Diese Übungen helfen Ihnen, die Konzepte von DHCP und IP-Adressierung in realen Szenarien anzuwenden und Vertrauen in die Netzwerkkonfiguration unter Linux aufzubauen.

## Quiz Question

Was versucht, IP-Adressen mit dem DHCP-Protokoll zuzuweisen?

## Quiz Answer

dhclient
