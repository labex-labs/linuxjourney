---
index: 1
lang: "fr"
title: "Permissions de fichiers"
meta_title: "Permissions de fichiers - Permissions"
meta_description: "Apprenez les permissions de fichiers Linux : comprenez les bits rwx, les permissions utilisateur, groupe et autres. Maîtrisez la sortie de `ls -l` pour les débutants. Commencez votre parcours Linux !"
meta_keywords: "permissions de fichiers Linux, commande ls -l, permissions rwx, tutoriel Linux, modes de fichiers, Linux pour débutants, guide Linux"
---

## Lesson Content

Comme nous l'avons appris précédemment, les fichiers ont différentes permissions ou modes de fichier. Regardons un exemple :

```bash
$ ls -l Desktop/
drwxr-xr-x 2 pete penguins 4096 Dec 1 11:45 .
```

Il y a quatre parties aux permissions d'un fichier. La première partie est le type de fichier, qui est indiqué par le premier caractère des permissions. Dans notre cas, comme nous regardons un répertoire, il affiche **d** pour le type de fichier. Le plus souvent, vous verrez un **-** pour un fichier ordinaire.

Les trois parties suivantes du mode de fichier sont les permissions réelles. Les permissions sont regroupées en 3 bits chacune. Les 3 premiers bits sont les permissions de l'utilisateur, puis les permissions du groupe, et enfin les autres permissions. J'ai ajouté la barre verticale pour faciliter la différenciation.

```plaintext
d | rwx | r-x | r-x
```

Chaque caractère représente une permission différente :

- r: lisible
- w: inscriptible
- x: exécutable (essentiellement un programme exécutable)
- -: vide

Donc, dans l'exemple ci-dessus, nous voyons que l'utilisateur pete a les permissions de lecture, d'écriture et d'exécution sur le fichier. Le groupe penguins a les permissions de lecture et d'exécution. Et enfin, les autres utilisateurs (tout le monde) ont les permissions de lecture et d'exécution.

## Exercise

La pratique rend parfait ! Voici quelques laboratoires pratiques pour renforcer votre compréhension des permissions de fichiers, des utilisateurs et des groupes Linux :

1. **[Utilisateur, groupe et permissions de fichiers Linux](https://labex.io/fr/labs/linux-linux-user-group-and-file-permissions-18002)** - Apprenez les concepts essentiels de gestion des utilisateurs et des groupes Linux, y compris la création d'utilisateurs, l'exploration des appartenances aux groupes, la compréhension des permissions de fichiers et la manipulation de la propriété des fichiers.
2. **[Ajouter un nouvel utilisateur et un nouveau groupe](https://labex.io/fr/labs/linux-add-new-user-and-group-17987)** - Entraînez-vous à créer de nouveaux comptes d'utilisateurs, à configurer des groupes personnalisés et à gérer les appartenances aux groupes, simulant des tâches d'administration système réelles.
3. **[Trouver un fichier](https://labex.io/fr/labs/linux-find-a-file-17993)** - Appliquez vos connaissances des permissions de fichiers en trouvant un fichier spécifique et en définissant son autorité d'accès, en vous assurant que vous êtes le seul utilisateur autorisé.

Ces laboratoires vous aideront à appliquer les concepts dans des scénarios réels et à renforcer votre confiance dans la gestion des permissions et des utilisateurs sous Linux.

## Quiz Question

Quel bit de permission est utilisé pour l'exécutable ?

## Quiz Answer

x
