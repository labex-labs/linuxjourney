---
lang: "de"
title: "less"
meta_title: "less - Command Line"
meta_description: "Erfahren Sie, wie Sie den Linux-Befehl 'less' für effizientes Anzeigen und Navigieren in Textdateien verwenden. Meistern Sie das Paging, Suchen und Beenden mit dieser anfängerfreundlichen Anleitung."
meta_keywords: "less command, Linux less, Textdateien anzeigen, Dateien navigieren, Linux Tutorial, Linux für Anfänger, Linux Anleitung"
---

## Lesson Content

Wenn Sie Textdateien anzeigen, die größer als eine einfache Ausgabe sind, ist `less` mehr. (Es gibt tatsächlich einen Befehl namens `more`, der etwas Ähnliches tut, daher ist dies ironisch.) Der Text wird seitenweise angezeigt, sodass Sie eine Textdatei Seite für Seite navigieren können.

Sehen Sie sich den Inhalt einer Datei mit `less` an. Sobald Sie sich im `less`-Befehl befinden, können Sie tatsächlich andere Tastaturbefehle verwenden, um in der Datei zu navigieren.

```bash
less /home/pete/Documents/text1
```

Verwenden Sie die folgenden Befehle, um durch `less` zu navigieren:

- `q` – Wird verwendet, um `less` zu beenden und zu Ihrer Shell zurückzukehren.
- `Page up`, `Page down`, `Up` und `Down` – Navigieren Sie mit den Pfeiltasten und den Seitentasten.
- `g` – Bewegt sich an den Anfang der Textdatei.
- `G` – Bewegt sich an das Ende der Textdatei.
- `/search` – Sie können nach bestimmten Texten innerhalb des Textdokuments suchen. Stellen Sie den Wörtern, nach denen Sie suchen möchten, ein `/` voran.
- `h` – Wenn Sie ein wenig Hilfe zur Verwendung von `less` benötigen, während Sie sich in `less` befinden, verwenden Sie Hilfe.

## Exercise

Führen Sie `less` für eine Datei aus, blättern Sie dann in der Datei nach oben und unten. Versuchen Sie, nach einem bestimmten Wort zu suchen. Navigieren Sie schnell zum Anfang oder Ende der Datei.

## Quiz Question

Wie beendet man einen `less`-Befehl?

## Quiz Answer

q
