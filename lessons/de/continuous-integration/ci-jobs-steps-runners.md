---
lesson_id: "ci-jobs-steps-runners"
course_id: "continuous-integration"
lang: "de"
order_index: 3
title: "Jobs, Schritte und Runner"
description: "Lerne, Jobs, Schritte und Runner in einem kurzen GitHub-Actions-Workflow zu erkennen."
meta_title: "Jobs, Schritte und Runner - Kontinuierliche Integration"
meta_description: "Lerne, Jobs, Schritte und Runner in einem kurzen GitHub-Actions-Workflow zu erkennen."
meta_keywords: "Jobs, Schritte, Runner, kontinuierliche Integration, DevOps, Linux Journey"
---

Ein Workflow ist der gesamte automatisierte Ablauf. Ein **Job** bündelt Aufgaben für einen **Runner**. Das ist der Rechner oder die Umgebung, die den Job ausführt. Ein **Schritt** ist eine einzelne Aktion innerhalb eines Jobs.

## Einen kurzen Workflow lesen

In diesem Beispiel läuft ein Job auf einem von GitHub gehosteten Ubuntu-Runner. Solche Workflows liegen im GitHub-Repository unter `.github/workflows/`.

```yaml
name: Page check
on: push
jobs:
  check:
    runs-on: ubuntu-latest
    steps:
      - name: Get the repository
        uses: actions/checkout@v6
      - name: Find the heading
        run: grep -q '<h1>Welcome</h1>' index.html
```

Die Job-ID lautet `check`. Das Feld `runs-on` wählt die Umgebung aus. Mit `uses` wird eine wiederverwendbare Action aufgerufen. Hier stellt sie die Dateien des Repositorys bereit. Mit `run` führst du einen Befehl auf dem Runner aus.

:::single-choice{#ci-jobs-steps-runners-job-fields} Welches Feld legt fest, wo der Job check läuft?

::option[runs-on.]{#ci-jobs-steps-runners-job-fields-a .correct explanation="Es legt den Runner-Typ für den Job fest."}
::option[uses.]{#ci-jobs-steps-runners-job-fields-b explanation="Dieser Schritt ruft die Checkout-Action auf."}
::option[name.]{#ci-jobs-steps-runners-job-fields-c explanation="Das Feld gibt dem Workflow einen Namen."}
:::

## Die Schritte nachvollziehen

Die Schritte eines Jobs laufen standardmäßig in der angegebenen Reihenfolge. Die Prüfung liest eine Datei aus dem Repository. Deshalb kommt der Checkout zuerst. Ein späterer Schritt desselben Jobs kann Dateien verwenden, die ein früherer Schritt geschrieben hat.

:::single-choice{#ci-jobs-steps-runners-step-order} Was würde dem grep-Schritt auf einem frischen Runner fehlen, wenn der Checkout erst danach käme?

::option[Der Name des Jobs.]{#ci-jobs-steps-runners-step-order-a explanation="Der Workflow hat den Job bereits ausgewählt."}
::option[Der Ubuntu-Runner selbst.]{#ci-jobs-steps-runners-step-order-c explanation="Der Runner wird ausgewählt, bevor die Schritte beginnen."}
::option[Die Projektdatei, die der Schritt lesen soll.]{#ci-jobs-steps-runners-step-order-b .correct explanation="Der Checkout stellt die Repository-Dateien vor der Prüfung bereit."}
:::

## Die getrennten Umgebungen der Jobs beachten

Verschiedene Jobs können gleichzeitig laufen. Jeder von GitHub gehostete Job erhält einen eigenen Runner. Daher ist eine Datei aus einem Job in einem anderen erst verfügbar, wenn der Workflow sie überträgt. Wenn ein Job erst nach einem anderen erfolgreich abgeschlossenen Job starten soll, gib die Abhängigkeit mit `needs` an. Falls dabei Dateien übertragen werden müssen, nutze ein Artefakt.

:::single-choice{#ci-jobs-steps-runners-separate-jobs} Ein Build-Job schreibt site.tar.gz. Ein späterer Job läuft auf einem anderen gehosteten Runner. Wie sollte er die Datei erhalten?

::option[Davon ausgehen, dass sie im selben Arbeitsverzeichnis liegt.]{#ci-jobs-steps-runners-separate-jobs-a explanation="Ein eigener gehosteter Runner hat ein eigenes Dateisystem."}
::option[Die Datei als Artefakt übertragen.]{#ci-jobs-steps-runners-separate-jobs-c .correct explanation="Der Workflow kann sie in einem Job hochladen und im anderen herunterladen."}
::option[Needs setzen, damit der zweite Job auf den Build wartet.]{#ci-jobs-steps-runners-separate-jobs-b explanation="Needs legt die Reihenfolge fest. Die Build-Datei musst du trotzdem zwischen den Runnern übertragen."}
:::

Wenn du einen Workflow in einem GitHub-Repository schreiben und ausführen möchtest, probiere [GitHub Actions für Einsteiger](https://labex.io/courses/github-actions-for-beginners) aus. Für diesen Übungskurs brauchst du ein GitHub-Konto.

## Zusammenfassung

Du kannst jetzt die wichtigsten Teile eines CI-Workflows lesen.

1. Finde einen Job und den zugehörigen Runner.
2. Erkenne eine wiederverwendbare Action und einen Shell-Schritt.
3. Erkenne, wann Jobs eine Abhängigkeit oder eine Dateiübertragung benötigen.
