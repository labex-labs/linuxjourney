---
lesson_id: "git-repositories"
course_id: "git"
lang: "fr"
order_index: 1
title: "Dépôts"
description: "Découvrez ce que conserve un dépôt Git et créez un dépôt vide pour un petit site web."
meta_title: "Dépôts - Git"
meta_description: "Créez un dépôt Git, repérez l’arbre de travail et apprenez quand initialiser ou cloner un dépôt."
meta_keywords: "dépôt Git, arbre de travail, git init, git clone, DevOps, Linux Journey"
---

Un site web commence par quelques fichiers. Git permet de conserver leur état à différents moments. Les fichiers du projet et leur historique forment ensemble votre espace de travail Git local.

## Créer un dépôt

Placez-vous dans un dossier d’exercice où vous pouvez créer un nouveau dossier. Exécutez les commandes suivantes une seule fois. Le signe dollar représente l’invite du shell.

```bash
$ mkdir journey-git
$ cd journey-git
$ git init --initial-branch=main
```

Le nouveau dossier est votre **arbre de travail**, où vous modifiez les fichiers du projet. Git y crée un dossier caché `.git` pour stocker l’historique et les réglages. Aucun changement n’a encore été enregistré dans ce nouveau dépôt. Ici, la branche initiale s’appelle `main`.

:::single-choice{#git-repositories-empty-history} Vous initialisez un dépôt dans un dossier qui contient déjà index.html. Qu’arrive-t-il à l’historique de ce fichier ?

::option[Git enregistre aussitôt le fichier dans un premier commit.]{#git-repositories-empty-history-b explanation="L’initialisation n’enregistre aucun fichier du projet."}
::option[Git pourra l’enregistrer dans un commit ultérieur.]{#git-repositories-empty-history-a .correct explanation="L’initialisation prépare le dépôt. L’enregistrement d’un état se fait séparément."}
::option[Git déplace le fichier dans son dossier caché.]{#git-repositories-empty-history-c explanation="Les fichiers du projet restent dans l’arbre de travail, où vous pouvez les modifier."}
:::

![Terminal LabEx affichant un dépôt Git vide nouvellement initialisé et le dossier d’exercice comme racine](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/git/git-repositories/init-and-root.png)

## Repérer l’arbre de travail

La commande `git rev-parse --show-toplevel` affiche la racine du dépôt courant. Une fois dans le nouveau dépôt, le chemin affiché doit se terminer par `journey-git`. Un sous-dossier de l’arbre de travail appartient au même dépôt, sauf s’il contient son propre dépôt.

```bash
$ git rev-parse --show-toplevel
```

:::single-choice{#git-repositories-find-root} Vous entrez dans un sous-dossier nommé images dans journey-git. Quel dossier Git doit-il afficher comme racine ?

::option[Le dossier journey-git.]{#git-repositories-find-root-b .correct explanation="Git trouve la racine du dépôt en remontant depuis votre emplacement actuel."}
::option[Le sous-dossier images.]{#git-repositories-find-root-a explanation="La racine est celle du dépôt, même si le shell est dans un sous-dossier."}
::option[Le dossier caché .git.]{#git-repositories-find-root-c explanation="La commande affiche la racine de l’arbre de travail, où se trouvent les fichiers du projet."}
:::

## Partir d’un historique existant

Utilisez `git clone` si le dépôt que vous souhaitez copier existe déjà. Un clonage normal crée un arbre de travail local et importe l’historique du dépôt. Utilisez `git init` pour commencer à suivre l’historique d’un nouveau projet local. Vous continuerez à utiliser `journey-git` dans les prochaines leçons.

:::single-choice{#git-repositories-choose-start} Un membre de votre équipe vous donne l’adresse d’un dépôt dont vous avez besoin de l’historique. Comment commencer ?

::option[Créer un dossier vide et y initialiser un dépôt.]{#git-repositories-choose-start-a explanation="Le nouveau dépôt démarre sans l’historique du dépôt de votre équipe."}
::option[Copier uniquement les fichiers visibles du site.]{#git-repositories-choose-start-b explanation="Ces fichiers donnent accès à une version précise, sans l’historique du dépôt."}
::option[Cloner le dépôt de votre équipe.]{#git-repositories-choose-start-c .correct explanation="Le clonage copie l’historique partagé et vous donne un arbre de travail local."}
:::

## Résumé

Vous savez maintenant choisir comment créer un dépôt Git local.

1. Repérer l’arbre de travail et le dossier caché de Git.
2. Retrouver la racine depuis un sous-dossier.
3. Initialiser un dépôt pour créer un historique ou le cloner pour reprendre un historique existant.
