---
lesson_id: "compose-services"
course_id: "docker-compose"
lang: "de"
order_index: 2
title: "Compose-Dienste"
description: "Lerne, wie du Compose-Dienste startest und den Zustand ihrer Container prüfst."
meta_title: "Compose-Dienste - Docker Compose"
meta_description: "Lerne, wie du Compose-Dienste startest und den Zustand ihrer Container prüfst."
meta_keywords: "Compose-Dienste, Containerstatus, Docker Compose, DevOps, Linux Journey"
---

Verwende die Datei `compose.yaml` mit `web` und `toolbox` aus der vorigen Lektion. Beide Dienste gehören zu einem Compose-**Projekt**. Das ist die Gruppe der Ressourcen, die Compose anhand dieser Konfiguration gemeinsam verwaltet. Führe die Befehle im Übungsordner aus.

## Das Projekt starten

Wenn Port 8080 bereits belegt ist, wähle in `compose.yaml` einen freien Host-Port. Der Container `published-web` aus dem Docker-Kurs belegt zum Beispiel Port 8080, solange er läuft. Du kannst ihn weiterlaufen lassen und in Compose die Zuordnung `127.0.0.1:8081:80` eintragen, sofern Port 8081 frei ist. Behalte auf der Containerseite Port 80 bei und verwende bei späteren Browseranfragen den ausgewählten Host-Port.

Starte die Dienste mit `docker compose up -d` im Hintergrund. Compose legt die benötigten Projektressourcen an und verwendet die Diensteinstellungen, um die Container zu erstellen oder zu aktualisieren.

```bash
$ docker compose up -d
```

:::single-choice{#compose-services-project-start} Du führst up -d im Übungsordner aus. Welche Einstellungen bestimmen, was startet?

::option[Alle Images, die auf dem Docker-Host verfügbar sind.]{#compose-services-project-start-a explanation="Auf dem Host können Images gespeichert sein, die mit diesem Projekt nichts zu tun haben."}
::option[Alle Container, die gerade gestoppt sind.]{#compose-services-project-start-c explanation="Compose bearbeitet das Projekt, das gestartet werden soll."}
::option[Die Dienste in der ausgewählten Compose-Datei.]{#compose-services-project-start-b .correct explanation="Compose verwendet hier die Definitionen von web und toolbox."}
:::

## Die Dienstliste lesen

Prüfe dieses Projekt mit `docker compose ps`. Die Dienstspalte zeigt die Namen aus der YAML-Datei. Docker gibt außerdem jedem Container einen eigenen Namen, der den Projektnamen enthalten kann.

```bash
$ docker compose ps
```

Suche nach `web` und `toolbox` und prüfe ihren Status. Ein laufender Container zeigt, dass das Programm zum Zeitpunkt der Prüfung läuft. Ob der Webserver die erwartete Antwort liefert, prüfst du mit einer eigenen Browseranfrage.

:::single-choice{#compose-services-compose-list} Compose zeigt web als laufend an. Wie prüfst du direkt, ob der Dienst die erwartete Seite liefert?

::option[Zähle die Dienste in der Ausgabe von config.]{#compose-services-compose-list-b explanation="Aus der Anzahl der Dienste geht nicht hervor, welche Seite der Webserver ausliefert."}
::option[Rufe die veröffentlichte Webadresse auf.]{#compose-services-compose-list-a .correct explanation="Mit der Anfrage prüfst du, welche Seite tatsächlich ausgeliefert wird."}
::option[Prüfe den Namen eines anderen Containers.]{#compose-services-compose-list-c explanation="Der Name kennzeichnet den Container. Ob der Dienst antwortet, lässt sich daraus nicht ablesen."}
:::

![Compose-Status mit den laufenden Diensten web und toolbox sowie Host-Port 8080](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/docker-compose/compose-services/project-status.png)

Im Screenshot ist der ursprüngliche Host-Port 8080 zu sehen. Wenn du einen anderen Port gewählt hast, suche auf der Host-Seite der Zuordnung nach dieser Nummer.

## Einen gestoppten Dienst prüfen

Der Werkzeugcontainer ist nur vorübergehend im Einsatz. Wenn seine Wartezeit abgelaufen ist oder du ihn stoppst, zeigt Compose ihn mit `-a` ebenfalls in der Liste an. Der Beispielbefehl unten stoppt den Werkzeugcontainer dieses Übungsprojekts. Der Webdienst läuft dabei weiter. Starte den Werkzeugcontainer erneut, wenn du den Kurs fortsetzen möchtest.

```bash
$ docker compose stop toolbox
$ docker compose ps -a
$ docker compose start toolbox
```

:::single-choice{#compose-services-stopped-service} Wo findest du toolbox, nachdem du den Dienst gestoppt hast?

::option[In der Ausgabe von docker compose ps -a für dieses Projekt.]{#compose-services-stopped-service-c .correct explanation="Die Option zeigt auch gestoppte Container des Projekts an."}
::option[Nur in der Image-Liste.]{#compose-services-stopped-service-a explanation="Wenn du das laufende Programm stoppst, bleibt der Container bestehen und lässt sich prüfen."}
::option[In der Containerliste eines anderen Projekts.]{#compose-services-stopped-service-b explanation="Toolbox gehört zu diesem Projekt."}
:::

Weitere Übungen zu Containern und Compose findest du in den [Docker Command Labs](https://labex.io/courses/docker-command-labs).

## Zusammenfassung

Du kannst jetzt mehrere Dienste aus einer Compose-Datei starten und überprüfen.

1. Starte die Dienste des ausgewählten Projekts.
2. Ermittle den Dienstnamen und den aktuellen Status.
3. Beziehe bei der Prüfung auch gestoppte Dienste ein.
