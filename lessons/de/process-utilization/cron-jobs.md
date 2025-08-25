---
index: 8
lang: "de"
title: "Cron-Jobs"
meta_title: "Cron-Jobs - Prozessauslastung"
meta_description: "Lernen Sie, Linux-Aufgaben mit Cron-Jobs zu planen. Verstehen Sie die Crontab-Syntax und automatisieren Sie Skripte für den täglichen Betrieb. Starten Sie mit diesem anfängerfreundlichen Leitfaden!"
meta_keywords: "Cron-Jobs, Crontab, Aufgaben planen, Linux-Automatisierung, Linux-Befehle, Linux für Anfänger, Linux-Tutorial, Crontab -e"
---

## Lesson Content

Obwohl wir über Ressourcennutzung gesprochen haben, denke ich, dass dies ein guter Zeitpunkt ist, um ein nützliches Tool in Linux zu erwähnen, das zur Planung von Aufgaben mithilfe von Cron verwendet wird. Es gibt einen Dienst, der Programme zu jeder von Ihnen festgelegten Zeit für Sie ausführt. Dies ist wirklich nützlich, wenn Sie ein Skript haben, das einmal täglich ausgeführt werden soll und etwas für Sie erledigen muss.

Nehmen wir zum Beispiel an, ich habe ein Skript unter `/home/pete/scripts/change_wallpaper`. Ich verwende dieses Skript jeden Morgen, um das Bild für meinen Hintergrund zu ändern, aber jeden Morgen muss ich dieses Skript manuell ausführen. Stattdessen kann ich einen Cron-Job erstellen, der mein Skript über Cron ausführt. Ich kann die Zeit angeben, zu der dieser Cron-Job ausgeführt und mein Skript ausgeführt werden soll.

```plaintext
30 08 * * * /home/pete/scripts/change_wallpaper
```

Die Felder sind von links nach rechts wie folgt:

- Minute - (0-59)
- Stunde - (0-23)
- Tag des Monats - (1-31)
- Monat - (1-12)
- Wochentag - (0-7). 0 und 7 stehen für Sonntag

Der Stern in dem Feld bedeutet, jeden Wert abzugleichen. In meinem obigen Beispiel möchte ich also, dass dies jeden Tag in jedem Monat um 8:30 Uhr ausgeführt wird.

Um einen Cron-Job zu erstellen, bearbeiten Sie einfach die crontab-Datei:

```bash
crontab -e
```

## Exercise

Übung macht den Meister! Hier sind einige praktische Übungen, um Ihr Verständnis der Aufgabenplanung in Linux zu vertiefen:

1. **[Aufgaben mit at und cron in Linux planen](https://labex.io/de/labs/comptia-schedule-tasks-with-at-and-cron-in-linux-590870)** - Üben Sie das Erstellen, Verwalten und Entfernen von Jobs mit `at`, `atq`, `atrm` und `crontab`, um praktische Erfahrungen bei der Automatisierung von Systemadministrationsaufgaben zu sammeln.

Dieses Labor wird Ihnen helfen, die Konzepte in realen Szenarien anzuwenden und Vertrauen in die Aufgabenplanung aufzubauen.

## Quiz Question

Wie lautet der Befehl zum Bearbeiten Ihrer Cron-Jobs?

## Quiz Answer

crontab -e
