---
lang: "de"
title: "tr (Übersetzen)"
meta_title: "tr (Übersetzen) - Text-Fu"
meta_description: "Erfahren Sie, wie Sie den Linux-Befehl 'tr' verwenden, um Zeichen zu übersetzen und zu löschen. Verstehen Sie die Zeichenübersetzung mit Beispielen und Übungen. Beginnen Sie Ihre Linux-Reise!"
meta_keywords: "tr Befehl, Linux tr, Zeichen übersetzen, Zeichen löschen, Linux Tutorial, Linux für Anfänger, Linux Anleitung"
---

## Lesson Content

Der `tr` (translate) Befehl ermöglicht es Ihnen, einen Zeichensatz in einen anderen Zeichensatz zu übersetzen. Versuchen wir ein Beispiel, bei dem alle Kleinbuchstaben in Großbuchstaben übersetzt werden.

```bash
$ tr a-z A-Z
hello
HELLO
```

Wie Sie sehen können, haben wir die Bereiche von `a-z` in `A-Z` umgewandelt, und jeder Text, den wir eingeben und der klein geschrieben ist, wird groß geschrieben.

## Exercise

Probieren Sie den folgenden Befehl aus. Was passiert?

```bash
$ tr -d ello
hello
```

## Quiz Question

Welcher Befehl wird verwendet, um Zeichen zu übersetzen?

## Quiz Answer

tr
