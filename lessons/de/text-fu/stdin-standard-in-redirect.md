---
lesson_id: "stdin-standard-in-redirect"
course_id: "text-fu"
lang: "de"
order_index: 2
title: "stdin (Standardeingabe)"
description: "Lerne, wie Programme die Standardeingabe lesen und wie Bash diesen Strom mit einer Datei verbindet."
meta_title: "stdin (Standardeingabe) - Text-Fu"
meta_description: "Meistern Sie Linux-Befehlszeilenoperationen, indem Sie lernen, wie man stdin (Standardeingabe) umleitet. Dieser Leitfaden behandelt die Beziehung zwischen stdin und stdout, die Verwendung des '<'-Operators und praktische Beispiele wie 'cat stdin', um Datenströme effektiv zu verwalten."
meta_keywords: "stdin, standardeingabe, stdin umleiten, cat stdin, stdin und stdout, Standardeingabe, Linux-Umleitung, Befehlszeile, Eingabestrom"
---

Die Standardeingabe, abgekürzt **stdin**, ist der Strom, aus dem ein Programm normalerweise eingehende Daten liest. In einem interaktiven Terminal verbindet die Shell stdin üblicherweise mit deiner Terminaleingabe, sodass ein Programm lesen kann, was du tippst.

## Standardeingabe und Dateideskriptor 0

Konventionsgemäß verwenden die drei Standardströme folgende Dateideskriptoren:

- `0`: Standardeingabe (`stdin`)
- `1`: Standardausgabe (`stdout`)
- `2`: Standardfehlerausgabe (`stderr`)

Ein Programm entscheidet selbst, ob und wie es diese Ströme verwendet. Ein Befehl, der stdin liest, wartet häufig auf Terminaleingaben, wenn weder ein Dateioperand noch eine andere Eingabequelle angegeben ist.

