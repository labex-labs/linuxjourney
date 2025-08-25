---
index: 4
lang: "de"
title: "ls (Verzeichnisse auflisten)"
meta_title: "ls (Verzeichnisse auflisten) - Befehlszeile"
meta_description: "Erfahren Sie, wie Sie den Befehl 'ls' in Linux verwenden, um Verzeichnisinhalte aufzulisten, versteckte Dateien anzuzeigen und Dateidetails zu verstehen. Verbessern Sie Ihre Linux-Befehlszeilenkenntnisse!"
meta_keywords: "ls Befehl, Verzeichnisse auflisten, Linux Tutorial, versteckte Dateien, Linux Befehle, Linux für Anfänger, Linux Anleitung"
---

## Lesson Content

Nachdem wir nun wissen, wie man sich im System bewegt, wie finden wir heraus, was uns zur Verfügung steht? Im Moment ist es, als würden wir uns im Dunkeln bewegen. Nun, wir können den wunderbaren Befehl `ls` verwenden, um Verzeichnisinhalte aufzulisten. Der Befehl `ls` listet standardmäßig Verzeichnisse und Dateien im aktuellen Verzeichnis auf; Sie können jedoch angeben, welchen Pfad Sie auflisten möchten.

```bash
ls
ls /home/pete
```

`ls` ist ein sehr nützliches Werkzeug; es zeigt Ihnen auch detaillierte Informationen über die Dateien und Verzeichnisse, die Sie betrachten.

Beachten Sie auch, dass nicht alle Dateien in einem Verzeichnis sichtbar sind. Dateinamen, die mit `.` beginnen, sind versteckt. Sie können sie jedoch mit dem Befehl `ls` anzeigen, indem Sie das Flag `-a` (für all) übergeben.

```bash
ls -a
```

Es gibt noch ein weiteres nützliches `ls`-Flag, `-l` für lang. Dies zeigt eine detaillierte Liste von Dateien in einem langen Format. Dies zeigt Ihnen detaillierte Informationen, beginnend von links: Dateiberechtigungen, Anzahl der Links, Besitzername, Besitzergruppe, Dateigröße, Zeitstempel der letzten Änderung und Datei-/Verzeichnisname.

```bash
ls -l
```

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

Befehle haben sogenannte Flags (oder Argumente oder Optionen, wie auch immer Sie sie nennen möchten), um weitere Funktionen hinzuzufügen. Sehen Sie, wie wir `-a` und `-l` hinzugefügt haben; nun, Sie können sie beide zusammen mit `-la` hinzufügen. Die Reihenfolge der Flags bestimmt die Reihenfolge, in der sie ausgeführt werden. Meistens spielt das keine Rolle, daher können Sie auch `ls -al` verwenden, und es würde immer noch funktionieren.

```bash
ls -la
```

## Exercise

Übung macht den Meister! Hier ist ein praktisches Labor, um Ihr Verständnis des `ls`-Befehls zu vertiefen:

- **[Linux ls Command: Content Listing](https://labex.io/de/labs/linux-linux-ls-command-content-listing-219205)** - Üben Sie die Verwendung des `ls`-Befehls, um Datei- und Verzeichnisinhalte effizient aufzulisten und zu analysieren. Sie lernen verschiedene Optionen für detaillierte Auflistungen, die Anzeige versteckter Dateien, menschenlesbare Größen und Sortiertechniken, um Ihre Befehlszeilenkenntnisse zu verbessern.

Dieses Labor wird Ihnen helfen, die Konzepte in einem realen Szenario anzuwenden und Vertrauen in die Verzeichnisauflistung unter Linux aufzubauen.

## Quiz Question

Welchen Befehl würden Sie verwenden, um versteckte Dateien anzuzeigen?

## Quiz Answer

ls -a