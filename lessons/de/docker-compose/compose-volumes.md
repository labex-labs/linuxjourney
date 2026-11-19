---
lesson_id: "compose-volumes"
course_id: "docker-compose"
lang: "de"
order_index: 4
title: "Volumes"
description: "Lerne, warum Dateien in einem benannten Volume den Austausch eines Containers überstehen."
meta_title: "Volumes - Docker Compose"
meta_description: "Lerne, warum Dateien in einem benannten Volume den Austausch eines Containers überstehen."
meta_keywords: "benannte Volumes, dauerhafte Speicherung, Docker Compose, DevOps, Linux Journey"
---

Ein Container kann eine Datei in seine eigene beschreibbare Schicht schreiben. Wenn du den Container entfernst, entfernt Docker auch diese Schicht. Ein **benanntes Volume** ist Speicher, den Docker separat verwaltet. Du kannst ihn in einen neuen Container einbinden.

## Ein Volume für die Übung definieren

Speichere dieses separate Beispiel als `compose.volume.yaml` im Übungsordner. Es bindet den Speicher namens `notes` unter `/data` im Werkzeugcontainer ein. Der Abschnitt `volumes` am Ende der Datei deklariert das benannte Volume.

```yaml
services:
  toolbox:
    image: busybox:1.36
    volumes:
      - notes:/data
volumes:
  notes:
```

Die Dienstdefinition legt fest, wo das Volume im Container eingebunden wird. Die Deklaration auf oberster Ebene legt fest, dass Compose das Volume gemeinsam mit dem Projekt verwaltet.

:::single-choice{#compose-volumes-attached-path} Welcher Pfad im Werkzeugcontainer verwendet das benannte Volume?

::option[/notes.]{#compose-volumes-attached-path-b explanation="Notes ist der Name des Volumes. Der Einhängepfad im Container steht rechts vom Doppelpunkt."}
::option[/data.]{#compose-volumes-attached-path-a .correct explanation="Die rechte Seite von notes:/data gibt den Pfad im Container an."}
::option[Jeder Pfad im Container.]{#compose-volumes-attached-path-c explanation="Das Volume ist nur im angegebenen Verzeichnis eingebunden."}
:::

## Mit getrennten Containern schreiben und lesen

Mit `-f` wählst du die alternative Datei aus. Mit `-p` legst du einen eigenen Projektnamen fest. Der Befehl `run --rm` erstellt für den Aufruf einen Container und entfernt ihn anschließend wieder. Führe die Befehle im separaten Übungsordner aus. Der erste Befehl überschreibt die Testdatei unter `/data/note.txt`.

```bash
$ docker compose -p journey-volume -f compose.volume.yaml run --rm toolbox sh -c 'echo ready > /data/note.txt'
$ docker compose -p journey-volume -f compose.volume.yaml run --rm toolbox cat /data/note.txt
```

Der zweite Container sollte `ready` ausgeben. In ihn ist dasselbe Volume eingebunden wie in den ersten Container.

:::single-choice{#compose-volumes-persistence} Warum kann der zweite Container die Datei lesen, nachdem der erste entfernt wurde?

::option[Dasselbe benannte Volume war in beide Container eingebunden.]{#compose-volumes-persistence-b .correct explanation="Die Datei wurde in den separaten Speicher geschrieben, der unter /data eingebunden ist."}
::option[Beide Container haben die beschreibbare Schicht des ersten Containers übernommen.]{#compose-volumes-persistence-a explanation="Die Schicht des ersten Containers wurde zusammen mit ihm entfernt."}
::option[BusyBox hat die Datei automatisch ins Image aufgenommen.]{#compose-volumes-persistence-c explanation="Beim Ausführen eines Containers bleibt das ursprüngliche Image unverändert."}
:::

![Zwei getrennte Werkzeugcontainer, die dieselbe Datei in einem benannten Volume schreiben und lesen](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/docker-compose/compose-volumes/persisted-note.png)

## Bewusst entscheiden, welche Daten du behältst

Eine Datei wie `/tmp/note.txt` liegt außerhalb des eingebundenen Verzeichnisses und bleibt an ihren Container gebunden, sofern dort kein anderer Speicher eingebunden ist. Prüfe den Pfad, bevor du davon ausgehst, dass eine Datei dauerhaft gespeichert wird. Wenn du das Volume selbst löschst, können seine Daten verloren gehen. Ein Backup ist eine separate Kopie. Geht das Volume verloren, kannst du die Daten daraus wiederherstellen.

:::single-choice{#compose-volumes-inside-mount} Auf welche Datei kann der nächste Werkzeugcontainer über dieses Volume zugreifen?

::option[Auf /tmp/note.txt aus der beschreibbaren Schicht des ersten Werkzeugcontainers.]{#compose-volumes-inside-mount-a explanation="Dieser Pfad liegt außerhalb des eingebundenen Volumes."}
::option[Auf eine Datei in einem anders benannten Volume.]{#compose-volumes-inside-mount-b explanation="Der neue Container muss dieses andere Volume ebenfalls einbinden, um darauf zuzugreifen."}
::option[Auf /data/note.txt, geschrieben vom ersten Werkzeugcontainer.]{#compose-volumes-inside-mount-c .correct explanation="Über den Einhängepfad /data greifen beide Container auf dieselbe gespeicherte Datei zu."}
:::

## Zusammenfassung

Du kannst jetzt erklären, warum eine Datei noch da sein kann, wenn ihr ursprünglicher Container entfernt wurde.

1. Lies den Namen des Volumes und den Einhängepfad.
2. Prüfe, ob die Datei in einem anderen Container noch lesbar ist.
3. Unterscheide zwischen dem Löschen eines Volumes und dem Austausch eines Containers.
