---
lesson_id: "git-status-command"
course_id: "git"
lang: "fr"
order_index: 2
title: "git status"
description: "Apprenez à reconnaître les fichiers non suivis, indexés ou modifiés à l’aide de git status."
meta_title: "git status - Git"
meta_description: "Vérifiez les changements de l’arbre de travail et repérez ce que Git a sélectionné pour le prochain commit."
meta_keywords: "git status, état Git, index Git, fichiers non suivis, DevOps, Linux Journey"
---

Dans un dépôt, `git status` indique ce que Git voit dans l’arbre de travail et ce que vous avez sélectionné pour le prochain enregistrement. Utilisez le dépôt vide `journey-git` de la leçon précédente.

## Repérer un nouveau fichier

Créez une petite page, puis utilisez le format court pour rendre la sortie plus lisible.

```bash
$ printf '%s\n' '<h1>Hello</h1>' > index.html
$ git status --short
```

Ici, `>` écrit dans le fichier indiqué et remplace son contenu s’il existe déjà. Pour le nouveau fichier, l’état abrégé affiche `?? index.html`. Git appelle ce fichier **non suivi**. Le fichier existe, mais il n’a pas encore été sélectionné pour un enregistrement.

:::single-choice{#git-status-command-untracked-file} Git affiche deux points d’interrogation à côté d’un nouveau fichier. Qu’est-ce que cela signifie ?

::option[Le fichier faisait partie du dernier état enregistré.]{#git-status-command-untracked-file-a explanation="Un fichier non suivi ne figure pas dans cet état."}
::option[Le fichier a été supprimé de l’arbre de travail.]{#git-status-command-untracked-file-c explanation="Git voit ce fichier dans votre arbre de travail."}
::option[Le fichier existe et n’est pas encore sélectionné pour le prochain commit.]{#git-status-command-untracked-file-b .correct explanation="Vous pouvez choisir de l’ajouter à l’index."}
:::

![État abrégé de Git montrant le passage de index.html de non suivi à indexé](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/git/git-status-command/staged-file.png)

## Consulter les changements indexés

Exécutez `git add` pour sélectionner le contenu actuel du fichier pour le prochain état enregistré, appelé **commit**. L’**index** contient cette sélection. L’état abrégé affiche maintenant un `A` dans la première colonne pour indiquer que l’ajout est prêt à être enregistré.

```bash
$ git add index.html
$ git status --short
```

:::single-choice{#git-status-command-staged-new} Après git add, où se trouve la version sélectionnée de index.html ?

::option[Déjà dans un nouveau commit.]{#git-status-command-staged-new-a explanation="Git add prépare le prochain commit. Il ne le crée pas."}
::option[Dans l’index.]{#git-status-command-staged-new-c .correct explanation="Git a sélectionné le contenu que le fichier avait au moment où vous avez exécuté git add."}
::option[Dans le dépôt de quelqu’un d’autre.]{#git-status-command-staged-new-b explanation="Cette opération ne modifie que votre index local."}
:::

## Vérifier deux types de changements

Le format court présente deux colonnes avant le nom du fichier. La première donne les changements indexés, la seconde les modifications apportées depuis l’indexation. Par exemple, `AM index.html` signifie que Git a indexé un nouveau fichier et que vous avez ensuite modifié la copie de travail. Si vous préférez une présentation par groupes, utilisez `git status` sans option.

:::single-choice{#git-status-command-two-columns} Vous voyez AM à côté de index.html. Que faut-il vérifier avant le prochain commit ?

::option[Que la copie indexée contient la modification à enregistrer.]{#git-status-command-two-columns-a .correct explanation="Le M de la deuxième colonne indique que la copie de travail contient une modification ultérieure."}
::option[Que le dépôt contient un autre fichier nommé AM.]{#git-status-command-two-columns-b explanation="AM correspond à deux indicateurs d’état pour index.html."}
::option[Que le fichier a été supprimé du disque.]{#git-status-command-two-columns-c explanation="Le M signale une modification dans l’arbre de travail."}
:::

## Résumé

Vous savez maintenant vérifier quels changements Git enregistrerait dans le prochain commit.

1. Reconnaître un nouveau fichier non suivi.
2. Indexer un fichier avec git add.
3. Lire séparément les changements indexés et ceux de l’arbre de travail.
