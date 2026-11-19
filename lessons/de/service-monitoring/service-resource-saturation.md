---
lesson_id: "service-resource-saturation"
course_id: "service-monitoring"
lang: "de"
order_index: 5
title: "Ressourcensättigung"
description: "Lerne, anhand von Auslastung und Warteschlangen mögliche Kapazitätsgrenzen eines Dienstes zu erkennen."
meta_title: "Ressourcensättigung - Dienstüberwachung"
meta_description: "Lerne, anhand von Auslastung und Warteschlangen mögliche Kapazitätsgrenzen eines Dienstes zu erkennen."
meta_keywords: "Ressourcensättigung, Auslastung, Dienstüberwachung, DevOps, Linux Journey"
---

Wenn bei einem Dienst mehr Arbeit eingeht, als eine Ressource sofort erledigen kann, müssen Anfragen möglicherweise warten. Längere Wartezeiten können sich in einer Warteschlange und in langsameren Antworten bemerkbar machen.

## Kapazität und Nachfrage einschätzen

Die **Auslastung** beschreibt, wie viel von einer Ressource gerade genutzt wird. Eine Gruppe von Arbeitsprozessen kann beispielsweise vier Aufträge gleichzeitig ausführen. Sind alle vier Prozesse beschäftigt, ist die Gruppe in diesem Moment voll ausgelastet. Trifft ein weiterer Auftrag ein, kann er in einer Warteschlange bleiben, bis ein Prozess frei wird.

:::single-choice{#service-resource-saturation-worker-capacity} Vier Arbeitsprozesse sind beschäftigt und drei Aufträge stehen in der Warteschlange. Was weißt du?

::option[Genau sieben Arbeitsprozesse sind im Einsatz.]{#service-resource-saturation-worker-capacity-b explanation="Drei Aufträge warten noch auf einen freien Platz."}
::option[Alle Anfragen sind bereits fehlgeschlagen.]{#service-resource-saturation-worker-capacity-c explanation="Wartende Aufträge können noch ausgeführt werden, sobald ein Arbeitsprozess frei ist."}
::option[Alle Plätze sind belegt und einige Aufträge warten.]{#service-resource-saturation-worker-capacity-a .correct explanation="Die Zahl der beschäftigten Prozesse zeigt die aktuelle Auslastung, die Warteschlange zeigt die zusätzliche Nachfrage."}
:::

## Messwerte im Zeitverlauf vergleichen

Eine kurze Lastspitze ist etwas anderes als eine Warteschlange, die über mehrere Messungen hinweg wächst. Vergleiche Warteschlange, Latenz und Verkehr im selben Zeitfenster.

```text
Time   Busy workers   Queued jobs   Typical response
09:10       2 / 4           0             80 ms
09:11       4 / 4           5            300 ms
09:12       4 / 4          14            640 ms
```

In diesem Beispiel deuten die volle Auslastung und die wachsende Warteschlange darauf hin, dass Aufträge schneller eintreffen, als sie erledigt werden. Prüfe, womit die Arbeitsprozesse beschäftigt sind.

:::single-choice{#service-resource-saturation-sustained-pressure} Welche Beobachtung deutet am stärksten auf eine anhaltende Überlastung hin?

::option[Zwei beschäftigte Arbeitsprozesse um 09:10 Uhr.]{#service-resource-saturation-sustained-pressure-a explanation="In dieser Zeile waren noch Plätze frei und keine Aufträge warteten."}
::option[Die Warteschlange wächst, während alle Arbeitsprozesse beschäftigt bleiben.]{#service-resource-saturation-sustained-pressure-b .correct explanation="Bei gleichbleibend voller Auslastung sammeln sich immer mehr wartende Aufträge an."}
::option[Eine einzelne langsamere Antwort bei leerer Warteschlange.]{#service-resource-saturation-sustained-pressure-c explanation="Ein langsames Ergebnis kann eine genauere Prüfung rechtfertigen. Eine über mehrere Messungen wachsende Schlange bei voller Auslastung ist ein stärkerer Hinweis auf anhaltende Überlastung."}
:::

![Simulierte Messwerte einer Gruppe von Arbeitsprozessen mit voller Auslastung und wachsender Warteschlange](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/service-monitoring/service-resource-saturation/worker-queue.png)

## Die Ursache prüfen

Arbeitsprozesse können ausgelastet sein, weil Anfragen schneller eintreffen, eine Abhängigkeit langsamer geworden ist oder eine kürzliche Änderung jeden Auftrag verlängert hat. Vergleiche Anfragevolumen, Bearbeitungsdauer und Beobachtungen zu den Abhängigkeiten. Ein zusätzliches Signal hilft dir bei der Wahl der nächsten Maßnahme.

:::single-choice{#service-resource-saturation-next-observation} Das Anfragevolumen blieb stabil, aber die Bearbeitung dauert länger. Was hilft dir, den Rückstau zu erklären?

::option[Vergleiche Auftragsdauer und Antwortzeiten der Abhängigkeiten.]{#service-resource-saturation-next-observation-c .correct explanation="Damit kannst du eingrenzen, warum Aufträge die Plätze länger belegen."}
::option[Ändere die Kapazität, bevor du weitere Anhaltspunkte sammelst.]{#service-resource-saturation-next-observation-a explanation="Mehr Kapazität hilft möglicherweise nicht, wenn die Aufträge auf eine Abhängigkeit warten."}
::option[Zähle die Rollen im Repository.]{#service-resource-saturation-next-observation-b explanation="An den Rollen erkennst du nicht, worauf die Arbeitsprozesse warten."}
:::

## Zusammenfassung

Du kannst eine ausgelastete Ressource von einem anhaltenden Rückstau unterscheiden.

1. Setze die Zahl beschäftigter Arbeitsprozesse ins Verhältnis zur Kapazität der Gruppe.
2. Vergleiche Warteschlangen und Anfrageverhalten im Zeitverlauf.
3. Untersuche, welche Aufträge die knappe Ressource belegen.
