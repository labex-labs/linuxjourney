---
index: 14
lang: "fr"
title: "find"
meta_title: "find - Ligne de commande"
meta_description: "Apprenez à utiliser la commande Linux 'find' pour localiser des fichiers et des répertoires. Découvrez les options de recherche de base et améliorez vos compétences en gestion de fichiers Linux."
meta_keywords: "Commande Linux find, trouver des fichiers Linux, recherche de répertoire Linux, tutoriel commande find, gestion de fichiers Linux, Linux débutant, guide Linux"
---

## Lesson Content

Avec tous les fichiers que nous avons sur le système, il peut être un peu difficile d'en trouver un spécifique. Eh bien, il y a une commande que nous pouvons utiliser pour cela : `find` !

```bash
find /home -name puppies.jpg
```

Avec `find`, vous devrez spécifier le répertoire dans lequel vous recherchez et ce que vous recherchez. Dans ce cas, nous essayons de trouver un fichier nommé `puppies.jpg`.

Vous pouvez spécifier le type de fichier que vous essayez de trouver.

```bash
find /home -type d -name MyFolder
```

Vous pouvez voir que j'ai défini le type de fichier que je cherche comme `d` pour répertoire, et je cherche toujours par le nom de `MyFolder`.

Une chose intéressante à noter est que `find` ne s'arrête pas au répertoire que vous recherchez ; il cherchera également à l'intérieur de tous les sous-répertoires que ce répertoire pourrait avoir.

## Exercise

La pratique rend parfait ! Voici quelques laboratoires pratiques pour renforcer votre compréhension de la recherche de fichiers et de répertoires sous Linux :

1. **[Commande Linux find : Recherche de fichiers](https://labex.io/fr/labs/linux-linux-find-command-file-searching-219191)** - Ce laboratoire offre une introduction à la commande `find`, un utilitaire polyvalent pour rechercher et localiser des fichiers et des répertoires en fonction de divers critères. Vous vous entraînerez à utiliser `find` pour localiser des fichiers spécifiques.
2. **[Découvrir les ressources système critiques](https://labex.io/fr/labs/linux-discover-critical-system-resources-388032)** - Apprenez les commandes Linux essentielles pour localiser des fichiers et des exécutables, y compris `find`. Vous vous entraînerez à naviguer efficacement dans le système de fichiers et à découvrir les ressources système critiques.

Ces laboratoires vous aideront à appliquer les concepts dans des scénarios réels et à renforcer votre confiance dans l'utilisation efficace de la commande `find`.

## Quiz Question

Quelle option dois-je spécifier pour `find` si je veux rechercher par nom ?

## Quiz Answer

-name
