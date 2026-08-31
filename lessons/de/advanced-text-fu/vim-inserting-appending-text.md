---
lesson_id: "vim-inserting-appending-text"
course_id: "advanced-text-fu"
lang: "de"
order_index: 6
title: "Vim: Text einfügen und anhängen"
description: "Lerne, wie du in Vim vor, hinter, über oder unter der aktuellen Cursorposition in den Einfügemodus wechselst."
meta_title: "Vim: Text einfügen und anhängen – Fortgeschrittenes Text-Fu"
meta_description: "Lerne den Unterschied zwischen Einfügen und Anhängen in Vim. Beherrsche Befehle wie 'i', 'a' und 'o', um Text effizient zu bearbeiten und neue Zeilen anzulegen."
meta_keywords: "vim anhängen, append vs insert vim, vim einfügen vs anhängen, vim zeile hinzufügen, vim textbearbeitung, vim befehle, vim tutorial, einfügemodus, anhängemodus"
---

Im Normalmodus interpretiert Vim Tasteneingaben als Befehle. Im Einfügemodus wird der eingegebene Text in den Puffer eingefügt. Verschiedene Befehle des Normalmodus wechseln an unterschiedlichen Positionen in den Einfügemodus. So kannst du direkt mit dem Tippen beginnen, ohne vorher separat dorthin zu navigieren.

Drücke `Esc`, um den Einfügemodus zu verlassen und in den Normalmodus zurückzukehren. Wenn du nicht sicher bist, welcher Modus aktiv ist, kannst du mit `Esc` zuverlässig wieder den Normalmodus herstellen. Beachte jedoch, dass dadurch eine noch ausstehende Operation abgebrochen werden kann.

