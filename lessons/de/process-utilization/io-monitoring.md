---
lesson_id: "io-monitoring"
course_id: "process-utilization"
lang: "de"
order_index: 5
title: "E/A-Überwachung"
description: "Lerne, mit iostat-Stichproben CPU- und Blockgeräteaktivität zu untersuchen."
meta_title: "E/A-Überwachung – Prozessauslastung"
meta_description: "Lerne die Linux-E/A-Überwachung mit dem Befehl iostat. Diese Anleitung erklärt, wie du Messwerte zur CPU- und Datenträgernutzung analysierst, um die Systemleistung zu beurteilen."
meta_keywords: "E/A-Überwachung, iostat, Linux-E/A-Überwachung, CPU-Auslastung, Datenträgernutzung, Systemleistung, iowait, Linux-Befehle"
---

`iostat`, das gewöhnlich vom Paket `sysstat` bereitgestellt wird, meldet CPU- und Blockgeräteaktivität. Verwende wiederholte Stichproben zusammen mit der Anwendungslatenz: Durchsatz oder Auslastung allein belegen nicht, ob Speicher ein für Benutzer sichtbares Problem verursacht.

## Aussagekräftige Stichproben erfassen

Führe erweiterte Gerätestatistiken in Abständen von einer Sekunde aus:

```bash
$ iostat -xz 1
```

Bei üblichen Implementierungen enthält der erste Bericht Mittelwerte seit dem Bootvorgang, während spätere Berichte jeweils ein Intervall abdecken. Die Option `-x` ergänzt erweiterte Felder, und `-z` unterdrückt inaktive Geräte. Lasse mehrere Intervalle verstreichen, um normale und problematische Zeiträume zu erfassen.

:::single-choice{#iostat-first-report} Was stellt der erste `iostat`-Bericht üblicherweise dar?

::option[Nur Vorgänge aus der letzten Sekunde des Befehls.]{#iostat-final-second explanation="Dies beschreibt nicht den anfänglichen kumulativen Bericht."}
::option[Aktivitätsmittelwerte seit dem Systemstart.]{#iostat-since-boot .correct explanation="Spätere Berichte beziehen sich normalerweise auf einzelne Intervalle; der erste muss daher gesondert interpretiert werden."}
::option[Eine Prognose der Geräteauslastung von morgen.]{#iostat-forecast explanation="Das Werkzeug meldet beobachtete Statistiken und keinen künftigen Bedarf."}
:::

## CPU-Felder lesen

Der CPU-Abschnitt enthält häufig Benutzerzeit (`%user`), Systemzeit (`%system`), Leerlaufzeit (`%idle`), E/A-Wartezeit (`%iowait`) und von virtuellen Maschinen entzogene Zeit (`%steal`). E/A-Wartezeit ist CPU-Leerlaufzeit, während im System eine E/A-Anforderung noch nicht abgeschlossen ist; sie ist nicht der Prozentsatz, zu dem ein Datenträger ausgelastet ist.

:::single-choice{#iostat-iowait-meaning} Was beschreibt `%iowait`?

::option[Den Prozentsatz der bereits belegten Datenträgerkapazität.]{#iostat-capacity explanation="Dateisystemkapazität und CPU-Zeit sind unterschiedliche Messungen."}
::option[CPU-Leerlaufzeit, während eine E/A-Anforderung noch nicht abgeschlossen ist.]{#iostat-iowait-cpu .correct explanation="Es handelt sich um eine CPU-Zeitkategorie, die für sich allein kein Gerät identifizieren kann."}
::option[Die Anzahl der Dateien, die auf das Löschen warten.]{#iostat-delete-queue explanation="Anzahlen von Dateilöschungen werden durch dieses Feld nicht dargestellt."}
:::

## Gerätefelder lesen

Feldnamen unterscheiden sich je nach sysstat-Version, doch nützliche Konzepte sind:

- Lese- und Schreibvorgänge oder Daten pro Sekunde zeigen die Arbeitslastrate.
- `await` meldet die durchschnittliche Anforderungslatenz einschließlich Warteschlangen- und Bedienzeit.
- Felder für die durchschnittliche Warteschlangengröße zeigen wartende oder gerade bediente Anforderungen.
- `%util` meldet den Prozentsatz der verstrichenen Zeit, in der E/A auf dem Gerät im Gange war.

Ein hoher `%util`-Wert kann bei einem einfachen seriellen Gerät auf Sättigung hindeuten, lässt sich aber bei parallelem Speicher, Arrays oder virtuellen Geräten nicht unmittelbar in Leistungskapazität übersetzen. Vergleiche die Latenz mit dem Geräteaufbau, Arbeitslastmuster und Dienstziel.

:::single-choice{#iostat-await-purpose} Welches Feld steht am unmittelbarsten mit der durchschnittlichen Latenz von E/A-Anforderungen in Verbindung?

::option[Der Gerätename.]{#iostat-device-name explanation="Der Name identifiziert das Gerät, misst aber nicht die Dauer von Anforderungen."}
::option[`await`]{#iostat-await .correct explanation="Await bildet die durchschnittliche Dauer von Anforderungen einschließlich Warteschlangen- und Bedienzeit ab."}
::option[`%idle`]{#iostat-idle explanation="Dies ist ein CPU-Feld und nicht die Latenz von Geräteanforderungen."}
:::

## Die Belege miteinander verknüpfen

Ordne Gerätenamen Einhängepunkten und zugrunde liegenden Geräten zu, bevor du Schlussfolgerungen ziehst:

```bash
$ lsblk -o NAME,TYPE,SIZE,FSTYPE,MOUNTPOINTS
$ findmnt
```

Setze anschließend `iostat`-Intervalle zu Anwendungsantwortzeit, Datenbank- oder Dateisystemmesswerten und E/A auf Prozessebene in Beziehung. Device Mapper, RAID, Container und netzwerkgestützter Speicher können weitere Schichten hinzufügen, die eigene Werkzeuge erfordern.

:::single-choice{#iostat-high-util-conclusion} Was solltest du tun, nachdem du einen hohen `%util`-Wert auf einem Gerät gesehen hast?

::option[Annehmen, dass auf jedem Dateisystem der freie Speicherplatz erschöpft ist.]{#iostat-assume-full explanation="Auslastungszeit meldet nicht die Dateisystemkapazität."}
::option[Dateien löschen, bevor du die eingehängte Arbeitslast ermittelt hast.]{#iostat-delete-first explanation="Löschen verändert den Zustand und hat nichts mit dem Beleg eines E/A-Engpasses zu tun."}
::option[Latenz und Arbeitslastverhalten mit dem Speicheraufbau in Beziehung setzen.]{#iostat-correlate .correct explanation="Geräteparallelität und Arbeitslastziele bestimmen, ob die Beobachtung schädlich ist."}
:::

## Zusammenfassung

Du kannst `iostat` nun als Beleg in einer E/A-Untersuchung verwenden.

1. Erfasse mehrere Intervalle mit erweiterten Statistiken.
2. Unterscheide CPU-E/A-Wartezeit von Geräteauslastungszeit.
3. Interpretiere Latenz, Warteschlangen, Durchsatz und Auslastung gemeinsam.
4. Ordne Geräte Arbeitslasten zu und überprüfe die Auswirkungen auf die Anwendung.
