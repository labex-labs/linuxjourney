---
lesson_id: "docker-run-command"
course_id: "docker"
lang: "de"
order_index: 3
title: "docker run"
description: "Lerne, wie Docker mit docker run einen Container aus einem Image erstellt und startet."
meta_title: "docker run – Docker"
meta_description: "Lies einen docker-run-Befehl, vergib Containernamen und unterscheide einen kurzen Vordergrundprozess von einem Server im Hintergrund."
meta_keywords: "docker run, Docker-Container starten, Container-Namen, Vordergrund, Hintergrundmodus"
---

Du hast ein Image mit einem Webserver. Mit `docker run` erstellst und startest du daraus einen Container. Probiere zuerst einen Befehl aus, der schnell endet. Dann siehst du, wann du wieder etwas ins Terminal eingeben kannst.

## Einen kurzen Befehl ausführen

BusyBox ist ein kleines Image mit grundlegenden Linux-Befehlen. Im Beispiel gibt `echo` eine Nachricht aus. Schreibe die Image-Referenz vor den Befehl, der im Container laufen soll. Fehlt das Image lokal, lädt Docker es normalerweise herunter. `$` markiert die Eingabeaufforderung. Falls Docker das Image zuerst laden muss, kann vor der gezeigten Zeile noch die Download-Ausgabe erscheinen.

```text
$ docker run busybox:1.36 echo Hello
Hello
```

Die Ausgabe erscheint im Terminal. Sobald `echo` fertig ist, stoppt der Container und die Eingabeaufforderung erscheint wieder.

:::single-choice{#docker-run-command-short-task} Was läuft in diesem Beispiel im Container?

::option[`busybox:1.36` als Shell-Befehl.]{#docker-run-command-short-image explanation="BusyBox ist das Image, das die Werkzeuge bereitstellt. Der Befehl folgt hinter der Image-Referenz."}
::option[`echo Hello` mit den Werkzeugen aus dem Image.]{#docker-run-command-short-echo .correct explanation="Hinter der Image-Referenz steht der Befehl echo mit dem Text, den er ausgeben soll."}
::option[`docker run` als zweiter Docker-Befehl.]{#docker-run-command-short-docker explanation="Du führst docker run im Terminal aus. Das startet den Befehl im Container."}
:::

## Den Container benennen

Setze `--name` vor die Image-Referenz, um dem Container einen Namen zu geben, den du später wiedererkennst. Dieser Befehl nennt den Container für die kurze Aufgabe `report`.

```bash
$ docker run --name report busybox:1.36 echo Ready
```

Ein Container behält seinen Namen auch dann, wenn er gestoppt ist. Wähle in derselben Docker-Umgebung einen freien Namen, wenn du einen weiteren Container erstellst.

:::single-choice{#docker-run-command-name-choice} Report ist fertig, aber der Container existiert noch. Was kannst du ändern, wenn du einen zweiten Container aus demselben Image erstellen möchtest?

::option[Einen neuen Containernamen wählen und die Image-Referenz beibehalten.]{#docker-run-command-name-new .correct explanation="Mit einem freien Namen kann Docker aus demselben Image einen separaten Container erstellen."}
::option[Den Image-Tag ändern und den Containernamen beibehalten.]{#docker-run-command-name-change-tag explanation="Der alte Container belegt den Namen weiterhin, auch wenn du ein anderes Image auswählst."}
::option[Die Nachricht ändern und den Containernamen beibehalten.]{#docker-run-command-name-change-message explanation="Die Nachricht ist die Eingabe für echo. Der Name report bleibt belegt."}
:::

## Einen Server im Hintergrund starten

Ein Image kann einen Standardbefehl vorgeben. `nginx:alpine` startet einen Webserver, wenn du hinter dem Image-Namen keinen Befehl angibst. Mit `-d` läuft der Container **im Hintergrund**, und du erhältst die Eingabeaufforderung zurück, während der Server weiterläuft.

```bash
$ docker run -d --name web nginx:alpine
```

Docker gibt eine Container-ID aus, mit der sich der gestartete Container eindeutig bezeichnen lässt. In der nächsten Lektion prüfst du, ob der Server noch läuft.

![LabEx-Terminal mit den Ausgaben Hello und Ready aus kurzen Docker-Aufgaben und der Container-ID eines im Hintergrund gestarteten Servers](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/docker/docker-run-command/foreground-and-detached.png)

Die kurzen Aufgaben geben ihre Nachrichten direkt im Terminal aus. Beim Start des Servers im Hintergrund gibt Docker eine Container-ID zurück.

:::single-choice{#docker-run-command-detach-meaning} Docker gibt eine ID aus und die Eingabeaufforderung erscheint wieder. Was kannst du in diesem Modus tun?

::option[Das Terminal erst wieder nutzen, wenn der Server fertig ist.]{#docker-run-command-detach-wait explanation="Der Hintergrundmodus gibt das Terminal frei, während der Server weiterläuft."}
::option[Den Start des Servers überspringen und nur das Image bereithalten.]{#docker-run-command-detach-skip explanation="Docker startet den Container auch im Hintergrundmodus."}
::option[Das Terminal nutzen, während der Server läuft.]{#docker-run-command-detach-continue .correct explanation="Nach dem Start des Containers kannst du wieder Befehle im Terminal eingeben."}
:::

## Einen neuen Container erkennen

Jeder erfolgreiche Aufruf von `docker run` erstellt einen neuen Container. Wenn du das Server-Image erneut mit einem freien Namen verwendest, erstellt Docker einen zweiten Container. Der erste behält seinen Namen und seinen Zustand.

:::single-choice{#docker-run-command-second-instance} Web läuft. Was macht `docker run -d --name demo nginx:alpine`, wenn der Name demo frei ist?

::option[Der laufende Container web wird in demo umbenannt.]{#docker-run-command-second-rename explanation="Docker run erstellt einen Container. Der bisherige Container web behält seinen Namen."}
::option[Das Image erhält einen weiteren Tag namens demo.]{#docker-run-command-second-tag explanation="Die Option legt den Containernamen fest. Die Image-Referenz bleibt nginx:alpine."}
::option[Ein separater Container namens demo startet.]{#docker-run-command-second-new .correct explanation="Docker erstellt aus diesem Image einen neuen Container und nennt ihn demo."}
:::

Wenn du selbst einen Container starten und seine Ausgabe beobachten möchtest, probiere [Dein erstes Docker-Lab](https://labex.io/labs/docker-your-first-docker-lab-92719) aus.

## Zusammenfassung

Du kannst jetzt einen docker-run-Befehl lesen und einschätzen, was Docker damit erstellt.

1. Image und optionalen Befehl für den Container erkennen.
2. Mit `--name` einen leicht wiederzufindenden Containernamen festlegen.
3. Beschreiben, was am Ende einer kurzen Aufgabe passiert.
4. Mit `-d` die Eingabeaufforderung zurückerhalten, während ein Server läuft.
