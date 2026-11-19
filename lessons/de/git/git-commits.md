---
lesson_id: "git-commits"
course_id: "git"
lang: "de"
order_index: 4
title: "Commits"
description: "Lerne, einen vorgemerkten Stand zu speichern und im Git-Verlauf zu finden."
meta_title: "Commits – Git"
meta_description: "Speichere die ausgewählten Änderungen mit einer Commit-Nachricht und finde den Commit anhand seiner ID im Verlauf."
meta_keywords: "Git-Commits, Staging-Bereich, git commit, git log, DevOps, Linux Journey"
---

Ein **Commit** speichert die Dateien, die im Staging-Bereich ausgewählt sind. Zum Commit gehören außerdem eine Nachricht, die Angaben zum Autor und die Verbindung zu früheren Commits. Über die von Git vergebene ID findest du genau diesen Punkt im Verlauf wieder.

## Die Autorenangaben für das Übungsrepository festlegen

Git speichert zu jedem Commit einen Namen und eine E-Mail-Adresse. Lege Beispielwerte fest, die nur für dieses Repository gelten. Diese Angaben stehen im Verlauf. Sie geben dir keine Zugriffsrechte auf einen entfernten Dienst.

```bash
$ git config --local user.name "Journey Learner"
$ git config --local user.email "learner@example.com"
```

Verwende das Übungsrepository mit der vorgemerkten Datei `index.html`. Mit `git status` kannst du überprüfen, welche Dateien in den Commit aufgenommen werden.

:::single-choice{#git-commits-identity-scope} Was bewirkt die Option --local hier?

::option[Sie meldet dich bei einem gemeinsamen Hosting-Dienst an.]{#git-commits-identity-scope-b explanation="Name und E-Mail-Adresse sind Metadaten für den Commit. Die Anmeldung am entfernten Dienst ist davon getrennt."}
::option[Sie legt die Autorenangaben für dieses Repository fest.]{#git-commits-identity-scope-a .correct explanation="Die lokalen Einstellungen gelten für das aktuelle Repository."}
::option[Sie ändert den Autor aller vorhandenen Commits.]{#git-commits-identity-scope-c explanation="Die Einstellungen wirken sich erst auf künftige Commits aus."}
:::

## Den ausgewählten Stand speichern

Führe `git commit` aus, nachdem du die gewünschte Fassung vorgemerkt hast. Mit `-m` gibst du die Nachricht direkt auf der Kommandozeile an.

```bash
$ git commit -m "Set the homepage heading"
```

Der Commit speichert die vorgemerkte Fassung einer Datei. Wenn du sie nach dem Vormerken im Arbeitsbaum weiter bearbeitest, bleibt die spätere Änderung außerhalb des Commits, bis du sie ebenfalls vormerkst.

:::single-choice{#git-commits-staged-snapshot} Du hast Welcome vorgemerkt und dann Hi eingegeben, ohne die Datei erneut vorzumerken. Welche Überschrift enthält der Commit?

::option[Welcome, weil diese Fassung vorgemerkt war.]{#git-commits-staged-snapshot-c .correct explanation="Git liest die vorgemerkten Inhalte, wenn es den Commit erstellt."}
::option[Hi, weil das der neueste Text in der Datei ist.]{#git-commits-staged-snapshot-a explanation="Die neueste Arbeitskopie kann von der vorgemerkten Fassung abweichen."}
::option[Beide, weil Git jede Änderung automatisch speichert.]{#git-commits-staged-snapshot-b explanation="Der vorgemerkte Stand enthält genau eine ausgewählte Fassung dieser Datei."}
:::

## Den Verlauf in Kurzform lesen

Mit `git log --oneline` siehst du den Verlauf in Kurzform. Jede Zeile beginnt mit einer abgekürzten Commit-ID. Danach folgt die Nachricht. Deine ID wird sich von der im Beispiel unterscheiden.

```text
$ git log --oneline
a12c345 Set the homepage heading
```

Referenziere einen Commit über seine ID, denn mehrere Commits können dieselbe Nachricht haben. Die Anzeige beginnt normalerweise mit dem neuesten Commit auf dem aktuellen Branch.

:::single-choice{#git-commits-identify-snapshot} Zwei Commits haben die Nachricht Set the homepage heading. Wie kannst du ihre Stände unterscheiden?

::option[Anhand der gemeinsamen Commit-Nachricht.]{#git-commits-identify-snapshot-a explanation="Derselbe Text kann bei mehreren Commits vorkommen."}
::option[Anhand des Dateinamens, der in beiden Commits vorkommt.]{#git-commits-identify-snapshot-c explanation="Dieselbe Datei kann Bestandteil vieler Commits sein."}
::option[Anhand der Commit-ID.]{#git-commits-identify-snapshot-b .correct explanation="Mit der ID kannst du einen bestimmten Eintrag eindeutig angeben."}
:::

Zum Vormerken und Erstellen von Commits im Browser-Terminal kannst du [Dein erstes Git-Lab](https://labex.io/tutorials/git-your-first-git-lab-92739) ausprobieren.

## Zusammenfassung

Du kannst jetzt vorgemerkte Arbeit speichern und im Verlauf wiederfinden.

1. Die Autorenangaben für ein Übungsrepository festlegen.
2. Den ausgewählten Stand mit einer aussagekräftigen Nachricht speichern.
3. Einen Commit in der Kurzansicht des Verlaufs erkennen.
