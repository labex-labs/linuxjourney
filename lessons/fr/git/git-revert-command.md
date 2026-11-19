---
lesson_id: "git-revert-command"
course_id: "git"
lang: "fr"
order_index: 8
title: "git revert"
description: "Découvrez comment git revert annule un changement tout en conservant le commit d’origine."
meta_title: "git revert - Git"
meta_description: "Découvrez comment git revert annule un changement tout en conservant le commit d’origine."
meta_keywords: "git revert, annuler un commit, git, devops, Linux Journey"
---

Il est possible d’annuler un changement déjà partagé. Utilisez `git revert` pour appliquer le changement inverse dans un nouveau commit. L’historique conserve alors la modification d’origine et la décision de l’annuler.

## Trouver le changement à annuler

Dans le dépôt d’exercice, `main` contient les commits de la page d’accueil et de la page d’état. Consultez l’historique abrégé pour confirmer quelle entrée est la plus récente. Les identifiants ci-dessous servent d’exemple.

```text
$ git log --oneline
3ab4501 Add a health page
a12c345 Set the homepage heading
```

`HEAD` désigne le commit actuellement extrait dans l’arbre de travail. Vérifiez qu’il s’agit bien du changement à annuler. Avant de continuer, utilisez `git status` pour vous assurer que l’arbre de travail est propre.

:::single-choice{#git-revert-command-newest-commit} Dans cet exemple, quel changement serait annulé si vous annuliez HEAD ?

::option[L’ancienne modification du titre de la page d’accueil.]{#git-revert-command-newest-commit-b explanation="La modification du titre figure dans le commit précédent."}
::option[Les deux changements en une seule opération.]{#git-revert-command-newest-commit-c explanation="Ici, HEAD désigne un seul commit. L’annulation s’applique à ce commit."}
::option[L’ajout de la page d’état.]{#git-revert-command-newest-commit-a .correct explanation="HEAD pointe sur l’entrée la plus récente de cette branche."}
:::

## Consigner l’annulation

Dans le dépôt d’exercice, assurez-vous que l’arbre de travail est propre, puis annulez le commit de la page d’état. L’opération modifie les fichiers dans l’arbre de travail et crée un commit. Utilisez `--no-edit` pour garder le message d’annulation proposé par Git.

```bash
$ git revert --no-edit HEAD
```

Dans cet exemple, le fichier d’état est supprimé, car le commit d’origine l’avait ajouté. Si des travaux plus récents ont modifié les mêmes lignes, Git peut s’arrêter et vous demander de résoudre les conflits. Consultez l’état du dépôt avant de continuer.

:::single-choice{#git-revert-command-undo-effect} Si l’annulation réussit, quel changement devriez-vous constater dans les fichiers du projet ?

::option[Les fichiers de la page d’accueil et de la page d’état sont supprimés.]{#git-revert-command-undo-effect-a explanation="Le commit précédent, qui concerne la page d’accueil, reste en vigueur."}
::option[Le fichier de la page d’état est supprimé.]{#git-revert-command-undo-effect-b .correct explanation="L’annulation inverse l’ajout effectué par le commit sélectionné."}
::option[La page d’état est ajoutée une deuxième fois.]{#git-revert-command-undo-effect-c explanation="Git inverse le changement effectué par le commit d’origine."}
:::

![Historique Git avec le nouveau commit d’annulation et le commit d’origine de la page d’état](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/git/git-revert-command/recorded-undo.png)

## Vérifier l’historique après l’annulation

Relancez `git log --oneline`. Une nouvelle entrée d’annulation devrait apparaître au-dessus du commit d’origine de la page d’état. Lancez `git status --short` pour repérer les éventuelles modifications locales restantes. Vous pouvez faire relire et partager le nouveau commit comme n’importe quel autre changement.

:::single-choice{#git-revert-command-history-after-revert} Qu’est-ce qui doit encore apparaître sous la nouvelle entrée d’annulation ?

::option[Le commit d’origine de la page d’état.]{#git-revert-command-history-after-revert-c .correct explanation="Ensemble, les deux commits gardent une trace du changement d’origine et de son annulation."}
::option[Seulement le premier commit qui modifie le titre.]{#git-revert-command-history-after-revert-a explanation="Le commit d’origine de la page d’état figure toujours dans l’historique."}
::option[Plus aucun commit.]{#git-revert-command-history-after-revert-b explanation="Une annulation ajoute un commit à l’historique de la branche, qui conserve ses entrées précédentes."}
:::

## Conserver les autres changements

Imaginons un historique avec trois changements distincts. Le fichier d’état a d’abord été ajouté, puis une faute de frappe a été corrigée sur la page d’accueil, et ces changements ont été partagés. En annulant le commit qui a ajouté le fichier d’état, vous pouvez retirer ce fichier tout en conservant la correction. Consultez l’historique et les fichiers concernés avant de choisir un commit.

:::single-choice{#git-revert-command-final-application} Quelle observation montre que l’annulation a bien conservé le changement souhaité ?

::option[Le commit qui a ajouté le fichier d’état a disparu de l’historique.]{#git-revert-command-final-application-b explanation="Une annulation laisse le commit d’origine dans l’historique."}
::option[La correction de la faute de frappe a également disparu de la page d’accueil.]{#git-revert-command-final-application-c explanation="La correction était un changement distinct. Elle doit rester en place."}
::option[Le fichier d’état a disparu, la correction est toujours présente et l’historique indique l’annulation.]{#git-revert-command-final-application-a .correct explanation="Vous avez vérifié les trois points : l’ajout a été annulé, la correction est restée et l’annulation figure dans l’historique."}
:::

## Résumé

Vous savez maintenant annuler un changement validé tout en gardant une trace des deux opérations.

1. Identifiez précisément le commit à annuler.
2. Annulez-le dans un arbre de travail propre.
3. Vérifiez que les deux entrées figurent dans l’historique.
