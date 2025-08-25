---
index: 11
lang: "fr"
title: "mv (Déplacer)"
meta_title: "mv (Déplacer) - Ligne de commande"
meta_description: "Apprenez à utiliser la commande Linux mv pour déplacer et renommer des fichiers/répertoires. Comprenez ses options et évitez les écrasements. Commencez votre parcours Linux !"
meta_keywords: "commande mv, Linux mv, déplacer fichiers Linux, renommer fichiers Linux, tutoriel Linux, débutant, guide Linux"
---

## Lesson Content

Utilisé pour déplacer des fichiers et aussi les renommer. Assez similaire à la commande `cp` en termes d'options et de fonctionnalités.

Vous pouvez renommer des fichiers comme ceci :

```bash
mv oldfile newfile
```

Ou vous pouvez réellement déplacer un fichier vers un répertoire différent :

```bash
mv file2 /home/pete/Documents
```

Et déplacer plus d'un fichier :

```bash
mv file_1 file_2 /somedirectory
```

Vous pouvez également renommer des répertoires :

```bash
mv directory1 directory2
```

Comme `cp`, si vous `mv` un fichier ou un répertoire, il écrasera tout ce qui se trouve dans le même répertoire. Vous pouvez donc utiliser l'option `-i` pour vous demander confirmation avant d'écraser quoi que ce soit.

```bash
mv -i directory1 directory2
```

Supposons que vous vouliez `mv` un fichier pour écraser le précédent. Vous pouvez également faire une sauvegarde de ce fichier, et il renommera simplement l'ancienne version avec un `~`.

```bash
mv -b directory1 directory2
```

## Exercise

La pratique rend parfait ! L'expérience pratique est cruciale pour maîtriser les commandes Linux comme `mv`. Ces laboratoires vous aideront à solidifier votre compréhension du déplacement et du renommage de fichiers et de répertoires dans un environnement réel :

1. **[Commande Linux mv : Déplacement et renommage de fichiers](https://labex.io/fr/labs/linux-linux-mv-command-file-moving-and-renaming-209743)** - Entraînez-vous à utiliser la commande `mv` pour déplacer et renommer des fichiers et des répertoires, y compris la compréhension de ses différentes options et comportements.
2. **[Organisation des fichiers et des répertoires](https://labex.io/fr/labs/linux-organizing-files-and-directories-387877)** - Appliquez vos connaissances de `mv` (ainsi que `cp` et `rm`) dans un défi pratique pour organiser une structure de projet, déplacer des fichiers et nettoyer des répertoires.

Ces laboratoires vous aideront à appliquer les concepts dans des scénarios réels et à renforcer votre confiance dans la gestion des fichiers et des répertoires à l'aide de la commande `mv`.

## Quiz Question

Comment renommez-vous un fichier appelé `cat` en `dog` ?

## Quiz Answer

mv cat dog