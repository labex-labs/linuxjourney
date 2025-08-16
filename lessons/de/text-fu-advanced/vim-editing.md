---
title: "Vim-Bearbeitung"
description: "Lernen Sie die Grundlagen der Vim-Bearbeitung: Text effizient löschen, ändern, kopieren und einfügen. Meistern Sie wesentliche Vim-Befehle für Anfänger und verbessern Sie Ihre Fähigkeiten zur Textbearbeitung unter Linux."
keywords: "Vim-Bearbeitung, Vim-Befehle, Linux-Texteditor, Vim-Tutorial, Vim-Anleitung, Vim für Anfänger, dd-Befehl, Vim löschen"
---

## Lesson Content

Das Bearbeiten in Vim erfolgt aus dem Normalmodus heraus unter Verwendung von Operatoren und Bewegungen. Sie können Text effizient löschen, ändern, kopieren (yank), einfügen (put) und ersetzen.

- Drücken Sie `Esc`, um sicherzustellen, dass Sie sich im Normalmodus befinden, bevor Sie diese Befehle verwenden.

Löschen (Operator `d`):

- `x` – löscht das Zeichen unter dem Cursor
- `dw` – löscht vom Cursor bis zum Anfang des nächsten Wortes
- `d$` – löscht vom Cursor bis zum Zeilenende
- `dd` – löscht die aktuelle Zeile
- Zählungen anwendbar: `3dd` löscht drei Zeilen; `2dw` löscht zwei Wörter

Ändern (Operator `c`, löschen und dann in den Einfügemodus wechseln):

- `cw` – ändert das Wort ab dem Cursor
- `c$` – ändert bis zum Zeilenende
- `cc` – ändert die gesamte Zeile

Yank und Put (Kopieren/Einfügen):

- `yw` – yank word
- `yy` – yank the current line
- `p` – put (einfügen) nach dem Cursor oder unterhalb der Zeile
- `P` – put (einfügen) vor dem Cursor oder oberhalb der Zeile

Ersetzen und andere nützliche Bearbeitungen:

- `r{char}` – ersetzt das Zeichen unter dem Cursor durch `{char}`
- `R` – wechselt in den Ersetzungsmodus, um Text zu überschreiben
- `J` – verbindet die aktuelle Zeile mit der nächsten Zeile
- `.` – wiederholt die letzte Änderung

Kombinieren Sie Operatoren mit Bewegungen für mehr Leistung: `d}` löscht bis zum nächsten Absatz; `caw` ändert „a word“ (Wort unter dem Cursor einschließlich umgebendem Leerzeichen).

## Exercise

Öffnen Sie eine Datei mit `vim [file]` und versuchen Sie: `dw`, `cw`, `yy` dann `p`, `dd`, `J` und `.` um eine Änderung zu wiederholen.

## Quiz Question

Welcher Befehl löscht die aktuelle Zeile in Vim?

## Quiz Answer

dd
