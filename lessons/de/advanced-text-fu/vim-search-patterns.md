---
lesson_id: "vim-search-patterns"
course_id: "advanced-text-fu"
lang: "de"
order_index: 4
title: "Vim Suchmuster"
description: "Lerne, in Vim vorwärts oder rückwärts zu suchen und Mustertreffer zu wiederholen, zu verfeinern oder auszublenden."
meta_title: "Vim Suchmuster - Fortgeschrittenes Text-Fu"
meta_description: "Lernen Sie, wie Sie eine Vorwärts- und Rückwärtssuche in Vim mithilfe von Mustern durchführen. Meistern Sie Vim-Suchtechniken, um Text schnell zu finden, und navigieren Sie mit 'n' und 'N' durch die Ergebnisse."
meta_keywords: "Vim Suche, Vim Nachschlagen, Vim Befehle, Linux Texteditor, Vim Tutorial, Vim Anleitung, Suchmuster"
---

Vim sucht ab der aktuellen Cursorposition nach Mustern. Beginne im Normalmodus, starte eine Vorwärts- oder Rückwärtssuche und wechsle anschließend zwischen Treffern, ohne das Muster erneut einzugeben.

## Vorwärts suchen

Gib im Normalmodus `/` und danach ein Muster ein und drücke Enter. Vim bewegt sich zum nächsten Treffer hinter dem Cursor:

```vim
/pretty
```

Suchen verwenden Vims Syntax regulärer Ausdrücke. Zeichen wie `.`, `*`, `[` und `\` können daher eine besondere Bedeutung besitzen. Setze `\V` an den Anfang, wenn der Rest des Musters als „very nomagic“ behandelt werden soll, oder schütze Sonderzeichen gezielt.

:::single-choice{#vim-search-forward-key} Welcher Befehl startet im Normalmodus eine Vorwärtssuche nach `pretty`?

::option[`?pretty`, gefolgt von Enter]{#vim-backward-pretty explanation="Ein Fragezeichen startet ab der aktuellen Cursorposition eine Rückwärtssuche."}
::option[`/pretty`, gefolgt von Enter]{#vim-forward-pretty .correct explanation="Ein Schrägstrich beginnt eine Vorwärtssuche; mit Enter sendest du das Muster ab."}
::option[`:pretty`, gefolgt von Enter]{#vim-command-pretty explanation="Ein Doppelpunkt öffnet den Befehlszeilenmodus für einen Ex-Befehl; `pretty` wird so nicht als Suche eingeführt."}
:::

## Rückwärts suchen

Gib `?` und danach ein Muster ein und drücke Enter, um zum vorherigen Treffer vor dem Cursor zu wechseln:

```vim
?pretty
```

Das bedeutet nicht grundsätzlich „der letzte Treffer in der Datei“. Das Ergebnis hängt von der aktuellen Cursorposition ab. Mit Vims Standardeinstellung `wrapscan` kann eine Suche am Anfang oder Ende umbrechen; `:set nowrapscan` deaktiviert dieses Verhalten.

:::single-choice{#vim-search-backward-key} Welches Suchpräfix des Normalmodus sucht vom Cursor aus in früherem Text?

::option[`/`]{#vim-slash-forward explanation="Ein Schrägstrich sucht vom Cursor aus vorwärts statt in vorhergehendem Text."}
::option[`?`]{#vim-question-backward .correct explanation="Ein Fragezeichen startet ab der aktuellen Cursorposition eine rückwärts gerichtete Mustersuche."}
::option[`:`]{#vim-colon-command explanation="Ein Doppelpunkt beginnt eine Ex-Befehlszeile und ist nicht das Präfix einer Rückwärtssuche."}
:::

## Eine Suche wiederholen

Nach beiden Sucharten gilt:

- Drücke `n`, um in der ursprünglichen Suchrichtung zu wiederholen.
- Drücke `N`, um in der entgegengesetzten Richtung zu wiederholen.

Nach `/pretty` bewegt sich `n` daher vorwärts und `N` rückwärts. Nach `?pretty` bewegt sich `n` rückwärts und `N` vorwärts.

:::single-choice{#vim-repeat-backward-search} Welche Taste wiederholt nach `?error` die Suche in derselben Rückwärtsrichtung?

::option[`n`]{#vim-same-question-search .correct explanation="Das kleine `n` wiederholt die letzte Suche in ihrer ursprünglichen Richtung, hier also rückwärts."}
::option[`N`]{#vim-opposite-question-search explanation="Das große `N` kehrt die ursprüngliche Suchrichtung um und bewegt sich nach einer `?`-Suche daher vorwärts."}
::option[`/`]{#vim-new-forward-search explanation="Ein Schrägstrich startet eine neue Vorwärtssuche und wartet auf ein Muster, statt die vorherige Suche zu wiederholen."}
:::

## Nach dem Wort unter dem Cursor suchen

Setze den Cursor im Normalmodus auf ein Wort und verwende:

- `*`, um vorwärts nach diesem vollständigen Wort zu suchen.
- `#`, um rückwärts nach diesem vollständigen Wort zu suchen.

