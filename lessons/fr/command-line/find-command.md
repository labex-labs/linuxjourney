---
index: 14
lang: "fr"
title: "find"
meta_title: "find - Ligne de commande"
meta_description: "Guide complet de la commande find sous Linux. Apprenez à utiliser la ligne de commande find pour localiser des fichiers et des répertoires par nom, type, etc. Améliorez votre gestion de fichiers avec l'utilitaire puissant find de Linux."
meta_keywords: "commande find, find linux, commande find linux, find ligne de commande, recherche fichier, recherche répertoire, tutoriel linux"
---

## Lesson Content

Avec d'innombrables fichiers sur un système, il peut être difficile d'en localiser un en particulier. Heureusement, il existe un utilitaire puissant que nous pouvons utiliser pour cela : la commande `find`. Cet outil est essentiel pour une gestion efficace des fichiers.

### Utilisation de la ligne de commande Find

La syntaxe de base pour la `ligne de commande find` est `find [chemin] [expression]`. Vous devez spécifier le répertoire à rechercher et les critères de ce que vous recherchez.

Par exemple, pour rechercher un fichier nommé `puppies.jpg` dans le répertoire `/home` et tous ses sous-répertoires, vous utiliseriez :

```bash
find /home -name puppies.jpg
```

La `commande find sous linux` est très flexible, permettant de nombreuses expressions de recherche différentes.

### Recherche par nom et par type

L'une des utilisations les plus courantes de la `commande find` est la recherche par nom de fichier. Comme vu ci-dessus, l'option `-name` vous permet de spécifier le nom exact du fichier que vous souhaitez trouver.

Vous pouvez également spécifier le type d'élément que vous recherchez. L'option `-type` est utilisée à cette fin. Par exemple, si vous souhaitez trouver un répertoire au lieu d'un fichier, vous pouvez utiliser `d`.

```bash
find /home -type d -name MyFolder
```

Dans cette commande, nous définissons le type sur `d` pour répertoire et recherchons un élément nommé `MyFolder`. Pour rechercher spécifiquement des fichiers réguliers, vous utiliseriez `-type f`.

### Recherche récursive

Une caractéristique clé de la `commande find linux` que les utilisateurs apprécient est sa nature récursive. Lorsque vous spécifiez un répertoire de départ, `find` ne regarde pas seulement dans ce répertoire unique ; il recherche automatiquement dans tous les sous-répertoires qu'il contient. Cela en fait un outil incroyablement complet pour localiser des éléments n'importe où dans une arborescence de répertoires.

## Exercise

La pratique est essentielle pour maîtriser la `commande find sous linux`. Ces laboratoires pratiques vous aideront à renforcer votre compréhension de la recherche de fichiers et de répertoires :

1. **[Commande find Linux : Recherche de fichiers](https://labex.io/fr/labs/linux-linux-find-command-file-searching-219191)** - Ce laboratoire présente la commande `find`, un utilitaire polyvalent pour rechercher et localiser des fichiers et des répertoires en fonction de divers critères. Vous vous entraînerez à utiliser `find` pour localiser des fichiers spécifiques.
2. **[Découvrir les ressources système critiques](https://labex.io/fr/labs/linux-discover-critical-system-resources-388032)** - Apprenez les commandes Linux essentielles pour localiser des fichiers et des exécutables, y compris `find`. Vous vous entraînerez à naviguer efficacement dans le système de fichiers et à découvrir des ressources système critiques.

Ces laboratoires vous aideront à appliquer les concepts dans des scénarios réels et à renforcer votre confiance dans l'utilisation efficace de la commande `find`.

## Quiz Question

Quelle option devez-vous spécifier pour la commande `find` afin de rechercher par nom ? Veuillez répondre en utilisant uniquement l'option anglaise, en faisant attention au format requis (par exemple, -option).

## Quiz Answer

-name
