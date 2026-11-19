---
lesson_id: "ci-workflow-triggers"
course_id: "continuous-integration"
lang: "fr"
order_index: 2
title: "Déclencheurs d’un workflow"
description: "Apprenez à prévoir quand un workflow GitHub Actions s’exécute à partir de ses événements et de ses filtres de branche."
meta_title: "Déclencheurs d’un workflow - Intégration continue"
meta_description: "Apprenez à prévoir quand un workflow GitHub Actions s’exécute à partir de ses événements et de ses filtres de branche."
meta_keywords: "déclencheurs, filtres de branche, intégration continue, DevOps, Linux Journey"
---

Un workflow s’exécute lorsqu’un événement le déclenche. Dans GitHub Actions, la section `on` indique quels événements peuvent le lancer. Un **événement** peut être un envoi vers une branche, une modification de pull request ou une autre action prise en charge.

## Examiner un envoi

Lisez cet extrait d’un workflow. En YAML, l’indentation indique que `branches` est un réglage de `push`.

```yaml
on:
  push:
    branches:
      - main
```

Le workflow s’exécute lorsqu’un commit est envoyé sur la branche `main`, à condition que le workflow soit activé et que les autres exigences soient remplies. Créer un commit dans un terminal local ne l’envoie pas à GitHub. C’est l’envoi qui déclenche le workflow dans cet exemple.

:::single-choice{#ci-workflow-triggers-push-filter} Quelle action correspond à ce déclencheur push ?

::option[Créer un commit en local sur main.]{#ci-workflow-triggers-push-filter-a explanation="Le déclencheur attend un événement dans le dépôt sur GitHub."}
::option[Envoyer un commit sur une branche appelée draft.]{#ci-workflow-triggers-push-filter-b explanation="Le filtre sélectionne la branche main."}
::option[Envoyer le commit sur main.]{#ci-workflow-triggers-push-filter-c .correct explanation="L’événement correspond à push et au filtre de branche."}
:::

## Examiner une pull request

Un autre événement permet de vérifier des changements proposés avant leur intégration. Dans cet extrait, le filtre de branche s’applique à la branche cible de la pull request.

```yaml
on:
  pull_request:
    branches:
      - main
```

Une proposition de `health-page` vers `main` correspond à ce filtre. Avec les types d’activité par défaut, l’ouverture de la demande et l’envoi d’un nouveau commit sur sa branche source sont deux exemples d’actions qui peuvent déclencher le workflow.

:::single-choice{#ci-workflow-triggers-pr-target} Une pull request propose d’intégrer notes à main. À quel nom le filtre de branche s’applique-t-il ?

::option[Notes, la branche source.]{#ci-workflow-triggers-pr-target-b explanation="Notes contient les changements proposés."}
::option[Main, la branche cible.]{#ci-workflow-triggers-pr-target-a .correct explanation="Le filtre de la pull request porte sur la branche de base, celle qui recevra les changements."}
::option[Le nom du fichier modifié par la proposition.]{#ci-workflow-triggers-pr-target-c explanation="Cet extrait filtre sur les noms de branche."}
:::

## Lire plusieurs déclencheurs

Un fichier peut déclarer les deux événements sous la même clé `on`. Une exécution déclenchée par une pull request peut vérifier l’intégration proposée. Après une fusion qui met à jour `main`, une exécution déclenchée par push peut vérifier le nouvel état de cette branche. Chaque résultat correspond à l’événement et à la révision indiqués dans son exécution.

:::single-choice{#ci-workflow-triggers-after-merge} Un workflow utilise les deux déclencheurs ci-dessus. Une fusion met main à jour. Quel événement correspond à cette mise à jour ?

::option[Un push sur main.]{#ci-workflow-triggers-after-merge-b .correct explanation="La branche qui reçoit les changements a été mise à jour et correspond au filtre de push."}
::option[L’ouverture d’une pull request sur une nouvelle branche.]{#ci-workflow-triggers-after-merge-a explanation="L’action décrite est une mise à jour de main après la fusion."}
::option[Un commit local sans mise à jour du dépôt distant.]{#ci-workflow-triggers-after-merge-c explanation="Dans ce scénario, main a déjà changé sur GitHub."}
:::

## Résumé

Vous savez maintenant associer le déclencheur d’un workflow à un événement du dépôt.

1. Lisez un événement push et son filtre de branche.
2. Repérez la branche cible à laquelle s’applique le filtre d’une pull request.
3. Reliez chaque résultat à l’événement qui a déclenché le workflow.
