---
lesson_id: "emacs-editing"
course_id: "advanced-text-fu"
lang: "de"
order_index: 12
title: "Text in Emacs bearbeiten"
description: "Lerne, den Eingabepunkt zu bewegen, einen Bereich zu aktivieren und Text mit Emacs' Kill-Ring-Befehlen zu bearbeiten."
meta_title: "Text in Emacs bearbeiten – Fortgeschrittenes Text-Fu"
meta_description: "Lerne die Grundlagen der Textbearbeitung in Emacs: Navigiere im Text, markiere Bereiche und schneide, kopiere oder füge Text mit dem Kill Ring ein."
meta_keywords: "Emacs, Emacs Tutorial, Emacs Befehle, Texteditor, Linux Editor, Emacs Navigation, Emacs Anfänger, Emacs Anleitung"
---

Emacs nennt die aktuelle Cursorposition **Eingabepunkt** („point“). Bewegungsbefehle versetzen den Eingabepunkt; Bearbeitungsbefehle fügen Text ein, löschen, „killen“, kopieren oder „yanken“ ihn in seiner Umgebung. In der folgenden Tastennotation steht `C-` für Strg und `M-` für Meta, meist Alt.

## Zeichen- und zeilenweise bewegen

Pfeiltasten und andere Navigationstasten der Plattform funktionieren möglicherweise ebenfalls. Die Standardbefehle von Emacs stehen jedoch sowohl in Terminal- als auch in grafischen Sitzungen zur Verfügung:

- `C-f`: Ein Zeichen vorwärts.
- `C-b`: Ein Zeichen rückwärts.
- `C-n`: In die nächste Zeile.
- `C-p`: In die vorherige Zeile.
- `C-a`: An den Zeilenanfang.
- `C-e`: Ans Zeilenende.

