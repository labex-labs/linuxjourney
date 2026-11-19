---
lesson_id: "ci-workflow-permissions"
course_id: "continuous-integration"
lang: "fr"
order_index: 7
title: "Autorisations des workflows"
description: "Apprenez à donner à une vérification CI courante le seul accès au dépôt dont elle a besoin."
meta_title: "Autorisations des workflows - Intégration continue"
meta_description: "Apprenez à donner à une vérification CI courante le seul accès au dépôt dont elle a besoin."
meta_keywords: "autorisations, accès en lecture, workflows, intégration continue, DevOps, Linux Journey"
---

Un job de CI exécute des commandes et peut recevoir des identifiants d’accès. Une **autorisation** détermine ce que ces identifiants permettent de lire ou de modifier. Un job qui vérifie simplement une page a généralement besoin de lire les fichiers source.

## Accorder un accès en lecture

Cet extrait GitHub Actions limite le jeton intégré du workflow à un accès en lecture au contenu du dépôt.

```yaml
permissions:
  contents: read
```

Le checkout et le test local peuvent lire le dépôt. Un job qui publie un paquet a besoin d’une autre autorisation, sur une autre ressource. Accordez le droit de publication au seul job qui en a besoin.

:::single-choice{#ci-workflow-permissions-choose-permission} Un job lit la page et exécute grep. Quelle autorisation lui faut-il sur le contenu du dépôt ?

::option[L’écriture, parce que le résultat du test s’écrit dans le terminal.]{#ci-workflow-permissions-choose-permission-a explanation="Afficher une sortie dans le terminal ne nécessite pas de pouvoir modifier le contenu du dépôt."}
::option[La lecture.]{#ci-workflow-permissions-choose-permission-c .correct explanation="Le job doit récupérer le contenu et n’a aucune modification à faire dans le dépôt."}
::option[L’écriture, parce que le code source se trouve dans un dépôt Git.]{#ci-workflow-permissions-choose-permission-b explanation="Lire les fichiers source suffit pour cette vérification."}
:::

## Protéger les valeurs sensibles

Un **secret** est une valeur sensible comme un jeton privé. Utilisez le coffre de secrets de la plateforme lorsqu’un job autorisé en a besoin. Gardez les réglages ordinaires de la page séparés des secrets. Les vérifications courantes sur un exemple local doivent fonctionner sans identifiants de publication.

:::single-choice{#ci-workflow-permissions-secret-needed} Quelle valeur doit être placée dans un coffre de secrets dont l’accès est contrôlé ?

::option[Un identifiant d’accès privé pour téléverser un paquet.]{#ci-workflow-permissions-secret-needed-a .correct explanation="Un tel identifiant peut donner accès à un autre système."}
::option[Le texte Welcome utilisé par le test.]{#ci-workflow-permissions-secret-needed-b explanation="Ce texte d’exemple est public."}
::option[Le nom du dossier de sortie dist.]{#ci-workflow-permissions-secret-needed-c explanation="Le nom du dossier est un réglage ordinaire."}
:::

## Garder des journaux utiles

Les journaux d’un workflow peuvent être partagés. Indiquez l’action et son résultat sans afficher la valeur des secrets. Un message d’échec peut indiquer qu’un identifiant requis est absent ou que l’accès a été refusé. Indiquez le nom du job et la révision à la personne qui maintient le workflow pour lui permettre d’enquêter. Gardez la valeur de l’identifiant hors du message.

:::single-choice{#ci-workflow-permissions-safe-diagnostic} Un job de publication ne parvient pas à s’authentifier. Quel message aide au diagnostic sans révéler l’identifiant d’accès ?

::option[Afficher l’intégralité de l’identifiant pour permettre de le copier.]{#ci-workflow-permissions-safe-diagnostic-a explanation="Toute personne ayant accès au journal pourrait le voir."}
::option[Afficher toutes les variables d’environnement pour décrire l’état du job.]{#ci-workflow-permissions-safe-diagnostic-c explanation="L’ensemble de ces variables peut inclure des valeurs sensibles."}
::option[Signaler l’étape de publication qui a échoué et le résultat de la tentative d’accès.]{#ci-workflow-permissions-safe-diagnostic-b .correct explanation="La personne chargée de la vérification peut repérer l’échec et contrôler séparément les autorisations configurées."}
:::

## Examiner un nouveau job

Un workflow proposé vérifie la page lors des pull requests et ajoute un job pour publier un paquet. Les deux jobs ont besoin d’autorisations différentes. Donnez à la vérification le seul accès en lecture nécessaire. Réservez les autorisations de publication approuvées au job qui publie effectivement le paquet.

:::single-choice{#ci-workflow-permissions-final-application} Quelle modification de la proposition répond le mieux aux besoins des deux jobs ?

::option[Donner aux deux jobs le droit de modifier le dépôt.]{#ci-workflow-permissions-final-application-b explanation="La vérification lit uniquement les sources. La publication du paquet peut demander une autorisation différente."}
::option[Utiliser le même identifiant de téléversement dans toutes les étapes pour que les relances se déroulent de la même façon.]{#ci-workflow-permissions-final-application-c explanation="Seul le job de publication a besoin d’un identifiant de téléversement."}
::option[Garder les vérifications en lecture seule et limiter le job de publication à l’accès au paquet dont il a besoin.]{#ci-workflow-permissions-final-application-a .correct explanation="Chaque job dispose ainsi des autorisations nécessaires, et les autres accès restent limités."}
:::

## Résumé

Vous savez maintenant évaluer les accès nécessaires dans un petit pipeline de CI.

1. Adaptez les autorisations sur le dépôt à la tâche du job.
2. Stockez les identifiants privés dans un emplacement dont l’accès est contrôlé.
3. Consignez des erreurs utiles sans exposer la valeur des identifiants.
