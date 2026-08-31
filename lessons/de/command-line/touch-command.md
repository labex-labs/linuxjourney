---
lesson_id: "touch-command"
course_id: "command-line"
lang: "de"
order_index: 5
title: "touch"
description: "Lerne, mit touch leere Dateien zu erstellen und Dateizeitstempel zu verwalten."
meta_title: "touch - Kommandozeile"
meta_description: "Lernen Sie den Linux-Befehl touch mit Beispielen zum Erstellen leerer Dateien, Aktualisieren von Zeitstempeln, Setzen von Daten, Verwenden von Referenzdateien und Vermeiden von Überschreibungen."
meta_keywords: "linux touch befehl, touch befehl, datei erstellen linux, zeitstempel aktualisieren linux, touch -d, touch -r, touch -c"
---

Der Befehl `touch` ändert Dateizeitstempel. Außerdem wird er häufig verwendet, um eine oder mehrere leere Dateien anzulegen.

Die grundlegende Syntax lautet:

```bash
touch [OPTIONS] FILE...
```

## Leere Dateien erstellen

Existiert die angegebene Datei noch nicht, erstellt `touch` sie als leere Datei:

```bash
$ touch mysuperduperfile
```

Du kannst mehrere Dateien in einem Befehl erstellen, indem du ihre Namen nacheinander angibst:

```bash
$ touch file1.txt file2.txt file3.log
```

Das ist praktisch für Platzhalter. `touch` fügt einer Datei jedoch keinen Text hinzu. Für eine nicht leere Datei benötigst du einen Texteditor oder einen anderen Befehl, der Inhalte schreibt.

