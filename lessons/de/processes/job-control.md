---
title: "Job-Steuerung"
description: "Lernen Sie die Linux-Jobsteuerung, um Hintergrundprozesse zu verwalten. Verstehen Sie die Befehle 'jobs', 'bg', 'fg' und 'kill' für eine effiziente Shell-Nutzung. Beginnen Sie Ihre Linux-Reise!"
keywords: "Linux Job-Steuerung, Hintergrundprozesse, jobs Befehl, bg Befehl, fg Befehl, kill Befehl, Linux Tutorial, Linux für Anfänger"
---

## Lesson Content

Nehmen wir an, Sie arbeiten in einem einzigen Terminalfenster und führen einen Befehl aus, der ewig dauert. Sie können nicht mit der Shell interagieren, bis er abgeschlossen ist. Wir möchten jedoch weiterhin an unseren Maschinen arbeiten, daher benötigen wir diese Shell geöffnet. Glücklicherweise können wir steuern, wie unsere Prozesse mit Jobs ausgeführt werden:

### Einen Job in den Hintergrund senden

Das Anhängen eines kaufmännischen Und-Zeichens (`&`) an den Befehl führt ihn im Hintergrund aus, sodass Sie Ihre Shell weiterhin verwenden können. Sehen wir uns ein Beispiel an:

```bash
sleep 1000 &
sleep 1001 &
sleep 1002 &
```

### Alle Hintergrundjobs anzeigen

Jetzt können Sie die Jobs anzeigen, die Sie gerade in den Hintergrund geschickt haben.

```bash
$ jobs

[1]    Running     sleep 1000 &
[2]-   Running     sleep 1001 &
[3]+   Running     sleep 1002 &
```

Dies zeigt Ihnen die Job-ID in der ersten Spalte, dann den Status und den ausgeführten Befehl. Das **+** neben der Job-ID bedeutet, dass es der zuletzt gestartete Hintergrundjob ist. Der Job mit dem **-** ist der zweitletzte Befehl.

### Einen Job im Hintergrund auf einem bestehenden Job senden

Wenn Sie bereits einen Job ausgeführt haben und ihn in den Hintergrund senden möchten, müssen Sie ihn nicht beenden und von vorne beginnen. Halten Sie den Job zuerst mit Ctrl-Z an und führen Sie dann den Befehl **bg** aus, um ihn in den Hintergrund zu senden.

```bash
pete@icebox ~ $ sleep 1003
^Z
[4]+    Stopped     sleep 1003

pete@icebox ~ $ bg
[4]+    sleep 1003 &

pete@icebox ~ $ jobs

[1]    Running     sleep 1000 &
[2]    Running     sleep 1001 &
[3]-   Running     sleep 1002 &
[4]+   Running     sleep 1003 &
```

### Einen Job vom Hintergrund in den Vordergrund verschieben

Um einen Job aus dem Hintergrund zu holen, geben Sie einfach die gewünschte Job-ID an. Wenn Sie `fg` ohne Optionen ausführen, wird der zuletzt im Hintergrund ausgeführte Job (der Job mit dem +-Zeichen daneben) wieder in den Vordergrund geholt.

```bash
fg %1
```

### Hintergrundjobs beenden

Ähnlich wie beim Verschieben von Jobs aus dem Hintergrund können Sie dieselbe Form verwenden, um die Prozesse mithilfe ihrer Job-ID zu beenden.

```bash
kill %1
```

## Exercise

Move some jobs between the background and the foreground.

## Quiz Question

Welcher Befehl wird verwendet, um Hintergrundjobs aufzulisten?

## Quiz Answer

jobs
