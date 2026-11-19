---
lesson_id: "compose-service-dependencies"
course_id: "docker-compose"
lang: "de"
order_index: 6
title: "Dienstabhängigkeiten"
description: "Lerne, warum die richtige Startreihenfolge allein noch nicht zeigt, ob ein Dienst Anfragen beantworten kann."
meta_title: "Dienstabhängigkeiten - Docker Compose"
meta_description: "Lerne, warum die richtige Startreihenfolge allein noch nicht zeigt, ob ein Dienst Anfragen beantworten kann."
meta_keywords: "Dienstabhängigkeiten, Healthcheck, Startreihenfolge, Docker Compose, DevOps, Linux Journey"
---

Ein Hilfsprogramm, das einen Webserver benötigt, kann seine erste Anfrage zu früh senden, obwohl beide in der richtigen Reihenfolge gestartet wurden. Ein **Healthcheck** ist ein kleiner Test, den Docker ausführt. Er zeigt zum Beispiel, ob ein Dienst eine HTTP-Anfrage beantworten kann.

## Die Betriebsbereitschaft prüfen

In diesem separaten Beispiel läuft die Prüfung im Webcontainer. Sie ruft dort die lokale Webseite ab. Eine erfolgreiche Anfrage zeigt Docker, dass der Server von dieser Stelle aus erreichbar ist und antwortet.

```yaml
services:
  web:
    image: nginx:alpine
    healthcheck:
      test: ["CMD", "wget", "-q", "-O", "/dev/null", "http://127.0.0.1/"]
      interval: 3s
      timeout: 2s
      retries: 5
  toolbox:
    image: busybox:1.36
    command: ["sleep", "3600"]
    depends_on:
      web:
        condition: service_healthy
```

Speichere das Beispiel als `compose.health.yaml` im selben Übungsordner. Die Prüfung läuft in regelmäßigen Abständen und hat für jeden Versuch ein Zeitlimit. Sie prüft die Antwort innerhalb des Webcontainers.

:::single-choice{#compose-service-dependencies-check-location} Wo läuft wget für diesen Healthcheck?

::option[Im Webcontainer.]{#compose-service-dependencies-check-location-c .correct explanation="Die Loopback-Adresse wird aus dem Webcontainer aufgerufen."}
::option[Im Browser des Hosts.]{#compose-service-dependencies-check-location-a explanation="Docker führt den Befehl anhand der Definition des Webdienstes aus."}
::option[Im Werkzeugcontainer.]{#compose-service-dependencies-check-location-b explanation="Die Prüfung ist unter web definiert."}
:::

## Auf einen einsatzbereiten Dienst warten

Mit der Bedingung `service_healthy` wartet Compose auf einen erfolgreichen Healthcheck, bevor es den abhängigen Werkzeugcontainer startet. Eine reine Startreihenfolge lässt den Werkzeugcontainer anlaufen, sobald der Webdienst läuft. Das kann schon vor der ersten erfolgreichen Anfrage geschehen.

```bash
$ docker compose -p journey-health -f compose.health.yaml up -d
$ docker compose -p journey-health -f compose.health.yaml ps
```

Prüfe, ob in der Zeile von web ein gesunder Zustand angezeigt wird und der Werkzeugcontainer läuft.

:::single-choice{#compose-service-dependencies-ready-condition} Der Webprozess läuft, aber die lokale Anfrage schlägt noch fehl. Welche Einstellung soll den Start des Werkzeugcontainers verzögern?

::option[Nur die Startreihenfolge.]{#compose-service-dependencies-ready-condition-b explanation="Auch wenn web zuerst startet, kann es eine Weile dauern, bis der Dienst antwortet."}
::option[Der Hintergrundmodus.]{#compose-service-dependencies-ready-condition-c explanation="Der Hintergrundmodus bestimmt, ob das Terminal auf die Dienste wartet. Die Betriebsbereitschaft legst du damit nicht fest."}
::option[Die Bedingung service_healthy.]{#compose-service-dependencies-ready-condition-a .correct explanation="Mit dieser Abhängigkeit wartet Compose auf das Prüfergebnis."}
:::

![Compose-Status mit gesundem Webdienst und laufendem Werkzeugcontainer](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/docker-compose/compose-service-dependencies/healthy-dependency.png)

## Auf einen späteren Ausfall reagieren

Eine Startbedingung in Compose bestimmt, wann abhängige Dienste anlaufen. Ein zuvor gesunder Dienst kann nach dem Start trotzdem ausfallen. Ein Client sollte mit fehlgeschlagenen Anfragen umgehen und die Verbindung neu aufbauen, sobald der benötigte Dienst wieder erreichbar ist. Prüfe den aktuellen Zustand des Dienstes und sende eine direkte Anfrage.

:::single-choice{#compose-service-dependencies-later-failure} Eine Anfrage schlägt eine Stunde nach dem Start beider Dienste fehl. Was hilft dir jetzt weiter?

::option[Nur die ursprüngliche Startreihenfolge.]{#compose-service-dependencies-later-failure-a explanation="Sie beschreibt den Ablauf beim Start."}
::option[Ein aktuelles Prüfergebnis und eine Anfrage aus dem abhängigen Dienst.]{#compose-service-dependencies-later-failure-b .correct explanation="Damit prüfst du sowohl den aktuellen Zustand des Dienstes als auch den Verbindungsweg des Clients."}
::option[Die Anzahl der Images im Docker-Cache.]{#compose-service-dependencies-later-failure-c explanation="Die vorhandenen Images sagen wenig darüber aus, wie ein laufender Dienst antwortet."}
:::

## Aus zwei Blickwinkeln prüfen

Ein erfolgreicher lokaler Healthcheck zeigt, was aus dem Webcontainer selbst erreichbar ist. Der Werkzeugcontainer benötigt weiterhin das Projektnetzwerk und eine nutzbare Dienstadresse. Prüfe das Ergebnis des Healthchecks und die Anfrage aus dem Werkzeugcontainer getrennt.

:::single-choice{#compose-service-dependencies-final-application} Der Healthcheck ist grün, aber die Anfrage aus dem Werkzeugcontainer schlägt fehl. Welcher Vergleich hilft bei der Fehlersuche?

::option[Lies nur die ursprüngliche Startzeit ab.]{#compose-service-dependencies-final-application-b explanation="Die Startzeit sagt nichts darüber aus, welcher Verbindungsweg gerade funktioniert."}
::option[Werte beide Anfragen als erfolgreich, weil der Healthcheck grün ist.]{#compose-service-dependencies-final-application-c explanation="Der Healthcheck liefert nur einen Befund aus einem bestimmten Container."}
::option[Vergleiche dieselbe Anfrage aus web mit einer Anfrage an web aus dem Werkzeugcontainer.]{#compose-service-dependencies-final-application-a .correct explanation="So prüfst du die Betriebsbereitschaft im Webcontainer und den Verbindungsweg des abhängigen Dienstes."}
:::

## Zusammenfassung

Du kannst jetzt anhand eines Healthchecks beurteilen, ob eine Abhängigkeit einsatzbereit ist.

1. Ermittle, was der Healthcheck tatsächlich prüft.
2. Verwende eine Bedingung für die Betriebsbereitschaft, wenn die Startreihenfolge allein nicht ausreicht.
3. Prüfe den aktuellen Zustand, wenn ein Dienst später ausfällt.
