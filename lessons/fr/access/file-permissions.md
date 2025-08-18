---
index: 1
lang: "fr"
title: "Permissions de Fichiers"
meta_title: "Permissions de Fichiers - Permissions"
meta_description: "Apprenez les permissions de fichiers Linux : comprenez les bits rwx, les permissions utilisateur, groupe et autres. Maîtrisez la sortie de `ls -l` pour les débutants. Commencez votre parcours Linux !"
meta_keywords: "permissions de fichiers Linux, commande ls -l, permissions rwx, tutoriel Linux, modes de fichiers, Linux pour débutants, guide Linux"
---

## Lesson Content

Comme nous l'avons appris précédemment, les fichiers ont différentes permissions ou modes de fichier. Examinons un exemple :

```bash
$ ls -l Desktop/
drwxr-xr-x 2 pete penguins 4096 Dec 1 11:45 .
```

Il y a quatre parties aux permissions d'un fichier. La première partie est le type de fichier, qui est indiqué par le premier caractère des permissions. Dans notre cas, puisque nous examinons un répertoire, il affiche **d** pour le type de fichier. Le plus souvent, vous verrez un **-** pour un fichier régulier.

Les trois parties suivantes du mode de fichier sont les permissions réelles. Les permissions sont regroupées en 3 bits chacune. Les 3 premiers bits sont les permissions de l'utilisateur, puis les permissions du groupe, et enfin les autres permissions. J'ai ajouté le pipe pour faciliter la différenciation.

```plaintext
d | rwx | r-x | r-x
```

Chaque caractère représente une permission différente :

- r: lisible
- w: inscriptible
- x: exécutable (essentiellement un programme exécutable)
- -: vide

Donc, dans l'exemple ci-dessus, nous voyons que l'utilisateur pete a les permissions de lecture, d'écriture et d'exécution sur le fichier. Le groupe penguins a les permissions de lecture et d'exécution. Et enfin, les autres utilisateurs (tous les autres) ont les permissions de lecture et d'exécution.

## Exercise

Utilisez la commande `ls -l` sur plusieurs fichiers et énoncez leurs permissions, utilisateur et groupe.

## Quiz Question

Quel bit de permission est utilisé pour l'exécutable ?

## Quiz Answer

x