:::single-choice{#stdin-descriptor-number}
Welcher Dateideskriptor steht konventionsgemäß für die Standardeingabe?

::option[`0`]{#stdin-fd-zero .correct explanation="Die Standardeingabe ist konventionsgemäß der Dateideskriptor 0."}
::option[`1`]{#stdin-fd-one explanation="Dateideskriptor 1 steht konventionsgemäß für die Standardausgabe, also den Strom für reguläre Ergebnisse."}
::option[`2`]{#stdin-fd-two explanation="Dateideskriptor 2 steht konventionsgemäß für die Standardfehlerausgabe, nicht für die Standardeingabe."}
:::

## Eine Datei nach stdin umleiten

Der Operator `<` weist Bash an, eine Datei zum Lesen zu öffnen und mit der Standardeingabe des Befehls zu verbinden:

```bash
$ cat < peanuts.txt
Hello World
```

Die Shell verarbeitet `< peanuts.txt`; `cat` liest lediglich Dateideskriptor 0. Der Pfad wird `cat` nicht als normaler Dateioperand übergeben.

Existiert die Eingabedatei nicht oder kann sie nicht geöffnet werden, meldet die Shell den Umleitungsfehler und startet den Befehl nicht mit dieser Eingabe.

:::single-choice{#stdin-from-file}
Welcher Befehl lässt `sort` seine Standardeingabe aus `names.txt` lesen?

::option[`sort < names.txt`]{#sort-stdin-file .correct explanation="Bash öffnet `names.txt` zum Lesen und verbindet die Datei über Dateideskriptor 0 mit `sort`."}
::option[`sort > names.txt`]{#stdout-to-names explanation="Ein Größer-als-Zeichen leitet stdout in die Datei um und kann sie leeren. Als Eingabe wird die Datei damit nicht bereitgestellt."}
::option[`sort names.txt >`]{#incomplete-sort-output explanation="Dieser Befehl enthält eine unvollständige Ausgabeumleitung. Die verlangte stdin-Verbindung beschreibt er nicht."}
:::

## Dateioperand und Eingabeumleitung unterscheiden

Einige Befehle akzeptieren sowohl einen Dateinamen als Operand als auch stdin, doch die Ergebnisse können sich geringfügig unterscheiden. Zum Beispiel:

```bash
$ wc -l peanuts.txt
1 peanuts.txt
$ wc -l < peanuts.txt
1
```

Beide Formen zählen die Zeilen derselben Daten. In der ersten kennt `wc` den Dateinamen, weil er als Argument übergeben wurde. In der zweiten erhält der Befehl nur einen Strom auf stdin und kennt deshalb keinen auszugebenden Dateinamen.

:::single-choice{#stdin-not-command-argument}
Warum lässt `wc -l < peanuts.txt` den Namen `peanuts.txt` normalerweise in seiner Ausgabe weg?

::option[`wc` löscht den Dateinamen nach dem Zählen der Zeilen.]{#stdin-delete-name explanation="Der Befehl benennt die Quelldatei weder um noch löscht er sie. Nur die Eingabeverbindung unterscheidet sich."}
::option[Der Operator `<` blendet jedes vom Befehl ausgegebene Wort aus.]{#stdin-hide-words explanation="Eine Eingabeumleitung filtert stdout nicht. Der Dateiname fehlt, weil `wc` ihn nie als Argument erhalten hat."}
::option[Bash stellt die Datei über stdin statt als Dateinamenargument bereit.]{#stdin-no-filename .correct explanation="Die Shell verarbeitet die Umleitung und verbindet die Datei mit Deskriptor 0; `wc` erhält den Pfad daher nicht als Operanden."}
:::

## Ein- und Ausgabeumleitung kombinieren

In einer Befehlszeile kannst du mehrere Ströme umleiten:

```bash
$ cat < peanuts.txt > banana.txt
```

Die Shell richtet zwei unabhängige Verbindungen ein:

1. `< peanuts.txt` öffnet `peanuts.txt` als Standardeingabe von `cat`.
2. `> banana.txt` erstellt oder leert `banana.txt` und verbindet die Datei mit der Standardausgabe von `cat`.

`cat` liest Bytes von stdin und schreibt sie nach stdout, sodass `banana.txt` den Quellinhalt erhält. Zum gewöhnlichen Kopieren einer Datei drückt `cp peanuts.txt banana.txt` die Absicht deutlicher aus; dieses Beispiel veranschaulicht Stromverbindungen.

:::single-choice{#stdin-and-stdout-files}
Welche Datei liefert in `cat < input.txt > output.txt` die Standardeingabe und welche empfängt die Standardausgabe?

::option[`output.txt` liefert stdin; `input.txt` empfängt stdout.]{#stdin-output-stdout-input explanation="Damit werden die Bedeutungen der Umleitungsoperatoren vertauscht. Der Pfeil zeigt bei der Eingabe zum Befehl und bei der Ausgabe zur Datei."}
::option[`input.txt` liefert stdin; `output.txt` empfängt stdout.]{#stdin-input-stdout-output .correct explanation="Die Umleitung `<` öffnet `input.txt` für Deskriptor 0; `>` öffnet `output.txt` für Deskriptor 1."}
::option[Beide Dateien liefern stdin; stdout bleibt mit dem Terminal verbunden.]{#both-stdin explanation="Die beiden Operatoren beeinflussen unterschiedliche Standardströme. `>` leitet stdout vom Terminal weg."}
:::

Mit diesen Übungen kannst du die Umleitung von stdin, stdout und stderr praktisch trainieren:

1. **[Eingabe- und Ausgabeumleitung in Linux](https://labex.io/de/labs/comptia-redirecting-input-and-output-in-linux-590840)** – Steuere Standardausgabe, Standardfehler und Standardeingabe mit Operatoren wie >, >> und 2> sowie dem Befehl tee.
2. **[Datenstromumleitung](https://labex.io/de/labs/linux-data-stream-redirection-17995)** – Verarbeite Eingabe-, Ausgabe- und Fehlerströme, kombiniere Ausgaben und nutze /dev/null für fortgeschrittene Dateioperationen.

## Zusammenfassung

Du kannst nun die Standardeingabe eines Befehls über die Shell mit einer Datei verbinden.

1. Erkenne stdin als Dateideskriptor 0.
2. Leite eine lesbare Datei mit `<` um.
3. Unterscheide einen Dateinamenoperanden von umgeleiteter Eingabe.
4. Kombiniere stdin- und stdout-Umleitungen bewusst.
