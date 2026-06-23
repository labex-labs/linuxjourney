---
index: 2
lang: "de"
title: "pwd (Arbeitsverzeichnis anzeigen)"
meta_title: "pwd (Arbeitsverzeichnis anzeigen) - Kommandozeile"
meta_description: "Lerne den Linux-Befehl pwd, was Arbeitsverzeichnis anzeigen bedeutet und wie absolute Pfade deinen aktuellen Standort im Dateisystem zeigen."
meta_keywords: "pwd Befehl, linux pwd, Arbeitsverzeichnis anzeigen, aktuelles Verzeichnis linux, absoluter Pfad, linux Dateisystem, Verzeichnisbaum"
---

## Lesson Content

In Linux sind Dateien und Verzeichnisse in einer Hierarchie organisiert, die als Dateisystem bezeichnet wird. Bevor du dich sicher bewegen kannst, musst du wissen, wo du dich befindest. Der Befehl `pwd` beantwortet diese Frage, indem er dein aktuelles Arbeitsverzeichnis ausgibt.

### Der Verzeichnisbaum in Linux

Das gesamte Dateisystem beginnt mit einem einzigen obersten Verzeichnis, dem Wurzelverzeichnis, dargestellt durch einen Schrägstrich (`/`). Vom Wurzelverzeichnis verzweigt sich der Verzeichnisbaum in Unterverzeichnisse, die Dateien und weitere Unterverzeichnisse enthalten können.

Hier ist ein vereinfachtes Beispiel, wie diese Struktur aussieht:

```plaintext
/
|-- bin
|   |-- file1
|   |-- file2
|-- etc
|   |-- file3
|   `-- directory1
|       |-- file4
|       `-- file5
|-- home
|-- var
```

### Verständnis von Dateipfaden

Der Ort jeder Datei oder jedes Verzeichnisses wird durch seinen Pfad beschrieben. Ein Pfad ist eine Folge von Verzeichnissen, die von einem Startpunkt zu einem bestimmten Ziel führen.

Zum Beispiel, wenn du einen Ordner namens `pete` im Verzeichnis `/home` hast und darin einen Ordner `Movies`, dann ist der vollständige Pfad:

```plaintext
/home/pete/Movies
```

Ein Pfad, der mit `/` beginnt, ist ein absoluter Pfad, weil er im Wurzelverzeichnis startet. Ein Pfad wie `Movies` ist relativ, weil er von deinem aktuellen Standort abhängt.

### Was ist die vollständige Bedeutung von PWD in Linux?

Die vollständige Bedeutung von `pwd` ist „print working directory“ (Arbeitsverzeichnis anzeigen). Dein Arbeitsverzeichnis ist das Verzeichnis, in dem sich deine Shell gerade befindet. Befehle, die relative Pfade verwenden, starten von diesem Ort.

### Verwendung des Befehls pwd

Um dein aktuelles Verzeichnis zu finden, gib `pwd` ein und drücke Enter.

```bash
$ pwd
/home/pete
```

Die Ausgabe ist ein absoluter Pfad. In diesem Beispiel befindet sich die Shell gerade im Home-Verzeichnis des Benutzers `pete`.

### Warum pwd nützlich ist

Verwende `pwd`, wenn:

- Du Anweisungen folgst und deinen Standort bestätigen musst.
- Ein Befehl fehlgeschlagen ist, weil ein Dateipfad falsch war.
- Du dich durch mehrere Verzeichnisse bewegt hast und nicht mehr weißt, wo du bist.
- Du den Pfad des aktuellen Verzeichnisses in einen anderen Befehl kopieren möchtest.

Zum Beispiel:

```bash
$ pwd
/home/pete/projects
$ ls
app.py  README.md
```

Dies zeigt dir, dass sich `app.py` und `README.md` im Verzeichnis `/home/pete/projects` befinden.

### Häufige Fragen

**Ändert pwd etwas?** Nein. `pwd` gibt nur Informationen aus.

**Warum ist die Ausgabe auf meinem System anders?** Dein Benutzername, dein Home-Verzeichnis und dein aktueller Standort können unterschiedlich sein.

**Was ist der Unterschied zwischen pwd und cd?** `pwd` zeigt, wo du bist. `cd` ändert, wo du bist.

## Exercise

Übung macht den Meister! Hier sind einige praktische Labs, um dein Verständnis der Navigation im Linux-Dateisystem und der Bestimmung deines aktuellen Standorts zu vertiefen:

1. **[Linux pwd Command: Directory Displaying](https://labex.io/de/labs/linux-linux-pwd-command-directory-displaying-209734)** – Dieses Lab bietet einen fokussierten Überblick und praktische Anwendung des Befehls `pwd`, passend zur Lektion über das Finden deines aktuellen Verzeichnisses.
2. **[Linux Directory Navigation](https://labex.io/de/labs/linux-directory-navigation-387844)** – Teste deine grundlegenden Linux-Kommandozeilenfähigkeiten, indem du dich durch verschiedene Verzeichnisse bewegst und so dein Verständnis von Pfaden und Dateisystemstruktur festigst.
3. **[Linux cd Command: Directory Changing](https://labex.io/de/labs/linux-linux-cd-command-directory-changing-209733)** – Lerne, dein Dateisystem effizient mit dem Befehl `cd` zu navigieren, verschiedene Techniken zum Wechseln von Verzeichnissen und zur Erkundung der Dateistruktur.

Diese Labs helfen dir, die Konzepte der Dateisystemhierarchie und Navigation in realen Szenarien anzuwenden und Vertrauen in wichtige Linux-Befehle zu gewinnen.

## Quiz Question

Welcher Befehl wird verwendet, um das Verzeichnis zu finden, in dem du dich gerade befindest? (Bitte antworte auf Englisch, nur mit dem Befehlsnamen in Kleinbuchstaben.)

## Quiz Answer

pwd
