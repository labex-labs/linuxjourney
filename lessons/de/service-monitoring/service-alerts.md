---
lesson_id: "service-alerts"
course_id: "service-monitoring"
lang: "de"
order_index: 6
title: "Warnmeldungen für Dienste"
description: "Lerne, die Bedingung, das Zeitfenster und den nächsten Schritt einer Warnmeldung zu verstehen."
meta_title: "Warnmeldungen für Dienste - Dienstüberwachung"
meta_description: "Lerne, die Bedingung, das Zeitfenster und den nächsten Schritt einer Warnmeldung zu verstehen."
meta_keywords: "Warnmeldungen, Dienstüberwachung, DevOps, Linux Journey"
---

Ein Dashboard zeigt Messwerte. Eine **Warnmeldung** weist dich auf einen Zustand hin, der eine Reaktion erfordern kann. Eine gute Warnmeldung hilft dir zu erkennen, was passiert ist und was du prüfen solltest.

## Die Bedingung der Warnmeldung lesen

Eine Regel könnte prüfen, ob innerhalb von fünf Minuten mehr als 5 Prozent der Anfragen an die Startseite fehlschlagen. Zusätzlich verlangt sie mindestens 100 Anfragen, damit die Stichprobe für diesen Dienst aussagekräftig ist.

```text
Window   09:10–09:15 UTC
Route    /
Requests 120
Failures 12
```

Zwölf Fehler bei 120 Anfragen ergeben 10 Prozent. Beide Bedingungen sind erfüllt. Die Meldung weist auf die beobachteten Fehler beim Aufruf der Startseite hin.

:::single-choice{#service-alerts-condition-match} Würde dieselbe Regel bei einem Fehler in zehn Anfragen eine Warnmeldung auslösen?

::option[Nein, weil die Mindestzahl an Anfragen nicht erreicht wurde.]{#service-alerts-condition-match-b .correct explanation="Bei dieser Beispielregel müssen sowohl die Fehlerrate als auch die Anzahl die jeweilige Bedingung erfüllen."}
::option[Ja, weil die Fehlerrate über 5 Prozent liegt.]{#service-alerts-condition-match-a explanation="Die Bedingung verlangt zusätzlich mindestens 100 Anfragen."}
::option[Nein, weil ein Fehler bei zehn Anfragen 1 Prozent ergibt.]{#service-alerts-condition-match-c explanation="Eins von zehn sind 10 Prozent, aber die Anzahl der Anfragen ist für diese Regel zu klein."}
:::

## Das Zeitfenster prüfen

Verwende das Zeitfenster aus der Meldung, auch wenn das Dashboard inzwischen normale Werte zeigt. Die Warnmeldung kann sich auf einen früheren Zustand beziehen. Prüfe, ob der Messwert wieder im üblichen Bereich liegt und ob die wichtigsten Funktionen für Nutzer wieder verfügbar sind.

:::single-choice{#service-alerts-alert-window} Die Warnmeldung kam um 09:16 Uhr und bezieht sich auf 09:10 bis 09:15 Uhr. Wo solltest du zuerst nach den zugehörigen Fehlern suchen?

::option[Nur in einem Bericht aus der Vorwoche.]{#service-alerts-alert-window-b explanation="Er kann Vergleichswerte liefern, deckt aber das betroffene Zeitfenster nicht ab."}
::option[Nur in den Aufzeichnungen nach 09:16 Uhr.]{#service-alerts-alert-window-c explanation="Zwischen der Beobachtung und dem Eintreffen der Meldung kann Zeit vergehen."}
::option[Im Zeitfenster, das die Warnmeldung nennt.]{#service-alerts-alert-window-a .correct explanation="In diesem Zeitraum hat die Regel die Fehler gezählt."}
:::

## Den nächsten Schritt wählen

Eine Warnmeldung über fehlgeschlagene Aufrufe der Startseite kann auf deren Messwerte und aktuelle Protokolle verweisen. Prüfe zuerst, was Nutzer bemerken, und untersuche dann die Ursache. Hat sich der Dienst erholt, halte genug Informationen fest, um eine wiederkehrende Warnmeldung untersuchen zu können.

:::single-choice{#service-alerts-next-check} Mit welchem ersten Schritt prüfst du direkt, ob Aufrufe der Startseite weiterhin fehlschlagen?

::option[Zähle alle Container-Images im Cache.]{#service-alerts-next-check-a explanation="Die Warnmeldung bezieht sich auf die Ergebnisse laufender Anfragen."}
::option[Sende eine freigegebene Testanfrage an den betroffenen Pfad.]{#service-alerts-next-check-c .correct explanation="Mit einer neuen Anfrage prüfst du, ob der gemeldete Fehler dort weiterhin auftritt."}
::option[Deaktiviere die Regel, damit keine Meldung mehr erscheint.]{#service-alerts-next-check-b explanation="Das ändert die Benachrichtigungen, ohne die Funktion des Dienstes zu prüfen."}
:::

## Zusammenfassung

Du kannst jetzt eine Warnmeldung lesen und entscheiden, was du überprüfen solltest.

1. Prüfe Messgröße, Schwellenwert und Mindestgröße der Stichprobe.
2. Suche im Zeitfenster der Warnmeldung nach passenden Anhaltspunkten.
3. Stelle mit einer passenden Prüfung fest, ob Nutzer das Problem weiterhin bemerken.
