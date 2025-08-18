---
index: 10
lang: "de"
title: "/proc-Dateisystem"
meta_title: "/proc-Dateisystem - Prozesse"
meta_description: "Erfahren Sie mehr über das /proc-Dateisystem in Linux, wie es Prozessinformationen speichert und wie es strukturiert ist. Entdecken Sie Prozessdetails mit diesem wichtigen Linux-Leitfaden."
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

No exercises for this lesson.

## Quiz Question

Welches Dateisystem speichert Prozessinformationen?

## Quiz Answer

/proc
