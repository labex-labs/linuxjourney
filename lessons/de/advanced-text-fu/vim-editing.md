---
lesson_id: "vim-editing"
course_id: "advanced-text-fu"
lang: "de"
order_index: 7
title: "Text in Vim bearbeiten"
description: "Lerne, wie Vim Operatoren, Bewegungen, Register, Einfügebefehle und Rückgängig-Funktionen zur Textbearbeitung kombiniert."
meta_title: "Text in Vim bearbeiten – Fortgeschrittenes Text-Fu"
meta_description: "Ein Vim-Tutorial für Einsteiger zu wichtigen Bearbeitungsbefehlen. Lerne, wie du im Vim-Texteditor Text löschst, änderst, kopierst und einfügst."
meta_keywords: "Vim Bearbeitung, Vim Befehle, Linux Texteditor, Vim Tutorial, Vim Anleitung, Vim Anfänger, dd Befehl, Vim löschen"
---

Vims Bearbeitungsbefehle kombinieren häufig einen Operator mit einer Bewegung oder einem Textobjekt. Dank dieser Grammatik lassen sich dieselben Aktionen auf Zeichen, Wörter, Zeilen und größere Bereiche anwenden. Drücke vor dem Üben `Esc`, um in den Normalmodus zurückzukehren.

## Einen Operator mit einer Bewegung kombinieren

Die allgemeine Form lautet:

```text
[Anzahl] Operator [Anzahl] Bewegung
```

Häufig verwendete Operatoren sind:

- `d`: Text löschen.
- `c`: Text ändern und anschließend in den Einfügemodus wechseln.
- `y`: Text „yanken“, also kopieren.

`dw` löscht beispielsweise den von der Bewegung `w` erfassten Bereich, während `d$` vom Cursor bis einschließlich des Zeilenendes löscht. `2dw` wendet das Löschen auf zwei Wortbewegungen an.

