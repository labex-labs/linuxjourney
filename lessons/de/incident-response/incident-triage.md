---
lesson_id: "incident-triage"
course_id: "incident-response"
lang: "de"
order_index: 1
title: "Ersteinschätzung eines Vorfalls"
description: "Lerne, aus einer ersten Vorfallmeldung eine gezielte Untersuchung abzuleiten."
meta_title: "Ersteinschätzung eines Vorfalls - Reaktion auf Sicherheitsvorfälle"
meta_description: "Lerne, aus einer ersten Vorfallmeldung eine gezielte Untersuchung abzuleiten."
meta_keywords: "Ersteinschätzung, Triage, Vorfallreaktion, Cybersicherheit, Linux Journey"
---

Eine erste Meldung kann besagen, dass eine Seite nicht erreichbar war oder dass eine Warnung ausgelöst wurde. Bei der **Triage** entscheidest du, was zuerst Aufmerksamkeit braucht. Notiere den betroffenen Dienst, die Uhrzeit und das beobachtete Verhalten, bevor du eine Maßnahme auswählst.

## Die Meldung lesen

Ein Teammitglied schreibt diese simulierte Meldung.

```text
09:22 UTC: Visitors received 503 from the public homepage.
The staff preview still loaded during the same check.
First failure observed at approximately 09:19 UTC.
```

Die Meldung nennt zwei Pfade und zwei unterschiedliche Beobachtungen. Überprüfe das Ergebnis für die öffentliche Startseite und halte die Uhrzeit und die geprüfte Adresse fest.

:::single-choice{#incident-triage-affected-service} Auf welches Fehlerbild sollte sich die erste Prüfung konzentrieren?

::option[Die interne Vorschau liefert 503.]{#incident-triage-affected-service-b explanation="In der Meldung steht, dass sich die Vorschau weiterhin öffnen ließ."}
::option[Die öffentliche Startseite liefert 503.]{#incident-triage-affected-service-a .correct explanation="Das ist der betroffene Pfad aus der Meldung."}
::option[Eine fehlende Seite auf einem anderen Host.]{#incident-triage-affected-service-c explanation="Dieser Pfad fällt nicht unter die Meldung."}
:::

## Die Auswirkungen abschätzen

Prüfe, wie viele Nutzer oder Anfragen betroffen sind und ob der Dienst nutzbar bleibt. Stelle fest, ob die Störung noch andauert. Kennzeichne unsichere Zahlen als Schätzungen, bis du bessere Belege hast. Entscheide anhand des Plans zur Vorfallreaktion, wen du benachrichtigen musst.

:::single-choice{#incident-triage-triage-scope} Welche Beobachtung hilft dir zu entscheiden, ob das Problem noch dringend ist?

::option[Eine aktuelle Prüfung des fehlerhaften Pfads und die Ergebnisse der jüngsten Anfragen.]{#incident-triage-triage-scope-b .correct explanation="Das zeigt, ob das Fehlerbild noch auftritt und wie verbreitet es ist."}
::option[Das Alter des ersten Commits im Repository.]{#incident-triage-triage-scope-a explanation="Daran erkennst du die aktuellen Auswirkungen nicht."}
::option[Allein die Einstufung der Schwere in der ursprünglichen Meldung.]{#incident-triage-triage-scope-c explanation="Die ursprüngliche Einstufung gibt Kontext. Die aktuellen Auswirkungen helfen dir, die Dringlichkeit einzuschätzen."}
:::

## Einen passenden ersten Schritt wählen

Wenn auch die aktuelle Anfrage fehlschlägt, sichere das Ergebnis. Prüfe dann kürzliche Änderungen am Dienst und seine Protokolle aus dem betroffenen Zeitfenster. Ein anderer Pfad, der zur selben Zeit funktioniert, hilft bei der Eingrenzung. Behandle die erste plausible Erklärung als Vermutung, bis du sie belegen kannst.

:::single-choice{#incident-triage-first-next-step} Der öffentliche Pfad schlägt weiterhin fehl und die interne Vorschau funktioniert noch. Was solltest du als Nächstes ansehen?

::option[Alle anderen Projekte im Unternehmen.]{#incident-triage-first-next-step-a explanation="Die Meldung bezieht sich auf einen bestimmten Dienst und Zeitraum."}
::option[Einen beliebigen alten Fehler von einem anderen Tag.]{#incident-triage-first-next-step-b explanation="Beginne mit Belegen aus der Zeit rund um den beobachteten Fehler."}
::option[Aufzeichnungen zum öffentlichen Pfad aus dem gemeldeten Zeitfenster.]{#incident-triage-first-next-step-c .correct explanation="Damit kannst du möglicherweise zwischen einem Problem mit dem Zugriffsweg und einem Ausfall des Dienstes unterscheiden."}
:::

## Zusammenfassung

Du kannst jetzt gezielt auf eine erste Vorfallmeldung reagieren.

1. Nenne den betroffenen Pfad, die Zeit und das Fehlerbild.
2. Prüfe die aktuellen Auswirkungen auf Nutzer.
3. Wähle die nächste Belegquelle für den betroffenen Pfad.
