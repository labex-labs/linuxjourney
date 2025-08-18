---
lang: "de"
title: "regex (Reguläre Ausdrücke)"
meta_title: "regex (Reguläre Ausdrücke) - Fortgeschrittenes Text-Fu"
meta_description: "Lernen Sie reguläre Ausdrücke (regex) für das Musterabgleich in Linux. Verstehen Sie die Regex-Syntax wie ^, $, ., und [] für die Textmanipulation. Verbessern Sie Ihre grep-Fähigkeiten!"
meta_keywords: "reguläre Ausdrücke, regex, Linux regex, grep regex, Musterabgleich, regex Tutorial, Linux Befehle, Anfänger"
---

## Lesson Content

Reguläre Ausdrücke sind ein mächtiges Werkzeug für die musterbasierte Auswahl. Sie verwenden spezielle Notationen, ähnlich denen, die wir bereits kennengelernt haben, wie das `*`-Platzhalterzeichen.

Wir werden einige der gängigsten regulären Ausdrücke durchgehen; diese sind in fast jeder Programmiersprache universell einsetzbar.

Wir werden diesen Satz als unseren Test-String verwenden:

```plaintext
sally sells seashells
by the seashore
```

### 1. Zeilenanfang mit ^

```plaintext
^by
would match the line "by the seashore"
```

### 2. Zeilenende mit $

```plaintext
seashore$
would match the line "by the seashore"
```

### 3. Beliebiges einzelnes Zeichen abgleichen mit

```plaintext
b.
would match by
```

### 4. Klammernotation mit [] und ()

Das kann etwas knifflig sein. Klammern ermöglichen es uns, Zeichen anzugeben, die innerhalb der Klammer gefunden werden.

```plaintext
d[iou]g
would match: dig, dog, dug
```

Der vorherige Anker-Tag `^`, wenn er in einer Klammer verwendet wird, bedeutet alles außer den Zeichen innerhalb der Klammer.

```plaintext
d[^i]g
would match: dog and dug but not dig
```

Klammern können auch Bereiche verwenden, um die Anzahl der Zeichen zu erhöhen, die Sie verwenden möchten.

```plaintext
d[a-c]g
will match patterns like dag, dbg, and dcg
```

Seien Sie jedoch vorsichtig, da Klammern Groß- und Kleinschreibung beachten:

```plaintext
d[A-C]g
will match dAg, dBg and dCg but not dag, dbg and dcg
```

Und das sind einige grundlegende reguläre Ausdrücke.

## Exercise

Versuchen Sie, reguläre Ausdrücke mit `grep` zu kombinieren und einige Dateien zu durchsuchen.

```bash
grep [regular expression here] [file]
```

## Quiz Question

Welchen regulären Ausdruck würden Sie verwenden, um ein einzelnes Zeichen abzugleichen?

## Quiz Answer

.
