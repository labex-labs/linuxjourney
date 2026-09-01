---
lesson_id: "network-layer"
course_id: "network-basics"
lang: "de"
order_index: 7
title: "Netzwerkschicht"
description: "Lerne, wie IP-Adressierung, Präfixe, Routingtabellen und Hop-Limits Pakete zwischen Netzwerken transportieren."
meta_title: "Netzwerkschicht – Netzwerkgrundlagen"
meta_description: "Erkunde die Netzwerkschicht der Linux-Vernetzung. Diese Anleitung erklärt, wie IP-Adressen und Subnetze das Routing von Paketen zur Datenübertragung über Netzwerke ermöglichen."
meta_keywords: "Netzwerkschicht, IP-Adressen, Subnetze, Linux-Vernetzung, Paketrouting, Datenübertragung, OSI-Modell, IP-Paket"
---

Die Netzwerkschicht stellt logische Adressierung und Paketzustellung nach bestem Bemühen über verbundene Netzwerke hinweg bereit. In der Internetprotokollfamilie transportieren IPv4 und IPv6 Pakete, während Router den nächsten Hop zu jedem Ziel auswählen.

## IP-Pakete

Ein IP-Header enthält Quell- und Zieladressen sowie für Weiterleitung und Protokollverarbeitung erforderliche Felder. Die Nutzlast enthält gewöhnlich ein TCP-Segment, UDP-Datagramm oder eine ICMP-Nachricht. IP garantiert weder Ankunft noch Reihenfolge oder das Ausbleiben von Duplikaten.

:::single-choice{#network-layer-ip-service} Welchen Zustelldienst bietet IP für sich allein?

::option[Garantierte Bestätigungen von Anwendungstransaktionen.]{#network-layer-guaranteed-commit explanation="Ein IP-Zustellergebnis kann keine dauerhafte Speicherung durch eine Anwendung beweisen."}
::option[Paketzustellung nach bestem Bemühen.]{#network-layer-best-effort .correct explanation="Höhere Schichten oder Anwendungen ergänzen erforderliche Wiederherstellung oder Reihenfolge."}
::option[Dauerhafte Reservierung eines physischen Kabels.]{#network-layer-cable-reservation explanation="Paketweiterleitung reserviert keinen eigenen physischen Pfad."}
:::

## Präfixe und Subnetze

Eine Adresse und Präfixlänge legen fest, welche führenden Bits ein Netzwerkpräfix bilden. Hosts verwenden diese Informationen und ihre Routen, um zu entscheiden, ob ein Ziel direkt erreichbar ist oder einen Next-Hop-Router benötigt. Ein Subnetz ist ein Adressbereich unter einem Präfix und einer Richtlinie; Subnetze sind nicht automatisch mit jedem anderen Subnetz verbunden.

:::single-choice{#network-layer-prefix-decision} Was hilft einem Host zu entscheiden, ob ein IPv4-Ziel direkt erreichbar ist?

::option[Das Anwendungspasswort des Ziels.]{#network-layer-password explanation="Authentifizierungsdaten definieren keine Netzwerkpräfixe."}
::option[Die Farbe des Ethernet-Kabels.]{#network-layer-cable-color explanation="Das Aussehen eines Kabels besitzt keine Adressierungssemantik."}
::option[Seine konfigurierten Präfixe und die Routingtabelle.]{#network-layer-prefix-routes .correct explanation="Der Host vergleicht Ziele mit Routen einschließlich direkt verbundener Präfixe."}
:::

## Routingentscheidungen

Linux prüft Routingrichtlinien und -tabellen, um eine ausgehende Schnittstelle, einen nächsten Hop und bevorzugte Quellinformationen auszuwählen. Unter ansonsten geeigneten Routen wird normalerweise das spezifischste passende Präfix bevorzugt. Untersuche die tatsächliche Entscheidung für ein Ziel mit:

```bash
$ ip route get 203.0.113.10
```

Dies ist eine lokale Routensuche und kein Beweis, dass jeder nachgelagerte Router eine funktionierende Route besitzt oder das Ziel Datenverkehr annimmt.

:::single-choice{#network-layer-longest-prefix} Welche Route gewinnt normalerweise unter geeigneten Routen zum selben Ziel?

::option[Die Route, deren Schnittstellenname alphabetisch zuerst steht.]{#network-layer-alphabetical explanation="Die Schreibweise der Schnittstelle ist keine Auswahlregel."}
::option[Die älteste Route unabhängig von ihrem Präfix.]{#network-layer-oldest explanation="Das Alter allein setzt die Präfixübereinstimmung nicht außer Kraft."}
::option[Die Route mit dem spezifischsten passenden Präfix.]{#network-layer-most-specific .correct explanation="Die längste Präfixübereinstimmung wählt die Route aus, die den kleinsten passenden Adressbereich umfasst."}
:::

## Hop-Limits und Änderungen bei der Weiterleitung

Jedes IPv4-Paket besitzt eine TTL und jedes IPv6-Paket ein Hop Limit. Ein Router verringert den Wert; erreicht er null, verwirft der Router das Paket und kann einen ICMP-Fehler senden. Dies verhindert, dass Pakete endlos in Routingschleifen kreisen.

Router bewahren gewöhnlich die Ende-zu-Ende-IP-Adressen, doch NAT, Tunnel, Proxys und andere Middleboxes können Pakete umwandeln oder einkapseln. Header der Verbindungsschicht ändern sich unabhängig davon an jedem gerouteten Hop.

:::single-choice{#network-layer-hop-limit} Warum verringern Router TTL oder Hop Limit?

::option[Um die Dateiberechtigungen der Anwendung zu erhöhen.]{#network-layer-hop-permissions explanation="Die Hop-Anzahl hat nichts mit Dateisystemautorisierung zu tun."}
::option[Um jedes Paket von IPv4 in IPv6 umzuwandeln.]{#network-layer-hop-convert explanation="Protokollübersetzung ist nicht der Zweck dieses Felds."}
::option[Um zu verhindern, dass Pakete für immer kreisen.]{#network-layer-prevent-loop .correct explanation="Eine endliche Hop-Anzahl stellt sicher, dass eine dauerhafte Routingschleife das Paket schließlich verwirft."}
:::

## Zusammenfassung

Du kannst nun erklären, wie ein IP-Host den nächsten Schritt zu einem Ziel auswählt.

1. Behandle IP-Zustellung als bestmöglich.
2. Verwende Präfixe und Routen, um direkt erreichbare von gerouteten Zielen zu unterscheiden.
3. Wende die längste Präfixübereinstimmung auf die Routenauswahl an.
4. Erkenne, wie Hop-Limits Routingschleifen begrenzen.