:::single-choice{#create-several-empty-files}
Welcher Befehl erstellt drei leere Dateien namens `one`, `two` und `three`, sofern sie noch nicht existieren?

::option[`touch "one two three"`]{#touch-one-spaced explanation="Durch die Anführungszeichen entsteht ein einzelner Dateiname mit Leerzeichen. Der Befehl bezieht sich daher auf eine statt auf drei Dateien."}
::option[`mkdir one two three`]{#mkdir-three explanation="`mkdir` erstellt Verzeichnisse und keine leeren regulären Dateien. Für die verlangten Dateien verwendest du `touch`."}
::option[`touch one two three`]{#touch-three .correct explanation="`touch` akzeptiert mehrere Dateioperanden. Jede fehlende Datei wird erstellt, ohne Inhalt einzufügen."}
:::

## Dateizeitstempel aktualisieren

Dateien speichern mehrere Zeitstempel. Wird `touch` ohne weitere Optionen auf eine vorhandene Datei angewendet, setzt der Befehl sowohl ihre Zugriffs- als auch ihre Änderungszeit auf die aktuelle Zeit. Der Dateiinhalt bleibt unverändert.

Du kannst die angezeigte Änderungszeit vor und nach dem Befehl vergleichen:

```bash
$ ls -l mysuperduperfile
$ touch mysuperduperfile
$ ls -l mysuperduperfile
```

Die Ausgabe von `ls -l` zeigt normalerweise die Änderungszeit, nicht die Zugriffszeit.

:::single-choice{#touch-existing-file}
Was geschieht bei `touch report.txt`, wenn `report.txt` bereits existiert?

::option[Die Zeitstempel werden aktualisiert, ohne den Inhalt zu ersetzen.]{#timestamps-only .correct explanation="Standardmäßig aktualisiert `touch` die Zugriffs- und Änderungszeit einer vorhandenen Datei. Die gespeicherten Daten werden nicht überschrieben."}
::option[Der Inhalt wird gelöscht und die Datei wird geleert.]{#contents-deleted explanation="Eine leere Datei wird nur angelegt, wenn sie fehlt. Bei einer vorhandenen Datei aktualisiert `touch` die Zeitstempel und erhält den Inhalt."}
::option[Der Befehl schlägt fehl, weil der Dateiname bereits verwendet wird.]{#existing-error explanation="`touch` ist sowohl für vorhandene als auch für fehlende Dateien vorgesehen. Ein bestehender Name ist allein kein Fehler."}
:::

## Den zu ändernden Zeitstempel auswählen

Mit `-a` änderst du nur die Zugriffszeit, mit `-m` nur die Änderungszeit:

```bash
$ touch -a notes.txt
$ touch -m notes.txt
```

:::single-choice{#change-modification-time-only}
Welcher Befehl aktualisiert ausschließlich die Änderungszeit von `notes.txt`?

::option[`touch -a notes.txt`]{#access-only explanation="Die Option `-a` ändert nur die Zugriffszeit. Sie wählt nicht die hier verlangte Änderungszeit aus."}
::option[`touch -m notes.txt`]{#modification-only .correct explanation="Die Option `-m` beschränkt die Änderung auf die Änderungszeit. Die Zugriffszeit bleibt unverändert."}
::option[`touch -c notes.txt`]{#no-create explanation="Die Option `-c` steuert, ob eine fehlende Datei angelegt wird. Sie beschränkt die Aktualisierung nicht auf einen bestimmten Zeitstempel."}
:::

## Eine Zeit setzen oder kopieren

Mit der Option `-d` gibst du statt der aktuellen Zeit eine Datumszeichenfolge an:

```bash
$ touch -d "2026-06-23 12:30:00" mysuperduperfile
```

Mit `-r` übernimmst du die Zugriffs- und Änderungszeit einer Referenzdatei:

```bash
$ touch -r file1.txt file2.txt
```

Hier liefert `file1.txt` die Zeitstempel, während `file2.txt` geändert wird. Mit `-t` kannst du eine Zeit außerdem in einem kompakten numerischen Format angeben.

:::single-choice{#copy-reference-timestamps}
Welcher Befehl kopiert die Zeitstempel von `source.txt` nach `target.txt`?

::option[`touch -r source.txt target.txt`]{#reference-source .correct explanation="Bei `-r` ist der nächste Operand die Referenzdatei; der letzte Operand bezeichnet die Datei, deren Zeitstempel aktualisiert werden."}
::option[`touch -r target.txt source.txt`]{#reference-target explanation="Damit wären die Rollen vertauscht: `target.txt` würde als Referenz dienen und `source.txt` würde aktualisiert."}
::option[`touch -d source.txt target.txt`]{#date-source explanation="Die Option `-d` erwartet eine Datumszeichenfolge und keinen Referenzdateinamen. Zum Kopieren von Zeitstempeln dient `-r`."}
:::

## Das Erstellen einer Datei verhindern

Normalerweise erstellt `touch` eine Datei, wenn der angegebene Pfad nicht existiert. Verwende `-c`, wenn eine Datei nur dann aktualisiert werden soll, wenn sie bereits vorhanden ist:

```bash
$ touch -c existing-file.txt
```

Fehlt `existing-file.txt`, legt dieser Befehl sie nicht an. Dieses Verhalten ist in Skripten hilfreich, die einen Zeitstempel aktualisieren sollen, ohne versehentlich eine neue Datei zu erzeugen.

:::single-choice{#update-without-creating}
Welcher Befehl aktualisiert `status.log`, falls die Datei existiert, legt sie aber nicht an, wenn sie fehlt?

::option[`touch -a status.log`]{#touch-access explanation="Die Option `-a` wählt die Zugriffszeit aus, eine fehlende Datei kann aber weiterhin angelegt werden. Sie verhindert das Erstellen nicht."}
::option[`touch -m status.log`]{#touch-modification explanation="Die Option `-m` wählt die Änderungszeit aus, verhindert jedoch nicht das Anlegen einer fehlenden Datei. Dafür dient `-c`."}
::option[`touch -c status.log`]{#touch-no-create .correct explanation="Die Option `-c` unterdrückt das Erstellen einer fehlenden Datei. Bei einer vorhandenen Datei können die Zeitstempel weiterhin aktualisiert werden."}
:::

## Zusammenfassung

Du kannst nun mit `touch` leere Dateien erstellen und Dateizeitstempel gezielt steuern.

1. Erstelle eine oder mehrere leere Dateien.
2. Aktualisiere Zeitstempel, ohne Dateiinhalte zu verändern.
3. Wähle Zugriffs- oder Änderungszeit gezielt aus.
4. Setze eine bestimmte Zeit oder kopiere die Zeitstempel einer Referenzdatei.
5. Verhindere das Erstellen einer fehlenden Datei.
