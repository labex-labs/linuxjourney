---
lesson_id: "continuous-monitoring"
course_id: "process-utilization"
lang: "de"
order_index: 7
title: "Kontinuierliche Überwachung"
description: "Lerne, wie die Datenerfassung von sysstat und sar-Berichte historische Linux-Leistungsanalysen unterstützen."
meta_title: "Kontinuierliche Überwachung – Prozessauslastung"
meta_description: "Lerne die kontinuierliche Überwachung von Linux-Systemen mit sar. Verstehe Installation, Datenerfassung und die Analyse historischer Ressourcennutzung zur Leistungsbeurteilung."
meta_keywords: "sar, sysstat, Linux-Überwachung, Systemleistung, kontinuierliche Überwachung, Einsteiger, Tutorial, Anleitung"
---

Interaktive Werkzeuge zeigen, was geschieht, während du sie beobachtest. Wenn eine Verlangsamung bereits vorbei ist, wird historische Überwachung benötigt. Die Werkzeugsammlung `sysstat` erfasst regelmäßig Systemzähler, und `sar` liest entweder aktuelle Zähler oder gespeicherte Aktivitätsdateien.

## Datenerfassung aktivieren

Installiere das `sysstat`-Paket der Distribution und bestätige anschließend, dass sein Erfassungs- und Aufbewahrungsmechanismus aktiviert ist. Die genauen Dienst-, Timer- und Konfigurationspfade unterscheiden sich je nach Distribution; die Paketinstallation garantiert nicht, dass die Erfassung begonnen hat.

Untersuche auf einem systemd-Host die vom Paket bereitgestellten Units, statt ihre Namen zu erraten:

```bash
$ systemctl list-unit-files | grep sysstat
$ systemctl list-timers --all | grep sysstat
```

Überprüfe, ob im sysstat-Datenverzeichnis der Distribution neue Aktivitätsdateien erstellt werden, und prüfe ihre Berechtigungen sowie die Aufbewahrungsrichtlinie.

:::single-choice{#sar-installation-verification} Was solltest du nach der Installation von `sysstat` überprüfen?

::option[Dass die Erfassung aktiviert ist und Aktivitätsdateien aktualisiert werden.]{#sar-collector-updating .correct explanation="Paketinstallation und aktive regelmäßige Datenerfassung sind getrennte Bedingungen."}
::option[Dass jeder Prozess manuell neu gestartet wurde.]{#sar-restart-processes explanation="Die Installation eines Überwachungsdatensammlers erfordert keinen Neustart jeder Arbeitslast."}
::option[Dass alle historischen Dateien für jeden schreibbar sind.]{#sar-world-writable explanation="Überwachungsdaten sollten angemessene Zugriffskontrollen behalten."}
:::

## Aktuelle Stichproben lesen

Fordere von `sar` drei CPU-Berichte in Abständen von einer Sekunde an:

```bash
$ sar -u 1 3
```

Weitere häufige Berichte umfassen Ausführungswarteschlange und Last (`-q`), Arbeitsspeicher (`-r`), Paging (`-B`), Blockgeräte (`-d`) und Aktivität einzelner CPUs (`-P ALL`). Optionen und Felder unterscheiden sich je nach sysstat-Version; lies daher `sar --help` oder die lokale Handbuchseite.

:::single-choice{#sar-one-second-count} Was fordert `sar -u 1 3` an?

::option[Drei CPU-Berichte in Abständen von einer Sekunde.]{#sar-three-cpu-samples .correct explanation="Die erste Zahl ist das Intervall in Sekunden, die zweite die Anzahl der Berichte."}
::option[Einen Bericht, der genau drei Tage abdeckt.]{#sar-three-days explanation="Die Operanden geben Stichprobenintervall und Anzahl und keinen Datumsbereich an."}
::option[Das Löschen von drei gespeicherten CPU-Dateien.]{#sar-delete-files explanation="Der Befehl liest Zähler und fordert kein Löschen an."}
:::

## Historische Dateien lesen

Speicherorte und Namen gespeicherter Dateien unterscheiden sich und liegen häufig unter `/var/log/sysstat` oder `/var/log/sa`. Übergib mit `-f` eine ausgewählte Aktivitätsdatei:

```bash
$ sar -q -f /var/log/sysstat/sa02
```

Bestätige das vollständige Datum der Datei anhand der Berichtsüberschriften. Eine zweistellige Endung bezeichnet häufig einen Tag des Monats und kann über mehrere Aufbewahrungszeiträume hinweg mehrdeutig sein. Gespeicherte Binärformate können außerdem eine kompatible sysstat-Version erfordern.

:::single-choice{#sar-historical-file-option} Welche Option weist `sar` an, eine bestimmte Aktivitätsdatei zu lesen?

::option[`-P`]{#sar-option-p explanation="Dies wählt die Prozessorberichterstattung und keine Eingabedatei aus."}
::option[`-q`]{#sar-option-q explanation="Dies wählt die Berichterstattung zu Warteschlange und Last aus."}
::option[`-f`]{#sar-option-f .correct explanation="Die Dateioption wählt die zu lesenden gespeicherten Aktivitätsdaten aus."}
:::

## Einen Vorfall untersuchen

Bestimme Zeit und Zeitzone des Vorfalls und vergleiche anschließend mehrere Signale über dasselbe Intervall. Suche nach Änderungen bei Last, CPU, Ausführungswarteschlange, Paging, Geräteaktivität, Netzwerkverkehr und Anwendungslatenz. Zähleränderungen zeigen Korrelation und nicht unbedingt Kausalität; Bereitstellungsaufzeichnungen und Anwendungsprotokolle können den Auslöser erklären.

Lücken können bedeuten, dass der Host außer Betrieb war, die Erfassung fehlgeschlagen ist oder Daten durch die Aufbewahrung entfernt wurden. Überwache die Überwachungspipeline selbst, damit fehlende Belege schon vor einem Vorfall sichtbar werden.

:::single-choice{#sar-incident-method} Wie sollten historische `sar`-Daten bei der Nachbereitung eines Vorfalls verwendet werden?

::option[Den höchsten einzelnen Zähler als bewiesene Ursache behandeln.]{#sar-single-root explanation="Eine einzelne Korrelation belegt keine Kausalität."}
::option[Mehrere Messwerte über dasselbe bestätigte Zeitfenster vergleichen.]{#sar-correlate-window .correct explanation="Zeitlich ausgerichtete Signale helfen, Hypothesen zu unterscheiden und Systemverhalten mit dem Vorfall zu verbinden."}
::option[Lücken ignorieren, weil die Erfassung nach der Installation garantiert ist.]{#sar-ignore-gaps explanation="Die Erfassung kann fehlschlagen oder deaktiviert sein; Lücken müssen erklärt werden."}
:::

## Zusammenfassung

Du kannst `sar` nun verwenden, um Leistung außerhalb einer interaktiven Sitzung zu untersuchen.

1. Überprüfe, dass Erfassung und Aufbewahrung tatsächlich aktiv sind.
2. Fordere begrenzte aktuelle Stichproben mit Intervall und Anzahl an.
3. Wähle historische Aktivitätsdateien ausdrücklich aus.
4. Richte mehrere Messwerte an Vorfallszeit und Arbeitslastbelegen aus.
