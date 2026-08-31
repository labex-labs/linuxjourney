---
lesson_id: "distance-vector-protocols"
course_id: "routing"
lang: "de"
order_index: 5
title: "Distanzvektorprotokolle"
description: "Lerne, wie Distanzvektorprotokolle Routen aus Nachbarankündigungen ableiten und Schleifen begrenzen."
meta_title: "Distanzvektorprotokolle – Routing"
meta_description: "Eine Einführung in Distanzvektorprotokolle beim Netzwerkrouting. Erfahre, wie Protokolle wie RIP Routen anhand der Hop-Anzahl bestimmen und welche Grenzen sie besitzen."
meta_keywords: "Distanzvektorprotokolle, Netzwerkrouting, RIP, Routing Information Protocol, Hop-Anzahl, Linux-Vernetzung, Einsteiger-Anleitung, Tutorial"
---

Distanzvektorrouting teilt Nachbarn mit, welche Ziele erreichbar sind, und beschreibt die Entfernung durch einen Messwert. Ein Router verbindet die Ankündigung eines Nachbarn mit den Kosten zu diesem Nachbarn, um seinen eigenen Pfadkandidaten abzuleiten.

## Über Nachbarn lernen

Wenn Router A eine Entfernung von drei zu einem Präfix ankündigt und Router B A mit Kosten von eins erreicht, kann B über A die Entfernung vier ableiten. Die Information beschreibt eine Richtung und einen Messwert und keine vollständige Topologiekarte. Deshalb wird der Ansatz mitunter als Routing nach Hörensagen bezeichnet.

:::single-choice{#distance-vector-derived-distance}
Welcher Messwert wird abgeleitet, wenn ein Nachbar den Wert 3 ankündigt und die Verbindungskosten 1 betragen?

::option[2]{#distance-vector-two explanation="Die Verbindungskosten werden addiert und nicht subtrahiert."}
::option[31]{#distance-vector-thirty-one explanation="Die Werte sind Messwerte und keine aneinanderzureihenden Dezimalziffern."}
::option[4]{#distance-vector-four .correct explanation="Nachbarentfernung und lokale Verbindungskosten ergeben gemeinsam den Pfadkandidaten."}
:::

## Schleifen und Count to Infinity

Nach einem Fehler können Nachbarn einander fälschlich eine Route zurückmelden und ihren Messwert schrittweise erhöhen. Protokolle begrenzen dies durch endliche Unendlichkeitswerte, Split Horizon, Route Poisoning, Poison Reverse, ausgelöste Aktualisierungen und Timer. Diese Mechanismen verringern Probleme, machen aber nicht jede Topologieänderung zu einer sofortigen Konvergenz.

:::single-choice{#distance-vector-split-horizon}
Was soll Split Horizon verringern?

::option[Die Anzahl der Bits in jeder IPv4-Adresse.]{#distance-vector-ip-bits explanation="Die Größe einer IPv4-Adresse ist unabhängig von Routingaktualisierungen festgelegt."}
::option[Verschlüsselungsaufwand in Anwendungsnutzlasten.]{#distance-vector-encryption explanation="Das Verfahren betrifft die Richtung von Routenankündigungen."}
::option[Eine gelernte Route zurück zu dem Nachbarn anzukündigen, von dem sie stammt.]{#distance-vector-no-return .correct explanation="Die Unterdrückung dieser Richtung hilft, einfache Rückkopplungsschleifen zu verhindern."}
:::

## RIP-Messwerte und -Grenzen

RIP verwendet die Hop-Anzahl. Eine Route mit Messwert 16 ist nicht erreichbar, sodass der größte verwendbare Messwert 15 ist. Dies begrenzt die Eskalation von Schleifen, aber auch den Netzwerkdurchmesser. Weniger Hops bedeuten nicht zwangsläufig geringere Latenz oder mehr Bandbreite.

RIPv2 verwendet regelmäßige und ausgelöste Aktualisierungen und unterstützt CIDR-Informationen. Es sendet Aktualisierungen gewöhnlich per Multicast, statt unter allen Umständen eine vollständige Tabelle als Broadcast zu senden. Authentifizierung und Filterung erfordern weiterhin bewusste Konfiguration.

:::single-choice{#distance-vector-rip-infinity}
Was stellt der RIP-Messwert 16 dar?

::option[Den schnellsten Pfad mit sechzehn parallelen Verbindungen.]{#distance-vector-fastest-16 explanation="RIP behandelt den Wert als nicht erreichbar."}
::option[Unendlich, also ein nicht erreichbares Ziel.]{#distance-vector-unreachable .correct explanation="RIP begrenzt verwendbare Pfade auf 15 Hops."}
::option[Eine von BGP gelernte Route.]{#distance-vector-bgp-route explanation="Die Zahl besitzt eine RIP-spezifische Bedeutung."}
:::

## Eine gelernte Route bewerten

Prüfe Nachbarzustand, empfangene und angekündigte Präfixe, Messwert, nächsten Hop, Routeninstallation und Erreichbarkeit auf der Datenebene. Eine Route kann innerhalb von RIP gültig sein, aber gemäß der lokalen Präferenzrichtlinie gegen eine andere Routenquelle verlieren.

:::single-choice{#distance-vector-fewest-hop-limit}
Warum kann die RIP-Route mit den wenigsten Hops schlecht funktionieren?

::option[Die Hop-Anzahl codiert weder Verbindungsbandbreite noch Latenz, Verlust oder Überlastung.]{#distance-vector-hop-limited .correct explanation="Ein Pfad mit mehr Hops kann bessere Verbindungen und Anwendungsleistung besitzen."}
::option[RIP wählt immer die Route mit den meisten Hops.]{#distance-vector-most-hops explanation="Sein Messwert bevorzugt kleinere verwendbare Hop-Anzahlen."}
::option[Die Hop-Anzahl wird in Byte Datenträgerspeicher gemessen.]{#distance-vector-disk-bytes explanation="Sie zählt geroutete Übergänge und keinen Speicher."}
:::

## Zusammenfassung

Du kannst nun sowohl die Einfachheit als auch die Grenzen von Distanzvektorrouting erklären.

1. Leite die Pfaddistanz aus der Ankündigung eines Nachbarn ab.
2. Erkenne Schleifen- und Count-to-Infinity-Verhalten.
3. Erkläre RIPs verwendbare 15-Hop-Grenze und Messwert 16.
4. Überprüfe Routeninstallation und Ergebnis der Datenebene getrennt.
