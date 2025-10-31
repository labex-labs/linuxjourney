---
index: 3
lang: "de"
title: "Subnetz-Mathematik"
meta_title: "Subnetz-Mathematik - Subnetting"
meta_description: "Meistern Sie die Grundlagen der Subnetz-Mathematik. Diese Anleitung erklärt, wie man Subnetzmasken-Berechnungen durchführt, um die Anzahl der verfügbaren Hosts in Ihrem Netzwerk zu ermitteln. Lernen Sie wesentliche IP-Adressierungs- und Binärkonzepte für Linux-Netzwerke."
meta_keywords: "Subnetz-Mathematik, Subnetzmasken-Berechnung, IP-Adresse, Subnetzmaske, Netzwerk-Hosts, Binär, Linux-Netzwerke, Host-Berechnung, Anfänger-Tutorial"
---

## Lesson Content

Um die Anzahl der Hosts zu bestimmen, die ein Subnetz unterstützen kann, müssen Sie einige Grundlagen der **Subnetz-Mathematik** verstehen. Die Subnetzmaske ist der Schlüssel zu dieser Berechnung.

### Die Rolle der Subnetzmaske

Nehmen wir eine IP-Adresse von **192.168.1.0** mit einer Subnetzmaske von **255.255.255.0**.
Die Hauptfunktion der Subnetzmaske besteht darin, den Netzwerkanteil der Adresse vom Hostanteil zu unterscheiden.

Um zu sehen, wie dies funktioniert, können wir diese Werte in ihre binäre Form umwandeln.

```
192.168.1.165  = 11000000.10101000.00000001.10100101
255.255.255.0  = 11111111.11111111.11111111.00000000
```

### Durchführung der Subnetzmasken-Mathematik

In der obigen binären Darstellung entsprechen die `1`en in der Subnetzmaske dem Netzwerkanteil der IP-Adresse. Dieser Teil ist "maskiert" oder fest. Die `0`en in der Subnetzmaske entsprechen dem Hostanteil, der den Adressbereich darstellt, den Sie Geräten zuweisen können.

In unserem Beispiel ist der Hostanteil `00000000`. Dies ist ein 8-Bit-Feld, und mit 8 Bits können Sie 2^8 oder 256 eindeutige Kombinationen erstellen (von 0 bis 255).

### Berechnung der verfügbaren Hosts

Obwohl es 256 mögliche Kombinationen gibt, können nicht alle Geräten zugewiesen werden. In jedem Subnetz sind zwei Adressen reserviert:

1. **Netzwerkadresse:** Die erste Adresse, bei der alle Host-Bits `0` sind (z. B. 192.168.1.0).
2. **Broadcast-Adresse:** Die letzte Adresse, bei der alle Host-Bits `1` sind (z. B. 192.168.1.255).

Daher beträgt die tatsächliche Anzahl nutzbarer Hosts 256 - 2 = 254. Das bedeutet, für das Netzwerk `192.168.1.0` mit der Maske `255.255.255.0` können Sie IP-Adressen von `192.168.1.1` bis `192.168.1.254` zuweisen. Diese Kernberechnung ist ein grundlegender Bestandteil der **Subnetz-Mathematik**.

## Exercise

Übung macht den Meister! Hier sind einige praktische Labs, um Ihr Verständnis von IP-Adressierung und Subnetting zu festigen:

1. **[IP-Subnetting und Binärkonvertierung im Linux-Terminal durchführen](https://labex.io/de/labs/comptia-perform-ip-subnetting-and-binary-conversion-in-the-linux-terminal-592782)** - Meistern Sie IP-Subnetting und Binärkonvertierung, wesentliche Fähigkeiten für die Netzwerkkonfiguration und -planung.
2. **[IP-Adresstypen und Erreichbarkeit unter Linux untersuchen](https://labex.io/de/labs/comptia-explore-ip-address-types-and-reachability-in-linux-592780)** - Vertiefen Sie Ihr Verständnis verschiedener IP-Adresstypen und wie Sie die Netzwerkerreichbarkeit mithilfe von Linux-Befehlen überprüfen.
3. **[Konnektivität auf der Netzwerkebene in Linux simulieren](https://labex.io/de/labs/comptia-simulate-network-layer-connectivity-in-linux-592752)** - Wenden Sie Ihr Wissen an, indem Sie Netzwerkkonfigurationen simulieren und die Konnektivität zwischen verschiedenen IP-Subnetzen in einer praktischen Umgebung testen.

Diese Labs helfen Ihnen, die Konzepte von IP-Adressierung, Subnetzmasken und Host-Berechnung in realen Szenarien anzuwenden und Selbstvertrauen in die Netzwerk-Grundlagen aufzubauen.

## Quiz Question

Was ist das binäre Äquivalent von 255?

## Quiz Answer

11111111
