---
index: 4
lang: "de"
title: "Network Manager"
meta_title: "Network Manager - Netzwerkkonfiguration"
meta_description: "Erfahren Sie mehr über NetworkManager in Linux, wie er die Netzwerkkonfiguration automatisiert und verwenden Sie die Befehle nm-tool & nmcli. Starten Sie mit diesem Anfängerleitfaden!"
meta_keywords: "NetworkManager, nm-tool, nmcli, Linux-Netzwerk, Netzwerkkonfiguration, Linux-Tutorial, Anfängerleitfaden"
---

## Lesson Content

Wenn Sie möchten, dass die Netzwerkfunktionen Ihres Systems automatisch eingerichtet und ausgeführt werden, gibt es dafür natürlich bereits eine Lösung. Die meisten Distributionen verwenden den NetworkManager-Daemon, um ihre Netzwerke automatisch zu konfigurieren.

Sie werden NetworkManager in Form eines Applets irgendwo in der Taskleiste Ihres Desktops bemerken, wenn Sie eine GUI verwenden. Wie Sie sehen können, verwaltet es die Hardware- und Verbindungsinformationen Ihres Netzwerks. Zum Beispiel sammelt NetworkManager beim Start Hardwareinformationen des Netzwerks, sucht nach Verbindungen (drahtlos, kabelgebunden usw.) und aktiviert diese dann.

Es gibt auch Befehlszeilentools zur Interaktion mit NetworkManager:

### nm-tool

`nm-tool` meldet den Status von NetworkManager und dessen Geräten.

```plaintext
pete@icebox:/$ nm-tool
NetworkManager Tool

State: connected (global)

- Device: eth0  [Wired connection 1] -------------------------------------------
  Type:              Wired
  Driver:            pcnet32
  State:             connected
  Default:           yes
  HW Address:        12:3D:45:56:7D:CC

  Capabilities:
    Carrier Detect:  yes

  Wired Properties
    Carrier:         on

  IPv4 Settings:
    Address:         192.168.22.1
    Prefix:          24 (255.255.255.0)
    Gateway:         192.168.22.2

    DNS:             192.168.22.2
```

### nmcli

Der Befehl `nmcli` ermöglicht Ihnen die Steuerung und Änderung von NetworkManager. Weitere Details finden Sie in der Manpage.

## Exercise

Übung macht den Meister! Während NetworkManager einen Großteil der Netzwerkkonfiguration automatisiert, ist das Verständnis der zugrunde liegenden Befehle und Konzepte, die es verwaltet, entscheidend für die Fehlerbehebung und fortgeschrittene Administration. Hier sind einige praktische Übungen, um Ihr Verständnis der Netzwerkidentifikation und -verwaltung in Linux zu vertiefen:

1. **[MAC- und IP-Adressen in Linux identifizieren](https://labex.io/de/labs/comptia-identify-mac-and-ip-addresses-in-linux-592731)** - Üben Sie die Verwendung des Befehls `ip a`, um Netzwerkinformationen, einschließlich MAC- und IP-Adressen, auf einem Linux-System zu identifizieren.
2. **[IP-Adressierung in Linux verwalten](https://labex.io/de/labs/comptia-manage-ip-addressing-in-linux-592736)** - Lernen Sie, statische und dynamische IP-Adressen zu konfigurieren, Standard-Gateways festzulegen und Netzwerkkonfigurationen mit dem Befehl `ip` und `dhclient` zu überprüfen.
3. **[Netzwerkschicht-Interaktion mit ping und arp in Linux erkunden](https://labex.io/de/labs/comptia-explore-network-layer-interaction-with-ping-and-arp-in-linux-592746)** - Verwenden Sie `ping` und `arp`, um zu verstehen, wie Netzwerk- und Datenverbindungsschichten interagieren, beobachten Sie ARP in Aktion und wie Standard-Gateways den Datenverkehr handhaben.

Diese Übungen helfen Ihnen, die Konzepte der Netzwerkidentifikation und -konfiguration in realen Szenarien anzuwenden und Vertrauen in die Grundlagen der Linux-Netzwerktechnik aufzubauen.

## Quiz Question

Wie lautet der Befehl zum Anzeigen von NetworkManager-Informationen?

## Quiz Answer

nm-tool
