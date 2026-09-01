---
lesson_id: "list-directories-ls-command"
course_id: "command-line"
lang: "de"
order_index: 4
title: "ls (Verzeichnisse auflisten)"
description: "Lerne, mit ls-Optionen Dateien, versteckte Einträge, Details, Größen und Sortierreihenfolgen zu untersuchen."
meta_title: "ls (Verzeichnisse auflisten) - Kommandozeile"
meta_description: "Lerne den Linux-Befehl ls mit Beispielen zum Auflisten von Dateien, versteckten Dateien, Langformat-Ausgabe, menschenlesbaren Größen, Sortierung und Kombinieren von Optionen."
meta_keywords: "ls Befehl, linux ls, dateien auflisten linux, verzeichnisse auflisten, ls -a, ls -l, ls -lh, ls -r, versteckte dateien"
---

Nachdem du dich im Dateisystem bewegen kannst, stellt sich die Frage, was an einem Ort vorhanden ist. Der Befehl `ls` listet Dateien und Verzeichnisse auf, sodass du dein aktuelles Verzeichnis oder einen anderen Pfad untersuchen kannst.

## Grundlegende Verwendung von ls

Standardmäßig listet `ls` die Verzeichnisse und Dateien im aktuellen Verzeichnis auf. Du kannst jedoch auch einen Pfad angeben, um den Inhalt eines anderen Verzeichnisses anzuzeigen.

```bash
$ ls
$ ls /home/pete
```

Auch eine einzelne Datei lässt sich auflisten:

```bash
$ ls /etc/hosts
/etc/hosts
```

