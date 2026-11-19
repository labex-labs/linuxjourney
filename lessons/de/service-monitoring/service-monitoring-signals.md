---
lesson_id: "service-monitoring-signals"
course_id: "service-monitoring"
lang: "de"
order_index: 1
title: "Signale der Dienstüberwachung"
description: "Lerne, das passende Überwachungssignal für eine Frage zu einem Webdienst auszuwählen."
meta_title: "Signale der Dienstüberwachung - Dienstüberwachung"
meta_description: "Lerne, das passende Überwachungssignal für eine Frage zu einem Webdienst auszuwählen."
meta_keywords: "Überwachungssignale, Dienstüberwachung, DevOps, Linux Journey"
---

Ein Besucher sagt, die Seite sei langsam. Geh von seiner Erfahrung aus und wähle eine Messgröße, mit der du sie beschreiben kannst. Ein **Signal** ist eine Beobachtung wie eine Anzahl, ein Messwert oder ein aufgezeichnetes Ereignis.

## Die Erfahrung der Nutzer prüfen

Die **Verfügbarkeit** beschreibt, ob der Dienst seine erwartete Aufgabe erfüllen kann. Eine Prüfung könnte die Startseite anfragen und kontrollieren, ob eine erfolgreiche Antwort zurückkommt. Die **Latenz** ist die Dauer der Anfrage. Eine Seite kann sich erfolgreich öffnen und trotzdem mehrere Sekunden brauchen.

:::single-choice{#service-monitoring-signals-slow-page} Die Besucher erhalten die Seite, aber erst nach mehreren Sekunden. Welches Signal beschreibt das Problem am direktesten?

::option[Die Anzahl der Container auf dem Server.]{#service-monitoring-signals-slow-page-b explanation="Sie misst nicht, wie lange die Besucher warten."}
::option[Die Zeit, bis die Seite beim Besucher ankommt.]{#service-monitoring-signals-slow-page-a .correct explanation="Die Latenz misst, wie lange die Anfrage gedauert hat."}
::option[Die Größe des Quellcode-Repositorys in Bytes.]{#service-monitoring-signals-slow-page-c explanation="Aus der Größe des Repositorys kannst du die Dauer einer Anfrage nicht ablesen."}
:::

## Anfragen und Fehler zählen

Der **Verkehr** beschreibt, wie stark ein Dienst nachgefragt wird, etwa anhand der Anfragen pro Minute. Erfasse die Gesamtzahl zusammen mit der Zahl fehlgeschlagener Anfragen. Fünf Fehler bei 1.000 Anfragen haben ein anderes Gewicht als fünf Fehler bei zehn Anfragen.

:::single-choice{#service-monitoring-signals-count-context} In zwei Zeitfenstern siehst du jeweils fünf Fehler. Was hilft dir, die Auswirkungen auf Nutzer zu vergleichen?

::option[Die Gesamtzahl der Anfragen pro Zeitfenster.]{#service-monitoring-signals-count-context-b .correct explanation="Du brauchst beide Gesamtzahlen als Nenner für den Vergleich der Fehlerraten."}
::option[Der Name des Dashboards.]{#service-monitoring-signals-count-context-a explanation="Der Name verrät, wo das Diagramm steht, aber nichts über den Verkehr."}
::option[Die Reihenfolge der Dienste in der Liste.]{#service-monitoring-signals-count-context-c explanation="Die Position in der Liste sagt nichts über die Anzahl betroffener Anfragen aus."}
:::

## Engpässe erkennen

Die **Sättigung** gibt an, wie nah eine Ressource an ihrer Kapazitätsgrenze ist. Ein Dienst kann auf die Datenbank warten, obwohl der Webprozess läuft. Vergleiche die Messwerte der Ressource mit dem Verhalten, das Nutzer bemerken, bevor du Schlüsse ziehst.

:::single-choice{#service-monitoring-signals-saturation-check} Die Anfragen werden langsamer, während die Warteschlange wächst. Was ist ein sinnvoller nächster Schritt?

::option[Behaupte, die Warteschlange sei eindeutig die Ursache.]{#service-monitoring-signals-saturation-check-a explanation="Beide Änderungen liefern einen Anhaltspunkt. Für die Ursache brauchst du weitere Belege."}
::option[Zähle die auf dem Host gespeicherten Images erneut.]{#service-monitoring-signals-saturation-check-b explanation="Die verfügbaren Images erklären nicht, warum Anfragen warten."}
::option[Prüfe die Ressource, welche die wartenden Aufträge abarbeitet.]{#service-monitoring-signals-saturation-check-c .correct explanation="Dabei kannst du feststellen, ob die Ressource mit den Aufträgen Schritt hält."}
:::

## Zusammenfassung

Du kannst jetzt ein Signal passend dazu auswählen, was ein Nutzer bemerkt hat.

1. Unterscheide Verfügbarkeit und Latenz.
2. Setze die Fehlerzahl ins Verhältnis zum Anfragevolumen.
3. Nutze Sättigung als Hinweis auf mögliche Kapazitätsengpässe.
