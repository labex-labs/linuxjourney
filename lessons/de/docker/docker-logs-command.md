---
lesson_id: "docker-logs-command"
course_id: "docker"
lang: "de"
order_index: 6
title: "docker logs"
description: "Lerne, wie du die erfasste Ausgabe eines Containers liest und daraus einen ersten Schritt zur Fehlersuche ableitest."
meta_title: "docker logs – Docker"
meta_description: "Lies die Logs laufender oder beendeter Container, beschränke die Ausgabe auf die letzten Zeilen und unterscheide Programmfehler vom Containerstatus."
meta_keywords: "docker logs, Container-Logs, Docker-Fehlersuche, Startfehler, letzte Logzeilen"
---

Ein Container namens `preview` wurde beendet. In der Containerliste siehst du seinen Status und Exit-Code. Was das Programm gemeldet hat, steht in der Ausgabe, die Docker von diesem Container gesammelt hat.

## Den richtigen Container auswählen

Gib den Containernamen an `docker logs` weiter. Der Befehl kann auch aufbewahrte Ausgaben eines gestoppten Containers lesen, solange dieser noch existiert. In diesem Beispiel hat ein kurzer Auftrag versucht, die Datei `/site/title.txt` zu lesen.

```text
$ docker logs preview
cat: can't open '/site/title.txt': No such file or directory
```

Hier ist `cat` das Programm, das die Datei lesen wollte. Seine Meldung nennt den Pfad, den das Programm im Container nicht finden konnte.

:::single-choice{#docker-logs-command-read-exited} Preview und report verwendeten dasselbe Image. Welcher Befehl liest die Ausgabe von preview?

::option[`docker logs report`]{#docker-logs-command-exited-report explanation="Der Name wählt den Container aus. Report bezeichnet einen anderen Lauf."}
::option[`docker logs busybox:1.36`]{#docker-logs-command-exited-image explanation="Das ist eine Image-Referenz. Die Logs gehören zu einem Container, der aus dem Image erstellt wurde."}
::option[`docker logs preview`]{#docker-logs-command-exited-preview .correct explanation="Dieser Befehl verwendet den Namen des Containers, dessen Ausgabe du sehen willst."}
:::

## Die Meldung einordnen

Logs enthalten Meldungen, die das Programm selbst geschrieben hat. Eine Startmeldung kann zeigen, dass es jetzt Anfragen annimmt. Eine Fehlermeldung kann die Aktion benennen, die es nicht ausführen konnte. Im Beispiel meldet `preview` einen fehlenden Pfad im Container. Prüfe, ob die Datei an genau diesem Pfad vorhanden sein sollte. Die Meldung gibt dir einen konkreten Ausgangspunkt.

:::single-choice{#docker-logs-command-error-boundary} Was kannst du aus der Meldung über die fehlende Datei schließen?

::option[Die Datei fehlt in sämtlichen Verzeichnissen auf dem Host.]{#docker-logs-command-error-host-path explanation="Das Programm hat einen Pfad im Container gesucht. Die Meldung beschreibt nicht alle Dateien des Hosts."}
::option[Das Programm hat die genannte Datei in preview nicht gefunden.]{#docker-logs-command-error-container-path .correct explanation="Die Meldung beschreibt die Dateisuche des Programms in preview."}
::option[Der Browser auf dem Host hat einen unveröffentlichten Port verwendet.]{#docker-logs-command-error-network explanation="Die Meldung betrifft eine Dateisuche und macht keine Aussage über den Port des Browsers."}
:::

## Die letzten Ausgaben ansehen

Wenn ein Container viele Zeilen ausgibt, verwende `--tail` mit einer Zahl. Docker gibt höchstens so viele Zeilen vom Ende der erfassten Ausgabe zurück. Beginne mit wenigen Zeilen und lies bei Bedarf mehr, wenn der erste Fehler weiter oben steht.

```bash
$ docker logs --tail 5 web
```

![LabEx-Terminal mit der Meldung über eine fehlende Datei in preview und den letzten fünf Logzeilen von web](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/docker/docker-logs-command/preview-and-tail.png)

Die Befehle lesen zwei verschiedene Container. In LabEx meldet `preview` die fehlende Datei und `web` den Start von Nginx.

:::single-choice{#docker-logs-command-tail-choice} Du möchtest nur die zwei neuesten verfügbaren Zeilen von web sehen. Welcher Befehl passt?

::option[`docker logs --tail 2 web`]{#docker-logs-command-tail-two .correct explanation="Tail 2 gibt bis zu zwei Zeilen vom Ende der Ausgabe dieses Containers aus."}
::option[`docker logs --tail 5 web`]{#docker-logs-command-tail-five explanation="Der Befehl kann bis zu fünf Zeilen ausgeben und damit mehr als zwei."}
::option[`docker logs web`]{#docker-logs-command-tail-unlimited explanation="Ohne Limit kann Docker alle verfügbaren Zeilen zurückgeben."}
:::

## Eine leere Ausgabe einordnen

Docker zeigt nur Ausgaben, die es erfasst hat. Manche Befehle arbeiten ohne Meldungen. Programme können ihre Logs auch in eine Datei schreiben, die Docker nicht erfasst. Wenn `docker logs` erfolgreich ist, aber nichts ausgibt, prüfe den Status mit `docker ps -a`. Aus leeren Logs allein geht der Zustand des Containers nicht hervor.

:::single-choice{#docker-logs-command-empty-result} Für die Aufgabe cleanup gibt es keine Logzeilen. Wie kannst du prüfen, ob sie noch läuft oder schon beendet ist?

::option[Docker nach weiteren Zeilen für cleanup fragen.]{#docker-logs-command-empty-more-lines explanation="Eine andere Zeilenzahl zeigt nicht, ob ein Programm ohne Ausgabe beendet wurde."}
::option[Das Image ermitteln, aus dem cleanup gestartet wurde.]{#docker-logs-command-empty-image explanation="Das Image beschreibt die ursprünglichen Dateien und Einstellungen. Den Zustand zeigt die Containerliste."}
::option[Den Zustand von cleanup in der vollständigen Containerliste prüfen.]{#docker-logs-command-empty-container-state .correct explanation="Die vollständige Liste enthält vorhandene beendete und laufende Container."}
:::

## Zusammenfassung

Du kannst jetzt anhand der Ausgabe eines Containers entscheiden, was du als Nächstes prüfst.

1. Die erfasste Ausgabe eines benannten Containers lesen, auch wenn er beendet wurde.
2. Die Programmmeldung nutzen, um das gemeldete Problem zu finden.
3. Die Ausgabe mit `--tail` begrenzen.
4. Eine zusätzliche Prüfung wählen, wenn die Logs eine Frage offenlassen.
