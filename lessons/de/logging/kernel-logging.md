---
lesson_id: "kernel-logging"
course_id: "logging"
lang: "de"
order_index: 4
title: "Kernelprotokollierung"
description: "Lerne, aktuelle und aufbewahrte Linux-Kernelmeldungen mit dmesg und journalctl abzufragen."
meta_title: "Kernelprotokollierung – Protokollierung"
meta_description: "Erkunde das Linux-Kernelprotokoll einschließlich /var/log/kern.log und dmesg. Lerne, Bootmeldungen und Treiberinformationen zu prüfen und Systemprobleme zu untersuchen."
meta_keywords: "Kernelprotokoll, kern.log, /var/log/kern.log, Linux-Kernelprotokoll, dmesg, Linux-Protokollierung, Bootmeldungen, Kernelereignisse"
---

Der Kernel gibt Meldungen zu Bootvorgang, Treibern, Geräten, Dateisystemen, Netzwerk, Speicher und Fehlern aus. Diese Datensätze können Symptome auf niedriger Ebene erklären, doch eine einzelne Warnmeldung beweist nicht, dass Hardware defekt ist.

## Den Kernel-Ringpuffer lesen

`dmesg` liest Meldungen aus dem Ringpuffer des Kernels:

```bash
$ dmesg --human
```

Der Puffer besitzt eine begrenzte Kapazität, sodass neuere Meldungen ältere überschreiben können. Der Zugriff kann außerdem auf privilegierte Benutzer beschränkt sein. `dmesg --follow` verfolgt bei Implementierungen, die dies unterstützen, neue Kernelmeldungen; beende es nach einer begrenzten Reproduktion.

:::single-choice{#kernel-log-ring-buffer-limit} Warum kann ein älteres Kernelereignis in der aktuellen `dmesg`-Ausgabe fehlen?

::option[Kernelereignisse dürfen nur ein Zeichen enthalten.]{#kernel-log-one-character explanation="Kernelmeldungen können gewöhnlichen Diagnosetext und Metadaten enthalten."}
::option[`dmesg` löscht jede Zeile dauerhaft, nachdem sie angezeigt wurde.]{#kernel-log-display-deletes explanation="Ein gewöhnlicher Lesevorgang verbraucht nicht alle angezeigten Kernelmeldungen."}
::option[Der begrenzte Ringpuffer kann es überschrieben haben.]{#kernel-log-overwritten .correct explanation="Der speicherresidente Puffer bewahrt nur eine begrenzte Menge an Kernelmeldungsdaten auf."}
:::

## Lesbare Zeitstempel verwenden

Rohe Kernelzeitstempel sind gewöhnlich relativ zum Bootvorgang. `dmesg --ctime` oder `--human` kann sie als Uhrzeiten darstellen, doch umgerechnete Werte hängen vom Verlauf der Systemuhr ab und können ungenau sein, wenn sich die Uhr nach dem Bootvorgang geändert hat. Bewahre die bootrelative Zeitangabe, wenn eine genaue Reihenfolge wichtig ist.

:::single-choice{#kernel-log-timestamp-caution} Warum solltest du umgerechnete Uhrzeitstempel von `dmesg` mit Bedacht behandeln?

::option[Sie beziehen sich immer auf einen anderen Rechner.]{#kernel-log-other-machine explanation="Sie werden lokal abgeleitet, doch Uhränderungen können die Umrechnung beeinflussen."}
::option[Sie beruhen auf der Zuordnung bootrelativer Zeit zu einer Uhr, die sich ändern kann.]{#kernel-log-clock-change .correct explanation="Zeitsynchronisierung oder manuelle Uhränderungen können die dargestellte Uhrzeit irreführend machen."}
::option[Sie zeigen freien Dateisystemspeicher statt einer Zeit an.]{#kernel-log-free-space explanation="Zeitstempeloptionen zeigen weiterhin Zeiten und keine Speicherkapazität."}
:::

## Dauerhafte Kernelaufzeichnungen abfragen

Frage auf einem systemd-Host Kernelaufzeichnungen des aktuellen Bootvorgangs ab mit:

```bash
$ journalctl -k -b
```

Falls frühere Bootvorgänge in einem dauerhaften Journalspeicher aufbewahrt wurden, untersuche die Bootliste und wähle einen aus:

```bash
$ journalctl --list-boots
$ journalctl -k -b -1
```

Herkömmliche Syslog-Weiterleitung kann `/var/log/kern.log` oder eine andere Datei erstellen, doch dies hängt von der Konfiguration ab. Auch eine gespeicherte Datei `/var/log/dmesg` ist nicht allgemeingültig und stellt möglicherweise nur eine Momentaufnahme vom Bootvorgang dar.

:::single-choice{#kernel-log-previous-boot} Welcher Befehl fordert Kernelmeldungen des vorherigen aufbewahrten Bootvorgangs an?

::option[`journalctl -u kernel -f`]{#kernel-log-unit-follow explanation="Kernelmeldungen werden mit `-k` ausgewählt, und das Verfolgen wählt keinen vorherigen Bootvorgang."}
::option[`dmesg --clear`]{#kernel-log-clear explanation="Das Leeren verändert den Pufferzustand und ruft keinen früheren Bootvorgang ab."}
::option[`journalctl -k -b -1`]{#kernel-log-previous .correct explanation="Der Kernelfilter zusammen mit dem Bootversatz minus eins wählt den vorherigen aufbewahrten Bootvorgang aus."}
:::

## Ein Kernelereignis untersuchen

Ermittle Bootvorgang, Zeitstempel, Gerät, Subsystem und die zu diesem Zeitpunkt ausgeführte Aktion. Frage umgebende Kernel- und Dienstdatensätze ab und vergleiche anschließend Hardwareinventar und aktuellen Zustand:

```bash
$ journalctl -k -b --since '10 minutes ago'
$ lspci -k
$ lsblk
```

Verwende nur Werkzeuge, die für das Subsystem relevant sind. Beurteile vor dem Neuladen eines Treibers, dem Trennen eines Geräts oder einem Neustart die Auswirkungen auf Speicher, Netzwerk, Konsole und Dienste und bewahre einen Wiederherstellungszugang.

:::single-choice{#kernel-log-warning-response} Was ist die beste Reaktion auf eine einzelne Kernelwarnung?

::option[Sofort jeden geladenen Treiber entladen.]{#kernel-log-unload-all explanation="Dies kann wichtige Geräte unterbrechen und grenzt die Ursache der Warnung nicht ein."}
::option[Annehmen, dass der gesamte Rechner ersetzt werden muss.]{#kernel-log-replace-machine explanation="Ein einzelner Datensatz reicht für diese Schlussfolgerung nicht aus."}
::option[Sie mit umgebenden Ereignissen und dem aktuellen Subsystemzustand verknüpfen.]{#kernel-log-correlate .correct explanation="Zusammenhang und reproduzierbare Auswirkungen sind erforderlich, bevor eine Korrekturmaßnahme ausgewählt wird."}
:::

## Zusammenfassung

Du kannst aktuelle Meldungen des Kernelpuffers nun von aufbewahrten Kernelprotokollen unterscheiden.

1. Lies den begrenzten Ringpuffer mit `dmesg`.
2. Interpretiere bootrelative und umgerechnete Zeitstempel mit Bedacht.
3. Frage aktuelle oder vorherige Bootvorgänge mit `journalctl -k` ab.
4. Verknüpfe Kernelmeldungen, bevor du unterbrechende Änderungen vornimmst.
