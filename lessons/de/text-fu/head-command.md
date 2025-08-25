---
index: 8
lang: "de"
title: "head"
meta_title: "head - Text-Fu"
meta_description: "Erfahren Sie, wie Sie den Linux-Befehl 'head' verwenden, um den Anfang von Dateien anzuzeigen. Verstehen Sie Optionen wie -n für die Zeilenanzahl. Ein unverzichtbares Linux-Befehls-Tutorial."
meta_keywords: "head Befehl, Linux head, Dateianfang anzeigen, Linux Tutorial, Linux Befehle, Linux für Anfänger, head -n, Linux Anleitung"
---

## Lesson Content

Nehmen wir an, wir haben eine sehr lange Datei; tatsächlich haben wir viele zur Auswahl. Führen Sie `cat /var/log/syslog` aus. Sie sollten seitenweise Text sehen. Was wäre, wenn ich nur die ersten paar Zeilen dieser Textdatei sehen wollte? Nun, das können wir mit dem Befehl `head` tun. Standardmäßig zeigt der Befehl `head` die ersten 10 Zeilen einer Datei an.

```bash
head /var/log/syslog
```

Sie können die Zeilenanzahl auch nach Belieben ändern. Nehmen wir an, ich wollte stattdessen die ersten 15 Zeilen sehen.

```bash
head -n 15 /var/log/syslog
```

Das Flag `-n` steht für „Anzahl der Zeilen“.

## Exercise

Übung macht den Meister! Hier sind einige praktische Übungen, um Ihr Verständnis für das Anzeigen des Dateianfangs und die allgemeine Textdateibearbeitung zu vertiefen:

1. **[Linux head Befehl: Dateianfang anzeigen](https://labex.io/de/labs/linux-linux-head-command-file-beginning-display-214302)** – Dieses Lab führt Sie durch die Verwendung des `head`-Befehls, um die ersten Zeilen von Textdateien anzuzeigen, einschließlich der Änderung der Zeilenanzahl.
2. **[Anzeigen von Log- und Konfigurationsdateien in Linux](https://labex.io/de/labs/linux-viewing-log-and-configuration-files-in-linux-387914)** – Üben Sie grundlegende Linux-Befehlszeilenkenntnisse für das effiziente Anzeigen und Navigieren in Textdateien, einschließlich Systemprotokollen und Konfigurationsdateien, die oft Befehle wie `head` erfordern.
3. **[Schnelle Bedrohungserkennung](https://labex.io/de/labs/linux-rapid-threat-detection-387930)** – Wenden Sie Ihr Wissen über `head` (und `tail`) an, um schnell aktuelle Protokolleinträge zu extrahieren und zu analysieren, wodurch eine reale Cybersicherheitsanalyse simuliert wird.

Diese Labs helfen Ihnen, die Konzepte in realen Szenarien anzuwenden und Vertrauen beim Anzeigen und Analysieren von Textdateien in Linux aufzubauen.

## Quiz Question

Welches Flag würden Sie verwenden, um die Anzahl der Zeilen zu ändern, die Sie für den `head`-Befehl anzeigen möchten?

## Quiz Answer

-n
