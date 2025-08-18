---
lang: "fr"
title: "find"
meta_description: "Apprenez à utiliser la commande Linux 'find' pour localiser des fichiers et des répertoires. Découvrez les options de recherche de base et améliorez vos compétences en gestion de fichiers Linux."
meta_keywords: "commande Linux find, trouver des fichiers Linux, recherche de répertoire Linux, tutoriel commande find, gestion de fichiers Linux, Linux pour débutants, guide Linux"
---

## Lesson Content

Avec tous les fichiers que nous avons sur le système, il peut devenir un peu chaotique d'essayer d'en trouver un spécifique. Eh bien, il y a une commande que nous pouvons utiliser pour cela : `find` !

```bash
find /home -name puppies.jpg
```

Avec `find`, vous devrez spécifier le répertoire dans lequel vous effectuerez la recherche et ce que vous recherchez. Dans ce cas, nous essayons de trouver un fichier nommé `puppies.jpg`.

Vous pouvez spécifier le type de fichier que vous essayez de trouver.

```bash
find /home -type d -name MyFolder
```

Vous pouvez voir que j'ai défini le type de fichier que j'essaie de trouver comme `d` pour répertoire, et je recherche toujours par le nom de `MyFolder`.

Une chose intéressante à noter est que `find` ne s'arrête pas au répertoire que vous recherchez ; il cherchera également à l'intérieur de tous les sous-répertoires que ce répertoire pourrait avoir.

## Exercise

1. Trouvez un fichier à partir du répertoire racine qui contient le mot "net".

## Quiz Question

Quelle option dois-je spécifier pour `find` si je veux rechercher par nom ?

## Quiz Answer

-name
