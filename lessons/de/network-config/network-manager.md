---
index: 4
lang: "de"
title: "Netzwerkmanager"
meta_title: "Netzwerkmanager - Netzwerkkonfiguration"
meta_description: "Entdecken Sie die Rolle des NetworkManager-Daemons in der modernen Linux-Netzwerkverwaltung. Erfahren Sie, wie dieses Tool die Netzwerkkonfiguration automatisiert und wie Sie mit nm-tool und dem leistungsstarken Befehlszeilenprogramm nmcli interagieren."
meta_keywords: "NetworkManager, nm-tool, nmcli, Netzwerkmanager Linux, networkmanager linux, linux netzwerkmanager, linux netzwerkverwaltung, netzwerkkonfiguration, Linux-Netzwerk"
---

## Lesson Content

Damit die Netzwerkkonfiguration eines Systems automatisch erfolgt, ist typischerweise bereits ein Dienst eingerichtet. Die meisten modernen Linux-Distributionen verwenden dafür den NetworkManager-Daemon, was ihn zu einem Eckpfeiler des **Linux-Netzwerkmanagements** macht.

### Was ist Network Manager unter Linux?

Wenn Sie eine grafische Benutzeroberfläche (GUI) verwenden, werden Sie den Dienst **Network Manager Linux** wahrscheinlich als Applet in der Taskleiste Ihres Desktops bemerken. Dieses Tool verwaltet Ihre Netzwerkhardware und Verbindungsinformationen. Beispielsweise sammelt NetworkManager beim Start Informationen über die Netzwerkhardware, sucht nach verfügbaren Verbindungen (wie drahtlose oder kabelgebundene Netzwerke) und aktiviert diese dann, um Sie online zu bringen.

### Interaktion über die Kommandozeile

Obwohl das GUI-Applet praktisch ist, gibt es auch leistungsstarke Kommandozeilenwerkzeuge, um mit dem Dienst **networkmanager linux** zu interagieren. Diese sind für die Serveradministration und das Skripting unerlässlich.

### Verwendung von nm-tool

Der Befehl `nm-tool` meldet den aktuellen Zustand von NetworkManager und eine Liste der verwalteten Geräte. Beachten Sie, dass `nm-tool` auf vielen modernen Systemen zugunsten von `nmcli` als veraltet gilt.

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

### Das moderne nmcli-Tool

Der Befehl `nmcli` ist das primäre Kommandozeilenwerkzeug zur Steuerung und Änderung des **Linux Network Manager**. Er ermöglicht es Ihnen, den Status anzuzeigen, Verbindungen zu verwalten und Netzwerkgeräte direkt über das Terminal zu konfigurieren. Eine vollständige Liste seiner Fähigkeiten finden Sie in seiner Manpage (`man nmcli`).

## Exercise

Übung macht den Meister! Während NetworkManager einen Großteil der Netzwerkkonfiguration automatisiert, ist das Verständnis der zugrunde liegenden Befehle und Konzepte, die es verwaltet, für die Fehlerbehebung und fortgeschrittene Administration entscheidend. Hier sind einige praktische Labs, um Ihr Verständnis der Netzwerkerkennung und -verwaltung unter Linux zu festigen:

1. **[MAC- und IP-Adressen unter Linux identifizieren](https://labex.io/de/labs/comptia-identify-mac-and-ip-addresses-in-linux-592731)** - Üben Sie die Verwendung des Befehls `ip a`, um Netzwerkadressinformationen, einschließlich MAC- und IP-Adressen, auf einem Linux-System zu identifizieren.
2. **[IP-Adressierung unter Linux verwalten](https://labex.io/de/labs/comptia-manage-ip-addressing-in-linux-592736)** - Lernen Sie, statische und dynamische IP-Adressen zu konfigurieren, Standard-Gateways festzulegen und Netzwerkkonfigurationen mithilfe des Befehls `ip` und `dhclient` zu überprüfen.
3. **[Interaktion auf Netzwerkebene mit ping und arp unter Linux erkunden](https://labex.io/de/labs/comptia-explore-network-layer-interaction-with-ping-and-arp-in-linux-592746)** - Verwenden Sie `ping` und `arp`, um zu verstehen, wie die Netzwerk- und Data-Link-Schichten interagieren, beobachten Sie ARP in Aktion und wie Standard-Gateways den Datenverkehr verarbeiten.

Diese Labs helfen Ihnen, die Konzepte der Netzwerkerkennung und -konfiguration in realen Szenarien anzuwenden und Vertrauen in die Grundlagen der Linux-Netzwerkkonfiguration aufzubauen.

## Quiz Question

Was ist der Befehl, um eine Zusammenfassung des Zustands und der Geräte von NetworkManager anzuzeigen, wie in der Lektion gezeigt? Bitte antworten Sie nur mit dem englischen Befehlsnamen in Kleinbuchstaben.

## Quiz Answer

nm-tool
