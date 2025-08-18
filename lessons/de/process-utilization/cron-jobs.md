---
lang: "de"
title: "Cron-Jobs"
meta_description: "Lernen Sie, Linux-Aufgaben mit Cron-Jobs zu planen. Verstehen Sie die Crontab-Syntax und automatisieren Sie Skripte für den täglichen Betrieb. Starten Sie mit dieser anfängerfreundlichen Anleitung!"
meta_keywords: "Cron-Jobs, Crontab, Aufgaben planen, Linux-Automatisierung, Linux-Befehle, Linux für Anfänger, Linux-Tutorial, crontab -e"
---

## Lesson Content

Obwohl wir über die Ressourcennutzung gesprochen haben, halte ich dies für einen guten Zeitpunkt, um ein nützliches Tool in Linux zu erwähnen, das zur Aufgabenplanung mittels cron verwendet wird. Es gibt einen Dienst, der Programme zu jeder von Ihnen geplanten Zeit für Sie ausführt. Dies ist wirklich nützlich, wenn Sie ein Skript haben, das Sie einmal täglich ausführen möchten und das etwas für Sie erledigen muss.

Nehmen wir zum Beispiel an, ich habe ein Skript unter `/home/pete/scripts/change_wallpaper`. Ich verwende dieses Skript jeden Morgen, um das Bild für meinen Hintergrund zu ändern, aber jeden Morgen muss ich dieses Skript manuell ausführen. Stattdessen kann ich einen Cron-Job erstellen, der mein Skript über cron ausführt. Ich kann die Zeit angeben, zu der dieser Cron-Job ausgeführt und mein Skript gestartet werden soll.

```plaintext
30 08 * * * /home/pete/scripts/change_wallpaper
```

Die Felder sind von links nach rechts wie folgt:

- Minute - (0-59)
- Hour - (0-23)
- Day of the month - (1-31)
- Month - (1-12)
- Day of the week - (0-7). 0 und 7 stehen für Sonntag

Der Stern in einem Feld bedeutet, dass jeder Wert übereinstimmt. In meinem obigen Beispiel möchte ich also, dass dies jeden Tag in jedem Monat um 8:30 Uhr ausgeführt wird.

Um einen Cron-Job zu erstellen, bearbeiten Sie einfach die Datei crontab:

```bash
crontab -e
```

## Exercise

Erstellen Sie einen Cron-Job, den Sie zu einer geplanten Zeit ausführen möchten.

## Quiz Question

Wie lautet der Befehl zum Bearbeiten Ihrer Cron-Jobs?

## Quiz Answer

crontab -e
