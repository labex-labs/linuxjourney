---
lesson_id: "git-diff-command"
course_id: "git"
lang: "de"
order_index: 3
title: "git diff"
description: "Lerne, mit git diff die Arbeitskopie einer Datei mit ihrer vorgemerkten Fassung zu vergleichen."
meta_title: "git diff – Git"
meta_description: "Lies geänderte Zeilen mit git diff und prüfe vorgemerkte Änderungen, bevor du sie mit einem Commit speicherst."
meta_keywords: "git diff, Arbeitsbaum, Staging-Bereich, Diff, DevOps, Linux Journey"
---

Der Status zeigt, welche Dateien sich geändert haben. Mit `git diff` siehst du, welche Zeilen sich geändert haben. In diesem Beispiel ist aus der vorherigen Lektion schon eine Fassung von `index.html` mit der Überschrift Hello vorgemerkt.

## Eine Arbeitsdatei mit ihrer vorgemerkten Fassung vergleichen

Ersetze die Überschrift in der Übungsdatei und vergleiche die Arbeitskopie mit der vorgemerkten Fassung.

```bash
$ printf '%s\n' '<h1>Welcome</h1>' > index.html
$ git diff -- index.html
```

`--` trennt die Optionen von dem Pfad, den du prüfen möchtest. In der Ausgabe stammt die Zeile mit `-` aus der früheren Fassung. Die Zeile mit `+` zeigt die Änderung. Die folgenden Zeilen aus dem Diff beschreiben genau diese Ersetzung.

```diff
-<h1>Hello</h1>
+<h1>Welcome</h1>
```

:::single-choice{#git-diff-command-changed-heading} Welche Überschrift steht gerade in der Arbeitskopie?

::option[Welcome.]{#git-diff-command-changed-heading-b .correct explanation="Die Zeile mit dem Pluszeichen zeigt hier den neuen Text im Arbeitsbaum."}
::option[Hello.]{#git-diff-command-changed-heading-a explanation="Die Zeile mit dem Minuszeichen zeigt die frühere vorgemerkte Fassung."}
::option[Beide Überschriften.]{#git-diff-command-changed-heading-c explanation="Die beiden Zeilen zeigen denselben Text vor und nach der Änderung."}
:::

## Den Staging-Bereich mit dem Verlauf vergleichen

Mit `git diff --staged -- index.html` vergleichst du die vorgemerkte Fassung mit dem letzten Commit. Vor dem ersten Commit geht Git von einem leeren Ausgangsstand aus. Die Ausgabe zeigt dann die vorgemerkte Überschrift Hello als hinzugefügt. Gleichzeitig zeigt `git diff` ohne weitere Optionen die spätere Änderung in Welcome.

```bash
$ git diff --staged -- index.html
```

:::single-choice{#git-diff-command-preview-commit} Welcher Befehl zeigt als Vorschau, welche Änderung jetzt in den Commit eingehen würde?

::option[git diff -- index.html]{#git-diff-command-preview-commit-b explanation="Das vergleicht die Arbeitskopie mit der vorgemerkten Fassung."}
::option[git status --short]{#git-diff-command-preview-commit-c explanation="Die Statusanzeige zeigt, wo es Änderungen gibt. Sie listet die geänderten Zeilen nicht auf."}
::option[git diff --staged -- index.html]{#git-diff-command-preview-commit-a .correct explanation="Der Befehl vergleicht den ausgewählten Inhalt mit dem vorherigen Stand."}
:::

![LabEx-Terminal mit dem Vergleich zwischen der Arbeitskopie mit Welcome und der vorgemerkten Fassung mit Hello](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/git/git-diff-command/working-and-staged.png)

## Eine leere Diff-Ausgabe verstehen

Füge die aktuelle Datei erneut hinzu, um die vorgemerkte Fassung zu aktualisieren.

```bash
$ git add index.html
$ git diff -- index.html
```

`git diff` ohne Optionen kann jetzt leer bleiben, weil Arbeitskopie und vorgemerkte Fassung übereinstimmen. Der Vergleich mit dem Staging-Bereich zeigt weiterhin, welche Änderung noch auf einen Commit wartet. Unversionierte Dateien erscheinen in diesen Dateivergleichen nicht. Wenn du den Stand einer Änderung nicht kennst, prüfe zuerst den Status.

:::single-choice{#git-diff-command-empty-diff} Direkt nach dem Vormerken zeigt git diff nichts an. Wo kannst du die Änderung gegenüber dem Verlauf noch sehen?

::option[In einem zweiten Aufruf von git diff ohne weitere Optionen.]{#git-diff-command-empty-diff-a explanation="Ein erneuter Aufruf vergleicht in diesem Fall dieselben identischen Fassungen."}
::option[In git diff --staged.]{#git-diff-command-empty-diff-c .correct explanation="Das vergleicht die vorgemerkte Fassung mit dem bisherigen Stand im Verlauf."}
::option[Erst nachdem du einen Commit erstellt hast.]{#git-diff-command-empty-diff-b explanation="Du kannst den geplanten Commit prüfen, bevor du ihn speicherst."}
:::

## Zusammenfassung

Du kannst jetzt den Diff auswählen, der deine Frage beantwortet.

1. Entfernte und hinzugefügte Zeilen lesen.
2. Die Arbeitskopie mit der vorgemerkten Fassung vergleichen.
3. Vorgemerkte Änderungen vor einem Commit anzeigen.
