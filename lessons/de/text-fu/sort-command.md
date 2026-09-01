---
lesson_id: "sort-command"
course_id: "text-fu"
lang: "de"
order_index: 12
title: "sort"
description: "Lerne, Textzeilen mit sort lexikalisch, numerisch oder nach ausgewählten Feldern zu ordnen."
meta_title: "sort - Text-Fu"
meta_description: "Erfahren Sie, wie Sie den Linux-Befehl sort zum Sortieren von Textdateien verwenden. Entdecken Sie Optionen wie umgekehrte und numerische Sortierung. Verbessern Sie Ihre Linux-Befehlszeilenkenntnisse!"
meta_keywords: "Linux sort Befehl, sort -r, sort -n, Linux Tutorial, Befehlszeile, Linux für Anfänger, sort Anleitung"
---

Der Befehl `sort` liest vollständige Zeilen, ordnet sie nach gewählten Vergleichsregeln und schreibt das Ergebnis nach stdout. Eine Eingabedatei wird nur verändert, wenn du ausdrücklich eine Ausgabeoperation dafür wählst.

## Vollständige Zeilen sortieren

Betrachte `animals.txt`:

```text
dog
cow
cat
elephant
bird
```

Sortiere die Zeilen aufsteigend:

```bash
$ sort animals.txt
bird
cat
cow
dog
elephant
```

Die Textreihenfolge richtet sich nach der aktuellen Locale, was Großschreibung, Akzente und Satzzeichen beeinflussen kann. Verwende eine einheitliche Locale wie `LC_ALL=C`, wenn ein Skript eine reproduzierbare byteorientierte Kollation benötigt:

```bash
$ LC_ALL=C sort animals.txt
```

