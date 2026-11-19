---
lesson_id: "incident-reports"
course_id: "incident-response"
lang: "de"
order_index: 6
title: "Vorfallberichte"
description: "Lerne, eine kurze Meldung zum Vorfall anhand von Beobachtungen und offenen Fragen zu schreiben."
meta_title: "Vorfallberichte - Reaktion auf Sicherheitsvorfälle"
meta_description: "Lerne, eine kurze Meldung zum Vorfall anhand von Beobachtungen und offenen Fragen zu schreiben."
meta_keywords: "Vorfallberichte, Vorfallreaktion, Cybersicherheit, Linux Journey"
---

Ein kurzer Vorfallbericht hilft einer anderen Person, die Untersuchung zu übernehmen, ohne sie vollständig nachvollziehen zu müssen. Nenne den betroffenen Dienst, einige Beobachtungen mit Zeitangabe und den nächsten Schritt.

## Beobachtungen berichten

Hier sind drei simulierte Aufzeichnungen zum Dienstvorfall.

```text
09:17 UTC  Deployment record: version 3 reached production
09:22 UTC  Visitor-path check: homepage returned 503
09:31 UTC  After rollback: version 2, homepage returned 200
```

Die Einträge zeigen eine Änderung, eine fehlgeschlagene Prüfung und eine erfolgreiche Prüfung nach der Wiederherstellung. Nenne den betroffenen Pfad und die Uhrzeit. Halte genau fest, was geprüft wurde.

:::single-choice{#incident-reports-report-claim} Welche Aussage kannst du direkt aus den Aufzeichnungen ableiten?

::option[Die Prüfung der Startseite schlug um 09:22 Uhr fehl und war nach dem Rollback erfolgreich.]{#incident-reports-report-claim-b .correct explanation="Das fasst die beobachteten Ergebnisse und ihre Reihenfolge zusammen."}
::option[Version 3 hat definitiv die Datenbank beschädigt.]{#incident-reports-report-claim-a explanation="Die Aufzeichnungen zeigen nicht, wodurch der Fehler entstand."}
::option[Alle Nutzer waren während des gesamten Zeitfensters betroffen.]{#incident-reports-report-claim-c explanation="Die vorliegenden Ergebnisse erfassen nicht jede Anfrage."}
:::

![Simulierte Belege zum Vorfall mit einer Änderung in der Produktionsumgebung, einer 503-Antwort und einer erfolgreichen Wiederherstellungsprüfung](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/incident-response/incident-reports/evidence-timeline.png)

## Offene Fragen benennen

Eine erfolgreiche Anfrage nach dem Rollback kann Anlass sein, die Bereitstellung zu untersuchen. Lass die Ursache offen, bis Belege sie stützen. Die für den Dienst zuständige Person kann zum Beispiel die Dienstprotokolle beider Versionen für das Zeitfenster der fehlgeschlagenen Anfrage vergleichen.

:::single-choice{#incident-reports-uncertainty-statement} Welche Aussage gehört zu den offenen Fragen?

::option[Es gibt nichts, was sich sinnvoll untersuchen lässt.]{#incident-reports-uncertainty-statement-b explanation="Die Release- und Fehlereinträge grenzen eine sinnvolle Folgeprüfung ein."}
::option[Der Dienst war für immer unerreichbar.]{#incident-reports-uncertainty-statement-c explanation="Das spätere erfolgreiche Ergebnis widerlegt die Aussage für die Testanfrage."}
::option[Die Ursache der 503-Antwort ist noch ungeklärt.]{#incident-reports-uncertainty-statement-a .correct explanation="Die Belege zeigen den Fehler und die Wiederherstellungsprüfung. Für die Ursache fehlen noch Belege."}
:::

## Die nächste Prüfung übergeben

Nenne, wer den nächsten Schritt übernehmen kann, welche Aufzeichnungen gesucht werden sollen und welches Ergebnis die offene Frage beantworten würde. Lass Zugangsdaten und personenbezogene Angaben in Meldungen an größere Verteiler weg. Ein kurzer Bericht kann für berechtigte Personen auf geschützte Belege verweisen.

:::single-choice{#incident-reports-useful-handoff} Welcher nächste Schritt ergibt sich am besten aus diesem Fall?

::option[Bitte jemanden um einen allgemeinen Screenshot ohne Angaben zu Uhrzeit oder Dienst.]{#incident-reports-useful-handoff-a explanation="Damit legst du keine Belege für den Fehler fest."}
::option[Bitte die für den Dienst zuständige Person, die Protokolle von Version 3 für das Zeitfenster der fehlgeschlagenen Startseitenanfrage zu prüfen.]{#incident-reports-useful-handoff-c .correct explanation="Damit ordnest du der offenen Frage eine konkrete Quelle und ein Zeitfenster zu."}
::option[Bitte die zuständige Person, nur die bereits erfolgreiche Prüfung von Version 2 zu wiederholen.]{#incident-reports-useful-handoff-b explanation="Das kann die Wiederherstellung erneut bestätigen. Der frühere Fehler von Version 3 bleibt dadurch ungeklärt."}
:::

## Den Umfang der Wiederherstellung festhalten

Ein Bericht kann festhalten, dass die Wiederherstellung geprüft wurde und das Ausmaß der Auswirkungen noch nicht feststeht. Eine erfolgreiche Prüfung der Startseite nach dem Rollback belegt die Wiederherstellung für den getesteten Pfad. Um die Zahl betroffener Besucher zu schätzen, brauchst du noch Anfragezahlen oder andere geeignete Beobachtungen aus dem Fehlerzeitfenster.

:::single-choice{#incident-reports-final-application} Welche Übergabe gibt beide Erkenntnisse korrekt wieder?

::option[Für alle Besucher war der Dienst wiederhergestellt, weil eine einzelne Anfrage 200 zurückgab.]{#incident-reports-final-application-b explanation="Die erfolgreiche Anfrage bestätigt nur den getesteten Pfad und Zeitpunkt."}
::option[Die fehlgeschlagene Prüfung sollte jetzt aus dem Bericht entfernt werden, da die Wiederherstellung erfolgreich war.]{#incident-reports-final-application-c explanation="Der frühere Fehler gehört zu den Belegen für den Vorfall."}
::option[Die Prüfung der Startseite war nach dem Rollback erfolgreich. Wie viele Anfragen insgesamt betroffen waren, ist weiterhin unbekannt.]{#incident-reports-final-application-a .correct explanation="Der Bericht unterscheidet das bestätigte Prüfergebnis von einer Zahl, die aus den vorhandenen Aufzeichnungen nicht hervorgeht."}
:::

Wenn du bereits mit Paketmitschnitten und Host-Aufzeichnungen gearbeitet hast, findest du eine längere Übung in [Wiederholung der SOC-Grundlagen](https://labex.io/courses/project-soc-foundations-review).

## Zusammenfassung

Du kannst jetzt einen Vorfall mit beobachteten Fakten, offenen Fragen und einem nächsten Schritt übergeben.

1. Nenne den betroffenen Pfad und die beobachtete Abfolge.
2. Unterscheide eine vermutete Ursache von bestätigten Beobachtungen.
3. Weise eine Folgeprüfung mit konkreter Quelle und konkretem Zeitfenster zu.
