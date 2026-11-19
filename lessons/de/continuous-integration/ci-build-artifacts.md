---
lesson_id: "ci-build-artifacts"
course_id: "continuous-integration"
lang: "de"
order_index: 6
title: "Build-Artefakte"
description: "Lerne, wie du eine in CI erzeugte Datei ihrem Lauf und ihrer Quellrevision zuordnest."
meta_title: "Build-Artefakte - Kontinuierliche Integration"
meta_description: "Lerne, wie du eine in CI erzeugte Datei ihrem Lauf und ihrer Quellrevision zuordnest."
meta_keywords: "Build-Artefakte, Quellrevision, kontinuierliche Integration, DevOps, Linux Journey"
---

Ein **Build-Artefakt** ist eine Datei oder eine Gruppe von Dateien, die aus einem Lauf zur späteren Verwendung gespeichert wird. Das kann etwa ein Testbericht oder ein Archiv der Website sein. Wenn du Lauf und Revision mit dem Artefakt festhältst, kann jede Person bei der Prüfung nachvollziehen, aus welchen Quelldateien es entstanden ist.

## Den Ausgabeordner verpacken

Verwende den Übungsordner, in dem `dist` die fertige Seite enthält. Dieses Beispiel erstellt ein komprimiertes Archiv, das den gesamten Ordnerinhalt in einer Datei enthält. Ein vorhandenes Archiv mit demselben Namen wird im aktuellen Ordner überschrieben.

```bash
$ tar -czf site.tar.gz -C dist .
$ tar -tzf site.tar.gz
```

Im ersten Befehl erstellt `-c` das Archiv, `-z` komprimiert es und `-f` gibt den Namen der Ausgabedatei an. Mit `-C dist .` beginnt tar in `dist`. Der zweite Befehl listet mit `-t` den Inhalt des Archivs auf. Prüfe vor der Weitergabe, ob `./index.html` enthalten ist.

:::single-choice{#ci-build-artifacts-inspect-archive} Wie prüfst du, ob die Seite im Archiv enthalten ist?

::option[Liste den Inhalt mit tar -tzf site.tar.gz auf.]{#ci-build-artifacts-inspect-archive-b .correct explanation="Die Liste zeigt, ob index.html im Archiv liegt."}
::option[Erstelle das Archiv noch einmal.]{#ci-build-artifacts-inspect-archive-a explanation="Durch das erneute Verpacken siehst du nicht, welche Einträge darin liegen."}
::option[Lies nur den Dateinamen.]{#ci-build-artifacts-inspect-archive-c explanation="Aus dem Namen des Archivs geht sein Inhalt nicht hervor."}
:::

![Ausgabe von tar, in der index.html im Archiv site.tar.gz aufgeführt ist](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/continuous-integration/ci-build-artifacts/archive-contents.png)

## Ein Artefakt seinem Lauf zuordnen

Ein Workflow kann das fertige Archiv hochladen. Auf der Seite des Laufs steht, welche Revision gebaut wurde. Zwei Artefakte namens `site.tar.gz` können sich unterscheiden, wenn sie aus verschiedenen Revisionen stammen. Berücksichtige bei der Auswahl des Downloads sowohl den Lauf als auch die Revision.

:::single-choice{#ci-build-artifacts-choose-run} Die Läufe 41 und 42 enthalten site.tar.gz. Wo findest du das Paket für die Revision, die du geprüft hast?

::option[Beim ersten Download namens site.tar.gz.]{#ci-build-artifacts-choose-run-b explanation="Der Name verrät nicht, aus welchem Quellstand die Datei stammt."}
::option[Beim letzten erfolgreichen Lauf, unabhängig von seiner Revision.]{#ci-build-artifacts-choose-run-c explanation="Ein späterer Lauf kann mit einem anderen Quellstand erfolgreich sein. Suche nach der Revision, die du verwenden willst."}
::option[Beim Lauf, dessen angegebene Revision mit der geprüften Revision übereinstimmt.]{#ci-build-artifacts-choose-run-a .correct explanation="Mehrere Läufe können denselben Dateinamen verwenden."}
:::

## Ein Archiv von einem Container-Image unterscheiden

Ein Website-Archiv enthält Dateien, die du entpacken kannst. Ein Container-Image bringt das Dateisystem und die Einstellungen mit, die Docker zum Starten eines Containers verwendet. Ein Workflow kann ein Image in einer Registry veröffentlichen. Wenn später ein Container daraus gestartet werden soll, halte die Image-Referenz zusammen mit der Quellrevision fest.

:::single-choice{#ci-build-artifacts-deployable-type} Die nächste Phase soll einen Container aus einer Registry starten. Auf welche Ausgabe sollte sie verweisen?

::option[Auf einen heruntergeladenen Testbericht des Laufs.]{#ci-build-artifacts-deployable-type-a explanation="Ein Bericht enthält Testergebnisse, aber kein Container-Dateisystem."}
::option[Auf die Referenz des veröffentlichten Container-Images.]{#ci-build-artifacts-deployable-type-c .correct explanation="Mit dieser Referenz kann Docker das vorbereitete Image abrufen."}
::option[Auf den Dateinamen des Website-Archivs.]{#ci-build-artifacts-deployable-type-b explanation="Das Archiv enthält die Seitendateien und bezeichnet kein Image in einer Registry."}
:::

## Zusammenfassung

Du kannst jetzt ein Build-Artefakt erkennen und seine Herkunft nachvollziehen.

1. Verpacke die Ausgabedateien und prüfe den Inhalt des Archivs.
2. Prüfe, aus welchem Lauf und welcher Quellrevision das Artefakt stammt.
3. Wähle ein Datei-Artefakt oder ein Container-Image, je nachdem, was der nächste Schritt braucht.
