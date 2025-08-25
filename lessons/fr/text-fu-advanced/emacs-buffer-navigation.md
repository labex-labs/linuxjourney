---
index: 11
lang: "fr"
title: "Navigation des tampons Emacs"
meta_title: "Navigation des tampons Emacs - Maîtrise avancée du texte"
meta_description: "Apprenez les commandes de navigation des tampons Emacs. Basculez, fermez et divisez les tampons efficacement avec ce tutoriel Emacs convivial pour les débutants. Améliorez votre flux de travail !"
meta_keywords: "navigation des tampons Emacs, commandes Emacs, C-x b, C-x k, tutoriel Linux, guide Emacs, Emacs pour débutants"
---

## Lesson Content

Pour vous déplacer entre les tampons (ou les fichiers que vous visitez), utilisez les commandes suivantes :

### Changer de tampon

```
C-x b - switch buffer
C-x right arrow - right-cycle through buffer
C-x left arrow - left-cycle through buffer
```

### Fermer le tampon

```
C-x k
```

### Diviser le tampon actuel

```
C-x 2
```

Cela vous permet de voir plusieurs tampons sur un seul écran. Pour vous déplacer entre ces tampons, utilisez : C-x o

### Définir un seul tampon comme écran actuel

```
C-x 1
```

Si vous avez déjà utilisé un multiplexeur de terminal comme `screen` ou `tmux`, les commandes de tampon vous sembleront très familières.

## Exercise

C'est en forgeant qu'on devient forgeron ! Voici quelques exercices pratiques pour renforcer votre compréhension de la navigation et de la manipulation des fichiers texte et des tampons :

1. **[Modifier des fichiers texte sous Linux avec Vim et Nano](https://labex.io/fr/labs/comptia-edit-text-files-in-linux-with-vim-and-nano-591076)** - Entraînez-vous à créer, modifier, enregistrer et naviguer dans le texte au sein des éditeurs Vim et Nano, qui sont cruciaux pour travailler avec des tampons.
2. **[Commande Linux cat : Concaténation de fichiers](https://labex.io/fr/labs/linux-linux-cat-command-file-concatenating-210986)** - Apprenez à visualiser, concaténer et manipuler des fichiers texte, en appliquant directement la façon dont vous pourriez interagir avec le contenu des tampons.
3. **[Visualisation des fichiers journaux et de configuration sous Linux](https://labex.io/fr/labs/linux-viewing-log-and-configuration-files-in-linux-387914)** - Entraînez-vous à utiliser des commandes comme `cat`, `more` et `less` pour visualiser et naviguer efficacement dans les fichiers texte, simulant des scénarios réels d'examen de contenu de type tampon.

Ces laboratoires vous aideront à appliquer les concepts dans des scénarios réels et à renforcer votre confiance dans la manipulation des fichiers texte et des tampons sous Linux.

## Quiz Question

Comment "tuer" un tampon ?

## Quiz Answer

C-x k
