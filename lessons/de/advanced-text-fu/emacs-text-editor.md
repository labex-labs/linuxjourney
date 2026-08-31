---
lesson_id: "emacs-text-editor"
course_id: "advanced-text-fu"
lang: "de"
order_index: 9
title: "Emacs"
description: "Lerne, wie du Emacs startest, seine Tastennotation liest und Puffer, Fenster und Frames voneinander unterscheidest."
meta_title: "Emacs – Fortgeschrittenes Text-Fu"
meta_description: "Lerne Emacs als leistungsfähigen und erweiterbaren Texteditor für Linux kennen. Verstehe Emacs-Puffer, Fenster, Frames und die grundlegende Bedienung."
meta_keywords: "Emacs, Linux Texteditor, Emacs Tutorial, Emacs Puffer, Linux Befehle, Anfänger, Anleitung"
---

GNU Emacs ist ein erweiterbarer Texteditor, dessen Verhalten sich mit Emacs Lisp anpassen lässt. Er unterstützt die Bearbeitung reiner Textdateien, Programmiermodi, die Verwaltung von Dateien und Puffern sowie zahlreiche optionale Pakete. Du kannst seine grundlegenden Bearbeitungsbefehle erlernen, ohne jede Erweiterung zu übernehmen.

## Emacs prüfen und starten

Gehe nicht davon aus, dass Emacs installiert ist. Prüfe zunächst, wie die Shell den Befehl auflöst:

```bash
$ command -v emacs
/usr/bin/emacs
```

Starte Emacs mit der normalen Auswahl der Anzeige:

```bash
$ emacs
```

In einer grafischen Sitzung kann dadurch ein grafischer Frame entstehen. Verwende `-nw` für „no window system“, wenn Emacs im aktuellen Terminal bleiben soll:

```bash
$ emacs -nw
```

