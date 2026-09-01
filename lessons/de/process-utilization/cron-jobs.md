---
lesson_id: "cron-jobs"
course_id: "process-utilization"
lang: "de"
order_index: 8
title: "Cron-Jobs"
description: "Lerne, wiederkehrende Aufgaben mit cron zu erstellen, zu untersuchen, zu testen und sicher zu betreiben."
meta_title: "Cron-Jobs – Prozessauslastung"
meta_description: "Lerne, mit Cron-Jobs Aufgaben unter Linux zu planen und Skripte zu automatisieren. Diese Anleitung behandelt die Crontab-Syntax, wichtige Befehle wie crontab -e und praktische Beispiele."
meta_keywords: "Cron-Jobs, crontab, Aufgaben planen, Linux-Automatisierung, Linux-Befehle, Linux für Einsteiger, Linux-Tutorial, crontab -e, cron"
---

Cron führt Befehle nach wiederkehrenden Zeitplänen ohne interaktive Shell aus. Automatisierung wiederholt sowohl korrektes Verhalten als auch Fehler. Teste deshalb den Befehl, verwende ausdrückliche Pfade, begrenze Berechtigungen und plane Protokollierung sowie Fehlerbenachrichtigung, bevor du ihn einplanst.

## Einen Crontab-Eintrag lesen

Ein Eintrag in einer Benutzer-Crontab enthält fünf Zeitfelder, gefolgt von einem Befehl:

```cron
30 8 * * * /home/pete/scripts/change_wallpaper
```

Von links nach rechts sind die Felder Minute, Stunde, Tag des Monats, Monat und Wochentag. Dieses Beispiel wird entsprechend der für den Cron-Daemon geltenden Zeitzone um 08:30 Uhr ausgeführt. Ein Sternchen bezeichnet jeden erlaubten Wert in diesem Feld.

Wenn sowohl der Tag des Monats als auch der Wochentag eingeschränkt sind, führen viele Cron-Implementierungen den Befehl aus, sobald eines der beiden Felder übereinstimmt. Bestätige die lokale Semantik, bevor du einen Zeitplan erstellst, der beide verwendet.

