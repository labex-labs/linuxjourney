---
lang: "de"
title: "tail"
meta_description: "Erfahren Sie, wie Sie den Befehl `tail` in Linux verwenden, um Dateiendungen anzuzeigen und Protokolle zu überwachen. Entdecken Sie `tail -f` für Echtzeit-Updates. Beginnen Sie Ihre Linux-Reise!"
meta_keywords: "tail Befehl, Linux tail, tail -f, Protokolle anzeigen, Linux Tutorial, Linux für Anfänger, Linux Anleitung"
---

## Lesson Content

Ähnlich wie der `head`-Befehl zeigt Ihnen der `tail`-Befehl standardmäßig die letzten 10 Zeilen einer Datei an.

```bash
tail /var/log/syslog
```

Wie bei `head` können Sie die Anzahl der Zeilen ändern, die Sie sehen möchten.

```bash
tail -n 10 /var/log/syslog
```

Eine weitere großartige Option, die Sie verwenden können, ist das `-f` (follow)-Flag; dies verfolgt die Datei, während sie wächst. Probieren Sie es aus und sehen Sie, was passiert.

```bash
tail -f /var/log/syslog
```

Ihre `syslog`-Datei wird sich ständig ändern, während Sie mit Ihrem System interagieren, und mit `tail -f` können Sie alles sehen, was dieser Datei hinzugefügt wird.

## Exercise

Schauen Sie sich die Manpage von `tail` an und lesen Sie einige der anderen Befehle, die wir nicht besprochen haben.

```bash
man tail
```

## Quiz Question

Welches Flag wird verwendet, um eine Datei in `tail` zu verfolgen?

## Quiz Answer

-f
