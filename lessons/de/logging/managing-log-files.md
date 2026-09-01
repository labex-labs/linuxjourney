---
lesson_id: "managing-log-files"
course_id: "logging"
lang: "de"
order_index: 6
title: "Protokolldateien verwalten"
description: "Lerne, eine sichere Rotation von Textprotokollen mit logrotate zu konfigurieren, zu testen und zu überprüfen."
meta_title: "Protokolldateien verwalten – Protokollierung"
meta_description: "Lerne die Linux-Protokollverwaltung mit logrotate. Diese Einführung erklärt, wie Protokollrotation Speicherplatz spart, konfiguriert wird und Systemprotokolle geordnet hält."
meta_keywords: "logrotate, Linux-Protokolle, Protokollverwaltung, Protokollrotation, Linux-Tutorial, Einsteiger, Anleitung, Speicherplatz"
---

Unbegrenzte Textprotokolle können ein Dateisystem füllen, während zu aggressives Löschen für Betrieb oder Compliance erforderliche Belege entfernen kann. `logrotate` wendet konfigurierte Richtlinien zu Größe, Zeit, Komprimierung, Eigentum und Aufbewahrung auf dateibasierte Protokolle an.

## Rotation verstehen

Bei einer typischen Rotation wird die aktive Datei umbenannt, ein Ersatz erstellt, die Anwendung optional zum erneuten Öffnen aufgefordert, ältere Generationen komprimiert und Dateien außerhalb der Aufbewahrung entfernt. Diese Schritte hängen von der Konfiguration ab. Rotation ist keine Sicherung, weil aufbewahrte Kopien weiterhin gelöscht oder beschädigt werden beziehungsweise mit demselben Host verloren gehen können.

