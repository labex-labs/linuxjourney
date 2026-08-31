---
lesson_id: "tcp-ip-model"
course_id: "network-basics"
lang: "de"
order_index: 3
title: "TCP/IP-Modell"
description: "Lerne, wie Anwendungs-, Transport-, Internet- und Verbindungsschicht im TCP/IP-Modell zusammenarbeiten."
meta_title: "TCP/IP-Modell – Netzwerkgrundlagen"
meta_description: "Erkunde die grundlegenden Schichten des TCP/IP-Modells als Basis moderner Vernetzung. Lerne Anwendungs-, Transport-, Internet- und Verbindungsschicht kennen."
meta_keywords: "TCP/IP-Modell, Schichten im TCP/IP-Modell, Vernetzung mit TCP/IP, TCP-Protokollschichten, Netzwerkschichten, TCP, IP, Linux-Vernetzung"
---

Das TCP/IP-Modell ordnet die von Internet-Hosts verwendeten Protokolle in funktionale Schichten. Eine verbreitete vierschichtige Form verwendet Anwendung, Transport, Internet und Verbindung. Manche Lehrmodelle trennen das physische Medium von der Verbindungsschicht und zeigen deshalb fünf Schichten.

## Anwendungsschicht

Anwendungsprotokolle definieren Nachrichten und Verhalten für Dienste wie HTTP, DNS, SSH und SMTP. Diese Schicht umfasst außerdem viele Darstellungs- und Sitzungsaufgaben, die das OSI-Modell getrennt behandelt.

:::single-choice{#tcpip-http-layer}
Welcher TCP/IP-Schicht wird HTTP normalerweise zugeordnet?

::option[Internet.]{#tcpip-http-internet explanation="Die Internetschicht verarbeitet IP-Adressierung und Paketweiterleitung."}
::option[Verbindung.]{#tcpip-http-link explanation="Die Verbindungsschicht transportiert Datenverkehr auf einem lokalen Medium."}
::option[Anwendung.]{#tcpip-http-application .correct explanation="HTTP definiert die Semantik von Anwendungsanfragen und -antworten."}
:::

## Transportschicht

Transportprotokolle ermöglichen die Kommunikation zwischen Anwendungsendpunkten. TCP bietet einen zuverlässigen geordneten Bytestrom mit Überlastungs- und Flusskontrolle. UDP stellt unabhängige Datagramme ohne TCPs Garantien für Verbindung, Reihenfolge oder erneute Übertragung bereit. Portnummern helfen, Transportendpunkte zu identifizieren, doch eine Portnummer allein beweist nicht, welche Anwendung lauscht.

:::single-choice{#tcpip-udp-property}
Welche Eigenschaft gehört zu UDP und nicht zu TCP?

::option[Unabhängige Datagramme ohne eingebaute Garantie erneuter Übertragung.]{#tcpip-udp-datagrams .correct explanation="UDP-Anwendungen entscheiden, ob und wie sie Zuverlässigkeit ergänzen."}
::option[Garantierte geordnete Zustellung eines einzelnen Bytestroms.]{#tcpip-udp-ordered explanation="Dies ist eine Diensteigenschaft von TCP, sofern eine Verbindung zustande kommt."}
::option[Pakete zwischen unterschiedlichen IP-Netzwerken weiterleiten.]{#tcpip-udp-routing explanation="Die Weiterleitung zwischen Netzwerken ist eine Funktion der Internetschicht."}
:::

## Internetschicht

Das Internet Protocol transportiert Pakete anhand von Quell- und Ziel-IP-Adressen. Router untersuchen Routinginformationen und verringern Hop-Limits, während sie Pakete zum Ziel weiterleiten. ICMP übermittelt Steuerungs- und Fehlerinformationen für den IP-Betrieb. Die Zustellung erfolgt nach bestem Bemühen; höhere Schichten oder Anwendungen übernehmen jede erforderliche Wiederherstellung.

:::single-choice{#tcpip-router-layer}
Welche Schicht stellt das von Routern verwendete IP-Ziel bereit?

::option[Internet.]{#tcpip-router-internet .correct explanation="Der IP-Header enthält das Netzwerkschichtziel für die geroutete Weiterleitung."}
::option[Anwendung.]{#tcpip-router-application explanation="Anwendungsnachrichten werden innerhalb der Protokolldaten niedrigerer Schichten transportiert."}
::option[Verbindung.]{#tcpip-router-link explanation="Verbindungsadressen wählen das Frameziel für den nächsten lokalen Hop aus."}
:::

## Verbindungsschicht und Kapselung

Die Verbindungsschicht sendet ein IP-Paket über eine lokale Verbindung mithilfe von Ethernet, WLAN, einem Punkt-zu-Punkt-Protokoll oder einer anderen Technik. Während sich Anwendungsdaten nach unten bewegen, ergänzt jede Schicht die für ihren Bereich erforderlichen Informationen. Beim Empfänger validieren und entfernen die Schichten ihre eigene Kapselung, bevor sie Daten nach oben weitergeben.

Verbindungsheader ändern sich gewöhnlich an jedem gerouteten Hop; Transport- und Anwendungsunterhaltungen laufen von Ende zu Ende, sofern keine Middlebox sie beendet oder umwandelt.

:::single-choice{#tcpip-link-scope}
Was ist der normale Geltungsbereich eines Frames der Verbindungsschicht?

::option[Eine lokale Verbindung oder ein Hop.]{#tcpip-one-link .correct explanation="Ein Router entfernt den eingehenden Frame und erstellt einen Frame für die nächste Verbindung."}
::option[Jede Anwendungssitzung im weltweiten Internet.]{#tcpip-global-frame explanation="Frames bleiben über geroutete Netzwerke hinweg nicht unverändert."}
::option[Nur der Speicher des Quellprozesses.]{#tcpip-process-memory explanation="Frames werden über eine Netzwerkverbindung übertragen."}
:::

## Zusammenfassung

Du kannst häufige Internetfunktionen nun im TCP/IP-Modell einordnen.

1. Ordne Dienstprotokolle der Anwendungsschicht zu.
2. Unterscheide TCP-Ströme von UDP-Datagrammen.
3. Ordne IP-Adressierung und Routing der Internetschicht zu.
4. Behandle Verbindungskapselung als Kapselung für einen lokalen Hop.
