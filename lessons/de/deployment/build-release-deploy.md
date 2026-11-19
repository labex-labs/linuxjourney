---
lesson_id: "build-release-deploy"
course_id: "deployment"
lang: "de"
order_index: 1
title: "Build, Release und Deployment"
description: "Lerne, wie du eine Quellrevision anhand ihrer Build-, Release- und Deployment-Einträge verfolgst."
meta_title: "Build, Release und Deployment - Bereitstellung"
meta_description: "Lerne, wie du eine Quellrevision anhand ihrer Build-, Release- und Deployment-Einträge verfolgst."
meta_keywords: "Build, Release, Deployment, Bereitstellung, DevOps, Linux Journey"
---

Jemand im Team sagt, Version 2 sei fertig. Vielleicht wurden die Dateien bereits gebaut, vielleicht wurde die Version freigegeben, oder die Besucher können schon darauf zugreifen. An den Einträgen erkennst du, welche Phase erreicht ist.

## Den Build zuordnen

Ein Build erzeugt aus einer bestimmten Quellrevision eine Ausgabe. In diesem Beispiel wird eine kleine Website als Container-Image verpackt und in einer Image-Registry gespeichert. Halte neben der Referenz des erzeugten Images auch den Quell-Commit fest.

```text
Build 81
Source commit: 3ab4501
Image: registry.example/journey/site:2
Result: succeeded
```

Dieser Eintrag zeigt, was erzeugt wurde. Die Website kann zu diesem Zeitpunkt noch eine ältere Version ausliefern.

:::single-choice{#build-release-deploy-build-record} Welcher Eintrag verbindet das verpackte Image mit der Quellrevision?

::option[Ein Lesezeichen im Browser.]{#build-release-deploy-build-record-b explanation="Ein Lesezeichen enthält eine Adresse. Daraus geht nicht hervor, wie die Dateien gebaut wurden."}
::option[Build 81.]{#build-release-deploy-build-record-a .correct explanation="Der Eintrag nennt den Quell-Commit und das daraus erzeugte Image."}
::option[Der Name des neuesten lokalen Branches.]{#build-release-deploy-build-record-c explanation="Ein Branch-Name kann auf andere Commits zeigen und identifiziert diesen Build nicht eindeutig."}
:::

## Den Release-Eintrag lesen

Ein **Release** bezeichnet eine zur Verteilung freigegebene Version. Ein Release-Eintrag kann zum Beispiel genau das Image aus Build 81 für die Staging-Umgebung freigeben. Nach der Freigabe kannst du so auf dasselbe Artefakt verweisen, ohne eine neue Kopie zu bauen.

:::single-choice{#build-release-deploy-release-record} Release 2 ist für Staging freigegeben. Was belegt das?

::option[Das eingetragene Artefakt wurde für diesen Einsatz freigegeben.]{#build-release-deploy-release-record-b .correct explanation="Im Release-Eintrag steht, welches Artefakt in Staging verwendet werden darf."}
::option[In jeder Umgebung wird schon Version 2 ausgeliefert.]{#build-release-deploy-release-record-a explanation="Die Freigabe erlaubt den nächsten Schritt. Welche Version tatsächlich läuft, lässt sich daraus nicht ablesen."}
::option[Version 2 erhält mehr Anfragen.]{#build-release-deploy-release-record-c explanation="Ein Release-Eintrag misst keinen Datenverkehr."}
:::

## Die bereitgestellte Version ermitteln

Ein **Deployment** bringt eine bestimmte Version in eine Umgebung und startet oder aktualisiert dort die Anwendung. Eine Umgebung wie Staging oder Produktion hat eigene Einstellungen und Ressourcen. Eine erfolgreiche Anfrage an einen Versionsendpunkt hilft dir zu prüfen, welche Version dort antwortet.

```text
Staging version response: 2
Production version response: 1
```

In diesem Beispiel antwortet in Staging die neue Version, während die Produktion weiterhin mit Version 1 antwortet.

:::single-choice{#build-release-deploy-running-version} Wie kannst du direkt prüfen, ob Version 2 in Produktion ausgeliefert wird?

::option[Mit einer zweiten Antwort aus Staging, die Version 2 anzeigt.]{#build-release-deploy-running-version-a explanation="Damit prüfst du weiterhin nur Staging."}
::option[Mit der Freigabemeldung des Releases.]{#build-release-deploy-running-version-b explanation="Die Freigabe prüft den laufenden Dienst nicht."}
::option[Mit einer Versionsantwort von der Produktionsadresse.]{#build-release-deploy-running-version-c .correct explanation="Damit prüfst du genau die Umgebung, um die es geht."}
:::

## Zusammenfassung

Du kannst jetzt die Einträge unterscheiden, die auf dem Weg zur Bereitstellung entstehen.

1. Ordne die Build-Ausgabe ihrem Quellstand zu.
2. Ermittle das Artefakt, das in einem Release freigegeben wurde.
3. Prüfe, welche Version in der vorgesehenen Umgebung antwortet.
