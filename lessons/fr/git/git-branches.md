---
lesson_id: "git-branches"
course_id: "git"
lang: "fr"
order_index: 5
title: "Branches"
description: "Apprenez à travailler sur plusieurs branches et à intégrer un changement dans main à l’aide d’une fusion."
meta_title: "Branches - Git"
meta_description: "Créez une branche, enregistrez-y un changement et fusionnez-le dans main."
meta_keywords: "branches Git, git switch, git merge, avance rapide, DevOps, Linux Journey"
---

Une **branche** est un nom qui pointe vers un commit. Quand vous créez un nouveau commit sur la branche courante, le nom avance vers ce nouvel état. Une autre branche garde sa position jusqu’à ce que vous la mettiez à jour.

## Démarrer un travail sur une branche à part

Dans le dépôt d’exercice, partez de `main`, créez la branche `health-page` et basculez dessus. L’option `-c` de `git switch` demande de créer une branche.

```bash
$ git switch -c health-page
```

Au départ, les deux noms pointent vers le même commit. Utilisez `git branch --show-current` pour savoir quelle branche avancera au prochain commit.

:::single-choice{#git-branches-start-pointer} Juste après git switch -c health-page, vers quel commit pointe la nouvelle branche ?

::option[Vers un commit vide créé par la commande.]{#git-branches-start-pointer-a explanation="La commande crée un nom qui pointe vers un commit déjà présent."}
::option[Vers un commit dans le dépôt de quelqu’un d’autre.]{#git-branches-start-pointer-c explanation="La commande crée une branche locale dans le dépôt actuel."}
::option[Vers le commit duquel vous êtes parti.]{#git-branches-start-pointer-b .correct explanation="Au début, les deux noms pointent vers le même état."}
:::

## Enregistrer un changement sur la branche

Ajoutez un fichier d’état d’une ligne et créez un commit pendant que `health-page` est la branche courante.

```bash
$ printf '%s\n' ready > health.txt
$ git add health.txt
$ git commit -m "Add a health page"
```

Appelons A le commit de la page d’accueil et B celui de la page d’état.

```text
A (main) --- B (health-page)
```

Seule `health-page` a avancé vers B. Si vous revenez sur `main` avec un arbre de travail propre, vos fichiers retrouvent l’état enregistré dans A.

:::single-choice{#git-branches-branch-snapshot} Avant la fusion, quelle branche contient le commit de la page d’état ?

::option[Les deux, puisqu’elles partagent le même dépôt.]{#git-branches-branch-snapshot-a explanation="Des branches d’un même dépôt peuvent désigner des états différents."}
::option[Health-page uniquement.]{#git-branches-branch-snapshot-c .correct explanation="C’était la branche courante lors de la création du commit B."}
::option[Main uniquement, puisque c’est votre branche de départ.]{#git-branches-branch-snapshot-b explanation="Main n’a pas bougé lors du commit sur health-page."}
:::

## Fusionner dans main

Basculez vers la branche qui doit recevoir le changement, puis indiquez la branche d’origine dans la commande de fusion.

```bash
$ git switch main
$ git merge health-page
```

Ici, `main` n’a reçu aucun nouveau commit depuis A. Git peut le faire pointer directement vers B. C’est ce qu’on appelle une **avance rapide** ou fast-forward. Si chaque branche possède de nouveaux commits, il peut être nécessaire de combiner leurs changements. Lisez la sortie avant de considérer la fusion comme terminée.

:::single-choice{#git-branches-merge-direction} Vous voulez que main reçoive le changement de health-page. Où lancez-vous la fusion ?

::option[Sur main, avec health-page comme source.]{#git-branches-merge-direction-a .correct explanation="La branche courante reçoit le résultat de la fusion."}
::option[Sur health-page, avec main comme source.]{#git-branches-merge-direction-b explanation="Cette commande mettrait health-page à jour."}
::option[Sur une autre branche que personne n’utilise.]{#git-branches-merge-direction-c explanation="Main garde sa position tant qu’elle ne reçoit pas le changement."}
:::

## Résumé

Vous savez maintenant suivre un changement d’une branche locale jusque dans main.

1. Créer une branche qui pointe vers le commit courant.
2. Enregistrer un changement sur la branche prévue.
3. Fusionner le changement dans la branche qui doit le recevoir.
