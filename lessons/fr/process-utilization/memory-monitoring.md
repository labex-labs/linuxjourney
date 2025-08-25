---
index: 6
lang: "fr"
title: "Surveillance de la mémoire"
meta_title: "Surveillance de la mémoire - Utilisation des processus"
meta_description: "Apprenez à surveiller l'utilisation de la mémoire Linux avec vmstat. Comprenez la mémoire, le swap et les métriques CPU pour les performances du système. Commencez votre parcours Linux !"
meta_keywords: "vmstat, surveillance mémoire Linux, performances système, tutoriel Linux, utilisation mémoire, Linux débutant, guide Linux"
---

## Lesson Content

En plus de la surveillance du CPU et de la surveillance des E/S, vous pouvez surveiller votre utilisation de la mémoire avec **vmstat**.

```bash
pete@icebox:~$ vmstat
procs -----------memory---------- ---swap-- -----io---- -system-- ------cpu-----
 r  b   swpd   free   buff  cache   si   so    bi    bo   in   cs us sy id wa st
 1  0      0 396528  38816 384036    0    0     4     2   38   79  0  0 99  0  0
```

Les champs sont les suivants :

### procs

- r - Nombre de processus en cours d'exécution
- b - Nombre de processus en sommeil ininterrompu

### memory

- swpd - Quantité de mémoire virtuelle utilisée
- free - Quantité de mémoire libre
- buff - Quantité de mémoire utilisée comme tampons (buffers)
- cache - Quantité de mémoire utilisée comme cache

### swap

- si - Quantité de mémoire échangée depuis le disque (swap in)
- so - Quantité de mémoire échangée vers le disque (swap out)

### io

- bi - Quantité de blocs reçus d'un périphérique de bloc
- bo - Quantité de blocs envoyés à un périphérique de bloc

### system

- in - Nombre d'interruptions par seconde
- cs - Nombre de changements de contexte par seconde

### cpu

- us - Temps passé en mode utilisateur
- sy - Temps passé en mode noyau
- id - Temps passé inactif
- wa - Temps passé à attendre les E/S

## Exercise

La pratique rend parfait ! Voici quelques laboratoires pratiques pour renforcer votre compréhension de la surveillance du système et de la mémoire :

1. **[Commande Linux free : Surveillance de la mémoire système](https://labex.io/fr/labs/linux-linux-free-command-monitoring-system-memory-388496)** - Apprenez à surveiller et analyser l'utilisation de la mémoire système, en comprenant les différents formats d'affichage et la consommation totale de mémoire.
2. **[Commande Linux top : Surveillance du système en temps réel](https://labex.io/fr/labs/linux-linux-top-command-real-time-system-monitoring-388500)** - Apprenez à surveiller les performances du système en temps réel, y compris les processus, l'utilisation du CPU et de la mémoire, en utilisant diverses options de tri et de filtrage.

Ces laboratoires vous aideront à appliquer les concepts de surveillance des ressources système dans des scénarios réels et à renforcer votre confiance dans l'analyse des performances des systèmes Linux.

## Quiz Question

Quel outil est utilisé pour visualiser l'utilisation de la mémoire ?

## Quiz Answer

vmstat
