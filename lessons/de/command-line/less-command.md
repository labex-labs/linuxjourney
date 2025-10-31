---
index: 8
lang: "de"
title: "less"
meta_title: "less - Befehlszeile"
meta_description: "Meistern Sie den Linux-Befehl less zur effizienten Anzeige von Textdateien. Diese Anleitung behandelt die Verwendung des Befehls less, die Navigation, die Durchführung einer Unix less-Suche und wie man less beendet."
meta_keywords: "less Befehl, Befehl less, less beenden, unix less Suche, linux less, Textdateien anzeigen, Dateien navigieren, linux Befehlszeile"
---

## Lesson Content

Wenn Textdateien angezeigt werden, die zu groß sind, um auf einen einzigen Bildschirm zu passen, ist der `less Befehl` ein unschätzbares Werkzeug. Wie das alte Unix-Sprichwort besagt: „weniger ist mehr.“ (Dies ist ein Wortspiel mit der Tatsache, dass es auch einen `more Befehl` mit ähnlicher Funktionalität gibt). Das Dienstprogramm `less` zeigt Text in einem seitenweisen Format an, sodass Sie Seite für Seite durch eine Datei navigieren können, ohne die gesamte Datei in den Speicher zu laden.

### Erste Schritte mit dem Less-Befehl

Um mit der Anzeige einer Datei zu beginnen, verwenden Sie einfach den `Befehl less`, gefolgt vom Dateinamen. Dadurch wird die Datei in der `less`-Oberfläche geöffnet.

```bash
less /home/pete/Documents/text1
```

Sobald Sie sich im `less`-Viewer befinden, funktionieren Ihre Standard-Shell-Befehle nicht mehr. Stattdessen verwenden Sie einen bestimmten Satz von Tasten, um durch den Text zu navigieren und mit ihm zu interagieren.

### Navigation und Steuerung

Sie können verschiedene Tasten verwenden, um sich durch das Dokument zu bewegen:

- **Pfeiltasten und Seitentasten**: Verwenden Sie `Page Up`, `Page Down`, `Up` (Pfeil nach oben) und `Down` (Pfeil nach unten), um zeilen- oder seitenweise zu navigieren.
- **Zum Anfang**: Drücken Sie `g`, um direkt zum Anfang der Textdatei zu springen.
- **Zum Ende**: Drücken Sie `G` (Umschalt + g), um zum Ende der Textdatei zu springen.
- **Hilfemenü**: Wenn Sie die Befehle innerhalb von `less` vergessen haben, drücken Sie einfach `h`, um eine hilfreiche Zusammenfassung anzuzeigen.

### Unix Less Suche

Eine leistungsstarke Funktion von `less` ist die Möglichkeit, nach Text zu suchen. Um eine `unix less Suche` durchzuführen, geben Sie `/` gefolgt von dem Text ein, den Sie finden möchten, und drücken Sie dann die Eingabetaste. Dadurch werden alle Vorkommen Ihres Suchbegriffs hervorgehoben.

- `/suchbegriff`: Sucht vorwärts nach „suchbegriff“.
- `?suchbegriff`: Sucht rückwärts nach „suchbegriff“.
- `n`: Springt zur nächsten Übereinstimmung des Suchbegriffs.
- `N`: Springt zur vorherigen Übereinstimmung.

### Wie man Less beendet

Wenn Sie mit der Anzeige der Datei fertig sind, müssen Sie wissen, wie Sie `less beenden` und zu Ihrer Eingabeaufforderung zurückkehren.

- **Beenden**: Drücken Sie einfach `q`, um den `less`-Viewer zu beenden und zu Ihrer Shell zurückzukehren.

Die Beherrschung des `less Befehls` ist eine grundlegende Fähigkeit für jeden, der mit der Linux-Kommandozeile arbeitet, da sie die Dateiinspektion wesentlich effizienter macht.

## Exercise

Übung macht den Meister! Hier sind einige praktische Übungen, um Ihr Verständnis für das Anzeigen und Navigieren von Textdateien in Linux zu festigen:

1. **[Linux less Befehl: Dateiseitenumbruch](https://labex.io/de/labs/linux-linux-less-command-file-paging-214301)** - Lernen Sie den Linux 'less'-Befehl für die effiziente Anzeige und Navigation von Textdateien kennen, einschließlich Suche, Zeilennummern und Musterabgleich.
2. **[Linux more Befehl: Dateiscrolling](https://labex.io/de/labs/linux-linux-more-command-file-scrolling-214299)** - Lernen Sie den Linux 'more'-Befehl für die effiziente Anzeige von Textdateien kennen, einschließlich der grundlegenden Verwendung, des Starts von bestimmten Zeilen und der Anpassung der Anzeige.
3. **[Anzeigen von Protokoll- und Konfigurationsdateien in Linux](https://labex.io/de/labs/linux-viewing-log-and-configuration-files-in-linux-387914)** - Lernen Sie wesentliche Linux-Kommandozeilenfähigkeiten für die effiziente Anzeige und Navigation von Textdateien, einschließlich Systemprotokollen und Konfigurationsdateien, mithilfe von Befehlen wie `cat`, `more` und `less`.

Diese Labs helfen Ihnen, die Konzepte in realen Szenarien anzuwenden und Vertrauen in die Textdateiverwaltung und -navigation aufzubauen.

## Quiz Question

Wie beenden Sie den `less`-Befehl? Bitte geben Sie den einzelnen Zeichenschlüssel als Antwort an. Hinweis: Die Antwort ist ein groß-/kleingeschriebener englischer Buchstabe.

## Quiz Answer

q
