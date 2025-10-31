---
index: 8
lang: "de"
title: "Kopf"
meta_title: "head - Text-Fu"
meta_description: "Ein Linux-Leitfaden für Anfänger zur Verwendung des head-Befehls, um den Anfang einer Datei anzuzeigen. Erfahren Sie, wie Sie die Option head -n verwenden, um die Zeilenanzahl zu steuern – eine wesentliche Fähigkeit für jedes Linux-Tutorial."
meta_keywords: "head-Befehl, Linux head, Dateianfang anzeigen, Linux-Tutorial, Linux-Befehle, Linux für Anfänger, head -n, Linux-Leitfaden, Textdateien, Kommandozeile"
---

## Lesson Content

Unter Linux müssen Sie oft den Inhalt sehr großer Dateien inspizieren, wie z. B. Systemprotokolle. Wenn Sie beispielsweise `cat /var/log/syslog` ausführen, sehen Sie Seiten von Text, die vorbeiscrollen, was es schwierig macht, einen schnellen Überblick zu bekommen. Was aber, wenn Sie nur **den Anfang einer Datei anzeigen** möchten? Der Befehl `head` ist das perfekte Werkzeug für diese Aufgabe.

### Standardverhalten des head-Befehls

Standardmäßig zeigt der `head`-Befehl die ersten 10 Zeilen jeder angegebenen Datei an. Dies ist ein grundlegender Bestandteil unseres **Linux-Leitfadens für Anfänger** im Umgang mit Text. Um ihn in Aktion zu sehen, geben Sie einfach einen Dateinamen als Argument an:

```bash
head /var/log/syslog
```

Dieser Befehl gibt die ersten 10 Zeilen aus `/var/log/syslog` aus, sodass Sie den Anfangsinhalt der Datei schnell überprüfen können, ohne sie in einem Editor zu öffnen.

### Anpassung der Zeilenanzahl

Der **Linux head**-Befehl ist flexibel. Sie können die Anzahl der angezeigten Zeilen einfach mit der Option `-n` ändern, was für „Anzahl der Zeilen“ steht. Wenn Sie beispielsweise die ersten 15 Zeilen einer Datei sehen möchten, verwenden Sie die Option `head -n` wie folgt:

```bash
head -n 15 /var/log/syslog
```

Dies macht `head` zu einem der nützlichsten **Linux-Befehle** zur schnellen Überprüfung von Dateikopfzeilen oder Protokolleinträgen.

## Exercise

Übung macht den Meister! Hier sind einige praktische Übungen, um Ihr Verständnis für die Anzeige des Anfangs von Dateien und die allgemeine Textdateiverwaltung zu festigen:

1. **[Linux head Befehl: Anzeige des Dateianfangs](https://labex.io/de/labs/linux-linux-head-command-file-beginning-display-214302)** – Dieses Labor führt Sie durch die Verwendung des `head`-Befehls zur Anzeige der Anfangszeilen von Textdateien, einschließlich der Änderung der Zeilenanzahl.
2. **[Anzeigen von Protokoll- und Konfigurationsdateien in Linux](https://labex.io/de/labs/linux-viewing-log-and-configuration-files-in-linux-387914)** – Üben Sie wesentliche Linux-Kommandozeilenfähigkeiten zur effizienten Anzeige und Navigation von Textdateien, einschließlich Systemprotokollen und Konfigurationsdateien, die oft Befehle wie `head` erfordern.
3. **[Schnelle Bedrohungserkennung](https://labex.io/de/labs/linux-rapid-threat-detection-387930)** – Wenden Sie Ihr Wissen über `head` (und `tail`) an, um schnell aktuelle Protokolleinträge zu extrahieren und zu analysieren, was reale Cybersicherheitsanalysen simuliert.

Diese Labore helfen Ihnen, die Konzepte in realen Szenarien anzuwenden und Vertrauen in die Anzeige und Analyse von Textdateien unter Linux aufzubauen.

## Quiz Question

Welche Option würden Sie beim `head`-Befehl verwenden, um die Anzahl der anzuzeigenden Zeilen zu ändern? Bitte antworten Sie nur mit der englischen Option und achten Sie auf die Groß-/Kleinschreibung.

## Quiz Answer

-n
