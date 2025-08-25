---
index: 3
lang: "fr"
title: "Détails des processus"
meta_title: "Détails des processus - Processus"
meta_description: "Découvrez les détails des processus Linux, comment le noyau gère les ressources et ce que sont les processus. Comprenez les concepts de processus pour les débutants."
meta_keywords: "processus Linux, noyau, gestion des processus, ps aux, tutoriel Linux, guide du débutant"
---

## Lesson Content

Avant d'aborder des applications plus pratiques des processus, nous devons d'abord comprendre ce qu'ils sont et comment ils fonctionnent. Cette partie peut devenir confuse car nous allons plonger dans les détails, alors n'hésitez pas à revenir à cette leçon si vous ne souhaitez pas l'apprendre maintenant.

Un processus, comme nous l'avons dit précédemment, est un programme en cours d'exécution sur le système. Plus précisément, c'est le système qui alloue de la mémoire, du CPU et des E/S pour faire fonctionner le programme. Un processus est une instance d'un programme en cours d'exécution. Allez-y et ouvrez 3 fenêtres de terminal. Dans deux fenêtres, exécutez la commande `cat` sans passer d'options (le processus `cat` restera ouvert en tant que processus car il attend une entrée standard). Maintenant, dans la troisième fenêtre, exécutez : `ps aux | grep cat`. Vous verrez qu'il y a deux processus pour `cat`, même s'ils appellent le même programme.

Le noyau est en charge des processus. Lorsque nous exécutons un programme, le noyau charge le code du programme en mémoire, détermine et alloue les ressources, puis garde un œil sur chaque processus. Il connaît :

- L'état du processus
- Les ressources que le processus utilise et reçoit
- Le propriétaire du processus
- La gestion des signaux (plus à ce sujet plus tard)
- Et pratiquement tout le reste

Tous les processus essaient d'obtenir une part de ce doux gâteau de ressources. C'est le travail du noyau de s'assurer que les processus obtiennent la bonne quantité de ressources en fonction des demandes du processus. Lorsqu'un processus se termine, les ressources qu'il a utilisées sont maintenant libérées pour d'autres processus.

## Exercise

La pratique rend parfait ! Voici quelques laboratoires pratiques pour renforcer votre compréhension des processus Linux et de leur gestion :

1. **[Gérer et surveiller les processus Linux](https://labex.io/fr/labs/comptia-manage-and-monitor-linux-processes-590864)** - Apprenez les compétences essentielles pour gérer et surveiller les processus sur un système Linux, y compris l'interaction avec les processus de premier plan/arrière-plan, l'inspection avec `ps`, la surveillance avec `top` et la terminaison avec `kill`.
2. **[Commande Linux top : Surveillance du système en temps réel](https://labex.io/fr/labs/linux-linux-top-command-real-time-system-monitoring-388500)** - Apprenez à utiliser la commande `top` pour la surveillance du système en temps réel, y compris le tri des processus, l'ajustement des intervalles de mise à jour et le filtrage par utilisateur.
3. **[Commande Linux free : Surveillance de la mémoire système](https://labex.io/fr/labs/linux-linux-free-command-monitoring-system-memory-388496)** - Apprenez à utiliser la commande `free` pour surveiller et analyser l'utilisation de la mémoire système, en comprenant comment le noyau alloue les ressources aux processus.

Ces laboratoires vous aideront à appliquer les concepts dans des scénarios réels et à renforcer votre confiance dans la gestion des processus sous Linux.

## Quiz Question

Qu'est-ce qui gère et contrôle les processus ?

## Quiz Answer

kernel