:::single-choice{#vim-edit-operator-motion} Was bewirkt `d$` im Normalmodus?

::option[Es löscht ab dem Cursor die gesamte Datei.]{#vim-edit-delete-file-end explanation="Die Dollar-Bewegung zielt auf das Ende der aktuellen Zeile, nicht auf das Ende des gesamten Puffers."}
::option[Es löscht vom Cursor bis einschließlich des Zeilenendes.]{#vim-edit-delete-line-end .correct explanation="Der Operator `d` wird auf die Bewegung `$` zum Zeilenende angewendet."}
::option[Es bewegt den Cursor ans Zeilenende, ohne den Text zu verändern.]{#vim-edit-move-line-end explanation="`$` allein bewegt den Cursor. Das vorangestellte `d` macht aus dem erfassten Bereich jedoch eine Löschoperation."}
:::

## Zeichen und Zeilen bearbeiten

Einige Befehle dienen als praktische Kurzformen:

- `x`: Das Zeichen unter dem Cursor löschen.
- `dd`: Die aktuelle Zeile zeilenweise löschen.
- `3dd`: Drei Zeilen löschen, beginnend mit der aktuellen Zeile.
- `cc`: Die aktuelle Zeile ändern und in den Einfügemodus wechseln.
- `r{char}`: Das Zeichen unter dem Cursor durch `{char}` ersetzen.
- `R`: Bis zum Drücken von `Esc` in den Ersetzen-Modus wechseln.

Wird ein Operator wie in `dd` wiederholt, arbeitet er zeilenweise. Ein Zähler erweitert die Anzahl der betroffenen Zeilen.

:::single-choice{#vim-edit-delete-three-lines} Welcher Befehl des Normalmodus löscht die aktuelle und die beiden folgenden Zeilen?

::option[`dd3`]{#vim-edit-dd-three explanation="Bei dieser Befehlsform steht der Zähler vor dem verdoppelten Operator."}
::option[`3x`]{#vim-edit-three-x explanation="Dieser Befehl löscht drei Zeichen ab dem Cursor, nicht drei vollständige Zeilen."}
::option[`3dd`]{#vim-edit-three-dd .correct explanation="Der Zähler gilt für den zeilenweisen Befehl `dd` und löscht ab der aktuellen Zeile insgesamt drei Zeilen."}
:::

## Text ändern und in den Einfügemodus wechseln

Der Operator `c` entfernt den ausgewählten Text und wechselt anschließend in den Einfügemodus, damit du einen Ersatz eingeben kannst:

- `ce`: Bis zum Ende des Wortes ändern.
- `c$`: Bis zum Ende der Zeile ändern.
- `cc`: Die gesamte aktuelle Zeile ändern.
- `ciw`: Das innere Wort unter dem Cursor ändern.
- `caw`: Ein Wort-Textobjekt einschließlich der von Vim festgelegten umgebenden Abstände ändern.

Das Verhalten von `cw` ist historisch bedingt ein Sonderfall und entspricht häufig `ce`. Textobjekte wie `iw` können die beabsichtigte Grenze deutlicher ausdrücken.

:::single-choice{#vim-edit-change-inner-word} Welcher Befehl des Normalmodus ersetzt das innere Wort unter dem Cursor, indem er es löscht und in den Einfügemodus wechselt?

::option[`diw`]{#vim-edit-delete-inner-word explanation="Dieser Befehl löscht das innere Wort, bleibt jedoch im Normalmodus, statt die Eingabe des Ersatztexts zu beginnen."}
::option[`yiw`]{#vim-edit-yank-inner-word explanation="Dieser Befehl kopiert das innere Wort, ohne den Puffer zu verändern oder in den Einfügemodus zu wechseln."}
::option[`ciw`]{#vim-edit-change-inner-word-answer .correct explanation="Der Operator `c` ändert das Textobjekt `iw` und wechselt danach in den Einfügemodus."}
:::

## Text kopieren und einfügen

Vim bezeichnet das Kopieren als **Yanking** und das Einfügen als **Putting**:

- `yw`: Den von einer Wortbewegung erfassten Text kopieren.
- `yy`: Die aktuelle Zeile kopieren.
- `p`: Zeichenweisen Text hinter dem Cursor oder zeilenweisen Text unter der aktuellen Zeile einfügen.
- `P`: Text vor dem Cursor beziehungsweise über der aktuellen Zeile einfügen.

Auch beim Löschen und Ändern wird Text in Registern gespeichert. Daher kann ein späteres `p` den zuletzt gelöschten Text anstelle eines zuvor kopierten Texts einfügen. In benannten Registern kannst du bestimmten Text gezielt aufbewahren. Beobachte am Anfang aber zunächst, was die jeweils letzte Operation gespeichert hat.

:::single-choice{#vim-edit-yank-put-line} Welcher Befehl fügt die mit `yy` kopierte aktuelle Zeile unterhalb der aktuellen Zeile ein?

::option[`p`]{#vim-edit-put-below .correct explanation="Bei zeilenweise kopiertem Text fügt das kleine `p` die gespeicherte Zeile unterhalb der aktuellen Zeile ein."}
::option[`P`]{#vim-edit-put-above explanation="Das große `P` fügt zeilenweisen Text oberhalb der aktuellen Zeile ein."}
::option[`u`]{#vim-edit-undo-not-put explanation="Das kleine `u` macht eine Änderung rückgängig; es fügt die kopierte Zeile nicht ein."}
:::

## Rückgängig machen, wiederholen und erneut anwenden

Im Normalmodus:

- `u`: Die letzte Änderung rückgängig machen.
- `Ctrl+R`: Eine rückgängig gemachte Änderung wiederherstellen.
- `.`: Die letzte Änderung, soweit anwendbar, an der aktuellen Position erneut ausführen.
- `J`: Die aktuelle mit der nächsten Zeile verbinden.

Der Rückgängig-Verlauf gilt für Änderungen am Puffer, nicht für reine Cursorbewegungen. Speichere Zwischenstände und prüfe deine Änderungen, statt dich auf einen unbegrenzten oder dauerhaften Rückgängig-Verlauf zu verlassen.

:::single-choice{#vim-edit-redo-change} Welcher Befehl des Normalmodus stellt eine soeben rückgängig gemachte Änderung wieder her?

::option[`Ctrl+U`]{#vim-edit-control-u explanation="Im Normalmodus scrollt `Ctrl+U` ungefähr einen halben Bildschirm nach oben; es ist kein Wiederherstellen-Befehl."}
::option[`.`]{#vim-edit-dot-repeat explanation="Der Punkt führt die letzte Änderung als neue Aktion erneut aus, statt im Rückgängig-Verlauf vorwärtszugehen."}
::option[`Ctrl+R`]{#vim-edit-control-r .correct explanation="Mit `Ctrl+R` gehst du in Vims Rückgängig-Verlauf im Normalmodus wieder vorwärts."}
:::

In diesem praktischen Lab kannst du Operatoren, Bewegungen und die Wiederherstellung an entbehrlichem Text üben:

1. **[Textdateien unter Linux mit Vim und Nano bearbeiten](https://labex.io/labs/comptia-edit-text-files-in-linux-with-vim-and-nano-591076)** – Übe, Dateien anzulegen, Text zu bearbeiten und zu speichern sowie mit vi/vim und nano zu navigieren. Das Lab hilft dir, das Löschen, Ändern, Kopieren und Einfügen von Text in realistischen Situationen anzuwenden.

## Zusammenfassung

Du kannst nun im Normalmodus Bearbeitungsbefehle zusammensetzen und dich von Fehlern erholen.

1. Kombiniere Operatoren mit Bewegungen, Textobjekten und Zählern.
2. Lösche Zeichen oder vollständige Zeilen im gewünschten Umfang.
3. Ändere Text und wechsle zur Eingabe des Ersatzes in den Einfügemodus.
4. Kopiere und füge zeichen- oder zeilenweisen Text ein.
5. Mache Änderungen gezielt rückgängig, stelle sie wieder her oder führe sie erneut aus.