:::single-choice{#vim-insert-return-normal}
Mit welcher Taste kehrst du normalerweise vom Einfügemodus in den Normalmodus zurück?

::option[`Esc`]{#vim-insert-escape .correct explanation="Escape beendet die aktuelle Eingabe und bringt Vim zurück in den Normalmodus."}
::option[`Enter`]{#vim-insert-enter explanation="Enter fügt einen Zeilenumbruch ein und lässt Vim im Einfügemodus."}
::option[`Tab`]{#vim-insert-tab explanation="Tab fügt eine Einrückung ein oder löst eine konfigurierte Vervollständigung aus; normalerweise verlässt du damit nicht den Einfügemodus."}
:::

## Vor oder hinter dem Cursor einfügen

Aus dem Normalmodus:

- `i`: Vor dem Cursor in den Einfügemodus wechseln.
- `a`: Hinter dem Cursor in den Einfügemodus wechseln.

Steht der Cursor beispielsweise auf dem `b` in `abc`, beginnt `i` vor dem `b`, während `a` nach dem `b` beginnt. Beide Befehle wechseln den Modus; der Text, den du anschließend eingibst, wird an dieser Stelle eingefügt.

:::single-choice{#vim-insert-before-cursor}
Welche Taste wechselt aus dem Normalmodus unmittelbar vor dem Cursor in den Einfügemodus?

::option[`a`]{#vim-insert-a-after explanation="Das kleine `a` hängt Text hinter dem Cursor an, statt ihn davor einzufügen."}
::option[`o`]{#vim-insert-o-below explanation="Das kleine `o` öffnet unter der aktuellen Zeile eine neue Zeile und wechselt dann in den Einfügemodus."}
::option[`i`]{#vim-insert-i-before .correct explanation="Das kleine `i` beginnt die Eingabe an der aktuellen Cursorposition, also vor dem Zeichen unter dem Cursor."}
:::

## An Zeilengrenzen einfügen

Großgeschriebene Befehle springen zu wichtigen Positionen in der aktuellen Zeile:

- `I`: Vor dem ersten Zeichen der Zeile, das kein Leerraum ist, in den Einfügemodus wechseln.
- `A`: Am Ende der Zeile in den Einfügemodus wechseln.

In einer eingerückten Zeile überspringt `I` die Einrückung und beginnt vor dem ersten sichtbaren Text. Verwende `0i`, wenn du ausdrücklich in Spalte null einfügen möchtest.

:::single-choice{#vim-insert-first-nonblank}
Welcher Befehl des Normalmodus beginnt die Eingabe vor dem ersten Zeichen der aktuellen Zeile, das kein Leerraum ist?

::option[`i`]{#vim-insert-lower-i explanation="Das kleine `i` verwendet die aktuelle Cursorposition und springt nicht zuerst zum Textanfang der Zeile."}
::option[`A`]{#vim-insert-capital-a explanation="Das große `A` beginnt die Eingabe am Ende der aktuellen Zeile."}
::option[`I`]{#vim-insert-capital-i .correct explanation="Das große `I` springt zum ersten Nicht-Leerraum-Zeichen und wechselt davor in den Einfügemodus."}
:::

:::single-choice{#vim-append-line-end}
Welcher Befehl des Normalmodus springt ans Ende der aktuellen Zeile und wechselt in den Einfügemodus?

::option[`A`]{#vim-append-capital-a .correct explanation="Das große `A` verbindet den Sprung ans Zeilenende mit dem Wechsel in den Einfügemodus."}
::option[`$`]{#vim-move-line-end explanation="Die Dollar-Bewegung erreicht das Zeilenende, bleibt aber im Normalmodus."}
::option[`a`]{#vim-append-one-position explanation="Das kleine `a` beginnt hinter der aktuellen Cursorposition, statt ans Zeilenende zu springen."}
:::

## Eine neue Zeile öffnen

Aus dem Normalmodus:

- `o`: Unter der aktuellen Zeile eine neue Zeile öffnen und in den Einfügemodus wechseln.
- `O`: Über der aktuellen Zeile eine neue Zeile öffnen und in den Einfügemodus wechseln.

Vim richtet die neue Zeile entsprechend den aktuellen Einstellungen und den Regeln für den Dateityp ein. Mit einem Zähler lässt sich das Öffnen von Zeilen wiederholen. Lerne zunächst die Form für eine einzelne Zeile, damit die anschließende Cursorposition vorhersehbar bleibt.

:::single-choice{#vim-open-line-above}
Welcher Befehl des Normalmodus öffnet über der aktuellen Zeile eine neue Zeile und wechselt in den Einfügemodus?

::option[`o`]{#vim-open-lower-o explanation="Das kleine `o` öffnet eine Zeile unterhalb der aktuellen Zeile."}
::option[`O`]{#vim-open-upper-o .correct explanation="Das große `O` öffnet darüber eine neue Zeile und beginnt dort mit der Eingabe."}
::option[`A`]{#vim-open-upper-a explanation="Das große `A` hängt Text am Ende der vorhandenen Zeile an und öffnet darüber keine neue Zeile."}
:::

Mit diesem praktischen Lab kannst du den Wechsel zwischen Normal- und Einfügemodus üben:

1. **[Textdateien unter Linux mit Vim und Nano bearbeiten](https://labex.io/labs/comptia-edit-text-files-in-linux-with-vim-and-nano-591076)** – Übe, Dateien anzulegen, Text zu bearbeiten und zu speichern sowie mit vi/vim und nano zu navigieren. Das Lab hilft dir, die grundlegende Arbeit mit Vims Normal- und Einfügemodus zu beherrschen.

## Zusammenfassung

Du kannst nun genau dort in den Einfügemodus wechseln, wo neuer Text stehen soll.

1. Kehre mit `Esc` in den Normalmodus zurück.
2. Füge mit `i` oder `a` Text vor beziehungsweise hinter dem Cursor ein.
3. Beginne mit `I` am ersten Text der Zeile oder mit `A` am Zeilenende.
4. Öffne mit `o` eine Zeile darunter.
5. Öffne mit `O` eine Zeile darüber.
