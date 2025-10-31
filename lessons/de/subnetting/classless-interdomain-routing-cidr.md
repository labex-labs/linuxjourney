---
index: 5
lang: "de"
title: "CIDR"
meta_title: "CIDR - Subnetzmaskierung"
meta_description: "Ein Leitfaden zur CIDR-Notation. Erfahren Sie mehr über das CIDR-Format, CIDR-Subnetzmaskierung und wie Sie Hosts für Ihr Netzwerk berechnen, auch auf einem Ubuntu-Server. Meistern Sie die IP-Adressierung mit CIDR."
meta_keywords: "CIDR, CIDR Subnetzmaskierung, CIDR Format, Subnetzmaske, IP-Adressierung, Ubuntu Server Subnetz CIDR, Ubuntu Subnetz CIDR, Netzwerkpräfix, Linux Networking"
---

## Lesson Content

CIDR (Classless Inter-Domain Routing) ist eine Methode zur Zuweisung von IP-Adressen und zum Routing von Internet Protocol-Paketen. Es bietet eine kompaktere und effizientere Möglichkeit, eine Subnetzmaske darzustellen und ersetzt das ältere klassenbasierte Netzwerkdesign. Das Verständnis von CIDR ist für die moderne Netzwerkadministration unerlässlich.

### Das CIDR-Format

Sie werden Netzwerke häufig in der **CIDR-Notation** sehen, wobei auf eine IP-Adresse ein Schrägstrich und eine Zahl folgt. Zum Beispiel wird ein Subnetz wie `10.42.3.0` mit einer Subnetzmaske von `255.255.255.0` als `10.42.3.0/24` geschrieben. Diese einzelne Notation enthält sowohl die Netzadresse als auch die Präfixlänge.

Die Zahl nach dem Schrägstrich gibt an, wie viele Bits der IP-Adresse für das Netzwerkpräfix verwendet werden. Dies ist eine häufige Aufgabe bei der Konfiguration der Netzwerke auf einem System wie einem **Ubuntu-Server**, wo Sie möglicherweise eine Schnittstelle mit einer `ubuntu subnet cidr`-Adresse definieren.

### CIDR-Subnetting und Host-Berechnung

Eine IPv4-Adresse besteht aus 4 Bytes, also insgesamt 32 Bits. Das CIDR-Präfix bestimmt die Aufteilung zwischen dem Netzwerk- und dem Host-Teil der Adresse. Für effektives **cidr subnetting** müssen Sie wissen, wie man die Anzahl der verfügbaren Hosts berechnet.

Nehmen wir das Beispiel `123.12.24.0/23`. Dies bedeutet, dass die ersten 23 Bits das Netzwerkpräfix sind. Um die Anzahl der verfügbaren Hosts zu ermitteln:

1. Subtrahieren Sie das CIDR-Präfix von der Gesamtanzahl der Bits (32): `32 - 23 = 9`. Dies ergibt 9 Bits für den Host-Teil.
2. Berechnen Sie die Gesamtanzahl der Adressen im Subnetz: `2^9 = 512`.
3. Subtrahieren Sie 2 von der Gesamtzahl. Eine Adresse ist für das Netzwerk selbst reserviert, und eine für die Broadcast-Adresse. Dies ergibt `512 - 2 = 510` nutzbare Host-Adressen.

Ein weiteres häufiges Beispiel ist ein `/30`-Netzwerk, das `32 - 30 = 2` Host-Bits bereitstellt. Dies führt zu `2^2 = 4` Gesamtadressen, wobei nur 2 nutzbare Adressen übrig bleiben, was es ideal für Punkt-zu-Punkt-Verbindungen macht.

## Exercise

Um diese Konzepte zu beherrschen, üben Sie mit einigen praktischen Labs, die Ihr Verständnis von CIDR, IP-Adressierung und **cidr subnetting** vertiefen:

1. **[Führen Sie IP-Subnetting und Binärkonvertierung im Linux-Terminal durch](https://labex.io/de/labs/comptia-perform-ip-subnetting-and-binary-conversion-in-the-linux-terminal-592782)** - Meistern Sie IP-Subnetting und Binärkonvertierung, einschließlich der Übersetzung von CIDR-Masken und der Berechnung nutzbarer Hosts.
2. **[Simulieren Sie die Konnektivität auf der Netzwerkschicht in Linux](https://labex.io/de/labs/comptia-simulate-network-layer-connectivity-in-linux-592752)** - Lernen Sie, statische IP-Adressen zuzuweisen und zu beobachten, wie IP-Subnetze die direkte Netzwerkkommunikation in einer simulierten Umgebung steuern.
3. **[Erkunden Sie IP-Adresstypen und Erreichbarkeit in Linux](https://labex.io/de/labs/comptia-explore-ip-address-types-and-reachability-in-linux-592780)** - Untersuchen Sie die IP-Adressierung und die Netzwerkerreichbarkeit mithilfe von Befehlen wie `ping` und `ip a`, um verschiedene IP-Typen und Konnektivität zu testen.

Diese Labs helfen Ihnen, die Konzepte von CIDR und IP-Adressierung in realen Szenarien anzuwenden und Vertrauen in die Netzwerkkonfiguration aufzubauen.
