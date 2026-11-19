---
lesson_id: "git-pull-requests"
course_id: "git"
lang: "fr"
order_index: 7
title: "Pull requests"
description: "Apprenez à lire une pull request et à repérer ce que couvre une revue ou une vérification automatisée."
meta_title: "Pull requests - Git"
meta_description: "Apprenez à lire une pull request et à repérer ce que couvre une revue ou une vérification automatisée."
meta_keywords: "pull request, revue de code, git, devops, Linux Journey"
---

Une **pull request**, souvent abrégée en PR, propose d’intégrer les changements d’une branche dans une autre. Git suit les commits et les branches. La plateforme d’hébergement fournit la page de revue, les discussions et les vérifications associées.

## Repérer la branche source et la branche cible

Un collègue propose d’ajouter une page d’état au site. La page de revue affiche `health-page → main`. La branche source, parfois appelée **head**, contient les changements proposés. La branche cible, parfois appelée **base**, est celle qui les recevrait.

```text
Source: health-page at 3ab4501
Target: main
Changed file: health.txt
```

À ce stade, la page de revue présente une proposition. Les changements seront intégrés à la branche cible lorsque la PR sera fusionnée.

:::single-choice{#git-pull-requests-pr-direction} Quelle branche recevra la page d’état une fois la PR fusionnée ?

::option[Une branche qui porte l’identifiant du commit.]{#git-pull-requests-pr-direction-a explanation="Cette valeur identifie un instantané, tandis que la branche cible a son propre nom."}
::option[Main.]{#git-pull-requests-pr-direction-b .correct explanation="La cible est main. C’est donc elle qui recevra le changement après la revue."}
::option[Health-page.]{#git-pull-requests-pr-direction-c explanation="Health-page est la branche source, d’où vient le changement."}
:::

## Examiner les différences

Ouvrez la liste des fichiers modifiés et comparez les changements à la branche cible de la PR. L’ajout d’une ligne dans `health.txt` correspond bien à une petite page d’état. Si la revue indique également une modification de `index.html`, vérifiez si elle a sa place dans la proposition. Appuyez-vous sur les fichiers qui figurent dans la PR.

:::single-choice{#git-pull-requests-unexpected-file} Une PR intitulée « Ajouter une page d’état » modifie aussi l’accueil. Où pouvez-vous voir le changement exact ?

::option[Dans le diff des fichiers modifiés.]{#git-pull-requests-unexpected-file-a .correct explanation="Le diff montre quelles lignes la proposition modifie."}
::option[Dans le titre de la PR.]{#git-pull-requests-unexpected-file-b explanation="Le titre résume l’objectif et peut laisser de côté certains détails."}
::option[Dans le nom de la branche.]{#git-pull-requests-unexpected-file-c explanation="Le nom de la branche indique le sujet du travail sans détailler chaque changement."}
:::

## Lire les résultats des vérifications automatisées

Une plateforme d’hébergement peut lancer un test lorsque la PR est modifiée. Repérez le commit ou la révision à laquelle le résultat correspond. Si un nouveau commit a été envoyé après la réussite du test, vérifiez que les tests requis ont bien été exécutés pour la nouvelle révision. Un résultat positif vous renseigne sur les vérifications qui ont effectivement été exécutées.

:::single-choice{#git-pull-requests-changed-revision} Un test a réussi pour 3ab4501. La PR pointe maintenant vers 78ac900. Que devez-vous examiner avant de vous fier au résultat ?

::option[La qualité du message du premier commit.]{#git-pull-requests-changed-revision-a explanation="Le message ne permet pas de savoir si les tests ont couvert le nouveau commit."}
::option[Le titre actuel de la PR.]{#git-pull-requests-changed-revision-b explanation="Le code peut évoluer sans que le titre change."}
::option[Si les vérifications ont été lancées pour la nouvelle révision.]{#git-pull-requests-changed-revision-c .correct explanation="Le résultat précédent portait sur une autre révision."}
:::

## Résumé

Vous savez maintenant lire ce que propose une pull request et sur quels éléments vous appuyer pour décider de la fusionner.

1. Repérez les branches source et cible.
2. Vérifiez les modifications proposées dans la liste des fichiers modifiés.
3. Identifiez la révision couverte par les vérifications automatisées.