:::single-choice{#sort-lines-ascending} Was bewirkt `sort animals.txt` ohne Schlüssel- oder Zahlenoption?

::option[Der Befehl ordnet vollständige Eingabezeilen nach der aktuellen Locale.]{#sort-locale-lines .correct explanation="Standardmäßig vergleicht `sort` ganze Zeilen nach den Kollationsregeln der aktiven Locale."}
::option[Der Befehl ordnet Wörter innerhalb jeder Zeile, behält aber die Zeilenreihenfolge bei.]{#sort-words-within-lines explanation="`sort` behandelt jede Zeile als Datensatz und ordnet keine Wörter innerhalb einzelner Zeilen neu."}
::option[Der Befehl überschreibt `animals.txt` automatisch an Ort und Stelle.]{#sort-auto-rewrite explanation="Das sortierte Ergebnis wird standardmäßig nach stdout geschrieben; die Eingabedatei bleibt unverändert."}
:::

## Das Ergebnis umkehren

Mit `-r` kehrst du das Vergleichsergebnis um:

```bash
$ sort -r animals.txt
elephant
dog
cow
cat
bird
```

:::single-choice{#sort-reverse-order} Welcher Befehl sortiert `animals.txt` in umgekehrter Reihenfolge?

::option[`sort -n animals.txt`]{#sort-numeric-animals explanation="Die Option `-n` fordert einen numerischen Vergleich an. Für eine umgekehrte Reihenfolge steht sie nicht."}
::option[`sort -u animals.txt`]{#sort-unique-animals explanation="Die Option `-u` unterdrückt doppelte Schlüssel. Die Ausgabe wird dadurch nicht umgekehrt."}
::option[`sort -r animals.txt`]{#sort-reverse-animals .correct explanation="Die Option `-r` kehrt die von den übrigen Vergleichsregeln bestimmte Reihenfolge um."}
:::

## Zahlen vergleichen

Eine lexikalische Reihenfolge vergleicht Zeichen, weshalb `10` normalerweise vor `2` steht. Verwende `-n` für einen gewöhnlichen numerischen Vergleich:

```bash
$ printf '10\n2\n30\n' | sort -n
2
10
30
```

Kombiniere Optionen bei Bedarf. `sort -nr scores.txt` vergleicht numerisch und setzt größere Werte zuerst.

:::single-choice{#sort-numbers-descending} Welcher Befehl sortiert numerische Zeilen in `scores.txt` vom größten zum kleinsten Wert?

::option[`sort -n scores.txt`]{#sort-numeric-ascending explanation="Der numerische Vergleich ist gewählt, doch die Standardrichtung setzt kleinere Werte zuerst."}
::option[`sort -nr scores.txt`]{#sort-numeric-reverse .correct explanation="`-n` wählt den numerischen Vergleich; `-r` kehrt ihn um und erzeugt eine absteigende Zahlenreihenfolge."}
::option[`sort -r scores.txt`]{#sort-lexical-reverse explanation="Dieser Befehl kehrt die Textkollation um, fordert aber keinen Zahlenvergleich an. Werte wie `10` und `2` können dadurch unerwartet sortiert werden."}
:::

## Nach einem Feld sortieren

Mit `-k START[,END]` wählst du einen Schlüssel. Standardmäßig werden Felder durch Folgen von Leerraum getrennt. Für durch Doppelpunkte getrennte Datensätze verwendest du `-t ':'`:

```bash
$ printf 'alice:30\nbob:8\ncarol:20\n' | sort -t ':' -k 2,2n
bob:8
carol:20
alice:30
```

Hier legt `-t ':'` das Trennzeichen fest, `-k 2,2` begrenzt den Schlüssel auf Feld 2 und das angehängte `n` vergleicht diesen Schlüssel numerisch. Ohne das abschließende `,2` reicht ein bei Feld 2 beginnender Schlüssel normalerweise bis zum Zeilenende.

:::single-choice{#sort-second-colon-field} Welcher Befehl sortiert `users.txt` numerisch und ausschließlich nach dem zweiten durch Doppelpunkte getrennten Feld?

::option[`sort -n -k 1,1 users.txt`]{#sort-first-blank-field explanation="Dieser Befehl verwendet die standardmäßigen leerraumgetrennten Felder und wählt Feld 1 statt des zweiten Doppelpunktfelds."}
::option[`cut -d ':' -f 2 users.txt`]{#cut-second-user-field explanation="`cut` extrahiert Feld 2, sortiert aber die ursprünglichen Datensätze nicht nach diesem Schlüssel."}
::option[`sort -t ':' -k 2,2n users.txt`]{#sort-colon-field-two .correct explanation="Der Doppelpunkt legt die Feldgrenzen fest, `2,2` beschränkt den Schlüssel auf Feld 2 und `n` wählt dafür den numerischen Vergleich."}
:::

## Duplikate entfernen und Ausgabe speichern

Mit `-u` gibst du für jeden gleichen Vergleichsschlüssel nur eine Zeile aus:

```bash
$ sort -u names.txt
```

Damit wird gleichzeitig sortiert und nach den gewählten Vergleichsregeln dedupliziert. Möchtest du nur benachbarte Duplikate aus bereits sortierten Daten entfernen, eignet sich der später behandelte Befehl `uniq`.

Soll das Ergebnis in eine andere Datei geschrieben werden, genügt eine gewöhnliche Umleitung:

```bash
$ sort names.txt > names-sorted.txt
```

Führe nicht `sort names.txt > names.txt` aus; die Shell leert die Eingabe, bevor `sort` sie liest. GNU `sort -o names.txt names.txt` verwaltet die eigene Ausgabe sicher, wenn du bewusst denselben Pfad verwenden möchtest:

```bash
$ sort -o names.txt names.txt
```

Bewahre eine Sicherung auf oder schreibe und prüfe zunächst ein separates Ergebnis, wenn die Originaldaten wichtig sind.

:::single-choice{#sort-safe-same-file} Welcher Befehl weist `sort` unter GNU/Linux an, das sortierte Ergebnis sicher nach `names.txt` zurückzuschreiben, ohne dass eine Shell-Umleitung die Datei zuvor leert?

::option[`sort -o names.txt names.txt`]{#sort-output-same-file .correct explanation="GNU `sort` verwaltet die Ausgabe mit `-o` nach dem nötigen Lesen selbst; die Shell leert die Eingabe nicht vorab durch `>`."}
::option[`sort names.txt > names.txt`]{#sort-redirection-same-file explanation="Die Shell leert `names.txt`, bevor sie `sort` startet, sodass die Eingabe verloren gehen kann."}
::option[`sort -u names.txt`]{#sort-unique-stdout explanation="Dieser Befehl schreibt eindeutige sortierte Zeilen nach stdout und lässt die Eingabedatei unverändert."}
:::

Mit diesen Übungen kannst du zeilenorientierte Daten praktisch ordnen und analysieren:

1. **[Linux sort Befehl: Textsortierung](https://labex.io/de/labs/linux-linux-sort-command-text-sorting-219196)** – Sortiere mit `sort` Textzeilen auf verschiedene Arten, darunter auf- und absteigend.
2. **[Wortzählung und Sortierung](https://labex.io/de/labs/linux-word-count-and-sorting-388125)** – Kombiniere Sortierung und Wortzählung, um Textdaten zu analysieren und häufige Muster zu finden.

## Zusammenfassung

Du kannst nun Vergleichsregeln und Ziele für sortierten Text auswählen.

1. Sortiere vollständige Zeilen unter einer ausdrücklichen Locale, wenn Reproduzierbarkeit wichtig ist.
2. Kehre Ergebnisse mit `-r` um.
3. Vergleiche Zahlenwerte mit `-n`.
4. Wähle mit `-t` und `-k` einen begrenzten Feldschlüssel.
5. Entferne Duplikate oder speichere Ausgaben, ohne die Eingabe zu leeren.
