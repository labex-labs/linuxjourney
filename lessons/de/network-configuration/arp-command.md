---
index: 5
lang: "de"
title: "arp"
meta_title: "arp - Netzwerkkonfiguration"
meta_description: "Erfahren Sie mehr über den Linux ARP-Befehl und wie Sie Ihren ARP-Cache anzeigen können. Verstehen Sie die Rolle von ARP in der Netzwerkkommunikation. Ein Leitfaden für Anfänger zu ARP."
meta_keywords: "Linux ARP, ARP-Cache, ip neighbour show, Netzwerkbefehle, Linux-Netzwerk, Linux für Anfänger, Linux-Tutorial"
---

## Lesson Content

Erinnern Sie sich, wenn wir eine MAC-Adresse mit ARP nachschlagen, prüft es zuerst den lokal gespeicherten ARP-Cache auf unserem System. Sie können diesen Cache tatsächlich anzeigen:

```
pete@icebox:~$ arp
Address                  HWtype  HWaddress           Flags Mask            Iface
192.168.22.1            ether   00:12:24:fc:12:cc   C                     eth0
192.168.22.254          ether   00:12:45:f2:84:64   C                     eth0
```

Der ARP-Cache ist tatsächlich leer, wenn eine Maschine hochfährt; er wird gefüllt, wenn Pakete an andere Hosts gesendet werden. Wenn wir ein Paket an ein Ziel senden, das sich nicht im ARP-Cache befindet, geschieht Folgendes:

1. Der Quell-Host erstellt den Ethernet-Frame mit einem ARP-Anfragepaket.
2. Der Quell-Host sendet diesen Frame als Broadcast an das gesamte Netzwerk.
3. Wenn einer der Hosts im Netzwerk die korrekte MAC-Adresse kennt, sendet er ein Antwortpaket und einen Frame, der die MAC-Adresse enthält.
4. Der Quell-Host fügt die IP-zu-MAC-Adresszuordnung zum ARP-Cache hinzu und fährt dann mit dem Senden des Pakets fort.

Sie können Ihren ARP-Cache auch über den Befehl `ip` anzeigen:

```bash
ip neighbour show
```

## Exercise

Übung macht den Meister! Hier sind einige praktische Übungen, um Ihr Verständnis von ARP und der Interaktion auf der Netzwerkschicht zu vertiefen:

1. **[Erkunden Sie die Netzwerkschicht-Interaktion mit ping und arp in Linux](https://labex.io/de/labs/comptia-explore-network-layer-interaction-with-ping-and-arp-in-linux-592746)** – Verwenden Sie die Befehle `ping` und `arp`, um zu beobachten, wie IP-Adressen in MAC-Adressen aufgelöst werden und wie das Standard-Gateway den Datenverkehr handhabt.
2. **[Identifizieren Sie MAC- und IP-Adressen in Linux](https://labex.io/de/labs/comptia-identify-mac-and-ip-addresses-in-linux-592731)** – Lernen Sie, den Befehl `ip a` zu verwenden, um Netzwerkkonfigurationsinformationen, einschließlich MAC- und IP-Adressen, zu identifizieren, die für das Verständnis von ARP grundlegend sind.
3. **[Verwalten Sie die IP-Adressierung in Linux](https://labex.io/de/labs/comptia-manage-ip-addressing-in-linux-592736)** – Üben Sie die Verwaltung der IP-Adressierung mit dem Befehl `ip` und überprüfen Sie die Netzwerkkonfiguration mit `arp` und `traceroute`.

Diese Übungen helfen Ihnen, die Konzepte von ARP und der Netzwerkadressierung in realen Szenarien anzuwenden und Vertrauen in die Linux-Netzwerkverwaltung aufzubauen.

## Quiz Question

Welchen Befehl können Sie verwenden, um Ihren ARP-Cache anzuzeigen?

## Quiz Answer

arp
