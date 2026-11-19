---
lesson_id: "service-availability-errors"
course_id: "service-monitoring"
lang: "de"
order_index: 3
title: "Verfügbarkeit und Fehler"
description: "Lerne, Anfragefehler anhand eines Zeitfensters und der Gesamtzahl der Anfragen zu vergleichen."
meta_title: "Verfügbarkeit und Fehler - Dienstüberwachung"
meta_description: "Lerne, Anfragefehler anhand eines Zeitfensters und der Gesamtzahl der Anfragen zu vergleichen."
meta_keywords: "Verfügbarkeit, Fehlerrate, Dienstüberwachung, DevOps, Linux Journey"
---

Ein Dienst kann die meisten Besucher bedienen, während einzelne Anfragen fehlschlagen. Ermittle den Anteil fehlgeschlagener Anfragen aus der Gesamtzahl und der Fehlerzahl desselben Zeitfensters.

## Die Fehlerrate berechnen

Für die **Fehlerrate** teilst du die Zahl fehlgeschlagener Anfragen durch die Zahl aller beobachteten Anfragen. Multipliziere das Ergebnis mit 100, um es in Prozent anzugeben.

```text
Window          Requests   Failures
09:00–09:05          100          2
09:05–09:10           20          2
```

Im ersten Zeitfenster schlagen zwei von hundert Anfragen fehl, also 2 Prozent. Im nächsten Zeitfenster sind es ebenfalls zwei Fehler, diesmal bei zwanzig Anfragen, also 10 Prozent.

:::single-choice{#service-availability-errors-compare-windows} In welchem Zeitfenster war der Anteil fehlgeschlagener Anfragen größer?

::option[Von 09:05 bis 09:10 Uhr.]{#service-availability-errors-compare-windows-b .correct explanation="Zwei Fehler bei zwanzig Anfragen machen einen größeren Anteil aus als zwei bei hundert."}
::option[In beiden war er gleich, weil jeweils zwei Fehler auftraten.]{#service-availability-errors-compare-windows-a explanation="Die Gesamtzahl der Anfragen ist unterschiedlich."}
::option[Von 09:00 bis 09:05 Uhr, weil dort mehr Anfragen eingingen.]{#service-availability-errors-compare-windows-c explanation="Bei einer höheren Gesamtzahl ergibt dieselbe Fehlerzahl einen kleineren Anteil."}
:::

## Vergleichbare Anfragen auswählen

Achte auf das Zeitfenster, den angefragten Pfad und darauf, was als Fehler zählt. Ein Endpunkt für Healthchecks kann erfolgreich antworten, während eine Seite wegen eines abhängigen Dienstes ausfällt. Möchtest du wissen, was die Nutzer der Seite erleben, zähle die Anfragen an diese Seite.

:::single-choice{#service-availability-errors-route-scope} Der Healthcheck ist immer erfolgreich, aber Kunden melden Fehler beim Bezahlen. Was solltest du untersuchen?

::option[Nur die Antworten des Endpunkts für Healthchecks.]{#service-availability-errors-route-scope-b explanation="Diese Antworten betreffen einen anderen Vorgang."}
::option[Den Namen des Dienstkontos.]{#service-availability-errors-route-scope-c explanation="Der Name sagt nichts über die Zahl der betroffenen Anfragen aus."}
::option[Die Anfragen an die Bezahlseite und die dabei aufgetretenen Fehler.]{#service-availability-errors-route-scope-a .correct explanation="Die gemeldeten Fehler betreffen genau diesen Pfad."}
:::

## Wenig Verkehr einordnen

Wenn von zwei Anfragen eine fehlschlägt, liegt die beobachtete Fehlerrate bei 50 Prozent. Das beschreibt diese Stichprobe. Wenige Anfragen können zu starken Schwankungen führen. Gib deshalb zum Prozentwert auch die Anzahl an. Ohne Anfragen ist die Fehlerrate für echten Besucherverkehr nicht definiert. Ein eigener geplanter Test kann trotzdem zeigen, ob eine Anfrage erfolgreich war.

:::single-choice{#service-availability-errors-zero-traffic} In einem Zeitfenster gab es keine Besucheranfragen. Was solltest du zur Fehlerrate der Besucher melden?

::option[Das belegt eine einwandfreie Verfügbarkeit.]{#service-availability-errors-zero-traffic-a explanation="Es gab keine beobachtete Besucheranfrage, die das belegen könnte."}
::option[Für dieses Zeitfenster fehlen Anfragedaten zur Berechnung der Fehlerrate.]{#service-availability-errors-zero-traffic-c .correct explanation="Mit einem eigenen Test kannst du bei Bedarf prüfen, ob der Dienst antwortet."}
::option[Sie liegt eindeutig bei 100 Prozent.]{#service-availability-errors-zero-traffic-b explanation="Die Anzahl beobachteter Anfragen im Nenner beträgt null."}
:::

## Zusammenfassung

Du kannst eine Fehlerrate jetzt mit den dazugehörigen Angaben erklären.

1. Setze die Fehler ins Verhältnis zu allen Anfragen desselben Zeitfensters.
2. Wähle den Pfad und die Fehlerdefinition passend zur Fragestellung.
3. Gib bei geringem Verkehr auch die absoluten Zahlen an.
