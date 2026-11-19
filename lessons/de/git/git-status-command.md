---
lesson_id: "git-status-command"
course_id: "git"
lang: "de"
order_index: 2
title: "git status"
description: "Lerne, mit git status unversionierte, vorgemerkte und geänderte Dateien zu erkennen."
meta_title: "git status – Git"
meta_description: "Prüfe mit git status, was sich im Arbeitsbaum geändert hat und welche Änderungen für den nächsten Commit vorgemerkt sind."
meta_keywords: "git status, Git-Status, Staging-Bereich, unversionierte Dateien, DevOps, Linux Journey"
---

Im Repository zeigt `git status`, was Git im Arbeitsbaum sieht und welche Änderungen du für den nächsten Commit ausgewählt hast. Verwende das leere Repository `journey-git` aus der vorherigen Lektion.

## Eine neue Datei finden

Erstelle eine kleine Seite. Verwende danach das Kurzformat, damit die Ausgabe übersichtlich bleibt.

```bash
$ printf '%s\n' '<h1>Hello</h1>' > index.html
$ git status --short
```

Das Zeichen `>` schreibt in die angegebene Datei und ersetzt ihren Inhalt, falls sie schon existiert. Für die neue Datei zeigt das Kurzformat `?? index.html`. Git bezeichnet sie als **unversioniert**. Sie liegt im Arbeitsbaum, ist aber noch nicht für einen gespeicherten Stand ausgewählt.

:::single-choice{#git-status-command-untracked-file} Git zeigt zwei Fragezeichen neben einer neuen Datei. Was bedeutet das?

::option[Die Datei gehört zum zuletzt gespeicherten Stand.]{#git-status-command-untracked-file-a explanation="Eine unversionierte Datei hat dort keinen Eintrag."}
::option[Die Datei wurde aus dem Arbeitsbaum entfernt.]{#git-status-command-untracked-file-c explanation="Git sieht die Datei in deinem Arbeitsbaum."}
::option[Die Datei existiert und ist bisher nicht für den nächsten Stand ausgewählt.]{#git-status-command-untracked-file-b .correct explanation="Du kannst die Datei zum Staging-Bereich hinzufügen."}
:::

![Die Git-Kurzansicht zeigt, wie index.html von unversioniert zu vorgemerkt wechselt](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/git/git-status-command/staged-file.png)

## Vorgemerkte Änderungen ansehen

Mit `git add` wählst du den aktuellen Inhalt der Datei für den nächsten gespeicherten Stand aus. Ein solcher Stand heißt **Commit**. Die Auswahl liegt im **Staging-Bereich**. In der ersten Spalte der Kurzansicht steht nun ein `A` für die zum Speichern vorgemerkte neue Datei.

```bash
$ git add index.html
$ git status --short
```

:::single-choice{#git-status-command-staged-new} Wo liegt die ausgewählte Fassung von index.html nach git add?

::option[Schon in einem neuen Commit.]{#git-status-command-staged-new-a explanation="Git add bereitet den nächsten Commit vor. Ein Commit wird dabei noch nicht erstellt."}
::option[Im Staging-Bereich.]{#git-status-command-staged-new-c .correct explanation="Git hat den Inhalt ausgewählt, der beim Aufruf von git add in der Datei stand."}
::option[Im Repository einer anderen Person.]{#git-status-command-staged-new-b explanation="Die Änderung betrifft nur deinen lokalen Staging-Bereich."}
:::

## Zwei Arten von Änderungen prüfen

Im Kurzformat stehen zwei Spalten vor dem Dateinamen. Die erste zeigt vorgemerkte Änderungen. Die zweite zeigt Änderungen im Arbeitsbaum nach dem Vormerken. `AM index.html` bedeutet zum Beispiel, dass Git eine neue Datei vorgemerkt hat und du die Arbeitskopie danach geändert hast. Wenn dir Überschriften lieber sind, zeigt `git status` die Details in Gruppen.

:::single-choice{#git-status-command-two-columns} Neben index.html steht AM. Was solltest du vor dem nächsten Commit überprüfen?

::option[Ob die vorgemerkte Fassung die Änderung enthält, die du speichern willst.]{#git-status-command-two-columns-a .correct explanation="Das M in der zweiten Spalte zeigt eine spätere Änderung in deiner Arbeitskopie."}
::option[Ob das Repository noch eine andere Datei namens AM enthält.]{#git-status-command-two-columns-b explanation="AM besteht aus zwei Statuszeichen für index.html."}
::option[Ob die Datei gelöscht wurde.]{#git-status-command-two-columns-c explanation="M steht für eine Änderung im Arbeitsbaum."}
:::

## Zusammenfassung

Du kannst jetzt prüfen, welche Änderungen Git beim nächsten Commit speichern würde.

1. Eine neue unversionierte Datei erkennen.
2. Eine Datei mit git add für den nächsten Commit vormerken.
3. Vorgemerkte Änderungen und Änderungen im Arbeitsbaum separat lesen.
