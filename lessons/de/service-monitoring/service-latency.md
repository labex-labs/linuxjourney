---
lesson_id: "service-latency"
course_id: "service-monitoring"
lang: "de"
order_index: 4
title: "Latenz"
description: "Lerne, typische Anfragezeiten mit den langsamsten beobachteten Anfragen zu vergleichen."
meta_title: "Latenz - Dienstüberwachung"
meta_description: "Lerne, typische Anfragezeiten mit den langsamsten beobachteten Anfragen zu vergleichen."
meta_keywords: "Latenz, Dienstüberwachung, DevOps, Linux Journey"
---

Die **Latenz** gibt an, wie lange eine Anfrage dauert. Ein einzelner Messwert kann verdecken, wie unterschiedlich lange Nutzer warten. Vergleiche typische mit langsameren Anfragen für denselben Pfad und dasselbe Zeitfenster.

## Eine kleine Stichprobe lesen

Die folgenden fünf Zeiten sind in Millisekunden angegeben. Vier Anfragen waren nach weniger als 100 Millisekunden abgeschlossen. Eine dauerte zwei Sekunden.

```text
40  50  60  70  2000
```

Der **Median**, auch 50. Perzentil genannt, ist der mittlere Wert der sortierten Stichprobe. Hier beträgt er 60 Millisekunden. Der höchste beobachtete Wert beträgt 2.000 Millisekunden. Der Mittelwert ergibt sich aus der Summe geteilt durch fünf und beträgt 444 Millisekunden.

:::single-choice{#service-latency-sample-median} Welcher Wert gehört zur mittleren Anfrage in dieser sortierten Stichprobe?

::option[444 Millisekunden.]{#service-latency-sample-median-a explanation="Das ist der Mittelwert, in den auch die langsame Anfrage eingeht."}
::option[60 Millisekunden.]{#service-latency-sample-median-b .correct explanation="Der dritte der fünf sortierten Werte ist der Median."}
::option[2.000 Millisekunden.]{#service-latency-sample-median-c explanation="Das ist der höchste beobachtete Wert."}
:::

## Die langsamen Anfragen betrachten

Ein **Perzentil** gibt an, bei welchem Wert ein bestimmter Anteil der Beobachtungen erreicht ist. Das 95. Perzentil der Latenz, oft p95 genannt, bezeichnet eine Schwelle am langsamen Ende einer größeren Stichprobe. Verwende für Vergleiche dieselbe Berechnung wie im Dashboard. Bei sehr kleinen Stichproben schwanken Schätzungen für die langsamen Anfragen stark.

:::single-choice{#service-latency-slow-end} Der Median ändert sich kaum, aber Besucher melden immer wieder Verzögerungen. Welche Ansicht hilft weiter?

::option[Die hohen Latenzwerte zusammen mit der Anfragezahl.]{#service-latency-slow-end-a .correct explanation="Langsame Antworten können sich verändern, während der Median ähnlich bleibt."}
::option[Noch einmal nur der Median.]{#service-latency-slow-end-b explanation="So können Änderungen unbemerkt bleiben, die nur wenige Besuche betreffen."}
::option[Die Gesamtgröße der Protokolldatei.]{#service-latency-slow-end-c explanation="Die Dateigröße zeigt nicht, wie lange Anfragen dauerten."}
:::

## Ähnliche Anfragen vergleichen

Vergleiche denselben Pfad bei ähnlichem Verkehr. Ein Download darf länger dauern als eine kleine Statusabfrage. Fällt ein Pfad durch hohe Latenz auf, prüfe seine Anfrageprotokolle und Abhängigkeiten im selben Zeitfenster. Die Messwerte helfen dir, das Problem einzugrenzen. Mit weiteren Belegen gehst du der Ursache nach.

:::single-choice{#service-latency-compare-route} Welcher Vergleich eignet sich am besten, um zu prüfen, ob dieselbe Startseite nach einem Release langsamer wurde?

::option[Heutige Antworten der Startseite mit Downloads vom letzten Monat vergleichen.]{#service-latency-compare-route-a explanation="Unterschiedliche Vorgänge und Zeiträume erschweren die Auswertung."}
::option[Je eine einzelne Anfrage pro Release ohne zeitlichen Zusammenhang vergleichen.]{#service-latency-compare-route-b explanation="Eine einzelne Messung erfasst keine Schwankungen."}
::option[Die Latenz der Startseite in vergleichbaren Zeitfenstern vor und nach dem Release vergleichen.]{#service-latency-compare-route-c .correct explanation="Bei gleichem Pfad und ähnlicher Last lässt sich die Änderung leichter einordnen."}
:::

## Zusammenfassung

Du kannst jetzt typische und langsame Anfragezeiten gemeinsam auswerten.

1. Bestimme den Median einer kleinen sortierten Stichprobe.
2. Betrachte langsame Anfragen zusammen mit der Anfragezahl.
3. Vergleiche ähnliche Anfragen, bevor du Unterschiede untersuchst.
