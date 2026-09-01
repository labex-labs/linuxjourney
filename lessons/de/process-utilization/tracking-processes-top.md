---
lesson_id: "tracking-processes-top"
course_id: "process-utilization"
lang: "de"
order_index: 1
title: "Prozesse verfolgen: top"
description: "Lerne, mit top Systemlast, CPU, Arbeitsspeicher und die Aktivität einzelner Prozesse zu beurteilen."
meta_title: "Prozesse verfolgen: top – Prozessauslastung"
meta_description: "Lerne den Linux-Befehl top kennen. Diese Anleitung erklärt, wie du Systemressourcen überwachst, Prozesse verfolgst und Kennzahlen wie VIRT und RES verstehst."
meta_keywords: "Linux top-Befehl, Prozesse überwachen, Systemauslastung, Funktionsweise von Linux, Linux top VIRT RES, Linux lernen, Linux-Leistung, Prozessverwaltung, kostenloses Linux-Training"
---

`top` bietet eine wiederholt aktualisierte Ansicht der Systemaktivität und laufenden Prozesse. Das Programm eignet sich dazu, eine Leistungshypothese zu entwickeln, doch eine einzelne stark ausgelastete Stichprobe beweist noch nicht die Ursache eines Problems. Vergleiche mehrere Aktualisierungen und setze sie zu Protokollen sowie arbeitslastspezifischen Messwerten in Beziehung.

## Die Systemübersicht lesen

Eine typische Anzeige beginnt mit Übersichtszeilen, gefolgt von einer Prozesstabelle:

```text
top - 18:06:26 up 6 days, 4:07, 2 users, load average: 0.92, 0.62, 0.59
Tasks: 389 total, 1 running, 387 sleeping, 0 stopped, 1 zombie
%Cpu(s): 1.8 us, 0.4 sy, 0.0 ni, 97.6 id, 0.1 wa, 0.0 hi, 0.0 si, 0.0 st
MiB Mem : 32099.0 total, 5276.3 free, 7031.2 used, 19791.5 buff/cache
MiB Swap: 32700.0 total, 32661.0 free, 39.0 used
```

Die erste Zeile enthält die aktuelle Uhrzeit, Betriebsdauer, Anzahl angemeldeter Benutzer und die Lastmittelwerte über 1, 5 und 15 Minuten. Die Taskzeile zählt die Prozesszustände. Der Lastmittelwert ist kein unmittelbarer CPU-Prozentwert; unter Linux umfasst er ausführbare Tasks und Tasks in nicht unterbrechbarem Schlaf. Beurteile ihn deshalb zusammen mit CPU-Anzahl, E/A-Aktivität und Latenz.

