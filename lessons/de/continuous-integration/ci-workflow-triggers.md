---
lesson_id: "ci-workflow-triggers"
course_id: "continuous-integration"
lang: "de"
order_index: 2
title: "Workflow-Auslöser"
description: "Lerne, anhand von Ereignissen und Branch-Filtern vorherzusagen, wann ein GitHub-Actions-Workflow läuft."
meta_title: "Workflow-Auslöser - Kontinuierliche Integration"
meta_description: "Lerne, anhand von Ereignissen und Branch-Filtern vorherzusagen, wann ein GitHub-Actions-Workflow läuft."
meta_keywords: "Workflow-Auslöser, Branch-Filter, kontinuierliche Integration, DevOps, Linux Journey"
---

Ein Workflow beginnt mit einem Auslöser. In GitHub Actions steht unter `on`, welche Ereignisse ihn starten können. Ein **Ereignis** kann beispielsweise ein Push auf einen Branch, eine Änderung an einem Pull Request oder eine andere unterstützte Aktion sein.

## Einen Push auswerten

Lies diesen Ausschnitt eines Workflows. Die Einrückung in YAML zeigt, dass `branches` eine Einstellung für `push` ist.

```yaml
on:
  push:
    branches:
      - main
```

Dieser Workflow läuft, wenn ein Commit auf den Branch `main` gepusht wird, sofern der Workflow aktiviert ist und die übrigen Voraussetzungen erfüllt sind. Wenn du im lokalen Terminal einen Commit erstellst, ist er noch nicht auf GitHub. Dieser Ausschnitt reagiert auf den anschließenden Push.

:::single-choice{#ci-workflow-triggers-push-filter} Welche Aktion entspricht diesem Push-Auslöser?

::option[Du erstellst lokal einen Commit auf main.]{#ci-workflow-triggers-push-filter-a explanation="Der Auslöser reagiert auf ein Ereignis im Repository auf GitHub."}
::option[Du pushst einen Commit auf den Branch draft.]{#ci-workflow-triggers-push-filter-b explanation="Der Branch-Filter wählt main aus."}
::option[Du pushst den Commit auf main.]{#ci-workflow-triggers-push-filter-c .correct explanation="Das Ereignis passt zu push und zum Branch-Filter."}
:::

## Einen Pull Request auswerten

Ein weiteres Ereignis kann vorgeschlagene Änderungen vor dem Merge erfassen. In diesem Ausschnitt bezieht sich der Branch-Filter auf den Ziel-Branch des Pull Requests.

```yaml
on:
  pull_request:
    branches:
      - main
```

Ein Vorschlag aus `health-page` für `main` entspricht diesem Filter. Mit den Standardeinstellungen kann der Workflow zum Beispiel beim Öffnen des Pull Requests oder beim Push eines weiteren Commits auf seinen Quell-Branch starten.

:::single-choice{#ci-workflow-triggers-pr-target} Ein Pull Request soll notes in main übernehmen. Welcher Name ist für den Branch-Filter maßgeblich?

::option[Notes, der Quell-Branch.]{#ci-workflow-triggers-pr-target-b explanation="Notes enthält die vorgeschlagenen Änderungen."}
::option[Main, der Ziel-Branch.]{#ci-workflow-triggers-pr-target-a .correct explanation="Der Filter für einen Pull Request bezieht sich auf den Branch, der die Änderungen aufnehmen soll."}
::option[Der Dateiname, den der Vorschlag betrifft.]{#ci-workflow-triggers-pr-target-c explanation="Dieser Ausschnitt filtert nach Branch-Namen."}
:::

## Mehrere Auslöser lesen

Eine Datei kann beide Ereignisse unter demselben Schlüssel `on` aufführen. Der Lauf für einen Pull Request kann die vorgeschlagene Zusammenführung prüfen. Wenn ein Merge danach `main` aktualisiert, kann ein Push-Lauf den neuen Stand dieses Branches prüfen. Jedes Ergebnis gehört zum Ereignis und zur Revision, die im jeweiligen Lauf angezeigt werden.

:::single-choice{#ci-workflow-triggers-after-merge} Ein Workflow enthält die beiden Auslöser aus den Beispielen. Ein Merge aktualisiert main. Welches der aufgeführten Ereignisse passt dazu?

::option[Ein Push auf main.]{#ci-workflow-triggers-after-merge-b .correct explanation="Der aktualisierte Ziel-Branch entspricht dem Push-Filter."}
::option[Ein Pull Request, der auf einem neuen Branch geöffnet wird.]{#ci-workflow-triggers-after-merge-a explanation="Das beschriebene Ereignis ist die Aktualisierung von main nach dem Merge."}
::option[Ein lokaler Commit ohne Aktualisierung auf GitHub.]{#ci-workflow-triggers-after-merge-c explanation="Main hat sich in diesem Beispiel bereits auf GitHub geändert."}
:::

## Zusammenfassung

Du kannst jetzt ein Repository-Ereignis einem Workflow-Auslöser zuordnen.

1. Lies ein Push-Ereignis und den zugehörigen Branch-Filter.
2. Ermittle den Ziel-Branch, auf den der Pull-Request-Filter angewendet wird.
3. Ordne ein Workflow-Ergebnis seinem auslösenden Ereignis zu.
