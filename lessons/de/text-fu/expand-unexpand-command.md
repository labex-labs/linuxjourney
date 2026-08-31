---
lesson_id: "expand-unexpand-command"
course_id: "text-fu"
lang: "de"
order_index: 10
title: "Erweitern und Zurücksetzen"
description: "Lerne, wie Tabulatorstopps die Umwandlung zwischen Tabulatoren und Leerzeichen mit expand und unexpand steuern."
meta_title: "Erweitern und Zurücksetzen - Text-Fu"
meta_description: "Beherrschen Sie die Textformatierung unter Linux mit unserem Leitfaden zu den Befehlen expand und unexpand. Erfahren Sie, wie Sie Tabs in Leerzeichen und Leerzeichen wieder in Tabs umwandeln, um konsistente Dateilayouts zu erhalten."
meta_keywords: "expand Befehl, unexpand Befehl, Linux Tabs, Linux Leerzeichen, Textformatierung, Linux Tutorial, Anfänger Linux, Linux Anleitung"
---

Tabulatoren speichern eine Bewegung zum nächsten Tabulatorstopp und keine feste Anzahl sichtbarer Leerzeichen. Ihre dargestellte Breite hängt von der aktuellen Spalte und den Tabulatorstopps ab. `expand` und `unexpand` wandeln unter Berücksichtigung dieser Positionen zwischen Tabulatorzeichen und Leerzeichen um.

## Tabulatoren in Leerzeichen umwandeln

`expand` liest eine Eingabe, ersetzt Tabulatoren durch die zum Erreichen der passenden Tabulatorstopps nötigen Leerzeichen und schreibt das Ergebnis nach stdout:

```bash
$ expand sample.txt
```

Standardmäßig liegen Tabulatorstopps alle 8 Spalten. Ein Tabulator in Spalte 1 wird daher anders erweitert als einer in Spalte 6; er wird nicht immer durch acht Leerzeichen ersetzt.

