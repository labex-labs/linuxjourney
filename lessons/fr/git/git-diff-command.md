---
lesson_id: "git-diff-command"
course_id: "git"
lang: "fr"
order_index: 3
title: "git diff"
description: "Apprenez à comparer la copie de travail d’un fichier avec sa version indexée à l’aide de git diff."
meta_title: "git diff - Git"
meta_description: "Lisez les lignes modifiées et vérifiez les différences déjà indexées avant de les enregistrer dans un commit."
meta_keywords: "git diff, arbre de travail, index Git, différences, DevOps, Linux Journey"
---

L’état indique quels fichiers ont changé. Avec `git diff`, vous pouvez voir quelles lignes ont changé. Dans l’exemple, la version indexée de `index.html` contient déjà le titre Hello de la leçon précédente.

## Comparer un fichier à sa copie indexée

Remplacez le titre dans le fichier d’exercice et comparez la copie de travail à la copie indexée.

```bash
$ printf '%s\n' '<h1>Welcome</h1>' > index.html
$ git diff -- index.html
```

`--` sépare les options du chemin à examiner. Dans la sortie, la ligne qui commence par `-` vient de l’ancienne copie. La ligne qui commence par `+` indique ce qui la remplace. Les deux lignes ci-dessous sont la partie du diff qui décrit cette modification.

```diff
-<h1>Hello</h1>
+<h1>Welcome</h1>
```

:::single-choice{#git-diff-command-changed-heading} Quel titre figure actuellement dans la copie de travail ?

::option[Welcome.]{#git-diff-command-changed-heading-b .correct explanation="La ligne qui commence par un signe plus affiche ici le nouveau texte de l’arbre de travail."}
::option[Hello.]{#git-diff-command-changed-heading-a explanation="La ligne qui commence par un signe moins montre l’ancien texte indexé."}
::option[Les deux titres.]{#git-diff-command-changed-heading-c explanation="Les deux lignes montrent l’état avant et après la modification d’une même ligne."}
:::

## Comparer l’index à l’historique

Utilisez `git diff --staged -- index.html` pour comparer la version indexée au dernier commit. Avant le premier commit, Git prend un état vide comme référence. Ici, cette sortie présente le titre Hello comme un ajout. En parallèle, `git diff` sans option affiche le passage de Hello à Welcome dans la copie de travail.

```bash
$ git diff --staged -- index.html
```

:::single-choice{#git-diff-command-preview-commit} Quelle commande permet de vérifier ce qui entrerait maintenant dans un commit ?

::option[git diff -- index.html]{#git-diff-command-preview-commit-b explanation="Elle compare le fichier de travail à la copie indexée."}
::option[git status --short]{#git-diff-command-preview-commit-c explanation="L’état indique où sont les changements, sans afficher le détail des lignes modifiées."}
::option[git diff --staged -- index.html]{#git-diff-command-preview-commit-a .correct explanation="Elle compare le contenu sélectionné à l’état précédemment enregistré."}
:::

![Terminal LabEx comparant le titre Welcome de l’arbre de travail au titre Hello indexé](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/git/git-diff-command/working-and-staged.png)

## Comprendre pourquoi un diff est vide

Ajoutez de nouveau le fichier actuel pour mettre à jour la copie indexée.

```bash
$ git add index.html
$ git diff -- index.html
```

`git diff` sans option peut ne plus rien afficher puisque le fichier de travail et la copie indexée sont identiques. Utilisez la comparaison de l’index pour voir ce qui reste à enregistrer. Git exclut aussi les fichiers non suivis de ces comparaisons ordinaires. En cas de doute sur l’état d’un changement, consultez l’état du dépôt.

:::single-choice{#git-diff-command-empty-diff} Juste après l’indexation, git diff sans option n’affiche rien. Où pouvez-vous encore voir la différence par rapport à l’historique ?

::option[En relançant git diff sans option.]{#git-diff-command-empty-diff-a explanation="Relancer la même comparaison revient à comparer deux copies identiques."}
::option[Dans la sortie de git diff --staged.]{#git-diff-command-empty-diff-c .correct explanation="Cette commande compare la copie indexée à la référence de l’historique."}
::option[Uniquement après la création d’un commit.]{#git-diff-command-empty-diff-b explanation="Vous pouvez vérifier le contenu prévu du commit avant de l’enregistrer."}
:::

## Résumé

Vous savez maintenant choisir le diff qui répond à votre question.

1. Lire les lignes supprimées et ajoutées dans un diff.
2. Comparer le fichier de travail au contenu de l’index.
3. Vérifier les changements indexés avant de créer un commit.
