---
lesson_id: "memory-monitoring"
course_id: "process-utilization"
lang: "de"
order_index: 6
title: "Arbeitsspeicherüberwachung"
description: "Lerne, vmstat-Stichproben zu Speicher, Paging, Prozessen, E/A und CPU zu interpretieren."
meta_title: "Arbeitsspeicherüberwachung – Prozessauslastung"
meta_description: "Lerne die Linux-Arbeitsspeicherüberwachung mit dem Befehl vmstat. Diese Anleitung erklärt, wie du mit diesem Werkzeug Messwerte zur Systemleistung analysierst."
meta_keywords: "Arbeitsspeicherüberwachung, Speicherauslastungsmonitor, vmstat, Linux-Arbeitsspeicher, Systemleistung, Speichernutzung, Linux-Tutorial"
---

Linux verwendet ansonsten ungenutzten Speicher absichtlich für Caches. Ein kleiner `free`-Wert allein beweist daher keinen Speicherdruck. `vmstat` hilft, Speicher zu ausführbaren Tasks, Paging, E/A und CPU-Aktivität in Beziehung zu setzen.

## Stichproben mit vmstat

Erfasse eine Stichprobe pro Sekunde:

```bash
$ vmstat 1
```

Die erste Datenzeile meldet im Allgemeinen Mittelwerte seit dem Bootvorgang; spätere Zeilen decken jeweils ein Intervall ab. Beende die Erfassung nach einem repräsentativen Zeitraum mit `Ctrl-C`. Einheiten und verfügbare Felder unterscheiden sich; prüfe deshalb `vmstat --unit` und die lokale Handbuchseite.

:::single-choice{#vmstat-interval-rows} Welche Zeilen eignen sich am besten, um mit `vmstat 1` Änderungen von Sekunde zu Sekunde zu beobachten?

::option[Die späteren Zeilen nach dem ersten Bericht.]{#vmstat-later-rows .correct explanation="Spätere Zeilen beschreiben jeweils das angeforderte Intervall statt des kumulativen Zeitraums."}
::option[Nur die Überschriften oberhalb der ersten Datenzeile.]{#vmstat-headings explanation="Überschriften definieren Felder, enthalten aber keine Aktivitätsstichproben."}
::option[Nur eine von einem anderen Host kopierte Zeile.]{#vmstat-other-host explanation="Ein anderes System bildet die aktuelle Arbeitslast nicht ab."}
:::

## Prozesse und Arbeitsspeicher

Häufige Prozessfelder sind `r` für ausführbare Tasks und `b` für Tasks, die in nicht unterbrechbarem Schlaf blockiert sind. Zu den Speicherfeldern gehören verwendeter Swap (`swpd`), ungenutzter Speicher (`free`), Puffer (`buff`) und Cache (`cache`). Dies sind systemweite Werte und kein Verbrauch einzelner Prozesse.

Vergleiche für eine leichter verständliche Ansicht des aktuell verfügbaren Speichers mit:

```bash
$ free -h
```

Die Schätzung `available` ist im Allgemeinen nützlicher als `free` allein, weil rückgewinnbarer Cache neue Speicherzuweisungen erfüllen kann.

:::single-choice{#vmstat-free-memory} Warum kann ein niedriger `free`-Wert unter Linux normal sein?

::option[Der Wert schließt immer den gesamten physischen Arbeitsspeicher aus.]{#vmstat-excludes-ram explanation="Es handelt sich um ein Speicherfeld, dessen genaue Einheit allerdings geprüft werden sollte."}
::option[Der Kernel kann ungenutzten Speicher für rückgewinnbare Caches verwenden.]{#vmstat-reclaimable-cache .correct explanation="Zwischengespeicherter Speicher kann häufig zurückgewonnen werden, wenn Anwendungen ihn benötigen."}
::option[Wenig freier Speicher beweist, dass die CPU ausgeschaltet ist.]{#vmstat-cpu-off explanation="Speicherzuweisung und CPU-Energiezustand lassen keine solche gemeinsame Schlussfolgerung zu."}
:::

## Paging und E/A

`si` und `so` zeigen die Swap-in- und Swap-out-Raten. Anhaltendes Paging zusammen mit Latenz und Aktivität zur Speicherrückgewinnung kann auf Druck hindeuten. Eine von null verschiedene Swap-Nutzung (`swpd`) beweist für sich allein jedoch kein aktuelles Problem. `bi` und `bo` melden Blockeingabe- und Blockausgaberaten und sind nicht auf Swap-Verkehr beschränkt.

:::single-choice{#vmstat-swap-pressure} Welche Belege stützen die Diagnose eines aktuellen Speicherdrucks besser?

::option[Ein von null verschiedener `swpd`-Wert ohne weitere Beobachtungen.]{#vmstat-swpd-alone explanation="Seiten können nach früherem Druck im Swap verbleiben; die Menge allein reicht daher nicht aus."}
::option[Anhaltendes Paging in Verbindung mit Rückgewinnungsaktivität und Arbeitslastlatenz.]{#vmstat-correlated-pressure .correct explanation="Wiederholte, verknüpfte Belege verbinden das Speicherverhalten mit aktuellen Auswirkungen."}
::option[Der bei der Anmeldung ausgegebene Hostname.]{#vmstat-hostname explanation="Ein Hostname misst weder Rückgewinnungs- noch Paging-Aktivität."}
:::

## CPU- und Systemaktivität

CPU-Spalten enthalten gewöhnlich die Prozentanteile für Benutzer (`us`), System (`sy`), Leerlauf (`id`), E/A-Wartezeit (`wa`) und entzogene Zeit (`st`). Systemspalten enthalten Interrupts (`in`) und Kontextwechsel (`cs`) pro Sekunde. Interpretiere Spitzen im Vergleich zu einer Grundlinie; hohe Kontextwechselraten können für manche Arbeitslasten normal sein.

:::single-choice{#vmstat-r-column} Was stellt das Prozessfeld `r` dar?

::option[Schreibgeschützt eingehängte Dateisysteme.]{#vmstat-readonly explanation="Mount-Optionen von Dateisystemen werden durch das Prozessfeld nicht dargestellt."}
::option[Entfernte Benutzer mit aktiven Shells.]{#vmstat-remote-users explanation="Anmeldesitzungen werden von anderen Werkzeugen gemeldet."}
::option[Tasks, die ausführbar sind oder auf CPU warten.]{#vmstat-runnable .correct explanation="Der Vergleich dieser Anzahl mit der CPU-Kapazität kann helfen, CPU-Bedarf zu erkennen."}
:::

## Zusammenfassung

Du kannst `vmstat` nun als zeitlich verknüpfte Systemansicht interpretieren.

1. Trenne den ersten kumulativen Bericht von den Intervallstichproben.
2. Behandle Cache als möglicherweise rückgewinnbaren Speicher.
3. Setze Paging zu Rückgewinnung und Anwendungsauswirkungen in Beziehung.
4. Lies Prozess-, E/A-, System- und CPU-Felder gemeinsam.
