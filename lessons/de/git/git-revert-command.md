---
lesson_id: "git-revert-command"
course_id: "git"
lang: "de"
order_index: 8
title: "git revert"
description: "Lerne, wie git revert eine Änderung rückgängig macht und den ursprünglichen Commit im Verlauf behält."
meta_title: "git revert – Git"
meta_description: "Erstelle einen neuen Commit, der eine geteilte Änderung rückgängig macht, und prüfe anschließend Dateien und Verlauf."
meta_keywords: "git revert, Änderung rückgängig machen, Git-Verlauf, DevOps, Linux Journey"
---

Du kannst auch eine schon geteilte Änderung rückgängig machen. Mit `git revert` speicherst du die entgegengesetzte Änderung als neuen Commit. Im Verlauf bleiben damit die ursprüngliche Änderung und ihre Rücknahme sichtbar.

## Die Änderung finden

Im Übungsrepository enthält `main` die Commits für die Startseite und die Statusseite. Prüfe den neuesten Eintrag in der Kurzansicht des Verlaufs. Die IDs unten dienen nur als Beispiel.

```text
$ git log --oneline
3ab4501 Add a health page
a12c345 Set the homepage heading
```

`HEAD` bezeichnet den Commit, den du gerade ausgecheckt hast. Prüfe, ob er die Änderung enthält, die du zurücknehmen möchtest. Kontrolliere mit `git status`, ob der Arbeitsbaum sauber ist.

:::single-choice{#git-revert-command-newest-commit} Welche Änderung würde ein Revert von HEAD in diesem Beispiel rückgängig machen?

::option[Die frühere Änderung an der Startseitenüberschrift.]{#git-revert-command-newest-commit-b explanation="Die Überschrift wurde im vorherigen Commit geändert."}
::option[Beide Änderungen in einer Aktion.]{#git-revert-command-newest-commit-c explanation="HEAD bezeichnet hier einen Commit. Der Revert bezieht sich auf diesen Commit."}
::option[Das Hinzufügen der Statusseite.]{#git-revert-command-newest-commit-a .correct explanation="HEAD zeigt auf den neuesten angezeigten Eintrag in diesem Branch."}
:::

## Die Rücknahme speichern

Mache im sauberen Übungsrepository den Commit der Statusseite rückgängig. Dabei werden Dateien im Arbeitsbaum geändert und ein Commit erstellt. Mit `--no-edit` behältst du die von Git vorgeschlagene Revert-Nachricht.

```bash
$ git revert --no-edit HEAD
```

Im Beispiel wird die Statusdatei entfernt, weil sie im ursprünglichen Commit hinzugefügt wurde. Wenn spätere Arbeit dieselben Zeilen geändert hat, kann Git anhalten und dich bitten, den Konflikt aufzulösen. Prüfe dann den Status, bevor du weitermachst.

:::single-choice{#git-revert-command-undo-effect} Welche Dateiänderung solltest du nach einem erfolgreichen Revert sehen?

::option[Die Datei der Startseite und die Statusseite werden beide gelöscht.]{#git-revert-command-undo-effect-a explanation="Der ältere Commit für die Startseite bleibt wirksam."}
::option[Die Datei der Statusseite wird entfernt.]{#git-revert-command-undo-effect-b .correct explanation="Der Revert nimmt das Hinzufügen der Datei aus dem gewählten Commit zurück."}
::option[Die Statusseite wird ein zweites Mal hinzugefügt.]{#git-revert-command-undo-effect-c explanation="Revert wendet die entgegengesetzte Änderung an. Das Hinzufügen wird nicht wiederholt."}
:::

![Git-Verlauf mit dem neuen Revert-Eintrag und dem ursprünglichen Commit für die Statusseite](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/git/git-revert-command/recorded-undo.png)

## Den Verlauf danach prüfen

Führe erneut `git log --oneline` aus. Über dem ursprünglichen Commit für die Statusseite sollte ein neuer Revert-Eintrag stehen. Prüfe mit `git status --short`, ob lokale Änderungen übrig sind. Der neue Commit kann wie jede andere Änderung geprüft und geteilt werden.

:::single-choice{#git-revert-command-history-after-revert} Was sollte unter dem neuen Revert-Eintrag weiterhin erscheinen?

::option[Der ursprüngliche Commit für die Statusseite.]{#git-revert-command-history-after-revert-c .correct explanation="Das Paar dokumentiert die Änderung und ihre Rücknahme."}
::option[Nur der erste Commit für die Überschrift.]{#git-revert-command-history-after-revert-a explanation="Der ursprüngliche Commit für die Statusseite bleibt im Verlauf sichtbar."}
::option[Keine Commits.]{#git-revert-command-history-after-revert-b explanation="Ein Revert fügt einen Commit hinzu und ersetzt nicht den Verlauf des Branches."}
:::

## Andere Änderungen erhalten

Angenommen, der Verlauf enthält drei separate Änderungen. Zuerst wurde die Statusdatei hinzugefügt. Danach wurde ein Tippfehler auf der Startseite korrigiert. Beide Commits wurden geteilt. Du kannst die Statusdatei entfernen, indem du den zugehörigen Commit rückgängig machst. Die unabhängige Korrektur bleibt erhalten. Prüfe Verlauf und betroffene Dateien, bevor du einen Commit auswählst.

:::single-choice{#git-revert-command-final-application} Welche Prüfung zeigt, dass die beabsichtigten Änderungen erhalten geblieben sind?

::option[Der Commit mit der Statusdatei ist aus dem Verlauf verschwunden.]{#git-revert-command-final-application-b explanation="Ein Revert lässt den ursprünglichen Eintrag im Verlauf bestehen."}
::option[Die Tippfehlerkorrektur ist ebenfalls von der Startseite verschwunden.]{#git-revert-command-final-application-c explanation="Die Korrektur war eine separate Änderung und soll erhalten bleiben."}
::option[Die Statusdatei ist weg, die korrigierte Startseite bleibt erhalten und der Verlauf zeigt die Rücknahme.]{#git-revert-command-final-application-a .correct explanation="Diese Beobachtungen prüfen die gewählte Rücknahme, die unabhängige Änderung und den neuen Eintrag im Verlauf."}
:::

## Zusammenfassung

Du kannst jetzt einen Commit rückgängig machen und die Änderung samt Rücknahme nachvollziehbar halten.

1. Den genauen Commit finden, dessen Änderung du zurücknehmen möchtest.
2. Den Commit in einem sauberen Arbeitsbaum rückgängig machen.
3. Beide Einträge im Verlauf überprüfen.
