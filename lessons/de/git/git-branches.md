---
lesson_id: "git-branches"
course_id: "git"
lang: "de"
order_index: 5
title: "Branches"
description: "Lerne, wie Git-Branches verschiedene Entwicklungsstände bezeichnen und wie ein Merge Änderungen in main übernimmt."
meta_title: "Branches – Git"
meta_description: "Arbeite in einem eigenen Branch, speichere dort eine Änderung und übernimm sie per Merge in main."
meta_keywords: "Git-Branches, git switch, git merge, Fast-Forward, DevOps, Linux Journey"
---

Ein **Branch** ist ein Name, der auf einen Commit zeigt. Sobald du auf dem aktuellen Branch einen Commit erstellst, zeigt er auf den neuen Eintrag. Andere Branches behalten ihre Position, bis du sie aktualisierst.

## In einem eigenen Branch weiterarbeiten

Erstelle im Übungsrepository ausgehend von `main` einen Branch namens `health-page` und wechsle zu ihm. Bei `git switch` steht die Option `-c` für das Anlegen eines Branches.

```bash
$ git switch -c health-page
```

Zunächst zeigen beide Namen auf denselben Commit. Mit `git branch --show-current` prüfst du, welcher Branch beim nächsten Commit vorrückt.

:::single-choice{#git-branches-start-pointer} Worauf zeigt der neue Branch direkt nach git switch -c health-page?

::option[Auf einen leeren Commit, den der Befehl erstellt hat.]{#git-branches-start-pointer-a explanation="Der Befehl erstellt einen Namen für einen bereits vorhandenen Commit."}
::option[Auf einen Commit im Repository einer anderen Person.]{#git-branches-start-pointer-c explanation="Der Befehl legt einen lokalen Branch in deinem aktuellen Repository an."}
::option[Auf den Commit, von dem du ausgegangen bist.]{#git-branches-start-pointer-b .correct explanation="Zunächst zeigen beide Branches auf denselben Stand."}
:::

## Eine Änderung auf dem Branch speichern

Füge eine einzeilige Statusdatei hinzu und erstelle den Commit, während `health-page` der aktuelle Branch ist.

```bash
$ printf '%s\n' ready > health.txt
$ git add health.txt
$ git commit -m "Add a health page"
```

Nennen wir den Startseiten-Commit A und den Statusseiten-Commit B.

```text
A (main) --- B (health-page)
```

Nur `health-page` ist zu B vorgerückt. Wechselst du mit einem sauberen Arbeitsbaum zu `main` zurück, entsprechen deine Dateien wieder dem Stand von A.

:::single-choice{#git-branches-branch-snapshot} Welcher Branch enthält vor dem Merge den Commit der Statusseite?

::option[Beide, weil sie zum gleichen Repository gehören.]{#git-branches-branch-snapshot-a explanation="Branches im selben Repository können auf unterschiedliche Stände zeigen."}
::option[Nur health-page.]{#git-branches-branch-snapshot-c .correct explanation="Dieser Branch war aktuell, als Commit B erstellt wurde."}
::option[Nur main, weil der Branch dort begonnen hat.]{#git-branches-branch-snapshot-b explanation="Main hat sich beim Commit auf health-page nicht verändert."}
:::

## Änderungen in main übernehmen

Wechsle zu dem Branch, der die Änderung übernehmen soll. Gib beim Merge den Branch an, aus dem die Änderung kommt.

```bash
$ git switch main
$ git merge health-page
```

Hier hat `main` seit A keine eigenen neuen Commits. Git kann ihn direkt zu B verschieben. Das nennt sich **Fast-Forward**. Haben beide Branches neue Commits, muss Git die Änderungen möglicherweise zusammenführen. Prüfe die Ausgabe, bevor du davon ausgehst, dass der Merge abgeschlossen ist.

:::single-choice{#git-branches-merge-direction} Main soll die Änderung von health-page übernehmen. Wo führst du den Merge aus?

::option[Auf main, mit health-page als Quelle.]{#git-branches-merge-direction-a .correct explanation="Das Ergebnis des Merge landet im aktuellen Branch."}
::option[Auf health-page, mit main als Quelle.]{#git-branches-merge-direction-b explanation="Dieser Befehl würde health-page aktualisieren."}
::option[Auf einem neuen Branch, den keine Seite verwendet.]{#git-branches-merge-direction-c explanation="Main behält seine Position, bis er die Änderung übernimmt."}
:::

## Zusammenfassung

Du kannst jetzt nachvollziehen, wie eine Änderung aus einem lokalen Branch in main gelangt.

1. Einen Branch ausgehend vom aktuellen Commit erstellen.
2. Eine Änderung auf dem vorgesehenen Branch speichern.
3. Die Änderung in den Branch übernehmen, der sie erhalten soll.