Diese Befehle setzen das aktuelle Suchmuster, sodass `n` und `N` daran anschließen können.

:::single-choice{#vim-current-word-forward} Welche Taste des Normalmodus sucht vorwärts nach dem vollständigen Wort unter dem Cursor?

::option[`#`]{#vim-hash-current-word explanation="Die Rautetaste sucht rückwärts nach dem Wort unter dem Cursor."}
::option[`*`]{#vim-star-current-word .correct explanation="Der Sternbefehl bildet aus dem Wort unter dem Cursor ein Ganzwortmuster und sucht vorwärts."}
::option[`n`]{#vim-repeat-current-pattern explanation="Die Taste `n` wiederholt eine bestehende Suche; sie erzeugt nicht zuerst ein Muster aus dem aktuellen Wort."}
:::

## Großschreibung und Hervorhebung steuern

Vim-Optionen können das Verhalten bei Groß- und Kleinschreibung ändern:

- `:set ignorecase` lässt Suchen die Großschreibung ignorieren.
- `:set smartcase` macht eine Suche bei einem Großbuchstaben wieder abhängig von der Schreibweise, wenn zugleich `ignorecase` gesetzt ist.
- `\c` im Muster erzwingt für diese Suche die Missachtung der Großschreibung.
- `\C` erzwingt für diese Suche die Beachtung der Großschreibung.

Beispielsweise passt `/\cerror` unabhängig von den aktuellen Optionen auf `error`, `Error` und `ERROR`.

Ist die Suchhervorhebung aktiv, entfernt `:nohlsearch` die aktuell sichtbaren Markierungen, ohne das Suchmuster zu löschen. Die nächste Suche oder Wiederholung kann Treffer erneut hervorheben.

:::single-choice{#vim-force-case-insensitive} Welches Muster zwingt eine einzelne Vim-Suche nach `error`, unabhängig von den aktuellen Optionen die Großschreibung zu ignorieren?

::option[`/\Cerror`]{#vim-pattern-match-case explanation="Das große `\C` erzwingt die Beachtung der Groß- und Kleinschreibung und damit das Gegenteil."}
::option[`/:error`]{#vim-pattern-colon-error explanation="Ein Doppelpunkt im Muster ist hier ein wörtliches Zeichen und wählt kein Verhalten für die Großschreibung aus."}
::option[`/\cerror`]{#vim-pattern-ignore-case .correct explanation="Das Element `\c` macht diese Suche unabhängig von der Großschreibung, sodass verschiedene Schreibweisen passen können."}
:::

Mit dieser Übung kannst du Navigation und Suche in einer kontrollierten Datei trainieren:

1. **[Textdateien in Linux mit Vim und Nano bearbeiten](https://labex.io/de/labs/comptia-edit-text-files-in-linux-with-vim-and-nano-591076)** – Übe das Erstellen, Bearbeiten, Speichern und Navigieren von Textdateien mit Vim und Nano.

## Zusammenfassung

Du kannst nun einen Vim-Puffer durchsuchen und vorhersehbar zwischen Treffern wechseln.

1. Starte Vorwärtssuchen mit `/` und Rückwärtssuchen mit `?`.
2. Wiederhole mit `n` in derselben und mit `N` in der Gegenrichtung.
3. Suche mit `*` oder `#` nach dem vollständigen Wort unter dem Cursor.
4. Steuere Großschreibung für ein Muster oder über Optionen.
5. Blende Hervorhebungen aus, ohne das aktuelle Suchmuster zu verlieren.
