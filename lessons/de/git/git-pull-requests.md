---
lesson_id: "git-pull-requests"
course_id: "git"
lang: "de"
order_index: 7
title: "Pull Requests"
description: "Lerne, einen Pull Request zu lesen und zu erkennen, was ein Review oder eine automatische Prüfung tatsächlich abdeckt."
meta_title: "Pull Requests – Git"
meta_description: "Sieh dir die Quell- und Ziel-Branches eines Pull Requests an, prüfe den Diff und finde den Commit, für den automatische Ergebnisse gelten."
meta_keywords: "Pull Request, Git, PR, Code-Review, DevOps, Linux Journey"
---

Ein **Pull Request**, kurz PR, schlägt vor, Änderungen aus einem Branch in einen anderen zu übernehmen. Git verwaltet Commits und Branches. Der Hosting-Dienst stellt die Review-Seite, die Diskussion und die Prüfungen für die Änderungen bereit.

## Quell- und Ziel-Branch lesen

Angenommen, jemand aus deinem Team schlägt eine Statusseite für die Website vor. Auf der Review-Seite steht `health-page → main`. Der Quell-Branch, auch **Head** genannt, liefert die vorgeschlagenen Änderungen. Der Ziel-Branch, auch **Base** genannt, würde sie übernehmen.

```text
Source: health-page at 3ab4501
Target: main
Changed file: health.txt
```

Die Review-Seite zeigt zunächst einen Vorschlag. Erst mit dem Merge des PR gelangen die Änderungen in den Ziel-Branch.

:::single-choice{#git-pull-requests-pr-direction} Welcher Branch erhält die Statusseite, wenn der PR gemergt wird?

::option[Ein Branch mit der Commit-ID als Namen.]{#git-pull-requests-pr-direction-a explanation="Dieser Wert bezeichnet einen gespeicherten Stand. Den Ziel-Branch gibt er nicht an."}
::option[Main.]{#git-pull-requests-pr-direction-b .correct explanation="Das Ziel ist main. Dieser Branch übernimmt daher die geprüfte Änderung."}
::option[Health-page.]{#git-pull-requests-pr-direction-c explanation="Health-page ist die Quelle der Änderung."}
:::

## Den Diff prüfen

Öffne die Ansicht der geänderten Dateien und lies den Diff gegenüber dem Ziel-Branch. Eine neue Zeile in `health.txt` passt zur vorgeschlagenen Statusseite. Falls im Review außerdem eine Änderung an `index.html` auftaucht, prüfe, ob sie in denselben PR gehört. Sieh dir die Dateien an, die im PR tatsächlich aufgeführt sind.

:::single-choice{#git-pull-requests-unexpected-file} Ein PR mit dem Titel Add a health page bearbeitet auch die Startseite. Wo prüfst du die genaue Änderung?

::option[Im Diff der geänderten Dateien.]{#git-pull-requests-unexpected-file-a .correct explanation="Im Diff siehst du, welche Zeilen der Vorschlag ändert."}
::option[Nur im Titel.]{#git-pull-requests-unexpected-file-b explanation="Der Titel fasst das Ziel zusammen und kann Einzelheiten auslassen."}
::option[Im Namen des Branches.]{#git-pull-requests-unexpected-file-c explanation="Der Branch-Name steht für eine Entwicklungslinie und beschreibt nicht jede einzelne Änderung."}
:::

## Automatische Prüfergebnisse lesen

Ein Hosting-Dienst kann einen Test ausführen, wenn sich ein PR ändert. Sieh nach, für welchen Commit oder Stand das Ergebnis gilt. Wird nach einer erfolgreichen Prüfung ein weiterer Commit gepusht, vergewissere dich, dass der neue Stand die nötigen Prüfungen durchlaufen hat. Ein grünes Ergebnis zeigt nur, dass die tatsächlich ausgeführten Prüfungen erfolgreich waren.

:::single-choice{#git-pull-requests-changed-revision} Ein Test war für 3ab4501 erfolgreich. Der PR zeigt jetzt auf 78ac900. Was solltest du prüfen, bevor du dich auf das Ergebnis verlässt?

::option[Ob die alte Commit-Nachricht gut formuliert war.]{#git-pull-requests-changed-revision-a explanation="Aus der Nachricht geht nicht hervor, ob der neue Commit geprüft wurde."}
::option[Ob der PR noch denselben Titel hat.]{#git-pull-requests-changed-revision-b explanation="Der Titel kann gleich bleiben, obwohl sich der Code ändert."}
::option[Ob die Prüfungen für den aktualisierten Stand liefen.]{#git-pull-requests-changed-revision-c .correct explanation="Das frühere Ergebnis gehörte zu einem anderen Stand."}
:::

## Zusammenfassung

Du kannst jetzt lesen, was ein Pull Request vorschlägt und welche Belege für einen Merge sprechen.

1. Quell- und Ziel-Branch finden.
2. Vorgeschlagene Änderungen in der Dateiansicht überprüfen.
3. Erkennen, für welchen Stand ein automatisches Ergebnis gilt.
