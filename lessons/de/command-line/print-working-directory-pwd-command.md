---
lesson_id: "print-working-directory-pwd-command"
course_id: "command-line"
lang: "de"
order_index: 2
title: "pwd (Arbeitsverzeichnis anzeigen)"
description: "Lerne, mit pwd deinen aktuellen Ort im Linux-Dateisystem zu bestimmen."
meta_title: "pwd (Arbeitsverzeichnis anzeigen) - Kommandozeile"
meta_description: "Lerne den Linux-Befehl pwd, was Arbeitsverzeichnis anzeigen bedeutet und wie absolute Pfade deinen aktuellen Standort im Dateisystem zeigen."
meta_keywords: "pwd Befehl, linux pwd, Arbeitsverzeichnis anzeigen, aktuelles Verzeichnis linux, absoluter Pfad, linux Dateisystem, Verzeichnisbaum"
---

Unter Linux sind Dateien und Verzeichnisse in einer Hierarchie organisiert, die als Dateisystem bezeichnet wird. Bevor du dich darin sicher bewegen kannst, musst du wissen, wo du dich befindest. Der Befehl `pwd` beantwortet diese Frage, indem er dein aktuelles Arbeitsverzeichnis ausgibt.

## Der Verzeichnisbaum unter Linux

Das gesamte Dateisystem beginnt in einem einzigen obersten Verzeichnis, dem Wurzelverzeichnis oder Root-Verzeichnis. Es wird durch einen Schrägstrich (`/`) dargestellt. Von dort verzweigt sich der Verzeichnisbaum in Unterverzeichnisse, die Dateien und weitere Unterverzeichnisse enthalten können.

Ein vereinfachtes Beispiel sieht so aus:

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

