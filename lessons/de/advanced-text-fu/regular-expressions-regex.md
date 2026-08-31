---
lesson_id: "regular-expressions-regex"
course_id: "advanced-text-fu"
lang: "de"
order_index: 1
title: "Regex (Reguläre Ausdrücke)"
description: "Lerne, wie Anker, Zeichensätze, Wiederholungen und Regex-Varianten den Textabgleich steuern."
meta_title: "Regex (Reguläre Ausdrücke) - Fortgeschrittene Text-Fu"
meta_description: "Meistern Sie die Grundlagen von Linux mit unserem Leitfaden zu regulären Ausdrücken (Regex). Lernen Sie Mustererkennung mit grep und verwenden Sie Syntax wie ^, $ und []. Dies ist einer der besten Wege, um Textmanipulation unter Linux zu lernen und Ihre Fähigkeiten zu erweitern."
meta_keywords: "regulärer ausdruck linux, regex, linux grundlagen, mustererkennung, grep, textverarbeitung, linux lernen, linux tutorial, schnellster weg zu fortgeschrittenem linux"
---

Reguläre Ausdrücke, häufig als **Regex** abgekürzt, beschreiben Textmuster. Werkzeuge wie `grep`, `sed` und `awk` verwenden Regex, unterstützen jedoch möglicherweise unterschiedliche Syntax. Ermittle deshalb immer das Werkzeug und die verwendete Regex-Variante.

GNU `grep` verwendet standardmäßig einfache reguläre Ausdrücke (BRE) und mit `-E` erweiterte reguläre Ausdrücke (ERE). Diese Lektion führt zunächst gemeinsame Konstrukte ein und nennt danach verbreitete ERE-Erweiterungen.

Für die Beispiele dient diese Eingabe:

```text
sally sells seashells
by the seashore
```

## Wörtlichen Text abgleichen

Die meisten gewöhnlichen Zeichen stehen für sich selbst. Das Muster `seashells` wählt eine Zeile aus, die genau diese Zeichenfolge an beliebiger Stelle enthält:

```bash
$ grep 'seashells' sample.txt
sally sells seashells
```

Setze Regex-Muster in Anführungszeichen, damit die Shell sie nicht erweitert oder aufteilt, bevor das Werkzeug sie erhält. Regex unterscheidet sich außerdem von der Shell-Pfaderweiterung: In einem regulären Ausdruck wiederholt `*` das vorangehende Element; in einem Shell-Glob ist `*` selbst ein Platzhalter für eine Zeichenfolge in Pfadnamen.

