---
lang: "fr"
title: "Le Shell"
meta_description: "Découvrez le shell Linux, Bash et les commandes de base comme 'echo'. Comprenez les invites de shell et commencez votre parcours Linux avec ce guide convivial pour débutants."
meta_keywords: "shell Linux, Bash, commande echo, tutoriel Linux, ligne de commande, Linux débutant, invite de shell, guide Linux"
---

## Lesson Content

Le monde est à vous, ou plutôt, le shell est à vous. Qu'est-ce que le shell ? Le shell est fondamentalement un programme qui prend vos commandes depuis le clavier et les envoie au système d'exploitation pour les exécuter. Si vous avez déjà utilisé une interface graphique, vous avez probablement vu des programmes tels que "Terminal" ou "Console" ; ce ne sont que des programmes qui lancent un shell pour vous. Tout au long de ce cours, nous allons découvrir les merveilles du shell.

Dans ce cours, nous utiliserons le programme shell Bash (Bourne Again Shell). Presque toutes les distributions Linux utiliseront Bash par défaut. D'autres shells sont disponibles, tels que `ksh`, `zsh` et `tsch`, mais nous n'aborderons aucun d'entre eux.

Passons directement à l'action ! Selon la distribution, votre invite de shell peut changer, mais pour la plupart, elle devrait respecter le format suivant :

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

Essayez d'autres commandes Linux et voyez ce qu'elles affichent :

1. `$ date`
2. `$ whoami`

## Quiz Question

Que devrait être affiché à l'écran lorsque vous tapez `echo Hello World` ?

## Quiz Answer

Hello World
