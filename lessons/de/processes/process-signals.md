---
lesson_id: "process-signals"
course_id: "processes"
lang: "de"
order_index: 6
title: "Signale"
description: "Erfahre, wie Linux Signale zur Prozesssteuerung und Ereignisbenachrichtigung erzeugt, blockiert, zustellt und behandelt."
meta_title: "Signale – Prozesse"
meta_description: "Erkunde die Grundlagen von Linux-Signalen, einem wichtigen Mechanismus zur Prozessverwaltung. Erfahre, wie Linux-Prozesssignale wie SIGTERM (Signal 15 unter Linux) und SIGKILL funktionieren, und verstehe ihre Betriebssystem-Signalcodes."
meta_keywords: "Linux-Signale, Linux-Prozesssignale, Signal 15 Linux, Betriebssystem-Signalcode, SIGKILL, SIGTERM, SIGINT, Prozessverwaltung, Linux-Tutorial"
---

Ein Signal ist eine asynchrone Benachrichtigung, die einem Prozess oder einem bestimmten Thread zugestellt wird. Signale melden Ereignisse und fordern Aktionen an, übertragen aber im Vergleich zu datenorientierten Mechanismen der Interprozesskommunikation nur begrenzte Informationen.

## Woher Signale stammen

Signale können aus mehreren Quellen stammen:

- Ein Terminal kann bei `Ctrl-C` `SIGINT` oder bei `Ctrl-Z` `SIGTSTP` erzeugen und an die Vordergrundprozessgruppe richten.
- Der Kernel kann ein synchrones Signal wie `SIGSEGV` erzeugen, wenn ein Thread auf eine ungültige Speicheradresse zugreift.
- Ein Prozess kann ein autorisiertes Signal an einen anderen Prozess oder eine Prozessgruppe senden.
- Zeitgeber, Änderungen des Kindprozesszustands und Terminal-Hangups können weitere Signale erzeugen.

Der Sender muss über die entsprechende Berechtigung verfügen, die gewöhnlich auf Zugangsdaten oder Capabilities beruht. Signale sind daher eine vom Kernel vermittelte Steuerungsschnittstelle und keine uneingeschränkten Nachrichten zwischen beliebigen Benutzern.

