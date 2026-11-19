---
lesson_id: "deployment-health-checks"
course_id: "deployment"
lang: "de"
order_index: 4
title: "Healthchecks"
description: "Lerne, nach einer Bereitstellung den Prozess, einen Dienstendpunkt und den Zugriff eines Clients zu prüfen."
meta_title: "Healthchecks - Bereitstellung"
meta_description: "Lerne, nach einer Bereitstellung den Prozess, einen Dienstendpunkt und den Zugriff eines Clients zu prüfen."
meta_keywords: "Healthchecks, Versionsendpunkt, Bereitstellung, DevOps, Linux Journey"
---

Ein frisch gestartetes Programm kann schon laufen, obwohl es noch keine Anfragen beantworten kann. Prüfe den Dienst in mehreren Schritten. So weißt du bei jedem erfolgreichen Ergebnis, was es genau belegt.

## Den Prozess prüfen

Eine Containerliste kann dir zeigen, dass das Hauptprogramm läuft. Damit ist eine wichtige erste Frage zur neuen Bereitstellung beantwortet. Ob das Programm fertig initialisiert ist oder ein Browser es erreicht, musst du separat prüfen.

:::single-choice{#deployment-health-checks-process-scope} Beim neuen Container steht Up. Was kannst du daraus schließen?

::option[Besucher erhalten auf jeden Fall die neue Seite.]{#deployment-health-checks-process-scope-a explanation="Der Containerstatus sagt nichts über die Anfrage eines Besuchers aus."}
::option[Das Hauptprogramm des Containers läuft zum Zeitpunkt der Prüfung.]{#deployment-health-checks-process-scope-b .correct explanation="Up zeigt den Prozessstatus an."}
::option[Alle Abhängigkeiten wurden erfolgreich geprüft.]{#deployment-health-checks-process-scope-c explanation="Die Anzeige enthält keine Prüfergebnisse für Abhängigkeiten."}
:::

## Einen Dienstendpunkt prüfen

Ein **Endpunkt** ist eine Adresse mit einem Pfad, den der Dienst verarbeitet. Prüfe einen Pfad, der zu dem gewünschten Verhalten passt. Verwende für den lokalen Versuch einen leeren Übungsordner. Die Umleitung speichert die Versionsdatei. Lass den Python-Server in diesem Terminal auf der Loopback-Adresse laufen und beende ihn nach der Übung mit Strg+C.

```bash
$ mkdir site
$ printf '%s\n' 2 > site/version.txt
$ python3 -m http.server 8091 --bind 127.0.0.1 --directory site
```

Rufe die Versionsdatei in einem zweiten Terminal ab. Die Curl-Option `-f` behandelt HTTP-Fehlerantworten als Fehlschlag. `-sS` blendet Fortschrittsanzeigen aus, zeigt aber weiterhin Fehler an.

```bash
$ curl -fsS http://127.0.0.1:8091/version.txt
```

Die erwartete Ausgabe ist `2`. Eine erfolgreiche Anfrage an die Versionsdatei prüft nur einen kleinen Teil der Website.

:::single-choice{#deployment-health-checks-endpoint-mismatch} Die Anfrage klappt und gibt 1 aus. Was solltest du untersuchen?

::option[Welche Version an dieser Adresse antwortet.]{#deployment-health-checks-endpoint-mismatch-a .correct explanation="Die Verbindung hat funktioniert, aber die Antwort nennt eine andere Version als erwartet."}
::option[Warum Curl überhaupt keine Verbindung herstellen kann.]{#deployment-health-checks-endpoint-mismatch-b explanation="Die Antwort zeigt, dass die Verbindung und die Anfrage funktioniert haben."}
::option[Ob der Dienstname eine Ziffer enthält.]{#deployment-health-checks-endpoint-mismatch-c explanation="Aus dem Dienstnamen lässt sich die zurückgegebene Version nicht ableiten."}
:::

![Versionsendpunkt auf der Loopback-Adresse mit der Antwort 2 vom LabEx-Übungsserver](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/deployment/deployment-health-checks/version-response.png)

## Vom Standort des Clients aus prüfen

Wenn eine Anfrage auf dem Dienst-Host funktioniert, wiederhole eine sichere Prüfung von dort aus, wo Nutzer normalerweise zugreifen. Ein Load Balancer, Proxy oder eine Netzwerkregel kann den Verbindungsweg beeinflussen. Halte die Adresse und die Antwort fest. Passt das Ergebnis nicht zum Release, untersuche die Bereitstellung weiter.

:::single-choice{#deployment-health-checks-user-path} Eine lokale Anfrage liefert 2, die öffentliche Testadresse aber 1. Welche Prüfung hilft jetzt am meisten?

::option[Zähle die Zeilen aus der lokalen Anfrage.]{#deployment-health-checks-user-path-a explanation="Die Zeilenzahl zeigt nicht, welcher Dienst die öffentliche Adresse bedient."}
::option[Wiederhole nur dieselbe lokale Prüfung.]{#deployment-health-checks-user-path-b explanation="Der lokale Verbindungsweg hat bereits Version 2 geliefert."}
::option[Prüfe, welche Dienstversion über den öffentlichen Zugriffsweg antwortet.]{#deployment-health-checks-user-path-c .correct explanation="Die beiden Verbindungswege haben unterschiedliche Antworten geliefert."}
:::

## Zusammenfassung

Du kannst jetzt erklären, was die einzelnen Prüfungen nach der Bereitstellung belegen.

1. Prüfe, ob das Hauptprogramm läuft.
2. Frage einen Endpunkt ab, der die erwartete Version meldet.
3. Prüfe den Zugriffsweg der Nutzer separat.
