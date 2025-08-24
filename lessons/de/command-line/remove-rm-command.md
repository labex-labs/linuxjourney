---
index: 13
lang: "de"
title: "rm (Entfernen)"
meta_title: "rm (Entfernen) - Befehlszeile"
meta_description: "Erfahren Sie, wie Sie den Befehl `rm` in Linux verwenden, um Dateien und Verzeichnisse sicher zu löschen. Verstehen Sie Optionen wie -f, -i, -r und rmdir. Beginnen Sie Ihre Linux-Reise!"
meta_keywords: "rm Befehl, Dateien löschen Linux, Verzeichnisse entfernen, Linux Tutorial, Linux für Anfänger, rmdir, Linux Anleitung"
---

## Lesson Content

Ich denke, wir haben jetzt zu viele Dateien; lassen Sie uns einige entfernen. Um Dateien zu entfernen, können Sie den Befehl `rm` verwenden. Der Befehl `rm` (remove) wird zum Löschen von Dateien und Verzeichnissen verwendet.

```bash
rm file1
```

Seien Sie vorsichtig bei der Verwendung von `rm`; es gibt keinen magischen Papierkorb, aus dem Sie entfernte Dateien wiederherstellen können. Sobald sie weg sind, sind sie für immer weg, seien Sie also vorsichtig.

Glücklicherweise gibt es einige Sicherheitsmaßnahmen, sodass der durchschnittliche Benutzer nicht einfach eine Menge wichtiger Dateien entfernen kann. Schreibgeschützte Dateien werden Sie vor dem Löschen zur Bestätigung auffordern. Wenn ein Verzeichnis schreibgeschützt ist, wird es ebenfalls nicht einfach entfernt.

Wenn Ihnen das alles egal ist, können Sie natürlich eine Menge Dateien entfernen.

```bash
rm -f file1
```

Die Option `-f` oder force weist `rm` an, alle Dateien zu entfernen, egal ob sie schreibgeschützt sind oder nicht, ohne den Benutzer aufzufordern (solange Sie die entsprechenden Berechtigungen haben).

```bash
rm -i file
```

Das Hinzufügen des Flags `-i` wird, wie bei vielen anderen Befehlen, eine Aufforderung anzeigen, ob Sie die Dateien oder Verzeichnisse tatsächlich entfernen möchten.

```bash
rm -r directory
```

Sie können ein Verzeichnis nicht standardmäßig einfach mit `rm` entfernen; Sie müssen das Flag `-r` (recursive) hinzufügen, um alle Dateien und eventuelle Unterverzeichnisse zu entfernen.

Sie können ein Verzeichnis mit dem Befehl `rmdir` entfernen.

```bash
rmdir directory
```

## Exercise

Für praktische Übungen mit dem Befehl `rm` probieren Sie dieses interaktive Labor aus:

- [Linux rm Command: File Removing](https://labex.io/de/labs/linux-linux-rm-command-file-removing-209741)

## Quiz Question

Wie entfernen Sie eine Datei namens `myfile`?

## Quiz Answer

rm myfile
