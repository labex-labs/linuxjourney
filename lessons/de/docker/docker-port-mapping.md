---
lesson_id: "docker-port-mapping"
course_id: "docker"
lang: "de"
order_index: 5
title: "Portzuordnung"
description: "Lerne, wie du einen Container-Port veröffentlichst und die passende Adresse für den Browser findest."
meta_title: "Portzuordnung – Docker"
meta_description: "Lies eine Docker-Portzuordnung, unterscheide Host- und Container-Port und finde heraus, ob eine Anfrage an den falschen Port ging."
meta_keywords: "Docker-Portzuordnung, Ports veröffentlichen, docker run -p, Host-Port, Container-Port"
---

Ein Webserver kann im Container laufen, ohne dass dein Browser ihn schon erreichen kann. Ein **Port** ist eine Nummer, über die ein Rechner eingehende Netzwerkanfragen dem passenden Dienst zuordnet. Docker kann einen Port auf dem Host veröffentlichen und eingehende Anfragen an einen Port im Container weiterleiten.

## Eine Portzuordnung lesen

Der Nginx-Server nimmt in diesem Beispiel Webanfragen am Port 80 im Container an. Der Container `web` aus dem früheren Beispiel wurde ohne einen veröffentlichten Port erstellt. Gib dem neuen Container einen anderen Namen und lege die Zuordnung beim Erstellen mit `-p` fest.

```bash
$ docker run -d --name published-web -p 127.0.0.1:8080:80 nginx:alpine
```

Lies `8080:80` als Weiterleitung vom **Host-Port** 8080 zum **Container-Port** 80. Der Browser verbindet sich mit dem Host-Port. Der Server empfängt die Anfrage am Container-Port. Mit `127.0.0.1` bindest du die Zuordnung an die Loopback-Adresse des Hosts, über die sich der Rechner selbst erreicht.

