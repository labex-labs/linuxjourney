---
index: 10
lang: "de"
title: "cp (Kopieren)"
meta_title: "cp (Kopieren) - Kommandozeile"
meta_description: "Meistern Sie den Linux-cp-Befehl zum Kopieren von Dateien und Verzeichnissen. Diese Anleitung behandelt wesentliche Optionen wie rekursives Kopieren (-r), Beibehalten von Attributen mit der cp -p Flagge und Erzwingen von Überschreibungen mit der cp -f Flagge. Erfahren Sie, wie cp -p unter Linux hilft, Datei-Metadaten zu erhalten."
meta_keywords: "cp Befehl, Dateien kopieren Linux, linux cp -p, cp -p Flagge, cp -p in linux, cp -f Flagge, rekursives Kopieren, cp -r, linux Platzhalter, linux Kommandozeile"
---

## Lesson Content

Der Befehl `cp` ist das Standardwerkzeug zum Kopieren von Dateien und Verzeichnissen in Linux. Seine grundlegende Syntax lautet `cp [QUELLE] [ZIEL]`.

### Grundlegendes Kopieren von Dateien

Um eine Datei zu kopieren, geben Sie die Quelldatei und das Zielverzeichnis oder den Zielpfad an.

```bash
cp mycoolfile /home/pete/Documents/cooldocs
```

In diesem Beispiel ist `mycoolfile` die Quelldatei und `/home/pete/Documents/cooldocs` das Zielverzeichnis. Sie können eine Datei auch kopieren und ihr im Ziel einen neuen Namen geben.

```bash
cp mycoolfile /home/pete/Documents/mycoolfile_backup
```

### Verwenden von Wildcards für das Massenkopieren

Wildcards sind Sonderzeichen, die Ihnen helfen, mehrere Dateien anhand von Mustern auszuwählen, was große Flexibilität bietet.

- `*`: Entspricht einer beliebigen Zeichenfolge.
- `?`: Entspricht einem einzelnen Zeichen.
- `[]`: Entspricht einem der in den Klammern eingeschlossenen Zeichen.

Um beispielsweise alle JPEG-Bilder von Ihrem aktuellen Standort in das Verzeichnis `Pictures` zu kopieren:

```bash
cp *.jpg /home/pete/Pictures
```

### Rekursives Kopieren von Verzeichnissen

Wenn Sie versuchen, ein Verzeichnis ohne Optionen mit `cp` zu kopieren, erhalten Sie eine Fehlermeldung. Um ein Verzeichnis und alle seine Inhalte, einschließlich Unterverzeichnissen, zu kopieren, müssen Sie das Flag `-r` (rekursiv) verwenden.

```bash
cp -r Pumpkin/ /home/pete/Documents
```

Dieser Befehl kopiert das Verzeichnis `Pumpkin` und alles darin in Ihr Verzeichnis `Documents`.

### Umgang mit Überschreiben von Dateien

Standardmäßig überschreibt `cp` eine Datei am Zielort, wenn sie denselben Namen hat. Um versehentlichen Datenverlust zu vermeiden, verwenden Sie das Flag `-i` (interaktiv), das vor dem Überschreiben zur Bestätigung auffordert.

```bash
cp -i mycoolfile /home/pete/Pictures
```

Umgekehrt, wenn Sie ein Überschreiben ohne Aufforderung erzwingen möchten, können Sie das `cp -f Flag` verwenden. Dies ist nützlich in Skripten, in denen keine Benutzerinteraktion möglich ist.

```bash
cp -f mycoolfile /home/pete/Pictures
```

### Beibehalten von Dateiattributen mit cp -p

Wenn Sie eine Datei kopieren, werden deren Metadaten, wie z. B. Änderungszeit und Eigentümerschaft, normalerweise aktualisiert. Um diese ursprünglichen Attribute beizubehalten, ist das Flag `cp -p` unerlässlich. Die Verwendung von `cp -p in linux` stellt sicher, dass die Kopie eine exakte Replik ist, nicht nur inhaltlich, sondern auch hinsichtlich ihrer Metadaten.

Das `cp -p Flag` ist besonders nützlich für Backups oder bei der Migration von Dateien, bei denen die Beibehaltung von Zeitstempeln von entscheidender Bedeutung ist.

```bash
cp -p mycoolfile /home/pete/backups/
```

Dieser Befehl zeigt, wie `linux cp -p` verwendet wird, um `mycoolfile` zu kopieren und dabei seinen Modus, Eigentümer und Zeitstempel beizubehalten.

## Exercise

Übung macht den Meister! Hier sind einige praktische Übungen, um Ihr Verständnis für das Kopieren von Dateien und Verzeichnissen in Linux zu festigen:

1. **[Linux cp Befehl: Dateikopieren](https://labex.io/de/labs/linux-linux-cp-command-file-copying-209744)** - Üben Sie die grundlegende Verwendung, erweiterte Optionen wie rekursives Kopieren, Beibehalten von Attributen und die Verwendung von Wildcards, um Dateien und Verzeichnisse effizient zu kopieren.
2. **[Dateien und Verzeichnisse organisieren](https://labex.io/de/labs/linux-organizing-files-and-directories-387877)** - Üben Sie wesentliche Linux-Dateiverwaltungsfähigkeiten, indem Sie die Befehle `cp`, `mv` und `rm` verwenden, um eine Projektstruktur zu organisieren, Dateien zu verschieben und unnötige Verzeichnisse zu bereinigen.

Diese Labs helfen Ihnen, die Konzepte in realen Szenarien anzuwenden und Vertrauen in das Kopieren und Verwalten von Dateien in Linux aufzubauen.

## Quiz Question

Welches Flag müssen Sie angeben, um ein Verzeichnis zu überschreiben?

## Quiz Answer

-r
