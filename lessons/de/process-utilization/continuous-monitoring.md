---
index: 7
lang: "de"
title: "Kontinuierliche Überwachung"
meta_title: "Kontinuierliche Überwachung - Prozessauslastung"
meta_description: "Lernen Sie die kontinuierliche Linux-Systemüberwachung mit sar. Verstehen Sie Installation, Datenerfassung und wie Sie historische Ressourcennutzung für die Leistung analysieren. Legen Sie los!"
meta_keywords: "sar, sysstat, Linux-Überwachung, Systemleistung, kontinuierliche Überwachung, Anfänger, Tutorial, Anleitung"
---

## Lesson Content

Diese Überwachungstools sind gut, um sie zu betrachten, wenn Ihr Computer Probleme hat, aber was ist mit Computern, die Probleme haben, wenn Sie nicht hinschauen? Dafür benötigen Sie ein kontinuierliches Überwachungstool, das Ihre Systemaktivitätsinformationen sammelt, meldet und speichert. In dieser Lektion werden wir ein großartiges Tool vorstellen: **sar**.

### sar installieren

Sar ist ein Tool, das zur historischen Analyse Ihres Systems verwendet wird. Stellen Sie zunächst sicher, dass es installiert ist, indem Sie das Paket `sysstat` installieren: `sudo apt install sysstat`.

### Datenerfassung einrichten

Normalerweise beginnt Ihr System nach der Installation von `sysstat` automatisch mit der Datenerfassung. Falls nicht, können Sie dies aktivieren, indem Sie das Feld `ENABLED` in `/etc/default/sysstat` ändern.

### sar verwenden

```bash
sudo sar -q
```

Dieser Befehl listet die Details vom Beginn des Tages auf.

```bash
sudo sar -r
```

Dies listet die Details der Speichernutzung vom Beginn des Tages auf.

```bash
sudo sar -P
```

Dies listet die Details der CPU-Nutzung auf.

Um eine Ansicht eines anderen Tages zu sehen, können Sie nach `/var/log/sysstat/saXX` gehen, wobei `XX` der Tag ist, den Sie anzeigen möchten.

```bash
sar -q /var/log/sysstat/sa02
```

## Exercise

Übung macht den Meister! Hier sind einige praktische Übungen, um Ihr Verständnis der Systemüberwachung und Ressourcenanalyse zu vertiefen:

1. **[Linux-Prozesse verwalten und überwachen](https://labex.io/de/labs/comptia-manage-and-monitor-linux-processes-590864)** – Üben Sie die Interaktion mit Vordergrund- und Hintergrundprozessen, deren Überprüfung mit `ps`, die Überwachung von Ressourcen mit `top` und deren Beendigung mit `kill`.
2. **[Linux top Befehl: Echtzeit-Systemüberwachung](https://labex.io/de/labs/linux-linux-top-command-real-time-system-monitoring-388500)** – Lernen Sie, verschiedene Optionen mit dem Befehl `top` zu verwenden, um Prozesse zu sortieren, Aktualisierungsintervalle anzupassen, nach Benutzern zu filtern und sich auf aktive Prozesse zu konzentrieren, um die Systemleistung effektiv zu überwachen.
3. **[Linux df Befehl: Festplattenspeicher-Berichterstattung](https://labex.io/de/labs/linux-linux-df-command-disk-space-reporting-219188)** – Dieses Lab führt den Befehl `df` in Linux ein, ein Dienstprogramm, das Informationen über die Festplattenspeichernutzung auf gemounteten Dateisystemen anzeigt, was ein wichtiger Aspekt der Systemüberwachung ist.

Diese Labs helfen Ihnen, die Konzepte der Systemressourcenüberwachung in realen Szenarien anzuwenden und Vertrauen in die Analyse der Systemaktivität aufzubauen.

## Quiz Question

Welches Tool eignet sich gut zur Überwachung von Systemressourcen?

## Quiz Answer

sar
