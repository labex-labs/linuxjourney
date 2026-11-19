---
lesson_id: "incident-timelines"
course_id: "incident-response"
lang: "de"
order_index: 3
title: "Zeitleisten für Vorfälle"
description: "Lerne, Belege in einer Zeitleiste zusammenzuführen und unsichere Zeitangaben zu kennzeichnen."
meta_title: "Zeitleisten für Vorfälle - Reaktion auf Sicherheitsvorfälle"
meta_description: "Lerne, Belege in einer Zeitleiste zusammenzuführen und unsichere Zeitangaben zu kennzeichnen."
meta_keywords: "Zeitleisten, Vorfallreaktion, Cybersicherheit, Linux Journey"
---

Eine Zeitleiste ordnet Beobachtungen aus verschiedenen Quellen zeitlich ein. Verwende eine gemeinsame Zeitzone und halte die ursprünglichen Zeitstempel weiterhin fest. Die Reihenfolge hilft dir zu fragen, welche Beobachtungen zusammenhängen könnten.

## Einen Zeitstempel umrechnen

Hier verwendet der Bericht zum Webdienst UTC. Der Bereitstellungseintrag verwendet UTC+02:00, also eine Ortszeit, bei der die Uhr zwei Stunden weiter ist als bei UTC.

```text
Deployment record:  2026-11-19 11:17:00 +02:00
Web report:         2026-11-19 09:22:00 UTC
```

Auf einem Linux-System mit GNU date liest `-d` einen angegebenen Zeitstempel und `-u` fordert die Ausgabe in UTC an. Das Argument, das mit `+` beginnt, bestimmt das Anzeigeformat.

```bash
$ date -u -d '2026-11-19 11:17:00+02:00' '+%Y-%m-%d %H:%M:%S UTC'
```

Das Ergebnis lautet `2026-11-19 09:17:00 UTC`. In diesem Beispiel liegt es fünf Minuten vor der Meldung zum Webdienst.

:::single-choice{#incident-timelines-earlier-event} Welcher Eintrag liegt auf der umgerechneten Zeitleiste früher?

::option[Der Bereitstellungseintrag.]{#incident-timelines-earlier-event-a .correct explanation="Nach der Umrechnung ergibt er 09:17 Uhr UTC und liegt damit vor der Meldung um 09:22 Uhr."}
::option[Die Meldung zum Webdienst.]{#incident-timelines-earlier-event-b explanation="Die kleinere Stundenzahl allein sagt nichts über die Reihenfolge aus, weil die beiden Einträge unterschiedliche Zeitzonen verwenden."}
::option[Beide fielen auf genau denselben Zeitpunkt.]{#incident-timelines-earlier-event-c explanation="Die umgerechneten Zeiten liegen fünf Minuten auseinander."}
:::

![Aufgezeichnete Umrechnung mit GNU date von 11:17 Uhr bei +02:00 auf 09:17 Uhr UTC](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/incident-response/incident-timelines/normalize-utc.png)

## Beobachtungen von Schätzungen unterscheiden

In einer Meldung kann stehen, dass der erste Fehler gegen 09:19 Uhr auftrat. Halte diese Angabe als Schätzung fest. Die Uhrzeit, zu der ein Nutzer den Fehler meldet, kann von der Uhrzeit der ersten fehlgeschlagenen Anfrage abweichen. Gib für jede Zeile die Quelle und die Genauigkeit der Zeitangabe an.

:::single-choice{#incident-timelines-estimated-time} Ein Teammitglied sagt, es sei gegen 09:19 Uhr gewesen. Wie solltest du das eintragen?

::option[Als exakt 09:19:00 Uhr, bestätigt durch ein Protokoll.]{#incident-timelines-estimated-time-a explanation="Die Quelle gibt eine ungefähre Uhrzeit an."}
::option[Als Ereignis ohne Quellenangabe.]{#incident-timelines-estimated-time-c explanation="Die Quelle hilft einzuschätzen, wie verlässlich die Uhrzeit ist."}
::option[Als ungefähre Uhrzeit mit Verweis auf die Meldung.]{#incident-timelines-estimated-time-b .correct explanation="So bleiben die Aussage der Quelle und die Genauigkeit der Zeitangabe erhalten."}
:::

## Zeitliche Reihenfolge und Ursache unterscheiden

Eine Bereitstellung kann vor einer Störung liegen, ohne sie verursacht zu haben. Prüfe, ob sich der betroffene Pfad geändert hat und ob andere Anhaltspunkte einen Zusammenhang stützen. Halte offene Fragen neben der Zeitleiste fest.

:::single-choice{#incident-timelines-timeline-cause} Was zeigt die zeitliche Reihenfolge für sich allein?

::option[Die Bereitstellung verursachte den Ausfall des öffentlichen Zugangs.]{#incident-timelines-timeline-cause-a explanation="Die Reihenfolge deutet auf einen möglichen Zusammenhang hin, belegt aber keine Ursache."}
::option[Die aufgezeichnete Bereitstellung liegt vor der Meldung zum Webdienst.]{#incident-timelines-timeline-cause-c .correct explanation="Diesen zeitlichen Zusammenhang belegen die Aufzeichnungen."}
::option[Keine anderen Ereignisse können eine Rolle spielen.]{#incident-timelines-timeline-cause-b explanation="Die Zeitleiste enthält ausgewählte Beobachtungen."}
:::

## Zusammenfassung

Du kannst jetzt eine Zeitleiste erstellen, in der Belege und Unsicherheiten sichtbar bleiben.

1. Rechne die Zeitangaben einheitlich in dieselbe Zeitzone um.
2. Gib für jede Zeitangabe die Quelle an und kennzeichne Schätzungen.
3. Leite aus der Reihenfolge passende Folgeprüfungen ab.
