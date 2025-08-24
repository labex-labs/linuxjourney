---
index: 1
lang: "fr"
title: "Le Shell"
meta_title: "Le Shell - Ligne de Commande"
meta_description: "Découvrez le shell Linux, Bash, et les commandes de base comme 'echo'. Comprenez les invites de shell et commencez votre parcours Linux avec ce guide convivial pour débutants."
meta_keywords: "shell Linux, Bash, commande echo, tutoriel Linux, ligne de commande, Linux pour débutants, invite de shell, guide Linux"
---

## Lesson Content

Le monde est à vous, ou plutôt, le shell est votre huître. Qu'est-ce que le shell ? Le shell est essentiellement un programme qui prend vos commandes du clavier et les envoie au système d'exploitation pour exécution. Si vous avez déjà utilisé une interface graphique, vous avez probablement vu des programmes tels que "Terminal" ou "Console" ; ce ne sont que des programmes qui lancent un shell pour vous. Tout au long de ce cours, nous allons découvrir les merveilles du shell.

Dans ce cours, nous utiliserons le programme shell Bash (Bourne Again Shell). Presque toutes les distributions Linux utiliseront Bash par défaut. Il existe d'autres shells disponibles, tels que `ksh`, `zsh` et `tsch`, mais nous n'aborderons aucun d'entre eux.

Plongeons directement ! Selon la distribution, votre invite de shell peut changer, mais pour la plupart, elle devrait respecter le format suivant :

```plaintext
username@hostname:current_directory
pete@icebox:/home/pete $
```

Remarquez le `$` à la fin de l'invite ? Différents shells auront des invites différentes. Dans notre cas, le `$` est pour un utilisateur normal utilisant Bash, Bourne ou Korn shell. Vous n'ajoutez pas le symbole d'invite lorsque vous tapez la commande ; sachez simplement qu'il est là.

Commençons par une commande simple, `echo`. La commande `echo` affiche simplement les arguments de texte à l'écran.

```bash
echo Hello World
```

## Exercise

Pour une pratique concrète des commandes Linux de base, nous recommandons le cours interactif : [Linux Basic Commands Practice Online](https://labex.io/fr/courses/linux-basic-commands-practice-online)

## Quiz Question

Que devrait afficher la commande `echo Hello World` à l'écran ?

## Quiz Answer

Hello World
