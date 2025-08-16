---
lang: "de"
title: "Kontinuierliche Überwachung"
description: "Lernen Sie die kontinuierliche Linux-Systemüberwachung mit sar. Verstehen Sie die Installation, Datenerfassung und wie Sie historische Ressourcennutzung zur Leistungsanalyse nutzen können. Legen Sie los!"
keywords: "sar, sysstat, Linux-Überwachung, Systemleistung, kontinuierliche Überwachung, Anfänger, Tutorial, Anleitung"
---

## Lesson Content

Diese Überwachungstools sind gut, um sie zu betrachten, wenn Ihre Maschine Probleme hat, aber was ist mit Maschinen, die Probleme haben, wenn Sie nicht hinschauen? Dafür benötigen Sie ein kontinuierliches Überwachungstool, etwas, das Ihre Systemaktivitätsinformationen sammelt, meldet und speichert. In dieser Lektion werden wir ein großartiges Tool vorstellen: **sar**.

### Installing sar

Sar ist ein Tool, das zur historischen Analyse Ihres Systems verwendet wird. Stellen Sie zunächst sicher, dass es installiert ist, indem Sie das Paket `sysstat` installieren: `sudo apt install sysstat`.

### Setting up data collection

Normalerweise beginnt Ihr System nach der Installation von `sysstat` automatisch mit der Datenerfassung. Falls nicht, können Sie dies aktivieren, indem Sie das Feld `ENABLED` in `/etc/default/sysstat` ändern.

### Using sar

```bash
sudo sar -q
```

Dieser Befehl listet die Details vom Tagesanfang auf.

```bash
sudo sar -r
```

Dies listet die Details der Speichernutzung vom Tagesanfang auf.

```bash
sudo sar -P
```

Dies listet die Details der CPU-Nutzung auf.

Um eine Ansicht eines anderen Tages zu sehen, können Sie zu `/var/log/sysstat/saXX` gehen, wobei `XX` der Tag ist, den Sie anzeigen möchten.

```bash
sar -q /var/log/sysstat/sa02
```

## Exercise

Installieren Sie sar auf Ihrem System und beginnen Sie mit der Erfassung und Analyse Ihrer Systemressourcenauslastung.

## Quiz Question

Welches Tool eignet sich gut zur Überwachung von Systemressourcen?

## Quiz Answer

sar
