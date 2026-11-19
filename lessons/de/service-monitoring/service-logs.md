---
lesson_id: "service-logs"
course_id: "service-monitoring"
lang: "de"
order_index: 2
title: "Dienstprotokolle"
description: "Lerne, eine Anfrage anhand ihrer ID und Uhrzeit über mehrere Dienstprotokolle zu verfolgen."
meta_title: "Dienstprotokolle - Dienstüberwachung"
meta_description: "Lerne, eine Anfrage anhand ihrer ID und Uhrzeit über mehrere Dienstprotokolle zu verfolgen."
meta_keywords: "Dienstprotokolle, Anfrage-ID, Dienstüberwachung, DevOps, Linux Journey"
---

Ein Nutzer sieht eine Fehlermeldung. Im Dienstprotokoll kannst du nachsehen, bei welchem Schritt die Anfrage scheiterte. Suche zuerst nach der Uhrzeit und dann nach einer **Anfrage-ID**. Diese Kennung verbindet Einträge zur selben Anfrage.

## Einträge zu einer Anfrage lesen

Das folgende Beispiel zeigt zwei Dienste. Eine **Abhängigkeit** ist ein Dienst, den ein anderes Programm für seine Arbeit benötigt. Hier fragt der Webdienst bei einem Katalogdienst eine Artikelliste ab.

```text
09:14:02 service=web     request=r17 path=/items status=502
09:14:02 service=catalog request=r17 action=read result=timeout
09:14:03 service=catalog request=r18 action=read result=ok
```

Die Zeile des Webdienstes zeigt einen Fehler für `r17`. Die Zeile mit derselben ID beim Katalogdienst meldet eine Zeitüberschreitung. Die fast zeitgleiche erfolgreiche Kataloganfrage gehört zu `r18`.

:::single-choice{#service-logs-matching-request} Welches Ergebnis des Katalogdienstes gehört zum Fehler des Webdienstes bei r17?

::option[Das erfolgreiche Ergebnis für r18.]{#service-logs-matching-request-a explanation="Die Zeile gehört zu einer anderen Anfrage."}
::option[Beide Ergebnisse des Katalogdienstes.]{#service-logs-matching-request-c explanation="Nahe Zeitstempel können zu verschiedenen Anfragen gehören."}
::option[Die Zeitüberschreitung bei r17.]{#service-logs-matching-request-b .correct explanation="Die gemeinsame ID verbindet die beiden Einträge zu dieser Anfrage."}
:::

## Das Beispiel filtern

Speichere die drei Zeilen oben als `requests.log` in einem Übungsverzeichnis. Verwende `grep -F`, um nach einer festen Zeichenfolge zu suchen. Lass das Leerzeichen nach der Kennung stehen, um im Beispiel das Ende des Felds zu erfassen.

```bash
$ grep -F 'request=r17 ' requests.log
```

Du solltest die Zeilen des Web- und Katalogdienstes zu `r17` sehen. Echte Protokolle können ein anderes Format haben oder die Anfrage-ID weglassen. Prüfe, ob die gesuchten Felder in allen Diensten dasselbe bedeuten.

:::single-choice{#service-logs-choose-filter} Warum suchst du nach dem ganzen Anfragefeld und nicht nur nach dem Wort timeout?

::option[So stellst du sicher, dass im gesamten Verkehr derselbe Fehler auftrat.]{#service-logs-choose-filter-b explanation="Der Filter sucht Einträge zu einer einzigen Anfrage."}
::option[So erhältst du beide passenden Einträge, auch wenn nur einer timeout enthält.]{#service-logs-choose-filter-a .correct explanation="Mit der gemeinsamen ID verfolgst du die Anfrage durch beide Dienste."}
::option[So änderst du das Protokoll, damit spätere Suchen das richtige Ergebnis finden.]{#service-logs-choose-filter-c explanation="Grep liest die Datei und gibt passende Zeilen aus."}
:::

![Grep-Ausgabe, die den Webfehler und die Zeitüberschreitung des Katalogdienstes für Anfrage r17 verbindet](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/service-monitoring/service-logs/request-id.png)

## Den Befund eingrenzen

Die Zeitüberschreitung zeigt, an welcher Stelle die Anfrage scheiterte. Welche Komponente im Katalogdienst zu langsam war, bleibt offen. Prüfe als Nächstes die Messwerte oder aktuellen Protokolle der Abhängigkeit. Wenn du einem Teammitglied einen Auszug gibst, lass die Anfrage-ID stehen und entferne unnötige Geheimnisse oder personenbezogene Daten.

:::single-choice{#service-logs-evidence-limit} Was gehört in eine erste Meldung?

::option[Bei r17 hat der Katalogdienst nicht rechtzeitig geantwortet. Das sollte genauer geprüft werden.]{#service-logs-evidence-limit-c .correct explanation="Das fasst die zusammengehörigen Einträge zusammen, ohne über die Ursache zu spekulieren."}
::option[Alle Kataloganfragen haben zu lange gedauert.]{#service-logs-evidence-limit-a explanation="Das Beispiel enthält eine andere Kataloganfrage, die erfolgreich war."}
::option[Ein bestimmter Datenträger der Datenbank ist ausgefallen.]{#service-logs-evidence-limit-b explanation="In den Einträgen gibt es keinen Hinweis auf einen Datenträger."}
:::

Mit [Protokolle für die Vorfallreaktion analysieren](https://labex.io/labs/linux-monitoring-and-incident-response-log-analysis-594586) kannst du üben, Dienstprotokolle auf einem Linux-Host abzufragen.

## Zusammenfassung

Du kannst eine Anfrage jetzt über mehrere Dienstprotokolle verfolgen.

1. Ordne die relevanten Einträge anhand der Anfrage-ID einander zu.
2. Grenze die Stichprobe mit einer festen Suchzeichenfolge ein.
3. Melde, was die Einträge belegen, und leite daraus die nächste Prüfung ab.
