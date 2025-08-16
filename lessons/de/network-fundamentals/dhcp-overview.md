---
lang: "de"
title: "DHCP-Übersicht"
description: "Erfahren Sie mehr über DHCP (Dynamic Host Configuration Protocol) in Linux. Verstehen Sie, wie DHCP IP-Adressen zuweist und seinen vierstufigen Prozess. Beginnen Sie Ihre Linux-Netzwerkreise!"
keywords: "DHCP, Dynamic Host Configuration Protocol, Linux-Netzwerk, IP-Adresse, DHCP-Tutorial, Anfänger, Leitfaden"
---

## Lesson Content

Ein wichtiges Netzwerkkonzept, das wir noch nicht behandelt haben, ist DHCP (Dynamic Host Configuration Protocol).

DHCP weist unseren Maschinen IP-Adressen, Subnetzmasken und Gateways zu. Nehmen wir zum Beispiel an, Sie haben ein Mobiltelefon und möchten eine Mobiltelefonnummer erhalten, um mit Leuten zu sprechen. Sie müssen Ihren Telefonanbieter anrufen, und dieser gibt Ihnen eine Nummer. Solange Sie Ihre Rechnungen bezahlen, können Sie Ihr Telefon weiterhin nutzen. DHCP ist in diesem Fall der Telefonanbieter; es gibt Ihnen eine IP-Adresse, damit Sie mit anderen IP-Adressen kommunizieren können. Ihnen wird auch eine IP-Adresse zugewiesen; diese gelten für einen bestimmten Zeitraum und werden dann je nach Ihren Lease-Einstellungen erneuert.

DHCP ist aus vielen Gründen großartig: Es ermöglicht einem Netzwerkadministrator, sich keine Gedanken über die Zuweisung von IP-Adressen machen zu müssen, und es verhindert auch, dass doppelte IP-Adressen eingerichtet werden. Jedes physische Netzwerk sollte seinen eigenen DHCP-Server haben, damit ein Host eine IP-Adresse anfordern kann. In einer normalen Heimumgebung fungiert der Router normalerweise als DHCP-Server.

Die Art und Weise, wie DHCP alle Ihre dynamischen Host-Informationen erhält, ist:

1. DHCP DISCOVER - Diese Nachricht wird gesendet, um nach einem DHCP-Server zu suchen.
2. DHCP OFFER - Der DHCP-Server im Netzwerk antwortet mit einer Angebotsnachricht. Das Angebot enthält ein Paket mit DHCP-Lease-Zeit, Subnetzmaske, IP-Adresse usw.
3. DHCP REQUEST - Der Client sendet eine weitere Broadcast-Nachricht, um alle DHCP-Server wissen zu lassen, welches Angebot er angenommen hat.
4. DHCP ACK - Die Bestätigung wird vom Server gesendet.

DHCP ist komplexer als das, aber das ist das Wesentliche.

## Exercise

No exercises for this lesson.

## Quiz Question

Was sind die Schritte einer DHCP-Anfrage?

## Quiz Answer

DISCOVER, OFFER, REQUEST, ACK
