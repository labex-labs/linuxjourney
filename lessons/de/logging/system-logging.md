---
lesson_id: "system-logging"
course_id: "logging"
lang: "de"
order_index: 1
title: "Systemprotokollierung"
description: "Lerne, wie Linux-Protokollquellen, Datensammler, Speicher und Anzeigewerkzeuge zusammenwirken."
meta_title: "Systemprotokollierung – Protokollierung"
meta_description: "Lerne die Linux-Systemprotokollierung kennen. Diese Anleitung behandelt syslog, rsyslogd sowie das Auffinden und Lesen von Protokolldateien unter /var/log."
meta_keywords: "Linux lernen, Linux-Systemprotokollierung, syslog, rsyslogd, var log, Systemprotokolle, Linux-Befehlszeile lernen, Linux-Ressourcen"
---

Protokolle zeichnen Ereignisse auf, die vom Kernel, von Diensten, Anwendungen und Sicherheitskomponenten ausgegeben werden. Sie unterstützen Fehlersuche und Audits, aber nur, wenn die Erfassung funktioniert, Zeitstempel richtig verstanden werden und die betreffende Quelle einbezogen ist.

## Den Weg einer Protokollnachricht verfolgen

Ein Protokollierungsweg besteht aus mehreren unterschiedlichen Teilen:

1. Eine Quelle gibt ein Ereignis aus.
2. Ein Datensammler nimmt es an und reichert es an.
3. Weiterleitungs- und Aufbewahrungsregeln wählen Speicher- oder Weiterleitungsziele aus.
4. Ein Anzeigewerkzeug fragt die gespeicherten Datensätze ab.

Auf einem systemd-Host sammelt `systemd-journald` gewöhnlich die Standardausgabe von Diensten, Kernelmeldungen sowie native Journal- oder Syslog-Nachrichten. Ein Syslog-Daemon wie rsyslog kann ebenfalls Nachrichten empfangen und herkömmliche Textdateien schreiben oder sie weiterleiten. Anwendungen können stattdessen eigene Dateien oder externe Telemetrie verwalten.

