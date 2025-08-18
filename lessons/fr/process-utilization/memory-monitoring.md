---
lang: "fr"
title: "Surveillance de la mémoire"
meta_title: "Surveillance de la mémoire - Utilisation des Processus"
meta_description: "Apprenez à surveiller l'utilisation de la mémoire Linux avec vmstat. Comprenez la mémoire, le swap et les métriques CPU pour la performance du système. Commencez votre parcours Linux !"
meta_keywords: "vmstat, surveillance mémoire Linux, performance système, tutoriel Linux, utilisation mémoire, Linux débutant, guide Linux"
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
- buff - Quantité de mémoire utilisée comme buffers
- cache - Quantité de mémoire utilisée comme cache

### swap

- si - Quantité de mémoire échangée depuis le disque (swapped in)
- so - Quantité de mémoire échangée vers le disque (swapped out)

### io

- bi - Quantité de blocs reçus d'un périphérique bloc
- bo - Quantité de blocs envoyés vers un périphérique bloc

### system

- in - Nombre d'interruptions par seconde
- cs - Nombre de changements de contexte par seconde

### cpu

- us - Temps passé en mode utilisateur
- sy - Temps passé en mode noyau
- id - Temps passé inactif
- wa - Temps passé à attendre les E/S

## Exercise

Examinez votre utilisation de la mémoire avec vmstat.

## Quiz Question

Quel outil est utilisé pour visualiser l'utilisation de la mémoire ?

## Quiz Answer

vmstat
