---
lesson_id: "copy-cp-command"
course_id: "command-line"
lang: "de"
order_index: 10
title: "cp (Kopieren)"
description: "Lerne, Dateien und Verzeichnisbäume zu kopieren und dabei Überschreibungen sowie erhaltene Attribute zu steuern."
meta_title: "cp (Kopieren) - Kommandozeile"
meta_description: "Lernen Sie den Linux-Befehl cp mit Beispielen zum Kopieren von Dateien, Verzeichnissen, mehreren Dateien, Wildcards, Backups und Optionen wie cp -r, cp -i und cp -p."
meta_keywords: "linux cp befehl, cp befehl, dateien kopieren linux, cp -r, cp -i, cp -p, cp -a, cp -u, rekursives kopieren, linux wildcards"
---

Der Befehl `cp` kopiert Dateien und Verzeichnisse, während die Quelle erhalten bleibt. Seine grundlegende Syntax lautet:

```bash
cp [OPTIONS] SOURCE DESTINATION
```

Du kannst eine Datei an einen anderen Pfad kopieren, mehrere Dateien in ein Verzeichnis übernehmen oder einen vollständigen Verzeichnisbaum rekursiv kopieren.

## Eine Datei kopieren

Gib zuerst die Quelle und danach das Ziel an:

```bash
$ cp mycoolfile /home/pete/Documents/cooldocs
```

Ist `/home/pete/Documents/cooldocs` ein vorhandenes Verzeichnis, wird darin eine Kopie namens `mycoolfile` erstellt. Stattdessen kannst du einen neuen Zieldateinamen angeben:

```bash
$ cp mycoolfile /home/pete/Documents/mycoolfile_backup
```

Im zweiten Beispiel erhält die Kopie den Namen `mycoolfile_backup`.

