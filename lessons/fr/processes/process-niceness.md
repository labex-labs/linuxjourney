---
index: 8
lang: "fr"
title: "Agréabilité"
meta_title: "Agréabilité - Processus"
meta_description: "Découvrez ce qu'est l'agréabilité (niceness) sous Linux et comment elle affecte la priorité des processus. Cette leçon explique l'agréabilité des processus Linux, en utilisant les commandes nice et renice pour gérer l'ordonnancement du CPU et améliorer les performances du système."
meta_keywords: "agréabilité linux, linux agréabilité, qu'est-ce que l'agréabilité linux, agréabilité processus linux, agréabilité processus, priorité processus, commande nice, commande renice, ordonnancement CPU"
---

## Lesson Content

Lorsque vous exécutez plusieurs applications sur votre ordinateur, il semble qu'elles s'exécutent toutes simultanément. En réalité, le CPU bascule rapidement entre elles, accordant à chaque processus un petit laps de temps de traitement.

### Comment le CPU gère les processus

Chaque processus se voit allouer une petite quantité de temps CPU appelée « tranche de temps ». Après sa tranche de temps, un processus est mis en pause et le CPU passe au suivant. Par défaut, le noyau Linux planifie les processus de manière circulaire (round-robin), garantissant que chaque processus reçoive une part équitable du temps CPU jusqu'à ce qu'il soit terminé. Le planificateur du noyau est très efficace pour gérer ces commutations rapides.

### Qu'est-ce que la "Niceness" sous Linux

Bien que les processus ne puissent pas contrôler directement leur temps CPU, vous pouvez influencer les décisions de planification du noyau. Ceci est réalisé en ajustant la valeur de **niceness linux** d'un processus. Le terme "niceness" (gentillesse) fait référence à la manière dont un processus est "aimable" envers les autres processus du système.

La **niceness d'un processus** est représentée par un nombre allant de -20 (priorité la plus élevée) à 19 (priorité la plus basse).

- Une valeur de niceness élevée (par exemple, 19) signifie que le processus est très "aimable" et a une faible priorité, cédant du temps CPU aux autres.
- Une valeur de niceness faible ou négative (par exemple, -20) signifie que le processus n'est pas "aimable" et exige plus de temps CPU, ce qui lui confère une priorité plus élevée.

Comprendre la **niceness des processus linux** est essentiel pour gérer efficacement les ressources système.

### Ajuster la priorité des processus

Vous pouvez visualiser le niveau de niceness actuel des processus en cours d'exécution à l'aide de la commande `top`. Recherchez la colonne `NI`, qui affiche la valeur de niceness.

```bash
top
```

Pour contrôler la valeur de **niceness linux**, vous pouvez utiliser les commandes `nice` et `renice`.

Utilisez la commande `nice` pour démarrer un nouveau processus avec un niveau de niceness spécifique. Par exemple, la commande suivante démarre `apt upgrade` avec une niceness de 5.

```bash
nice -n 5 apt upgrade
```

Pour modifier la priorité d'un processus déjà en cours d'exécution, utilisez la commande `renice`. La commande suivante modifie la niceness d'un processus avec le PID 3245 à 10.

```bash
renice 10 -p 3245
```

## Exercise

Appliquez vos connaissances avec ce laboratoire pratique pour renforcer votre compréhension de la gestion et de la planification des processus Linux :

1. **[Gérer et Surveiller les Processus Linux](https://labex.io/fr/labs/comptia-manage-and-monitor-linux-processes-590864)** - Entraînez-vous à interagir avec les processus au premier plan et à l'arrière-plan, à les inspecter avec `ps`, à surveiller les ressources avec `top`, à ajuster la priorité avec `renice` et à les terminer avec `kill`.

Ce laboratoire vous aidera à appliquer les concepts de planification des processus et de niceness dans des scénarios réels et à gagner en confiance dans la gestion des processus sous Linux.

## Quiz Question

Si vous souhaitez qu'un processus obtienne plus de priorité CPU, devez-vous utiliser un numéro nice plus bas ou plus élevé ? Veuillez répondre par un seul mot anglais, tout en minuscules.

## Quiz Answer

lower
