---
index: 11
lang: "de"
title: "Jobsteuerung"
meta_title: "Jobsteuerung - Prozesse"
meta_description: "Entdecken Sie unser Linux-Tutorial zur Jobsteuerung, um Hintergrundprozesse effektiv zu verwalten. Lernen Sie die Befehle jobs, bg, fg und kill für leistungsstarkes Shell-Multitasking."
meta_keywords: "Linux Jobsteuerung, Hintergrundprozesse, jobs Befehl, bg Befehl, fg Befehl, kill Befehl, Linux Tutorial, Anfänger Linux"
---

## Lesson Content

Unter Linux stoßen Sie oft auf Befehle, deren Abschluss lange dauert. Anstatt zu warten und Ihr Terminal unbenutzbar zu machen, können Sie **Linux Job Control** verwenden, um diese Aufgaben zu verwalten. Diese leistungsstarke Funktion ermöglicht es Ihnen, mehrere **Hintergrundprozesse** innerhalb einer einzigen Shell-Sitzung auszuführen und zu verwalten, was Ihren Arbeitsablauf erheblich verbessert.

### Einen Befehl im Hintergrund ausführen

Um einen Prozess direkt im Hintergrund zu starten, hängen Sie einfach ein Ampersand (`&`) an Ihren Befehl an. Dadurch wird sofort Ihre Shell-Eingabeaufforderung zurückgegeben, sodass Sie weiterarbeiten können, während der Befehl ausgeführt wird.

```bash
sleep 1000 &
sleep 1001 &
sleep 1002 &
```

### Hintergrundjobs auflisten

Sie können alle im Hintergrund laufenden Jobs mit dem Befehl `jobs` anzeigen.

```bash
$ jobs

[1]    Running     sleep 1000 &
[2]-   Running     sleep 1001 &
[3]+   Running     sleep 1002 &
```

Die Ausgabe zeigt die Job-ID in der ersten Spalte, deren Status und den ursprünglichen Befehl. Das `+`-Symbol kennzeichnet den zuletzt gestarteten Hintergrundjob, während das `-`-Symbol den zweitneuesten kennzeichnet.

### Aktive Prozesse verwalten

Was ist, wenn ein Befehl bereits im Vordergrund läuft und Sie entscheiden, dass Sie Ihr Terminal zurückbenötigen? Sie müssen ihn nicht stoppen. Unterbrechen Sie zuerst den laufenden Prozess, indem Sie `Strg-Z` drücken. Verwenden Sie dann den Befehl `bg`, um diesen angehaltenen Job in den Hintergrund zu senden.

```bash
pete@icebox ~ $ sleep 1003
^Z
[4]+    Stopped     sleep 1003

pete@icebox ~ $ bg
[4]+    sleep 1003 &
```

Jetzt läuft der Prozess `sleep 1003` als Hintergrundjob, was Sie mit dem Befehl `jobs` überprüfen können.

### Einen Job in den Vordergrund holen

Um einen Hintergrundprozess wieder in den Vordergrund zu holen, verwenden Sie den Befehl `fg`. Sie können einen bestimmten Job anhand seiner ID angeben (z. B. `fg %1`). Wenn Sie den Befehl `fg` ohne Argumente ausführen, wird der zuletzt ausgeführte Hintergrundjob (der mit `+` markierte) in den Vordergrund geholt.

```bash
fg %1
```

### Hintergrundjobs beenden

Wenn Sie einen Hintergrundprozess stoppen müssen, können Sie den Befehl `kill` verwenden. Ähnlich wie beim `fg`-Befehl referenzieren Sie den Job mithilfe seiner ID, der ein Prozentzeichen (`%`) vorangestellt ist. Dies ist eine Schlüsselfunktion der Linux Job Control.

```bash
kill %1
```

Die Beherrschung dieser Befehle ist für jeden Linux-Anfänger, der effizient in der Shell multitasken möchte, unerlässlich.

## Exercise

Um Ihr Wissen über die Linux Job Control in die Praxis umzusetzen, versuchen Sie dieses praktische Labor. Es wird Ihnen helfen, Ihr Verständnis für die Verwaltung von Vordergrund- und Hintergrundprozessen zu festigen.

1. **[Linux-Prozesse verwalten und überwachen](https://labex.io/de/labs/comptia-manage-and-monitor-linux-processes-590864)** - Üben Sie die Interaktion mit Vordergrund- und Hintergrundprozessen, die Überwachung von Ressourcen und das Beenden von Prozessen, was direkt das Szenario lang laufender Befehle anspricht.

## Quiz Question

What command is used to list background jobs? (Please answer in English, using only lowercase letters.)

## Quiz Answer

jobs
