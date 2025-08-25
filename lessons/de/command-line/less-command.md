---
index: 8
lang: "de"
title: "less"
meta_title: "less - Befehlszeile"
meta_description: "Erfahren Sie, wie Sie den Linux-Befehl 'less' für effizientes Anzeigen und Navigieren von Textdateien verwenden. Meistern Sie das Paging, Suchen und Beenden mit dieser anfängerfreundlichen Anleitung."
meta_keywords: "less Befehl, Linux less, Textdateien anzeigen, Dateien navigieren, Linux Tutorial, Linux für Anfänger, Linux Anleitung"
---

## Lesson Content

Wenn Sie Textdateien anzeigen, die größer als eine einfache Ausgabe sind, ist `less` mehr. (Es gibt tatsächlich einen Befehl namens `more`, der etwas Ähnliches tut, was ironisch ist.) Der Text wird seitenweise angezeigt, sodass Sie eine Textdatei Seite für Seite durchsuchen können.

Sehen Sie sich den Inhalt einer Datei mit `less` an. Sobald Sie sich im `less`-Befehl befinden, können Sie tatsächlich andere Tastaturbefehle verwenden, um in der Datei zu navigieren.

```bash
less /home/pete/Documents/text1
```

Verwenden Sie die folgenden Befehle, um durch `less` zu navigieren:

- `q` - Wird verwendet, um `less` zu beenden und zu Ihrer Shell zurückzukehren.
- `Page up`, `Page down`, `Up` und `Down` - Navigieren Sie mit den Pfeiltasten und den Seitentasten.
- `g` - Bewegt sich an den Anfang der Textdatei.
- `G` - Bewegt sich an das Ende der Textdatei.
- `/search` - Sie können nach bestimmtem Text innerhalb des Textdokuments suchen. Stellen Sie den Wörtern, nach denen Sie suchen möchten, ein `/` voran.
- `h` - Wenn Sie ein wenig Hilfe zur Verwendung von `less` benötigen, während Sie sich in `less` befinden, verwenden Sie Hilfe.

## Exercise

Übung macht den Meister! Hier sind einige praktische Übungen, um Ihr Verständnis des Anzeigens und Navigierens von Textdateien in Linux zu vertiefen:

1. **[Linux less Befehl: Dateiseitenumbruch](https://labex.io/de/labs/linux-linux-less-command-file-paging-214301)** - Lernen Sie den Linux-Befehl 'less' für effizientes Anzeigen und Navigieren von Textdateien, einschließlich Suche, Zeilennummern und Musterabgleich.
2. **[Linux more Befehl: Dateiscrolling](https://labex.io/de/labs/linux-linux-more-command-file-scrolling-214299)** - Lernen Sie den Linux-Befehl 'more' für effizientes Anzeigen von Textdateien, einschließlich grundlegender Verwendung, Starten von bestimmten Zeilen und Anpassen der Anzeige.
3. **[Anzeigen von Log- und Konfigurationsdateien in Linux](https://labex.io/de/labs/linux-viewing-log-and-configuration-files-in-linux-387914)** - Lernen Sie grundlegende Linux-Befehlszeilenkenntnisse für das effiziente Anzeigen und Navigieren von Textdateien, einschließlich Systemprotokollen und Konfigurationsdateien, mithilfe von Befehlen wie `cat`, `more` und `less`.

Diese Übungen helfen Ihnen, die Konzepte in realen Szenarien anzuwenden und Vertrauen in die Textdateimanipulation und -navigation aufzubauen.

## Quiz Question

Wie beenden Sie einen `less`-Befehl?

## Quiz Answer

q