:::single-choice{#logrotate-not-backup} Warum ersetzt Protokollrotation keine Sicherung oder Archivierung?

::option[Rotierte Dateien unterliegen weiterhin lokaler Aufbewahrung und Hostausfällen.]{#logrotate-local-retention .correct explanation="Rotation steuert Arbeitsgenerationen von Protokollen, erstellt aber keine unabhängige dauerhafte Kopie."}
::option[Rotation kann nur Bilddateien verarbeiten.]{#logrotate-images explanation="Das Werkzeug ist in erster Linie für Protokolldateien vorgesehen."}
::option[Jede Rotation bewahrt alle Generationen für immer auf.]{#logrotate-forever explanation="Aufbewahrungsregeln entfernen normalerweise ältere Generationen."}
:::

## Konfiguration auffinden

Die Hauptdatei ist gewöhnlich `/etc/logrotate.conf`; Ausschnitte von Paketen oder Anwendungen liegen unter `/etc/logrotate.d/`. Eine vereinfachte Richtlinie kann so aussehen:

```text
/var/log/example/app.log {
    daily
    rotate 7
    compress
    delaycompress
    missingok
    notifempty
    create 0640 example adm
}
```

Dies fordert tägliche Prüfung, sieben aufbewahrte Rotationen, um eine Generation verzögerte Komprimierung, Toleranz für ein fehlendes oder leeres Protokoll und eine neu erstellte Datei mit ausdrücklichem Modus und Eigentum an. Die tatsächliche Rotation hängt außerdem vom aufgezeichneten Zustand und davon ab, wie der Scheduler logrotate aufruft.

:::single-choice{#logrotate-rotate-seven} Was legt `rotate 7` fest?

::option[Bis zu sieben rotierte Generationen gemäß der Richtlinie aufbewahren.]{#logrotate-seven-generations .correct explanation="Ältere Generationen werden entfernt, wenn die konfigurierte Aufbewahrung überschritten wird."}
::option[Die Anwendung siebenmal pro Tag ausführen.]{#logrotate-run-seven explanation="Die Direktive steuert aufbewahrte Generationen und nicht die Anwendungsausführung."}
::option[Die Berechtigungen jeder rotierten Datei auf Modus 0007 setzen.]{#logrotate-mode-seven explanation="Der Dateimodus wird durch Direktiven wie `create` gesteuert."}
:::

## Mit dem schreibenden Prozess koordinieren

Nach dem Umbenennen eines Protokolls kann ein Daemon über seinen weiterhin geöffneten Dateideskriptor weiterschreiben. Ein `postrotate`-Skript sendet häufig ein dokumentiertes Signal zum Neuladen oder erneuten Öffnen. Validiere das genaue Anwendungsverhalten und halte das Skript eng begrenzt.

`copytruncate` kopiert eine Datei und kürzt das Original an Ort und Stelle, wenn eine Anwendung Protokolle nicht erneut öffnen kann. Während des Kopier- und Kürzungsfensters können Schreibvorgänge verloren gehen oder dupliziert werden. Es ist daher ein Kompromiss und kein allgemeingültig sicherer Standard.

:::single-choice{#logrotate-open-descriptor} Warum kann eine Anwendung nach der Rotation ein Signal zum erneuten Öffnen benötigen?

::option[Ihr offener Deskriptor kann weiterhin auf die umbenannte Datei verweisen.]{#logrotate-descriptor-renamed .correct explanation="Durch erneutes Öffnen verwenden künftige Schreibvorgänge den neu erstellten aktiven Pfad."}
::option[Komprimierung stoppt automatisch jeden Anwendungsprozess.]{#logrotate-compression-stops explanation="Komprimierung verwaltet nicht von sich aus den Lebenszyklus des schreibenden Prozesses."}
::option[Der Kernel verbietet das Erstellen einer zweiten Protokolldatei.]{#logrotate-kernel-forbids explanation="Mehrere Protokolldateien können bestehen; entscheidend ist, welchen Inode der schreibende Prozess geöffnet hat."}
:::

## Vor der Aktivierung testen

Untersuche Entscheidungen im Debugmodus, ohne Dateien zu rotieren:

```bash
$ sudo logrotate -d /etc/logrotate.conf
```

Die Debugausgabe beweist nicht, dass Berechtigungen, Skripte, freier Speicherplatz oder das erneute Öffnen der Anwendung bei einem tatsächlichen Lauf erfolgreich sind. Teste eine neue Regel in einer kontrollierten Umgebung und untersuche anschließend aktive Datei, rotierte Generation, Eigentum, Komprimierung, Anwendungsausgabe und logrotate-Zustand. `-f` erzwingt eine Rotation und verändert den Zustand; verwechsle es nicht mit einem Probelauf.

:::single-choice{#logrotate-debug-mode} Was bietet `logrotate -d`?

::option[Das dauerhafte Löschen aller abgelaufenen Protokolle.]{#logrotate-debug-delete explanation="Der Debugmodus meldet beabsichtigte Entscheidungen, ohne eine Rotation auszuführen."}
::option[Eine erzwungene Produktionsrotation unabhängig von der Richtlinie.]{#logrotate-debug-force explanation="Die Option zum Erzwingen ist `-f` und verändert den Zustand."}
::option[Eine diagnostische Auswertung, ohne Protokolldateien oder Zustand zu verändern.]{#logrotate-debug-dry .correct explanation="Sie ist die geeignete erste Syntax- und Entscheidungsprüfung, gefolgt von einer kontrollierten tatsächlichen Überprüfung."}
:::

## Andere Speicher berücksichtigen

Logrotate verwaltet Dateien, die in seinen Richtlinien benannt sind. Das systemd-Journal besitzt eine eigene Größen- und Aufbewahrungskonfiguration, während Datenbanken und entfernte Protokollierungsdienste getrennte Lebenszyklussteuerungen besitzen. Überwache Dateisystemkapazität und Protokollierungszustand, damit ein festhängender schreibender Prozess oder eine fehlgeschlagene Rotation erkannt wird, bevor der Speicherplatz erschöpft ist.

:::single-choice{#logrotate-journal-retention} Erzwingt eine logrotate-Regel automatisch die Aufbewahrung des systemd-Journals?

::option[Nein, der Journalspeicher besitzt eigene Konfiguration und Grenzen.]{#logrotate-journal-separate .correct explanation="Logrotate verwaltet nur Pfade, die durch seine Dateirichtlinien ausgewählt werden."}
::option[Ja, weil alle Protokolle dieselbe Aufbewahrungsengine verwenden.]{#logrotate-all-logs explanation="Dateirotation und Journalaufbewahrung sind getrennte Mechanismen."}
::option[Ja, aber nur, wenn kein Textprotokoll existiert.]{#logrotate-journal-fallback explanation="Das Vorhandensein von Textprotokollen führt die beiden Aufbewahrungssysteme nicht zusammen."}
:::

## Zusammenfassung

Du kannst nun eine Richtlinie zur Rotation von Dateiprotokollen entwerfen und überprüfen, ohne sie mit Archivierung zu verwechseln.

1. Bringe Speicherplatz-, Betriebs- und Aufbewahrungsanforderungen ins Gleichgewicht.
2. Definiere Generationen, Komprimierung, Eigentum und Verhalten bei leeren Dateien.
3. Koordiniere sicher mit Anwendungen, die Deskriptoren geöffnet halten.
4. Prüfe die Konfiguration im Debugmodus vor einer kontrollierten tatsächlichen Rotation.
5. Verwalte die Aufbewahrung von Journal und externen Speichern getrennt.
