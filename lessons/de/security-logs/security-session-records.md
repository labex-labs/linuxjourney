---
lesson_id: "security-session-records"
course_id: "security-logs"
lang: "de"
order_index: 4
title: "Sitzungsprotokolle"
description: "Lerne, Sitzungsbeginn und Sitzungsende zuzuordnen und die Reichweite eines Protokollauszugs einzuschätzen."
meta_title: "Sitzungsprotokolle – Sicherheitsprotokolle"
meta_description: "Lies Linux-Sitzungsprotokolle, ordne Beginn und Ende einander zu und prüfe, was bei einem fehlenden Ende noch zu klären ist."
meta_keywords: "Linux-Sitzungsprotokolle, Sitzungsbeginn, Sitzungsende, Sitzungs-ID, Protokollaufbewahrung"
---

Eine erfolgreiche Anmeldeprüfung zeigt, dass jemand sich mit einem Konto anmelden konnte. Eine **Sitzung** ist der Zeitraum zwischen Anmeldung und Abmeldung oder Verbindungsabbruch. Wenn das System beide Ereignisse protokolliert, zeigen die entsprechenden Einträge, wann die Sitzung begonnen und geendet hat.

## Den Sitzungsbeginn lesen

Ein System kann eine **Sitzungs-ID** vergeben, damit sich eine Sitzung auf einem Rechner eindeutig zuordnen lässt. Die simulierten Zeilen zeigen für dasselbe Konto auf `web-01` zwei Sitzungsbeginne. Alle Zeiten in dieser Lektion verwenden dieselbe Zeitzone.

```text
t=09:14:05Z source=session host=web-01 account=alex session=42 state=opened
t=09:17:00Z source=session host=web-01 account=alex session=43 state=opened
```

Die erste Zeile meldet den Beginn von Sitzung 42. Die zweite meldet den Beginn einer separaten Sitzung 43 auf demselben Host.

:::single-choice{#security-session-records-two-openings} Welche Aussage stützen die beiden Einträge?

::option[Die erste Sitzung endete, als die zweite begann.]{#security-session-records-open-ended explanation="Der zweite Eintrag zeigt den Beginn einer weiteren Sitzung. Wann die erste endete, geht daraus nicht hervor."}
::option[Zwei verschiedene Konten meldeten sich am Host an.]{#security-session-records-open-accounts explanation="Beide Zeilen nennen dasselbe Konto. Das Sitzungsfeld unterscheidet die beiden Aktivitäten."}
::option[Dasselbe Konto eröffnete zwei getrennte Sitzungen.]{#security-session-records-open-two .correct explanation="In beiden Zeilen steht alex. Jede Sitzung hat auf web-01 eine eigene ID."}
:::

## Sitzungsbeginn und Sitzungsende zuordnen

Lies Host und Sitzungs-ID zusammen, bevor du zwei Einträge einander zuordnest. Vergleiche den folgenden Eintrag über das Sitzungsende mit den Einträgen über den Beginn.

```text
t=09:20:05Z source=session host=web-01 account=alex session=42 state=closed
```

Auf `web-01` liegen Beginn und Ende der Sitzung 42 sechs Minuten auseinander. Das Paar zeigt den protokollierten Anfang und das Ende. Es listet keine Aktionen auf, die in der Zwischenzeit ausgeführt wurden.

![LabEx-Terminal mit dem simulierten Beginn der Sitzungen 42 und 43 sowie dem Ende der Sitzung 42](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/security-logs/security-session-records/session-records.png)

Das Terminal stellt die simulierten Einträge über Sitzungsbeginn und Sitzungsende zusammen dar.

:::single-choice{#security-session-records-pair-ids} Angenommen, die Zeile über das Ende zeigt stattdessen `session=43`, während Host und Uhrzeit gleich bleiben. Wann hätte diese Sitzung begonnen?

::option[Um 09:14:05 Uhr.]{#security-session-records-pair-forty-two explanation="Dieser Eintrag nennt dasselbe Konto, gehört aber zur Sitzung 42."}
::option[Um 09:17:00 Uhr.]{#security-session-records-pair-forty-three .correct explanation="Web-01 und die Sitzungs-ID 43 passen zum zweiten Beginn um 09:17:00 Uhr."}
::option[Um 09:20:05 Uhr.]{#security-session-records-pair-end-time explanation="Das ist das protokollierte Ende. Der passende Beginn steht in einem anderen Eintrag."}
:::

## Ein fehlendes Sitzungsende prüfen

Kehre zum ursprünglichen Eintrag über das Ende der Sitzung 42 zurück. Der Auszug endet um 09:21 Uhr und enthält weiterhin kein passendes Ende für Sitzung 43. Die Sitzung könnte zu diesem Zeitpunkt noch aktiv gewesen sein. Der Eintrag über das Ende kann auch außerhalb des Zeitraums liegen oder in dieser Quelle fehlen. Die **Aufbewahrungsfrist** gibt an, wie lange ein Protokolleintrag gespeichert und einsehbar bleibt.

:::single-choice{#security-session-records-missing-close} Was kannst du allein aus dem Auszug über Sitzung 43 sagen?

::option[Sie war am Ende des Auszugs noch aktiv.]{#security-session-records-missing-active explanation="Das ist möglich, aber das fehlende Ende belegt den tatsächlichen Zustand nicht."}
::option[Der Auszug enthält keinen Endzeitpunkt für diese Sitzung.]{#security-session-records-missing-unknown .correct explanation="Das beschreibt die verfügbaren Einträge. Eine spätere oder andere Quelle kann den Endzeitpunkt enthalten."}
::option[Sie endete zusammen mit Sitzung 42.]{#security-session-records-missing-together explanation="Der vorhandene Eintrag gehört zu Sitzung 42. Für 43 gibt es hier keinen passenden Eintrag zum Ende."}
:::

## Die passende Quelle wählen

Für einen früheren Endzeitpunkt suchst du im späteren Protokoll desselben Hosts nach einem passenden Eintrag. Willst du wissen, ob die Sitzung jetzt aktiv ist, prüfe die aktuelle Sitzungsliste auf diesem Host. Ein gespeichertes Protokoll und eine aktuelle Liste beantworten Fragen zu unterschiedlichen Zeitpunkten.

:::single-choice{#security-session-records-current-status} Du musst wissen, ob Sitzung 43 jetzt aktiv ist. Welche Quelle hilft am meisten?

::option[Eine aktuelle Sitzungsliste von web-01.]{#security-session-records-current-list .correct explanation="Die aktuelle Liste zeigt die Sitzungen, die der Host jetzt als aktiv meldet."}
::option[Eine ältere Kopie des Eintrags über den Sitzungsbeginn.]{#security-session-records-current-opening explanation="Sie zeigt, dass die Sitzung begonnen hat. Ob sie noch aktiv ist, steht dort nicht."}
::option[Ein Eintrag über das Ende der Sitzung 42 auf web-01.]{#security-session-records-current-other explanation="Das Ende einer anderen Sitzung beantwortet die Frage zu Sitzung 43 nicht."}
:::

## Zusammenfassung

Du kannst jetzt anhand von Sitzungsprotokollen den erfassten Beginn und das Ende einer Sitzung beschreiben.

1. Den Sitzungsbeginn mit Host und Sitzungs-ID erkennen.
2. Einen Eintrag über das Sitzungsende dem richtigen Beginn zuordnen.
3. Benennen, was ohne einen Eintrag zum Ende offenbleibt.
4. Je nach Frage zwischen historischen Einträgen und einer aktuellen Sitzungsliste wählen.
