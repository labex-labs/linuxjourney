---
lesson_id: "make-directory-mkdir-command"
course_id: "command-line"
lang: "de"
order_index: 12
title: "mkdir (Verzeichnis erstellen)"
description: "Lerne, mit mkdir einzelne, mehrere und verschachtelte Verzeichnisse zu erstellen."
meta_title: "mkdir (Verzeichnis erstellen) - Kommandozeile"
meta_description: "Lerne den Linux-Befehl mkdir mit Beispielen zum Erstellen eines Verzeichnisses, mehrerer Verzeichnisse, verschachtelter übergeordneter Verzeichnisse und zum Setzen von Berechtigungen."
meta_keywords: "mkdir Befehl, linux mkdir, Verzeichnis erstellen linux, Verzeichnis anlegen linux, mkdir -p, mkdir -m, Ordner erstellen linux"
---

Der Befehl `mkdir`, kurz für „make directory“, erstellt Verzeichnisse, in denen du Dateien und weitere Verzeichnisse organisieren kannst.

Die grundlegende Syntax lautet:

```bash
mkdir [OPTIONS] DIRECTORY...
```

## Ein Verzeichnis erstellen

Übergib einen Pfad, um ein einzelnes Verzeichnis zu erstellen. Dieses Beispiel legt `documents` im aktuellen Arbeitsverzeichnis an:

```bash
$ mkdir documents
```

Existiert bereits ein Eintrag namens `documents`, meldet `mkdir` einen Fehler, statt ihn zu ersetzen. Mit `ls -ld documents` kannst du den vorhandenen Eintrag untersuchen.

:::single-choice{#create-one-directory} Welcher Befehl erstellt im aktuellen Arbeitsverzeichnis ein Verzeichnis namens `documents`?

::option[`mkdir documents`]{#mkdir-documents .correct explanation="`mkdir` erstellt das verlangte Verzeichnis am relativen Pfad `documents`."}
::option[`touch documents`]{#touch-documents explanation="`touch` erstellt bei einem fehlenden Pfad eine leere reguläre Datei. Ein Verzeichnis legt der Befehl nicht an."}
::option[`cd documents`]{#cd-documents explanation="`cd` versucht, in ein vorhandenes Verzeichnis zu wechseln. Ein fehlendes Verzeichnis erstellt der Befehl nicht."}
:::

## Mehrere Verzeichnisse erstellen

Führe mehrere Pfade auf, um mit einem Befehl mehrere Verzeichnisse anzulegen:

```bash
$ mkdir books paintings
```

:::single-choice{#create-separate-directories} Welcher Befehl erstellt zwei gleichrangige Verzeichnisse namens `books` und `paintings`?

::option[`mkdir books/paintings`]{#nested-paintings explanation="Dieser Pfad beschreibt `paintings` innerhalb von `books`, nicht zwei gleichrangige Verzeichnisse. Fehlt `books`, schlägt er außerdem fehl."}
::option[`mkdir "books paintings"`]{#spaced-directory explanation="Die Anführungszeichen verbinden beide Wörter zu einem Pfad. So wird ein einzelnes Verzeichnis mit einem Leerzeichen im Namen angefordert."}
::option[`mkdir books paintings`]{#two-directories .correct explanation="Getrennte Operanden weisen `mkdir` an, `books` und `paintings` als zwei Verzeichnisse zu erstellen."}
:::

## Fehlende übergeordnete Verzeichnisse erstellen

Ohne Option schlägt `mkdir books/hemingway/favorites` fehl, wenn ein Zwischenverzeichnis fehlt. Mit `-p` werden alle fehlenden übergeordneten Verzeichnisse entlang des Pfads angelegt:

```bash
$ mkdir -p books/hemingway/favorites
```

Damit entstehen alle fehlenden Pfadbestandteile. Außerdem wird nicht allein deshalb ein Fehler gemeldet, weil das letzte Verzeichnis bereits existiert. Andere Fehler, etwa fehlende Berechtigungen, sind weiterhin möglich.

:::single-choice{#create-nested-path} Kein Teil von `projects/app/src` existiert bisher. Welcher Befehl erstellt den vollständigen Verzeichnispfad?

::option[`mkdir -p projects/app/src`]{#mkdir-parents .correct explanation="Die Option `-p` erstellt jedes fehlende übergeordnete Verzeichnis, bevor das letzte Verzeichnis angelegt wird."}
::option[`mkdir projects/app/src`]{#mkdir-no-parents explanation="Ohne `-p` kann `mkdir` das Verzeichnis `src` nicht erstellen, wenn die Zwischenverzeichnisse fehlen."}
::option[`mkdir -m projects/app/src`]{#mkdir-mode-missing explanation="Die Option `-m` benötigt ein Modusargument und fordert nicht das Erstellen fehlender übergeordneter Verzeichnisse an."}
:::

## Den anfänglichen Modus festlegen

Mit `-m MODE` gibst du die Berechtigungen für ein neu erstelltes Verzeichnis an:

```bash
$ mkdir -m 755 public
```

Berechtigungsmodi lernst du später ausführlicher kennen. In diesem Beispiel erhält der Eigentümer mit Modus `755` Lese-, Schreib- und Suchrechte; Gruppe und andere erhalten Lese- und Suchrechte.

Mit `-v` lässt du für jedes erstellte Verzeichnis eine Meldung ausgeben:

```bash
$ mkdir -pv projects/app/src
mkdir: created directory 'projects'
mkdir: created directory 'projects/app'
mkdir: created directory 'projects/app/src'
```

:::single-choice{#set-directory-mode} Welcher Befehl erstellt `public` mit dem Berechtigungsmodus `755`?

::option[`mkdir -p 755 public`]{#parents-755 explanation="Die Option `-p` behandelt die übrigen Wörter als Verzeichnispfade. Den Berechtigungsmodus `755` setzt sie nicht."}
::option[`mkdir -v 755 public`]{#verbose-755 explanation="Die Option `-v` gibt Erstellungsmeldungen aus. `755` wird damit nicht als Berechtigungsmodus interpretiert."}
::option[`mkdir -m 755 public`]{#mode-public .correct explanation="Die Option `-m` übernimmt den gewünschten Modus; `public` ist der zu erstellende Verzeichnispfad."}
:::

Mit diesen Übungen kannst du Verzeichnisse, verschachtelte Strukturen und anfängliche Berechtigungen praktisch trainieren:

1. **[Linux mkdir Command: Directory Creating](https://labex.io/de/labs/linux-linux-mkdir-command-directory-creating-209739)** – Erstelle mit `mkdir` einfache und verschachtelte Verzeichnisse, setze Berechtigungen und organisiere das Dateisystem.
2. **[Setting Up a New Project Structure](https://labex.io/de/labs/linux-setting-up-a-new-project-structure-387859)** – Erstelle eine vorgegebene Projektstruktur und navigiere darin mit grundlegenden Befehlen wie `mkdir` und `cd`.

## Zusammenfassung

Du kannst nun Verzeichnisstrukturen mit bewusst gewählten Namen, Eltern und Modi erstellen.

1. Erstelle ein oder mehrere Verzeichnisse mit einem Befehl.
2. Erkenne einen Fehler durch einen bereits vorhandenen Pfad.
3. Lege fehlende übergeordnete Verzeichnisse mit `-p` an.
4. Setze den Modus eines neuen Verzeichnisses mit `-m`.
