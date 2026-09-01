---
lesson_id: "cpu-monitoring"
course_id: "process-utilization"
lang: "de"
order_index: 4
title: "CPU-Überwachung"
description: "Lerne, Linux-Lastmittelwerte zusammen mit CPU-Anzahl, Auslastung und Taskzustand zu interpretieren."
meta_title: "CPU-Überwachung – Prozessauslastung"
meta_description: "Lerne die Grundlagen der Linux-CPU-Überwachung mit dem Befehl uptime. Diese Einführung erklärt, wie du Lastmittelwerte interpretierst, Prozessauslastung verstehst und die Systemleistung beurteilst."
meta_keywords: "uptime-Befehl, Linux-CPU-Überwachung, Lastmittelwert, Systemleistung, Prozessauslastung, Linux-Tutorial, Einführung"
---

Die CPU-Fehlersuche beginnt damit, Last, Auslastung und Reaktionsfähigkeit voneinander zu trennen. Kein einzelner Wert belegt einen Engpass. Vergleiche deshalb mehrere Zeitfenster und setze Hostmesswerte zu der Arbeitslast in Beziehung, die Benutzer tatsächlich erleben.

## uptime lesen

`uptime` bietet einen kompakten Ausgangspunkt:

```text
$ uptime
 17:23:35 up 1 day, 5:59, 2 users, load average: 0.00, 0.02, 0.05
```

Die letzten drei Werte sind Lastmittelwerte über ungefähr 1, 5 und 15 Minuten. Ihr Vergleich zeigt die Richtung: Ein deutlich größerer 1-Minuten-Wert kann auf steigende Last hindeuten, während ein größerer 15-Minuten-Wert auf fallende Last hinweisen kann.