:::single-choice{#emacs-edit-next-line}
Welche Emacs-Taste verschiebt den Eingabepunkt in die nächste Zeile?

::option[`C-p`]{#emacs-edit-previous-line explanation="`C-p` bewegt sich in die entgegengesetzte Richtung zur vorherigen Zeile."}
::option[`C-n`]{#emacs-edit-next-line-answer .correct explanation="`C-n` für „next-line“ bewegt den Eingabepunkt nach unten an die entsprechende Position der nächsten Bildschirmzeile."}
::option[`C-f`]{#emacs-edit-forward-character explanation="`C-f` bewegt sich ein Zeichen vorwärts, nicht in die nächste Zeile."}
:::

## Wortweise und zu Puffergrenzen bewegen

Meta-Befehle bewegen sich über größere Einheiten:

- `M-f`: Ein Wort vorwärts.
- `M-b`: Ein Wort rückwärts.
- `M-<`: An den Anfang des Puffers.
- `M->`: An das Ende des Puffers.

Auf vielen Tastaturen übernimmt Alt die Meta-Funktion. Ist diese Tastenkombination nicht verfügbar, bewirkt das Drücken von `Esc` und danach der betreffenden Taste häufig denselben Meta-Befehl.

:::single-choice{#emacs-edit-buffer-end}
Welche Emacs-Taste verschiebt den Eingabepunkt an das Ende des Puffers?

::option[`C-e`]{#emacs-edit-line-end explanation="`C-e` bewegt sich nur an das Ende der aktuellen Zeile, nicht des gesamten Puffers."}
::option[`M-<`]{#emacs-edit-buffer-start explanation="`M-<` bewegt sich an den Anfang des Puffers."}
::option[`M->`]{#emacs-edit-buffer-end-answer .correct explanation="`M->` verschiebt den Eingabepunkt an das Ende des aktuellen Puffers."}
:::

## Einen Bereich festlegen

Die **Marke** („mark“) ist eine gespeicherte Position im Puffer. Der Text zwischen Eingabepunkt und Marke ist der **Bereich** („region“). Drücke `C-SPC`, in manchen Dokumentationen als `C-space` geschrieben, um `set-mark-command` auszuführen. Bewege danach den Eingabepunkt, um den aktiven Bereich zu erweitern.

In einem Terminal kann `C-SPC` als `C-@` codiert sein. Ob der Bereich hervorgehoben wird, hängt von den Einstellungen für „transient mark“ ab; Eingabepunkt und Marke legen dennoch einen Bereich fest.

:::single-choice{#emacs-edit-set-mark}
Welche Taste beginnt das Festlegen eines Bereichs, indem sie die Marke am Eingabepunkt setzt?

::option[`C-w`]{#emacs-edit-kill-region-before-mark explanation="`C-w` killt einen bereits festgelegten Bereich; es ist nicht der anfängliche Befehl zum Setzen der Marke."}
::option[`C-y`]{#emacs-edit-yank-before-mark explanation="`C-y` fügt Text aus dem Kill Ring ein und beginnt keine Auswahl."}
::option[`C-SPC`]{#emacs-edit-control-space .correct explanation="`set-mark-command` setzt die Marke. Anschließende Bewegungen verändern den Bereich zwischen Marke und Eingabepunkt."}
:::

## Einen Bereich killen oder kopieren

Emacs speichert gekillten und kopierten Text im **Kill Ring**:

- `C-w`: Den aktiven Bereich killen, also entfernen und zum Kill Ring hinzufügen.
- `M-w`: Den aktiven Bereich in den Kill Ring kopieren, ohne ihn zu entfernen.
- `C-k`: Vom Eingabepunkt bis zum Zeilenende killen; bei Wiederholung kann der Zeilenumbruch einbezogen werden.

Killen ist mehr als gewöhnliches Löschen, weil der entfernte Text für späteres Yanken aufbewahrt wird.

:::single-choice{#emacs-edit-copy-region}
Welche Taste kopiert den aktiven Bereich in den Kill Ring, ohne ihn zu entfernen?

::option[`M-w`]{#emacs-edit-copy-active-region .correct explanation="`kill-ring-save`, gebunden an `M-w`, kopiert den Bereich, ohne ihn zu löschen."}
::option[`C-w`]{#emacs-edit-kill-active-region explanation="`C-w` entfernt den Bereich und speichert ihn dabei im Kill Ring."}
::option[`C-k`]{#emacs-edit-kill-line explanation="`C-k` killt Text in Richtung Zeilenende, statt den ausgewählten Bereich unverändert zu kopieren."}
:::

## Aus dem Kill Ring yanken

Mit `C-y` yankst du den neuesten Eintrag des Kill Rings am Eingabepunkt. Unmittelbar nach dem Yanken ersetzt `M-y` den eingefügten Text durch einen älteren Eintrag; wiederholtes `M-y` durchläuft die Einträge.

```text
C-y
M-y
```

Wird nach `C-y` ein anderer, unabhängiger Befehl ausgeführt, besitzt `M-y` nicht mehr denselben „yank-pop“-Kontext.

:::single-choice{#emacs-edit-yank-latest}
Welche Taste fügt den neuesten Eintrag des Kill Rings am Eingabepunkt ein?

::option[`C-y`]{#emacs-edit-yank-answer .correct explanation="`yank`, gebunden an `C-y`, fügt den neuesten Text aus dem Kill Ring in den aktuellen Puffer ein."}
::option[`M-y`]{#emacs-edit-yank-pop explanation="`M-y` ersetzt normalerweise einen soeben eingefügten Eintrag durch einen älteren und benötigt dafür den vorausgehenden Yank-Kontext."}
::option[`C-d`]{#emacs-edit-delete-character explanation="`C-d` löscht das Zeichen nach dem Eingabepunkt und holt keinen Text aus dem Kill Ring."}
:::

Übe in `*scratch*` oder einer entbehrlichen Datei: Bewege den Eingabepunkt, setze die Marke, kopiere einen Bereich, kille einen anderen und yanke beide wieder zurück. Speichere nur, wenn du die entstandene Datei behalten möchtest.

## Zusammenfassung

Du kannst Text in Emacs nun mithilfe von Eingabepunkt, Marke und Kill Ring navigieren und neu anordnen.

1. Bewege dich mit Strg-Befehlen zeichen- oder zeilenweise.
2. Bewege dich mit Meta-Befehlen wortweise oder zu den Puffergrenzen.
3. Setze mit `C-SPC` die Marke, um einen Bereich festzulegen.
4. Kille mit `C-w` oder kopiere mit `M-w`.
5. Yanke mit `C-y` und wechsle unmittelbar danach mit `M-y` durch ältere Einträge.
