---
lesson_id: "git-repositories"
course_id: "git"
lang: "de"
order_index: 1
title: "Repositorys"
description: "Lerne, was ein Git-Repository speichert, und lege ein leeres Repository für eine kleine Website an."
meta_title: "Repositorys – Git"
meta_description: "Lege ein leeres Git-Repository an, lerne Arbeitsbaum und .git-Verzeichnis kennen und unterscheide das Initialisieren vom Klonen."
meta_keywords: "Git-Repository, Arbeitsbaum, git init, git clone, DevOps, Linux Journey"
---

Eine Website beginnt mit ein paar Dateien. Mit Git kannst du festhalten, wie diese Dateien zu bestimmten Zeitpunkten aussahen. Projektdateien und Verlauf bilden zusammen deinen lokalen Git-Arbeitsbereich.

## Ein Repository erstellen

Beginne in einem Übungsverzeichnis, in dem du einen neuen Ordner erstellen kannst. Führe die folgenden Befehle einmal aus. Das Dollarzeichen steht für die Eingabeaufforderung.

```bash
$ mkdir journey-git
$ cd journey-git
$ git init --initial-branch=main
```

Der neue Ordner ist dein **Arbeitsbaum**. Dort bearbeitest du die Projektdateien. Git erstellt darin das versteckte Verzeichnis `.git` für Verlauf und Einstellungen. Das neue Repository enthält noch keine gespeicherten Änderungen. Der erste Branch heißt hier `main`.

:::single-choice{#git-repositories-empty-history} Du initialisierst ein Repository in einem Ordner, der schon index.html enthält. Was geschieht mit dem Verlauf dieser Datei?

::option[Git speichert die Datei sofort im ersten Commit.]{#git-repositories-empty-history-b explanation="Beim Initialisieren werden keine Projektdateien erfasst."}
::option[Git kann die Datei in einem späteren Commit speichern.]{#git-repositories-empty-history-a .correct explanation="Beim Initialisieren wird das Repository vorbereitet. Einen Stand zu speichern ist ein eigener Schritt."}
::option[Git verschiebt die Datei in das versteckte Git-Verzeichnis.]{#git-repositories-empty-history-c explanation="Die Projektdateien bleiben im Arbeitsbaum, wo du sie bearbeiten kannst."}
:::

![LabEx-Terminal mit einem neu initialisierten Git-Repository und dessen ausgegebenem Stammverzeichnis](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/git/git-repositories/init-and-root.png)

## Den Arbeitsbaum erkennen

Mit `git rev-parse --show-toplevel` kannst du das Stammverzeichnis des aktuellen Repositorys ausgeben. Im Übungsverzeichnis sollte der Pfad auf `journey-git` enden. Ein Unterordner im Arbeitsbaum gehört zum selben Repository, außer wenn er ein eigenes Repository enthält.

```bash
$ git rev-parse --show-toplevel
```

:::single-choice{#git-repositories-find-root} Du wechselst in den Unterordner images in journey-git. Welches Verzeichnis sollte Git als oberste Ebene anzeigen?

::option[Das Verzeichnis journey-git.]{#git-repositories-find-root-b .correct explanation="Git findet das Stammverzeichnis oberhalb des aktuellen Ordners."}
::option[Den Unterordner images.]{#git-repositories-find-root-a explanation="Das Stammverzeichnis gehört zum Repository. Es ändert sich nicht, wenn du in einem Unterordner arbeitest."}
::option[Das versteckte Verzeichnis .git.]{#git-repositories-find-root-c explanation="Der Befehl zeigt die Wurzel des Arbeitsbaums, in dem die Projektdateien liegen."}
:::

## Mit vorhandenem Verlauf beginnen

Verwende `git clone`, wenn du ein vorhandenes Repository kopieren möchtest. Ein normaler Klon erstellt einen lokalen Arbeitsbaum und übernimmt den vorhandenen Verlauf. Mit `git init` beginnst du dagegen einen neuen Projektverlauf auf deinem Rechner. In den folgenden Lektionen verwendest du weiterhin `journey-git`.

:::single-choice{#git-repositories-choose-start} Jemand aus dem Team gibt dir die Adresse eines Repositorys, dessen Verlauf du brauchst. Wie fängst du an?

::option[Einen leeren Ordner anlegen und ein Repository initialisieren.]{#git-repositories-choose-start-a explanation="Das neue Repository enthält den Verlauf aus dem Team-Repository nicht."}
::option[Nur die sichtbaren Website-Dateien kopieren.]{#git-repositories-choose-start-b explanation="Die sichtbaren Dateien liefern einen bestimmten Stand. Der Verlauf des Repositorys fehlt dabei."}
::option[Das Repository aus dem Team klonen.]{#git-repositories-choose-start-c .correct explanation="Beim Klonen bekommst du den vorhandenen Verlauf und einen lokalen Arbeitsbaum."}
:::

## Zusammenfassung

Du kannst jetzt entscheiden, wie du zu einem lokalen Git-Repository kommst.

1. Den Arbeitsbaum und das versteckte Git-Verzeichnis erkennen.
2. Das Stammverzeichnis aus einem Unterordner finden.
3. Für einen neuen Verlauf ein Repository initialisieren und für einen bestehenden Verlauf ein Repository klonen.