:::single-choice{#top-load-average-periods} Was stellen die drei Lastmittelwerte in `top` dar?

::option[Die durchschnittliche Last über 1, 5 und 15 Minuten.]{#top-one-five-fifteen .correct explanation="Die Werte fassen zunehmend längere vergangene Zeitfenster zusammen."}
::option[Die CPU-Auslastung durch die drei aktivsten Prozesse.]{#top-three-processes explanation="Die CPU-Auslastung einzelner Prozesse erscheint in der Prozesstabelle und nicht in diesen drei Übersichtswerten."}
::option[Freien Arbeitsspeicher, Cache und Swap in Megabyte.]{#top-three-memory-values explanation="Arbeitsspeicher und Swap besitzen eigene Übersichtszeilen."}
:::

## CPU-Zeit interpretieren

Häufige CPU-Felder sind:

- `us`: Ausführungszeit im Userspace.
- `sy`: Ausführungszeit im Kernel.
- `ni`: Userspace-Zeit für Tasks mit angepasstem Nice-Wert.
- `id`: Leerlaufzeit.
- `wa`: Leerlaufzeit, während eine noch nicht abgeschlossene E/A-Anforderung besteht.
- `hi` und `si`: Verarbeitung von Hardware- und Software-Interrupts.
- `st`: virtuelle CPU-Zeit, die der Hypervisor für andere Gäste beansprucht.

Ein hoher `wa`-Wert kann eine Hypothese über E/A-Wartezeit stützen, identifiziert aber weder ein Gerät noch beweist er, dass Speicher der einzige Engpass ist. Untersuche Gerätelatenz und Anwendungsverhalten, bevor du eine Schlussfolgerung ziehst.

:::single-choice{#top-cpu-wa-meaning} Was meldet das CPU-Feld `wa`?

::option[Zeit, die mit der Ausführung gewöhnlichen Benutzercodes verbracht wurde.]{#top-wa-user explanation="Die Ausführung im Userspace wird unter `us` gemeldet."}
::option[Die Anzahl der seit dem Bootvorgang in den Swap geschriebenen Speicherseiten.]{#top-wa-swap explanation="Swap-Aktivität ist keine CPU-Zeitkategorie."}
::option[CPU-Leerlaufzeit, während eine E/A-Anforderung noch nicht abgeschlossen ist.]{#top-wa-io .correct explanation="Das Feld bezeichnet E/A-Wartezeit und erfordert zur Diagnose unterstützende Gerätebelege."}
:::

## Die Prozesstabelle lesen

Wichtige Spalten sind häufig:

- `PID`, `USER` und `COMMAND`: Identität und Eigentümer.
- `S`: Zustand wie laufend (`R`), schlafend (`S`), nicht unterbrechbarer Schlaf (`D`), gestoppt (`T`) oder Zombie (`Z`).
- `%CPU` und `%MEM`: gemessene CPU-Aktivität und Anteil am physischen Arbeitsspeicher.
- `TIME+`: angesammelte CPU-Zeit.
- `VIRT`: gesamter virtueller Adressraum, der dem Task zugeordnet ist.
- `RES`: aktuell zugeordneter residenter, nicht ausgelagerter physischer Speicher.
- `SHR`: residenter Speicher, der möglicherweise mit anderen Prozessen geteilt wird.

`VIRT` ist nicht die Menge des verbrauchten physischen Arbeitsspeichers. Der Wert kann abgebildete Dateien, gemeinsam genutzte Bibliotheken, reservierten Adressraum und ausgelagerte Seiten umfassen. Selbst `RES` ist mit Bedacht zu interpretieren, da gemeinsam genutzte Seiten die Zuordnung erschweren.

:::single-choice{#top-res-versus-virt} Welches Feld kommt dem aktuell residenten physischen Speicher eines Prozesses am nächsten?

::option[`TIME+`]{#top-time-field explanation="Dieses Feld summiert CPU-Zeit und keinen Speicher."}
::option[`VIRT`]{#top-virt-field explanation="Die virtuelle Größe umfasst Adressraum, der nicht im Arbeitsspeicher resident sein muss."}
::option[`RES`]{#top-res-field .correct explanation="Die residente Größe bildet die derzeit für den Prozess im physischen Speicher befindlichen Seiten ab, unter Vorbehalt gemeinsam genutzter Seiten."}
:::

## Fokussieren und sortieren

Überwache bekannte PIDs direkt:

```bash
$ top -p 1234,5678
```

Drücke innerhalb von `top` bei üblichen procps-ng-Implementierungen `P` zum Sortieren nach CPU, `M` zum Sortieren nach Speicher, `1` zum Umschalten einzelner CPU-Zeilen und `q` zum Beenden. Drücke `h` für die lokale interaktive Hilfe, da sich Tasten und Felder je nach Implementierung unterscheiden können.

Notiere PID, Befehl, Zeitstempel und mehrere Stichproben, bevor du eingreifst. Dass ein Prozess kurz an der Spitze erscheint, kann normal sein; ihn zu beenden kann Datenverlust oder einen Ausfall verursachen.

:::single-choice{#top-monitor-known-pid} Welcher Aufruf beschränkt die Anzeige auf PID 1234?

::option[`top -u 1234`]{#top-user-filter explanation="Die Form `-u` filtert nach Benutzer, statt den Wert als PID zu behandeln."}
::option[`top -d 1234`]{#top-delay-filter explanation="Die Option `-d` steuert bei üblichen Implementierungen das Aktualisierungsintervall."}
::option[`top -p 1234`]{#top-pid-filter .correct explanation="Die Option `-p` wählt eine oder mehrere Prozess-IDs zur Überwachung aus."}
:::

## Zusammenfassung

Du kannst `top` nun verwenden, um eine Hypothese zur Systemleistung aufzustellen und zu prüfen.

1. Lies Lastmittelwerte als Last über Zeitfenster und nicht als CPU-Prozentwerte.
2. Vergleiche CPU-Kategorien über mehrere Stichproben hinweg.
3. Unterscheide virtuellen Adressraum von residentem Speicher.
4. Konzentriere dich auf bekannte PIDs und prüfe Belege, bevor du eingreifst.
