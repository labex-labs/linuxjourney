---
index: 1
lang: "de"
title: "IPv4"
meta_title: "IPv4 - Subnetting"
meta_description: "Erfahren Sie mehr über IPv4-Adressen, ihre Struktur und wie Sie Ihre IP mit ifconfig finden. Verstehen Sie die Grundlagen des Netzwerks für Linux-Anfänger."
meta_keywords: "IPv4, IP-Adresse, ifconfig, Netzwerk-Grundlagen, Linux-Netzwerk, Anfänger, Tutorial, Anleitung"
---

## Lesson Content

Wir wissen also, dass Netzwerk-Hosts eine eindeutige Adresse haben, unter der sie gefunden werden können. Diese Adressen werden als IP-Adressen bezeichnet. Eine IPv4-Adresse sieht etwa so aus:

```
204.23.124.23
```

Diese Adresse enthält tatsächlich zwei Teile: den Netzwerkanteil, der uns sagt, in welchem Netzwerk sie sich befindet, und den Host-Anteil, der uns sagt, welcher Host in diesem Netzwerk es ist. In diesem Kurs werden wir uns hauptsächlich mit IPv4-Adressen befassen, die Sie üblicherweise sehen werden, wenn von IP-Adressen die Rede ist.

Eine IP-Adresse wird durch Punkte in Oktette unterteilt. Eine IPv4-Adresse besteht also aus 4 Oktetten. Wenn Sie ein wenig Informatikkenntnisse haben, ist ein Oktett 8 Bit, und 8 Bit entsprechen tatsächlich 1 Byte, daher bezeichnen wir eine IPv4-Adresse auch als 4 Bytes. Wir verwenden Bits häufig, wenn wir uns mit Subnetzen und IP-Adressen befassen.

Sie können Ihre IP-Adresse mit dem Befehl `ifconfig -a` anzeigen:

```bash
pete@icebox:~$ ifconfig -a
eth0      Link encap:Ethernet  HWaddr 1d:3a:32:24:4d:ce
          inet addr:192.168.1.129  Bcast:192.168.1.255  Mask:255.255.255.0
          inet6 addr: fd60::21c:29ff:fe63:5cdc/64 Scope:Link
```

Wie Sie sehen können, lautet meine IPv4-Adresse: 192.168.1.129

## Exercise

Übung macht den Meister! Hier sind einige praktische Übungen, um Ihr Verständnis von IP-Adressierung und Netzwerkidentifikation in Linux zu vertiefen:

1. **[MAC- und IP-Adressen in Linux identifizieren](https://labex.io/de/labs/comptia-identify-mac-and-ip-addresses-in-linux-592731)** – Üben Sie die Verwendung des Befehls `ip a`, um Netzwerkinformationen, einschließlich IPv4- und IPv6-Adressen, auf einem Linux-System zu identifizieren.
2. **[IP-Adresstypen und Erreichbarkeit in Linux erkunden](https://labex.io/de/labs/comptia-explore-ip-address-types-and-reachability-in-linux-592780)** – Erkunden Sie verschiedene IP-Adresstypen und testen Sie die Netzwerkerreichbarkeit mit Befehlen wie `ping` und `ip a`.
3. **[IP-Subnetting und Binärkonvertierung im Linux-Terminal durchführen](https://labex.io/de/labs/comptia-perform-ip-subnetting-and-binary-conversion-in-the-linux-terminal-592782)** – Meistern Sie IP-Subnetting und Binärkonvertierung, unerlässlich für ein tieferes Verständnis, wie IP-Adressen und Netzwerke auf Bitebene strukturiert sind.

Diese Übungen helfen Ihnen, die Konzepte der IP-Adressierung in realen Szenarien anzuwenden und Vertrauen in die Netzwerkkonfiguration und Fehlerbehebung in Linux aufzubauen.

## Quiz Question

Wie viele Bytes hat eine IPv4-Adresse?

## Quiz Answer

4
