---
index: 9
lang: "de"
title: "DHCP-Übersicht"
meta_title: "DHCP-Übersicht - Netzwerk-Grundlagen"
meta_description: "Erfahren Sie mehr über DHCP (Dynamic Host Configuration Protocol) in Linux. Verstehen Sie, wie DHCP IP-Adressen zuweist und seinen vierstufigen Prozess. Beginnen Sie Ihre Linux-Netzwerkreise!"
meta_keywords: "DHCP, Dynamic Host Configuration Protocol, Linux-Netzwerk, IP-Adresse, DHCP-Tutorial, Anfänger, Leitfaden"
---

## Lesson Content

Ein wichtiges Netzwerkkonzept, das wir noch nicht behandelt haben, ist DHCP (Dynamic Host Configuration Protocol).

DHCP weist unseren Maschinen IP-Adressen, Subnetzmasken und Gateways zu. Nehmen wir zum Beispiel an, Sie haben ein Mobiltelefon und möchten eine Mobiltelefonnummer erhalten, um mit anderen Leuten zu sprechen. Sie müssen Ihren Telefonanbieter anrufen, und dieser gibt Ihnen eine Nummer. Solange Sie Ihre Rechnungen bezahlen, können Sie Ihr Telefon weiter nutzen. DHCP ist in diesem Fall der Telefonanbieter; es gibt Ihnen eine IP-Adresse, damit Sie mit anderen IP-Adressen kommunizieren können. Ihnen wird auch eine IP-Adresse zugewiesen; diese gilt für einen bestimmten Zeitraum und wird dann je nach Ihren Lease-Einstellungen erneuert.

DHCP ist aus vielen Gründen großartig: Es ermöglicht einem Netzwerkadministrator, sich nicht um die Zuweisung von IP-Adressen kümmern zu müssen, und es verhindert auch, dass doppelte IP-Adressen eingerichtet werden. Jedes physische Netzwerk sollte seinen eigenen DHCP-Server haben, damit ein Host eine IP-Adresse anfordern kann. In einer normalen Heimumgebung fungiert der Router normalerweise als DHCP-Server.

DHCP erhält alle Ihre dynamischen Host-Informationen auf folgende Weise:

1. DHCP DISCOVER - Diese Nachricht wird gesendet, um nach einem DHCP-Server zu suchen.
2. DHCP OFFER - Der DHCP-Server im Netzwerk antwortet mit einer Angebotsnachricht. Das Angebot enthält ein Paket mit DHCP-Lease-Zeit, Subnetzmaske, IP-Adresse usw.
3. DHCP REQUEST - Der Client sendet eine weitere Broadcast-Nachricht, um alle DHCP-Server wissen zu lassen, welches Angebot er angenommen hat.
4. DHCP ACK - Die Bestätigung wird vom Server gesendet.

DHCP ist komplexer als das, aber das ist die Essenz davon.

## Exercise

Übung macht den Meister! Hier sind einige praktische Übungen, um Ihr Verständnis der dynamischen IP-Adressierung und Netzwerkkonfiguration zu vertiefen:

1. **[IP-Adressierung in Linux verwalten](https://labex.io/de/labs/comptia-manage-ip-addressing-in-linux-592736)** - Üben Sie die Verwendung des `ip`-Befehls, um Schnittstellen zu inspizieren und speziell `dhclient` zu verwenden, um eine dynamische IP-Adresse zu erhalten, wodurch Sie Ihr Wissen über DHCP direkt anwenden.
2. **[MAC- und IP-Adressen in Linux identifizieren](https://labex.io/de/labs/comptia-identify-mac-and-ip-addresses-in-linux-592731)** - Lernen Sie, den Befehl `ip a` zu verwenden, um Netzwerkkonfigurationsinformationen, einschließlich der von DHCP zugewiesenen IP-Adressen, zu identifizieren und Netzwerkschnittstellen zu inspizieren.
3. **[IP-Adresstypen und Erreichbarkeit in Linux erkunden](https://labex.io/de/labs/comptia-explore-ip-address-types-and-reachability-in-linux-592780)** - Erkunden Sie die IP-Adressierung und Netzwerk-Erreichbarkeit mit `ping` und `ip a`, was Ihnen hilft zu verstehen, wie dynamisch zugewiesene IPs innerhalb eines Netzwerks funktionieren.

Diese Übungen helfen Ihnen, die Konzepte der dynamischen IP-Zuweisung und Netzwerkkonfiguration in realen Szenarien anzuwenden und Vertrauen in die Linux-Netzwerkverwaltung aufzubauen.

## Quiz Question

Was sind die Schritte bei einer DHCP-Anfrage?

## Quiz Answer

DISCOVER, OFFER, REQUEST, ACK
