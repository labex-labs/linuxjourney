---
lesson_id: "tr-translate-command"
course_id: "text-fu"
lang: "de"
order_index: 13
title: "tr (Übersetzen)"
description: "Lerne, Zeichensätze in einem Standardeingabestrom zu übersetzen, zu löschen und zusammenzuziehen."
meta_title: "tr (Übersetzen) - Text-Fu"
meta_description: "Lerne den Linux-Befehl tr mit Beispielen zum Übersetzen von Zeichen, Löschen von Zeichen, Zusammenziehen von Wiederholungen, Verwendung von Zeichenklassen und Bereinigung von Text."
meta_keywords: "linux tr befehl, tr befehl, tr -d, tr -s, zeichen übersetzen, zeichen löschen, zeichenklassen, textverarbeitung linux"
---

Der Befehl `tr`, kurz für „translate“, übersetzt, löscht oder komprimiert Zeichen, die er von stdin liest. Gewöhnliche Eingabedateioperanden akzeptiert er nicht; stelle Daten daher über eine Pipe oder Eingabeumleitung bereit.

Die grundlegende Syntax lautet:

```bash
tr [OPTIONS] SET1 [SET2]
```

`tr` arbeitet mit Zeichensätzen statt mit Wörtern oder allgemeinen regulären Ausdrücken. Verwende ein anderes Werkzeug, wenn eine Umwandlung von vollständigen Wörtern, der Zeilenstruktur oder dem umgebenden Kontext abhängt.

## Zeichen übersetzen

Bei zwei Sätzen werden Zeichen aus `SET1` positionsgleich auf Zeichen aus `SET2` abgebildet:

```bash
$ echo "hello world" | tr a-z A-Z
HELLO WORLD
```

Hier werden Positionen im Kleinbuchstabenbereich auf die entsprechenden Großbuchstaben abgebildet. Schütze Satzausdrücke durch Anführungszeichen, damit die Shell sie unverändert übergibt.

Du kannst auch einzelne Zeichen übersetzen:

```bash
$ echo "2026-06-23" | tr '-' '/'
2026/06/23
```

```bash
$ echo "abc123" | tr 'abc' 'ABC'
ABC123
```

Zeichen, die nicht in `SET1` vorkommen, bleiben unverändert.