:::single-choice{#copy-file-under-new-name} Welcher Befehl kopiert `draft.txt` nach `final.txt`, während `draft.txt` erhalten bleibt?

::option[`mv draft.txt final.txt`]{#move-draft explanation="`mv` benennt den ursprünglichen Pfad um oder verschiebt ihn. Die verlangte Quelle bleibt dabei nicht als Kopie erhalten."}
::option[`cp final.txt draft.txt`]{#copy-reversed explanation="Hier sind Quelle und Ziel vertauscht. Der Befehl würde `final.txt` nach `draft.txt` kopieren."}
::option[`cp draft.txt final.txt`]{#copy-draft .correct explanation="`cp` liest `draft.txt` und erstellt oder ersetzt `final.txt`, während die Quelldatei erhalten bleibt."}
:::

## Mehrere Dateien in ein Verzeichnis kopieren

Führe zuerst alle Quellen auf und setze das Zielverzeichnis ans Ende:

```bash
$ cp report.txt notes.txt summary.txt /home/pete/Documents/
```

Bei mehreren Quellen muss das letzte Argument ein Verzeichnis sein.

:::single-choice{#copy-multiple-files} Welcher Befehl kopiert `a.txt` und `b.txt` in das vorhandene Verzeichnis `archive/`?

::option[`cp archive/ a.txt b.txt`]{#destination-first explanation="Bei dieser Form von `cp` gehört das Zielverzeichnis ans Ende. An erster Stelle werden die Operanden anders interpretiert."}
::option[`cp a.txt b.txt archive/`]{#destination-last .correct explanation="Bei mehreren Quellen behandelt `cp` das letzte vorhandene Verzeichnis als gemeinsames Ziel aller vorherigen Dateien."}
::option[`cp a.txt archive/ b.txt`]{#destination-middle explanation="Alle Quelloperanden müssen vor dem Ziel stehen. Das vorhandene Verzeichnis gehört an die letzte Stelle."}
:::

## Dateien mit Platzhaltern auswählen

Die Shell kann Platzhaltermuster zu mehreren Quellpfaden erweitern:

- `*`: Passt auf eine beliebige Zeichenfolge.
- `?`: Passt auf genau ein Zeichen.
- `[]`: Passt auf eines der in den Klammern enthaltenen Zeichen.

So kopierst du beispielsweise alle Namen im aktuellen Verzeichnis, die auf `.jpg` enden, nach `Pictures`:

```bash
$ cp *.jpg /home/pete/Pictures
```

Prüfe die Treffer vor einem umfangreichen Kopiervorgang, besonders wenn das Ziel wichtige Daten enthält:

```bash
$ ls *.jpg
beach.jpg  lunch.jpg  profile.jpg
$ cp *.jpg /home/pete/Pictures
```

:::single-choice{#preview-copy-pattern} Welcher Befehl zeigt vor dem Kopieren die nicht versteckten Namen an, auf die `*.jpg` derzeit passt?

::option[`cp *.jpg`]{#copy-no-destination explanation="Dieser Befehl versucht bei mehreren Treffern ohne eindeutiges Ziel zu kopieren. Er dient nicht als Vorschau."}
::option[`ls *.jpg`]{#list-jpg-matches .correct explanation="Die Shell erweitert für `ls` dasselbe Muster, sodass du die passenden Namen vor dem Kopieren prüfen kannst."}
::option[`file '*.jpg'`]{#quoted-jpg-pattern explanation="Die Anführungszeichen verhindern die Erweiterung des Platzhalters. `file` erhält daher die wörtlichen Zeichen `*.jpg`, nicht die üblichen Treffer."}
:::

## Verzeichnisbäume kopieren

Zum Kopieren eines Verzeichnisses samt aller darunterliegenden Inhalte ist ein rekursiver Vorgang erforderlich. Verwende `-r` oder `-R`:

```bash
$ cp -r Pumpkin/ /home/pete/Documents
```

Damit werden das Verzeichnis `Pumpkin` und alle seine Nachkommen nach `Documents` kopiert.

Auch das große `-R` fordert rekursives Kopieren an:

```bash
$ cp -R website /home/pete/backups/
```

Der Archivmodus `-a` eignet sich für sicherungsähnliche Kopien. Er kopiert rekursiv und erhält Links sowie zahlreiche Dateiattribute:

```bash
$ cp -a project/ project-backup/
```

:::single-choice{#archive-directory-tree} Du möchtest `project/` rekursiv und sicherungsähnlich kopieren und dabei Links sowie zahlreiche Attribute erhalten. Welcher Befehl passt dazu?

::option[`cp -p project/ project-backup/`]{#preserve-directory-only explanation="`-p` erhält ausgewählte Attribute, macht das Kopieren eines Verzeichnisses für sich allein aber nicht rekursiv."}
::option[`cp -u project/ project-backup/`]{#update-directory-only explanation="`-u` steuert anhand des Zielzustands, wann Dateien kopiert werden. Rekursives Kopieren wird dadurch allein nicht aktiviert."}
::option[`cp -a project/ project-backup/`]{#archive-project .correct explanation="Der Archivmodus kopiert rekursiv und erhält Links sowie zahlreiche Attribute für ein sicherungsähnliches Ergebnis."}
:::

## Überschreibungen steuern

Standardmäßig kann `cp` eine vorhandene Zieldatei ersetzen. Mit `-i` lässt du vor dem Überschreiben nachfragen:

```bash
$ cp -i mycoolfile /home/pete/Pictures
cp: overwrite '/home/pete/Pictures/mycoolfile'? n
```

Verwende `-n`, wenn ein vorhandenes Ziel nicht überschrieben werden soll:

```bash
$ cp -n mycoolfile /home/pete/Pictures
```

Die Option `-f` weist GNU `cp` an, ein vorhandenes Ziel zu entfernen und den Kopiervorgang erneut zu versuchen, falls die Datei nicht zum Schreiben geöffnet werden kann. Sie ersetzt keine sorgfältige Zielprüfung. Auch Shell-Aliase können Optionen wie `-i` ergänzen; untersuche eine unerwartete Nachfrage, statt von einer bestimmten Konfiguration auszugehen.

:::single-choice{#skip-existing-destination} Welcher Befehl kopiert `report.txt` nach `backup/`, überspringt aber ein bereits vorhandenes Ziel gleichen Namens?

::option[`cp -n report.txt backup/`]{#no-clobber-report .correct explanation="Die Option `-n` verhindert, dass `cp` eine vorhandene Zieldatei überschreibt."}
::option[`cp -i report.txt backup/`]{#interactive-report explanation="`-i` fragt vor dem Überschreiben nach, sodass das Ergebnis von der Antwort abhängt. Vorhandene Ziele werden nicht automatisch immer übersprungen."}
::option[`cp -f report.txt backup/`]{#force-report explanation="`-f` kann helfen, ein zunächst nicht schreibbares Ziel zu ersetzen. Die Option schützt vorhandene Dateien nicht vor dem Überschreiben."}
:::

## Dateien erhalten oder auffrischen

Mit `-p` erhältst du den Modus, die Eigentümerschaft soweit zulässig und die Zeitstempel der Quelldatei:

```bash
$ cp -p mycoolfile /home/pete/backups/
```

Mit `-u` kopierst du eine Quelle nur dann, wenn das Ziel fehlt oder die Quelle neuer ist:

```bash
$ cp -u *.txt /home/pete/Documents/
```

Weitere gebräuchliche Optionen sind:

- `-f`: Versucht bei Bedarf, das Ziel vor dem erneuten Kopieren zu entfernen.
- `-v`: Zeigt jede Datei beim Kopieren an.

Zum praktischen Üben eignen sich diese Labs:

1. **[Linux cp Command: File Copying](https://labex.io/de/labs/linux-linux-cp-command-file-copying-209744)** – Übe die grundlegende Verwendung, rekursives Kopieren, das Bewahren von Attributen und den Einsatz von Platzhaltern für Dateien und Verzeichnisse.
2. **[Organizing Files and Directories](https://labex.io/de/labs/linux-organizing-files-and-directories-387877)** – Organisiere mit `cp`, `mv` und `rm` eine Projektstruktur, verschiebe Dateien und entferne nicht mehr benötigte Verzeichnisse.

## Zusammenfassung

Du kannst nun Dateien und Verzeichnisbäume kopieren und den Umgang mit Zielen gezielt steuern.

1. Setze Quelloperanden vor das Ziel.
2. Prüfe Platzhaltertreffer vor einem umfangreichen Kopiervorgang.
3. Kopiere Verzeichnisbäume rekursiv oder im Archivmodus.
4. Bestätige, überspringe oder ersetze vorhandene Ziele bewusst.
5. Erhalte Attribute oder kopiere bei Bedarf nur neuere Quellen.
