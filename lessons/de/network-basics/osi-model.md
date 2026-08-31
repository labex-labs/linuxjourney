---
lesson_id: "osi-model"
course_id: "network-basics"
lang: "de"
order_index: 2
title: "OSI-Modell"
description: "Lerne, wie das siebenschichtige OSI-Referenzmodell Netzwerkfunktionen und die Sprache der Fehlersuche ordnet."
meta_title: "OSI-Modell – Netzwerkgrundlagen"
meta_description: "Erkunde das OSI-Modell als grundlegendes siebenschichtiges Netzwerkmodell. Lerne, wie dieses theoretische Konzept das TCP/IP-Modell beeinflusst und bei der Linux-Vernetzung hilft."
meta_keywords: "OSI Linux, OSI-Modell, Netzwerkkonzepte, TCP/IP, Linux-Vernetzung, Netzwerkschichten, theoretisches Modell, Siebenschichtenmodell"
---

Das Open-Systems-Interconnection-Modell ist ein siebenschichtiges Referenzmodell. Es bietet Fachleuten ein gemeinsames Vokabular, um Verantwortlichkeiten, Schnittstellen und Fehler einzuordnen; es ist keine wörtliche Beschreibung jeder Implementierung.

## Die sieben Schichten

Von der niedrigsten bis zur höchsten sind die OSI-Schichten:

1. Bitübertragung: Signale, Medien, Anschlüsse und Übertragung von Bits.
2. Sicherung: lokale Frames, Verbindungsadressierung und Medienzugriff.
3. Vermittlung: logische Adressierung und Weiterleitung zwischen Netzwerken.
4. Transport: Kommunikation zwischen Endpunkten oder Prozessen.
5. Sitzung: Verwaltung von Kommunikationssitzungen.
6. Darstellung: Darstellung, Umwandlung und Codierung von Daten.
7. Anwendung: von Anwendungen verwendete Netzwerkdienste.

:::single-choice{#osi-network-layer-number}
Welche OSI-Schicht verarbeitet logische Adressierung und Weiterleitung zwischen Netzwerken?

::option[Schicht 3, Vermittlung.]{#osi-layer-three .correct explanation="Die Vermittlungsschicht beschreibt logische Adressierung und die Weiterleitung zwischen Netzwerken."}
::option[Schicht 1, Bitübertragung.]{#osi-layer-one explanation="Die Bitübertragungsschicht betrifft Signale und Medien."}
::option[Schicht 7, Anwendung.]{#osi-layer-seven explanation="Die Anwendungsschicht beschreibt Dienste, die Netzwerkanwendungen bereitgestellt werden."}
:::

## Das Modell als Vokabular verwenden

Aussagen wie „eine Schleife auf Schicht 2“ oder „ein Port auf Schicht 4“ bezeichnen einen Funktionsbereich, ohne jedes Implementierungsdetail zu erklären. Ein tatsächliches Protokoll kann Grenzen überschreiten, und Verschlüsselung, Tunnel, Proxys oder Overlays können mehrere verschachtelte Schichten erzeugen.

:::single-choice{#osi-model-purpose}
Wofür ist das OSI-Modell bei der alltäglichen Fehlersuche am nützlichsten?

::option[Um zu garantieren, dass jedes Protokoll genau sieben Header besitzt.]{#osi-seven-headers explanation="Implementierungen lassen sich nicht eins zu eins auf sieben Header auf der Leitung abbilden."}
::option[Um alle Paketaufzeichnungen durch ein Diagramm zu ersetzen.]{#osi-replace-captures explanation="Das Modell leitet die Untersuchung, ersetzt aber keine Belege."}
::option[Um Netzwerkfunktionen auf gemeinsame Weise einzuordnen.]{#osi-shared-vocabulary .correct explanation="Das Modell hilft Teams, den besprochenen Funktionsbereich einzugrenzen."}
:::

## OSI und TCP/IP vergleichen

Die Internetprotokollfamilie und das OSI-Referenzmodell entstanden in unterschiedlichen Standardisierungsgeschichten. Das praktische TCP/IP-Modell fasst die OSI-Aufgaben von Sitzung und Darstellung häufig in seiner Anwendungsschicht zusammen und verbindet Belange von Bitübertragungs- und Sicherungsschicht in einer Verbindungs- oder Netzzugangsschicht. Zuordnungen sind Näherungen und kein Beweis, dass ein Stack unmittelbar aus dem anderen implementiert wurde.

:::single-choice{#osi-tcpip-mapping}
Wie sollte eine Zuordnung von OSI- zu TCP/IP-Schichten interpretiert werden?

::option[Als genaue Regel, die jedes Protokoll einhalten muss.]{#osi-exact-rule explanation="Protokollaufgaben überschreiten häufig konzeptionelle Grenzen."}
::option[Als Beleg, dass TCP/IP sieben vorgeschriebene Schichten auf der Leitung verwendet.]{#osi-tcp-seven explanation="TCP/IP wird gewöhnlich mit vier oder fünf Schichten beschrieben."}
::option[Als ungefährer Vergleich zwischen funktionalen Modellen.]{#osi-approximate-map .correct explanation="Die Modelle gruppieren manche Aufgaben unterschiedlich."}
:::

## Fehler über Schichten hinweg untersuchen

Beginne beim Symptom und prüfe Annahmen, statt die Schichten mechanisch in numerischer Reihenfolge abzuarbeiten. Ein Webfehler kann lokalen Verbindungszustand, IP-Routing, Transporterreichbarkeit, TLS, Namensauflösung, Authentifizierung oder Anwendungsverhalten betreffen. Belege auf einer Schicht können den nächsten Test leiten, ohne zu beweisen, dass höhere Schichten funktionieren.

:::single-choice{#osi-link-success-limit}
Was beweist eine funktionierende lokale Ethernet-Verbindung?

::option[Dass jeder entfernte HTTP-Dienst fehlerfrei ist.]{#osi-link-proves-http explanation="Der lokale Verbindungszustand kann den Zustand einer entfernten Anwendung nicht belegen."}
::option[Dass DNS keine falschen Datensätze enthält.]{#osi-link-proves-dns explanation="Namensdaten sind unabhängig von grundlegender Verbindungskonnektivität."}
::option[Nur, dass die betreffenden lokalen Verbindungsbedingungen funktionieren.]{#osi-link-limited-proof .correct explanation="Fehler bei Routing, Transport, Namensauflösung, Sicherheit und Anwendung können weiterhin bestehen."}
:::

## Zusammenfassung

Du kannst das OSI-Modell nun als geschichtetes Diagnosevokabular verwenden.

1. Benenne die sieben Schichten in ihrer Reihenfolge.
2. Ordne jeder Schicht ihre grobe Aufgabe zu.
3. Behandle Zuordnungen zu TCP/IP als Näherungen.
4. Verwende Schichtbelege als Leitfaden und nicht als Ersatz für Ende-zu-Ende-Tests.
