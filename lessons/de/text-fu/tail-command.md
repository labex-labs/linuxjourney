---
index: 9
lang: "de"
title: "tail"
meta_title: "tail - Text-Fu"
meta_description: "Lernen Sie, wie Sie den `tail`-Befehl in Linux verwenden, um Dateiendungen anzuzeigen und Protokolle zu überwachen. Entdecken Sie `tail -f` für Echtzeit-Updates. Beginnen Sie Ihre Linux-Reise!"
meta_keywords: "tail Befehl, Linux tail, tail -f, Protokolle anzeigen, Linux Tutorial, Linux für Anfänger, Linux Anleitung"
---

## Lesson Content

Ähnlich wie der Befehl `head` zeigt Ihnen der Befehl `tail` standardmäßig die letzten 10 Zeilen einer Datei an.

```bash
tail /var/log/syslog
```

Zusammen mit `head` können Sie die Anzahl der Zeilen ändern, die Sie sehen möchten.

```bash
tail -n 10 /var/log/syslog
```

Eine weitere großartige Option, die Sie verwenden können, ist das Flag `-f` (follow); dies folgt der Datei, während sie wächst. Probieren Sie es aus und sehen Sie, was passiert.

```bash
tail -f /var/log/syslog
```

Ihre `syslog`-Datei wird sich ständig ändern, während Sie mit Ihrem System interagieren, und mit `tail -f` können Sie alles sehen, was dieser Datei hinzugefügt wird.

## Exercise

Übung macht den Meister! Hier sind einige praktische Übungen, um Ihr Verständnis des `tail`-Befehls und seiner Anwendungen zu vertiefen:

1. **[Linux tail Befehl: Dateiende anzeigen](https://labex.io/de/labs/linux-linux-tail-command-file-end-display-214303)** - Lernen Sie den Linux `tail`-Befehl zum Anzeigen und Überwachen des Endes von Textdateien, einschließlich der Option `-f` für Echtzeit-Updates.
2. **[Anzeigen von Log- und Konfigurationsdateien in Linux](https://labex.io/de/labs/linux-viewing-log-and-configuration-files-in-linux-387914)** - Üben Sie die Verwendung von `tail` (zusammen mit `cat` und `more`), um Log- und Konfigurationsdateien effizient anzuzeigen und zu navigieren, was für die Systemüberwachung entscheidend ist.
3. **[Schnelle Bedrohungserkennung](https://labex.io/de/labs/linux-rapid-threat-detection-387930)** - Wenden Sie Ihr Wissen über `tail` an, um aktuelle Log-Einträge schnell zu extrahieren und zu analysieren, wodurch eine schnelle Bedrohungserkennung im Kontext der Cybersicherheit simuliert wird.

Diese Übungen helfen Ihnen, die Konzepte des Anzeigens und Überwachens von Dateiinhalten in realen Szenarien anzuwenden und Vertrauen in den `tail`-Befehl aufzubauen.

## Quiz Question

Welches Flag wird verwendet, um einer Datei in `tail` zu folgen?

## Quiz Answer

-f
