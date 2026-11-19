---
lesson_id: "ci-workflow-logs"
course_id: "continuous-integration"
lang: "de"
order_index: 5
title: "Workflow-Protokolle"
description: "Lerne, einen fehlgeschlagenen Workflow-Schritt zu finden und die erste hilfreiche Fehlermeldung zu lesen."
meta_title: "Workflow-Protokolle - Kontinuierliche Integration"
meta_description: "Lerne, einen fehlgeschlagenen Workflow-Schritt zu finden und die erste hilfreiche Fehlermeldung zu lesen."
meta_keywords: "Workflow-Protokolle, Fehleranalyse, kontinuierliche Integration, DevOps, Linux Journey"
---

Das Workflow-Ergebnis zeigt den Gesamtstatus. Um einen Fehler zu verstehen, klappe den fehlgeschlagenen Job auf und lies seine Schritte der Reihe nach. Ein späterer Schritt kann übersprungen werden, wenn ein früherer nicht erfolgreich abgeschlossen wurde.

## Den ersten Fehler finden

Dieser simulierte Lauf zeigt den Status jedes Schritts im Job zur Seitenprüfung.

```text
Prepare: passed
Build page: failed
Check heading: skipped
Package site: skipped
```

Beginne mit `Build page`. Die übersprungenen Prüfungen liefern kein Ergebnis für die Seite. Wenn der Fehler behoben ist, überprüfe die späteren Schritte in einem neuen Lauf.

:::single-choice{#ci-workflow-logs-first-failure} Die Ausgabe welches Schritts solltest du zuerst lesen?

::option[Package site, weil er ganz unten steht.]{#ci-workflow-logs-first-failure-a explanation="Der Befehl zum Verpacken wurde in diesem Lauf übersprungen."}
::option[Check heading, weil der Workflow für eine Seite gedacht ist.]{#ci-workflow-logs-first-failure-c explanation="Laut Status wurde die Überschriftenprüfung nicht ausgeführt."}
::option[Build page, weil er zuerst fehlgeschlagen ist.]{#ci-workflow-logs-first-failure-b .correct explanation="Sein Protokoll zeigt, warum die folgenden Schritte übersprungen wurden."}
:::

![Simulierter CI-Lauf mit einem fehlgeschlagenen Build und übersprungenen Folgeschritten](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/continuous-integration/ci-workflow-logs/skipped-steps.png)

## Der Fehlermeldung folgen

Der fehlgeschlagene Schritt zeigt diese Zeilen.

```text
Run cp index.html dist/index.html
cp: cannot create regular file 'dist/index.html': No such file or directory
Process completed with exit code 1.
```

Die Meldung nennt den Zielpfad. Fehlt das übergeordnete Verzeichnis `dist`, kann der Kopierbefehl darin keine Datei anlegen. Prüfe, ob ein früherer Befehl das Verzeichnis vor dem Kopieren erstellt hat. Exitcode 1 zeigt, dass der Befehl fehlgeschlagen ist. Aus der Meldung erfährst du, wo du nachsehen solltest.

:::single-choice{#ci-workflow-logs-actionable-log} Dist fehlt. Welche Änderung behebt das gemeldete Problem?

::option[Ändere die Überschrift, die grep prüft.]{#ci-workflow-logs-actionable-log-b explanation="Die Überschriftenprüfung lief gar nicht. Ob der Text passt, ist deshalb noch offen."}
::option[Erstelle dist vor dem Kopieren.]{#ci-workflow-logs-actionable-log-a .correct explanation="Damit die Zieldatei erstellt werden kann, muss das übergeordnete Verzeichnis existieren."}
::option[Lade ein Artefakt aus dem übersprungenen Schritt herunter.]{#ci-workflow-logs-actionable-log-c explanation="Der Schritt zum Verpacken hat hier kein Artefakt erzeugt."}
:::

## Einen neuen Lauf prüfen

Vergleiche nach der Korrektur die Revision und den Status der Schritte im neuen Lauf. Wenn das Kopieren klappt, wurde die Ausgabedatei erstellt. Prüfe auch die Ergebnisse des Tests und der Paketerstellung, bevor du den gesamten Ablauf als erfolgreich einstufst. Wenn du einen Fehler meldest, gib die erste hilfreiche Meldung und den Namen des Schritts an.

:::single-choice{#ci-workflow-logs-rerun-evidence} Im neuen Lauf war Build page erfolgreich, aber Check heading schlug fehl. Was hat sich geändert?

::option[Der Build war erfolgreich. Jetzt gibt es ein Ergebnis der Überschriftenprüfung, das du untersuchen kannst.]{#ci-workflow-logs-rerun-evidence-c .correct explanation="Der erste verbliebene Fehler liegt jetzt im Testschritt."}
::option[Der neue Lauf spielt keine Rolle, weil der alte Build fehlgeschlagen ist.]{#ci-workflow-logs-rerun-evidence-a explanation="Jeder Lauf liefert Ergebnisse für seine eigene Revision."}
::option[Die Paketerstellung muss erfolgreich gewesen sein, weil der Build erfolgreich war.]{#ci-workflow-logs-rerun-evidence-b explanation="Ein späterer Schritt kann noch immer fehlschlagen oder übersprungen werden."}
:::

## Zusammenfassung

Du kannst jetzt einen Workflow-Fehler im Zusammenhang mit den übrigen Schritten lesen.

1. Finde den ersten ausgeführten Schritt, der fehlgeschlagen ist.
2. Nutze die Protokollzeile, um zu entscheiden, was du untersuchst.
3. Prüfe nach einer Korrektur die neue Revision und die späteren Schritte.
