---
index: 7
lang: "de"
title: "Vim-Bearbeitung"
meta_title: "Vim-Bearbeitung - Fortgeschrittene Text-Fu"
meta_description: "Lernen Sie die Grundlagen der Vim-Bearbeitung: Text effizient löschen, ändern, kopieren und einfügen. Meistern Sie wichtige Vim-Befehle für Anfänger und verbessern Sie Ihre Linux-Textbearbeitungsfähigkeiten."
meta_keywords: "Vim-Bearbeitung, Vim-Befehle, Linux-Texteditor, Vim-Tutorial, Vim-Anleitung, Vim für Anfänger, dd-Befehl, Vim löschen"
---

## Lesson Content

Das Bearbeiten in Vim erfolgt im Normalmodus unter Verwendung von Operatoren und Bewegungen. Sie können Text effizient löschen, ändern, kopieren (yank), einfügen (put) und ersetzen.

- Drücken Sie `Esc`, um sicherzustellen, dass Sie sich im Normalmodus befinden, bevor Sie diese Befehle verwenden.

Löschen (Operator `d`):

- `x` – löscht das Zeichen unter dem Cursor
- `dw` – löscht vom Cursor bis zum Anfang des nächsten Wortes
- `d$` – löscht vom Cursor bis zum Ende der Zeile
- `dd` – löscht die aktuelle Zeile
- Zählungen gelten: `3dd` löscht drei Zeilen; `2dw` löscht zwei Wörter

Ändern (Operator `c`, löschen und dann in den Einfügemodus wechseln):

- `cw` – ändert das Wort ab dem Cursor
- `c$` – ändert bis zum Ende der Zeile
- `cc` – ändert die gesamte Zeile

Yank und Put (Kopieren/Einfügen):

- `yw` – yankt ein Wort
- `yy` – yankt die aktuelle Zeile
- `p` – fügt (paste) nach dem Cursor oder unter der Zeile ein
- `P` – fügt (paste) vor dem Cursor oder über der Zeile ein

Ersetzen und andere nützliche Bearbeitungen:

- `r{char}` – ersetzt das Zeichen unter dem Cursor durch `{char}`
- `R` – wechselt in den Ersetzungsmodus, um Text zu überschreiben
- `J` – verbindet die aktuelle Zeile mit der nächsten Zeile
- `.` – wiederholt die letzte Änderung

Kombinieren Sie Operatoren mit Bewegungen für mehr Leistung: `d}` löscht bis zum nächsten Absatz; `caw` ändert „ein Wort“ (Wort unter dem Cursor einschließlich des umgebenden Leerzeichens).

## Exercise

Übung macht den Meister! Hier ist ein praktisches Labor, um Ihr Verständnis der Textbearbeitung in Vim zu vertiefen:

1. **[Textdateien in Linux mit Vim und Nano bearbeiten](https://labex.io/de/labs/comptia-edit-text-files-in-linux-with-vim-and-nano-591076)** – Üben Sie das Erstellen von Dateien, das Bearbeiten von Text, das Speichern von Dateien und die Navigation mit vi/vim und nano. Dieses Labor hilft Ihnen, die grundlegenden Bearbeitungsbefehle, die besprochen wurden, wie das Löschen, Ändern, Yanking und Einfügen von Text, zu meistern.

Dieses Labor wird Ihnen helfen, die Konzepte in realen Szenarien anzuwenden und Vertrauen in die Textbearbeitung unter Linux aufzubauen.

## Quiz Question

Welcher Befehl löscht die aktuelle Zeile in Vim?

## Quiz Answer

dd
