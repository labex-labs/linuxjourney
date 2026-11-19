---
lesson_id: "ci-builds-and-tests"
course_id: "continuous-integration"
lang: "de"
order_index: 4
title: "Builds und Tests"
description: "Lerne bei einem kleinen lokalen Seitentest, wie du Vorbereitung, Build und Test unterscheidest."
meta_title: "Builds und Tests - Kontinuierliche Integration"
meta_description: "Lerne bei einem kleinen lokalen Seitentest, wie du Vorbereitung, Build und Test unterscheidest."
meta_keywords: "Builds und Tests, Exitcode, kontinuierliche Integration, DevOps, Linux Journey"
---

Eine fehlgeschlagene Prüfung lässt sich leichter einordnen, wenn jede Phase eine klare Aufgabe hat. Die **Vorbereitung** stellt Eingabedateien und Werkzeuge bereit. Ein **Build** erzeugt eine Ausgabe. Ein **Test** prüft, ob die Quelle oder die Ausgabe eine Erwartung erfüllt.

## Die Eingabedatei vorbereiten

Erstelle in einem leeren Übungsordner eine Beispielseite. Die Umleitung überschreibt eine vorhandene Datei namens `index.html`. Verwende deshalb einen neuen Übungsordner.

```bash
$ printf '%s\n' '<h1>Welcome</h1>' > index.html
```

In einem CI-Job würde der Checkout die Seite bereitstellen. Bei manchen Projekten werden zusätzlich Abhängigkeiten installiert, also Bibliotheken oder Werkzeuge, die der Build oder die Tests benötigen.

:::single-choice{#ci-builds-and-tests-prepare-input} Die Seite fehlt schon vor dem Kopierbefehl. Welche Phase solltest du zuerst untersuchen?

::option[Den Download des Artefakts in einem späteren Job.]{#ci-builds-and-tests-prepare-input-a explanation="Die Eingabedatei wird bereits benötigt, bevor die Ausgabe erzeugt werden kann."}
::option[Die Vorbereitung.]{#ci-builds-and-tests-prepare-input-b .correct explanation="Die Eingabedatei hätte in diesem Job bereitgestellt werden sollen."}
::option[Die Antwortzeit im Produktivbetrieb.]{#ci-builds-and-tests-prepare-input-c explanation="Hier geht es um Dateien auf dem Runner."}
:::

## Die Build-Ausgabe erzeugen

Kopiere die Seite in den Ordner, der die fertige Website enthält.

```bash
$ mkdir -p dist
$ cp index.html dist/index.html
```

Mit der Option `-p` gelingt `mkdir` auch, wenn der Ordner bereits existiert. Beim Kopieren entsteht eine eigene Datei im Ausgabeordner. Spätere Tests können diese Ausgabe prüfen.

:::single-choice{#ci-builds-and-tests-build-product} Welche Datei kannst du nach erfolgreichem Kopieren in ein Paket aufnehmen?

::option[dist/index.html.]{#ci-builds-and-tests-build-product-a .correct explanation="Der Build hat eine Kopie im Ausgabeordner abgelegt."}
::option[Die bereitgestellte Seite auf der öffentlichen Website.]{#ci-builds-and-tests-build-product-b explanation="Das lokale Kopieren startet keinen öffentlich erreichbaren Dienst."}
::option[Einen Statuseintrag des Workflows.]{#ci-builds-and-tests-build-product-c explanation="Der Build liefert hier eine Seite. Der Runner erfasst den Prüfstatus separat."}
:::

## Die Seite testen

Führe diese Prüfung direkt nach dem Build aus. Die Option `-F` sucht nach dem wörtlichen Text. Mit `-q` gibt der Befehl keine Treffer aus. Die Shell speichert den Exitcode des letzten Befehls in `$?`. Null bedeutet, dass der Text gefunden wurde. Eins bedeutet, dass keine Zeile dazu passte.

```bash
$ grep -Fq '<h1>Welcome</h1>' dist/index.html
$ echo "$?"
```

Erwarte `0`. Der Test hat nach dem exakten Text in der erzeugten Datei gesucht. Farben, Darstellung im Browser und Antwortzeit wurden dabei nicht geprüft.

:::single-choice{#ci-builds-and-tests-test-scope} Der Test ist erfolgreich. Welche Schlussfolgerung kannst du ziehen?

::option[Die Seite ist über das Internet erreichbar.]{#ci-builds-and-tests-test-scope-a explanation="Die Prüfung hat eine lokale Ausgabedatei gelesen."}
::option[Die Seite wird in jedem unterstützten Browser dargestellt.]{#ci-builds-and-tests-test-scope-b explanation="Bei diesem Test wurde kein Browser verwendet."}
::option[Die erzeugte Datei enthält den erwarteten Text der Überschrift.]{#ci-builds-and-tests-test-scope-c .correct explanation="Genau diese Bedingung hat der grep-Befehl geprüft."}
:::

![Erfolgreiche lokale Prüfung der Überschrift mit Exitcode null in der LabEx-Shell](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/continuous-integration/ci-builds-and-tests/heading-check.png)

## Zusammenfassung

Du kannst jetzt einordnen, was die einzelnen Phasen einer kleinen CI-Prüfung belegen.

1. Stelle die Eingabedatei bereit, bevor du den Build ausführst.
2. Ermittle, welche Datei der Build erzeugt.
3. Lies den Exitcode und prüfe, welche Bedingung der Test tatsächlich abdeckt.
