---
lesson_id: "process-threads"
course_id: "process-utilization"
lang: "de"
order_index: 3
title: "Prozess-Threads"
description: "Lerne, welche Prozessressourcen Linux-Threads gemeinsam nutzen und wie du sie mit ps untersuchst."
meta_title: "Prozess-Threads – Prozessauslastung"
meta_description: "Eine Anleitung zu Linux-Prozess-Threads. Lerne den Unterschied zwischen ein- und mehrthreadigen Prozessen kennen und erfahre, wie du Threads mit dem Befehl ps anzeigst."
meta_keywords: "Linux-Threads, Prozess-Threads, ps Threads anzeigen, ps m, mehrthreadig, einthreadig, leichtgewichtiger Prozess, Linux-Prozessverwaltung"
---

Ein Thread ist ein innerhalb eines Prozesses eingeplanter Ausführungsfluss. Jeder laufende Prozess besitzt mindestens einen Thread, und ein mehrthreadiger Prozess besitzt mehrere Abläufe, die gleichzeitig Fortschritte machen können.

## Prozesse und Threads

Threads eines Prozesses nutzen Ressourcen wie den virtuellen Adressraum und offene Dateideskriptoren gemeinsam. Jeder Thread besitzt dennoch einen eigenen Ausführungszustand einschließlich Registern und Stack. Das gemeinsame Nutzen ermöglicht effiziente Kommunikation, bedeutet aber auch, dass eine nicht synchronisierte Änderung eines Threads die anderen beeinflussen kann.

Getrennte Prozesse besitzen normalerweise unterschiedliche Adressräume und kommunizieren über ausdrückliche Interprozessmechanismen. Keine der beiden Bauweisen ist automatisch schneller oder sicherer; Arbeitslast und Implementierung bestimmen den Kompromiss.

:::single-choice{#threads-shared-resource} Welche Ressource wird normalerweise von Threads desselben Prozesses gemeinsam genutzt?

::option[Der virtuelle Adressraum des Prozesses.]{#threads-shared-address-space .correct explanation="Threads können auf denselben Prozessspeicher zugreifen, unter Beachtung der Programmsynchronisierung."}
::option[Eine eigene Kernelinstallation für jeden Thread.]{#threads-separate-kernel explanation="Alle Threads verwenden den laufenden Systemkernel."}
::option[Eine andere Dateisystemwurzel für jeden Thread.]{#threads-different-root explanation="Threads teilen normalerweise den Dateisystemkontext des Prozesses, statt getrennte Wurzeln zu erhalten."}
:::

## Thread-Kennungen

Linux stellt jeden Thread als ein planbares Task mit eigener Thread-ID dar. Die ID des Threadgruppenleiters wird gewöhnlich als Prozess-ID angezeigt, während alle Mitglieder eine Threadgruppen-ID gemeinsam haben. Werkzeuge verwenden Bezeichnungen wie `PID`, `TID`, `LWP` und `SPID`; prüfe die Felddefinitionen des Werkzeugs, statt anzunehmen, dass jede Bezeichnung dasselbe bedeutet.

:::single-choice{#threads-own-scheduling-state} Was verwaltet jeder Thread unabhängig?

::option[Die vollständige Tabelle offener Dateien des Prozesses.]{#threads-open-files-shared explanation="Threads eines Prozesses nutzen offene Dateideskriptoren normalerweise gemeinsam."}
::option[Die systemweite Benutzerdatenbank des Rechners.]{#threads-user-database explanation="Kontendatenbanken sind kein privater Threadzustand."}
::option[Seinen Ausführungszustand und Stack.]{#threads-stack-state .correct explanation="Ein Thread benötigt einen eigenen Ausführungskontext, obwohl Prozessressourcen gemeinsam genutzt werden."}
:::

## Threads mit ps auflisten

Verwende ausdrückliche Ausgabefelder, um mehrdeutige Standarddarstellungen zu vermeiden:

```bash
$ ps -eLo pid,tid,psr,stat,comm
```

Bei `ps` aus procps zeigt `-L` Threads an, und `-e` wählt alle Prozesse aus. `pid` bezeichnet die Threadgruppe, `tid` einen einzelnen Thread, `psr` die CPU, auf der er zuletzt lief, und `stat` seinen Zustand. So untersuchst du einen einzelnen Prozess:

```bash
$ ps -L -p 1234 -o pid,tid,stat,pcpu,comm
```

Threadauflistungen sind Momentaufnahmen. Ein Thread kann unmittelbar danach enden oder seinen Zustand ändern.

:::single-choice{#threads-ps-one-process} Welcher Befehl listet die Threads von PID 1234 mit ausdrücklichen Feldern auf?

::option[`ps -p 1234 -o pid,ppid,stat,pcpu,comm`]{#threads-process-only explanation="Diese Ausgabe fordert keine einzelnen Threadzeilen an."}
::option[`ps -L -p 1234 -o pid,tid,stat,pcpu,comm`]{#threads-ps-l .correct explanation="Die Option `-L` fordert Threadzeilen für den ausgewählten Prozess an."}
::option[`ps -e -o pid,user,stat,pcpu,comm`]{#threads-all-processes explanation="Dies wählt systemweit Prozesse ohne Thread-IDs aus."}
:::

## Threadaktivität interpretieren

Eine hohe CPU-Auslastung eines einzelnen Threads kann durch einen prozessweiten Mittelwert verborgen werden. Verknüpfe CPU-Stichproben auf Threadebene mit Anwendungsprotokollen, Stacktraces und Profiling-Werkzeugen. Hänge keine Debugger an Produktions-Tasks und sende ihnen keine Signale, ohne die Auswirkungen von Pausen, Berechtigungen und Diensten zu verstehen.

:::single-choice{#threads-snapshot-limit} Warum solltest du eine Threadauflistung von `ps` nicht als dauerhaften Zustand betrachten?

::option[`ps` erzeugt für jede Zeile einen Ersatz-Thread.]{#threads-ps-creates explanation="Der Befehl beobachtet Tasks und klont nicht jeden aufgelisteten Task."}
::option[Thread-IDs sind auf jedem Linux-Host identisch.]{#threads-identical-ids explanation="Kennungen werden innerhalb eines laufenden Systems vergeben und sind nicht universell."}
::option[Threads können nach der Momentaufnahme ihren Zustand ändern oder enden.]{#threads-change-after-snapshot .correct explanation="Die Prozessuntersuchung beobachtet einen Augenblick in einem sich ständig ändernden System."}
:::

## Zusammenfassung

Du kannst nun Prozessressourcen von Ausführungszuständen einzelner Threads unterscheiden.

1. Erkenne, dass jeder Prozess mindestens einen Thread besitzt.
2. Ermittle Ressourcen, die Threads eines Prozesses gemeinsam nutzen.
3. Liste mit `ps -L` ausdrückliche Prozess- und Thread-IDs auf.
4. Behandle Threadausgaben als Momentaufnahme und verknüpfe sie mit weiteren Belegen.