:::single-choice{#cpu-uptime-windows} In welcher Reihenfolge zeigt `uptime` die Zeitfenster der Lastmittelwerte an?

::option[15, 5 und 1 Sekunde.]{#cpu-windows-seconds explanation="Die Werte sind Mittelwerte über Minuten und werden nicht mit dem längsten zuerst ausgegeben."}
::option[1, 5 und 15 Minuten.]{#cpu-windows-one-five-fifteen .correct explanation="Das kürzeste vergangene Zeitfenster steht zuerst und das längste zuletzt."}
::option[Aktueller, minimaler und maximaler CPU-Prozentwert.]{#cpu-windows-percentages explanation="Der Lastmittelwert ist kein minimaler oder maximaler CPU-Prozentwert."}
:::

## Linux-Last verstehen

Der Linux-Lastmittelwert zählt ausführbare Tasks, einschließlich derjenigen, die CPU verwenden oder darauf warten, sowie Tasks in nicht unterbrechbarem Schlaf, der häufig mit E/A zusammenhängt. Er ist deshalb nicht mit der CPU-Auslastung identisch.

Eine Last von `4.0` hat auf Systemen mit einer beziehungsweise sechzehn logischen CPUs unterschiedliche Bedeutung. Ermittle die Anzahl der dem System verfügbaren Verarbeitungseinheiten mit:

```bash
$ nproc
```

CPU-Kontingente, Affinität, Virtualisierung und Containergrenzen können die für eine bestimmte Arbeitslast sichtbare Kapazität verringern. Die CPU-Anzahl des Hosts ist daher nur ein Ausgangspunkt.

:::single-choice{#cpu-load-not-percentage} Warum ist der Lastmittelwert kein CPU-Auslastungsprozentwert?

::option[Er meldet nur die CPU-Taktfrequenz.]{#cpu-load-clock explanation="Die Taktfrequenz ist ein getrennter Hardware- oder Skalierungsmesswert."}
::option[Er misst nur freien physischen Arbeitsspeicher.]{#cpu-load-memory explanation="Die Speicherverfügbarkeit wird durch andere Messwerte gemeldet."}
::option[Er umfasst ausführbare Tasks und Tasks in nicht unterbrechbarem Schlaf.]{#cpu-load-task-count .correct explanation="Last basiert auf Taskbedarf und Wartezustand statt auf einem Prozentanteil verstrichener CPU-Zeit."}
:::

## Last mit CPU-Aktivität vergleichen

Erfasse mehrere Stichproben, statt dich auf eine einzelne Ausgabe zu verlassen. Nützliche ergänzende Werkzeuge sind:

```bash
$ top
$ vmstat 1
$ mpstat -P ALL 1
```

`top` verbindet Host- und Prozessansichten. `vmstat` zeigt die Anzahl ausführbarer und blockierter Tasks zusammen mit CPU-Kategorien. `mpstat`, das auf vielen Distributionen von `sysstat` bereitgestellt wird, zeigt die Aktivität einzelner CPUs. Verfügbarkeit und genaue Felder unterscheiden sich; verwende daher die lokalen Handbuchseiten.

Hohe Last bei ausgelasteten CPUs kann auf CPU-Bedarf hindeuten. Hohe Last zusammen mit auffällig vielen blockierten Tasks, E/A-Latenz oder beobachteter E/A-Wartezeit weist auf eine andere eingeschränkte Ressource hin. Eine niedrige durchschnittliche Auslastung kann außerdem eine gesättigte einzelne CPU oder eine kurze Latenzspitze verbergen.

:::single-choice{#cpu-high-load-next-step} Was ist der beste nächste Schritt, nachdem du einen hohen Lastmittelwert beobachtet hast?

::option[Wiederholte CPU-, Taskzustands-, E/A- und Arbeitslastmessungen vergleichen.]{#cpu-load-correlate .correct explanation="Miteinander verknüpfte Stichproben unterscheiden konkurrierende Erklärungen für die Last."}
::option[Sofort neu starten, ohne weitere Daten zu erfassen.]{#cpu-load-reboot explanation="Ein Neustart beseitigt Belege und kann Dienste unterbrechen, ohne die Ursache zu ermitteln."}
::option[Annehmen, dass jede CPU vollständig ausgelastet ist.]{#cpu-load-assume explanation="Last kann nicht unterbrechbare Tasks umfassen und ungleichmäßig auf CPUs verteilt sein."}
:::

## Kapazität und Auswirkungen bewerten

Es gibt keine allgemeingültige Regel, nach der die Last immer unter der CPU-Anzahl bleiben muss. Stapelverarbeitungssysteme können Warteschlangen akzeptieren, während interaktive Dienste schon vorher ihre Latenzziele verfehlen können. Erstelle eine Grundlinie für denselben Host und dieselbe Arbeitslast und vergleiche anschließend Antwortzeit, Durchsatz, Fehlerrate, Sättigung und Ressourcennutzung.

:::single-choice{#cpu-capacity-threshold} Woran solltest du entscheiden, ob die beobachtete Last akzeptabel ist?

::option[An der Vorgabe, dass der Wert immer unter eins bleiben muss.]{#cpu-below-one explanation="Mehrkernkapazität und Arbeitslastziele machen diesen festen Schwellenwert unzuverlässig."}
::option[Allein an der von `uptime` angezeigten Benutzeranzahl.]{#cpu-user-count explanation="Angemeldete Shellbenutzer stellen nicht den gesamten Arbeitslastbedarf dar."}
::option[An der Grundlinie und den Dienstzielen der Arbeitslast.]{#cpu-baseline-objectives .correct explanation="Die Akzeptanz hängt vom erwarteten Verhalten und der für Benutzer sichtbaren Leistung ab, nicht von einem allgemeingültigen Schwellenwert."}
:::

## Zusammenfassung

Du kannst den Lastmittelwert nun als einen Bestandteil einer CPU-Untersuchung interpretieren.

1. Lies die Lastzeitfenster über 1, 5 und 15 Minuten.
2. Unterscheide Tasklast von CPU-Zeitprozenten.
3. Vergleiche die Last mit der verfügbaren Verarbeitungskapazität.
4. Verknüpfe wiederholte Hostmessungen mit Dienstergebnissen.
