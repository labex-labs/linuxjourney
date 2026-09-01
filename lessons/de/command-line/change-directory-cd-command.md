---
lesson_id: "change-directory-cd-command"
course_id: "command-line"
lang: "de"
order_index: 3
title: "cd (Verzeichnis wechseln)"
description: "Lerne, mit cd, Pfaden und Abkürzungen durch das Linux-Dateisystem zu navigieren."
meta_title: "cd (Verzeichnis wechseln) - Kommandozeile"
meta_description: "Lerne den Linux-Befehl cd mit Beispielen für absolute Pfade, relative Pfade, Home-Verzeichnis-Verknüpfungen, übergeordnete Verzeichnisse und Navigation zum vorherigen Verzeichnis."
meta_keywords: "cd Befehl, linux cd Befehl, Verzeichnis wechseln, cd übergeordnetes Verzeichnis, cd Home, cd vorheriges Verzeichnis, absoluter Pfad, relativer Pfad"
---

Zum Navigieren im Linux-Dateisystem gibst du dein Ziel mithilfe eines Pfads an. Das wichtigste Werkzeug dafür ist `cd`, kurz für „change directory“. Der Befehl ändert das aktuelle Arbeitsverzeichnis der Shell.

Das Ziel muss ein Verzeichnis und darf keine gewöhnliche Datei sein. Existiert das Verzeichnis nicht, ist sein Name falsch geschrieben oder fehlen dir die nötigen Zugriffsrechte, meldet `cd` einen Fehler, statt den Standort zu wechseln.

Die grundlegende Syntax lautet:

```bash
cd [DIRECTORY]
```

## Pfade verstehen

Einen Pfad kannst du auf zwei Arten angeben: absolut oder relativ.

- **Absoluter Pfad**: Der vollständige Pfad ab dem Wurzelverzeichnis (`/`), zum Beispiel `/home/pete/Desktop`.
- **Relativer Pfad**: Ein Pfad, der von deinem aktuellen Standort ausgeht. Befindest du dich in `/home/pete/Documents` und möchtest das darin liegende Unterverzeichnis `taxes` öffnen, genügt `taxes/`.

