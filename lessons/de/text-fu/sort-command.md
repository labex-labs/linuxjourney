---
lang: "de"
title: "sort"
description: "Lernen Sie, wie Sie den Linux-Befehl sort zum Sortieren von Textdateien verwenden. Entdecken Sie Optionen wie umgekehrte und numerische Sortierung. Verbessern Sie Ihre Linux-Befehlszeilenkenntnisse!"
keywords: "Linux sort Befehl, sort -r, sort -n, Linux Tutorial, Befehlszeile, Linux für Anfänger, sort Anleitung"
---

## Lesson Content

Der Befehl `sort` ist nützlich zum Sortieren von Zeilen.

```plaintext
file1.txt
dog
cow
cat
elephant
bird

$ sort file1.txt
bird
cat
cow
dog
elephant
```

Sie können auch eine umgekehrte Sortierung vornehmen:

```bash
$ sort -r file1.txt
elephant
dog
cow
cat
bird
```

Und auch nach numerischem Wert sortieren:

```bash
$ sort -n file1.txt
bird
cat
cow
elephant
dog
```

## Exercise

Die wahre Stärke von `sort` liegt in seiner Fähigkeit, mit anderen Befehlen kombiniert zu werden. Probieren Sie den folgenden Befehl aus und sehen Sie, was passiert:

```bash
ls /etc | sort -rn
```

## Quiz Question

Welches Flag verwenden Sie, um eine umgekehrte Sortierung durchzuführen?

## Quiz Answer

-r
