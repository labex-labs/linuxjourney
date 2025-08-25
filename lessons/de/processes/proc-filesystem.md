---
index: 10
lang: "de"
title: "/proc-Dateisystem"
meta_title: "/proc-Dateisystem - Prozesse"
meta_description: "Erfahren Sie mehr über das /proc-Dateisystem in Linux, wie es Prozessinformationen speichert und wie es strukturiert ist. Entdecken Sie Prozessdetails mit diesem grundlegenden Linux-Leitfaden."
meta_keywords: "/proc-Dateisystem, Linux-Prozesse, Prozessinformationen, Linux-Tutorial, Linux für Anfänger, Linux-Leitfaden"
---

## Lesson Content

Denken Sie daran, in Linux ist alles eine Datei, sogar Prozesse. Prozessinformationen werden in einem speziellen Dateisystem gespeichert, das als `/proc`-Dateisystem bekannt ist.

```bash
ls /proc
```

Sie sollten hier mehrere Werte sehen; es gibt Unterverzeichnisse für jede PID. Wenn Sie eine PID in der `ps`-Ausgabe betrachtet haben, könnten Sie diese im `/proc`-Verzeichnis finden.

Gehen Sie voran und geben Sie einen der Prozesse ein und sehen Sie sich diese Datei an:

```bash
cat /proc/12345/status
```

Sie sollten Prozessstatusinformationen sowie detailliertere Informationen sehen. Das `/proc`-Verzeichnis ist die Art und Weise, wie der Kernel das System sieht, daher gibt es hier viel mehr Informationen, als Sie in `ps` sehen würden.

## Exercise

Übung macht den Meister! Hier sind einige praktische Übungen, um Ihr Verständnis von Linux-Prozessen und der Systemüberwachung zu vertiefen:

1. **[Linux-Prozesse verwalten und überwachen](https://labex.io/de/labs/comptia-manage-and-monitor-linux-processes-590864)** – In diesem Lab lernen Sie grundlegende Fähigkeiten zur Verwaltung und Überwachung von Prozessen auf einem Linux-System. Sie werden erfahren, wie Sie mit Vordergrund- und Hintergrundprozessen interagieren, diese mit `ps` inspizieren, Ressourcen mit `top` überwachen, die Priorität mit `renice` anpassen und sie mit `kill` beenden.

Diese Labs helfen Ihnen, die Konzepte in realen Szenarien anzuwenden und Vertrauen in die Prozessverwaltung und Systembeobachtung aufzubauen.

## Quiz Question

Welches Dateisystem speichert Prozessinformationen?

## Quiz Answer

/proc
