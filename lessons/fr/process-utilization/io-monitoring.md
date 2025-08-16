---
lang: "fr"
title: "Surveillance des E/S"
description: "Apprenez à utiliser iostat pour la surveillance des E/S sous Linux. Comprenez les métriques d'utilisation du CPU et du disque avec cette commande essentielle. Améliorez les performances du système !"
keywords: "iostat, surveillance E/S Linux, utilisation CPU, utilisation disque, commandes Linux, débutant, tutoriel, guide"
---

## Lesson Content

Nous pouvons surveiller l'utilisation du CPU ainsi que l'utilisation du disque avec un outil pratique connu sous le nom de **iostat**.

```bash
pete@icebox:~$ iostat
Linux 3.13.0-39-lowlatency (icebox)     01/28/2016      _i686_  (1 CPU)

avg-cpu:  %user   %nice %system %iowait  %steal   %idle
           0.13    0.03    0.50    0.01    0.00   99.33

Device:            tps    kB_read/s    kB_wrtn/s    kB_read    kB_wrtn
sda               0.17         3.49         1.92     385106     212417
```

La première partie concerne les informations CPU :

- **%user** - Affiche le pourcentage d'utilisation du CPU qui s'est produit lors de l'exécution au niveau utilisateur (application).
- **%nice** - Affiche le pourcentage d'utilisation du CPU qui s'est produit lors de l'exécution au niveau utilisateur avec une priorité nice.
- **%system** - Affiche le pourcentage d'utilisation du CPU qui s'est produit lors de l'exécution au niveau système (noyau).
- **%iowait** - Affiche le pourcentage de temps pendant lequel le ou les CPU étaient inactifs, période durant laquelle le système avait une requête d'E/S disque en attente.
- **%steal** - Affiche le pourcentage de temps passé en attente involontaire par le ou les CPU virtuels pendant que l'hyperviseur servait un autre processeur virtuel.
- **%idle** - Affiche le pourcentage de temps pendant lequel le ou les CPU étaient inactifs et le système n'avait pas de requête d'E/S disque en attente.

La deuxième partie concerne l'utilisation du disque :

- **tps** - Indique le nombre de transferts par seconde qui ont été émis vers le périphérique. Un transfert est une requête d'E/S vers le périphérique. Plusieurs requêtes logiques peuvent être combinées en une seule requête d'E/S vers le périphérique. Un transfert est de taille indéterminée.
- **kB_read/s** - Indique la quantité de données lues depuis le périphérique, exprimée en kilooctets par seconde.
- **kB_wrtn/s** - Indique la quantité de données écrites sur le périphérique, exprimée en kilooctets par seconde.
- **kB_read** - Le nombre total de kilooctets lus.
- **kB_wrtn** - Le nombre total de kilooctets écrits.

## Exercise

Utilisez iostat pour visualiser votre utilisation du disque.

## Quiz Question

Quelle commande peut être utilisée pour visualiser l'utilisation des E/S et du CPU ?

## Quiz Answer

iostat
