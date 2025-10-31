---
index: 12
lang: "fr"
title: "Liens symboliques"
meta_title: "Liens symboliques - Le système de fichiers"
meta_description: "Explorez les liens symboliques (symlinks) et les liens physiques sous Linux. Apprenez à les créer avec la commande ln, à vérifier le nombre de liens avec ls, et à comprendre la différence dans les sorties de ls pour les liens symboliques et physiques."
meta_keywords: "Liens symboliques Linux, liens physiques, commande ln, liens symboliques, ls lien symbolique, nombre de liens sous Linux, ls liens symboliques, ls liens, système de fichiers Linux, tutoriel Linux"
---

## Lesson Content

Lorsque vous listez les fichiers en détail, vous voyez beaucoup d'informations. Examinons un exemple précédent d'informations d'inode provenant de la commande `ls -li` :

```plaintext
pete@icebox:~$ ls -li
140 drwxr-xr-x 2 pete pete 6 Jan 20 20:13 Desktop
141 drwxr-xr-x 2 pete pete 6 Jan 20 20:01 Documents
```

Nous avons précédemment survolé le troisième champ de ce résultat. Ce champ est le nombre de liens (link count).

### Le Nombre de Liens sous Linux

Le **nombre de liens sous Linux** est le nombre total de liens physiques (hard links) qu'un fichier possède. Pour comprendre ce que cela signifie, nous devons d'abord discuter de ce que sont les liens. Sous Linux, il existe deux types de liens : les liens symboliques (symlinks) et les liens physiques (hard links).

### Comprendre les Liens Symboliques (Symlinks)

Dans le système d'exploitation Windows, vous avez des raccourcis, qui sont essentiellement des alias pointant vers d'autres fichiers. Sous Linux, l'équivalent est un lien symbolique, également connu sous le nom de lien souple ou **symlink**. Un symlink est un type de fichier spécial qui pointe vers un autre fichier ou répertoire par son nom.

Voyons cela en pratique. Nous allons créer quelques fichiers, puis un lien symbolique.

```bash
pete@icebox:~/Desktop$ echo 'myfile' > myfile
pete@icebox:~/Desktop$ echo 'myfile2' > myfile2
pete@icebox:~/Desktop$ echo 'myfile3' > myfile3

pete@icebox:~/Desktop$ ln -s myfile myfilelink
pete@icebox:~/Desktop$ ls -li
total 12
  151 -rw-rw-r-- 1 pete pete 7 Jan 21 21:36 myfile
93401 -rw-rw-r-- 1 pete pete 8 Jan 21 21:36 myfile2
93402 -rw-rw-r-- 1 pete pete 8 Jan 21 21:36 myfile3
93403 lrwxrwxrwx 1 pete pete 6 Jan 21 21:39 myfilelink -> myfile
```

Ici, nous avons créé un lien symbolique nommé `myfilelink` qui pointe vers `myfile`. Lorsque vous utilisez `ls` pour visualiser un `ls symlink`, il est clairement identifié par le `l` au début de la chaîne de permissions et le symbole `->` pointant vers la cible. Notez que le symlink a son propre numéro d'inode unique (93403). Comme les symlinks pointent vers des noms de fichiers plutôt que vers des inodes, ils peuvent s'étendre sur différents systèmes de fichiers.

### Comprendre les Liens Physiques (Hard Links)

L'autre type de lien est le lien physique. Un lien physique crée une autre entrée de fichier qui pointe directement vers le même inode que le fichier original.

Créons un lien physique pour `myfile2` :

```bash
pete@icebox:~/Desktop$ ln myfile2 myhardlink
pete@icebox:~/Desktop$ ls -li
total 16
  151 -rw-rw-r-- 1 pete pete 7 Jan 21 21:36 myfile
93401 -rw-rw-r-- 2 pete pete 8 Jan 21 21:36 myfile2
93402 -rw-rw-r-- 1 pete pete 8 Jan 21 21:36 myfile3
93403 lrwxrwxrwx 1 pete pete 6 Jan 21 21:39 myfilelink -> myfile
93401 -rw-rw-r-- 2 pete pete 8 Jan 21 21:36 myhardlink
```

Remarquez que `myhardlink` partage exactement le même numéro d'inode (93401) que `myfile2`. Le nombre de liens pour les deux fichiers est également passé à 2. C'est parce que deux entrées de fichiers pointent maintenant vers le même inode. Si vous modifiez le contenu de `myfile2`, les changements seront reflétés dans `myhardlink`, et vice versa. Si vous supprimez `myfile2`, les données du fichier seront toujours accessibles via `myhardlink`. L'inode et ses données ne sont supprimés du disque que lorsque le nombre de liens tombe à zéro. Étant donné que les liens physiques pointent vers des inodes, qui sont uniques au sein d'un même système de fichiers, ils ne peuvent pas s'étendre sur différents systèmes de fichiers.

### Créer des Liens Symboliques et Physiques

Vous pouvez créer les deux types de liens à l'aide de la commande `ln`. La syntaxe est simple.

Pour créer un lien symbolique, utilisez l'option `-s` :

```bash
ln -s /chemin/vers/original /chemin/vers/lien
```

Pour créer un lien physique, omettez l'option `-s` :

```bash
ln /chemin/vers/original /chemin/vers/lien
```

L'utilisation des commandes `ls symlinks` ou `ls links` générales avec l'option `-l` est essentielle pour gérer et identifier ces différents types de fichiers.

## Exercise

La pratique rend parfait ! Voici quelques laboratoires pratiques pour renforcer votre compréhension de la gestion des fichiers, des liens et des inodes :

1. **[Gérer les Fichiers et les Répertoires sous Linux](https://labex.io/fr/labs/comptia-manage-files-and-directories-in-linux-590835)** - Entraînez-vous à créer, copier, déplacer et supprimer des fichiers et des répertoires, et apprenez spécifiquement sur les liens symboliques et physiques, ainsi que sur la manière d'analyser les inodes.
2. **[Naviguer dans le Système de Fichiers sous Linux](https://labex.io/fr/labs/comptia-navigate-the-filesystem-in-linux-590971)** - Maîtrisez les commandes essentielles telles que `pwd`, `cd` et `ls` pour vous déplacer efficacement dans le système de fichiers Linux, une compétence fondamentale pour comprendre où se trouvent les fichiers et leurs inodes.

Ces laboratoires vous aideront à appliquer les concepts de gestion de fichiers et de liens dans des scénarios réels et à renforcer votre confiance avec le système de fichiers Linux.

## Quiz Question

Quelle est la commande et son option principale utilisée pour créer un lien symbolique ? Votre réponse doit être en anglais et sensible à la casse. Veuillez inclure l'espace entre la commande et l'option.

## Quiz Answer

ln -s
