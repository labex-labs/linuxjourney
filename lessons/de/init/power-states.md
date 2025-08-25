---
index: 7
lang: "de"
title: "Energiezustände"
meta_title: "Energiezustände - Init"
meta_description: "Lernen Sie die Linux-Systemzustände kennen: Befehle zum Herunterfahren, Neustarten und Anhalten. Verstehen Sie, wie Sie Ihr Linux-System sicher ausschalten oder neu starten können. Beginnen Sie mit den wichtigsten Befehlen!"
meta_keywords: "Linux herunterfahren, Neustart-Befehl, System anhalten, Linux ausschalten, Linux-Befehle, Linux für Anfänger, Linux-Tutorial, Systemzustände"
---

## Lesson Content

Es ist kaum zu glauben, dass wir noch keine Möglichkeiten besprochen haben, den Systemzustand über die Befehlszeile zu steuern. Wenn wir über `init` sprechen, diskutieren wir nicht nur die Modi, die unser System starten, sondern auch die, die es stoppen.

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

Obwohl es keine spezifischen Labs zu diesem Thema gibt, empfehlen wir Ihnen, den umfassenden [Linux-Lernpfad](https://labex.io/de/learn/linux) zu erkunden, um verwandte Linux-Fähigkeiten und -Konzepte zu üben.

## Quiz Question

Wie lautet der Befehl, um Ihr System in 4 Minuten auszuschalten?

## Quiz Answer

sudo shutdown -h +4
