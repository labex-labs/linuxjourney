---
lesson_id: "docker-images"
course_id: "docker"
lang: "de"
order_index: 2
title: "Images"
description: "Lerne, wie du eine Image-Referenz liest und prüfst, ob das Image lokal verfügbar ist."
meta_title: "Images – Docker"
meta_description: "Lies Docker-Image-Namen und Tags, lerne Registries und Pulls kennen und unterscheide die Image-Liste von der Container-Liste."
meta_keywords: "Docker-Images, Image-Tags, Docker-Registry, docker pull, docker image ls"
---

Ein Docker-Image enthält ein Programm, seine Dateien und die Standardeinstellungen. Docker verwendet dieses Paket als Ausgangspunkt für einen Container. Hier lernst du, Image-Namen zu lesen und herauszufinden, welche Images bereits verfügbar sind.

## Image-Namen und Tags lesen

In `nginx:alpine` ist `nginx` der Image-Name und `alpine` der **Tag**. Dieses Kürzel wählt eine bestimmte Version oder Variante aus, hier eine Variante auf Basis von Alpine Linux. Der Doppelpunkt trennt den Namen vom Tag. `nginx:alpine` und `nginx:latest` sind zwei verschiedene Referenzen mit demselben Image-Namen.

:::single-choice{#docker-images-read-reference} Welcher Teil von `busybox:1.36` ist der Tag?

::option[`busybox`]{#docker-images-reference-name explanation="BusyBox ist der Name vor dem Doppelpunkt."}
::option[`busybox:1.36`]{#docker-images-reference-whole explanation="Die vollständige Referenz enthält Image-Namen und Tag."}
::option[`1.36`]{#docker-images-reference-tag .correct explanation="Der Text hinter dem Doppelpunkt ist der Tag, nach dem Docker das Image auswählt."}
:::

## Einen Tag wählen

Wenn du bei einer Referenz wie `nginx` keinen Tag angibst, verwendet Docker `latest`. Das ist ein vereinbarter Name. Wer das Image veröffentlicht, legt fest, auf welches Image der Tag zeigt, und kann ihn später umsetzen. Mit `nginx:alpine` legst du die Variante fest. Auch das Image hinter diesem Tag kann später aktualisiert werden.

:::single-choice{#docker-images-default-tag} Jemand startet `nginx` ohne Tag und erwartet die jüngste Version. Welches Image wählt die Referenz tatsächlich aus?

::option[Das Image, auf das der Tag latest zeigt.]{#docker-images-default-latest .correct explanation="Ohne Tag verwendet Docker latest. Auf welches Image der Tag zeigt, bestimmt der Herausgeber."}
::option[Das zuletzt veröffentlichte Nginx-Image.]{#docker-images-default-newest explanation="Docker verwendet den Tag latest. Es sortiert Images nicht nach Veröffentlichungsdatum."}
::option[Das kleinste verfügbare Nginx-Image.]{#docker-images-default-smallest explanation="Die Größe bestimmt den Standard-Tag nicht. Gib die gewünschte Variante ausdrücklich an."}
:::

## Ein Image herunterladen

Eine **Registry** speichert Images und stellt sie zum Abruf bereit. Für Referenzen wie `nginx:alpine` verwendet Docker standardmäßig Docker Hub. Mit `docker pull` lädst du ein Image in die Docker-Umgebung, mit der du gerade verbunden bist. Beim Herunterladen eines Images spricht man auch von einem **Pull**.

```bash
$ docker pull nginx:alpine
```

Wenn der Befehl erfolgreich ist, steht das Image dort zur Verfügung. Einen Container startest du in einem eigenen Schritt. In den Terminalbeispielen markiert `$` die Eingabeaufforderung.

:::single-choice{#docker-images-pull-result} Ein Pull war erfolgreich. Was hat Docker dabei getan?

::option[Einen Container gestartet, der Webanfragen beantwortet.]{#docker-images-pull-started explanation="Ein Container startet erst, wenn du ihn ausführst. Der Pull stellt das Image bereit."}
::option[Das Image in dieser Docker-Umgebung bereitgestellt.]{#docker-images-pull-available .correct explanation="Du kannst das heruntergeladene Image jetzt als Grundlage für einen Container verwenden."}
::option[Eine Kopie des Images in die Registry hochgeladen.]{#docker-images-pull-uploaded explanation="Beim Pull überträgt Docker das Image aus der Registry in seinen lokalen Speicher."}
:::

## Lokale Images prüfen

Mit `docker image ls` siehst du bereits vorhandene Images. Im Beispiel sind nur die Spalten für Name und Tag zu sehen. Docker nennt die Spalte für den Image-Namen `REPOSITORY`.

```text
$ docker image ls
REPOSITORY   TAG
nginx        alpine
busybox      1.36
```

In der ersten Zeile steht `nginx:alpine`. Die Tabelle zeigt vorhandene Images. Den Zustand eines daraus erstellten Containers findest du in einer anderen Liste.

![LabEx-Terminal mit docker pull und den Spalten REPOSITORY und TAG in docker image ls](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/docker/docker-images/pull-and-list.png)

Für diese Aufnahme wurde die Liste auf die beiden Referenzen aus der Lektion eingeschränkt.

:::single-choice{#docker-images-local-list} Welche Referenz ist laut dieser Ausgabe verfügbar?

::option[`busybox:latest`]{#docker-images-local-busybox-latest explanation="In der BusyBox-Zeile steht der Tag 1.36. Eine BusyBox-Zeile mit latest ist im Beispiel nicht zu sehen."}
::option[`busybox:1.36`]{#docker-images-local-busybox .correct explanation="Setze busybox aus der Spalte REPOSITORY und 1.36 aus der Spalte TAG zusammen."}
::option[`nginx:1.36`]{#docker-images-local-nginx-mixed explanation="Name und Tag müssen aus derselben Zeile stammen. 1.36 gehört hier zur BusyBox-Zeile."}
:::

## Zusammenfassung

Du kannst jetzt eine Image-Referenz lesen und in der lokalen Image-Liste nachsehen.

1. Name und Tag einer Image-Referenz erkennen.
2. Erklären, was Docker bei einem fehlenden Tag verwendet.
3. Mit `docker pull` ein Image aus einer Registry herunterladen.
4. Die Spalten für Name und Tag in `docker image ls` lesen.
