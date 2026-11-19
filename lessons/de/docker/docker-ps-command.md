---
lesson_id: "docker-ps-command"
course_id: "docker"
lang: "de"
order_index: 4
title: "docker ps"
description: "Lerne, wie du Docker-Container auflistest und erkennst, welche laufen oder beendet sind."
meta_title: "docker ps – Docker"
meta_description: "Lies die Ausgabe von docker ps, finde beendete Container mit docker ps -a und ordne Namen, Status und Exit-Codes ein."
meta_keywords: "docker ps, Docker-Container auflisten, beendete Container, docker ps -a, Containerstatus, Exit-Code"
---

Läuft der Webserver noch, den du in Docker gestartet hast? Prüfe es mit `docker ps`. Ein Docker-Image enthält das Programm und die benötigten Dateien. Ein Container ist eine Instanz, die aus diesem Image erstellt wurde. Der Befehl zeigt die Containerliste zum Zeitpunkt der Abfrage.

## Laufende Container auflisten

Standardmäßig listet `docker ps` die laufenden Container auf. Die Beispiele zeigen wenige Spalten aus einer vorbereiteten Docker-Umgebung. Du kannst die Ausgabe auch ohne eigene Docker-Installation lesen. Im Terminal gibst du den Befehl hinter der Eingabeaufforderung `$` ein.

```text
$ docker ps
IMAGE         STATUS         NAMES
nginx:alpine  Up 4 minutes   web
nginx:alpine  Up 30 seconds  demo
```

Wenn Docker nur die Spaltenüberschriften ausgibt, ist die Liste der laufenden Container leer. In derselben Umgebung kann es weiterhin gestoppte Container geben.

