---
lesson_id: "emacs-exiting-and-help"
course_id: "advanced-text-fu"
lang: "de"
order_index: 13
title: "Emacs beenden und Hilfe verwenden"
description: "Lerne, Emacs sicher zu beenden, ausstehende Befehle abzubrechen, Hilfethemen nachzuschlagen und Änderungen rückgängig zu machen."
meta_title: "Emacs beenden und Hilfe verwenden – Fortgeschrittenes Text-Fu"
meta_description: "Lerne, Emacs sicher zu beenden, die integrierte Hilfe zu verwenden, Befehle abzubrechen und Änderungen rückgängig zu machen."
meta_keywords: "Emacs beenden, Emacs Hilfe, Emacs rückgängig, Emacs Tutorial, Linux Texteditor, Anfänger Anleitung"
---

Emacs bietet kontextbezogene Hilfe zu Tasten, Funktionen, Variablen und aktiven Modi. Beim Beenden schützt es außerdem geänderte dateibesuchende Puffer und gibt dir Gelegenheit, jeden Schreibvorgang zu bestätigen oder abzulehnen.

## Emacs beenden

Verwende `C-x C-c`, das `save-buffers-kill-terminal` ausführt, um das Schließen der Emacs-Sitzung oder Terminalverbindung anzufordern:

```text
C-x C-c
```

Emacs prüft die relevanten geänderten dateibesuchenden Puffer und fragt, ob sie gespeichert werden sollen. Lies jeden Puffernamen und antworte bewusst. Emacs kann auch nach aktiven Prozessen fragen. Brich das Beenden ab, wenn du deine Arbeit vor der Entscheidung noch prüfen musst.

Bei einem Arbeitsablauf mit `emacsclient` oder einem Emacs-Server kann sich das genaue Verhalten von Frames und Server unterscheiden. Fragen zu geänderten Puffern verdienen dennoch immer besondere Aufmerksamkeit.