:::single-choice{#process-signals-ctrl-c}
Welches Signal erzeugt ein Terminal gewöhnlich bei `Ctrl-C`?

::option[`SIGTSTP`]{#process-signals-ctrl-c-tstp explanation="`SIGTSTP` ist gewöhnlich mit dem Terminalzeichen zum Anhalten wie `Ctrl-Z` verbunden."}
::option[`SIGCONT`]{#process-signals-ctrl-c-cont explanation="`SIGCONT` setzt einen angehaltenen Prozess fort und steht nicht für eine Unterbrechung über die Tastatur."}
::option[`SIGINT`]{#process-signals-ctrl-c-int .correct explanation="Das Unterbrechungszeichen des Terminals erzeugt gewöhnlich `SIGINT` für die Vordergrundprozessgruppe."}
:::

## Behandlungen und Standardaktionen

Die meisten Signale besitzen eine prozessweite Behandlung, die eine von drei Reaktionen auswählt:

- die festgelegte Standardaktion des Signals ausführen
- das Signal ignorieren
- einen vom Benutzer eingerichteten Handler aufrufen

Die Standardaktionen unterscheiden sich: Ein Signal kann beenden, beenden und einen Core-Dump erzeugen, anhalten, fortsetzen oder ignoriert werden. Das Abfangen von `SIGTERM` kann einem Programm ermöglichen, ein geordnetes Herunterfahren einzuleiten. Ein Handler muss jedoch strenge Regeln zur Async-Signal-Sicherheit einhalten, und das Programm kann seine Beendigung weiterhin verzögern oder ablehnen.

Signalnamen sind portabler und lesbarer als Nummern. Obwohl verbreitete Linux-Architekturen `SIGTERM` als 15 verwenden, solltest du nicht annehmen, dass alle Signalenummern außer den vom jeweiligen Standard garantierten überall identisch sind. Verwende `kill -l`, um die lokale Zuordnung zu prüfen.

:::single-choice{#process-signals-term-behavior}
Warum kann ein Prozess geordnet auf `SIGTERM` reagieren?

::option[Er kann für dieses Signal einen Handler einrichten.]{#process-signals-term-handler .correct explanation="Anders als `SIGKILL` kann `SIGTERM` abgefangen werden, sodass ein Programm seine eigene Logik zum Herunterfahren einleiten kann."}
::option[Der Kernel speichert automatisch jedes geöffnete Dokument.]{#process-signals-term-kernel-save explanation="Die Bereinigung durch eine Anwendung hängt von ihrem Programmcode ab; der Kernel versteht und speichert keinen beliebigen Dokumentzustand."}
::option[`SIGTERM` kann standardmäßig keine Beendigung verursachen.]{#process-signals-term-no-default explanation="Seine Standardaktion ist die Beendigung, sofern der Prozess die Behandlung nicht geändert hat."}
:::

## Blockierte und ausstehende Signale

Threads besitzen Signalmasken, die die Zustellung ausgewählter Signale vorübergehend blockieren können. Ein erzeugtes blockiertes Signal bleibt ausstehend, bis es zugestellt werden kann, vorbehaltlich der Regeln für Standard- und Echtzeitsignale. Mehrere Standardsignale desselben Typs können zusammengefasst werden, statt jedes Auftreten einzeln in eine Warteschlange zu stellen.

In einem Prozess mit mehreren Threads kann ein an den Prozess gerichtetes Signal einem geeigneten Thread zugestellt werden, der es nicht blockiert; ein an einen Thread gerichtetes Signal zielt auf den angegebenen Thread. Eine korrekte Signalgestaltung erfordert daher mehr als die Prüfung, ob „der Prozess es blockiert“.

:::single-choice{#process-signals-blocked-state}
Was geschieht gewöhnlich, wenn ein blockierbares Signal erzeugt wird, während sein Ziel es blockiert?

::option[Es bleibt ausstehend, bis eine Zustellung möglich wird.]{#process-signals-pending .correct explanation="Die Blockierung verschiebt die Behandlung; das ausstehende Signal kann nach seiner Freigabe zugestellt werden."}
::option[Es wird automatisch in `SIGKILL` umgewandelt.]{#process-signals-convert-kill explanation="Der Kernel eskaliert ein gewöhnliches blockiertes Signal nicht zu einem nicht abfangbaren Signal."}
::option[Es ändert die Benutzer-ID des Zielprozesses.]{#process-signals-change-uid explanation="Signalmasken beeinflussen die Zustellung und ändern keine Prozesszugangsdaten."}
:::

## Signale, die nicht behandelt werden können

`SIGKILL` beendet einen Prozess und `SIGSTOP` hält ihn an. Keines der beiden Signale kann abgefangen, ignoriert oder blockiert werden. Dadurch behält der Kernel die letztliche Kontrolle. Zugleich bedeutet dies, dass `SIGKILL` keine Gelegenheit zur Bereinigung auf Anwendungsebene bietet.

Selbst `SIGKILL` lässt eine Aufgabe aus Sicht eines Beobachters möglicherweise nicht sofort verschwinden. Eine Aufgabe kann in einem nicht unterbrechbaren Kernelvorgang warten, und nach der Beendigung muss ihr Elternprozess den Status weiterhin aufräumen.

:::single-choice{#process-signals-uncatchable-pair}
Welches Paar kann weder abgefangen noch ignoriert oder blockiert werden?

::option[`SIGKILL` und `SIGSTOP`]{#process-signals-kill-stop .correct explanation="Der Kernel behält diese beiden Signale vor, damit ein Prozess ihre grundlegenden Aktionen weder überschreiben noch aufschieben kann."}
::option[`SIGINT` und `SIGTERM`]{#process-signals-int-term explanation="Für beide können benutzerdefinierte Handler eingerichtet werden, und beide lassen sich blockieren."}
::option[`SIGHUP` und `SIGCONT`]{#process-signals-hup-cont explanation="Diese Signale besitzen besondere Semantik, sind aber nicht das nicht abfangbare Paar."}
:::

## Zusammenfassung

Du kannst nun die wichtigsten Phasen und Einschränkungen der Linux-Signalbehandlung erklären.

1. Bestimme vom Terminal, Kernel und von Prozessen erzeugte Signale.
2. Unterscheide Standardaktionen, ignorierte Signale und Handler.
3. Setze Blockierung mit ausstehender Zustellung und Threadmasken in Beziehung.
4. Denke daran, dass `SIGKILL` und `SIGSTOP` weder behandelt noch blockiert werden können.