:::single-choice{#system-logging-distinct-roles} Welche Komponente entscheidet, wo angenommene Nachrichten gespeichert oder wohin sie weitergeleitet werden?

::option[Das aktuelle Arbeitsverzeichnis des Terminals.]{#system-logging-cwd explanation="Ein Shellverzeichnis definiert keine systemweiten Protokollierungswege."}
::option[Der Dateiname des laufenden Kernelabbilds.]{#system-logging-kernel-file explanation="Der Kernel kann Nachrichten ausgeben, doch der Dateiname seines Abbilds ist keine Weiterleitungsrichtlinie."}
::option[Die Konfiguration für Weiterleitung und Aufbewahrung.]{#system-logging-routing .correct explanation="Regeln zwischen Erfassung und Speicherung bestimmen Ziele und Aufbewahrungsverhalten."}
:::

## Verfügbare Protokolle ermitteln

Nimm nicht an, dass jeder Host dieselben Dateien besitzt. Untersuche die aktiven Protokollierungsdienste und die lokale Konfiguration:

```bash
$ systemctl --type=service --state=running | grep -E 'journal|syslog'
$ ls -la /var/log
$ journalctl --disk-usage
```

`/var/log/syslog` ist auf Systemen der Debian-Familie mit entsprechender Weiterleitung verbreitet, während andernorts häufig `/var/log/messages` verwendet wird. Auf einem reinen Journal-Host kann jede dieser Dateien fehlen. Die Anwendungsdokumentation und Unit-Konfiguration können weitere Ziele erkennen lassen.

:::single-choice{#system-logging-file-absence} Was bedeutet eine fehlende Datei `/var/log/syslog` zwingend?

::option[Der Host verwendet möglicherweise ein anderes konfiguriertes Protokollierungsziel.]{#system-logging-other-destination .correct explanation="Reine Journal-Systeme und andere Syslog-Richtlinien müssen diese Datei nicht erstellen."}
::option[Der Kernel hat noch nie eine Nachricht erzeugt.]{#system-logging-no-kernel explanation="Kernelaufzeichnungen können im Journal oder an einem anderen Ziel vorhanden sein."}
::option[Jede Anwendung wurde beendet.]{#system-logging-apps-stopped explanation="Der Anwendungszustand lässt sich aus einem einzigen fehlenden Pfad nicht ableiten."}
:::

## Das Journal abfragen

Beginne mit einer begrenzten Abfrage, statt das gesamte Journal auszugeben:

```bash
$ journalctl -b -p warning
$ journalctl -u ssh.service --since '1 hour ago'
```

`-b` wählt den aktuellen Bootvorgang aus, `-p` filtert nach Priorität und `-u` nach einer Unit. Unit-Namen und aufbewahrte Bootvorgänge unterscheiden sich je nach Host. Verwende `journalctl --list-boots`, um verfügbare Bootvorgänge zu sehen, und `journalctl -f`, um neue Datensätze während der Reproduktion eines Problems zu verfolgen.

:::single-choice{#system-logging-current-boot} Welche Option beschränkt eine `journalctl`-Abfrage auf den aktuellen Bootvorgang?

::option[`-b`]{#system-logging-boot-option .correct explanation="Ohne Argument wählt der Bootselektor den aktuellen Bootvorgang aus."}
::option[`-u`]{#system-logging-unit-option explanation="Dies filtert nach einer systemd-Unit."}
::option[`-f`]{#system-logging-follow-option explanation="Dies verfolgt neu angehängte Datensätze."}
:::

## Datensätze im Zusammenhang lesen

Eine herkömmliche Zeile im Syslog-Stil kann so aussehen:

```text
Jan 27 07:41:32 icebox anacron[4650]: Job `cron.weekly' started
```

Sie enthält einen Zeitstempel, Host, Programm und PID sowie anschließend eine Nachricht. Behandle den Nachrichtentext als Anwendungsausgabe und nicht als garantiert strukturierte Tatsache. Prüfe Zeitzone, Uhrsynchronisierung, Boot-ID, Wiederverwendung von PIDs und Datensätze unmittelbar vor und nach dem Ereignis. Journalfelder können stärkere Kennungen liefern als nur der dargestellte Text.

Protokolle können Benutzernamen, Adressen, Pfade, Token oder andere vertrauliche Daten enthalten. Verwende Zugriff mit geringstmöglichen Berechtigungen, schwärze Exporte und bewahre während einer Untersuchung Originale und Zeitstempel.

:::single-choice{#system-logging-export-safety} Was solltest du tun, bevor du einen Protokollauszug extern weitergibst?

::option[Jeden Zeitstempel durch einen Zufallswert ersetzen.]{#system-logging-random-time explanation="Das Zerstören von Zeitangaben kann Korrelationen verhindern und ist keine geeignete Schwärzungsmethode."}
::option[Ihn auf Geheimnisse und vertrauliche Kennungen prüfen.]{#system-logging-review-sensitive .correct explanation="Protokolle enthalten häufig Betriebs- oder personenbezogene Daten, die kontrolliert geschwärzt werden müssen."}
::option[Das ursprüngliche Protokoll für jeden schreibbar machen.]{#system-logging-world-writable explanation="Schwächere Zugriffskontrollen können die Integrität beeinträchtigen und weitere Daten offenlegen."}
:::

## Zusammenfassung

Du kannst Linux-Protokolle nun auffinden und abfragen, ohne einen allgemeingültigen Speicherpfad anzunehmen.

1. Trenne Ereignisquellen, Datensammler, Weiterleitung, Speicher und Anzeigewerkzeuge.
2. Ermittle die aktive Protokollierungskonfiguration des Hosts.
3. Verwende begrenzte Journalabfragen für eine Unit, einen Bootvorgang, Zeitraum oder eine Priorität.
4. Setze Datensätze in Zusammenhang und schütze vertrauliche Protokolldaten.
