---
lesson_id: "vim-navigation"
course_id: "advanced-text-fu"
lang: "de"
order_index: 5
title: "Vim-Navigation"
description: "Lerne, dich in Vims Normalmodus zeichen-, wort-, zeilen- und dateiweise zu bewegen."
meta_title: "Vim-Navigation - Fortgeschrittene Text-Fu"
meta_description: "Lernen Sie die Grundlagen der Vim-Navigation mit den Tasten h, j, k, l. Verstehen Sie die wesentliche Vim-Bewegung für Anfänger und verbessern Sie Ihre Linux-Befehlszeilenkenntnisse."
meta_keywords: "Vim-Navigation, Vim-Tutorial, Linux Vim, Vim-Bewegung, Vim-Grundlagen, Anfänger Vim, Linux-Texteditor, Vim-Anleitung"
---

Vim bietet Tastaturbewegungen, die im Terminal ohne Maus funktionieren. Einige Konfigurationen unterstützen zusätzlich eine Maus, doch Bewegungsbefehle lassen sich mit Bearbeitungsbefehlen kombinieren und sind deshalb besonders nützlich.

Drücke vor dem Üben `Esc`, um in den Normalmodus zurückzukehren.

## Zeichen- und bildschirmzeilenweise bewegen

Die grundlegenden Bewegungen des Normalmodus sind:

- `h`: Ein Zeichen nach links.
- `j`: Eine Bildschirmzeile nach unten.
- `k`: Eine Bildschirmzeile nach oben.
- `l`: Ein Zeichen nach rechts.

Pfeiltasten führen üblicherweise ähnliche Bewegungen aus; mit `h`, `j`, `k` und `l` bleiben deine Hände jedoch nahe an anderen Befehlen. Bei einer umgebrochen dargestellten Zeile bewegen sich `j` und `k` normalerweise nach Dateizeilen, `gj` und `gk` nach sichtbaren Bildschirmzeilen.

