---
lesson_id: "emacs-buffer-navigation"
course_id: "advanced-text-fu"
lang: "de"
order_index: 11
title: "In Emacs durch Puffer navigieren"
description: "Lerne, Emacs-Puffer zu wechseln und zu beenden sowie Anzeigefenster zu teilen, auszuwählen und zu schließen."
meta_title: "In Emacs durch Puffer navigieren – Fortgeschrittenes Text-Fu"
meta_description: "Lerne die Navigation durch Emacs-Puffer: Wechsle Puffer, teile Fenster und verwalte deinen Arbeitsbereich mit wichtigen Emacs-Befehlen."
meta_keywords: "emacs navigation, emacs puffer wechseln, emacs pufferverwaltung, emacs befehle, C-x b, C-x k, C-x 2, texteditor, linux"
---

Ein Emacs-Puffer enthält Text oder einen Editorzustand, während ein Fenster einen Puffer anzeigt. Ein Puffer kann existieren, ohne sichtbar zu sein, und mehrere Fenster können denselben Puffer anzeigen. Die Verwaltung des einen Objekts verwaltet nicht automatisch auch das andere.

## Puffer wechseln

Verwende `C-x b`, das `switch-to-buffer` ausführt, um im aktuellen Fenster einen Puffer anhand seines Namens auszuwählen:

```text
C-x b
```

Der Minipuffer bietet eine Vervollständigung für vorhandene Namen. Die Eingabe eines neuen Namens kann einen Puffer ohne zugehörige Datei anlegen; dadurch wird kein Dateipfad besucht.

Standardmäßig führt `C-x Right` den Befehl `next-buffer` und `C-x Left` den Befehl `previous-buffer` aus. Damit wechselst du im ausgewählten Fenster der Reihe nach durch die Puffer.

