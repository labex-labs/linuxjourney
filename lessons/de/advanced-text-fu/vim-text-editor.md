---
lesson_id: "vim-text-editor"
course_id: "advanced-text-fu"
lang: "de"
order_index: 3
title: "Vim (Vi Improved)"
description: "Lerne, was Vim ist, wie es mit vi zusammenhängt und wie du Dateien, Hilfe und angeleitete Übungen öffnest."
meta_title: "Vim (Vi Improved) - Fortgeschrittene Text-Fu"
meta_description: "Entdecken Sie Vim, den leistungsstarken und leichten Texteditor, bekannt als vi improved. Diese Lektion stellt die Grundlagen von Vim vi improved vor, einem Tool, das auf den meisten Linux-Systemen vorinstalliert ist."
meta_keywords: "Vim, vi improved, vim vi improved, Linux Texteditor, Vim Tutorial, Vi Editor, vim improved, Linux Befehle"
---

Vim ist ein konfigurierbarer Texteditor, dessen Name für **Vi Improved** steht. Er bewahrt das modale Bearbeitungsmodell des ursprünglichen Editors `vi` und ergänzt Funktionen wie mehrstufiges Rückgängigmachen, Syntaxunterstützung, Skripting und ein umfangreiches Hilfesystem.

## Vim und vi einordnen

`vi` bezeichnet sowohl einen historischen Editor als auch eine verbreitete Befehlsschnittstelle. Auf einem Linux-System kann `vi` Vim in einem kompatibilitätsorientierten Modus starten, auf einem anderen eine andere vi-Implementierung. Gehe deshalb nicht davon aus, dass jeder `vi`-Befehl alle Vim-Funktionen bereitstellt.

Prüfe die Auflösung in der aktuellen Shell:

```bash
$ command -v vim
/usr/bin/vim
$ command -v vi
/usr/bin/vi
```

An den aufgelösten Pfaden allein erkennst du nicht, ob `vi` und `vim` dieselbe Implementierung sind. `type -a vi vim` und die Versionsausgabe der Editoren liefern weitere Hinweise.