:::single-choice{#cron-daily-eight-thirty} Wann wird `30 8 * * * command` ausgeführt?

::option[Acht Stunden lang alle 30 Minuten.]{#cron-every-thirty explanation="Die Felder sind Positionen in einem Zeitplan und kein Dauerausdruck."}
::option[Jeden Tag um 08:30 Uhr.]{#cron-eight-thirty .correct explanation="Minute 30 und Stunde 8 sind festgelegt, während die drei Datumsfelder jeden Wert erlauben."}
::option[Um 30:08 Uhr am achten Tag jedes Monats.]{#cron-invalid-time explanation="Stunden reichen von 0 bis 23, und das Beispiel schränkt den Tag des Monats nicht ein."}
:::

## Eine Benutzer-Crontab verwalten

Bearbeite die Crontab des aktuellen Benutzers mit:

```bash
$ crontab -e
```

Liste die installierten Einträge vor und nach einer Änderung auf:

```bash
$ crontab -l
```

`crontab -r` entfernt die gesamte Crontab des Benutzers, möglicherweise ohne einen Editor zu öffnen. Verwende den Befehl nicht, um eine einzelne Zeile zu entfernen; bearbeite die Crontab und überprüfe die verbleibenden Einträge.

:::single-choice{#cron-list-current-user} Welcher Befehl listet die installierten Cron-Einträge des aktuellen Benutzers auf?

::option[`crontab -l`]{#cron-list .correct explanation="Die Auflistungsoption gibt die installierten Einträge zur Prüfung aus."}
::option[`crontab -r`]{#cron-remove-all explanation="Diese Option entfernt die Crontab, statt sie anzuzeigen."}
::option[`crontab -e`]{#cron-edit explanation="Dies öffnet die Crontab zur Bearbeitung, statt sie lediglich aufzulisten."}
:::

## Die Cron-Umgebung berücksichtigen

Cron stellt gewöhnlich eine eingeschränkte Umgebung und eine nicht interaktive Shell bereit. Verwende absolute Befehls- und Dateipfade, lege erforderliche Variablen ausdrücklich fest und verlasse dich weder auf Aliase noch auf ein aktuelles Terminalverzeichnis oder Shell-Startdateien.

Leite Standardausgabe und Standardfehler in ein kontrolliertes Protokoll um oder verwende einen für das System geeigneten Benachrichtigungsmechanismus. Schütze Anmeldedaten mit restriktiven Berechtigungen und bette Geheimnisse nicht direkt in einen Crontab-Befehl ein.

:::single-choice{#cron-absolute-paths} Warum sollte ein Cron-Befehl ausdrückliche Pfade und Umgebungseinstellungen verwenden?

::option[Cron läuft immer im aktuellen Terminal des Benutzers.]{#cron-current-terminal explanation="Geplante Jobs laufen unabhängig von einer interaktiven Sitzung."}
::option[Absolute Pfade führen jeden Befehl als root aus.]{#cron-path-root explanation="Pfade wählen Dateien aus, gewähren aber keine Berechtigungen."}
::option[Die Umgebung von Cron kann sich von der interaktiven Shell unterscheiden.]{#cron-limited-environment .correct explanation="Ausdrückliche Abhängigkeiten verhindern Fehler durch Annahmen zu PATH, Verzeichnis oder Startdateien."}
:::

## Testen und Überschneidungen verhindern

Führe das Skript als derselbe Benutzer mit einer ähnlich minimalen Umgebung manuell aus. Sorge dafür, dass es aussagekräftige Exit-Statuswerte zurückgibt und Ergebnisse mit Zeitstempeln schreibt. Warte nach der Installation auf einen harmlosen Testzeitplan oder einen kontrollierten Lauf und überprüfe die tatsächliche Wirkung sowie die Protokolle.

Falls ein Lauf länger als sein Intervall dauern kann, entwirf ihn für Nebenläufigkeit oder verwende, sofern verfügbar, einen Sperrmechanismus wie `flock`:

```cron
*/5 * * * * /usr/bin/flock -n /run/user/1000/report.lock /home/pete/bin/report
```

Wähle einen Sperrpfad, den der Jobbenutzer sicher erstellen darf, und entscheide, ob ausgelassene Läufe akzeptabel sind. Cron garantiert nicht automatisch, dass nur eine Instanz läuft.

:::single-choice{#cron-overlapping-runs} Welches Risiko besteht, wenn ein Job länger als sein Zeitplanintervall dauert?

::option[Mehrere Instanzen können sich überschneiden und um Ressourcen konkurrieren.]{#cron-overlap .correct explanation="Cron kann einen neuen Lauf starten, während der vorige Prozess noch läuft."}
::option[Die fünf Zeitplanfelder erhalten automatisch ein sechstes Sperrfeld.]{#cron-auto-lock explanation="Die Crontab-Syntax fügt keinen automatischen gegenseitigen Ausschluss hinzu."}
::option[Das Skript wird dauerhaft in einen Kernel-Thread umgewandelt.]{#cron-kernel-thread explanation="Das Einplanen eines Befehls ändert sein Prozessmodell nicht auf diese Weise."}
:::

## Den passenden Scheduler auswählen

Cron eignet sich für einfache wiederkehrende Befehle. Systemd-Timer können auf systemd-Hosts Abhängigkeitsintegration, dauerhaftes Nachholen verpasster Läufe, zufällige Verzögerungen und Journalprotokollierung bieten. Anwendungs- oder Cluster-Scheduler können sicherer sein, wenn ein Job über mehrere Rechner hinweg genau einmal laufen muss.

:::single-choice{#cron-cluster-exactly-once} Warum kann gewöhnliches hostbezogenes Cron für einen Cluster-Job, der genau einmal laufen soll, ungeeignet sein?

::option[Jeder Cron-Eintrag ist auf ein Zeichen beschränkt.]{#cron-one-character explanation="Crontab-Befehle können gewöhnliche Befehlszeilen enthalten."}
::option[Jeder Host kann unabhängig seine eigene Instanz starten.]{#cron-each-host .correct explanation="Ein verteilter Koordinierungsmechanismus ist nötig, um eine einzige Ausführung über alle Hosts hinweg durchzusetzen."}
::option[Cron kann keine auf dem Datenträger gespeicherten Skripte ausführen.]{#cron-no-scripts explanation="Das Ausführen von Skripten ist ein häufiger Anwendungsfall für Cron."}
:::

## Zusammenfassung

Du kannst einen wiederkehrenden Cron-Job nun mit ausdrücklichen Annahmen zu Zeitplan und Ausführung betreiben.

1. Lies die fünf Zeitfelder in ihrer festgelegten Reihenfolge.
2. Untersuche und bearbeite Benutzer-Crontabs, ohne unabhängige Jobs zu löschen.
3. Definiere Pfade, Umgebung, Protokollierung und Umgang mit Anmeldedaten.
4. Teste als Jobbenutzer und schütze vor unerwünschten Überschneidungen.
5. Wähle einen Scheduler, der zu Host- und Koordinierungsanforderungen passt.
