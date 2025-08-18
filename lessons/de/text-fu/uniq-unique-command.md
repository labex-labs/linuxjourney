---
lang: "de"
title: "uniq (Eindeutig)"
meta_description: "Erfahren Sie, wie Sie den Linux-Befehl `uniq` verwenden, um doppelte Zeilen aus Textdateien zu entfernen. Entdecken Sie Optionen wie -c, -u, -d und kombinieren Sie ihn mit `sort` für eine effektive Datenbereinigung."
meta_keywords: "uniq Befehl, Linux uniq, Duplikate entfernen, sort uniq, Linux Tutorial, Textverarbeitung, Linux für Anfänger, Linux Anleitung"
---

## Lesson Content

Der Befehl `uniq` (unique) ist ein weiteres nützliches Werkzeug zum Parsen von Text.

Nehmen wir an, Sie hätten eine Datei mit vielen Duplikaten:

```plaintext
reading.txt
book
book
paper
paper
article
article
magazine
```

Und Sie wollten die Duplikate entfernen; nun, Sie können den Befehl `uniq` verwenden:

```bash
$ uniq reading.txt
book
paper
article
magazine
```

Lassen Sie uns die Anzahl der Vorkommen einer Zeile ermitteln:

```bash
$ uniq -c reading.txt
2 book
2 paper
2 article
1 magazine
```

Lassen Sie uns nur eindeutige Werte erhalten:

```bash
$ uniq -u reading.txt
magazine
```

Lassen Sie uns nur doppelte Werte erhalten:

```bash
$ uniq -d reading.txt
book
paper
article
```

**Hinweis**: `uniq` erkennt doppelte Zeilen nur, wenn sie nebeneinander liegen. Zum Beispiel:

Nehmen wir an, Sie hätten eine Datei mit Duplikaten, die nicht nebeneinander liegen:

```plaintext
reading.txt
book
paper
book
paper
article
magazine
article
```

```bash
$ uniq reading.txt
reading.txt
book
paper
book
paper
article
magazine
article
```

Das von `uniq` zurückgegebene Ergebnis wird alle Einträge enthalten, im Gegensatz zum allerersten Beispiel.

Um diese Einschränkung von `uniq` zu überwinden, können wir `sort` in Kombination mit `uniq` verwenden:

```bash
$ sort reading.txt | uniq
article
book
magazine
paper
```

## Exercise

Welches Ergebnis würden Sie erhalten, wenn Sie `uniq -uc` versuchen würden?

## Quiz Question

Welchen Befehl würden Sie verwenden, um Duplikate in einer Datei zu entfernen?

## Quiz Answer

uniq