:::single-choice{#regex-versus-shell-star}
Was bewirkt `*` in einem regulären Ausdruck wie `ab*`?

::option[Es passt auf jeden Dateinamen im aktuellen Verzeichnis.]{#regex-shell-glob explanation="Das beschreibt die Pfaderweiterung der Shell in einem Befehlskontext, nicht die Bedeutung von `*` innerhalb eines regulären Ausdrucks."}
::option[Es wiederholt das vorangehende `b` nullmal oder beliebig oft.]{#regex-repeat-b .correct explanation="Ein Regex-Quantifizierer bezieht sich auf das unmittelbar vorangehende Element; `ab*` passt daher auf `a`, `ab`, `abb` und so weiter."}
::option[Es wiederholt die vollständige Zeichenfolge `ab` genau zweimal.]{#regex-repeat-ab-twice explanation="Der Stern bezieht sich nur auf das vorangehende Element und erlaubt null oder mehr Wiederholungen, nicht genau zwei Wiederholungen der gesamten Zeichenfolge."}
:::

## Einen Treffer verankern

Außerhalb eines Klammerausdrucks verankert `^` am Musteranfang den Treffer am Zeilenanfang:

```plaintext
^by
```

Der Anker `$` passt auf das Zeilenende:

```plaintext
seashore$
```

Kombiniere beide Anker, wenn die gesamte Zeile dem Muster entsprechen muss:

```text
^by the seashore$
```

:::single-choice{#regex-complete-line}
Welches Muster passt ausschließlich auf eine Zeile, deren vollständiger Text `by the seashore` lautet?

::option[`^by the seashore$`]{#regex-anchored-line .correct explanation="Das Caret erzwingt den Beginn am Zeilenanfang; das Dollarzeichen erzwingt das Ende mit der Zeile."}
::option[`by the seashore`]{#regex-unanchored-line explanation="Ohne Anker kann diese Zeichenfolge innerhalb einer längeren Zeile mit zusätzlichem Text davor oder danach passen."}
::option[`$by the seashore^`]{#regex-reversed-anchors explanation="Der Endanker kann in diesem beabsichtigten Muster nicht vor dem Text und der Startanker nicht dahinter stehen."}
:::

## Ein Zeichen abgleichen

Der Punkt steht im gewöhnlichen zeilenorientierten Regex-Modus für ein Zeichen:

```plaintext
b.
```

Das passt auf `by`, könnte aber auch `ba` oder `b7` treffen. Auf ein einzelnes `b` passt es nicht, weil danach ein Zeichen erforderlich ist. Einen wörtlichen Punkt schützt du als `\.` oder setzt ihn in einen geeigneten Klammerausdruck.

:::single-choice{#regex-dot-character}
Welche Zeichenfolge wird vom Ganzzeilenmuster `^b.$` nicht getroffen?

::option[`by`]{#regex-dot-by explanation="Der Punkt passt auf `y`; die zwei Zeichen lange Zeichenfolge erfüllt das Muster."}
::option[`b`]{#regex-dot-b .correct explanation="Der Punkt erfordert ein Zeichen nach `b`, doch diese Zeichenfolge endet sofort."}
::option[`b7`]{#regex-dot-b7 explanation="Der Punkt passt auf die Ziffer `7`; die zwei Zeichen lange Zeichenfolge erfüllt das Muster."}
:::

## Klammerausdrücke verwenden

Ein Klammerausdruck passt auf ein Zeichen aus einer angegebenen Menge:

```plaintext
s[ae]lls
```

An dieser Stelle passt das auf `sells` oder `salls`.

Steht `^` als erstes Zeichen nach `[`, negiert es die Menge:

```plaintext
s[^e]lls
```

Das passt auf `salls`, aber nicht auf `sells`, weil das Zeichen hinter dem ersten `s` kein `e` sein darf.

:::single-choice{#regex-negated-bracket}
Worauf passt `[^e]`?

::option[Auf genau ein Zeichen außer `e`.]{#regex-not-e .correct explanation="Ein führendes Caret innerhalb der Klammern bildet das Komplement der aufgeführten Menge; der Ausdruck verbraucht weiterhin genau ein Zeichen."}
::option[Auf den Zeilenanfang, gefolgt von `e`.]{#regex-caret-e-anchor explanation="Innerhalb eines Klammerausdrucks negiert ein führendes Caret die Menge, statt eine Zeile zu verankern."}
::option[Auf null oder mehr Vorkommen des Buchstabens `e`.]{#regex-repeat-e explanation="Für eine Wiederholung wäre ein Quantifizierer wie `*` erforderlich; dieser Klammerausdruck passt auf ein Nicht-`e`-Zeichen."}
:::

Bereiche beschreiben Zeichen zwischen zwei Endpunkten:

```plaintext
d[a-c]g
```

Dies kann auf `dag`, `dbg` oder `dcg` passen. Das Verhalten von Bereichen kann von der Locale-Kollation abhängen. Zeichenklassen wie `[[:lower:]]`, `[[:upper:]]` und `[[:digit:]]` drücken die Absicht häufig klarer aus.

## Muster wiederholen und kombinieren

Sowohl in BRE als auch in ERE bedeutet `*` null oder mehr Wiederholungen des vorangehenden Elements:

```text
seashells*
```

Das passt auf `seashell`, gefolgt von null oder mehr zusätzlichen `s`. Im ERE-Modus mit `grep -E` stehen unter anderem diese Operatoren zur Verfügung:

- `+`: Eine oder mehrere Wiederholungen.
- `?`: Null oder eine Wiederholung.
- `|`: Der linke oder der rechte Ausdruck.
- `(...)`: Gruppiert Ausdrücke.

Zum Beispiel:

```bash
$ grep -E '^(cat|dog)s?$' animals.txt
```

Damit werden vollständige Zeilen `cat`, `cats`, `dog` oder `dogs` ausgewählt. Im BRE-Modus gelten für diese Operatoren andere Maskierungsregeln; übertrage ein Muster daher nicht ungeprüft zwischen Varianten.

:::single-choice{#regex-extended-alternation}
Welcher Befehl aktiviert für das Muster `^(cat|dog)s?$` die erweiterte Regex-Syntax?

::option[`grep -F '^(cat|dog)s?$' animals.txt`]{#regex-fixed-animals explanation="`-F` behandelt alle Regex-Operatoren als wörtlichen Text; Gruppierung, Alternative und optionale Wiederholung sind damit deaktiviert."}
::option[`grep -E '^(cat|dog)s?$' animals.txt`]{#regex-extended-animals .correct explanation="`-E` wählt erweiterte reguläre Ausdrücke und aktiviert die gezeigte Gruppierung, Alternative und das optionale `s`."}
::option[`grep '^(cat|dog)s?$' animals.txt`]{#regex-basic-animals explanation="Standardmäßig verwendet grep BRE; darin besitzen diese ungeschützten Gruppierungs- und Alternativzeichen nicht die beabsichtigte ERE-Bedeutung."}
:::

Mit diesen Übungen kannst du die Auswahl durch reguläre Ausdrücke praktisch trainieren:

1. **[Text mit grep unter Linux suchen](https://labex.io/de/labs/comptia-search-text-with-grep-in-linux-590841)** – Suche mit `grep` nach Text, zeige Zeilennummern an und verwende Anker wie `^` und `$` sowie grundlegende und erweiterte reguläre Ausdrücke.
2. **[Textverarbeitung und reguläre Ausdrücke](https://labex.io/de/labs/linux-text-processing-and-regular-expressions-18003)** – Nutze grep, sed, awk und reguläre Ausdrücke zur effizienten Textverarbeitung und Mustersuche.
3. **[Extrahieren von E-Mails und Zahlen](https://labex.io/de/labs/linux-extracting-mails-and-numbers-17991)** – Extrahiere mit grep und regulären Ausdrücken E-Mail-Adressen und Zahlen aus einer Datei.

## Zusammenfassung

Du kannst nun grundlegende zeilenorientierte reguläre Ausdrücke lesen und erstellen.

1. Unterscheide Regex-Operatoren von Shell-Pfadplatzhaltern.
2. Verankere Treffer am Anfang oder Ende einer Zeile.
3. Gleiche ein Zeichen mit einem Punkt oder Klammerausdruck ab.
4. Negiere Mengen und verwende localeabhängige Zeichenklassen.
5. Wähle BRE- oder ERE-Syntax bewusst.
