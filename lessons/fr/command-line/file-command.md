---
index: 6
lang: "fr"
title: "file"
meta_title: "file - Ligne de commande"
meta_description: "Apprenez à utiliser la commande Linux 'file' pour identifier les types et le contenu des fichiers. Comprenez les conventions de nommage des fichiers Linux avec ce guide pour débutants."
meta_keywords: "commande Linux file, identifier le type de fichier, tutoriel Linux, nommage de fichiers, Linux débutant, guide Linux"
---

## Lesson Content

Dans la leçon précédente, nous avons appris à utiliser `touch`. Revenons-y un instant. Avez-vous remarqué que le nom de fichier n'était pas conforme aux conventions de nommage standard, comme vous l'avez probablement vu avec d'autres systèmes d'exploitation tels que Windows ? Normalement, vous vous attendriez à ce qu'un fichier nommé `banana.jpeg` soit un fichier image JPEG.

Sous Linux, les noms de fichiers ne sont pas tenus de représenter le contenu du fichier. Vous pouvez créer un fichier nommé `funny.gif` qui n'est pas réellement un GIF.

Pour savoir de quel type de fichier il s'agit, vous pouvez utiliser la commande `file`. Elle vous montrera une description du contenu du fichier.

```bash
file banana.jpg
```

## Exercise

La pratique rend parfait ! Voici quelques laboratoires pratiques pour renforcer votre compréhension de l'inspection du contenu et des propriétés des fichiers :

1. **[Commande Linux ls : Liste de contenu](https://labex.io/fr/labs/linux-linux-ls-command-content-listing-219205)** - Apprenez la commande Linux `ls` pour lister et analyser efficacement le contenu des fichiers et des répertoires, ce qui précède ou suit souvent l'utilisation de la commande `file` pour comprendre ce qui se trouve dans vos répertoires.
2. **[Commande Linux cat : Concaténation de fichiers](https://labex.io/fr/labs/linux-linux-cat-command-file-concatenating-210986)** - Entraînez-vous à visualiser et à manipuler des fichiers texte, une tâche courante après avoir identifié le type d'un fichier.
3. **[Commande Linux more : Défilement de fichiers](https://labex.io/fr/labs/linux-linux-more-command-file-scrolling-214299)** - Améliorez vos compétences en ligne de commande pour naviguer et explorer de grands fichiers texte, en vous basant sur la capacité à identifier les types de fichiers puis à inspecter leur contenu.

Ces laboratoires vous aideront à appliquer les concepts d'inspection de fichiers et de visualisation de contenu dans des scénarios réels et à renforcer votre confiance dans la gestion des fichiers sous Linux.

## Quiz Question

Quelle commande pouvez-vous utiliser pour trouver le type d'un fichier ?

## Quiz Answer

file