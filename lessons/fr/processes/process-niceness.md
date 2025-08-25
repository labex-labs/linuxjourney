---
index: 8
lang: "fr"
title: "gentillesse"
meta_title: "gentillesse - Processus"
meta_description: "Découvrez la gentillesse (niceness) et la priorité des processus sous Linux. Comprenez les commandes nice et renice pour gérer le temps CPU des processus. Améliorez les performances du système !"
meta_keywords: "gentillesse Linux, priorité des processus, commande nice, commande renice, tutoriel Linux, ordonnancement CPU, Linux pour débutants, guide Linux"
---

## Lesson Content

Lorsque vous exécutez plusieurs choses sur votre ordinateur, comme Chrome, Microsoft Word ou Photoshop en même temps, il peut sembler que ces processus s'exécutent simultanément, mais ce n'est pas tout à fait vrai.

Les processus utilisent le CPU pendant une petite période de temps appelée tranche de temps. Ensuite, ils se mettent en pause pendant des millisecondes, et un autre processus obtient une petite tranche de temps. Par défaut, l'ordonnancement des processus se fait de cette manière en tourniquet. Chaque processus obtient suffisamment de tranches de temps jusqu'à ce qu'il ait terminé son traitement. Le noyau gère toutes ces commutations de processus, et il fait un assez bon travail la plupart du temps.

Les processus ne peuvent pas décider quand et combien de temps ils obtiennent du temps CPU. Si tous les processus se comportaient normalement, ils obtiendraient chacun (à peu près) une quantité égale de temps CPU. Cependant, il existe un moyen d'influencer l'algorithme d'ordonnancement des processus du noyau avec une valeur de gentillesse (niceness). La gentillesse est un nom assez étrange, mais ce que cela signifie, c'est que les processus ont un nombre pour déterminer leur priorité pour le CPU. Un nombre élevé signifie que le processus est « gentil » et a une priorité plus faible pour le CPU, et un nombre faible ou négatif signifie que le processus n'est pas très « gentil » et qu'il veut obtenir autant de CPU que possible.

```bash
top
```

Vous pouvez voir une colonne pour `NI` en ce moment ; c'est le niveau de gentillesse d'un processus.

Pour modifier le niveau de gentillesse, vous pouvez utiliser les commandes `nice` et `renice` :

```bash
nice -n 5 apt upgrade
```

La commande `nice` est utilisée pour définir la priorité d'un nouveau processus. La commande `renice` est utilisée pour définir la priorité d'un processus existant.

```bash
renice 10 -p 3245
```

## Exercise

La pratique rend parfait ! Voici quelques laboratoires pratiques pour renforcer votre compréhension de la gestion et de l'ordonnancement des processus Linux :

1. **[Gérer et surveiller les processus Linux](https://labex.io/fr/labs/comptia-manage-and-monitor-linux-processes-590864)** - Entraînez-vous à interagir avec les processus de premier plan et d'arrière-plan, à les inspecter avec `ps`, à surveiller les ressources avec `top`, à ajuster la priorité avec `renice` et à les terminer avec `kill`.

Ce laboratoire vous aidera à appliquer les concepts d'ordonnancement des processus et de gentillesse dans des scénarios réels et à renforcer votre confiance dans la gestion des processus sous Linux.

## Quiz Question

Si je veux qu'un processus obtienne plus de priorité CPU, dois-je utiliser un nombre de gentillesse plus bas ou plus élevé ?

## Quiz Answer

lower
