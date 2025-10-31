---
index: 14
lang: "de"
title: "uniq (Eindeutig)"
meta_title: "uniq (Eindeutig) - Text-Fu"
meta_description: "Erkunden Sie den uniq-Befehl in Linux, um doppelte benachbarte Zeilen aus Text zu filtern und zu entfernen. Erfahren Sie, wie Sie das uniq Linux-Tool mit Optionen wie -c, -u, -d verwenden und es mit sort für leistungsstarke Textverarbeitung kombinieren."
meta_keywords: "uniq Befehl, Linux uniq, uniq linux, Duplikate entfernen, sort uniq, Textverarbeitung, Datenbereinigung, Linux Tutorial"
---

## Lesson Content

Der `uniq` (unique) Befehl ist ein wesentliches Werkzeug zur Textverarbeitung unter Linux. Er hilft Ihnen dabei, doppelte Zeilen in einer Textdatei zu filtern und zu verwalten, aber es ist wichtig zu verstehen, wie er funktioniert, um ihn effektiv einzusetzen.

### Entfernen einfacher Duplikate

Die Hauptfunktion des `uniq`-Befehls besteht darin, doppelte benachbarte Zeilen zu entfernen. Stellen Sie sich vor, Sie haben eine Datei namens `reading.txt` mit folgendem Inhalt:

```plaintext
book
book
paper
paper
article
article
magazine
```

Um die wiederholten Zeilen zu entfernen, können Sie den `uniq`-Befehl ausführen:

```bash
$ uniq reading.txt
book
paper
article
magazine
```

Wie Sie sehen, gibt `uniq` eine Version der Datei aus, bei der die doppelten benachbarten Zeilen entfernt wurden.

### Erweiterte Filteroptionen

Der `uniq`-Befehl bietet auch verschiedene Optionen für eine detailliertere Analyse.

Um die Vorkommen jeder Zeile zu zählen, verwenden Sie das Flag `-c` (count):

```bash
$ uniq -c reading.txt
      2 book
      2 paper
      2 article
      1 magazine
```

Um nur die Zeilen anzuzeigen, die nicht wiederholt werden (d. h. eindeutig sind), verwenden Sie das Flag `-u` (unique):

```bash
$ uniq -u reading.txt
magazine
```

Umgekehrt verwenden Sie das Flag `-d` (duplicated), um nur die Zeilen anzuzeigen, die wiederholt werden:

```bash
$ uniq -d reading.txt
book
paper
article
```

### Die Bedeutung des Sortierens

Ein entscheidendes Detail beim **uniq linux** Befehl ist, dass er doppelte Zeilen nur erkennt, wenn sie direkt nebeneinander liegen. Wenn die Duplikate über die Datei verstreut sind, erkennt `uniq` sie nicht.

Betrachten Sie diese Version von `reading.txt`, bei der die Duplikate nicht benachbart sind:

```plaintext
book
paper
book
paper
article
magazine
article
```

Wenn Sie `uniq` auf dieser Datei ausführen, erhalten Sie ein überraschendes Ergebnis:

```bash
$ uniq reading.txt
book
paper
book
paper
article
magazine
article
```

Es wurden keine Zeilen entfernt, da keine zwei identischen Zeilen direkt nebeneinander standen. Um dieses Problem zu lösen, müssen Sie zuerst den Inhalt der Datei sortieren. Indem Sie die Ausgabe von `sort` in `uniq` umleiten (pipen), stellen Sie sicher, dass alle identischen Zeilen benachbart werden, sodass `uniq` korrekt arbeiten kann. Diese Kombination ist ein leistungsstarkes und häufiges Muster im Shell-Scripting.

```bash
$ sort reading.txt | uniq
article
book
magazine
paper
```

Dieser Befehl sortiert zuerst die Zeilen alphabetisch, dann filtert `uniq` die Duplikate heraus und liefert Ihnen eine saubere Liste eindeutiger Einträge.

## Exercise

Übung macht den Meister! Hier sind einige praktische Übungen, um Ihr Verständnis der Textverarbeitung mit `uniq` und `sort` zu festigen:

1. **[Linux uniq Befehl: Duplikate filtern](https://labex.io/de/labs/linux-linux-uniq-command-duplicate-filtering-219199)** - Lernen Sie, wie Sie den Linux `uniq`-Befehl in Kombination mit `sort` verwenden, um doppelte Zeilen in Textdateien zu identifizieren, zu filtern und zu analysieren.
2. **[Linux sort Befehl: Text sortieren](https://labex.io/de/labs/linux-linux-sort-command-text-sorting-219196)** - Üben Sie die Verwendung des `sort`-Befehls, um Zeilen von Textdateien zu organisieren, ein entscheidender Schritt, bevor Sie `uniq` effektiv einsetzen können.
3. **[Wortanzahl und Sortierung](https://labex.io/de/labs/linux-word-count-and-sorting-388125)** - Lernen Sie in dieser praktischen Herausforderung die wesentlichen Linux-Textverarbeitungswerkzeuge `wc` (Wortanzahl) und `sort` kennen. Erfahren Sie, wie Sie Zeilen, Wörter und Zeichen zählen, häufige Muster finden und Daten effizient für verschiedene Textanalysen sortieren.

Diese Labs helfen Ihnen, die Konzepte in realen Szenarien anzuwenden und Selbstvertrauen beim Umgang mit Textverarbeitung und Datenmanipulation unter Linux aufzubauen.

## Quiz Question

Welchen Befehl würden Sie verwenden, um benachbarte doppelte Zeilen in einer Datei zu entfernen? Bitte antworten Sie nur mit dem Befehlsnamen in kleingeschriebenen englischen Buchstaben.

## Quiz Answer

uniq
