---
index: 8
lang: "de"
title: "Cron Jobs"
meta_title: "Cron Jobs - Prozessauslastung"
meta_description: "Erfahren Sie, wie Sie Aufgaben planen und Skripte in Linux mit Cron Jobs automatisieren. Diese Anleitung behandelt die Crontab-Syntax, wichtige Befehle wie crontab -e und praktische Beispiele für Anfänger."
meta_keywords: "cron jobs, crontab, Aufgaben planen, Linux Automatisierung, Linux Befehle, Linux für Anfänger, Linux Tutorial, crontab -e, cron"
---

## Lesson Content

Während die Prozessauslastung wichtig ist, ist dies auch ein guter Zeitpunkt, um ein leistungsstarkes Werkzeug für die `Linux-Automatisierung` einzuführen: den `cron`-Daemon. Dieser Hintergrunddienst ermöglicht es Ihnen, `Aufgaben zu planen`, die automatisch zu bestimmten Zeiten oder Intervallen ausgeführt werden. Diese geplanten Aufgaben sind allgemein als `Cron-Jobs` bekannt. Dies ist unglaublich nützlich für die Automatisierung routinemäßiger Aktionen, wie z. B. das nächtliche Ausführen eines Backup-Skripts oder das wöchentliche Bereinigen temporärer Dateien.

### Was sind Cron-Jobs

Stellen Sie sich vor, Sie haben ein Skript unter `/home/pete/scripts/change_wallpaper`, das Sie jeden Morgen ausführen, um einen neuen Desktop-Hintergrund festzulegen. Anstatt es täglich manuell auszuführen, können Sie einen `Cron-Job` erstellen, um es für Sie auszuführen. Durch die Definition eines Zeitplans können Sie dem `cron`-Dienst genau mitteilen, wann er Ihr Skript ausführen soll, was es zu einer echten „einstellen und vergessen“-Lösung macht.

### Verständnis der Crontab-Syntax

Um einen `Cron-Job` zu erstellen, müssen Sie den Zeitplan und den auszuführenden Befehl angeben. Der Zeitplan wird durch fünf Felder definiert, gefolgt von dem Befehl.

```plaintext
30 08 * * * /home/pete/scripts/change_wallpaper
```

Die fünf Zeit- und Datumsfelder sind von links nach rechts:

- **Minute:** 0-59
- **Stunde:** 0-23 (im 24-Stunden-Format)
- **Tag des Monats:** 1-31
- **Monat:** 1-12
- **Wochentag:** 0-7 (wobei sowohl 0 als auch 7 Sonntag darstellen)

Ein Sternchen (`*`) in einem Feld fungiert als Platzhalter und bedeutet „jeder“. Im obigen Beispiel weist der Zeitplan `30 08 * * *` `cron` an, den Befehl um 8:30 Uhr, jeden Tag des Monats, jeden Monat und jeden Wochentag auszuführen.

### Verwaltung von Cron-Jobs mit Crontab

Sie verwalten Ihre persönlichen `Cron-Jobs` mit dem Befehl `crontab`, mit dem Sie Ihre benutzerspezifische Crontab-Datei bearbeiten können. Diese Datei enthält alle von Ihnen geplanten `Cron-Jobs`.

Um Ihre `Cron-Jobs` hinzuzufügen oder zu bearbeiten, verwenden Sie das Flag `-e` (editieren). Dadurch wird Ihre Crontab-Datei in Ihrem Standard-Texteditor geöffnet.

```bash
crontab -e
```

Sobald Sie Ihre Job-Definition hinzugefügt und die Datei gespeichert haben, liest `cron` den neuen Zeitplan automatisch ein. Sie können Ihre aktiven `Cron-Jobs` auch mit `crontab -l` auflisten oder alle mit `crontab -r` entfernen. Die Verwendung von `Cron-Jobs` ist eine grundlegende Fähigkeit für jeden, der sich für `Linux-Automatisierung` interessiert.

## Exercise

Übung macht den Meister! Dieses praktische Labor hilft Ihnen, Ihr Verständnis dafür zu festigen, wie man `Aufgaben in Linux plant`.

1. **[Aufgaben mit at und cron in Linux planen](https://labex.io/de/labs/comptia-schedule-tasks-with-at-and-cron-in-linux-590870)** - Üben Sie das Erstellen, Verwalten und Entfernen von Jobs mit `at`, `atq`, `atrm` und `crontab` und sammeln Sie praktische Erfahrungen bei der Automatisierung von Systemadministrationsaufgaben.

Dieses Labor hilft Ihnen, die Konzepte aus dieser Lektion in einem realen Szenario anzuwenden und Ihr Selbstvertrauen in die `Linux-Automatisierung` zu stärken.

## Quiz Question

Was ist der Befehl, um Ihre persönlichen Cron-Jobs zu bearbeiten? (Bitte antworten Sie mit dem exakten Kleinbuchstabenbefehl und seiner Option.)

## Quiz Answer

crontab -e
