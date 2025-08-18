---
index: 3
lang: "fr"
title: "Détails des processus"
meta_title: "Détails des processus - Processus"
meta_description: "Apprenez les détails des processus Linux, comment le kernel gère les ressources et ce que sont les processus. Comprenez les concepts de processus pour les débutants."
meta_keywords: "processus Linux, kernel, gestion des processus, ps aux, tutoriel Linux, guide du débutant"
---

## Lesson Content

Avant d'aborder des applications plus pratiques des processus, nous devons d'abord comprendre ce qu'ils sont et comment ils fonctionnent. Cette partie peut être déroutante car nous allons plonger dans les détails, alors n'hésitez pas à revenir à cette leçon si vous ne souhaitez pas l'apprendre maintenant.

Un processus, comme nous l'avons dit précédemment, est un programme en cours d'exécution sur le système. Plus précisément, c'est le système qui alloue de la mémoire, du CPU et des E/S pour faire fonctionner le programme. Un processus est une instance d'un programme en cours d'exécution. Allez-y et ouvrez 3 fenêtres de terminal. Dans deux fenêtres, exécutez la commande `cat` sans passer d'options (le processus `cat` restera ouvert en tant que processus car il attend une entrée standard). Maintenant, dans la troisième fenêtre, exécutez : `ps aux | grep cat`. Vous verrez qu'il y a deux processus pour `cat`, même s'ils appellent le même programme.

Le kernel est en charge des processus. Lorsque nous exécutons un programme, le kernel charge le code du programme en mémoire, détermine et alloue les ressources, puis surveille chaque processus. Il connaît :

- Le statut du processus
- Les ressources que le processus utilise et reçoit
- Le propriétaire du processus
- La gestion des signaux (plus de détails plus tard)
- Et pratiquement tout le reste

Tous les processus essaient d'obtenir une part de ce délicieux gâteau de ressources. C'est le travail du kernel de s'assurer que les processus obtiennent la bonne quantité de ressources en fonction de leurs demandes. Lorsqu'un processus se termine, les ressources qu'il utilisait sont maintenant libérées pour d'autres processus.

## Exercise

Pas d'exercices pour cette leçon.

## Quiz Question

Qu'est-ce qui gère et contrôle les processus ?

## Quiz Answer

kernel
