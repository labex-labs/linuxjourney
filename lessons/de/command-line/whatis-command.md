---
index: 17
lang: "de"
title: "whatis"
meta_title: "whatis - Kommandozeile"
meta_description: "Lerne den Linux-Befehl whatis mit Beispielen kennen, um einzeilige Befehlsbeschreibungen aus Manpages zu erhalten und mehrere Handbuchabschnitte zu verstehen."
meta_keywords: "whatis Befehl, linux whatis, Befehlsbeschreibung linux, man page Zusammenfassung, Kommandozeilenhilfe, apropos"
---

## Lesson Content

Wenn du die Linux-Kommandozeile erkundest, wirst du auf eine Vielzahl von Befehlen stoßen. Es ist ganz natürlich, dass man vergisst, was ein bestimmter Befehl macht. Zum Glück gibt es ein einfaches Hilfsmittel, das dir weiterhilft.

### Was ist der Befehl whatis

Der Befehl `whatis` zeigt eine kurze, einzeilige Beschreibung eines Befehls direkt aus seiner Handbuchseite an. Es ist eine schnelle Möglichkeit, sich an die Hauptfunktion eines Befehls zu erinnern, ohne die gesamte Manpage lesen zu müssen.

### Wie man den Befehl whatis benutzt

Die Verwendung von `whatis` ist einfach. Tippe `whatis` gefolgt von dem Befehl, über den du mehr wissen möchtest.

```bash
$ whatis cat
cat (1)              - concatenate files and print on the standard output
```

### Das Ergebnis verstehen

Die Beschreibung, die `whatis` liefert, stammt aus dem Abschnitt `NAME` der Handbuchseite des Befehls. Wenn ein Name mehrere Handbuchseiten in verschiedenen Abschnitten hat, kann `whatis` mehr als eine Zeile anzeigen.

```bash
$ whatis passwd
passwd (1)           - change user password
passwd (5)           - the password file
```

Die Zahl in Klammern ist der Abschnitt der Manpage.

### Whatis vs Man vs Apropos

- `whatis ls`: Zeigt eine einzeilige Beschreibung für einen exakten Befehlsnamen.
- `man ls`: Öffnet die vollständige Handbuchseite.
- `apropos keyword`: Durchsucht die Beschreibungen der Manpages nach einem Stichwort.

Zum Beispiel:

```bash
$ apropos password
```

Verwende `whatis`, wenn du den Befehlsnamen kennst, aber vergessen hast, was er macht.

### Häufige Fragen

**Warum sagt whatis "nothing appropriate"?** Der Befehl hat möglicherweise keine installierte Manpage, oder die Man-Datenbank muss aktualisiert werden.

**Zeigt whatis Befehlsoptionen an?** Nein. Verwende `man BEFEHL` oder `BEFEHL --help` für Optionen.

**Ist whatis dasselbe wie which?** Nein. `whatis` beschreibt einen Befehl. `which` zeigt den Pfad zur ausführbaren Datei an.

## Exercise

Übung macht den Meister! Obwohl es kein spezielles Labor für den Befehl `whatis` gibt, ist es wichtig zu verstehen, wie man Informationen über Befehle und Dateien findet. Hier sind einige praktische Labs, um dein Verständnis für das Auffinden von Befehlen und Dateien in Linux zu vertiefen:

1. **[Linux which Command: Command Locating](https://labex.io/de/labs/linux-linux-which-command-command-locating-215210)** – Übe die Verwendung des Befehls `which`, um ausführbare Dateien zu finden und die Priorität von Befehlen im PATH deines Systems zu verstehen.
2. **[Linux whereis Command: File and Command Finding](https://labex.io/de/labs/linux-linux-whereis-command-file-and-command-finding-215211)** – Lerne, `whereis` zu verwenden, um Binärdateien, Quellcode und Handbuchseiten von Befehlen zu finden und so dein Verständnis der Befehlsstruktur zu vertiefen.
3. **[Discover Critical System Resources](https://labex.io/de/labs/linux-discover-critical-system-resources-388032)** – Diese Herausforderung kombiniert `which`, `whereis` und `find`, um dir zu helfen, effizient im Dateisystem zu navigieren und wichtige Systemressourcen zu entdecken.

Diese Labs helfen dir, die Konzepte der Befehls- und Dateisuche in realen Szenarien anzuwenden und Vertrauen im Umgang mit wichtigen Linux-Dienstprogrammen zu gewinnen.

## Quiz Question

Welchen Befehl kannst du verwenden, um eine kurze Beschreibung eines Befehls zu sehen? Bitte antworte auf Englisch und achte auf Kleinbuchstaben.

## Quiz Answer

whatis