:::single-choice{#emacs-terminal-start}
Welcher Befehl startet Emacs im aktuellen Terminal, anstatt ein grafisches Fenstersystem zu verwenden?

::option[`emacs -w`]{#emacs-window-option explanation="Dies ist nicht die hier vorgestellte dokumentierte Form für den Betrieb ohne Fenstersystem."}
::option[`emacs -nw`]{#emacs-no-window .correct explanation="Die Option `-nw` weist Emacs an, kein grafisches Fenstersystem zu verwenden und im Terminal zu laufen."}
::option[`command -v emacs`]{#emacs-check-only explanation="Dieser Befehl prüft lediglich die Befehlsauflösung und startet den Editor nicht."}
:::

## Eine Datei öffnen

Übergib beim Start einen Pfad, um eine Datei zu besuchen:

```bash
$ emacs notes.txt
```

Existiert die Datei, liest Emacs sie in einen Puffer ein. Fehlt sie, erstellt Emacs einen neuen Puffer, der diesem Pfad zugeordnet ist. Die eigentliche Datei entsteht erst nach erfolgreichem Speichern. Ob das Schreiben gelingt, hängt weiterhin von den Dateisystemberechtigungen ab.

:::single-choice{#emacs-open-file-buffer}
Was bewirkt `emacs notes.txt` normalerweise, wenn `notes.txt` noch nicht existiert?

::option[Es öffnet einen neuen Puffer, der diesem Pfad zugeordnet ist.]{#emacs-new-file-buffer .correct explanation="Der Puffer kann neuen Text für `notes.txt` aufnehmen; die eigentliche Datei wird erst beim Speichern angelegt."}
::option[Es legt die Datei auf dem Datenträger an, bevor der Editor startet.]{#emacs-immediate-file explanation="Emacs kann einen neuen Puffer mit dem Pfad verknüpfen, ohne die Datei vor einem erfolgreichen Speichervorgang anzulegen."}
::option[Es verweigert den Start, weil jede besuchte Datei bereits existieren muss.]{#emacs-refuse-new-file explanation="Emacs unterstützt das Erstellen neuer Dateien über Puffer, die fehlenden Pfaden zugeordnet sind."}
:::

## Puffer, Fenster und Frames verstehen

Emacs verwendet miteinander verbundene, aber unterschiedliche Objekte:

- Ein **Puffer** enthält Text oder einen anderen Editorzustand. Der Inhalt einer besuchten Datei liegt in einem Puffer.
- Ein **Fenster** ist ein Bereich innerhalb eines Emacs-Frames, der einen Puffer anzeigt.
- Ein **Frame** ist eine eigenständige Emacs-Anzeige, beispielsweise ein grafischer oder ein Terminal-Frame.

Mehrere Puffer können vorhanden sein, ohne sichtbar zu sein, und zwei Fenster können denselben Puffer anzeigen. Das Schließen eines Fensters beendet nicht zwangsläufig seinen Puffer und löscht keine Datei.

:::single-choice{#emacs-buffer-definition}
Was ist ein Emacs-Puffer?

::option[Ein eigenständiger grafischer Anwendungs-Frame.]{#emacs-buffer-frame explanation="Ein Frame ist das übergeordnete Anzeigeobjekt; ein Puffer enthält Editorinhalt oder -zustand."}
::option[Ein Objekt, das bearbeitbaren Text oder einen anderen Editorzustand enthält.]{#emacs-buffer-content .correct explanation="Die Inhalte besuchter Dateien und viele Ansichten ohne zugehörige Datei befinden sich in Emacs-Puffern."}
::option[Eine Shell-Verlaufsdatei mit früheren Befehlen.]{#emacs-buffer-history explanation="Der Shell-Verlauf ist vom Speicher der Emacs-Puffer getrennt."}
:::

## Emacs-Tastennotation lesen

Die Emacs-Dokumentation verwendet eine kompakte Schreibweise:

- `C-x` bedeutet: Halte Strg gedrückt und drücke `x`.
- `M-x` bedeutet: Halte Meta gedrückt und drücke `x`; auf modernen Terminals und Desktops übernimmt häufig Alt die Meta-Funktion.
- `C-x C-f` ist eine Tastenfolge: Drücke Strg+x und danach Strg+f.

Je nach Terminal können manche Tasten abgefangen oder anders zugeordnet werden. Häufig kann `Esc` gefolgt von einer Taste einen Meta-Tastenakkord ersetzen.

:::single-choice{#emacs-key-sequence-notation}
Wie gibst du die Emacs-Tastenfolge `C-x C-f` ein?

::option[Halte für `x` Strg gedrückt und anschließend erneut für `f`.]{#emacs-control-x-f .correct explanation="Jedes Präfix `C-` gilt für die jeweils folgende Taste; die beiden Tastenkombinationen werden nacheinander eingegeben."}
::option[Tippe die wörtlichen Zeichen `C-x C-f` in den Puffer.]{#emacs-literal-key-text explanation="Die Notation beschreibt Ereignisse mit der Steuerungstaste und keinen einzufügenden Text."}
::option[Halte Strg, `x` und `f` gleichzeitig als eine einzige Kombination gedrückt.]{#emacs-simultaneous-x-f explanation="Die Notation enthält zwei aufeinanderfolgende Tastenkombinationen und keine einzelne Kombination aus drei Tasten."}
:::

## Das integrierte Tutorial starten

Gib in Emacs `C-h t` ein, um das interaktive Tutorial zu öffnen. Es vermittelt Bewegung, Texteingabe, Speichern und Beenden in einem sicheren Übungspuffer. `C-h` ist das Hilfepräfix; `C-h C-h` zeigt Hilfe zur Verwendung der Hilfe an.

Falls Emacs ein Menü oder einen Willkommenspuffer anzeigt, ist das Tutorial ein besser strukturierter Einstieg als das Experimentieren mit einer wichtigen Datei.

:::single-choice{#emacs-open-tutorial}
Welche Emacs-Tastenfolge öffnet das integrierte Tutorial?

::option[`C-x C-s`]{#emacs-save-buffer explanation="Diese Tastenfolge speichert den aktuellen Puffer; sie öffnet nicht das Tutorial."}
::option[`C-x C-c`]{#emacs-exit-sequence explanation="Diese Tastenfolge leitet das Beenden von Emacs ein, statt eine Lektion zu starten."}
::option[`C-h t`]{#emacs-help-tutorial .correct explanation="Das Hilfepräfix `C-h` gefolgt von `t` startet das Emacs-Tutorial."}
:::

## Zusammenfassung

Du kannst Emacs nun starten und seine grundlegenden Oberflächenkonzepte einordnen.

1. Prüfe, ob der Befehl `emacs` verfügbar ist.
2. Wähle mit `-nw` zwischen grafischem Betrieb und Terminalbetrieb.
3. Besuche einen vorhandenen oder neuen Pfad in einem Puffer.
4. Unterscheide Puffer, Fenster und Frames.
5. Lies die Tastennotation und öffne das integrierte Tutorial.
