---
index: 12
lang: "de"
title: "mkdir (Verzeichnis erstellen)"
meta_title: "mkdir (Verzeichnis erstellen) - Kommandozeile"
meta_description: "Erfahren Sie, wie Sie den Befehl mkdir unter Linux verwenden, um ein neues Verzeichnis zu erstellen. Diese Anleitung behandelt den Befehl zum Erstellen von Ordnern unter Linux, einschließlich der Erstellung mehrerer Verzeichnisse und übergeordneter Verzeichnisse über die Eingabeaufforderung."
meta_keywords: "verzeichnis erstellen linux, mkdir befehl linux, verzeichnis erstellen in linux, verzeichnis befehl eingabeaufforderung, ordner erstellen linux befehl, mkdir, verzeichnis erstellen, linux"
---

## Lesson Content

Wenn Sie mit Dateien arbeiten, müssen Sie diese in Verzeichnissen organisieren. Das primäre Werkzeug für diese Aufgabe ist der Befehl `mkdir`, was für "Make Directory" (Verzeichnis erstellen) steht. Mit diesem Befehl können Sie **ein Verzeichnis unter Linux** direkt über Ihr Terminal oder die **Eingabeaufforderung** erstellen.

### Erstellen eines einzelnen Verzeichnisses

Die grundlegendste Verwendung des **mkdir-Befehls unter Linux** ist das Erstellen eines einzelnen neuen Verzeichnisses. Wenn das Verzeichnis noch nicht existiert, erstellt dieser Befehl es an Ihrem aktuellen Speicherort. Um beispielsweise ein Verzeichnis namens `documents` zu erstellen:

```bash
mkdir documents
```

### Erstellen mehrerer Verzeichnisse

You können auch mehrere Verzeichnisse gleichzeitig erstellen, indem Sie deren Namen durch Leerzeichen getrennt auflisten. Dies ist eine effiziente Methode, um schnell mehrere Ordner einzurichten.

```bash
mkdir books paintings
```

### Erstellen verschachtelter Verzeichnisse

Manchmal müssen Sie ein Verzeichnis und seine übergeordneten Verzeichnisse gleichzeitig erstellen. Die Option `-p` (parent/übergeordnet) ist dafür perfekt geeignet. Diese leistungsstarke Funktion des **Befehls zum Erstellen von Ordnern unter Linux** verhindert Fehler, falls übergeordnete Verzeichnisse nicht existieren. Um beispielsweise das Verzeichnis `favorites` innerhalb von `hemmingway` zu erstellen, welches sich innerhalb von `books` befindet:

```bash
mkdir -p books/hemmingway/favorites
```

Dieser einzelne Befehl erstellt `books`, `hemmingway` und `favorites`, falls sie noch nicht existieren, und demonstriert eine Schlüsselfunktion, wenn Sie **ein Verzeichnis unter Linux erstellen** müssen.

## Exercise

Übung macht den Meister! Hier sind einige praktische Übungen, um Ihr Verständnis der Verzeichniserstellung und -verwaltung zu festigen:

1. **[Linux mkdir Befehl: Verzeichnisse erstellen](https://labex.io/de/labs/linux-linux-mkdir-command-directory-creating-209739)** - Lernen Sie, wie Sie den `mkdir`-Befehl unter Linux verwenden, um Verzeichnisse zu erstellen, Berechtigungen festzulegen und Ihr Dateisystem zu organisieren. Dieses Labor behandelt die grundlegende und erweiterte Verwendung, einschließlich der Erstellung verschachtelter Verzeichnisse.
2. **[Einrichten einer neuen Projektstruktur](https://labex.io/de/labs/linux-setting-up-a-new-project-structure-387859)** - Üben Sie Ihre Linux-Verzeichnisverwaltungsfähigkeiten, indem Sie eine bestimmte Projektstruktur erstellen und mit Befehlen wie `mkdir` und `cd` darin navigieren.

Diese Labs helfen Ihnen, die Konzepte in realen Szenarien anzuwenden und Selbstvertrauen beim Erstellen und Organisieren von Verzeichnissen unter Linux aufzubauen.

## Quiz Question

Welcher Befehl wird verwendet, um ein Verzeichnis zu erstellen? Bitte antworten Sie nur mit dem englischen Befehl in Kleinbuchstaben.

## Quiz Answer

mkdir