Nutze eine abgeschottete Übungsumgebung. Bei Docker Engine vor Version 28.0.0 können andere Rechner im selben lokalen Netzwerksegment unter Umständen auf Ports zugreifen, die auf localhost veröffentlicht wurden. [Docker-Dokumentation zur Veröffentlichung von Ports](https://docs.docker.com/engine/network/port-publishing/)

:::single-choice{#docker-port-mapping-request-target} Mit welchem Port verbindet sich ein Browser auf dem Docker-Host bei `127.0.0.1:9090:80`?

::option[Mit Port 9090 auf dem Host.]{#docker-port-mapping-target-outer .correct explanation="Die mittlere Zahl gibt den Host-Port an, an den sich der Browser wendet."}
::option[Mit Port 80 auf dem Host.]{#docker-port-mapping-target-inner explanation="Port 80 ist das Ziel im Container."}
::option[Mit Port 9090 im Container.]{#docker-port-mapping-target-wrong-side explanation="Der Server empfängt die Anfrage hier am Container-Port 80."}
:::

## Vom Host aus testen

Öffne `http://127.0.0.1:8080` im Browser auf dem Rechner, auf dem Docker den Port veröffentlicht hat. Wenn Docker auf einem entfernten Rechner läuft, zeigt `127.0.0.1` im Browser deines Laptops auf den Laptop selbst. Nutze in einem Browser-Lab den dort angegebenen Zugriffsweg.

:::single-choice{#docker-port-mapping-local-browser} Docker hat Port 8080 auf einem separaten Übungsrechner veröffentlicht. Wohin zeigt `127.0.0.1`, wenn du die Adresse im Browser deines Laptops eingibst?

::option[Auf den separaten Übungsrechner.]{#docker-port-mapping-local-lab explanation="Auf den Übungsrechner zeigt die Adresse nur, wenn sie dort verwendet wird."}
::option[Auf den Web-Container in Docker.]{#docker-port-mapping-local-container explanation="Der Browser verwendet die Adresse seines eigenen Rechners. Eine Portzuordnung kann die Anfrage an einen Container weiterleiten."}
::option[Auf deinen Laptop.]{#docker-port-mapping-local-laptop .correct explanation="Die Loopback-Adresse bezeichnet den Rechner, auf dem der Browser läuft."}
:::

## Veröffentlichte Ports prüfen

Die Spalte `PORTS` in `docker ps` kann die Zuordnung anzeigen. Der Pfeil zeigt von der Host-Adresse und dem Host-Port zum Container-Port. Die Endung `/tcp` nennt das Netzwerkprotokoll für diese Zuordnung.

```text
$ docker ps
STATUS         PORTS                   NAMES
Up 2 minutes   127.0.0.1:8080->80/tcp   published-web
```

Eine Zeile kann auch nur `80/tcp` anzeigen. Wenn Host-Adresse und Pfeil fehlen, zeigt der Eintrag keinen veröffentlichten Host-Port.

![LabEx-Terminal mit einer Weiterleitung von Host-Port 8080 zu Container-Port 80 und einer erfolgreichen HTTP-200-Antwort](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/docker/docker-port-mapping/loopback-mapping.png)

In der Aufnahme wurde die Liste auf `published-web` gefiltert. Die Anfrage mit `curl` kommt vom Docker-Host und bestätigt, dass die veröffentlichte Adresse erfolgreich antwortet.

:::single-choice{#docker-port-mapping-read-listing} Eine Zeile zeigt `80/tcp` ohne Pfeil. Was kannst du aus diesem Eintrag ablesen?

::option[Docker hat Port 80 auf dem Host veröffentlicht.]{#docker-port-mapping-listing-host explanation="Eine veröffentlichte Zuordnung nennt einen Host-Port und zeigt auf den Container-Port."}
::option[Der Eintrag zeigt einen Container-Port ohne veröffentlichten Host-Port.]{#docker-port-mapping-listing-container .correct explanation="Er nennt Port 80 im Container. Host-Adresse und Weiterleitungspfeil fehlen."}
::option[Docker hat Port 8080 auf dem Host veröffentlicht.]{#docker-port-mapping-listing-default explanation="Der Eintrag enthält keinen Host-Port. Docker leitet daraus nicht den Port 8080 ab."}
:::

## Die richtige Adresse zum Testen wählen

Wenn sich die Seite nicht öffnen lässt, vergleiche deine Adresse mit der linken Seite der Zuordnung. Der Status `Up` und der Pfeil zeigen, was Docker ausführt und wohin es weiterleitet. Eine Browseranfrage prüft, ob der Server tatsächlich die Seite zurückgibt.

:::single-choice{#docker-port-mapping-correct-misdirected} Auf dem Docker-Host versuchst du es mit Port 8080, aber die Seite lädt nicht. Die Zeile zeigt `127.0.0.1:8081->80/tcp`. Was solltest du als Nächstes versuchen?

::option[`http://127.0.0.1:80` öffnen.]{#docker-port-mapping-misdirected-80 explanation="Port 80 steht auf der Container-Seite der Zuordnung."}
::option[`http://127.0.0.1:8081` öffnen.]{#docker-port-mapping-misdirected-8081 .correct explanation="Nutze den veröffentlichten Host-Port links vom Pfeil."}
::option[`http://127.0.0.1:8080` erneut versuchen.]{#docker-port-mapping-misdirected-8080 explanation="Angegeben ist der Host-Port 8081. Mit 8080 prüfst du diese Zuordnung nicht."}
:::

## Zusammenfassung

Du kannst jetzt eine Portzuordnung lesen und die richtige Browseradresse daraus ermitteln.

1. Den Host-Port vom Container-Port unterscheiden.
2. Erklären, wohin `127.0.0.1` zeigt.
3. Eine veröffentlichte Portzuordnung in der Containerliste erkennen.
4. Den Dienst über den veröffentlichten Host-Port testen.
