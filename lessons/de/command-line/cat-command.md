---
index: 7
lang: "de"
title: "cat"
meta_title: "cat - Kommandozeile"
meta_description: "Lernen Sie den Linux-Befehl cat mit Beispielen zum Anzeigen von Dateien, Verketten von Dateien, Nummerieren von Zeilen, Erstellen von Dateien und sicherer Verwendung von Umleitungen."
meta_keywords: "linux cat befehl, cat befehl, datei anzeigen linux, dateien verketten, cat -n, cat -b, cat umleitung, linux cat"
---

## Lesson Content

Nachdem Sie gelernt haben, sich im Dateisystem zu bewegen, ist der nächste Schritt, den Inhalt von Dateien anzusehen. Ein grundlegendes und vielseitiges Werkzeug dafür ist der Befehl `cat`. Der Name `cat` steht für "concatenate" (verketten), was auf seine Fähigkeit hinweist, Dateien zusammenzufügen.

### Anzeige von Datei-Inhalten

Die einfachste Verwendung des Befehls `cat` ist das direkte Anzeigen des Inhalts einer einzelnen Datei im Terminal.

```bash
$ cat myfile.txt
```

Dieser Befehl gibt den gesamten Inhalt von `myfile.txt` auf dem Bildschirm aus. Das ist perfekt für kurze Konfigurationsdateien oder Textausschnitte, aber nicht ideal für große Dateien, da der Text sehr schnell durchscrollt. Werkzeuge, die besser für große Dateien geeignet sind, behandeln wir in einer späteren Lektion.

### Dateien verketten

Ganz im Sinne seines Namens kann `cat` mehrere Dateien zusammenfügen und die kombinierte Ausgabe anzeigen. Es liest die Dateien in der angegebenen Reihenfolge und gibt sie nacheinander aus.

```bash
$ cat dogfile birdfile
```

Dieser Befehl zeigt zuerst den Inhalt von `dogfile` und direkt danach den Inhalt von `birdfile` an.

Um die kombinierte Ausgabe in einer neuen Datei zu speichern, verwenden Sie eine Umleitung:

```bash
$ cat dogfile birdfile > animals
```

### Dateien mit Umleitung erstellen

Sie können `cat` auch mit dem Ausgabenumleitungsoperator (`>`) verwenden, um neue Dateien zu erstellen. Dies ist eine schnelle Möglichkeit, Text direkt im Terminal in eine Datei zu schreiben.

```bash
$ cat > newfile.txt
```

Nach Ausführung dieses Befehls können Sie Ihren Text eingeben. Drücken Sie `Ctrl+D` in einer neuen Zeile, um zu speichern und zu beenden. Dadurch wird `newfile.txt` mit dem eingegebenen Text erstellt. Seien Sie vorsichtig, denn die Verwendung von `>` bei einer bestehenden Datei überschreibt diese vollständig.

Um an eine Datei anzuhängen, statt sie zu überschreiben, verwenden Sie `>>`.

```bash
$ cat >> notes.txt
```

### Häufige Optionen des cat-Befehls

Der Befehl `cat` hat mehrere Optionen, um sein Verhalten zu ändern.

- `-n`: Nummeriert alle Ausgabzeilen, beginnend mit 1.
- `-b`: Nummeriert nur nicht-leere Ausgabzeilen.
- `-s`: Komprimiert mehrere aufeinanderfolgende Leerzeilen zu einer einzigen.
- `-A`: Zeigt nicht druckbare Zeichen, Tabs und Zeilenenden an.

Beispiele:

```bash
$ cat -n script.sh
$ cat -b notes.txt
$ cat -s messy.txt
```

### Wann man cat nicht verwenden sollte

Verwenden Sie `cat` für kurze Dateien. Für lange Dateien nutzen Sie `less`, damit Sie scrollen, suchen und ohne Überflutung des Terminals beenden können.

```bash
$ less /var/log/syslog
```

### Häufige Fragen

**Wofür steht cat?** Es steht für concatenate (verketten).

**Kann cat eine Datei bearbeiten?** Nicht interaktiv. Es kann Dateien mit Umleitung erstellen oder überschreiben, aber ein Texteditor ist besser zum Bearbeiten geeignet.

**Was ist der Unterschied zwischen > und >>?** `>` überschreibt eine Datei. `>>` hängt an das Ende einer Datei an.

## Exercise

Übung macht den Meister! Hier sind einige praktische Labs, um Ihr Verständnis für das Anzeigen von Datei-Inhalten zu vertiefen:

1. **[Linux cat Command: File Concatenating](https://labex.io/de/labs/linux-linux-cat-command-file-concatenating-210986)** – Lernen Sie den `cat`-Befehl zum Anzeigen, Verketten und Bearbeiten von Textdateien und verbessern Sie Ihre Kommandozeilenfähigkeiten für effizientes Arbeiten mit Textdateien.
2. **[Viewing Log and Configuration Files in Linux](https://labex.io/de/labs/linux-viewing-log-and-configuration-files-in-linux-387914)** – Üben Sie den Einsatz von Befehlen wie `cat`, um Textdateien, einschließlich Systemprotokollen und Konfigurationsdateien, effizient anzuzeigen und zu durchsuchen, um wichtige Informationen zu extrahieren.

Diese Labs helfen Ihnen, die Konzepte in realen Szenarien anzuwenden und Vertrauen im Umgang mit Datei-Inhalten unter Linux zu gewinnen.

## Quiz Question

Welcher Befehl wird verwendet, um den Inhalt einer Datei in der Kommandozeile anzuzeigen? (Hinweis: Ihre Antwort sollte ein einzelnes, kleingeschriebenes englisches Wort sein.)

## Quiz Answer

cat
