---
lesson_id: "file-command"
course_id: "command-line"
lang: "de"
order_index: 6
title: "file"
description: "Lerne, den wahrscheinlichen Inhaltstyp einer Datei unabhängig von ihrem Namen oder ihrer Endung zu bestimmen."
meta_title: "file - Kommandozeile"
meta_description: "Lernen Sie den Linux-Befehl file mit Beispielen zur Identifikation von Textdateien, Bildern, Skripten, komprimierten Archiven, Binärdateien und MIME-Typen."
meta_keywords: "linux file befehl, file befehl, dateityp erkennen linux, mime typ linux, textdatei, binärdatei, archivdatei"
---

In der vorherigen Lektion hast du mit `touch` eine Datei ohne Erweiterung erstellt. Unter Linux muss ein Dateiname nicht verraten, was eine Datei enthält: Eine Datei namens `funny.gif` ist nicht zwangsläufig ein GIF-Bild.

Mit `file` untersuchst du eine Datei und lässt dir ihren wahrscheinlichen Typ melden:

```bash
$ file banana.jpg
banana.jpg: JPEG image data
```

## Warum Dateiendungen nicht ausreichen

Linux-Werkzeuge benötigen normalerweise keine Dateiendung, um den Dateityp zu bestimmen. Ein Shell-Skript kann `backup`, eine Textdatei `README` heißen und ein Bild kann eine irreführende Endung besitzen. `file` untersucht unter anderem Metadaten des Dateisystems und erkennbare Muster im Inhalt.

```bash
$ file README
README: ASCII text
$ file /bin/ls
/bin/ls: ELF 64-bit LSB executable
```

Das Ergebnis ist eine Klassifizierung, keine Garantie. Bei ungewöhnlichen, unvollständigen oder beschädigten Dateien liefert file möglicherweise nur eine allgemeine Beschreibung wie `data`.

:::single-choice{#identify-misleading-extension} Eine Datei namens `report.jpg` enthält möglicherweise kein Bild. Welcher Befehl prüft ihren wahrscheinlichen Inhaltstyp?

::option[`ls report.jpg`]{#list-report explanation="`ls` bestätigt den Namen und kann Metadaten anzeigen, klassifiziert aber nicht den Dateiinhalt."}
::option[`file report.jpg`]{#inspect-report .correct explanation="`file` untersucht die Datei und meldet einen wahrscheinlichen Typ. Der Befehl verlässt sich nicht nur auf die Endung `.jpg`."}
::option[`touch report.jpg`]{#touch-report explanation="`touch` aktualisiert Zeitstempel oder erstellt eine fehlende Datei. Der Befehl bestimmt keinen Inhaltstyp."}
:::

## Mehrere Dateien prüfen

Du kannst mehrere Dateien auf einmal untersuchen:

```bash
$ file notes.txt image.png archive.tar.gz
notes.txt: ASCII text
image.png: PNG image data
archive.tar.gz: gzip compressed data
```

Auch ein Shell-Platzhalter ist möglich. Die Shell erweitert `*` zu den passenden Namen, bevor `file` sie untersucht:

```bash
$ file *
```

:::single-choice{#inspect-multiple-files} Welcher Befehl lässt `file` alle nicht versteckten Namen untersuchen, auf die `*` im aktuellen Verzeichnis passt?

::option[`file *`]{#file-wildcard .correct explanation="Die Shell erweitert `*` zu passenden nicht versteckten Namen und `file` untersucht jeden daraus entstehenden Operanden."}
::option[`file .`]{#file-current-directory explanation="Ein einzelner Punkt bezeichnet das aktuelle Verzeichnis selbst. Dieser Befehl klassifiziert das Verzeichnis, nicht jeden Eintrag darin."}
::option[`file -b`]{#file-brief-no-operand explanation="Die Option `-b` ändert die Ausgabeform, doch in diesem Befehl fehlen die zu untersuchenden Dateien."}
:::

## MIME-Informationen anzeigen

Die Option `-i` gibt Informationen im MIME-Stil aus, darunter einen Medientyp und – sofern verfügbar – einen Zeichensatz. Diese Form ist nützlich, wenn ein anderes Programm Werte wie `text/html` erwartet.

```bash
$ file -i index.html
index.html: text/html; charset=us-ascii
```

:::single-choice{#show-mime-information} Welcher Befehl meldet MIME-Informationen für `index.html`?

::option[`file -b index.html`]{#brief-index explanation="Die Option `-b` lässt den Dateinamen in der üblichen Beschreibung weg. Sie fordert nicht ausdrücklich eine MIME-Ausgabe an."}
::option[`file -i index.html`]{#mime-index .correct explanation="Die Option `-i` fordert eine Ausgabe im MIME-Stil an, etwa `text/html` mit Zeichensatzangabe."}
::option[`file -L index.html`]{#follow-index explanation="Die Option `-L` steuert den Umgang mit symbolischen Links. Sie wählt nicht das MIME-Ausgabeformat aus."}
:::

## Nützliche file-Optionen

- `-i`: Zeigt Informationen im MIME-Stil an.
- `-b`: Verwendet den Kurzmodus und lässt den Dateinamen in der Ausgabe weg.
- `-L`: Folgt symbolischen Links und klassifiziert deren Ziele.
- `-z`: Versucht, den Inhalt komprimierter Dateien zu untersuchen.

Zum Beispiel:

```bash
$ file -b notes.txt
ASCII text
```

:::single-choice{#omit-filename-from-output} Welcher Befehl klassifiziert `notes.txt`, lässt aber den Dateinamen in der Ausgabe weg?

::option[`file -i notes.txt`]{#mime-notes explanation="Die Option `-i` fordert MIME-Informationen an. Der Dateiname ist normalerweise weiterhin Teil der Ausgabe."}
::option[`file -z notes.txt`]{#compressed-notes explanation="Die Option `-z` lässt `file` nach Möglichkeit in komprimierte Daten hineinsehen. Sie aktiviert keine Kurzausgabe."}
::option[`file -b notes.txt`]{#brief-notes .correct explanation="Der mit `-b` gewählte Kurzmodus gibt die Klassifizierung ohne vorangestellten Dateinamen aus."}
:::

## Zusammenfassung

Du kannst nun mit `file` untersuchen, was eine Datei wahrscheinlich enthält.

1. Klassifiziere eine Datei, ohne ihrer Endung zu vertrauen.
2. Untersuche mehrere Pfade mit einem Befehl.
3. Fordere Informationen im MIME-Stil an.
4. Steuere den Umgang mit Links, komprimierten Daten und Ausgabebezeichnungen.
