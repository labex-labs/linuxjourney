---
index: 15
lang: "de"
title: "wc und nl"
meta_title: "wc und nl - Text-Fu"
meta_description: "Lernen Sie die Linux-Befehle wc und nl. Verstehen Sie Wortzählung, Zeilennummerierung und Dateianalyse. Verbessern Sie noch heute Ihre Linux-Kommandozeilenkenntnisse!"
meta_keywords: "wc Befehl, nl Befehl, Linux Wortzählung, Linux Zeilennummern, Dateianalyse, Linux Tutorial, Linux für Anfänger, Linux Anleitung"
---

## Lesson Content

Der Befehl `wc` (word count) zeigt die Gesamtzahl der Wörter in einer Datei an.

```bash
$ wc /etc/passwd
 96     265    5925 /etc/passwd
```

Er zeigt die Anzahl der Zeilen, die Anzahl der Wörter bzw. die Anzahl der Bytes an.

Um nur die Anzahl eines bestimmten Feldes anzuzeigen, verwenden Sie die Optionen `-l`, `-w` oder `-c`.

```bash
$ wc -l /etc/passwd
96
```

Ein weiterer Befehl, den Sie verwenden können, um die Zeilenanzahl in einer Datei zu überprüfen, ist der Befehl `nl` (number lines).

```plaintext
file1.txt
i
like
turtles
```

```bash
$ nl file1.txt
1. i
2. like
3. turtles
```

## Exercise

Wie würden Sie die Gesamtzahl der Zeilen mit dem Befehl `nl` ermitteln, ohne die gesamte Ausgabe durchsuchen zu müssen? Tipp: Verwenden Sie einige der anderen Befehle, die Sie in diesem Kurs gelernt haben.

## Quiz Question

Welchen Befehl würden Sie verwenden, um die Gesamtzahl der Wörter in einer Datei und nur die Wörter zu erhalten?

## Quiz Answer

wc -w
