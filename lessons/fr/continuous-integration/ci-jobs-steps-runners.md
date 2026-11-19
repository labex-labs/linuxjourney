---
lesson_id: "ci-jobs-steps-runners"
course_id: "continuous-integration"
lang: "fr"
order_index: 3
title: "Jobs, étapes et runners"
description: "Apprenez à repérer les jobs, les étapes et le runner dans un court fichier GitHub Actions."
meta_title: "Jobs, étapes et runners - Intégration continue"
meta_description: "Apprenez à repérer les jobs, les étapes et le runner dans un court fichier GitHub Actions."
meta_keywords: "jobs, étapes, runners, GitHub Actions, intégration continue, DevOps, Linux Journey"
---

Un workflow est l’ensemble du processus automatisé. Un **job** regroupe des tâches confiées à un **runner**, c’est-à-dire la machine ou l’environnement qui les exécute. Une **étape** est une opération à l’intérieur d’un job.

## Lire un petit workflow

Cet exemple exécute un job sur un runner Ubuntu hébergé par GitHub. Ce type de workflow se trouve dans `.github/workflows/` dans un dépôt GitHub.

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

L’identifiant du job est `check`. Le champ `runs-on` sélectionne l’environnement d’exécution. `uses` invoque une action réutilisable, ici pour rendre les fichiers du dépôt disponibles. `run` exécute une commande sur le runner.

:::single-choice{#ci-jobs-steps-runners-job-fields} Quel champ détermine où le job check s’exécute ?

::option[runs-on.]{#ci-jobs-steps-runners-job-fields-a .correct explanation="Ce champ indique le type de runner du job."}
::option[uses.]{#ci-jobs-steps-runners-job-fields-b explanation="Cette étape lance l’action de checkout."}
::option[name.]{#ci-jobs-steps-runners-job-fields-c explanation="Ce champ donne un nom au workflow."}
:::

## Suivre les étapes

Par défaut, les étapes d’un job s’exécutent dans l’ordre indiqué. La vérification lit un fichier du dépôt, ce qui exige de récupérer les fichiers avec le checkout au préalable. Au sein du même job, une étape peut réutiliser des fichiers écrits par une étape précédente.

:::single-choice{#ci-jobs-steps-runners-step-order} Que manquerait-il à l’étape grep sur un runner neuf si le checkout était déplacé après elle ?

::option[Le nom du job.]{#ci-jobs-steps-runners-step-order-a explanation="Le workflow a déjà sélectionné le job."}
::option[Le runner Ubuntu lui-même.]{#ci-jobs-steps-runners-step-order-c explanation="Le runner est sélectionné avant l’exécution des étapes."}
::option[Le fichier du projet qu’elle doit lire.]{#ci-jobs-steps-runners-step-order-b .correct explanation="Le checkout fournit les fichiers du dépôt avant la vérification."}
:::

## Séparer les jobs

Des jobs distincts peuvent tourner en même temps. Chaque job exécuté par GitHub dispose de son propre runner. Un fichier créé dans un job doit être transféré par le workflow pour être utilisable dans un autre. Lorsqu’un job exige la réussite d’un autre, déclarez la dépendance avec `needs`. Pour transférer des fichiers si nécessaire, utilisez un artefact.

:::single-choice{#ci-jobs-steps-runners-separate-jobs} Un job de build écrit site.tar.gz. Un job suivant tourne sur un autre runner hébergé. Comment doit-il récupérer le fichier ?

::option[En supposant qu’il se trouve dans le même répertoire de travail.]{#ci-jobs-steps-runners-separate-jobs-a explanation="Un runner hébergé distinct démarre avec son propre système de fichiers."}
::option[En transférant le fichier sous forme d’artefact.]{#ci-jobs-steps-runners-separate-jobs-c .correct explanation="Le workflow peut le téléverser dans un job et le télécharger dans l’autre."}
::option[En définissant needs pour que le deuxième job attende le build.]{#ci-jobs-steps-runners-separate-jobs-b explanation="Needs règle l’ordre des jobs. Le fichier doit tout de même être transféré entre les runners."}
:::

Pour rédiger et exécuter un workflow dans un dépôt GitHub, essayez [GitHub Actions pour débutants](https://labex.io/courses/github-actions-for-beginners). Ce cours pratique nécessite un compte GitHub.

## Résumé

Vous savez maintenant lire les grandes parties d’un workflow de CI.

1. Repérez un job et son runner.
2. Distinguez une action réutilisable d’une commande exécutée par le shell.
3. Repérez quand un job a besoin d’une dépendance ou d’un transfert de fichiers.