:::single-choice{#identify-root-subdirectories}
In welchem Verhältnis stehen `home` und `etc` im gezeigten Verzeichnisbaum zu `/`?

::option[Sie sind Unterverzeichnisse, die direkt von `/` abzweigen.]{#root-subdirectories .correct explanation="Beide Verzeichnisse stehen im Baum unmittelbar unter `/`. Vom Wurzelverzeichnis aus verzweigt sich das Dateisystem in Unterverzeichnisse."}
::option[Sie sind Dateien, die im Verzeichnis `bin` gespeichert sind.]{#files-inside-bin explanation="Im Baum stehen `home` und `etc` auf derselben Ebene wie `bin`, nicht darin. Außerdem sind sie in diesem Beispiel Verzeichnisse."}
::option[Sie sind alternative Namen für das Wurzelverzeichnis.]{#alternate-root-names explanation="Linux besitzt ein einziges, durch `/` dargestelltes Wurzelverzeichnis. `home` und `etc` liegen darunter."}
:::

## Dateipfade verstehen

Der Ort einer Datei oder eines Verzeichnisses wird durch seinen Pfad beschrieben. Ein Pfad ist eine Folge von Verzeichnissen, die von einem Startpunkt zu einem bestimmten Ziel führt.

Befindet sich beispielsweise im Verzeichnis `/home` ein Ordner namens `pete` und im Ordner `pete` wiederum ein Ordner `Movies`, lautet der vollständige Pfad:

```plaintext
/home/pete/Movies
```

Ein Pfad, der mit `/` beginnt, ist ein absoluter Pfad, weil er am Wurzelverzeichnis startet. Ein Pfad wie `Movies` ist dagegen relativ, da seine Bedeutung vom aktuellen Standort abhängt.

:::single-choice{#recognize-absolute-path}
Wodurch wird `/home/pete/Movies` zu einem absoluten Pfad?

::option[Er enthält mehrere durch `/` getrennte Verzeichnisnamen.]{#contains-directories explanation="Sowohl absolute als auch relative Pfade können mehrere Verzeichnisnamen enthalten. Entscheidend ist der Startpunkt, nicht die Anzahl der Namen."}
::option[Er endet bei einem Verzeichnis namens `Movies`.]{#ends-with-movies explanation="Der Name des Ziels bestimmt nicht, ob ein Pfad absolut ist. Ein absoluter Pfad wird an seinem Start im Wurzelverzeichnis erkannt."}
::option[Er beginnt mit einem führenden `/` im Wurzelverzeichnis.]{#starts-at-root .correct explanation="Ein absoluter Pfad beginnt im Wurzelverzeichnis. Das führende `/` kennzeichnet diesen Startpunkt."}
:::

## Wofür steht PWD unter Linux?

`pwd` steht für „print working directory“, also „Arbeitsverzeichnis ausgeben“. Das Arbeitsverzeichnis ist das Verzeichnis, in dem sich deine Shell gerade befindet. Befehle mit relativen Pfaden gehen von diesem Ort aus.

:::single-choice{#expand-pwd-name}
Wofür steht `pwd`?

::option[Print working directory]{#print-working-directory .correct explanation="Der Name beschreibt genau, was der Befehl tut: Er gibt das aktuelle Arbeitsverzeichnis der Shell aus."}
::option[Present working directory]{#present-working-directory explanation="Umgangssprachlich könnte man vom gegenwärtigen Verzeichnis sprechen, doch dies ist nicht die ausgeschriebene Form von `pwd`."}
::option[Print whole directory]{#print-whole-directory explanation="`pwd` meldet den Pfad des aktuellen Verzeichnisses. Der Befehl gibt nicht dessen gesamten Inhalt aus."}
:::

## Den Befehl pwd verwenden

Gib `pwd` ein und drücke Enter, um dein aktuelles Verzeichnis zu ermitteln.

```bash
$ pwd
/home/pete
```

Die Ausgabe ist ein absoluter Pfad. In diesem Beispiel befindet sich die Shell im Home-Verzeichnis des Benutzers `pete`.

Die genaue Ausgabe kann auf deinem System anders aussehen, weil Benutzername, Home-Verzeichnis und aktueller Standort abweichen können. `pwd` gibt lediglich Informationen aus und ändert das Arbeitsverzeichnis nicht. Im Gegensatz dazu wechselt `cd` das Verzeichnis, in dem sich die Shell befindet.

:::single-choice{#check-location-without-changing-it}
Wie prüfst du dein aktuelles Verzeichnis, ohne es zu wechseln?

::option[Führe `cd` aus und lies ab, in welches Verzeichnis gewechselt wird.]{#run-cd explanation="Der Befehl `cd` ändert das Arbeitsverzeichnis. Damit erfüllt er nicht die Anforderung, den Standort ohne Wechsel zu prüfen."}
::option[Gib `/home/pete` ein und verwende den Pfad als Befehl.]{#run-path explanation="Ein absoluter Pfad bezeichnet zwar einen Ort, ist für sich genommen aber nicht der Befehl, der das aktuelle Verzeichnis meldet."}
::option[Führe `pwd` aus und lies den ausgegebenen absoluten Pfad.]{#run-pwd .correct explanation="`pwd` meldet den aktuellen Standort der Shell, ohne ihn zu ändern. Du kannst den Befehl daher jederzeit zur Orientierung einsetzen."}
:::

## Warum pwd nützlich ist

Verwende `pwd`, wenn:

- du einer Anleitung folgst und deinen Standort bestätigen möchtest,
- ein Befehl wegen eines falschen Dateipfads fehlgeschlagen ist,
- du durch mehrere Verzeichnisse gewechselt bist und die Orientierung verloren hast oder
- du den Pfad des aktuellen Verzeichnisses in einen anderen Befehl übernehmen möchtest.

Zum Beispiel:

```bash
$ pwd
/home/pete/projects
$ ls
app.py  README.md
```

Daran erkennst du, dass sich `app.py` und `README.md` in `/home/pete/projects` befinden.

Mit diesen praktischen Übungen kannst du die Navigation im Linux-Dateisystem und das Bestimmen deines aktuellen Standorts vertiefen:

1. **[Linux pwd Command: Directory Displaying](https://labex.io/de/labs/linux-linux-pwd-command-directory-displaying-209734)** – Diese Übung vermittelt die praktische Verwendung von `pwd` zum Ermitteln des aktuellen Verzeichnisses.
2. **[Linux Directory Navigation](https://labex.io/de/labs/linux-directory-navigation-387844)** – Navigiere durch verschiedene Verzeichnisse und festige dein Verständnis von Pfaden und Dateisystemstruktur.
3. **[Linux cd Command: Directory Changing](https://labex.io/de/labs/linux-linux-cd-command-directory-changing-209733)** – Lerne verschiedene Verfahren zum Verzeichniswechsel mit `cd` kennen.

## Zusammenfassung

Du kannst nun mit `pwd` deinen aktuellen Standort im Linux-Dateisystem bestimmen.

1. Erkenne das Wurzelverzeichnis des Verzeichnisbaums.
2. Unterscheide absolute und relative Pfade.
3. Erkläre die Bedeutung und Ausgabe von `pwd`.
4. Prüfe dein Arbeitsverzeichnis, ohne es zu wechseln.
