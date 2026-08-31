---
lesson_id: "link-state-protocols"
course_id: "routing"
lang: "de"
order_index: 6
title: "Link-State-Protokolle"
description: "Lerne, wie Link-State-Protokolle Nachbarschaften bilden, Topologieinformationen fluten und Pfade berechnen."
meta_title: "Link-State-Protokolle – Routing"
meta_description: "Lerne Link-State-Protokolle wie OSPF für große Netzwerke kennen. Verstehe ihre Konvergenz und die Aktualisierung von Routingtabellen."
meta_keywords: "Link-State-Protokolle, OSPF, Linux-Vernetzung, Routingprotokolle, Netzwerktopologie, Einsteiger"
---

Link-State-Protokolle beschreiben lokale Verbindungen und Präfixe, verteilen diese Beschreibungen in einem Routingbereich und lassen jeden Router anhand einer Topologiedatenbank Pfade berechnen. OSPF und IS-IS sind verbreitete Beispiele.

## Nachbarschaften bilden

Router erkennen kompatible Nachbarn und bilden gemäß Schnittstellentyp, Bereich, Timern, Authentifizierung und weiteren Parametern Protokollnachbarschaften. Sichtbare Hello-Pakete garantieren keine vollständige Nachbarschaft; nicht übereinstimmende Konfiguration kann die Zustandsmaschine früher anhalten.

:::single-choice{#link-state-hello-limit}
Was beweist der Empfang eines OSPF-Hellos nicht?

::option[Dass die Router eine vollständige synchronisierte Nachbarschaft gebildet haben.]{#link-state-not-full .correct explanation="Bereich, Timer, Authentifizierung, MTU und weiterer Zustand können den vollständigen Datenbankaustausch verhindern."}
::option[Dass der Nachbar mindestens eine Protokollnachricht gesendet hat.]{#link-state-hello-sent explanation="Der Empfang des Hellos beweist unmittelbar diese begrenzte Tatsache."}
::option[Dass eine Schnittstelle einen Frame empfangen kann.]{#link-state-frame-received explanation="Das empfangene Paket belegt, dass ein Teil des lokalen Empfangspfads funktioniert hat."}
:::

## Link-State-Informationen fluten

Jeder Router erzeugt Ankündigungen zu seinem relevanten Zustand. Nachbarn fluten neuere Informationen zuverlässig durch den festgelegten Bereich oder die Domäne, statt Aktualisierungen nur zwischen dem ursprünglichen Nachbarpaar zu behalten. Sequenz- und Alterungsmechanismen unterscheiden aktuelle Informationen und entfernen veralteten Zustand.

:::single-choice{#link-state-flooding-scope}
Warum werden Link-State-Informationen über einen Nachbarn hinaus geflutet?

::option[Jede Anwendung benötigt eine Kopie aller Routerpasswörter.]{#link-state-password-copy explanation="Anmeldedaten von Anwendungen sind keine Topologieankündigungen."}
::option[Ethernet kann keine Unicast-Frames senden.]{#link-state-no-unicast explanation="Ethernet unterstützt Unicast; das Fluten ist hier ein Verteilungsmechanismus des Routingprotokolls."}
::option[Router im Routingbereich benötigen eine konsistente Topologiedatenbank.]{#link-state-consistent-database .correct explanation="Jeder Router berechnet Pfade anhand derselben Menge aktueller Link-State-Ankündigungen."}
:::

## Kürzeste Pfade berechnen

Nach dem Aufbau einer Link-State-Datenbank führt ein Router einen Kürzeste-Wege-Algorithmus, gewöhnlich Dijkstras Algorithmus, mit sich selbst als Wurzel aus. OSPF summiert Schnittstellenkosten; Richtlinien und Regeln für gleiche Kosten beeinflussen, welche Ergebnisse installiert werden.

„Kürzeste“ bedeutet die niedrigsten Protokollkosten und nicht unbedingt die wenigsten Router oder die geringste gemessene Anwendungslatenz. Der Kostenentwurf muss die betriebliche Absicht widerspiegeln.

:::single-choice{#link-state-shortest-meaning}
Was bedeutet „kürzeste“ bei einer Link-State-Pfadberechnung?

::option[Die Route, deren Präfix die wenigsten geschriebenen Zeichen besitzt.]{#link-state-shortest-text explanation="Textlänge hat nichts mit Topologiekosten zu tun."}
::option[Der Pfad mit der kleinsten Summe von Protokollkosten.]{#link-state-lowest-cost .correct explanation="Das Kostenmodell entspricht möglicherweise weder unmittelbar der Hop-Anzahl noch der aktuellen Latenz."}
::option[Der Pfad, der immer null Paketverlust besitzt.]{#link-state-zero-loss explanation="Eine berechnete Route garantiert keine Anwendungsleistung."}
:::

## Bereiche und Konvergenz

OSPF-Bereiche begrenzen Topologieflutung und Berechnungsbereich; Area 0 dient im normalen bereichsübergreifenden Entwurf als Backbone. Zusammenfassung und Bereichstypen können unterschiedlichen Routern bewusst unterschiedlich detaillierte Datenbanken geben.

Nach einer Verbindungsänderung benötigen Erkennung, Fluten der Ankündigung, SPF-Berechnung, Routeninstallation und Wiederherstellung der Weiterleitung jeweils Zeit. Eine schnellere Konvergenz als bei einem einfachen Distanzvektorentwurf ist möglich, aber nicht bei jedem Fehler oder jeder Konfiguration automatisch gegeben.

:::single-choice{#link-state-convergence-stages}
Was sollte bei einer OSPF-Konvergenzuntersuchung gemessen werden?

::option[Nur der Zeitpunkt, zu dem ein Administrator ein Terminal geöffnet hat.]{#link-state-terminal-time explanation="Dies grenzt weder Protokoll- noch Weiterleitungsstufen ein."}
::option[Nur die alphabetische Reihenfolge der Routernamen.]{#link-state-router-names explanation="Namen bestimmen keine Konvergenzzeiten."}
::option[Erkennung, Fluten, Berechnung, Installation und Wiederherstellung der Weiterleitung.]{#link-state-all-stages .correct explanation="Die Trennung der Stufen zeigt, wo eine Konvergenzverzögerung oder ein Fehler auftritt."}
:::

## Zusammenfassung

Du kannst Link-State-Routing nun von der Nachbarerkennung bis zu installierten Pfaden verfolgen.

1. Unterscheide den Empfang eines Hellos von einer vollständigen Nachbarschaft.
2. Erkläre das zuverlässige Fluten durch einen Routingbereich.
3. Interpretiere den kürzesten Pfad als niedrigste konfigurierte Protokollkosten.
4. Miss jede Konvergenzstufe auf Steuerungs- und Datenebene.
