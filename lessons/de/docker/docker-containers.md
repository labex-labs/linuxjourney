---
lesson_id: "docker-containers"
course_id: "docker"
lang: "de"
order_index: 1
title: "Container"
description: "Lerne, was in einem Docker-Container läuft und wie der Container mit dem Rechner zusammenhängt, auf dem Docker läuft."
meta_title: "Container – Docker"
meta_description: "Lerne Container am Beispiel eines kleinen Webservers kennen und sieh, was sich ändert, wenn sein Hauptprogramm startet oder stoppt."
meta_keywords: "Docker-Container, Container-Grundlagen, Docker-Host, Container-Prozess, Webserver"
---

Im Browser öffnest du eine Seite von einem Webserver, der in Docker läuft. Wo läuft der Server eigentlich? Und was passiert mit der Seite, wenn du ihn stoppst? Schauen wir zuerst auf das Programm, das dem Browser antwortet.

## Ein Programm im Container

Ein **Webserver** ist ein Programm, das Anfragen nach Webseiten beantwortet. Stell dir vor, dein Browser und ein kleiner Webserver namens `web` laufen auf demselben Rechner. Docker führt den Server in einem **Container** aus. Darin hat das Programm eine eigene Sicht auf Dateien und andere Ressourcen. Die Beispiele im Kurs sind vorbereitet, sodass du auch ohne Docker-Installation folgen kannst.

:::single-choice{#docker-containers-page-request} Wer schickt den Seiteninhalt zurück, wenn der Browser eine Seite anfordert?

::option[Der Webserver, der im Container läuft.]{#docker-containers-page-server .correct explanation="Das Serverprogramm nimmt die Anfrage an und schickt die Seite zurück."}
::option[Die Dateien, die den Start des Containers beschreiben.]{#docker-containers-page-files explanation="Diese Dateien legen die technischen Voraussetzungen fest. Die Anfrage beantwortet ein laufendes Programm."}
::option[Die Liste der Docker-Container auf dem Rechner.]{#docker-containers-page-list explanation="Die Liste zeigt, was Docker ausführt. Sie liefert selbst keine Webseiten aus."}
:::

## Container und Host

Der Rechner, auf dem die Container laufen, heißt **Host**. Wenn Docker unter Linux Linux-Container ausführt, laufen die darin enthaltenen Programme als Prozesse auf diesem Host. Ein **Prozess** ist ein laufendes Programm. Mehrere Container können denselben Host nutzen, verfügen dabei aber jeweils nur über einen begrenzten Teil der Ressourcen. Bei Docker Desktop laufen Linux-Container in einer von Docker verwalteten Linux-VM.

:::single-choice{#docker-containers-shared-host} Zwei Linux-Container laufen auf demselben Linux-Host. Was folgt daraus?

::option[Ihre Programme müssen dieselben Dateien sehen.]{#docker-containers-host-shared-files explanation="Jeder Container kann auf demselben Host seine eigene Sicht auf Dateien haben."}
::option[Ihre Programme können als getrennte Prozesse auf dem Host laufen.]{#docker-containers-host-separate-processes .correct explanation="Ein gemeinsamer Host kann Programme in getrennten Containern ausführen."}
::option[Jeder Container muss eine eigene Linux-Maschine starten.]{#docker-containers-host-separate-machines explanation="Linux-Container können als Prozesse auf einem Host laufen. Dafür ist keine eigene Maschine pro Container nötig."}
:::

## Von einem Image ausgehen

Docker erstellt einen Container aus einem **Image**. Es enthält das Programm und die Dateien, die es braucht. Aus demselben Webserver-Image kannst du `web` und `demo` erstellen. Nach dem Start läuft in jedem Container ein eigener Prozess desselben Serverprogramms. Du kannst jeden Container unabhängig vom anderen stoppen.

:::single-choice{#docker-containers-two-from-image} Du stoppst demo, während web noch läuft. Was passiert mit web?

::option[Es pausiert, bis demo wieder startet.]{#docker-containers-two-paused explanation="Jeder Container führt sein eigenes Programm aus. In diesem Beispiel unterbricht das Stoppen von demo den Betrieb von web nicht."}
::option[Es muss aus dem Image neu erstellt werden.]{#docker-containers-two-recreate explanation="Der web-Container wurde separat erstellt und kann weiterlaufen."}
::option[Es läuft in seinem eigenen Container weiter.]{#docker-containers-two-independent .correct explanation="Die beiden Container verwenden dasselbe Image als Ausgangspunkt und laufen unabhängig voneinander."}
:::

## Den Dienst vor und nach dem Stoppen überprüfen

Angenommen, dein Browser kann bereits Anfragen an `web` senden. Bevor du den Container stoppst, erhält der Browser die Seite. Nach dem Stoppen liefert der Server bei einer neuen Anfrage keine Seite mehr. Das Image steht weiterhin bereit, falls du daraus einen anderen Container erstellen möchtest. Damit der Browser eine Seite erhält, muss das Serverprogramm laufen und vom Browser erreichbar sein. Wie du einen Container vom Browser aus erreichst, zeigt eine spätere Lektion.

:::single-choice{#docker-containers-stopped-server} Das Image ist noch verfügbar, aber web wurde gestoppt. Was muss passieren, damit web selbst wieder antwortet?

::option[Das Serverprogramm in web muss wieder laufen.]{#docker-containers-stopped-program .correct explanation="Das Image liefert die Dateien. Neue Anfragen verarbeitet ein laufendes Serverprogramm."}
::option[Das Image muss umbenannt werden, damit es wieder Seiten ausliefern kann.]{#docker-containers-stopped-rename explanation="Ein neuer Name startet kein gestopptes Serverprogramm."}
::option[Der Browser braucht eine weitere Kopie des Server-Images.]{#docker-containers-stopped-browser-image explanation="Der Browser sendet Anfragen. Das Serverprogramm läuft im Container."}
:::

![LabEx-Terminal mit HTTP 200 vor dem Stoppen des Containers und einem Verbindungsfehler danach](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/docker/docker-containers/server-response.png)

In diesem LabEx-Beispiel liefert der Container `page-demo` die Seite aus. Die erste Anfrage mit `curl` erhält HTTP 200. Nach dem Stoppen des Containers schlägt eine neue Anfrage fehl. Curl gibt `000` aus, weil keine HTTP-Antwort eingetroffen ist.

## Zusammenfassung

Du kannst jetzt erklären, wie ein Container ein Programm auf einem Host ausführt.

1. Erkennen, welches Programm eine Browseranfrage beantwortet.
2. Erklären, wie mehrere Container denselben Host nutzen können.
3. Beschreiben, wie aus einem Image mehrere Container entstehen können.
4. Mit einer neuen Anfrage prüfen, ob ein zuvor erreichbarer Server noch antwortet.
