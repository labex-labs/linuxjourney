---
index: 7
lang: "de"
title: "Katze"
meta_title: "Katze - Befehlszeile"
meta_description: "Meistern Sie den Linux-Katzenbefehl, um Dateien anzuzeigen, zu erstellen und zu verketten. Diese Anleitung behandelt die grundlegende Verwendung, gängige Optionen und wie man cat linux mit Umleitung wie linux cat > verwendet."
meta_keywords: "linux cat befehl, cat linux, cat handbuch linux, linux cat >, dateiinhalte anzeigen, dateien verketten, linux befehle, befehlszeile"
---

## Lesson Content

Nachdem Sie gelernt haben, im Dateisystem zu navigieren, besteht der nächste Schritt darin, den Inhalt von Dateien anzuzeigen. Ein grundlegendes und vielseitiges Werkzeug dafür ist der `linux cat Befehl`. Der Name `cat` ist die Kurzform für „concatenate“ (verketten), was auf seine Fähigkeit hindeutet, Dateien miteinander zu verknüpfen.

### Anzeigen von Dateiinhalt

Die grundlegendste Verwendung des `cat`-Befehls besteht darin, den Inhalt einer einzelnen Datei direkt im Terminal anzuzeigen.

```bash
cat myfile.txt
```

Dieser Befehl gibt den gesamten Inhalt von `myfile.txt` auf dem Bildschirm aus. Obwohl dies perfekt für kurze Konfigurationsdateien oder Textausschnitte ist, ist es nicht ideal für die Anzeige großer Dateien, da der Text sehr schnell durchläuft. Werkzeuge, die besser für große Dateien geeignet sind, behandeln wir in einer späteren Lektion.

### Dateien verketten (Konkatenieren)

Getreu seinem Namen kann `cat` mehrere Dateien kombinieren oder verketten und deren kombinierten Inhalt ausgeben. Das Dienstprogramm `cat linux` liest die Dateien in der angegebenen Reihenfolge und gibt sie nacheinander aus.

```bash
cat dogfile birdfile
```

Dieser Befehl zeigt zuerst den Inhalt von `dogfile` an, gefolgt vom Inhalt von `birdfile`.

### Erstellen von Dateien mit Umleitung

Sie können `cat` auch mit dem Umleitungsoperator (`>`) verwenden, um neue Dateien zu erstellen. Die Kombination `linux cat >` ist eine schnelle Methode, um Text direkt vom Terminal in eine Datei zu schreiben.

```bash
cat > newfile.txt
```

Nach der Ausführung dieses Befehls können Sie Ihren Text eingeben. Drücken Sie `Strg+D` in einer neuen Zeile, um zu speichern und zu beenden. Dadurch wird `newfile.txt` mit dem von Ihnen eingegebenen Text erstellt. Seien Sie vorsichtig, da die Verwendung von `>` bei einer vorhandenen Datei diese vollständig überschreibt.

### Häufige cat Befehlsoptionen

Der `cat`-Befehl verfügt über mehrere Optionen, um sein Verhalten zu ändern. Hier sind ein paar gängige:

- `-n`: Diese Option nummeriert alle Ausgabzeilen, beginnend mit 1.
- `-b`: Diese Option nummeriert nur die nicht leeren Ausgabzeilen.

Für eine vollständige Liste der Funktionen können Sie jederzeit die `cat manual linux`-Seite aufrufen, indem Sie `man cat` in Ihr Terminal eingeben.

## Exercise

Übung macht den Meister! Hier sind einige praktische Übungen, um Ihr Verständnis der Anzeige von Dateiinhalten zu festigen:

1. **[Linux cat Befehl: Dateiverkettung](https://labex.io/de/labs/linux-linux-cat-command-file-concatenating-210986)** - Lernen Sie den `cat`-Befehl zum Anzeigen, Verketten und Bearbeiten von Textdateien kennen und verbessern Sie Ihre Kommandozeilenfähigkeiten für die effiziente Textdateiverwaltung.
2. **[Anzeigen von Protokoll- und Konfigurationsdateien in Linux](https://labex.io/de/labs/linux-viewing-log-and-configuration-files-in-linux-387914)** - Üben Sie die Verwendung von Befehlen wie `cat`, um Textdateien, einschließlich Systemprotokollen und Konfigurationsdateien, effizient anzuzeigen und zu durchsuchen, um kritische Informationen zu extrahieren.

Diese Labs helfen Ihnen, die Konzepte in realen Szenarien anzuwenden und Vertrauen in die Anzeige von Dateiinhalten unter Linux aufzubauen.

## Quiz Question

Welcher Befehl wird verwendet, um den Inhalt einer Datei auf der Kommandozeile anzuzeigen? (Hinweis: Ihre Antwort sollte ein einzelnes, kleingeschriebenes englisches Wort sein.)

## Quiz Answer

cat
