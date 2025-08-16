---
lang: "de"
title: "cd (Verzeichnis wechseln)"
description: "Lernen Sie, wie Sie den Befehl 'cd' in Linux verwenden, um Verzeichnisse zu navigieren. Verstehen Sie absolute, relative Pfade und nützliche Abkürzungen. Beginnen Sie Ihre Linux-Reise!"
keywords: "cd Befehl, Verzeichnis wechseln, Linux Pfade, absoluter Pfad, relativer Pfad, Linux Tutorial, Linux für Anfänger, Linux Navigation"
---

## Lesson Content

Nachdem Sie nun wissen, wo Sie sich befinden, wollen wir uns ein wenig im Dateisystem bewegen. Denken Sie daran, dass wir uns mithilfe von Pfaden zurechtfinden müssen. Es gibt zwei verschiedene Möglichkeiten, einen Pfad anzugeben: mit absoluten und relativen Pfaden.

- Absoluter Pfad: Dies ist der Pfad vom Stammverzeichnis. Das Stammverzeichnis ist der Chef. Das Stammverzeichnis wird üblicherweise als Schrägstrich (`/`) dargestellt. Jedes Mal, wenn Ihr Pfad mit `/` beginnt, bedeutet dies, dass Sie vom Stammverzeichnis aus starten. Zum Beispiel, `/home/pete/Desktop`.

- Relativer Pfad: Dies ist der Pfad von Ihrem aktuellen Standort im Dateisystem aus. Wenn ich mich im Verzeichnis `/home/pete/Documents` befände und zu einem Unterverzeichnis namens `taxes` innerhalb von `Documents` wechseln wollte, muss ich nicht den gesamten Pfad vom Stammverzeichnis aus angeben, wie `/home/pete/Documents/taxes`; ich kann stattdessen einfach zu `taxes/` wechseln.

Nachdem Sie nun wissen, wie Pfade funktionieren, brauchen wir nur noch etwas, das uns hilft, in das gewünschte Verzeichnis zu wechseln. Glücklicherweise haben wir dafür `cd` oder „change directory“.

```bash
cd /home/pete/Pictures
```

Ich habe also meinen Verzeichnisstandort auf `/home/pete/Pictures` geändert.

Nun habe ich von diesem Verzeichnis aus einen Ordner namens `Hawaii` darin. Ich kann zu diesem Ordner navigieren mit:

```bash
cd Hawaii
```

Beachten Sie, dass ich nur den Namen des Ordners verwendet habe? Das liegt daran, dass ich bereits in `/home/pete/Pictures` war.

Es kann ziemlich ermüdend werden, ständig mit absoluten und relativen Pfaden zu navigieren. Glücklicherweise gibt es einige Abkürzungen, die Ihnen helfen.

- `.` (aktuelles Verzeichnis): Dies ist das Verzeichnis, in dem Sie sich gerade befinden.
- `..` (vorheriges Verzeichnis): Bringt Sie in das Verzeichnis oberhalb Ihres aktuellen Verzeichnisses.
- `~` (Home-Verzeichnis): Dieses Verzeichnis ist standardmäßig Ihr „Home-Verzeichnis“, wie z.B. `/home/pete`.
- `-` (vorheriges Verzeichnis): Dies bringt Sie in das vorherige Verzeichnis, in dem Sie sich gerade befanden.

```bash
cd .
cd ..
cd ~
cd -
```

Probieren Sie sie aus!

## Exercise

1. Führen Sie den Befehl `cd` ohne Optionen aus. Wohin bringt er Sie?

## Quiz Question

Wenn Sie sich in `/home/pete/Pictures` befinden und zu `/home/pete` wechseln möchten, welche gute Abkürzung können Sie verwenden?

## Quiz Answer

cd ..