:::single-choice{#vim-navigation-down}
Welche Taste bewegt den Cursor im Normalmodus eine Zeile nach unten?

::option[`k`]{#vim-nav-k-up explanation="Die Bewegung `k` führt eine Zeile nach oben."}
::option[`l`]{#vim-nav-l-right explanation="Die Bewegung `l` führt ein Zeichen nach rechts."}
::option[`j`]{#vim-nav-j-down .correct explanation="Die Bewegung `j` führt im Normalmodus eine Zeile nach unten."}
:::

## Bewegungen mit einer Anzahl versehen

Setze vor viele Bewegungen eine positive Anzahl, um sie zu wiederholen. Zum Beispiel:

```text
5j
3l
```

`5j` bewegt sich fünf Zeilen nach unten; `3l` bewegt sich soweit möglich drei Zeichenpositionen nach rechts. Anzahlen lassen sich auch mit Wort- und Bearbeitungsbefehlen kombinieren.

:::single-choice{#vim-navigation-count}
Was bewirkt `4k` im Normalmodus?

::option[Der Cursor bewegt sich soweit möglich vier Zeilen nach unten.]{#vim-nav-four-down explanation="Für die Bewegung nach unten dient `j`; `k` bewegt sich in die Gegenrichtung."}
::option[Der Cursor bewegt sich soweit möglich vier Zeilen nach oben.]{#vim-nav-four-up .correct explanation="Die Anzahl `4` wiederholt die Aufwärtsbewegung `k` viermal."}
::option[Vier Zeilen oberhalb des Cursors werden gelöscht.]{#vim-nav-delete-four explanation="Eine Bewegung allein ändert die Cursorposition. Zum Löschen wäre ein Operator wie `d` erforderlich."}
:::

## Wortweise bewegen

Nützliche Wortbewegungen sind:

- `w`: Zum Anfang des nächsten Worts.
- `b`: Zum Anfang des aktuellen oder vorherigen Worts.
- `e`: Zum Ende des aktuellen oder nächsten Worts.

Die großgeschriebenen Formen `W`, `B` und `E` verwenden durch Leerraum getrennte WÖRTER und behandeln Satzzeichen anders. Mit einer vorangestellten Anzahl bewegst du dich durch mehrere Wörter, etwa mit `3w`.

:::single-choice{#vim-navigation-next-words}
Welcher Befehl des Normalmodus bewegt sich vorwärts zum Anfang der dritten folgenden Wortposition?

::option[`3w`]{#vim-nav-three-words .correct explanation="Die Anzahl wendet die Bewegung zum nächsten Wort dreimal an."}
::option[`w3`]{#vim-nav-word-three explanation="Bei dieser Befehlsform stehen Anzahlen vor Bewegungen; eine nachgestellte `3` beschreibt nicht die verlangte Bewegung."}
::option[`3b`]{#vim-nav-three-back explanation="Die Bewegung `b` führt zu früheren Wortanfängen statt vorwärts."}
:::

## Innerhalb einer Zeile bewegen

Diese Bewegungen zielen auf Positionen der aktuellen Zeile:

- `0`: Zur Spalte null.
- `^`: Zum ersten Nicht-Leerzeichen.
- `$`: Zum Zeilenende.

Der Unterschied zwischen `0` und `^` ist bei eingerückten Zeilen wichtig.

:::single-choice{#vim-navigation-first-nonblank}
Welche Bewegung führt zum ersten Nicht-Leerzeichen einer eingerückten Zeile?

::option[`0`]{#vim-nav-column-zero explanation="Null führt in die erste Spalte, die Einrückungsleerraum enthalten kann."}
::option[`$`]{#vim-nav-line-end explanation="Die Dollar-Bewegung zielt auf das Zeilenende."}
::option[`^`]{#vim-nav-first-nonblank .correct explanation="Die Caret-Bewegung überspringt führende Leerzeichen und landet beim ersten Nicht-Leerzeichen."}
:::

## Durch die Datei bewegen

Für größere Sprünge dienen diese Befehle des Normalmodus:

- `gg`: Zur ersten Zeile.
- `G`: Zur letzten Zeile.
- `42G`: Zu Zeile 42.
- `Ctrl+F`: Ungefähr einen Bildschirm vorwärts.
- `Ctrl+B`: Ungefähr einen Bildschirm rückwärts.

`:42`, gefolgt von Enter, ist eine weitere Möglichkeit, zu Zeile 42 zu springen.

:::single-choice{#vim-navigation-file-end}
Welcher Befehl des Normalmodus führt zur letzten Zeile des Puffers?

::option[`gg`]{#vim-nav-first-line explanation="Das kleine `gg` führt zur ersten und nicht zur letzten Zeile."}
::option[`$`]{#vim-nav-current-line-end explanation="Die Dollar-Bewegung führt ans Ende der aktuellen Zeile statt ans Dateiende."}
::option[`G`]{#vim-nav-last-line .correct explanation="Das große `G` springt ohne Anzahl zur letzten Zeile."}
:::

Mit dieser Übung kannst du die Tastaturnavigation in einer entbehrlichen Datei trainieren:

1. **[Textdateien in Linux mit Vim und Nano bearbeiten](https://labex.io/de/labs/comptia-edit-text-files-in-linux-with-vim-and-nano-591076)** – Übe in einer echten Linux-Umgebung das Erstellen, Bearbeiten, Speichern und Navigieren mit Vim und Nano.

## Zusammenfassung

Du kannst nun auf mehreren sinnvollen Ebenen durch einen Vim-Puffer navigieren.

1. Bewege dich mit `h`, `j`, `k` und `l` zeichen- oder zeilenweise.
2. Wiederhole Bewegungen mit einem Zahlenpräfix.
3. Wechsle mit `w`, `b` und `e` zwischen Wortgrenzen.
4. Ziele auf Zeilenanfang, ersten Text oder Zeilenende.
5. Springe mit `gg`, `G` oder einer Zeilennummer zu Dateipositionen.