:::single-choice{#tr-map-characters}
Was gibt `printf '%s\n' 'abc123' | tr 'abc' 'ABC'` aus?

::option[`ABCABC`]{#tr-uppercase-digits explanation="Ziffern gehören nicht zum Quellsatz; `tr` ersetzt sie daher nicht durch Buchstaben."}
::option[`ABC123`]{#tr-uppercase-abc .correct explanation="`a`, `b` und `c` werden jeweils auf das Zeichen an derselben Position in `ABC` abgebildet; die Ziffern bleiben unverändert."}
::option[`abc123ABC`]{#tr-append-set explanation="`tr` übersetzt passende Eingabezeichen. Der Zielsatz wird nicht an den Strom angehängt."}
:::

## Zeichen löschen

Mit `-d` und einem Satz entfernst du jedes passende Zeichen:

```bash
$ echo "My address is 123 Main Street" | tr -d '0-9'
My address is  Main Street
```

Jede Ziffer wird unabhängig entfernt; `tr` erkennt dabei kein vollständiges Zahlentoken.

Zeichenklassen können von der aktuellen Locale definierte Gruppen beschreiben:

```bash
$ echo "Hello, world!" | tr -d '[:punct:]'
Hello world
```

Das Löschen von Zeilenumbrüchen verbindet Eingabezeilen, ohne ein Ersatztrennzeichen einzufügen:

```bash
$ printf "one\ntwo\nthree\n" | tr -d '\n'
onetwothree
```

:::single-choice{#tr-delete-digits}
Welcher Befehl entfernt jede Ziffer aus stdin und lässt andere Zeichen unverändert?

::option[`tr -d '[:digit:]'`]{#tr-delete-digit-class .correct explanation="Die Option `-d` löscht alle Zeichen der Ziffernklasse aus dem Eingabestrom."}
::option[`tr -s '[:digit:]'`]{#tr-squeeze-digits explanation="Die Option `-s` komprimiert wiederholte Ziffern, lässt aber ein Zeichen jeder Folge bestehen."}
::option[`tr '[:digit:]'`]{#tr-one-set-no-delete explanation="Für eine Übersetzung ist normalerweise ein zweiter Satz nötig. Ein Satz allein fordert keine Löschung an."}
:::

## Wiederholte Zeichen komprimieren

Mit `-s SET` ersetzt du jede Folge eines aufgeführten Zeichens durch eine einzelne Instanz:

```bash
$ echo "Hello      World,   how   are   you?" | tr -s ' '
Hello World, how are you?
```

Dieser Satz enthält ein gewöhnliches Leerzeichen; Tabulatoren und Zeilenumbrüche werden von diesem Befehl nicht komprimiert.

Auch wiederholte Zeilenumbrüche lassen sich zusammenziehen:

```bash
$ printf "one\n\n\nTwo\n" | tr -s '\n'
one
Two
```

:::single-choice{#tr-squeeze-spaces}
Welcher Befehl reduziert jede Folge gewöhnlicher Leerzeichen in stdin auf ein Leerzeichen?

::option[`tr -s ' '`]{#tr-squeeze-space .correct explanation="Die Option `-s` komprimiert Wiederholungen der Zeichen im angegebenen Satz, der hier ein gewöhnliches Leerzeichen enthält."}
::option[`tr -d ' '`]{#tr-delete-space explanation="Die Option `-d` entfernt alle gewöhnlichen Leerzeichen, statt eines pro Folge zu bewahren."}
::option[`tr ' ' ''`]{#tr-empty-destination explanation="Ein leerer Zielsatz ist keine eindeutige, portable Anforderung zum Komprimieren. Für Wiederholungen dient `-s`."}
:::

## Zeichenklassen und Komplemente verwenden

Zeichenklassen drücken die Absicht in vielen Locales deutlicher aus als selbst geschriebene Bereiche. Häufige Klassen sind:

- `[:lower:]`: Kleinbuchstaben.
- `[:upper:]`: Großbuchstaben.
- `[:digit:]`: Ziffern.
- `[:alpha:]`: Buchstaben.
- `[:alnum:]`: Buchstaben und Ziffern.
- `[:space:]`: Leerraumzeichen.
- `[:punct:]`: Satzzeichen.

So wandelst du Klein- in Großbuchstaben um:

```bash
$ echo "linux journey" | tr '[:lower:]' '[:upper:]'
LINUX JOURNEY
```

Die Option `-c` bildet das Komplement von `SET1`, also alle nicht darin enthaltenen Zeichen. Zusammen mit `-d` kannst du nur bestimmte Zeichenarten bewahren:

```bash
$ echo "user@example.com!" | tr -cd '[:alnum:]'
userexamplecom
```

Auch der Zeilenumbruch wird entfernt, weil er nicht alphanumerisch ist. Ergänze oder bewahre Trennzeichen bewusst, wenn Datensatzgrenzen wichtig sind.

:::single-choice{#tr-keep-alphanumeric}
Was bewirkt `tr -cd '[:alnum:]'` mit stdin?

::option[Alphanumerische Zeichen werden gelöscht, alle anderen bleiben erhalten.]{#tr-delete-alnum explanation="Das Komplement verändert die von `-d` betroffenen Zeichen. Der alphanumerische Satz selbst bleibt erhalten."}
::option[Jedes nicht alphanumerische Zeichen wird gelöscht.]{#tr-delete-nonalnum .correct explanation="`-c` bildet das Komplement des alphanumerischen Satzes; `-d` löscht den daraus entstehenden nicht alphanumerischen Satz."}
::option[Alle Buchstaben und Ziffern werden in Großbuchstaben umgewandelt.]{#tr-uppercase-alnum explanation="Es ist kein Zielzeichensatz vorhanden; eine Umwandlung der Großschreibung findet nicht statt."}
:::

## Stromtransformationen aufbauen

Mehrere `tr`-Prozesse lassen sich verbinden, wenn getrennte Schritte verständlicher sind:

```bash
$ echo "Hello,,,     world!!!" | tr -d '[:punct:]' | tr -s ' '
Hello world
```

Bei einfachen tabulatorgetrennten Daten kannst du Tabulatoren in Kommas übersetzen:

```bash
$ printf "name\tlevel\npete\tbeginner\n" | tr '\t' ','
name,level
pete,beginner
```

Da `tr` stdin liest, kann eine Datei mit `<` bereitgestellt werden:

```bash
$ tr '[:lower:]' '[:upper:]' < names.txt
```

Leite stdout in eine andere Datei um, wenn du das Ergebnis speichern möchtest. Eine Umleitung zurück in den Eingabepfad würde ihn leeren, bevor `tr` ihn liest.

:::single-choice{#tr-read-file-input}
Welcher Befehl lässt `tr` `names.txt` als stdin lesen und Kleinbuchstaben in Großbuchstaben umwandeln?

::option[`tr names.txt '[:lower:]' '[:upper:]'`]{#tr-file-operand explanation="`tr` akzeptiert auf diese Weise keinen gewöhnlichen Eingabedateinamen; der zusätzliche Operand macht die Syntax ungültig."}
::option[`tr -d '[:lower:]' < names.txt`]{#tr-delete-lowercase explanation="Dieser Befehl liest die Datei richtig, löscht Kleinbuchstaben aber, statt sie zu übersetzen."}
::option[`tr '[:lower:]' '[:upper:]' < names.txt`]{#tr-input-redirection .correct explanation="Die Shell öffnet `names.txt` als stdin; `tr` bildet die Kleinbuchstabenklasse auf die Großbuchstabenklasse ab."}
:::

Mit dieser Übung kannst du zeichenweise Stromtransformationen praktisch trainieren:

1. **[Linux tr Command: Character Translating](https://labex.io/de/labs/linux-linux-tr-command-character-translating-219198)** – Transformiere mit `tr` Zeichen in Textströmen, lösche bestimmte Zeichen, verwende Zeichenklassen und fasse Wiederholungen zusammen.

## Zusammenfassung

Du kannst nun Zeichenströme mit gezielten `tr`-Operationen verändern.

1. Bilde Zeichen zwischen positionsgleichen Sätzen ab.
2. Lösche ausgewählte Zeichen mit `-d`.
3. Komprimiere Wiederholungen mit `-s`.
4. Verwende localeabhängige Klassen und Komplemente bewusst.
5. Stelle die Eingabe über stdin statt über einen Dateinamenoperanden bereit.
