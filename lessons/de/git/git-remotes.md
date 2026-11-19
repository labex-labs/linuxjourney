---
lesson_id: "git-remotes"
course_id: "git"
lang: "de"
order_index: 6
title: "Remotes"
description: "Lerne, wie ein Git-Remote Repositorys verbindet und worin sich Fetch und Push unterscheiden."
meta_title: "Remotes – Git"
meta_description: "Richte ein lokales Bare-Repository als Remote ein, sende einen Commit und prüfe, was Git beim Abrufen übernimmt."
meta_keywords: "Git-Remotes, git remote, git fetch, git push, DevOps, Linux Journey"
---

Ein **Remote** ist eine benannte Adresse, über die dein lokales Git-Repository ein anderes Repository erreicht. Dieses kann bei einem Hosting-Dienst liegen oder in einem Ordner auf demselben Rechner. Für diese Übung verwendest du einen separaten lokalen Ordner. Ein Konto beim Hosting-Dienst ist nicht erforderlich.

## Eine Adresse hinzufügen

Erstelle vom Übungsrepository aus ein separates **Bare-Repository**. Ein solches Repository speichert Verlauf und Referenzen, hat aber keinen Arbeitsbaum für die Projektdateien. Es kann Commits aus deinem Arbeitsbereich empfangen. Für einen frischen Übungsdurchlauf brauchst du ein noch nicht verwendetes Verzeichnis `journey-remote.git`.

```bash
$ git init --bare --initial-branch=main ../journey-remote.git
$ git remote add origin ../journey-remote.git
$ git remote -v
```

Der Name `origin` ist eine verbreitete Konvention. Die Liste der Remotes zeigt, welche Adresse dahintersteht.

:::single-choice{#git-remotes-add-address} Du hast git remote add ausgeführt und siehst origin in der Liste. Was hat Git getan?

::option[Einen Namen für das andere Repository gespeichert.]{#git-remotes-add-address-b .correct explanation="In späteren Befehlen kannst du die Adresse als origin angeben."}
::option[Alle lokalen Commits hochgeladen.]{#git-remotes-add-address-a explanation="Beim Hinzufügen eines Remotes wird die Adresse gespeichert. Hochladen geht mit push."}
::option[Einen anderen Arbeitsbaum in dein Projekt geklont.]{#git-remotes-add-address-c explanation="Der vorhandene Arbeitsbaum bleibt an seinem Platz."}
:::

## Einen Branch senden

Mit `git push` sendest du lokale Commits und bittest das Remote, seinen Branch zu aktualisieren. Die Option `-u` speichert den Remote-Branch als Upstream, also als Gegenstück zum lokalen Branch für spätere Befehle.

```bash
$ git push -u origin main
```

Dieser Push geht nur in den separaten Übungsordner. Bei einem gemeinsamen Remote brauchst du eventuell eine Berechtigung. Der Server kann Änderungen auch ablehnen. Prüfe deshalb die Rückmeldung, bevor du einen Push für erfolgreich hältst.

:::single-choice{#git-remotes-push-direction} Welcher Befehl sendet einen neuen lokalen Commit von main an dieses Remote?

::option[git fetch origin]{#git-remotes-push-direction-b explanation="Fetch holt Informationen aus dem Remote in das lokale Repository."}
::option[git remote -v]{#git-remotes-push-direction-c explanation="Der Befehl zeigt, welche Adresse origin verwendet."}
::option[git push origin main]{#git-remotes-push-direction-a .correct explanation="Push überträgt die benötigten Commits und fordert die Aktualisierung des Branches an."}
:::

## Änderungen abrufen

Mit `git fetch origin` aktualisierst du deine lokale Sicht auf den Remote-Verlauf. Ein **Remote-Tracking-Branch** wie `origin/main` hält den zuletzt abgerufenen Stand fest. Du kannst ihn mit `git log --oneline origin/main` ansehen. Fetch allein lässt die ausgecheckten Dateien auf dem aktuellen lokalen Branch.

```bash
$ git fetch origin
$ git log --oneline origin/main
```

:::single-choice{#git-remotes-after-fetch} Nach einem Fetch ist origin/main vorgerückt, dein lokales main aber nicht. Welche Erklärung passt?

::option[Fetch hat die Dateien überschrieben, an denen du gearbeitet hast.]{#git-remotes-after-fetch-a explanation="Fetch aktualisiert die lokale Aufzeichnung des Remote-Branches."}
::option[Git hat die Remote-Änderung abgerufen. Sie zu übernehmen ist ein eigener Schritt.]{#git-remotes-after-fetch-c .correct explanation="Dein lokaler Branch kann seine Position behalten, während origin/main vorrückt."}
::option[Dein Push hat das Remote während des Fetchs aktualisiert.]{#git-remotes-after-fetch-b explanation="Bei einem Fetch werden Informationen empfangen."}
:::

## Zusammenfassung

Du kannst jetzt nachvollziehen, auf welches Repository sich ein Git-Befehl auswirkt.

1. Eine Adresse für ein Remote hinzufügen und prüfen.
2. Einen Branch mit Push senden und seinen Upstream erkennen.
3. Neuen Remote-Verlauf abrufen, ohne die ausgecheckten Dateien zu ändern.
