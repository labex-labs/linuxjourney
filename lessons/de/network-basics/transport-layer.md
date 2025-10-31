---
index: 6
lang: "de"
title: "Transportschicht"
meta_title: "Transportschicht - Netzwerk-Grundlagen"
meta_description: "Erkunden Sie die Transportschicht im Linux-Netzwerk. Diese Lektion behandelt wichtige Protokolle wie TCP und UDP, die Funktion von Netzwerk-Ports, Datensegmentierung und den TCP-Handshake für eine zuverlässige Datenübertragung."
meta_keywords: "Linux Transportschicht, TCP, UDP, TCP-Handshake, Netzwerk-Ports, Datensegmentierung, Linux-Netzwerk, Netzwerkprotokolle, zuverlässige Datenübertragung"
---

## Lesson Content

Die Transportschicht ist ein fundamentaler Bestandteil des Linux-Netzwerkbetriebs, der für die Ende-zu-Ende-Kommunikation und die zuverlässige Datenübertragung zwischen Anwendungen auf verschiedenen Hosts verantwortlich ist. Sie bereitet Daten strukturiert und verwaltbar für den Transport über das Netzwerk vor.

### Datensegmentierung

Eine der Hauptfunktionen der Transportschicht ist die Datensegmentierung. Sie zerlegt große Datenmengen in kleinere, besser handhabbare Blöcke, sogenannte Segmente. Dieser Prozess macht die Datenübertragung effizienter und ausfallsicherer. Geht ein Segment während der Übertragung verloren oder wird es beschädigt, muss nur dieser kleine Teil erneut gesendet werden, nicht der gesamte Datensatz. Sobald die Segmente am Zielort eintreffen, setzt die Transportschicht sie in der richtigen Reihenfolge wieder zusammen.

### Verständnis von Netzwerk-Ports

Während IP-Adressen den richtigen Host in einem Netzwerk identifizieren, geben sie nicht an, welche Anwendung oder welcher Dienst die Daten empfangen soll. Hier kommen Netzwerk-Ports ins Spiel. Dienste wie HTTP (Web-Traffic) oder SMTP (E-Mail) lauschen auf spezifischen, bekannten Ports. HTTP verwendet beispielsweise typischerweise Port 80. Die Transportschicht fügt jedem Segment Quell- und Zielportnummern hinzu, um sicherzustellen, dass die Daten an den korrekten Prozess auf dem empfangenden Host zugestellt werden.

### Kernprotokolle der Transportschicht: TCP und UDP

In modernen Netzwerken werden zwei Hauptprotokolle der Transportschicht verwendet: TCP (Transmission Control Protocol) und UDP (User Datagram Protocol). Wir werden UDP kurz behandeln und uns dann auf TCP konzentrieren, da es für die zuverlässige Kommunikation am weitesten verbreitet ist.

### UDP (User Datagram Protocol)

UDP ist ein verbindungsloses Protokoll, das eine schnelle, aber unzuverlässige Methode zum Transport von Daten bietet. Es garantiert weder, dass alle Segmente ankommen, noch, dass sie in der richtigen Reihenfolge eintreffen. Obwohl dies ein Nachteil zu sein scheint, ist UDP sehr effektiv für Anwendungen, bei denen Geschwindigkeit wichtiger ist als perfekte Genauigkeit, wie z. B. Live-Video-Streaming oder Online-Spiele. Der Verlust einiger Videobilder ist oft ein akzeptabler Kompromiss für einen flüssigeren, schnelleren Stream.

### TCP (Transmission Control Protocol)

TCP bietet einen zuverlässigen, verbindungsorientierten Datenstrom. Bevor Daten ausgetauscht werden, baut TCP eine formelle Verbindung zwischen den beiden Hosts auf, um sicherzustellen, dass beide zur Kommunikation bereit sind.

### Der TCP-Handshake

Um eine Verbindung herzustellen, verwendet TCP einen Prozess, der als Drei-Wege-Handshake bezeichnet wird:

1. **SYN**: Der Client sendet ein SYN (Synchronize)-Segment an den Server, um eine Verbindung zu initiieren.
2. **SYN-ACK**: Der Server antwortet mit einem SYN-ACK (Synchronize-Acknowledge)-Segment, um die Anforderung des Clients zu bestätigen.
3. **ACK**: Der Client sendet ein ACK (Acknowledge)-Segment zurück an den Server, wodurch die Verbindung als hergestellt bestätigt wird.

Sobald der Handshake abgeschlossen ist, können Daten zuverlässig ausgetauscht werden. TCP verwendet Sequenznummern, um jedes Segment zu verfolgen, wodurch der empfangende Host sie in der richtigen Reihenfolge wieder zusammensetzen und die erneute Übertragung fehlender Segmente anfordern kann. In unserem E-Mail-Beispiel würde die Transportschicht die Ziel-Portnummer für SMTP (Port 25) und einen Quell-Port des Client-Hosts an jedes Segment anhängen.

## Exercise

Obwohl es für dieses Thema keine spezifischen Übungen gibt, empfehlen wir Ihnen, den umfassenden [Linux Lernpfad](https://labex.io/de/learn/linux) zu erkunden, um verwandte Linux-Fähigkeiten und -Konzepte zu üben.

## Quiz Question

What is a reliable transport protocol? (Your answer should be in English and is case-sensitive).

## Quiz Answer

TCP
