---
lesson_id: "git-remotes"
course_id: "git"
lang: "fr"
order_index: 6
title: "Dépôts distants"
description: "Apprenez comment un dépôt distant relie deux dépôts et distinguez la récupération de l’envoi."
meta_title: "Dépôts distants - Git"
meta_description: "Configurez un dépôt nu local comme distant, envoyez un commit et vérifiez ce que Git met à jour lors de la récupération."
meta_keywords: "dépôts distants Git, git remote, git fetch, git push, DevOps, Linux Journey"
---

Un **dépôt distant** est une adresse nommée que votre dépôt Git local utilise pour joindre un autre dépôt. Celui-ci peut être hébergé en ligne ou se trouver dans un dossier de la même machine. Cet exercice utilise un autre dossier local. Vous n’avez donc pas besoin d’un compte chez un hébergeur.

## Ajouter une adresse

Depuis le dépôt d’exercice, créez un **dépôt nu** distinct. Un dépôt nu conserve l’historique et les références, sans arbre de travail. Il peut recevoir des commits de votre espace de travail. Pour repartir de zéro, assurez-vous que le dossier `journey-remote.git` n’est pas déjà utilisé.

```bash
$ git init --bare --initial-branch=main ../journey-remote.git
$ git remote add origin ../journey-remote.git
$ git remote -v
```

Le nom `origin` est choisi par convention. La liste des dépôts distants indique l’adresse à laquelle il correspond.

:::single-choice{#git-remotes-add-address} Vous avez exécuté git remote add et origin apparaît dans la liste. Qu’a fait Git ?

::option[Il a enregistré un nom pour l’autre dépôt.]{#git-remotes-add-address-b .correct explanation="Vous pouvez utiliser origin pour désigner cette adresse dans d’autres commandes."}
::option[Il a envoyé tous les commits locaux.]{#git-remotes-add-address-a explanation="L’ajout enregistre l’adresse. Pour envoyer des commits, utilisez push."}
::option[Il a cloné un autre arbre de travail dans le projet.]{#git-remotes-add-address-c explanation="L’arbre de travail existant est resté en place."}
:::

## Envoyer une branche

Utilisez `git push` pour envoyer les commits locaux et demander au dépôt distant de mettre sa branche à jour. L’option `-u` enregistre cette branche comme branche de suivi, ou upstream, que Git associe à votre branche locale pour les commandes ultérieures.

```bash
$ git push -u origin main
```

L’envoi vise seulement l’autre dossier d’exercice. Un dépôt partagé peut exiger une autorisation et refuser certaines mises à jour. Lisez sa réponse avant de conclure que l’envoi a réussi.

:::single-choice{#git-remotes-push-direction} Quelle commande envoie un nouveau commit de main local vers le dépôt distant ?

::option[git fetch origin]{#git-remotes-push-direction-b explanation="Fetch récupère des informations depuis le dépôt distant vers le dépôt local."}
::option[git remote -v]{#git-remotes-push-direction-c explanation="Cette commande affiche l’adresse utilisée par origin."}
::option[git push origin main]{#git-remotes-push-direction-a .correct explanation="Push transfère les commits nécessaires et demande de mettre la branche distante à jour."}
:::

## Récupérer les nouveautés

Utilisez `git fetch origin` pour actualiser votre vue locale de l’historique distant. Git utilise une **branche de suivi à distance**, comme `origin/main`, pour garder le dernier état connu. Vous pouvez la consulter avec `git log --oneline origin/main`. La récupération seule laisse l’arbre de travail sur la branche locale actuelle.

```bash
$ git fetch origin
$ git log --oneline origin/main
```

:::single-choice{#git-remotes-after-fetch} Après un fetch, origin/main avance, mais votre main local ne change pas. Quelle affirmation correspond à ce résultat ?

::option[Fetch a réécrit les fichiers que vous modifiiez.]{#git-remotes-after-fetch-a explanation="Fetch actualise la copie locale de l’état de la branche distante."}
::option[Git a appris le changement distant. L’intégrer est une étape distincte.]{#git-remotes-after-fetch-c .correct explanation="La branche locale peut garder sa position tandis que origin/main avance."}
::option[Votre push a mis à jour le dépôt distant pendant le fetch.]{#git-remotes-after-fetch-b explanation="Fetch reçoit des informations du dépôt distant."}
:::

## Résumé

Vous savez maintenant reconnaître le dépôt sur lequel agit une commande Git.

1. Ajouter et vérifier l’adresse d’un dépôt distant.
2. Envoyer une branche et repérer sa branche de suivi.
3. Récupérer l’historique distant sans modifier les fichiers extraits dans l’arbre de travail.