:::single-choice{#emacs-switch-buffer-key} Welche Tastenfolge fragt nach einem Puffernamen, der im aktuellen Fenster angezeigt werden soll?

::option[`C-x C-f`]{#emacs-buffer-find-file explanation="Diese Tastenfolge fragt nach einem Dateipfad und besucht ihn. Das ist etwas anderes als die Auswahl eines vorhandenen Puffers anhand seines Namens."}
::option[`C-x b`]{#emacs-switch-buffer .correct explanation="`switch-to-buffer` liest einen Puffernamen ein und zeigt diesen Puffer im ausgewählten Fenster an."}
::option[`C-x k`]{#emacs-buffer-kill explanation="Diese Tastenfolge fragt nach einem zu beendenden Puffer, statt das ausgewählte Fenster zu einem Puffer wechseln zu lassen."}
:::

## Das ausgewählte Fenster teilen

Teile das ausgewählte Fenster mit `C-x 2` in ein oberes und ein unteres Fenster:

```text
C-x 2
```

Mit `C-x 3` teilst du es in ein linkes und ein rechtes Fenster:

```text
C-x 3
```

Das neue Fenster zeigt zunächst einen Puffer an, häufig denselben. In beiden Fenstern kannst du die Puffer unabhängig voneinander wechseln.

:::single-choice{#emacs-split-side-by-side} Welche Tastenfolge teilt das ausgewählte Emacs-Fenster in ein linkes und ein rechtes Fenster?

::option[`C-x 1`]{#emacs-window-one explanation="Diese Tastenfolge löscht die anderen Fenster und macht das ausgewählte Fenster zum einzigen Fenster seines Frames."}
::option[`C-x 2`]{#emacs-window-below explanation="Diese Tastenfolge erzeugt ein oberes und ein unteres Fenster, keine nebeneinanderliegenden Fenster."}
::option[`C-x 3`]{#emacs-window-right .correct explanation="`split-window-right`, das an `C-x 3` gebunden ist, erzeugt ein linkes und ein rechtes Fenster."}
:::

## Fenster auswählen und schließen

Verwende `C-x o`, das `other-window` ausführt, um das nächste Fenster auszuwählen:

```text
C-x o
```

Mit diesen Befehlen entfernst du Fensteranzeigen:

- `C-x 0`: Das ausgewählte Fenster löschen.
- `C-x 1`: Die anderen Fenster im aktuellen Frame löschen.

Beim Löschen eines Fensters bleibt der darin angezeigte Puffer normalerweise erhalten. Du kannst diesen Puffer später wieder in einem anderen Fenster anzeigen.

:::single-choice{#emacs-select-other-window} Welche Tastenfolge verschiebt den Eingabepunkt und den Tastaturfokus in ein anderes Emacs-Fenster?

::option[`C-x 0`]{#emacs-delete-selected-window explanation="Diese Tastenfolge löscht das ausgewählte Fenster, statt den Fokus in ein anderes zu verschieben."}
::option[`C-x o`]{#emacs-other-window .correct explanation="`other-window` wählt der Reihe nach ein anderes Fenster im Frame aus."}
::option[`C-x b`]{#emacs-switch-in-window explanation="Diese Tastenfolge ändert den im aktuellen Fenster angezeigten Puffer, nicht das ausgewählte Fenster."}
:::

:::single-choice{#emacs-keep-one-window} Welche Tastenfolge behält das ausgewählte Fenster und löscht die anderen Fenster seines Frames?

::option[`C-x 1`]{#emacs-delete-other-windows .correct explanation="`delete-other-windows` macht das ausgewählte Fenster zum einzigen Fenster des Frames."}
::option[`C-x 0`]{#emacs-delete-current-window explanation="Diese Tastenfolge löscht das ausgewählte Fenster selbst, statt es beizubehalten."}
::option[`C-x 2`]{#emacs-add-lower-window explanation="Diese Tastenfolge fügt ein weiteres Fenster hinzu, statt den Frame auf eines zu reduzieren."}
:::

## Einen Puffer beenden

Verwende `C-x k`, das `kill-buffer` ausführt, um nach einem Puffer zu fragen, der aus Emacs entfernt werden soll:

```text
C-x k
```

Der aktuelle Puffer ist die Standardauswahl. Hat ein dateibesuchender Puffer ungespeicherte Änderungen, warnt Emacs vor dem Beenden. Lies die Frage sorgfältig, denn das Beenden eines geänderten Puffers kann Änderungen verwerfen.

Das Beenden eines Puffers unterscheidet sich vom Löschen eines Fensters. Emacs ersetzt einen beendeten Puffer in jedem Fenster, das ihn angezeigt hat. Das Löschen eines Fensters kann seinen Puffer dagegen unberührt lassen.

:::single-choice{#emacs-kill-buffer-key} Welche Tastenfolge fragt nach einem Emacs-Puffer, der beendet werden soll?

::option[`C-x 0`]{#emacs-kill-window-only explanation="Diese Tastenfolge löscht eine Fensteranzeige, lässt den Puffer aber normalerweise bestehen."}
::option[`C-x k`]{#emacs-kill-buffer-answer .correct explanation="`kill-buffer` entfernt den ausgewählten Puffer aus Emacs, nachdem gegebenenfalls die Bestätigung für einen geänderten Puffer erfolgt ist."}
::option[`C-x b`]{#emacs-kill-switch explanation="Diese Tastenfolge lässt das aktuelle Fenster zu einem benannten Puffer wechseln und beendet ihn nicht."}
:::

Übe diese Befehle mit `*scratch*` und entbehrlichen Puffern. Prüfe vor dem Beenden eines dateibesuchenden Puffers, ob seine Änderungsmarkierung auf ungespeicherte Arbeit hinweist.

## Zusammenfassung

Du kannst nun verwalten, was Emacs speichert und was jedes Fenster anzeigt.

1. Wechsle mit `C-x b` im ausgewählten Fenster den Puffer.
2. Teile das Fenster mit `C-x 2` nach unten oder mit `C-x 3` nach rechts.
3. Wähle mit `C-x o` ein anderes Fenster aus.
4. Entferne Fensteranzeigen mit `C-x 0` oder `C-x 1`.
5. Beende einen Puffer erst nach Prüfung ungespeicherter Änderungen mit `C-x k`.