:::single-choice{#emacs-exit-key} Welche Tastenfolge fordert das normale Beenden von Emacs an und prüft dabei geänderte Puffer?

::option[`C-x k`]{#emacs-exit-kill-buffer explanation="Diese Tastenfolge beendet einen ausgewählten Puffer und fordert nicht das Beenden der Emacs-Sitzung an."}
::option[`C-g`]{#emacs-exit-keyboard-quit explanation="Diese Taste bricht einen ausstehenden Befehl oder eine Frage ab, statt Emacs zu schließen."}
::option[`C-x C-c`]{#emacs-exit-save-buffers .correct explanation="Diese Tastenfolge führt den normalen Ablauf zum Speichern von Puffern und Beenden aus, einschließlich Fragen zu relevanter ungespeicherter Arbeit."}
:::

## Die Hilfeübersicht öffnen

Das Standardpräfix für Hilfe ist `C-h`. Verwende `C-h C-h`, das die Hilfe zur Hilfe ausführt, um Hinweise zu den verfügbaren Hilfebefehlen anzuzeigen:

```text
C-h C-h
```

Mit der zweiten Taste wählst du die benötigte Art von Hilfe.

:::single-choice{#emacs-help-for-help} Welche Tastenfolge erklärt die Verwendung des Emacs-Hilfesystems?

::option[`C-h C-h`]{#emacs-help-help .correct explanation="Das Hilfepräfix gefolgt von einem weiteren `C-h` öffnet Hilfe zur Hilfeübersicht selbst."}
::option[`C-x C-h`]{#emacs-help-prefix-list explanation="Dies ist nicht die hier vorgestellte Tastenfolge für Hilfe zur Hilfe."}
::option[`C-h t`]{#emacs-help-tutorial-other explanation="Diese Tastenfolge öffnet direkt das Tutorial, statt das umfassendere Hilfemenü zu erklären."}
:::

## Tasten und Editorzustand beschreiben

Nützliche Hilfebefehle sind:

- `C-h k KEY`: Beschreiben, welchen Befehl eine Tastenfolge ausführt.
- `C-h f FUNCTION`: Eine Emacs-Lisp-Funktion beschreiben.
- `C-h v VARIABLE`: Eine Emacs-Lisp-Variable beschreiben.
- `C-h m`: Die aktuellen Haupt- und Nebenmodi beschreiben.
- `C-h t`: Das interaktive Tutorial öffnen.

Gib beispielsweise `C-h k C-x C-s` ein, um die Dokumentation der Tastenbelegung für save-buffer anzuzeigen.

:::single-choice{#emacs-describe-key} Du möchtest wissen, was `C-x C-s` bewirkt. Welches Hilfepräfix gibst du vor dieser Tastenfolge ein?

::option[`C-h k`]{#emacs-describe-key-answer .correct explanation="`describe-key` wartet auf eine Tastenfolge und erklärt den daran gebundenen Befehl."}
::option[`C-h f`]{#emacs-describe-function explanation="Diese Tastenfolge fragt nach einem Funktionsnamen, statt eine Tastenfolge einzulesen und deren Bindung zu ermitteln."}
::option[`C-h v`]{#emacs-describe-variable explanation="Diese Tastenfolge fragt nach einem Variablennamen und untersucht keine Tastenbelegung."}
:::

## Einen ausstehenden Befehl abbrechen

Verwende `C-g`, das an `keyboard-quit` gebunden ist, wenn du in einer Frage, einer teilweise eingegebenen Tastenfolge, einer inkrementellen Suche oder einem anderen abzubrechenden Befehl feststeckst:

```text
C-g
```

Die Taste macht bereits erfolgte Änderungen am Puffer nicht rückgängig und beendet Emacs nicht. Sie stoppt die aktuelle Interaktion und gibt dir, soweit möglich, die Kontrolle über die gewöhnliche Bearbeitung zurück.

:::single-choice{#emacs-cancel-pending-command} Welche Taste bricht normalerweise die aktuelle Emacs-Frage oder einen ausstehenden Befehl ab?

::option[`C-x C-c`]{#emacs-cancel-exit explanation="Diese Tastenfolge leitet das Beenden von Emacs ein, statt nur die aktuelle Frage abzubrechen."}
::option[`C-y`]{#emacs-cancel-yank explanation="Diese Taste yankte Text aus dem Kill Ring und bricht keinen Befehl ab."}
::option[`C-g`]{#emacs-keyboard-quit-answer .correct explanation="`keyboard-quit` bricht die aktuelle Befehlsinteraktion ab und gibt die Kontrolle an Emacs zurück."}
:::

## Änderungen am Puffer rückgängig machen

Verwende in üblichen Emacs-Konfigurationen `C-/`, `C-_` oder `C-x u`, um den Rückgängig-Befehl auszuführen:

```text
C-/
```

Wiederholte Rückgängig-Befehle gehen schrittweise durch die letzten Änderungen am Puffer zurück. Eine reine Cursorbewegung ist normalerweise keine Pufferänderung. Emacs-Versionen und -Konfigurationen können `undo-redo` und weitergehende Verlaufswerkzeuge anbieten. Prüfe mit `C-h k` deine tatsächlichen Tastenbelegungen für Rückgängig und Wiederherstellen.

:::single-choice{#emacs-undo-change} Welche Tastenfolge ist eine Standardbelegung zum Rückgängigmachen einer kürzlich erfolgten Änderung am Emacs-Puffer?

::option[`C-/`]{#emacs-undo-control-slash .correct explanation="`C-/` ist eine Standardbelegung für Rückgängig; in üblichen Konfigurationen stehen daneben `C-_` und `C-x u` zur Verfügung."}
::option[`C-x C-s`]{#emacs-undo-save explanation="Diese Tastenfolge speichert den aktuellen Puffer, statt seinen Rückgängig-Verlauf zu durchlaufen."}
::option[`C-w`]{#emacs-undo-kill explanation="Diese Taste killt den aktiven Bereich und erzeugt eine weitere Änderung, statt eine rückgängig zu machen."}
:::

Übe, indem du `*scratch*` öffnest, eine entbehrliche Änderung vornimmst, sie rückgängig machst, mit `C-h k` nach einer unbekannten Taste fragst und eine Minipufferfrage mit `C-g` abbrichst, bevor du Emacs normal beendest.

## Zusammenfassung

Du kannst nun Hilfe erhalten und Emacs verlassen, ohne ungespeicherte Arbeit zu übergehen.

1. Beende Emacs mit `C-x C-c` und durchlaufe dabei die Prüfungen geänderter Puffer.
2. Öffne mit `C-h C-h` die Hilfe zur Hilfe.
3. Lass dir Tasten, Funktionen, Variablen oder aktive Modi beschreiben.
4. Brich einen ausstehenden Befehl mit `C-g` ab.
5. Mache letzte Pufferänderungen mit einer vor Ort geprüften Tastenbelegung rückgängig.