:::single-choice{#expand-default-tab-stops}
Wie ersetzt `expand` mit Standardeinstellungen ein Tabulatorzeichen?

::option[Der Befehl fügt genügend Leerzeichen bis zum nächsten standardmäßigen Tabulatorstopp ein.]{#expand-next-stop .correct explanation="`expand` erhält die Ausrichtung an Tabulatorstopps, indem es die nötigen Leerzeichen ab der aktuellen Spalte berechnet."}
::option[Der Befehl fügt immer genau acht Leerzeichen ein.]{#expand-eight-spaces explanation="Die Standardstopps liegen acht Spalten auseinander, doch die Anzahl der Leerzeichen hängt von der aktuellen Spalte ab."}
::option[Der Befehl entfernt den Tabulator, ohne Zeichen hinzuzufügen.]{#expand-remove-tab explanation="Der Tabulator wird durch Leerzeichen ersetzt, damit der folgende Text am gewählten Tabulatorstopp ausgerichtet bleibt."}
:::

## Tabulatorstopps wählen

Mit `-t NUMBER` setzt du Tabulatorstopps in Abständen der angegebenen Spaltenzahl. Für Stopps alle vier Spalten:

```bash
$ expand -t 4 sample.txt
```

GNU `expand` akzeptiert außerdem eine kommagetrennte Liste ausdrücklicher Tabulatorpositionen. Mit `-i` werden nur Tabulatoren vor dem ersten Nicht-Leerzeichen jeder Zeile umgewandelt.

:::single-choice{#expand-four-column-stops}
Welcher Befehl wandelt Tabulatoren mit Stopps alle vier Spalten um?

::option[`expand -i 4 sample.txt`]{#expand-initial-four explanation="Die Option `-i` beschränkt die Umwandlung auf anfängliche Tabulatoren und verwendet `4` nicht als Stoppabstand."}
::option[`unexpand -t 4 sample.txt`]{#unexpand-tabs-four explanation="`unexpand` wandelt passende Leerzeichen in Tabulatoren um und arbeitet damit in die entgegengesetzte Richtung."}
::option[`expand -t 4 sample.txt`]{#expand-tabs-four .correct explanation="Die Option `-t` legt den Abstand der Tabulatorstopps fest; `4` fordert Stopps alle vier Spalten an."}
:::

## Umgewandelte Ausgabe sicher speichern

`expand` bearbeitet die Eingabedatei nicht. Leite stdout an einen anderen Pfad um, wenn du den umgewandelten Text speichern möchtest:

```bash
$ expand sample.txt > result.txt
```

Verwende nicht `expand sample.txt > sample.txt`. Die Shell leert das Ziel, bevor `expand` es lesen kann, sodass die Quelldaten verloren gehen können. Nach Prüfung eines getrennt geschriebenen Ergebnisses kannst du das Original bewusst mit einem geeigneten Dateiverwaltungsschritt ersetzen.

:::single-choice{#expand-safe-output-file}
Welcher Befehl speichert den erweiterten Text, ohne `sample.txt` vor dem Lesen zu leeren?

::option[`expand sample.txt > sample.txt`]{#expand-same-file explanation="Die Shell öffnet und leert `sample.txt` für die Ausgabe, bevor sie `expand` startet, und kann dadurch die Eingabe löschen."}
::option[`expand sample.txt > result.txt`]{#expand-separate-result .correct explanation="Eingabe- und Ausgabepfad unterscheiden sich, sodass die Shell `result.txt` erstellen kann, ohne die Quelle zu zerstören."}
::option[`> sample.txt expand result.txt`]{#expand-leading-redirection explanation="Auch diese Form leert `sample.txt` und beschreibt keine sichere Umwandlung aus der ursprünglichen Datei."}
:::

## Leerzeichen in Tabulatoren umwandeln

`unexpand` ersetzt geeignete Leerzeichen durch Tabulatoren und erhält dabei die Ausrichtung an den gewählten Tabulatorstopps. Standardmäßig wandelt GNU `unexpand` nur anfängliche Leerzeichen vor dem ersten Nicht-Leerzeichen einer Zeile um:

```bash
$ unexpand result.txt
```

Mit `-a` werden geeignete Leerzeichen in der gesamten Zeile berücksichtigt:

```bash
$ unexpand -a result.txt
```

Dabei wird nicht einfach jede Folge aus acht Leerzeichen ersetzt. Wie bei `expand` hängt die Umwandlung von Spaltenpositionen und Tabulatorstopps ab. Verwende `-t 4` oder eine andere Stoppangabe, wenn die Datei einer abweichenden Konvention folgt.

:::single-choice{#unexpand-default-scope}
Welche Leerzeichen berücksichtigt GNU `unexpand` ohne `-a` normalerweise zur Umwandlung?

::option[Jede Gruppe von Leerzeichen an beliebiger Stelle der Datei.]{#unexpand-every-group explanation="Für Leerzeichen in der gesamten Zeile ist `-a` nötig; auch dann hängt die Umwandlung von den Tabulatorpositionen ab."}
::option[Nur Leerzeichen nach dem letzten Wort.]{#unexpand-trailing-blanks explanation="Der Standardbereich betrifft anfängliche Leerzeichen und nicht speziell nachgestellte Leerzeichen."}
::option[Nur anfängliche Leerzeichen vor dem ersten Nicht-Leerzeichen.]{#unexpand-initial-blanks .correct explanation="GNU `unexpand` beschränkt sich standardmäßig auf führende Leerzeichen jeder Zeile."}
:::

:::single-choice{#unexpand-all-blanks}
Welche Option weist GNU `unexpand` an, auch Leerzeichen nach dem ersten Nicht-Leerzeichen zu berücksichtigen?

::option[`-i`]{#unexpand-initial-option explanation="Bei `expand` beschränkt `-i` die Arbeit auf anfängliche Tabulatoren. Für `unexpand` ist es nicht die Option für alle Leerzeichen."}
::option[`-a`]{#unexpand-all-option .correct explanation="Die Option `-a` aktiviert die Umwandlung geeigneter Leerzeichen in der gesamten Eingabezeile."}
::option[`-t`]{#unexpand-tab-list-option explanation="Die Option `-t` legt Tabulatorstopps fest. Auch wenn sie bei GNU breiteres Verhalten einschließen kann, fordert `-a` ausdrücklich alle Leerzeichen an."}
:::

Ohne benannte Datei lesen beide Befehle von stdin und eignen sich daher für Pipelines. Beachte, dass eine Umwandlung in Leerzeichen und zurück die ursprüngliche Wahl zwischen Tabulatoren und Leerzeichen nicht unbedingt rekonstruiert, auch wenn die sichtbare Ausrichtung gleich bleibt.

## Zusammenfassung

Du kannst nun Tabulatoren und Leerzeichen unter Erhalt der Tabulatorstopp-Ausrichtung umwandeln.

1. Erweitere Tabulatoren bis zum nächsten konfigurierten Stopp.
2. Setze eigene Tabulatorstopps mit `-t`.
3. Speichere die Ausgabe in einer anderen Datei, bevor du eine Eingabe ersetzt.
4. Wandle mit `unexpand` standardmäßig führende Leerzeichen um.
5. Verwende `-a`, wenn Leerzeichen in der gesamten Zeile berücksichtigt werden sollen.
