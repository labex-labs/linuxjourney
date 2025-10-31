---
index: 6
lang: "fr"
title: "Surveillance de la mémoire"
meta_title: "Surveillance de la mémoire - Utilisation des processus"
meta_description: "Maîtrisez la surveillance de la mémoire Linux avec la commande vmstat. Ce guide explique comment utiliser cet outil puissant de surveillance de l'utilisation de la mémoire pour analyser les métriques de performance du système."
meta_keywords: "surveillance mémoire, moniteur d'utilisation mémoire, vmstat, mémoire linux, performance système, utilisation mémoire, tutoriel linux"
---

## Lesson Content

Une administration système efficace nécessite de surveiller de près l'utilisation des ressources, et la **surveillance de la mémoire** est un élément essentiel de ce processus. Lorsqu'un système manque de mémoire, ses performances peuvent se dégrader considérablement. Linux fournit plusieurs outils pour vous aider à suivre la consommation de mémoire, et l'un des plus polyvalents est `vmstat`.

### Introduction à vmstat

La commande `vmstat` (statistiques de mémoire virtuelle) est un **moniteur d'utilisation de la mémoire** puissant qui signale des informations sur les processus, la mémoire, la pagination, les E/S de bloc, les interruptions et l'activité du CPU. L'exécuter sans arguments fournit un instantané de l'état actuel du système depuis le dernier démarrage.

```bash
pete@icebox:~$ vmstat
procs -----------memory---------- ---swap-- -----io---- -system-- ------cpu-----
r  b   swpd   free   buff  cache   si   so    bi    bo   in   cs us sy id wa st
 1  0      0 396528  38816 384036    0    0     4     2   38   79  0  0 99  0  0
```

Le résultat est organisé en plusieurs colonnes. Décomposons la signification de chaque champ.

### Procs

- `r` : Le nombre de processus exécutables attendant du temps d'exécution.
- `b` : Le nombre de processus en sommeil non interrompable, attendant généralement des E/S.

### Memory

- `swpd` : La quantité de mémoire virtuelle utilisée (en kilooctets).
- `free` : La quantité de mémoire inactive (en kilooctets).
- `buff` : La quantité de mémoire utilisée comme tampons (buffers).
- `cache` : La quantité de mémoire utilisée comme cache de pages.

### Swap

- `si` : La quantité de mémoire échangée depuis le disque par seconde (en kilooctets). Des valeurs élevées indiquent que le système manque de mémoire physique.
- `so` : La quantité de mémoire échangée vers le disque par seconde (en kilooctets). Idéalement, cette valeur devrait être nulle.

### IO

- `bi` : Blocs reçus d'un périphérique de bloc (blocs/s).
- `bo` : Blocs envoyés à un périphérique de bloc (blocs/s).

### System

- `in` : Le nombre d'interruptions par seconde, y compris l'horloge.
- `cs` : Le nombre de changements de contexte par seconde.

### CPU

Ce sont des pourcentages du temps total du CPU.

- `us` : Temps passé à exécuter du code non noyau (temps utilisateur).
- `sy` : Temps passé à exécuter du code noyau (temps système).
- `id` : Temps passé au repos (inactif).
- `wa` : Temps passé à attendre des E/S.
- `st` : Temps volé à une machine virtuelle (pour les environnements virtualisés).

## Exercise

La pratique rend parfait ! Voici quelques laboratoires pratiques pour renforcer votre compréhension de la surveillance du système et de la mémoire :

1. **[Commande Linux free : Surveillance de la mémoire système](https://labex.io/fr/labs/linux-linux-free-command-monitoring-system-memory-388496)** - Apprenez à surveiller et analyser l'utilisation de la mémoire système, en comprenant les différents formats d'affichage et la consommation totale de mémoire.
2. **[Commande Linux top : Surveillance du système en temps réel](https://labex.io/fr/labs/linux-linux-top-command-real-time-system-monitoring-388500)** - Apprenez à surveiller les performances du système en temps réel, y compris les processus, le CPU et l'utilisation de la mémoire, en utilisant diverses options de tri et de filtrage.

Ces laboratoires vous aideront à appliquer les concepts de surveillance des ressources système dans des scénarios réels et à renforcer votre confiance dans l'analyse des performances du système Linux.

## Quiz Question

Quel outil est utilisé pour visualiser l'utilisation de la mémoire ? (Veuillez répondre en anglais, en faisant attention à la casse)

## Quiz Answer

vmstat
