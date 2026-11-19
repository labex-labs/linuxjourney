---
lesson_id: "ci-overview"
course_id: "continuous-integration"
lang: "de"
order_index: 1
title: "Kontinuierliche Integration"
description: "Lerne, wie die kontinuierliche Integration kleine Änderungen prüft, bevor sie in einen gemeinsamen Branch gelangen."
meta_title: "Kontinuierliche Integration - Kontinuierliche Integration"
meta_description: "Lerne, wie die kontinuierliche Integration kleine Änderungen prüft, bevor sie in einen gemeinsamen Branch gelangen."
meta_keywords: "kontinuierliche Integration, CI, DevOps, Linux Journey"
---

Eine Änderung an der Startseite kann bei dir im Browser gut aussehen und bei jemand anderem trotzdem Probleme verursachen. Bei der **kontinuierlichen Integration** (CI) führt das Team Änderungen häufig zusammen und prüft konkrete Versionen mit wiederholbaren Tests.

## Eine Änderung ihrer Prüfung zuordnen

Eine Revision bezeichnet die Version der Dateien, die geprüft wird. Wenn eine vorgeschlagene Änderung `index.html` betrifft, kann CI genau diese Version prüfen und melden, ob sie die Erwartungen erfüllt. Bei dieser Website könnte die Prüfung beispielsweise nach der geforderten Überschrift suchen. Das Team kann das Ergebnis bei der Entscheidung über den Merge berücksichtigen.

:::single-choice{#ci-overview-revision-result} Am Montag war eine Prüfung erfolgreich. Am Dienstag ändert ein neuer Commit die Seite. Was belegt das Ergebnis vom Montag?

::option[Beide Revisionen erfüllen die Anforderungen der Prüfung.]{#ci-overview-revision-result-b explanation="Für den späteren Commit brauchst du ein eigenes Ergebnis."}
::option[Die Revision vom Montag hat diese Prüfung bestanden.]{#ci-overview-revision-result-a .correct explanation="Das Ergebnis gehört zu der Revision, die geprüft wurde."}
::option[Die neue Seite ist für Besucher sichtbar.]{#ci-overview-revision-result-c explanation="Eine Prüfung der Quelldateien sagt nichts über den Stand der veröffentlichten Website aus."}
:::

## Eine fehlgeschlagene Prüfung lesen

Angenommen, die Prüfung meldet, dass die erwartete Überschrift fehlt. Damit weiß der Autor, wo er zuerst nachsehen sollte. Lies die Anforderung und das Prüfergebnis, bevor du die Seite änderst. Vielleicht ist beim Ändern ein Fehler passiert. Vielleicht hat sich auch das gewünschte Verhalten geändert und der Test muss entsprechend angepasst werden.

:::single-choice{#ci-overview-failed-action} Was solltest du zuerst prüfen, wenn die Überschriftenprüfung fehlschlägt?

::option[Die erwartete Überschrift und die Datei in der geprüften Revision.]{#ci-overview-failed-action-b .correct explanation="Ein Vergleich zeigt dir, woher diese konkrete Abweichung kommt."}
::option[Zuerst das Artefakt aus dem letzten erfolgreichen Lauf.]{#ci-overview-failed-action-a explanation="Das Artefakt stammt aus einem älteren Lauf. Das fehlgeschlagene Ergebnis und die geprüfte Datei geben dir direktere Hinweise."}
::option[Die Netzwerkeinstellungen der Besucher.]{#ci-overview-failed-action-c explanation="Diese Prüfung liest eine Datei und sendet keine Browseranfrage."}
:::

## Prüfung und Bereitstellung unterscheiden

Eine Pipeline kann Dateien prüfen, eine Ausgabe erzeugen und sie später an die Bereitstellung übergeben. Ein **Build** erstellt etwas, das spätere Schritte verwenden können, etwa einen Ordner mit Dateien, die ein Webserver direkt ausliefern kann. Ein **Deployment** installiert oder startet eine Version in einer Umgebung. Dein erster CI-Workflow prüft eine Seite vor der weiteren Verarbeitung.

:::single-choice{#ci-overview-output-vs-live} Die Tests waren erfolgreich und ein Website-Archiv wurde erstellt. Wie prüfst du, dass Besucher diese Version tatsächlich aufrufen können?

::option[Mit einer zweiten Kopie des Prüfprotokolls.]{#ci-overview-output-vs-live-a explanation="Das Protokoll beschreibt die Prüfung und den Build."}
::option[Indem du nachsiehst, ob das Archiv existiert.]{#ci-overview-output-vs-live-b explanation="Ein Archiv kann vorhanden sein, ohne dass ein Webserver es ausliefert."}
::option[Mit einem Bereitstellungseintrag und einer erfolgreichen Anfrage an die vorgesehene Seite.]{#ci-overview-output-vs-live-c .correct explanation="Damit kannst du die gebaute Version einer Antwort aus der Zielumgebung zuordnen."}
:::

## Zusammenfassung

Du kannst jetzt erklären, welche Rolle CI auf dem Weg einer Änderung spielt.

1. Ordne jedes Prüfergebnis einer konkreten Revision zu.
2. Leite aus einer fehlgeschlagenen Prüfung ab, was du zuerst untersuchen solltest.
3. Unterscheide zwischen Prüfung, Build und Bereitstellung.
