---
index: 4
lang: "de"
title: "ls (Verzeichnisse auflisten)"
meta_title: "ls (Verzeichnisse auflisten) - Kommandozeile"
meta_description: "Erfahren Sie, wie Sie den leistungsstarken Befehl ls unter Linux verwenden. Diese Anleitung behandelt das Auflisten von Verzeichnisinhalten, das Anzeigen versteckter Dateien mit ls -a, detaillierte Auflistungen mit ls -l und die Verwendung von ls -r zum Umkehren der Sortierung. Eine perfekte Lektion, um den cmd ls zu meistern."
meta_keywords: "ls Befehl, Verzeichnisse auflisten, cmd ls, ls -r Befehl, Befehl ls, linux ls -r, Befehl linux ls, versteckte Dateien, Linux Befehle, Anfänger Linux"
---

## Lesson Content

Nachdem wir nun wissen, wie man sich im Dateisystem bewegt, wie finden wir heraus, was uns zur Verfügung steht? Ohne das richtige Werkzeug ist es, als würde man im Dunkeln navigieren. Glücklicherweise ist der wunderbare `command linux ls` zur Stelle, um Verzeichnisinhalte aufzulisten.

### Grundlegende Verwendung des ls-Befehls

Standardmäßig listet der `ls`-Befehl die Verzeichnisse und Dateien in Ihrem aktuellen Verzeichnis auf. Sie können jedoch auch einen Pfad angeben, um den Inhalt eines anderen Verzeichnisses aufzulisten.

```bash
ls
ls /home/pete
```

Der `command ls` ist ein vielseitiges Werkzeug, das Ihnen detaillierte Informationen über die angezeigten Dateien und Verzeichnisse anzeigen kann.

### Anzeigen versteckter Dateien

Beachten Sie, dass nicht alle Dateien in einem Verzeichnis standardmäßig sichtbar sind. Unter Linux sind Dateinamen, die mit einem Punkt (`.`) beginnen, versteckt. Sie können sie anzeigen, indem Sie den `cmd ls` mit dem Flag `-a` verwenden, was für „all“ (alle) steht.

```bash
ls -a
```

### Detaillierte Informationen abrufen

Ein weiteres wichtiges `ls`-Flag ist `-l` für „long“ (lang). Diese Option liefert eine detaillierte Liste der Dateien im Langformat. Dies zeigt Ihnen detaillierte Informationen, beginnend von links: Dateiberechtigungen, Anzahl der Links, Besitzername, Besitzergruppe, Dateigröße, Zeitstempel der letzten Änderung und der Name der Datei oder des Verzeichnisses.

```bash
ls -l
```

Hier ist ein Beispiel für die Ausgabe:

```plaintext
pete@icebox:~$ ls -l
total 80
drwxr-x--- 7 pete penguingroup   4096 Nov 20 16:37 Desktop
drwxr-x--- 2 pete penguingroup   4096 Oct 19 10:46  Documents
drwxr-x--- 4 pete penguingroup   4096 Nov 20 09:30 Downloads
drwxr-x--- 2 pete penguingroup   4096 Oct  7 13:13   Music
drwxr-x--- 2 pete penguingroup   4096 Sep 21 14:02 Pictures
drwxr-x--- 2 pete penguingroup   4096 Jul 27 12:41   Public
drwxr-x--- 2 pete penguingroup   4096 Jul 27 12:41   Templates
drwxr-x--- 2 pete penguingroup   4096 Jul 27 12:41   Videos
```

### Sortieren in umgekehrter Reihenfolge

Manchmal möchten Sie die Sortierreihenfolge ändern. Der `ls -r command` listet Dateien und Verzeichnisse in umgekehrter alphabetischer Reihenfolge auf. Die Option `linux ls -r` ist besonders nützlich, wenn Sie die letzten Elemente einer langen Liste zuerst sehen möchten.

```bash
ls -r
```

### Kombinieren von Befehls-Flags

Befehle haben Flags (auch Argumente oder Optionen genannt), um zusätzliche Funktionalität hinzuzufügen. Wie wir bei `-a` und `-l` gesehen haben, können Sie diese zu einem einzigen Befehl wie `ls -la` kombinieren. Die Reihenfolge der Flags spielt normalerweise keine Rolle, daher würde `ls -al` identisch funktionieren. Sie können auch das Umkehr-Flag hinzufügen: `ls -lar`.

```bash
ls -la
```

## Exercise

Übung macht den Meister! Hier ist ein praktisches Labor, um Ihr Verständnis des `ls`-Befehls zu festigen:

- **[Linux ls Befehl: Inhaltsauflistung](https://labex.io/de/labs/linux-linux-ls-command-content-listing-219205)** - Üben Sie die Verwendung des `ls`-Befehls, um Datei- und Verzeichnisinhalte effizient aufzulisten und zu analysieren. Sie lernen verschiedene Optionen für detaillierte Auflistungen, die Anzeige versteckter Dateien, menschenlesbare Größen und Sortiertechniken kennen, um Ihre Kommandozeilenfähigkeiten zu verbessern.

Dieses Labor hilft Ihnen, die Konzepte in einem realen Szenario anzuwenden und Selbstvertrauen beim Auflisten von Verzeichnissen unter Linux aufzubauen.

## Quiz Question

Welchen Befehl würden Sie verwenden, um versteckte Dateien anzuzeigen? Bitte antworten Sie auf Englisch und achten Sie auf die Groß-/Kleinschreibung.

## Quiz Answer

ls -a