:::single-choice{#docker-ps-running-list} Docker gibt nach `docker ps` nur die Spaltenüberschriften aus. Was kannst du daraus ablesen?

::option[Es sind keine Images zum Starten verfügbar.]{#docker-ps-running-list-images explanation="Der Befehl listet Container auf. Auch bei leerer Liste können Images verfügbar sein."}
::option[Die Liste enthält keine laufenden Container.]{#docker-ps-running-list-empty .correct explanation="Die Standardliste zeigt laufende Container. Gestoppte Container können weiterhin vorhanden sein."}
::option[Es gibt keine gestoppten Container, die du prüfen kannst.]{#docker-ps-running-list-stopped explanation="Gestoppte Container sind in der Standardauswahl nicht enthalten. Die leere Liste sagt nichts über sie aus."}
:::

## Namen und Status lesen

Suche den gewünschten Container zunächst unter `NAMES`. Beide Zeilen zeigen in der Spalte `IMAGE` dasselbe Image, `nginx:alpine`. Suche ganz rechts nach `web` und lies in dieser Zeile die Spalte `STATUS`. `Up 4 minutes` bedeutet, dass der Container seit ungefähr vier Minuten läuft.

:::single-choice{#docker-ps-name-column} Welche Zeile beschreibt einen Container, der seit ungefähr 30 Sekunden läuft?

::option[Die Zeile mit dem Namen `demo`.]{#docker-ps-name-demo .correct explanation="Suche Up 30 seconds unter STATUS und folge der Zeile bis zu demo unter NAMES."}
::option[Die Zeile mit dem Namen `web`.]{#docker-ps-name-web explanation="In der Zeile für web steht Up 4 minutes. Beide Container verwenden dasselbe Image, wurden aber zu unterschiedlichen Zeiten gestartet."}
::option[Beide Zeilen mit dem Image `nginx:alpine`.]{#docker-ps-name-image-reference explanation="Jede Zeile hat einen eigenen Status. Gleiche Images bedeuten keine gleiche Startzeit."}
:::

## Auch beendete Container anzeigen

Wenn du den gesuchten Container nicht findest, versuche es mit `docker ps -a`. `-a` ist die Kurzform von `--all`. Damit siehst du auch gestoppte Container, die noch existieren. Das Beispiel enthält zusätzlich eine vorbereitete Aufgabe namens `preview`.

```text
$ docker ps -a
IMAGE         STATUS                         NAMES
nginx:alpine  Up 4 minutes                   web
nginx:alpine  Up 30 seconds                  demo
busybox:1.36  Exited (0) 2 minutes ago       report
busybox:1.36  Exited (1) About a minute ago  preview
```

Ein Container führt ein Hauptprogramm aus, etwa einen Webserver oder ein Skript. `Exited` bedeutet, dass dieses Programm beendet wurde. Die Zahl in Klammern ist der **Exit-Code**, den das Programm bei der Beendigung gemeldet hat. Null bedeutet normalerweise Erfolg. Ein anderer Wert weist meist auf einen Fehler hin. Die Aufgabe `report` zeigt `Exited (0)`, wie bei einem erfolgreich abgeschlossenen kurzen Auftrag zu erwarten ist.

![LabEx-Terminal mit laufenden und beendeten Containern, report mit Exit-Code 0 und preview mit Exit-Code 1](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/docker/docker-ps-command/running-and-exited.png)

Die Aufnahme aus LabEx zeigt nur Namen und Status der vier Beispielcontainer. Die Zeitangaben hängen davon ab, wann du den Befehl ausführst.

:::single-choice{#docker-ps-exit-code-reading} Welche Zeile würdest du aufgrund ihres Exit-Codes auf einen Fehler untersuchen?

::option[`report`, weil die Aufgabe beendet ist.]{#docker-ps-exit-code-report explanation="Ein kurzer Auftrag kann nach getaner Arbeit enden. Der Exit-Code null bedeutet normalerweise Erfolg."}
::option[`demo`, weil dieser laufende Container zuletzt gestartet wurde.]{#docker-ps-exit-code-demo explanation="Up zeigt die bisherige Laufzeit. Diese Zeile enthält keinen Exit-Code."}
::option[`preview`, weil die Aufgabe mit Code 1 beendet wurde.]{#docker-ps-exit-code-preview .correct explanation="Bei preview steht Exited (1). Das ist ein Anlass für weitere Nachforschungen. Der Status allein nennt keine Ursache."}
:::

## Die nächste Prüfung wählen

Der Exit-Code hilft dir einzuschätzen, was du als Nächstes prüfen solltest. Um zu sehen, ob `preview` einen Fehler ausgegeben hat, gib seinen Namen nach `docker logs` an. Der Befehl zeigt die Ausgabe, die Docker für diesen Container erfasst hat.

```bash
$ docker logs preview
```

Bei einem laufenden Webserver möchtest du vielleicht auch wissen, ob jemand die Seite aufrufen kann. Öffne sie auf dem Rechner, von dem aus der Zugriff funktionieren soll. `Up` beschreibt das Programm im Container. Eine erfolgreiche Browseranfrage bestätigt, dass die Seite vom getesteten Rechner aus erreichbar ist.

:::single-choice{#docker-ps-check-visitor-access} Auf dem Docker-Rechner lässt sich die Seite öffnen. Ein Kollege möchte sie von einem anderen Rechner aus öffnen. Welche Prüfung zeigt, ob das klappt?

::option[Die Seite auf dem Rechner des Kollegen öffnen.]{#docker-ps-next-check-visitor-browser .correct explanation="Die Anfrage prüft die Verbindung, die der Kollege tatsächlich verwendet."}
::option[Auf dem Docker-Rechner erneut `docker ps` ausführen.]{#docker-ps-next-check-status-again explanation="Die Liste kann zeigen, ob web weiterläuft. Für die Erreichbarkeit brauchst du eine Browseranfrage vom Rechner des Kollegen."}
::option[Die Seite auf dem Docker-Rechner noch einmal öffnen.]{#docker-ps-next-check-host-browser explanation="Damit wiederholst du die Prüfung aus derselben Umgebung. Die Verbindung des Kollegen kann sich anders verhalten."}
:::

## Zusammenfassung

Du kannst jetzt den richtigen Container finden, seinen Status lesen und die nächste Prüfung wählen.

1. Mit `docker ps` laufende Container auflisten.
2. Einen Container nach seinem Namen finden und seinen Status lesen.
3. Mit `docker ps -a` auch beendete Container anzeigen.
4. Logs oder eine Browseranfrage nutzen, wenn der Status allein nicht ausreicht.
