---
index: 5
lang: "de"
title: "arp"
meta_title: "arp - Netzwerkkonfiguration"
meta_description: "Erfahren Sie mehr über den Linux ARP-Befehl und wie Sie Ihren ARP-Cache anzeigen können. Verstehen Sie die Rolle von ARP in der Netzwerkkommunikation. Ein Leitfaden für Anfänger zu ARP."
meta_keywords: "Linux ARP, ARP-Cache, ip neighbour show, Netzwerkbefehle, Linux-Netzwerk, Linux für Anfänger, Linux-Tutorial"
---

## Lesson Content

Erinnern Sie sich, wenn wir eine MAC-Adresse mit ARP nachschlagen, prüft es zuerst den lokal gespeicherten ARP-Cache auf unserem System. Sie können diesen Cache tatsächlich einsehen:

```
pete@icebox:~$ arp
Address                  HWtype  HWaddress           Flags Mask            Iface
192.168.22.1            ether   00:12:24:fc:12:cc   C                     eth0
192.168.22.254          ether   00:12:45:f2:84:64   C                     eth0
```

Der ARP-Cache ist tatsächlich leer, wenn ein Computer hochfährt; er wird gefüllt, wenn Pakete an andere Hosts gesendet werden. Wenn wir ein Paket an ein Ziel senden, das sich nicht im ARP-Cache befindet, geschieht Folgendes:

1. Der Quell-Host erstellt den Ethernet-Frame mit einem ARP-Anfragepaket.
2. Der Quell-Host sendet diesen Frame als Broadcast an das gesamte Netzwerk.
3. Wenn einer der Hosts im Netzwerk die korrekte MAC-Adresse kennt, sendet er ein Antwortpaket und einen Frame, der die MAC-Adresse enthält.
4. Der Quell-Host fügt die IP-zu-MAC-Adresszuordnung zum ARP-Cache hinzu und fährt dann mit dem Senden des Pakets fort.

Sie können Ihren ARP-Cache auch über den Befehl `ip` einsehen:

```bash
ip neighbour show
```

## Exercise

Beobachten Sie, was mit Ihrem ARP-Cache passiert, wenn Sie Ihren Computer neu starten und dann etwas im Netzwerk tun.

## Quiz Question

Welchen Befehl können Sie verwenden, um Ihren ARP-Cache anzuzeigen?

## Quiz Answer

arp
