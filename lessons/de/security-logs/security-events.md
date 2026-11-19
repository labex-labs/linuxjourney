---
lesson_id: "security-events"
course_id: "security-logs"
lang: "de"
order_index: 1
title: "Sicherheitsereignisse"
description: "Lerne, ein Sicherheitsereignis, den dazugehörigen Protokolleintrag und eine Warnmeldung auseinanderzuhalten."
meta_title: "Sicherheitsereignisse – Sicherheitsprotokolle"
meta_description: "Lies einen kurzen Linux-Protokolleintrag, ordne eine Warnmeldung ein und entscheide, welche Informationen noch fehlen."
meta_keywords: "Sicherheitsereignisse, Sicherheitsprotokolle, Protokolleinträge, Warnmeldungen, Linux-Protokolle"
---

Ein Server meldet eine fehlgeschlagene Anmeldung. Was ist passiert und was lässt sich daraus schließen? Trenne zunächst das, was der Rechner festgehalten hat, von deinen Schlussfolgerungen.

## Ereignisse und Protokolleinträge

Ein **Ereignis** ist etwas, das passiert ist, etwa ein zurückgewiesener Anmeldeversuch. Ein **Protokolleintrag** hält dieses Ereignis fest. Ein **Protokoll** sammelt solche Einträge. In diesem Kurs übst du mit simulierten Einträgen, die einheitliche Feldnamen verwenden. Echte Werkzeuge benennen und speichern ihre Einträge unterschiedlich.

```text
t=08:55:00Z source=ssh host=web-01 account=alex login=rejected
```

Der Eintrag meldet eine abgelehnte Fernanmeldung für das Konto `alex`. Auch nach dem Versuch kannst du den gespeicherten Eintrag lesen. In späteren Lektionen lernst du, Zeitstempel aus verschiedenen Quellen zu vergleichen.

![LabEx-Terminal mit einem simulierten Eintrag zu einer abgelehnten SSH-Anmeldung für alex auf web-01](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/security-logs/security-events/event-fields.png)

Das LabEx-Terminal gibt denselben simulierten Eintrag aus einer Textdatei aus.

:::single-choice{#security-events-event-versus-record} Was ist in diesem Beispiel das Ereignis selbst?

::option[Die gespeicherte Zeile, die die Ablehnung beschreibt.]{#security-events-event-line explanation="Die Zeile ist der Eintrag, den du nach dem Ereignis lesen kannst."}
::option[Die spätere Durchsicht der gespeicherten Zeile.]{#security-events-event-review explanation="Die Durchsicht findet erst später statt. Das beschriebene Ereignis ist die abgelehnte Anmeldung."}
::option[Der Anmeldeversuch wurde abgelehnt.]{#security-events-event-attempt .correct explanation="Die Ablehnung fand auf dem Server statt. Der Protokolleintrag hält fest, was passiert ist."}
:::

## Felder lesen

Ein **Feld** enthält eine einzelne Information. In diesen Beispielen gibt `t` die erfasste Zeit an. `host` bezeichnet den Rechner, auf dem das Ereignis stattfand, und `source` das Werkzeug, das es meldete. `account` nennt das Konto und `login` das Ergebnis des Anmeldeversuchs.

:::single-choice{#security-events-field-host} Du möchtest wissen, welcher Rechner die abgelehnte Anmeldung erfasst hat. Welcher Wert bezeichnet ihn?

::option[`alex` aus dem Feld account.]{#security-events-field-host-account explanation="Account bezeichnet das Konto, um das es beim Versuch ging."}
::option[`web-01` aus dem Feld host.]{#security-events-field-host-web .correct explanation="Host bezeichnet den Rechner, auf dem das Ereignis stattfand."}
::option[`ssh` aus dem Feld source.]{#security-events-field-host-tool explanation="Source gibt an, welches Werkzeug das Ereignis gemeldet hat."}
:::

## Warnmeldungen und ihre Regeln

Eine **Warnmeldung** macht auf etwas aufmerksam, das geprüft werden sollte. Eine Überwachungsregel kann anschlagen, wenn innerhalb von fünf Minuten drei Anmeldungen für dasselbe Konto auf demselben Host abgelehnt werden. Die Regel gruppiert die Einträge nach Konto, Host und Zeit. Die Warnmeldung besagt, dass die Regel zutrifft. Vielleicht hat jemand einfach mehrmals ein falsches Passwort eingegeben.

:::single-choice{#security-events-alert-interpretation} Die Regel meldet drei fehlgeschlagene Anmeldungen für alex auf web-01. Was geht aus der Warnmeldung hervor?

::option[Die protokollierten Fehlversuche erfüllen die Bedingungen der Regel.]{#security-events-alert-condition .correct explanation="Die Meldung weist auf ein prüfenswertes Muster hin. Die Regel sagt nicht, wer es ausgelöst hat."}
::option[Drei verschiedene Personen haben versucht, sich anzumelden.]{#security-events-alert-people explanation="Drei Versuche können von einer oder von mehreren Personen stammen. Die Regel zählt Einträge."}
::option[Jemand hat sich nach drei Versuchen erfolgreich angemeldet.]{#security-events-alert-success explanation="Die Regel zählt abgelehnte Anmeldungen und sagt nichts über eine spätere erfolgreiche Anmeldung."}
:::

## Die nächste Prüfung auswählen

Wenn du wissen willst, ob sich `alex` später angemeldet hat, suche auf `web-01` nach dem Ergebnis einer Anmeldung nach den Fehlversuchen. Prüfe zuerst, welchen Zeitraum die vorhandenen Einträge abdecken. Ein Protokollexport enthält eine Auswahl von Einträgen und kann vor dem gesuchten Zeitraum enden.

:::single-choice{#security-events-next-record} Dein Export endet um 09:00 Uhr. Du willst prüfen, ob um 09:05 Uhr eine Anmeldung erfolgreich war. Wonach solltest du suchen?

::option[Nach demselben Export in absteigender Zeitfolge.]{#security-events-next-sort explanation="Eine andere Sortierung ändert die Reihenfolge. Sie ergänzt keine Einträge nach 09:00 Uhr."}
::option[Nach Anmeldeprotokollen von web-01, die 09:05 Uhr abdecken.]{#security-events-next-window .correct explanation="Du brauchst die passende Quelle und ein Zeitfenster, in dem das gesuchte Ereignis liegen kann."}
::option[Nach einer weiteren Zählung der Fehlversuche vor 09:00 Uhr.]{#security-events-next-count explanation="Die Zahl beschreibt ein anderes Ergebnis in einem früheren Zeitfenster."}
:::

## Zusammenfassung

Du kannst jetzt einen Sicherheitseintrag lesen und nach einer Warnmeldung die nächste Prüfung wählen.

1. Ein Ereignis von der Zeile unterscheiden, die es festhält.
2. Konto, Host und Ergebnis in einem Beispiel erkennen.
3. Anhand der Warnregel nachvollziehen, was beobachtet wurde.
4. Prüfen, ob Quelle und Zeitraum die Frage beantworten können.
