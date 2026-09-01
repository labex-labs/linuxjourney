---
lesson_id: "routing-protocols"
course_id: "routing"
lang: "de"
order_index: 4
title: "Routingprotokolle"
description: "Lerne, wie dynamische Routingprotokolle Erreichbarkeit austauschen und zu verwendbaren Weiterleitungspfaden konvergieren."
meta_title: "Routingprotokolle – Routing"
meta_description: "Erkunde die Grundlagen von Routingprotokollen in Linux-Netzwerken. Diese Anleitung behandelt Distanzvektor- und Link-State-Protokolle, Netzwerkkonvergenz und Routingtabellen."
meta_keywords: "Routingprotokolle, Netzwerkkonvergenz, Distanzvektor, Link State, Linux-Vernetzung, Routingtabelle, Netzwerk-Tutorial, Einsteiger-Anleitung, Routerkommunikation"
---

Statische Routen werden unmittelbar konfiguriert, während dynamische Routingprotokolle Erreichbarkeits- und Topologieinformationen austauschen, damit Router sich anpassen können. Dynamisches Lernen verringert manuelle Arbeit, führt jedoch Protokollzustand, Vertrauensgrenzen, Timer und Fehlermöglichkeiten ein, die überwacht werden müssen.

## Steuerungs- und Weiterleitungsebene

Ein Routingprotokoll lernt Kandidaten in seiner eigenen Datenbank. Der Router wählt Routen in eine Routinginformationsbasis aus und installiert verwendbare nächste Hops in einer Weiterleitungstabelle. Hardware oder Kernel leiten Pakete anschließend anhand dieser Tabelle weiter.

Eine hergestellte Protokollnachbarschaft beweist nicht, dass das gewünschte Präfix gelernt, ausgewählt, installiert oder von der Weiterleitungsrichtlinie erlaubt wurde.

:::single-choice{#routing-protocols-adjacency-limit} Was beweist eine hergestellte Routingnachbarschaft nicht?

::option[Dass jede gewünschte Route installiert ist und erfolgreich weiterleitet.]{#routing-protocols-not-full-proof .correct explanation="Routenankündigung, Auswahl, Installation, Filterung und Datenebenenbetrieb sind getrennte Stufen."}
::option[Dass zwei Protokollteilnehmer überhaupt Steuernachrichten ausgetauscht haben.]{#routing-protocols-no-messages explanation="Die Herstellung einer Nachbarschaft erfordert normalerweise Protokollkommunikation."}
::option[Dass eine Steuerungsebene existiert.]{#routing-protocols-no-control explanation="Die Nachbarschaft ist selbst Zustand der Steuerungsebene."}
:::

## Internes und externes Routing

Interior Gateway Protocols arbeiten innerhalb einer administrativen Routingdomäne. Beispiele sind RIP, OSPF und IS-IS. BGP tauscht richtliniengesteuerte Erreichbarkeit innerhalb und zwischen autonomen Systemen aus und ist das externe Routingprotokoll des Internets.

Messwerte besitzen protokollspezifische Bedeutung. OSPF-Kosten, RIP-Hop-Anzahl und BGP-Attribute können nicht verglichen werden, als hätten sie eine allgemeingültige numerische Skala. Implementierungen verwenden Routenpräferenz oder administrative Distanz, um vor oder neben der protokollspezifischen Auswahl zwischen Quellen zu wählen.

:::single-choice{#routing-protocols-metric-comparison} Kann eine RIP-Hop-Anzahl unmittelbar mit OSPF-Kosten verglichen werden?

::option[Ja, weil alle Routingmesswerte dieselben Einheiten verwenden.]{#routing-protocols-universal-metric explanation="Jedes Protokoll definiert seinen eigenen Messwert und Auswahlprozess."}
::option[Ja, aber nur, wenn beide Werte null sind.]{#routing-protocols-zero-metric explanation="Ihre Semantik bleibt unabhängig von einer angezeigten Zahl unterschiedlich."}
::option[Nein; sie besitzen protokollspezifische Bedeutungen.]{#routing-protocols-specific-metric .correct explanation="Die Auswahl zwischen Quellen verwendet Implementierungsrichtlinien, statt ungleiche Messwerte als eine Skala zu behandeln."}
:::

## Distanzvektor und Link State

Distanzvektorprotokolle kündigen Erreichbarkeit und Entfernung über Nachbarn an und leiten Pfade aus Nachbarberichten ab. Link-State-Protokolle bilden Nachbarschaften, fluten Verbindungszustandsinformationen in einem Bereich, erstellen eine Topologiedatenbank und berechnen Kürzeste-Wege-Bäume. Moderne Protokolle enthalten Verfeinerungen, durch die einfache Kategorienzusammenfassungen unvollständig bleiben.

:::single-choice{#routing-protocols-link-state-input} Was verwendet ein Link-State-Router für seine Pfadberechnung?

::option[Nur den Hostnamen seines Standardgateways.]{#routing-protocols-hostname-only explanation="Eine Topologieberechnung erfordert Verbindungs- und Präfixinformationen."}
::option[Eine synchronisierte Datenbank, die Verbindungen im Routingbereich beschreibt.]{#routing-protocols-link-database .correct explanation="Der Router führt einen Kürzeste-Wege-Algorithmus auf der gelernten Topologie aus."}
::option[Anwendungspasswörter jedes Hosts.]{#routing-protocols-passwords explanation="Der Austausch der Routingtopologie erfordert keine Anmeldedaten von Endbenutzern."}
:::

## Konvergenz

Nach einer Topologie- oder Richtlinienänderung erkennen Router sie, verbreiten Steuerinformationen, berechnen Pfade und aktualisieren den Weiterleitungszustand. Konvergenz ist Zeitraum und Ergebnis, in dem das Netzwerk für die betroffenen Ziele stabiles, gegenseitig verwendbares Routing erreicht. Sie erfordert nicht, dass jeder Router eine identische vollständige Tabelle besitzt; Rollen und Richtlinien können sich bewusst unterscheiden.

Während der Konvergenz können vorübergehender Verlust, Schleifen oder Blackholes auftreten. Miss Erkennung, Verbreitung, Berechnung und Installation getrennt und überprüfe sie mit Datenebenenprüfungen.

:::single-choice{#routing-protocols-convergence} Was ist Routingkonvergenz?

::option[Der Prozess, nach einer Änderung stabiles verwendbares Routing zu erreichen.]{#routing-protocols-stable-routing .correct explanation="Sie umfasst die Verbreitung auf der Steuerungsebene und die daraus folgenden Weiterleitungsaktualisierungen."}
::option[Die Anforderung, dass jeder Router eine identische globale Tabelle speichert.]{#routing-protocols-identical-table explanation="Richtlinie, Bereich und Rolle können bewusste Unterschiede erzeugen."}
::option[Die dauerhafte Verhinderung jedes möglichen Routingfehlers.]{#routing-protocols-no-failure explanation="Ein konvergiertes Netzwerk kann weiterhin Richtlinien- oder Kapazitätsprobleme besitzen."}
:::

## Zusammenfassung

Du kannst dynamische Routinginformationen nun auf dem Weg vom Protokollaustausch zur Weiterleitung einordnen.

1. Trenne gelernte Kandidaten, ausgewählte Routen und Weiterleitungseinträge.
2. Unterscheide internes Routing vom BGP-Richtlinienaustausch.
3. Vergleiche Messwerte nur innerhalb ihrer Protokollsemantik.
4. Überprüfe Konvergenz auf Steuerungs- und Datenebene.
