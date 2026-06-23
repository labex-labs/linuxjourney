---
index: 11
lang: "de"
title: "mv (Verschieben)"
meta_title: "mv (Verschieben) - Kommandozeile"
meta_description: "Lernen Sie den Linux-Befehl mv mit Beispielen zum Verschieben von Dateien, Umbenennen von Dateien und Verzeichnissen, Verschieben mehrerer Dateien und Vermeidung von Überschreibungen."
meta_keywords: "linux mv befehl, mv befehl, dateien verschieben linux, datei umbenennen linux, verzeichnis umbenennen linux, mv -i, mv -n, mv -t"
---

## Lesson Content

Der Befehl `mv`, kurz für „move“ (verschieben), ist ein grundlegendes Werkzeug in jeder Linux-Umgebung. Er erfüllt zwei Hauptzwecke: Dateien oder Verzeichnisse umzubenennen und sie an einen anderen Ort zu verschieben.

Die grundlegende Syntax lautet:

```bash
mv [OPTIONS] SOURCE DESTINATION
```

Im Gegensatz zu `cp`, das eine Kopie erstellt, ändert `mv` den Speicherort oder den Namen des Originals.

### Dateien und Verzeichnisse umbenennen

Eine der häufigsten Anwendungen von `mv` ist das Umbenennen. Die Syntax ist einfach: Geben Sie den alten Namen und den neuen Namen an.

Um eine Datei umzubenennen:

```bash
$ mv oldfile newfile
```

Das gleiche Prinzip gilt für das Umbenennen von Verzeichnissen:

```bash
$ mv old_directory_name new_directory_name
```

### Dateien und Verzeichnisse verschieben

Die andere Hauptfunktion des Befehls `mv` ist das Verschieben von Elementen von einem Ort zum anderen.

Um eine einzelne Datei in ein anderes Verzeichnis zu verschieben:

```bash
$ mv file2 /home/pete/Documents
```

Sie können auch mehrere Dateien auf einmal verschieben. Listen Sie einfach alle Quelldateien gefolgt vom Zielverzeichnis auf:

```bash
$ mv file_1 file_2 somedirectory/
```

Auf GNU/Linux-Systemen ist eine nützliche Option hierfür `-t`, mit der Sie das Zielverzeichnis zuerst angeben können. Das kann beim Verschieben vieler Dateien übersichtlicher sein.

```bash
$ mv -t somedirectory/ file_1 file_2
```

Im Gegensatz zum Befehl `cp` benötigen Sie keine rekursive Option, um ein Verzeichnis zu verschieben. `mv` behandelt Verzeichnisse standardmäßig.

### Wichtige Optionen für den mv-Befehl

Standardmäßig überschreibt `mv` eine Datei am Zielort ohne Warnung, wenn dort bereits eine Datei mit demselben Namen existiert. Um versehentlichen Datenverlust zu vermeiden, können Sie folgende Optionen verwenden:

- **-i (interaktiv)**: Dies ist eine wichtige Sicherheitsfunktion. Sie fordert Sie zur Bestätigung auf, bevor eine vorhandene Datei überschrieben wird.

  ```bash
  $ mv -i source_file destination_directory
  ```

- **-b (Backup)**: Wenn Sie eine Datei überschreiben möchten, aber die alte Version behalten wollen, erstellt diese Option eine Sicherungskopie der Zieldatei. Die Sicherung wird typischerweise mit einem Tilde-Suffix (`~`) umbenannt.

  ```bash
  $ mv -b file1 directory_with_file1
  ```

- **-v (ausführlich)**: Diese Option lässt den Befehl `mv` anzeigen, was gerade passiert, und zeigt jede verschobene oder umbenannte Datei an.

  ```bash
  $ mv -v file1 file2 somedirectory/
  ```

Eine weitere nützliche Option ist `-n`, was „no clobber“ bedeutet. Sie verhindert das Überschreiben einer bereits vorhandenen Zieldatei.

```bash
$ mv -n source_file destination_directory
```

### Häufige mv-Beispiele

Datei umbenennen:

```bash
$ mv draft.txt final.txt
```

Verzeichnis verschieben:

```bash
$ mv project /home/pete/Documents/
```

Alle Textdateien in einen Ordner verschieben:

```bash
$ mv *.txt notes/
```

Überprüfen Sie mit `ls` die Übereinstimmung von Wildcards, bevor Sie viele Dateien verschieben.

### Häufige Fragen

**Kopiert mv Dateien?** Nein. `mv` verschiebt oder benennt das Originalobjekt um.

**Kann mv Dateien überschreiben?** Ja. Verwenden Sie `mv -i`, um vorher gefragt zu werden, oder `mv -n`, um Überschreibungen zu vermeiden.

**Brauche ich mv -r für Verzeichnisse?** Nein. `mv` verschiebt Verzeichnisse ohne `-r`.

## Exercise

Übung macht den Meister! Praktische Erfahrung ist entscheidend, um Linux-Befehle wie `mv` zu beherrschen. Diese Labs helfen Ihnen, Ihr Verständnis für das Verschieben und Umbenennen von Dateien und Verzeichnissen in einer realen Umgebung zu festigen:

1. **[Linux mv Command: File Moving and Renaming](https://labex.io/de/labs/linux-linux-mv-command-file-moving-and-renaming-209743)** – Üben Sie den Umgang mit dem Befehl `mv`, um Dateien und Verzeichnisse zu verschieben und umzubenennen, einschließlich des Verständnisses seiner verschiedenen Optionen und Verhaltensweisen.
2. **[Organizing Files and Directories](https://labex.io/de/labs/linux-organizing-files-and-directories-387877)** – Wenden Sie Ihr Wissen über `mv` (zusammen mit `cp` und `rm`) in einer praktischen Herausforderung an, um eine Projektstruktur zu organisieren, Dateien zu verschieben und Verzeichnisse aufzuräumen.

Diese Labs helfen Ihnen, die Konzepte in realen Szenarien anzuwenden und Vertrauen im Umgang mit Datei- und Verzeichnisverwaltung mit dem Befehl `mv` zu gewinnen.

## Quiz Question

Wie würden Sie mit dem Befehl `mv` eine Datei namens `cat` in `dog` umbenennen? Bitte geben Sie den vollständigen Befehl an. Hinweis: Die Antwort ist case-sensitiv und sollte in englischer Kleinschreibung eingegeben werden.

## Quiz Answer

mv cat dog
