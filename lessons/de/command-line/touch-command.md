---
index: 5
lang: "de"
title: "touch"
meta_title: "touch - Kommandozeile"
meta_description: "Erfahren Sie, wie Sie den Linux-touch-Befehl verwenden, um Dateien zu erstellen und Zeitstempel zu verwalten. Diese Anleitung behandelt den touch-Befehl unter Linux, einschließlich Optionen wie linux touch -r und touch -d."
meta_keywords: "linux touch, touch befehl linux, bash touch, touch -d linux, linux touch -r, dateien erstellen, zeitstempel aktualisieren, dateiverwaltung, linux befehle"
---

## Lesson Content

Der `touch`-Befehl ist ein Standarddienstprogramm auf Unix-ähnlichen Betriebssystemen. Obwohl sein Hauptzweck darin besteht, Datei-Zeitstempel zu ändern, wird er auch häufig verwendet, um neue, leere Dateien zu erstellen. Lassen Sie uns untersuchen, wie der `linux touch`-Befehl funktioniert.

### Erstellen neuer Dateien

Die einfachste Methode, eine leere Datei zu erstellen, ist die Verwendung des `touch`-Befehls gefolgt von einem Dateinamen. Wenn die Datei nicht existiert, erstellt `touch` sie für Sie. Dies ist ein grundlegender `bash touch`-Vorgang für Skripte und tägliche Aufgaben.

```bash
touch mysuperduperfile
```

Nach der Ausführung dieses Befehls erscheint eine neue leere Datei namens `mysuperduperfile` in Ihrem aktuellen Verzeichnis. Sie können mehrere Dateien gleichzeitig erstellen, indem Sie ihre Namen auflisten.

```bash
touch file1.txt file2.txt file3.log
```

### Aktualisieren von Datei-Zeitstempeln

Die ursprüngliche Funktion des `touch command in linux` besteht darin, die Zugriffs- und Änderungszeitstempel einer Datei oder eines Verzeichnisses zu aktualisieren. Wenn Sie `touch` für eine vorhandene Datei verwenden, werden deren Zeitstempel auf die aktuelle Zeit aktualisiert.

Sie können dies überprüfen, indem Sie `ls -l` verwenden, um den Zeitstempel einer Datei zu überprüfen, `touch` darauf auszuführen und dann erneut zu überprüfen.

```bash
# Überprüfen des ursprünglichen Zeitstempels
ls -l mysuperduperfile

# Zeitstempel aktualisieren
touch mysuperduperfile

# Neuen Zeitstempel überprüfen
ls -l mysuperduperfile
```

### Erweiterte Zeitstempelsteuerung

Der `linux touch`-Befehl bietet auch Optionen für eine präzisere Zeitstempelmanipulation.

#### Verwendung einer Referenzdatei

Die Option `linux touch -r` ermöglicht es Ihnen, den Zeitstempel einer Datei so festzulegen, dass er dem einer anderen Datei (einer Referenzdatei) entspricht. Dies ist nützlich, um Zeitstempel über zusammengehörige Dateien hinweg zu synchronisieren.

```bash
# Zeitstempel von file2.txt an den von file1.txt anpassen
touch -r file1.txt file2.txt
```

#### Festlegen eines bestimmten Datums

Mit der Option `touch -d` können Sie den Zeitstempel einer Datei auf ein bestimmtes Datum und eine bestimmte Uhrzeit festlegen. Die Funktionalität `touch -d linux` akzeptiert verschiedene Zeichenkettenformate für das Datum.

```bash
# Zeitstempel auf ein bestimmtes Datum und eine bestimmte Uhrzeit festlegen
touch -d "2023-01-01 12:30:00" mysuperduperfile
```

Die Beherrschung von `touch` ist ein großer Schritt beim Erlernen der effizienten Verwaltung Ihres Dateisystems über die Befehlszeile.

## Exercise

Übung macht den Meister! Hier sind einige praktische Übungen, um Ihr Verständnis für die Erstellung und Verwaltung von Dateisystemobjekten zu festigen:

1. **[Linux mkdir Befehl: Verzeichniserstellung](https://labex.io/de/labs/linux-linux-mkdir-command-directory-creating-209739)** - Erfahren Sie, wie Sie den `mkdir`-Befehl unter Linux verwenden, um Verzeichnisse zu erstellen, Berechtigungen festzulegen und Ihr Dateisystem zu organisieren. Dies hilft Ihnen, das umfassendere Konzept der Erstellung neuer Elemente im Dateisystem zu verstehen.
2. **[Einrichten einer neuen Projektstruktur](https://labex.io/de/labs/linux-setting-up-a-new-project-structure-387859)** - Üben Sie Ihre Linux-Verzeichnisverwaltungsfähigkeiten, indem Sie eine bestimmte Projektstruktur erstellen und mit Befehlen wie `mkdir` und `cd` darin navigieren.

Diese Labs helfen Ihnen, die Konzepte der Dateisystemerstellung und -organisation in realen Szenarien anzuwenden und Vertrauen in Linux-Befehle aufzubauen.

## Quiz Question

Wie erstellen Sie eine Datei namens `myfile`? Bitte antworten Sie nur mit dem englischen Befehl und achten Sie auf die Groß- und Kleinschreibung.

## Quiz Answer

touch myfile
