---
lesson_id: "network-traffic-baselines"
course_id: "network-monitoring"
lang: "de"
order_index: 5
title: "Vergleichswerte für den Netzwerkverkehr"
description: "Lerne, vergleichbare Zeitfenster zu prüfen, bevor du eine Veränderung des Verkehrs als auffällig einstufst."
meta_title: "Vergleichswerte für den Netzwerkverkehr - Netzwerküberwachung"
meta_description: "Lerne, vergleichbare Zeitfenster zu prüfen, bevor du eine Veränderung des Verkehrs als auffällig einstufst."
meta_keywords: "Vergleichswerte, Netzwerkverkehr, Netzwerküberwachung, Cybersicherheit, Linux Journey"
---

Ein **Vergleichswert** beschreibt das Verhalten, das du normalerweise unter bestimmten Bedingungen beobachtest. Bei der Verkehrsüberwachung kann das eine typische Anzahl oder ein üblicher Bereich für denselben Dienst zur selben Tageszeit sein.

## Vergleichbare Zeitfenster wählen

Eine öffentliche Seite kann während der Arbeitszeit mehr Verkehr erhalten. Vergleiche Zeitfenster mit ähnlichen Abläufen, wenn du Veränderungen erkennen willst. In diesem Beispiel werden Anfragen an einen Dienst in Fünf-Minuten-Fenstern gezählt.

```text
Window                 Requests
Typical weekdays 09:00  90–120
Today 09:00                230
Typical nights 02:00       2–8
```

Die 230 Anfragen liegen außerhalb des üblichen Bereichs an Werktagen am Morgen. Die Werte aus der Nacht eignen sich weniger gut als Vergleich.

:::single-choice{#network-traffic-baselines-baseline-fit} Welche Zeile liefert einen passenden Vergleich für heute um 09:00 Uhr?

::option[Typische Nächte um 02:00 Uhr.]{#network-traffic-baselines-baseline-fit-b explanation="Das beschreibt ein anderes Verkehrsmuster."}
::option[Die heute beobachteten 230 Anfragen für sich genommen.]{#network-traffic-baselines-baseline-fit-c explanation="Eine einzelne aktuelle Zahl braucht einen Vergleich, um eine Veränderung zu zeigen."}
::option[Typische Werktage um 09:00 Uhr.]{#network-traffic-baselines-baseline-fit-a .correct explanation="Tageszeit und betrachteter Dienst stimmen überein."}
:::

## Nach einer Erklärung suchen

Eine Ankündigung auf der Website oder ein geplanter Auftrag kann eine Veränderung erklären. Sieh dir die angefragten Pfade, die Zeitpunkte und die genehmigten Änderungen an, bevor du über weitere Untersuchungen entscheidest. Der Vergleichswert macht die Abweichung sichtbar und gibt dir einen Ansatzpunkt für die Suche.

:::single-choice{#network-traffic-baselines-baseline-explain} Nach einem angekündigten Start hat sich der Verkehr verdoppelt. Was solltest du prüfen?

::option[Werte den Unterschied als Beweis, dass ein Konto kompromittiert wurde.]{#network-traffic-baselines-baseline-explain-a explanation="Die Zahl allein zeigt weder eine Ursache noch ein Ereignis am Konto."}
::option[Vergleiche Zeitpunkte und Pfade mit dem Verkehr, den du durch den Start erwartet hast.]{#network-traffic-baselines-baseline-explain-b .correct explanation="So prüfst du eine plausible Erklärung anhand passender Beobachtungen."}
::option[Ignoriere die Veränderung, weil ein Start immer jede Lastspitze erklärt.]{#network-traffic-baselines-baseline-explain-c explanation="Eine erwartete Veränderung kann zur gleichen Zeit wie andere Aktivitäten auftreten."}
:::

## Die Messung prüfen

Eine Änderung am Erfassungssystem kann den Messwert beeinflussen, auch wenn sich der Verkehr nicht geändert hat. Erfasst das System seit gestern ein zusätzliches Netz, prüfe, welchen Verkehr jedes Zeitfenster enthält. Halte für den Vergleich Dienst, Beobachtungspunkt, Zeit und Einheit fest.

:::single-choice{#network-traffic-baselines-changed-coverage} Die Erfassung umfasst seit Kurzem einen zweiten Standort. Was macht den nächsten Vergleich aussagekräftiger?

::option[Vergleiche Zählwerte für denselben Standort mit denselben erfassten Quellen.]{#network-traffic-baselines-changed-coverage-c .correct explanation="Ein einheitlicher Umfang hilft, eine Verkehrsänderung von einer Änderung der Erfassung zu unterscheiden."}
::option[Vergleiche die beiden Gesamtzahlen, ohne ihren Umfang zu prüfen.]{#network-traffic-baselines-changed-coverage-a explanation="Durch die geänderte Erfassung sind die Gesamtzahlen schlechter vergleichbar."}
::option[Vergleiche die neue Gesamtzahl mit der gestrigen, nachdem du das Zeitfenster verlängert hast.]{#network-traffic-baselines-changed-coverage-b explanation="Auch ein längeres Zeitfenster ändert nichts daran, dass die Zahlen unterschiedliche Standorte oder Quellen umfassen können."}
:::

## Zusammenfassung

Du kannst jetzt entscheiden, ob ein Vergleichswert für eine Netzwerkbeobachtung geeignet ist.

1. Gleiche Dienst, Zeit und Einheit ab.
2. Prüfe, ob erwartete Änderungen eine Abweichung erklären.
3. Prüfe, ob sich der Umfang der Erfassung geändert hat.
