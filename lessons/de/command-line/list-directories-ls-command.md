---
index: 4
lang: "de"
title: "ls (Verzeichnisse auflisten)"
meta_title: "ls (Verzeichnisse auflisten) - Kommandozeile"
meta_description: "Lerne den Linux-Befehl ls mit Beispielen zum Auflisten von Dateien, versteckten Dateien, Langformat-Ausgabe, menschenlesbaren Größen, Sortierung und Kombinieren von Optionen."
meta_keywords: "ls Befehl, linux ls, dateien auflisten linux, verzeichnisse auflisten, ls -a, ls -l, ls -lh, ls -r, versteckte dateien"
---

## Lesson Content

Jetzt, wo wir wissen, wie man sich im Dateisystem bewegt, wie finden wir heraus, was uns zur Verfügung steht? Der Befehl `ls` listet Dateien und Verzeichnisse auf, damit du deinen aktuellen Ort oder einen anderen Pfad inspizieren kannst.

### Grundlegende Verwendung des ls-Befehls

Standardmäßig listet der Befehl `ls` die Verzeichnisse und Dateien im aktuellen Verzeichnis auf. Du kannst jedoch auch einen Pfad angeben, um den Inhalt eines anderen Verzeichnisses aufzulisten.

```bash
$ ls
$ ls /home/pete
```

Du kannst auch eine bestimmte Datei auflisten:

```bash
$ ls /etc/hosts
/etc/hosts
```

### Versteckte Dateien anzeigen

Nicht alle Dateien in einem Verzeichnis sind standardmäßig sichtbar. In Linux sind Dateinamen, die mit einem Punkt (`.`) beginnen, versteckt. Du kannst sie mit der Option `-a` anzeigen, was für „alle“ steht.

```bash
$ ls -a
.  ..  .bashrc  Documents  Pictures
```

### Detaillierte Informationen erhalten

Eine weitere wichtige Option von `ls` ist `-l` für das Langformat. Es zeigt Dateiberechtigungen, Anzahl der Links, Besitzer, Gruppe, Größe, Änderungszeit und Namen an.

```bash
$ ls -l
```

Hier ist ein Beispiel für die Ausgabe:

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

Für einfachere Dateigrößen füge `-h` für menschenlesbare Ausgabe hinzu:

```bash
$ ls -lh
```

### Sortierung in umgekehrter Reihenfolge

Manchmal möchtest du die Sortierreihenfolge ändern. Die Option `-r` listet Dateien und Verzeichnisse in umgekehrter Reihenfolge auf.

```bash
$ ls -r
```

Du kannst nach Änderungszeit mit `-t` sortieren und dann mit `-r` umkehren:

```bash
$ ls -lt
$ ls -ltr
```

### Kombination von Befehlsoptionen

Befehle haben Flags, auch Optionen genannt, um mehr Funktionalität hinzuzufügen. Wie wir bei `-a` und `-l` gesehen haben, kannst du sie in einem einzigen Befehl kombinieren, z.B. `ls -la`. Die Reihenfolge der Flags spielt oft keine Rolle, also funktioniert `ls -al` genauso.

```bash
$ ls -la
```

Nützliche Kombinationen sind:

```bash
$ ls -lh
$ ls -la
$ ls -ltr
```

### Häufige ls-Optionen

- `-a`: Zeigt alle Dateien an, einschließlich versteckter Dateien.
- `-l`: Verwendet das Langformat.
- `-h`: Zeigt menschenlesbare Größen mit `-l`.
- `-r`: Kehrt die Sortierreihenfolge um.
- `-t`: Sortiert nach Änderungszeit.
- `-S`: Sortiert nach Dateigröße.
- `-d`: Listet das Verzeichnis selbst auf, anstatt dessen Inhalt.

### Häufige Fragen

**Warum beginnen manche Dateinamen mit einem Punkt?** Dotfiles sind standardmäßig versteckt und speichern oft Konfigurationen, wie z.B. `.bashrc`.

**Wie liste ich nur ein Verzeichnis selbst auf?** Verwende `ls -d directory/`.

**Wie sehe ich die neuesten Dateien zuletzt?** Verwende `ls -ltr`.

**Warum zeigt ls Farben an?** Viele Systeme konfigurieren `ls` so, dass Dateitypen über ein Alias oder eine Umgebungsvariable farbig dargestellt werden.

## Exercise

Übung macht den Meister! Hier ist ein praktisches Labor, um dein Verständnis des Befehls `ls` zu vertiefen:

- **[Linux ls Command: Content Listing](https://labex.io/de/labs/linux-linux-ls-command-content-listing-219205)** – Übe den Umgang mit dem Befehl `ls`, um Dateien und Verzeichnisse effizient aufzulisten und zu analysieren. Du lernst verschiedene Optionen für detaillierte Auflistungen, Anzeige versteckter Dateien, menschenlesbare Größen und Sortiertechniken, um deine Kommandozeilenfähigkeiten zu verbessern.

Dieses Labor hilft dir, die Konzepte in einem realen Szenario anzuwenden und Vertrauen im Umgang mit Verzeichnisauflistungen unter Linux zu gewinnen.

## Quiz Question

Welchen Befehl würdest du verwenden, um versteckte Dateien zu sehen? Bitte antworte auf Englisch und achte auf Groß- und Kleinschreibung.

## Quiz Answer

ls -a
