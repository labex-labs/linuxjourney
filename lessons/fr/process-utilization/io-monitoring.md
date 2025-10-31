---
index: 5
lang: "fr"
title: "Surveillance des E/S"
meta_title: "Surveillance des E/S - Utilisation des Processus"
meta_description: "Maîtrisez la surveillance des E/S sous Linux avec la commande iostat. Ce guide explique comment analyser les métriques d'utilisation du CPU et du disque pour optimiser les performances de votre système."
meta_keywords: "surveillance e/s, iostat, surveillance e/s linux, utilisation cpu, utilisation disque, performance système, iowait, commandes linux"
---

## Lesson Content

Une **surveillance des E/S** (Entrées/Sorties) efficace est cruciale pour maintenir un système Linux sain et réactif. Un outil puissant en ligne de commande pour cette tâche est **iostat**, qui fournit des rapports détaillés sur l'activité du CPU et du disque.

L'exécution de la commande `iostat` génère un instantané des métriques de performance de votre système.

```bash
pete@icebox:~$ iostat
Linux 3.13.0-39-lowlatency (icebox)     01/28/2016      _i686_  (1 CPU)

avg-cpu:  %user   %nice %system %iowait  %steal   %idle
           0.13    0.03    0.50    0.01    0.00   99.33

Device:            tps    kB_read/s    kB_wrtn/s    kB_read    kB_wrtn
sda               0.17         3.49         1.92     385106     212417
```

Le résultat est divisé en deux sections principales. Décortiquons-les.

### Comprendre les métriques du CPU

Le premier rapport détaille l'utilisation du CPU, donnant un aperçu de la manière dont le processeur passe son temps.

- **%user**: Pourcentage du temps CPU passé à exécuter des processus au niveau utilisateur (applications).
- **%nice**: Pourcentage du temps CPU passé sur des processus de niveau utilisateur avec une priorité modifiée (nice).
- **%system**: Pourcentage du temps CPU passé à exécuter des processus au niveau système (noyau).
- **%iowait**: Pourcentage du temps où le CPU était inactif en attendant qu'une requête d'E/S disque en attente se termine. Des valeurs élevées ici peuvent indiquer un goulot d'étranglement du stockage.
- **%steal**: Dans un environnement virtualisé, c'est le pourcentage de temps pendant lequel un processeur virtuel attend un processeur réel pendant que l'hyperviseur dessert un autre processeur virtuel.
- **%idle**: Pourcentage du temps où le CPU était inactif et n'attendait aucune requête d'E/S disque.

### Analyser l'utilisation du disque

Le deuxième rapport se concentre sur la **surveillance des E/S** au niveau du périphérique, montrant comment les données sont transférées vers et depuis vos périphériques de stockage.

- **tps**: Transferts par seconde émis vers le périphérique. Un transfert est une requête d'E/S, et plusieurs requêtes logiques peuvent être combinées en une seule.
- **kB_read/s**: Quantité de données lues depuis le périphérique, exprimée en kilooctets par seconde.
- **kB_wrtn/s**: Quantité de données écrites sur le périphérique, exprimée en kilooctets par seconde.
- **kB_read**: Nombre total de kilooctets lus depuis le périphérique depuis le dernier redémarrage.
- **kB_wrtn**: Nombre total de kilooctets écrits sur le périphérique depuis le dernier redémarrage.

## Exercise

La pratique rend parfait ! Voici quelques laboratoires pratiques pour renforcer votre compréhension de la surveillance du système et de l'utilisation du disque :

1. **[Commande Linux df : Rapport sur l'espace disque](https://labex.io/fr/labs/linux-linux-df-command-disk-space-reporting-219188)** - Entraînez-vous à rapporter l'utilisation de l'espace disque sur les systèmes de fichiers montés, un aspect clé de la surveillance.
2. **[Commande Linux du : Estimation de l'espace fichier](https://labex.io/fr/labs/linux-linux-du-command-file-space-estimating-219190)** - Apprenez à estimer l'utilisation de l'espace disque pour les répertoires et sous-répertoires, complétant les informations sur les E/S disque fournies par `iostat`.
3. **[Commande Linux top : Surveillance du système en temps réel](https://labex.io/fr/labs/linux-linux-top-command-real-time-system-monitoring-388500)** - Explorez la surveillance du système en temps réel, y compris l'utilisation du CPU et de la mémoire, ce qui fournit un contexte plus large pour les métriques CPU vues dans `iostat`.

Ces laboratoires vous aideront à appliquer les concepts dans des scénarios réels et à gagner en confiance dans la surveillance des ressources système Linux.

## Quiz Question

Quelle commande peut être utilisée pour visualiser les E/S et l'utilisation du CPU ? (Veuillez répondre uniquement en caractères anglais minuscules)

## Quiz Answer

iostat
