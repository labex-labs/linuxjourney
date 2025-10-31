---
index: 7
lang: "de"
title: "Vim-Bearbeitung"
meta_title: "Vim-Bearbeitung - Fortgeschrittenes Text-Fu"
meta_description: "Ein Vim-Tutorial für Anfänger über wesentliche Bearbeitungsbefehle. Lernen Sie, wie Sie Text im Vim-Texteditor löschen, ändern, kopieren (yank) und einfügen, um Ihren Linux-Workflow zu verbessern."
meta_keywords: "Vim-Bearbeitung, Vim-Befehle, Linux-Texteditor, Vim-Tutorial, Vim-Anleitung, Anfänger Vim, dd-Befehl, Vim löschen"
---

## Lesson Content

Das Bearbeiten von Text in Vim ist eine leistungsstarke Funktion, die auf der Kombination von Operatoren und Bewegungen aus dem Normalmodus beruht. Dieser Ansatz ermöglicht es Ihnen, Text effizient zu löschen, zu ändern, zu kopieren (yank) und einzufügen (put).

Bevor Sie Befehle ausführen, drücken Sie `Esc`, um sicherzustellen, dass Sie sich im Normalmodus befinden.

### Verstehen von Vim-Operatoren und -Bewegungen

Der Kern der Vim-Bearbeitung ist die Formel: `Operator + Bewegung`. Ein Operator ist eine Aktion (wie `d` für löschen), und eine Bewegung ist eine Navigation (wie `w` für Wort). Zum Beispiel kombiniert `dw` den Löschoperator mit der Wortbewegung, um ein Wort zu löschen. Sie können auch Zähler verwenden, um eine Aktion zu wiederholen, z. B. `2dw`, um zwei Wörter zu löschen.

### Text in Vim löschen

Der Löschoperator ist `d`. Er ist einer der häufigsten Vim-Befehle zur Textmanipulation.

- `x` – Löscht das Zeichen direkt unter dem Cursor.
- `dw` – Löscht vom Cursor bis zum Anfang des nächsten Wortes.
- `d$` – Löscht vom Cursor bis zum Ende der aktuellen Zeile.
- `dd` – Der Befehl `dd` löscht die gesamte aktuelle Zeile.
- `3dd` – Löscht drei Zeilen, beginnend mit der aktuellen Zeile.

### Text ändern

Der Änderungsoperator `c` funktioniert ähnlich wie löschen, versetzt Sie jedoch nach der Ausführung der Aktion in den Einfügemodus. Dies ist nützlich, um Text zu ersetzen.

- `cw` – Ändert den Text vom Cursor bis zum Ende des Wortes.
- `c$` – Ändert den Text vom Cursor bis zum Ende der Zeile.
- `cc` – Ändert die gesamte aktuelle Zeile.

### Text in Vim kopieren und einfügen

In Vim wird das Kopieren als „Yanking“ (Operator `y`) und das Einfügen als „Putting“ bezeichnet.

- `yw` – Yankt (kopiert) ein Wort.
- `yy` – Yankt die gesamte aktuelle Zeile.
- `p` – Put (fügt) den yanked Text nach dem Cursor oder in die nächste Zeile ein.
- `P` – Put den Text vor dem Cursor oder in die vorherige Zeile ein.

### Andere nützliche Bearbeitungsbefehle

Dieser Vim-Leitfaden wäre nicht vollständig ohne ein paar weitere praktische Befehle.

- `r{char}` – Ersetzt das einzelne Zeichen unter dem Cursor durch das angegebene Zeichen.
- `R` – Wechselt in den Ersetzen-Modus, sodass Sie Text kontinuierlich überschreiben können, bis Sie `Esc` drücken.
- `J` – Fügt die aktuelle Zeile mit der nächsten zusammen.
- `.` – Wiederholt die letzte vorgenommene Änderung, ein sehr leistungsstarker und effizienter Befehl.

Die Kombination von Operatoren mit verschiedenen Bewegungen schöpft das volle Potenzial dieses Linux-Texteditors aus. Zum Beispiel löscht `d}` bis zum nächsten Absatz, und `caw` ändert „ein Wort“ (das Wort unter dem Cursor einschließlich eventueller umgebender Leerzeichen).

## Exercise

Um Ihr Wissen in die Praxis umzusetzen, empfehlen wir das folgende praktische Labor. Es wird Ihnen helfen, die grundlegenden Bearbeitungsbefehle zu meistern, die in diesem Vim-Tutorial besprochen wurden.

1.  **[Textdateien in Linux mit Vim und Nano bearbeiten](https://labex.io/de/labs/comptia-edit-text-files-in-linux-with-vim-and-nano-591076)** - Üben Sie das Erstellen von Dateien, das Bearbeiten von Text, das Speichern von Dateien und die Navigation sowohl mit vi/vim als auch mit nano. Dieses Labor hilft Ihnen, Konzepte wie das Löschen, Ändern, Yanken und Putten von Text in realen Szenarien anzuwenden.

## Quiz Question

Welcher Befehl löscht die aktuelle Zeile in Vim? (Bitte antworten Sie auf Englisch und achten Sie auf die Groß-/Kleinschreibung).

## Quiz Answer

dd