:::single-choice{#recognize-absolute-cd-path} Welche Aussage beschreibt einen absoluten Pfad richtig?

::option[Er beginnt in dem Verzeichnis, das die Shell gerade verwendet.]{#begins-at-current-directory explanation="Ein Pfad, der vom aktuellen Standort der Shell abhängt, ist relativ. Er beginnt nicht zwangsläufig im Wurzelverzeichnis."}
::option[Er enthält nur den Namen des Zielverzeichnisses ohne übergeordnete Verzeichnisse.]{#contains-final-name-only explanation="Ein einzelner Zielname wird normalerweise relativ zum aktuellen Verzeichnis interpretiert. Ein absoluter Pfad enthält den Weg ab `/`."}
::option[Er beginnt im durch `/` dargestellten Wurzelverzeichnis.]{#begins-at-root .correct explanation="Ein absoluter Pfad beginnt an der Wurzel des Dateisystems. Durch das führende `/` ist sein Startpunkt unabhängig vom aktuellen Verzeichnis."}
:::

## Den Befehl cd verwenden

Mit einem absoluten Pfad wechselst du folgendermaßen in ein bestimmtes Verzeichnis:

```bash
$ cd /home/pete/Pictures
```

Dieser Befehl bringt dich direkt in das Verzeichnis `Pictures`.

Mit `pwd` kannst du deinen Standort bestätigen:

```bash
$ pwd
/home/pete/Pictures
```

:::single-choice{#verify-changed-directory} Welcher Befehl bestätigt nach `cd` den aktuellen Standort der Shell?

::option[`cd`]{#cd-command explanation="`cd` ändert das aktuelle Verzeichnis, gibt dessen vollständigen Pfad aber normalerweise nicht aus. Verwende zur Bestätigung `pwd`."}
::option[`ls`]{#ls-command explanation="`ls` zeigt den Inhalt eines Verzeichnisses an. Damit kannst du den Ort untersuchen, doch den Ort selbst meldet `pwd`."}
::option[`pwd`]{#pwd-command .correct explanation="`pwd` gibt das aktuelle Arbeitsverzeichnis aus. So kannst du prüfen, wohin `cd` die Shell bewegt hat."}
:::

## In ein Unterverzeichnis wechseln

Möchtest du von deinem aktuellen Verzeichnis in ein Unterverzeichnis wechseln, verwende einen relativen Pfad. Befindest du dich etwa in `/home/pete/Pictures` und liegt darin ein Ordner namens `Hawaii`, wechselst du so hinein:

```bash
$ cd Hawaii
```

Hier genügt der Ordnername, weil du dich bereits im übergeordneten Verzeichnis `/home/pete/Pictures` befindest.

## Wichtige Navigationsabkürzungen

Vollständige Pfade immer wieder einzugeben kann umständlich sein. Die Shell bietet deshalb mehrere Abkürzungen:

- `.` (aktuelles Verzeichnis): steht für das Verzeichnis, in dem du dich gerade befindest.
- `..` (übergeordnetes Verzeichnis): führt eine Ebene nach oben in das Verzeichnis, das dein aktuelles Verzeichnis enthält.
- `~` (Home-Verzeichnis): steht für dein persönliches Home-Verzeichnis, beispielsweise `/home/pete`.
- `-` (vorheriges Verzeichnis): bringt dich zurück in das zuletzt verwendete Verzeichnis.

Du kannst diese Abkürzungen mit `cd` verwenden:

```bash
$ cd .
$ cd ..
$ cd ~
$ cd -
```

:::single-choice{#move-to-parent-directory} Welcher Befehl wechselt von `/home/pete/Pictures` nach `/home/pete`?

::option[`cd .`]{#cd-current explanation="`.` steht für das aktuelle Verzeichnis. Dieser Befehl belässt die Shell in `/home/pete/Pictures`."}
::option[`cd -`]{#cd-previous explanation="`-` führt in das vorherige Arbeitsverzeichnis zurück, das nicht zwingend das übergeordnete ist. Für eine Ebene nach oben verwendest du `..`."}
::option[`cd ..`]{#cd-parent .correct explanation="`..` steht für das übergeordnete Verzeichnis. Das übergeordnete Verzeichnis von `Pictures` ist hier `/home/pete`."}
:::

:::single-choice{#return-to-previous-directory} Welcher Befehl kehrt in das unmittelbar zuvor verwendete Verzeichnis zurück?

::option[`cd -`]{#previous-directory .correct explanation="`cd -` wechselt in das vorherige Arbeitsverzeichnis. Dieses kann sich an einer beliebigen Stelle im Dateisystem befinden."}
::option[`cd ..`]{#parent-directory explanation="`cd ..` wechselt in das übergeordnete Verzeichnis. Das übergeordnete und das vorherige Verzeichnis müssen nicht identisch sein."}
::option[`cd ~`]{#home-directory explanation="`cd ~` wechselt in dein Home-Verzeichnis. Der Befehl berücksichtigt nicht, welches Verzeichnis du zuvor besucht hast."}
:::

Experimentiere mit diesen Abkürzungen, um auf der Kommandozeile effizienter zu navigieren.

## Praktische cd-Beispiele

Wechsle in dein Home-Verzeichnis:

```bash
$ cd
```

Auch `cd` ohne Verzeichnisargument führt in dein Home-Verzeichnis.

Wechsle zwei Ebenen nach oben:

```bash
$ cd ../..
```

Setze einen Verzeichnisnamen mit Leerzeichen in Anführungszeichen:

```bash
$ cd "Vacation Photos"
```

:::single-choice{#enter-directory-with-spaces} Bei welchem Befehl wird `Vacation Photos` als ein einziger Verzeichnisname behandelt?

::option[`cd Vacation Photos`]{#unquoted-directory-name explanation="Ohne Anführungszeichen übergibt die Shell `Vacation` und `Photos` als getrennte Argumente statt als einen Verzeichnisnamen."}
::option[`"cd Vacation Photos"`]{#quote-entire-command explanation="Steht die gesamte Zeile in Anführungszeichen, behandelt die Shell sie als einen einzigen Befehlsnamen. Nur der Pfad gehört in Anführungszeichen."}
::option[`cd "Vacation Photos"`]{#quote-directory-name .correct explanation="Die Anführungszeichen fassen beide Wörter zu einem einzigen Pfadargument für `cd` zusammen."}
:::

Kehre in das vorherige Verzeichnis zurück:

```bash
$ cd -
/home/pete/Documents
```

Mit diesen praktischen Übungen kannst du deine Kenntnisse der Linux-Verzeichnisnavigation festigen:

1. **[Linux cd Command: Directory Changing](https://labex.io/de/labs/linux-linux-cd-command-directory-changing-209733)** – Lerne den Befehl `cd` kennen und übe unterschiedliche Verfahren zum Wechseln von Verzeichnissen und den Umgang mit Pfaden.
2. **[Linux Directory Navigation](https://labex.io/de/labs/linux-directory-navigation-387844)** – Navigiere mit grundlegenden Kommandozeilenbefehlen durch verschiedene Verzeichnisse.
3. **[Setting Up a New Project Structure](https://labex.io/de/labs/linux-setting-up-a-new-project-structure-387859)** – Erstelle eine Projektstruktur und bewege dich darin mit Befehlen wie `mkdir` und `cd`.

## Zusammenfassung

Du kannst nun mit `cd`, vollständigen Pfaden und Shell-Abkürzungen zwischen Verzeichnissen wechseln.

1. Unterscheide absolute und relative Pfade.
2. Wechsle Verzeichnisse und prüfe das Ergebnis mit `pwd`.
3. Navigiere in übergeordnete, Home- und vorherige Verzeichnisse.
4. Öffne Verzeichnisnamen, die Leerzeichen enthalten.
5. Erkenne typische Pfad- und Berechtigungsfehler.
