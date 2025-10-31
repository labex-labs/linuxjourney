---
index: 2
lang: "de"
title: "pwd (Aktuelles Arbeitsverzeichnis anzeigen)"
meta_title: "pwd (Aktuelles Arbeitsverzeichnis anzeigen) - Kommandozeile"
meta_description: "Meistern Sie den Linux-pwd-Befehl, um Ihr aktuelles Verzeichnis in Linux anzuzeigen. Diese Lektion erklärt die ausgeschriebene Form von pwd in Linux und wie man im Linux-Verzeichnisbaum navigiert."
meta_keywords: "linux pwd, aktuelles verzeichnis linux, verzeichnisbaum linux, ausgeschriebene form von pwd in linux, aktuelles arbeitsverzeichnis, linux pfad, linux navigation, kommandozeilen grundlagen"
---

## Lesson Content

In Linux ist ein Kernkonzept, dass alles als Datei behandelt wird. Diese Dateien sind in einer hierarchischen Struktur organisiert, die als Dateisystem bekannt ist. Das Verständnis dieser Struktur ist der Schlüssel zur effektiven Navigation in Ihrem System.

### Der Verzeichnisbaum in Linux

Das gesamte Dateisystem beginnt mit einem einzigen Stammverzeichnis, das als Root-Verzeichnis bezeichnet wird und durch einen Schrägstrich (`/`) dargestellt wird. Vom Root aus verzweigt sich der **Verzeichnisbaum in linux** in verschiedene Unterverzeichnisse, die Dateien und weitere Unterverzeichnisse enthalten können.

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

Der Speicherort jeder Datei oder jedes Verzeichnisses wird durch seinen Pfad beschrieben. Ein Pfad ist eine Abfolge von Verzeichnissen, die von einem Ausgangspunkt zu einem bestimmten Ziel führt. Wenn Sie beispielsweise einen Ordner namens `pete` im Verzeichnis `/home` und einen Ordner `Movies` innerhalb von `pete` haben, wäre der vollständige Pfad `/home/pete/Movies`.

### Was ist die ausgeschriebene Form von PWD in Linux?

Beim Navigieren im Dateisystem ist es wichtig, den aktuellen Standort zu kennen. Der Befehl dafür ist `pwd`. Die **ausgeschriebene Form von pwd in linux** lautet „print working directory“ (Arbeitsverzeichnis ausgeben). Sein einziger Zweck ist die Anzeige des vollständigen Pfades des Verzeichnisses, in dem Sie sich gerade befinden, beginnend mit dem Root (`/`).

### Verwendung des linux pwd Befehls

Um Ihr **aktuelles Verzeichnis linux** zu finden, geben Sie einfach den Befehl **linux pwd** ein und drücken Sie die Eingabetaste. Er gibt den absoluten Pfad zu Ihrem aktuellen Standort in der Befehlszeile aus.

```bash
pwd
```

Wo sind Sie? Wo bin ich? Probieren Sie es aus, um Ihr eigenes aktuelles Arbeitsverzeichnis anzuzeigen.

## Exercise

Übung macht den Meister! Hier sind einige praktische Übungen, um Ihr Verständnis der Linux-Dateisystemnavigation und der Ermittlung Ihres aktuellen Standorts zu festigen:

1. **[Linux pwd Befehl: Verzeichnisanzeige](https://labex.io/de/labs/linux-linux-pwd-command-directory-displaying-209734)** - Dieses Labor bietet einen fokussierten Überblick und die praktische Anwendung des `pwd`-Befehls, der direkt auf die Einführung der Lektion zur Ermittlung Ihres aktuellen Verzeichnisses eingeht.
2. **[Linux Verzeichnisnavigation](https://labex.io/de/labs/linux-directory-navigation-387844)** - Testen Sie Ihre grundlegenden Linux-Befehlszeilenkenntnisse, indem Sie durch verschiedene Verzeichnisse navigieren, um Ihr Verständnis von Pfaden und der Dateisystemstruktur zu festigen.
3. **[Linux cd Befehl: Verzeichniswechsel](https://labex.io/de/labs/linux-linux-cd-command-directory-changing-209733)** - Lernen Sie, effizient durch Ihr Dateisystem zu navigieren, indem Sie den `cd`-Befehl verwenden, und verstehen Sie verschiedene Techniken zum Wechseln von Verzeichnissen und zum Erkunden der Dateistruktur.

Diese Labs helfen Ihnen, die Konzepte der Dateisystemhierarchie und Navigation in realen Szenarien anzuwenden und Vertrauen in wesentliche Linux-Befehle aufzubauen.

## Quiz Question

Welcher Befehl wird verwendet, um das Verzeichnis zu finden, in dem Sie sich gerade befinden? (Bitte antworten Sie auf Englisch, verwenden Sie nur den Befehlsnamen in Kleinbuchstaben.)

## Quiz Answer

pwd