:::single-choice{#list-another-directory} Welcher Befehl listet den Inhalt von `/home/pete` auf, ohne dorthin zu wechseln?

::option[`ls /home/pete`]{#ls-target-path .correct explanation="Wenn du `ls` einen Verzeichnispfad übergibst, listet der Befehl dessen Inhalt auf. Die Shell bleibt in ihrem aktuellen Arbeitsverzeichnis."}
::option[`cd /home/pete`]{#cd-target-path explanation="`cd` ändert das Arbeitsverzeichnis der Shell. Der Befehl führt für sich allein nicht die gewünschte Auflistung aus."}
::option[`pwd /home/pete`]{#pwd-target-path explanation="`pwd` meldet das aktuelle Arbeitsverzeichnis und nimmt kein aufzulistendes Ziel entgegen. Verwende stattdessen `ls` mit dem Pfad."}
:::

## Versteckte Dateien anzeigen

Nicht alle Dateien in einem Verzeichnis sind standardmäßig sichtbar. Unter Linux sind Dateinamen, die mit einem Punkt (`.`) beginnen, versteckt. Mit der Option `-a`, kurz für „all“, kannst du sie anzeigen.

```bash
$ ls -a
.  ..  .bashrc  Documents  Pictures
```

Solche Dotfiles sind standardmäßig verborgen und speichern häufig Konfigurationen, beispielsweise `.bashrc`.

:::single-choice{#show-hidden-files} Welcher Befehl nimmt versteckte Dateien in die Auflistung auf?

::option[`ls -l`]{#long-format explanation="Die Option `-l` ergänzt detaillierte Spalten, nimmt für sich allein aber keine versteckten Namen auf."}
::option[`ls -r`]{#reverse-order explanation="Die Option `-r` kehrt die Sortierreihenfolge um. Sie ändert nicht, ob versteckte Dateien angezeigt werden."}
::option[`ls -a`]{#all-files .correct explanation="Die Option `-a` steht für „all“, sodass `ls` auch Namen auflistet, die mit einem Punkt beginnen."}
:::

## Detaillierte Informationen anzeigen

Eine weitere wichtige `ls`-Option ist `-l` für das Langformat. Es zeigt Dateiberechtigungen, die Anzahl der Links, Eigentümer, Gruppe, Größe, Änderungszeit und Name an.

```bash
$ ls -l
```

Eine Beispielausgabe sieht so aus:

```plaintext
pete@icebox:~$ ls -l
total 80
drwxr-x--- 7 pete penguingroup   4096 Nov 20 16:37 Desktop
drwxr-x--- 2 pete penguingroup   4096 Oct 19 10:46  Documents
drwxr-x--- 4 pete penguingroup   4096 Nov 20 09:30 Downloads
drwxr-x--- 2 pete penguingroup   4096 Oct  7 13:13   Music
drwxr-x--- 2 pete penguingroup   4096 Sep 21 14:02 Pictures
drwxr-x--- 2 pete penguingroup   4096 Jul 27 12:41   Public
drwxr-x--- 2 pete penguingroup   4096 Jul 27 12:41   Templates
drwxr-x--- 2 pete penguingroup   4096 Jul 27 12:41   Videos
```

Ergänze `-h`, um leichter lesbare Dateigrößen zu erhalten:

```bash
$ ls -lh
```

:::single-choice{#show-readable-file-details} Welcher Befehl zeigt Details im Langformat und Größen in menschenlesbarer Form an?

::option[`ls -la`]{#long-all explanation="Diese Kombination zeigt das Langformat und versteckte Dateien. Sie fordert keine menschenlesbaren Größeneinheiten an."}
::option[`ls -lh`]{#long-human-readable .correct explanation="`-l` wählt das Langformat, während `-h` die Größen lesbarer darstellt. Beide Optionen lassen sich in einem Befehl kombinieren."}
::option[`ls -ltr`]{#long-time-reverse explanation="Diese Kombination verwendet Langformat, Sortierung nach Änderungszeit und umgekehrte Reihenfolge. Die Größenoption `-h` fehlt."}
:::

## In umgekehrter Reihenfolge sortieren

Mit der Option `-r` kannst du Dateien und Verzeichnisse in umgekehrter Reihenfolge auflisten.

```bash
$ ls -r
```

Mit `-t` sortierst du nach Änderungszeit und mit `-r` kehrst du diese Reihenfolge um:

```bash
$ ls -lt
$ ls -ltr
```

:::single-choice{#show-newest-files-last} Welcher Befehl sortiert nach Änderungszeit und stellt die neuesten Einträge zuletzt dar?

::option[`ls -ltr`]{#time-reversed .correct explanation="`-t` sortiert nach Änderungszeit und `-r` kehrt die Reihenfolge um. Zusammen erscheinen ältere Einträge vor neueren."}
::option[`ls -lt`]{#time-default explanation="Dieser Befehl sortiert nach Änderungszeit, behält aber die standardmäßige Reihenfolge mit den neuesten Einträgen zuerst bei."}
::option[`ls -lr`]{#reverse-name-order explanation="Dieser Befehl nutzt das Langformat und kehrt die normale Namenssortierung um. Ohne `-t` bestimmt die Änderungszeit nicht die Reihenfolge."}
:::

## Befehlsoptionen kombinieren

Optionen, auch Flags genannt, erweitern die Funktion eines Befehls. Wie bei `-a` und `-l` kannst du mehrere davon in einem Befehl wie `ls -la` zusammenfassen. Die Reihenfolge ist häufig unerheblich, daher funktioniert `ls -al` genauso.

```bash
$ ls -la
```

Nützliche Kombinationen sind:

```bash
$ ls -lh
$ ls -la
$ ls -ltr
```

## Häufige ls-Optionen

- `-a`: Zeigt alle Dateien einschließlich versteckter Dateien an.
- `-l`: Verwendet das Langformat.
- `-h`: Zeigt Größen zusammen mit `-l` in menschenlesbarer Form an.
- `-r`: Kehrt die Sortierreihenfolge um.
- `-t`: Sortiert nach Änderungszeit.
- `-S`: Sortiert nach Dateigröße.
- `-d`: Listet das Verzeichnis selbst statt seines Inhalts auf.

:::single-choice{#list-directory-entry-itself} Welcher Befehl listet den Verzeichniseintrag `projects/` statt seines Inhalts auf?

::option[`ls -d projects/`]{#directory-entry .correct explanation="Die Option `-d` weist `ls` an, den Verzeichniseintrag selbst anzuzeigen, statt das Verzeichnis für eine Inhaltsauflistung zu öffnen."}
::option[`ls projects/`]{#directory-contents explanation="Ohne `-d` zeigt `ls` bei einem übergebenen Verzeichnispfad die darin enthaltenen Einträge an."}
::option[`cd projects/`]{#change-to-directory explanation="`cd` wechselt das Arbeitsverzeichnis. Der Befehl listet den hier verlangten Verzeichniseintrag nicht auf."}
:::

Einige Systeme stellen die Ausgabe von `ls` für unterschiedliche Dateitypen in verschiedenen Farben dar. Dieses Verhalten stammt häufig von einem Alias oder einer Umgebungseinstellung, weshalb die Farben je nach System abweichen können.

Um dein Verständnis des Befehls `ls` zu vertiefen, probiere diese praktische Übung aus:

- **[Linux ls Command: Content Listing](https://labex.io/de/labs/linux-linux-ls-command-content-listing-219205)** – Nutze `ls`, um Datei- und Verzeichnisinhalte effizient aufzulisten und zu analysieren. Übe detaillierte Auflistungen, versteckte Dateien, menschenlesbare Größen und verschiedene Sortierungen.

So gewinnst du mehr Sicherheit beim Auflisten von Verzeichnissen unter Linux.

## Zusammenfassung

Du kannst nun mit `ls` Verzeichnisinhalte untersuchen und ihre Darstellung steuern.

1. Liste das aktuelle Verzeichnis oder einen anderen Pfad auf.
2. Beziehe versteckte Dateien in eine Auflistung ein.
3. Zeige detaillierte Informationen mit lesbaren Größen an.
4. Sortiere Einträge in umgekehrter Reihenfolge nach Änderungszeit.
5. Liste einen Verzeichniseintrag ohne dessen Inhalt auf.
