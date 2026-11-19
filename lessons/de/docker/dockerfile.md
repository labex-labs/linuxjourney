---
lesson_id: "dockerfile"
course_id: "docker"
lang: "de"
order_index: 7
title: "Dockerfile"
description: "Lerne, wie ein Dockerfile aus einer Seite und einem Basis-Image ein wiederverwendbares Webserver-Image erstellt."
meta_title: "Dockerfile – Docker"
meta_description: "Lies FROM, COPY und CMD in einem kurzen Dockerfile und unterscheide das Bauen eines Images vom Starten eines Containers."
meta_keywords: "Dockerfile, Docker-Image bauen, FROM, COPY, CMD, Build-Kontext"
---

Du hast schon einen Container aus einem vorhandenen Webserver-Image gestartet. Für deine eigene Seite kannst du ein Image bauen, das diese Seite bereits enthält. Ein **Dockerfile** ist eine Textdatei mit den Anweisungen für den Build.

## Mit einem Basis-Image beginnen

Ein **Basis-Image** liefert die Programme und Dateien für den Einstieg. Das folgende Dockerfile geht vom Nginx-Image aus, fügt eine Seite hinzu und legt den Standardbefehl für den Container fest. Lege das Dockerfile und eine Datei namens `index.html` in dasselbe Übungsverzeichnis. Für die Seite reicht eine einzige Zeile wie `<h1>Hello from Docker</h1>`.

```dockerfile
FROM nginx:alpine
COPY index.html /usr/share/nginx/html/index.html
CMD ["nginx", "-g", "daemon off;"]
```

`FROM nginx:alpine` wählt das genannte Image als Ausgangspunkt. Es enthält bereits das Programm Nginx. Docker verwendet es beim Bau des neuen Images.

:::single-choice{#dockerfile-base-image-purpose} Welche Zeile stellt Nginx bereit, bevor deine Seite hinzugefügt wird?

::option[`COPY index.html /usr/share/nginx/html/index.html`]{#dockerfile-base-image-copy explanation="COPY fügt die Seite hinzu. Das Serverprogramm kommt aus dem Basis-Image."}
::option[`FROM nginx:alpine`]{#dockerfile-base-image-from .correct explanation="FROM wählt das Basis-Image aus, das den Server bereits enthält."}
::option[Die Zeile, die mit `CMD` anfängt.]{#dockerfile-base-image-cmd explanation="CMD legt den Standardbefehl beim Start fest. Das Serverprogramm kommt aus dem Basis-Image."}
:::

## Eine Datei hinzufügen

`COPY` liest `index.html` aus den Dateien, die du beim Build bereitstellst. Es schreibt die Seite an den Pfad rechts in der Anweisung. Von dort liefert diese Version des Nginx-Images ihre Standardseite aus. Wenn du die lokale Seite bearbeitest, baue das Image erneut, damit die Änderung darin landet.

:::single-choice{#dockerfile-copy-after-edit} Du hast die Überschrift in deiner lokalen index.html nach dem Build geändert. Wie gelangt sie in ein neues Image?

::option[Einen weiteren Container aus dem vorhandenen Image starten.]{#dockerfile-copy-edit-run explanation="Dieser Container verwendet weiterhin die Seite, die bereits im Image enthalten ist."}
::option[Nur den Namen des vorhandenen Containers ändern.]{#dockerfile-copy-edit-rename explanation="Ein Containername ändert die im Image enthaltenen Dateien nicht."}
::option[Das Image mit der aktualisierten Seite neu bauen.]{#dockerfile-copy-edit-rebuild .correct explanation="Beim Build liest COPY die aktuelle lokale Datei und nimmt sie ins neue Image auf."}
:::

## Den Startbefehl festlegen

`CMD` legt den Standardbefehl für einen neuen Container fest. Im Beispiel läuft Nginx damit im Container im Vordergrund weiter. Mit `docker run -d` kann der Container trotzdem im Hintergrund laufen, während dein Terminal wieder frei wird.

:::single-choice{#dockerfile-cmd-start-time} Wann wird der Standardbefehl aus CMD im Beispiel ausgeführt?

::option[Wenn ein Container mit seinem Standardbefehl startet.]{#dockerfile-cmd-when-start .correct explanation="Docker verwendet den Standardbefehl des Images beim Containerstart."}
::option[Während Docker die Seite in das Image kopiert.]{#dockerfile-cmd-when-copy explanation="COPY fügt die Seite während des Builds hinzu. Dabei startet der Server nicht."}
::option[Sobald Docker mit dem Schreiben des Images fertig ist.]{#dockerfile-cmd-when-build explanation="Beim Build wird der Startbefehl für die spätere Verwendung gespeichert."}
:::

## Bauen und starten

Starte den Build in dem Verzeichnis, das beide Dateien enthält. Mit `-t` legst du die Image-Referenz `journey-web:1` fest. Der Punkt am Ende gibt an, dass die Dateien für den Build aus dem aktuellen Verzeichnis kommen.

```bash
$ docker build -t journey-web:1 .
$ docker run -d --name custom-web -p 127.0.0.1:8082:80 journey-web:1
```

Der zweite Befehl startet einen Container. Wenn Port 8082 frei ist, kannst du auf dem Docker-Host im Browser `http://127.0.0.1:8082` öffnen und deine Seite sehen.

:::single-choice{#dockerfile-build-versus-run} Der Build war erfolgreich. Du hast den zweiten Befehl noch nicht ausgeführt. Was steht bereits bereit?

::option[Das Image ist vorhanden und kann zur Erstellung eines Containers verwendet werden.]{#dockerfile-build-ready-image .correct explanation="Beim Build ist ein Image entstanden. Der nächste Befehl startet daraus einen Container."}
::option[Der benannte Container liefert deine Seite bereits aus.]{#dockerfile-build-ready-container explanation="Der Server startet erst, wenn du das Image in einem Container ausführst."}
::option[Docker hat den Browser-Port bereits für das Image veröffentlicht.]{#dockerfile-build-ready-port explanation="Die Portzuordnung ist eine Option von docker run. Der Build richtet diese Verbindung nicht ein."}
:::

![LabEx-Terminal mit Image-Build, Containerstart und HTML-Antwort der eigenen Seite](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/docker/dockerfile/build-and-run.png)

Die letzte Anfrage ruft die Seite ab, die beim Build ins Image gepackt wurde. Die Build-Ausgabe und die Image-IDs können in deiner Umgebung anders aussehen.

## Zusammenfassung

Du kannst jetzt ein kleines Dockerfile lesen und nachvollziehen, wie aus einer lokalen Seite ein laufender Server wird.

1. Das Basis-Image in `FROM` erkennen.
2. Beschreiben, von wo `COPY` eine Datei liest und wohin es sie schreibt.
3. `CMD` als Standardbefehl beim Containerstart erkennen.
4. Ein Image bauen und daraus einen Container starten.
