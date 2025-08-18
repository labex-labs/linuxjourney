---
lang: "de"
title: "Energiezustände"
meta_description: "Lernen Sie die Energiezustände von Linux-Systemen kennen: shutdown-, reboot- und halt-Befehle. Verstehen Sie, wie Sie Ihr Linux-System sicher ausschalten oder neu starten. Beginnen Sie mit den wichtigsten Befehlen!"
meta_keywords: "Linux herunterfahren, reboot Befehl, System anhalten, Linux ausschalten, Linux Befehle, Linux für Anfänger, Linux Tutorial, Systemzustände"
---

## Lesson Content

Es ist kaum zu glauben, dass wir noch nicht über Möglichkeiten gesprochen haben, den Systemzustand über die Befehlszeile zu steuern. Wenn wir über `init` sprechen, diskutieren wir nicht nur die Modi, die unser System starten, sondern auch die, die es stoppen.

Um Ihr System herunterzufahren:

```bash
sudo shutdown -h now
```

Dieser Befehl wird das System anhalten (ausschalten). Sie müssen auch eine Zeit angeben, wann dies geschehen soll. Sie können eine Zeit in Minuten hinzufügen, die das System in dieser Zeit herunterfährt.

```bash
sudo shutdown -h +2
```

Dies wird Ihr System in zwei Minuten herunterfahren. Sie können auch mit dem Befehl `shutdown` neu starten:

```bash
sudo shutdown -r now
```

Oder verwenden Sie einfach den Befehl `reboot`:

```bash
sudo reboot
```

## Exercise

Was glauben Sie, geschieht mit `init`, wenn Sie Ihren Computer herunterfahren?

## Quiz Question

Wie lautet der Befehl, um Ihr System in 4 Minuten auszuschalten?

## Quiz Answer

sudo shutdown -h +4
