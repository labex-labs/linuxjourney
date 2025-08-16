---
lang: "de"
title: "Vim-Suchmuster"
description: "Lernen Sie Vim-Suchmuster: Vorwärtssuche (/) und Rückwärtssuche (?). Navigieren Sie mit 'n' und 'N' durch die Ergebnisse. Verbessern Sie noch heute Ihre Vim-Fähigkeiten!"
keywords: "Vim-Suche, Vim-Befehle, Linux-Texteditor, Vim-Tutorial, Vim-Anleitung, Vim für Anfänger"
---

## Lesson Content

Um nach einem Ausdruck zu suchen, geben Sie einfach die Taste `/` und dann Ihren Suchbegriff ein, während Sie sich in einer Vim-Sitzung befinden. Sobald Sie die Eingabetaste drücken, können Sie `n` drücken, um in Ihren Suchergebnissen vorwärts zu gehen, oder `N`, um rückwärts zu gehen.

```plaintext
My pretty file is very pretty.

/pretty

will find the pretty words in the text file.
```

Der Suchbefehl `?` durchsucht die Textdatei rückwärts. Im vorherigen Beispiel würde also das letzte „pretty“ zuerst erscheinen.

```plaintext
My pretty file is very pretty.

?pretty

will find the pretty words in the text file.
```

## Exercise

Spielen Sie mit der Suchtaste. Öffnen Sie eine Textdatei in Vim mit: `vim [textfile]` und beginnen Sie mit der Suche!

## Quiz Question

Welche Taste wird zum Suchen in Vim verwendet?

## Quiz Answer

/
