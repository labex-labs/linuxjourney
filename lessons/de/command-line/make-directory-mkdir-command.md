---
index: 12
lang: "de"
title: "mkdir (Verzeichnis erstellen)"
meta_title: "mkdir (Verzeichnis erstellen) - Kommandozeile"
meta_description: "Lerne den Linux-Befehl mkdir mit Beispielen zum Erstellen eines Verzeichnisses, mehrerer Verzeichnisse, verschachtelter übergeordneter Verzeichnisse und zum Setzen von Berechtigungen."
meta_keywords: "mkdir Befehl, linux mkdir, Verzeichnis erstellen linux, Verzeichnis anlegen linux, mkdir -p, mkdir -m, Ordner erstellen linux"
---

## Lesson Content

Wenn du mit Dateien arbeitest, musst du sie in Verzeichnissen organisieren. Das wichtigste Werkzeug dafür ist der Befehl `mkdir`, der für „make directory“ (Verzeichnis erstellen) steht.

Die grundlegende Syntax lautet:

```bash
mkdir [OPTIONS] DIRECTORY...
```

### Ein einzelnes Verzeichnis erstellen

Die einfachste Verwendung von `mkdir` ist das Erstellen eines einzelnen neuen Verzeichnisses. Wenn das Verzeichnis noch nicht existiert, wird es an deinem aktuellen Ort erstellt.

```bash
$ mkdir documents
```

### Mehrere Verzeichnisse erstellen

Du kannst auch mehrere Verzeichnisse auf einmal erstellen, indem du ihre Namen mit Leerzeichen getrennt angibst. Das ist eine effiziente Methode, um schnell mehrere Ordner anzulegen.

```bash
$ mkdir books paintings
```

### Verschachtelte Verzeichnisse erstellen

Manchmal musst du ein Verzeichnis und seine übergeordneten Verzeichnisse gleichzeitig erstellen. Die Option `-p` ist dafür ideal. Sie verhindert Fehler, falls übergeordnete Verzeichnisse nicht existieren.

```bash
$ mkdir -p books/hemingway/favorites
```

Dieser einzelne Befehl erstellt `books`, `hemingway` und `favorites`, falls sie noch nicht existieren.

### Verzeichnisberechtigungen setzen

Verwende `-m`, um beim Erstellen eines Verzeichnisses Berechtigungen festzulegen.

```bash
$ mkdir -m 755 public
```

Mehr zu Berechtigungen lernst du später, aber dieses Beispiel erstellt ein Verzeichnis, das der Besitzer beschreiben kann und das andere lesen und betreten dürfen.

### Häufige mkdir-Optionen

- `-p`: Erstelle bei Bedarf übergeordnete Verzeichnisse.
- `-m MODE`: Setze Berechtigungen für das neue Verzeichnis.
- `-v`: Gib für jedes erstellte Verzeichnis eine Meldung aus.

Beispiel:

```bash
$ mkdir -pv projects/app/src
mkdir: created directory 'projects'
mkdir: created directory 'projects/app'
mkdir: created directory 'projects/app/src'
```

### Häufige Fragen

**Warum sagt mkdir „File exists“?** Eine Datei oder ein Verzeichnis mit diesem Namen existiert bereits. Verwende `ls`, um es zu überprüfen.

**Wie erstelle ich verschachtelte Verzeichnisse?** Verwende `mkdir -p parent/child/grandchild`.

**Kann mkdir Dateien erstellen?** Nein. Verwende `touch`, um leere Dateien zu erstellen.

## Exercise

Übung macht den Meister! Hier sind einige praktische Labs, um dein Verständnis für das Erstellen und Verwalten von Verzeichnissen zu vertiefen:

1. **[Linux mkdir Command: Directory Creating](https://labex.io/de/labs/linux-linux-mkdir-command-directory-creating-209739)** – Lerne, wie du den Befehl `mkdir` in Linux verwendest, um Verzeichnisse zu erstellen, Berechtigungen zu setzen und dein Dateisystem zu organisieren. Dieses Lab behandelt grundlegende und fortgeschrittene Anwendungen, einschließlich des Erstellens verschachtelter Verzeichnisse.
2. **[Setting Up a New Project Structure](https://labex.io/de/labs/linux-setting-up-a-new-project-structure-387859)** – Übe deine Linux-Verzeichnisverwaltung, indem du eine bestimmte Projektstruktur erstellst und dich mit wichtigen Befehlen wie `mkdir` und `cd` darin bewegst.

Diese Labs helfen dir, die Konzepte in realen Szenarien anzuwenden und Sicherheit beim Erstellen und Organisieren von Verzeichnissen unter Linux zu gewinnen.

## Quiz Question

Welcher Befehl wird verwendet, um ein Verzeichnis zu erstellen? Bitte antworte nur mit dem englischen Befehl in Kleinbuchstaben.

## Quiz Answer

mkdir
