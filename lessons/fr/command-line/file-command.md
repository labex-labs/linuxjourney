---
lang: "fr"
title: "fichier"
description: "Apprenez à utiliser la commande Linux 'file' pour identifier les types et le contenu des fichiers. Comprenez les conventions de nommage des fichiers Linux avec ce guide convivial pour débutants."
keywords: "commande Linux file, identifier type de fichier, tutoriel Linux, nommage de fichiers, Linux débutant, guide Linux"
---

## Lesson Content

Lors de la leçon précédente, nous avons appris à utiliser `touch`. Revenons-y un instant. Avez-vous remarqué que le nom de fichier ne respectait pas les conventions de nommage standard, comme vous l'avez probablement vu avec d'autres systèmes d'exploitation tels que Windows ? Normalement, vous vous attendriez à ce qu'un fichier nommé `banana.jpeg` soit un fichier image JPEG.

Sous Linux, les noms de fichiers ne sont pas tenus de représenter le contenu du fichier. Vous pouvez créer un fichier nommé `funny.gif` qui n'est pas réellement un GIF.

Pour savoir de quel type de fichier il s'agit, vous pouvez utiliser la commande `file`. Elle vous montrera une description du contenu du fichier.

```bash
file banana.jpg
```

## Exercise

Exécutez la commande `file` sur quelques répertoires et fichiers différents et notez la sortie.

## Quiz Question

Quelle commande pouvez-vous utiliser pour trouver le type d'un fichier ?

## Quiz Answer

file
