---
lesson_id: "git-commits"
course_id: "git"
lang: "fr"
order_index: 4
title: "Commits"
description: "Apprenez à enregistrer l’état de l’index et à retrouver le commit dans l’historique Git."
meta_title: "Commits - Git"
meta_description: "Enregistrez le contenu indexé avec un message et retrouvez le commit par son identifiant dans l’historique."
meta_keywords: "commits Git, index Git, git commit, git log, DevOps, Linux Journey"
---

Un **commit** enregistre les fichiers sélectionnés dans l’index. Il conserve aussi un message, les informations sur l’auteur et le lien avec les commits précédents. Son identifiant Git permet de retrouver exactement ce point de l’historique.

## Configurer une identité pour le dépôt d’exercice

Git associe un nom et une adresse e-mail à chaque commit. Définissez des valeurs d’exemple qui ne s’appliquent qu’à ce dépôt. Ces informations figurent dans l’historique, sans accorder d’accès à un service distant.

```bash
$ git config --local user.name "Journey Learner"
$ git config --local user.email "learner@example.com"
```

Reprenez le dépôt d’exercice où `index.html` est déjà indexé. Utilisez `git status` pour vérifier les fichiers qui entreront dans le commit.

:::single-choice{#git-commits-identity-scope} Quel est l’effet de l’option --local ?

::option[Elle vous connecte à un service d’hébergement partagé.]{#git-commits-identity-scope-b explanation="Le nom et l’adresse e-mail sont des métadonnées du commit. L’authentification distante est indépendante."}
::option[Elle définit les informations d’auteur pour ce dépôt.]{#git-commits-identity-scope-a .correct explanation="Les réglages locaux s’appliquent au dépôt actuel."}
::option[Elle change l’auteur des commits existants.]{#git-commits-identity-scope-c explanation="Ces paramètres seront utilisés pour les futurs commits."}
:::

## Enregistrer l’état sélectionné

Lancez `git commit` après avoir indexé la version à enregistrer. Avec l’option `-m`, vous indiquez le message sur la ligne de commande.

```bash
$ git commit -m "Set the homepage heading"
```

Un commit enregistre la version indexée d’un fichier. Si vous modifiez de nouveau l’arbre de travail après l’indexation, le changement ultérieur restera en dehors du commit tant que vous n’aurez pas indexé de nouveau le fichier.

:::single-choice{#git-commits-staged-snapshot} Vous avez indexé Welcome, puis saisi Hi sans mettre l’index à jour. Quel titre figurera dans le commit ?

::option[Welcome, car c’est la version indexée.]{#git-commits-staged-snapshot-c .correct explanation="Git lit le contenu indexé pour enregistrer le commit."}
::option[Hi, car c’est le texte le plus récent sur le disque.]{#git-commits-staged-snapshot-a explanation="La copie de travail peut différer de la copie indexée."}
::option[Les deux, car Git enregistre automatiquement toutes les modifications.]{#git-commits-staged-snapshot-b explanation="L’état indexé contient une seule version sélectionnée du fichier."}
:::

## Lire un historique abrégé

Utilisez `git log --oneline` pour voir un historique compact. Chaque ligne commence par un identifiant de commit abrégé, suivi du message. Votre identifiant sera différent de celui de l’exemple.

```text
$ git log --oneline
a12c345 Set the homepage heading
```

Fiez-vous à l’identifiant pour nommer un commit précis. Plusieurs commits peuvent avoir le même message. L’affichage commence normalement par le commit le plus récent de la branche actuelle.

:::single-choice{#git-commits-identify-snapshot} Deux commits ont pour message Set the homepage heading. Comment distinguer les états qu’ils ont enregistrés ?

::option[Grâce au message de commit commun.]{#git-commits-identify-snapshot-a explanation="Le même texte peut figurer sur plusieurs commits."}
::option[Grâce au nom du fichier touché par les deux changements.]{#git-commits-identify-snapshot-c explanation="Le même fichier peut figurer dans de nombreux commits."}
::option[Grâce à l’identifiant du commit.]{#git-commits-identify-snapshot-b .correct explanation="Chaque identifiant permet de désigner une entrée précise."}
:::

Pour vous entraîner à indexer des changements et à créer des commits dans un terminal en ligne, essayez [Votre premier atelier Git](https://labex.io/tutorials/git-your-first-git-lab-92739).

## Résumé

Vous savez maintenant enregistrer le travail indexé et le retrouver dans l’historique.

1. Configurer une identité d’auteur pour le dépôt d’exercice.
2. Enregistrer l’état indexé avec un message clair.
3. Identifier un commit dans l’historique abrégé.
