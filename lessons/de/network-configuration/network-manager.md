---
index: 4
lang: "de"
title: "Netzwerkmanager"
meta_title: "Netzwerkmanager - Netzwerkkonfiguration"
meta_description: "Erfahren Sie mehr über NetworkManager in Linux, wie er die Netzwerkkonfiguration automatisiert und verwenden Sie die Befehle nm-tool & nmcli. Starten Sie mit diesem Anfängerleitfaden!"
meta_keywords: "NetworkManager, nm-tool, nmcli, Linux-Netzwerk, Netzwerkkonfiguration, Linux-Tutorial, Anfängerleitfaden"
---

## Lesson Content

Wenn Sie möchten, dass die Netzwerkverbindung Ihres Systems automatisch hergestellt wird, gibt es dafür bereits eine Lösung. Die meisten Distributionen verwenden den NetworkManager-Daemon, um ihre Netzwerke automatisch zu konfigurieren.

Sie werden den NetworkManager in Form eines Applets irgendwo in der Taskleiste Ihres Desktops bemerken, wenn Sie eine GUI verwenden. Wie Sie sehen können, verwaltet er die Hardware- und Verbindungsinformationen Ihres Netzwerks. Zum Beispiel sammelt der NetworkManager beim Start Hardwareinformationen des Netzwerks, sucht nach Verbindungen (drahtlos, kabelgebunden usw.) und aktiviert diese dann.

Es gibt auch Befehlszeilentools zur Interaktion mit dem NetworkManager:

### nm-tool

`nm-tool` meldet den Status des NetworkManager und seiner Geräte.

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

Der Befehl `nmcli` ermöglicht Ihnen die Steuerung und Änderung des NetworkManager. Weitere Details finden Sie in der Manpage.

## Exercise

Keine Übungen für diese Lektion.

## Quiz Question

Wie lautet der Befehl, um NetworkManager-Informationen anzuzeigen?

## Quiz Answer

nm-tool
