---
index: 8
lang: "fr"
title: "niceness"
meta_title: "niceness - Processus"
meta_description: "Découvrez la niceness Linux et la priorité des processus. Comprenez les commandes nice et renice pour gérer le temps CPU des processus. Améliorez les performances du système !"
meta_keywords: "niceness Linux, priorité des processus, commande nice, commande renice, tutoriel Linux, ordonnancement CPU, Linux pour débutants, guide Linux"
---

## Lesson Content

Lorsque vous exécutez plusieurs choses sur votre ordinateur, comme Chrome, Microsoft Word ou Photoshop en même temps, il peut sembler que ces processus s'exécutent simultanément, mais ce n'est pas tout à fait vrai.

Les processus utilisent le CPU pendant une petite période de temps appelée tranche de temps. Ensuite, ils se mettent en pause pendant des millisecondes, et un autre processus obtient une petite tranche de temps. Par défaut, l'ordonnancement des processus se fait de cette manière en tourniquet. Chaque processus obtient suffisamment de tranches de temps jusqu'à ce qu'il ait terminé son traitement. Le noyau gère tous ces changements de processus, et il fait un assez bon travail la plupart du temps.

Les processus ne peuvent pas décider quand et combien de temps ils obtiennent du temps CPU. Si tous les processus se comportaient normalement, ils obtiendraient chacun (à peu près) une quantité égale de temps CPU. Cependant, il existe un moyen d'influencer l'algorithme d'ordonnancement des processus du noyau avec une valeur de niceness. Niceness est un nom assez étrange, mais ce que cela signifie, c'est que les processus ont un nombre pour déterminer leur priorité pour le CPU. Un nombre élevé signifie que le processus est "nice" et a une priorité plus faible pour le CPU, et un nombre faible ou négatif signifie que le processus n'est pas très "nice" et qu'il veut obtenir autant de CPU que possible.

```bash
top
```

Vous pouvez voir une colonne pour `NI` maintenant ; c'est le niveau de niceness d'un processus.

Pour changer le niveau de niceness, vous pouvez utiliser les commandes `nice` et `renice` :

```bash
nice -n 5 apt upgrade
```

La commande `nice` est utilisée pour définir la priorité d'un nouveau processus. La commande `renice` est utilisée pour définir la priorité d'un processus existant.

```bash
renice 10 -p 3245
```

## Exercise

Quels processus ne sont pas très "nice", et pourquoi ?

## Quiz Question

Si je veux qu'un processus obtienne plus de priorité CPU, dois-je utiliser un nombre "nice" plus bas ou plus élevé ?

## Quiz Answer

lower
