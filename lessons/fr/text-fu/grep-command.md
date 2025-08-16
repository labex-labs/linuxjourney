---
lang: "fr"
title: "grep"
description: "Apprenez à utiliser la commande grep sous Linux pour rechercher des modèles de texte dans des fichiers. Découvrez l'utilisation de base, la recherche insensible à la casse et la combinaison avec d'autres commandes. Commencez votre parcours Linux !"
keywords: "commande grep, Linux grep, rechercher des fichiers, traitement de texte, tutoriel Linux, Linux pour débutants, guide grep"
---

## Lesson Content

La commande `grep` est très probablement la commande de traitement de texte la plus courante que vous utiliserez. Elle vous permet de rechercher dans des fichiers des caractères qui correspondent à un certain modèle. Que feriez-vous si vous vouliez savoir si un fichier existe dans un certain répertoire, ou si vous vouliez voir si une chaîne a été trouvée dans un fichier ? Vous ne fouilleriez certainement pas chaque ligne de texte ; vous utiliseriez `grep` !

Utilisons notre fichier `sample.txt` comme exemple :

```bash
grep fox sample.txt
```

Vous devriez voir que `grep` a trouvé "fox" dans le fichier `sample.txt`.

Vous pouvez également `grep` des modèles insensibles à la casse avec l'option `-i` :

```bash
grep -i somepattern somefile
```

Pour être encore plus flexible avec `grep`, vous pouvez le combiner avec d'autres commandes en utilisant `|`.

```bash
env | grep -i User
```

Comme vous pouvez le voir, `grep` est assez polyvalent. Vous pouvez même utiliser des expressions régulières dans votre modèle :

```bash
ls /somedir | grep '.txt$'
```

Ceci devrait retourner tous les fichiers se terminant par `.txt` dans `somedir`.

## Exercise

Vous avez peut-être entendu parler de `egrep` ou `fgrep` ; ce sont des appels `grep` obsolètes qui ont depuis été remplacés par `grep -E` et `grep -F`. Lisez la page de manuel de `grep` pour en savoir plus.

## Quiz Question

Quelle commande utilisez-vous pour trouver un certain modèle ?

## Quiz Answer

grep