:::single-choice{#vim-name-origin} Wofür steht der Name Vim?

::option[Visual Input Manager]{#vim-visual-input explanation="Diese Auflösung ist nicht der Ursprung des Editornamens."}
::option[Virtual Interface Mode]{#vim-virtual-interface explanation="Vim verwendet zwar Modi, doch für diesen Ausdruck steht sein Name nicht."}
::option[Vi Improved]{#vim-vi-improved .correct explanation="Vim begann als verbesserter vi-kompatibler Editor; diese Herkunft spiegelt sich in seinem Namen wider."}
:::

:::single-choice{#vim-check-command} Welcher Befehl prüft, ob Bash den Namen `vim` derzeit auflösen kann?

::option[`vim --create`]{#vim-create-option explanation="Dies ist keine Prüfung der Shell-Auflösung und auch kein Verfahren zum Installieren oder Auffinden von Vim."}
::option[`command -v vim`]{#vim-command-resolution .correct explanation="Das Shell-Builtin meldet den für den Namen verwendeten Befehl, sofern einer verfügbar ist."}
::option[`file ~/.vimrc`]{#vim-file-vimrc explanation="Dieser Befehl untersucht eine mögliche Konfigurationsdatei, sagt aber nichts Verlässliches über die Verfügbarkeit der Vim-Programmdatei aus."}
:::

## Vim und Dateien öffnen

Starte Vim mit einem unbenannten Puffer:

```bash
$ vim
```

Übergib einen Pfad, um diese Datei zu bearbeiten:

```bash
$ vim filename.txt
```

Existiert `filename.txt` und ist lesbar, lädt Vim ihren Inhalt in einen Puffer. Existiert der Pfad nicht, öffnet Vim einen neuen Puffer, der mit diesem Namen verknüpft ist; eine Datei entsteht erst nach einem erfolgreichen Schreibvorgang.

Vim umgeht keine Dateisystemberechtigungen. Eine Datei öffnen zu können bedeutet nicht automatisch, dass dein Konto Änderungen unter ihrem Pfad speichern darf.

:::single-choice{#vim-open-missing-path} Was geschieht normalerweise, wenn `vim draft.txt` einen noch nicht vorhandenen Pfad bezeichnet?

::option[Vim öffnet einen neuen Puffer und erstellt die Datei erst beim Schreiben.]{#vim-new-buffer .correct explanation="Der Pfad wird für den Puffer vorgemerkt; die Datei auf dem Datenträger entsteht erst durch einen erfolgreichen Speichervorgang."}
::option[Vim erstellt sofort eine leere Datei auf dem Datenträger und öffnet danach die Oberfläche.]{#vim-immediate-create explanation="Der neue Puffer wird mit dem Pfad verknüpft, doch die Datei wird erst beim erfolgreichen Schreiben erstellt."}
::option[Vim verweigert den Start, weil jeder Pfad bereits existieren muss.]{#vim-refuse-missing explanation="Vim kann für einen fehlenden Pfad einen neuen Puffer öffnen, damit du eine neue Datei verfassen kannst."}
:::

## Integrierte Lernressourcen verwenden

Enthält die Vim-Installation `vimtutor`, startest du damit in der Shell eine interaktive Übungslektion:

```bash
$ vimtutor
```

Wechsle innerhalb von Vim mit `Esc` in den Normalmodus, gib `:help` ein und drücke Enter, um das Hilfesystem zu öffnen. Ein bestimmtes Thema kann hinter dem Befehl stehen:

```vim
:help user-manual
:help :write
```

Hilfetags sind genau, weshalb auch Satzzeichen eine Rolle spielen können. Mit `Ctrl+]` folgst du einem Hilfelink, mit `Ctrl+T` kehrst du zurück.

:::single-choice{#vim-guided-tutorial} Welcher Shell-Befehl startet Vims angeleitetes Tutorial, sofern es installiert ist?

::option[`vim --quiz`]{#vim-quiz-option explanation="Vim verwendet diese Option nicht als Standardschnittstelle für sein angeleitetes Tutorial."}
::option[`vimtutor`]{#vim-tutor-command .correct explanation="`vimtutor` öffnet eine Kopie des interaktiven Tutorials für sichere praktische Übungen."}
::option[`help vim`]{#vim-shell-help explanation="Bash `help` dokumentiert Shell-Builtins und startet nicht das interaktive Vim-Tutorial."}
:::

## Mit einer entbehrlichen Datei üben

Beginne mit einer Datei in einem Verzeichnis, das dir gehört:

```bash
$ printf 'alpha\nbeta\n' > vim-practice.txt
$ vim vim-practice.txt
```

Die folgenden Lektionen führen Suche, Navigation, Einfügen, Bearbeiten und Speichern ein. Bis du sicher beenden kannst, merke dir: `Esc` führt in den Normalmodus zurück; `:q!` gefolgt von Enter verwirft ungespeicherte Änderungen im aktuellen Fenster. Verwende den Befehl nur, wenn du diese Änderungen bewusst aufgeben möchtest.

:::single-choice{#vim-abandon-practice-changes} Welcher Vim-Befehl beendet bei einer entbehrlichen Übungsdatei das aktuelle Fenster und verwirft ungespeicherte Änderungen?

::option[`:w`]{#vim-write-only explanation="`:w` schreibt den Puffer, beendet aber nicht das aktuelle Fenster."}
::option[`:wq`]{#vim-write-quit explanation="`:wq` speichert Änderungen vor dem Beenden und verwirft sie daher nicht."}
::option[`:q!`]{#vim-quit-force .correct explanation="Das `!` weist Vim an, die Warnung vor einem veränderten Puffer zu übergehen und ohne Schreiben zu beenden."}
:::

Mit dieser Übung kannst du das Öffnen, Bearbeiten und Speichern mit Vim praktisch trainieren:

1. **[Textdateien in Linux mit Vim und Nano bearbeiten](https://labex.io/de/labs/comptia-edit-text-files-in-linux-with-vim-and-nano-591076)** – Übe in einer echten Linux-Umgebung das Erstellen, Bearbeiten, Speichern und Navigieren mit Vim und Nano.

## Zusammenfassung

Du kannst Vim nun einordnen, einen Puffer öffnen und sichere Lernressourcen finden.

1. Erkläre Vims Verhältnis zu vi, ohne eine bestimmte Implementierung anzunehmen.
2. Prüfe, ob der Befehl `vim` verfügbar ist.
3. Öffne eine vorhandene Datei oder einen neuen benannten Puffer.
4. Starte `vimtutor` oder öffne Vims integrierte Hilfe.
5. Verwirf ungespeicherte Übungsänderungen nur bewusst.
