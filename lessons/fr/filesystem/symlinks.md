---
index: 12
lang: "fr"
title: "Liens symboliques"
meta_title: "Liens symboliques - Le système de fichiers"
meta_description: "Découvrez les liens symboliques et physiques Linux, y compris comment les créer et les gérer. Comprenez leurs différences et leurs cas d'utilisation avec ce guide convivial pour débutants."
meta_keywords: "Liens symboliques Linux, liens physiques, commande ln, liens symboliques, système de fichiers Linux, tutoriel Linux, Linux pour débutants"
---

## Lesson Content

Utilisons un exemple précédent d'informations d'inode :

```plaintext
pete@icebox:~$ ls -li
140 drwxr-xr-x 2 pete pete 6 Jan 20 20:13 Desktop
141 drwxr-xr-x 2 pete pete 6 Jan 20 20:01 Documents
```

Vous avez peut-être remarqué que nous avons survolé le troisième champ de la commande `ls` ; ce champ est le nombre de liens. Le nombre de liens est le nombre total de liens physiques qu'un fichier possède. Eh bien, cela ne signifie rien pour vous pour l'instant, alors discutons d'abord des liens.

### Liens symboliques (Symlinks)

Dans le système d'exploitation Windows, il existe des choses appelées raccourcis. Les raccourcis ne sont que des alias vers d'autres fichiers. Si vous faites quelque chose au fichier original, vous pourriez potentiellement casser le raccourci. Sous Linux, l'équivalent des raccourcis sont les liens symboliques (ou liens souples ou symlinks). Les symlinks nous permettent de lier à un autre fichier par son nom de fichier. Un autre type de lien trouvé sous Linux est les liens physiques (hard links) ; ce sont en fait un autre fichier avec un lien vers un inode. Voyons ce que je veux dire en pratique, en commençant par les symlinks.

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

Vous pouvez voir que j'ai créé un lien symbolique nommé `myfilelink` qui pointe vers `myfile`. Les liens symboliques sont indiqués par `->`. Remarquez cependant que j'ai obtenu un nouveau numéro d'inode ; les symlinks ne sont que des fichiers qui pointent vers des noms de fichiers. Lorsque vous modifiez un symlink, le fichier est également modifié. Les numéros d'inode sont uniques aux systèmes de fichiers ; vous ne pouvez pas avoir deux fois le même numéro d'inode dans un seul système de fichiers, ce qui signifie que vous ne pouvez pas référencer un fichier dans un système de fichiers différent par son numéro d'inode. Cependant, si vous utilisez des symlinks, ils n'utilisent pas de numéros d'inode ; ils utilisent des noms de fichiers, ils peuvent donc être référencés à travers différents systèmes de fichiers.

### Liens physiques (Hardlinks)

Voyons un exemple de lien physique :

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

Un lien physique crée simplement un autre fichier avec un lien vers le même inode. Donc, si je modifiais le contenu de `myfile2` ou `myhardlink`, le changement serait visible sur les deux. Mais si je supprimais `myfile2`, le fichier serait toujours accessible via `myhardlink`. C'est ici que notre nombre de liens dans la commande `ls` entre en jeu. Le nombre de liens est le nombre de liens physiques qu'un inode possède. Lorsque vous supprimez un fichier, cela diminue ce nombre de liens. L'inode n'est supprimé que lorsque tous les liens physiques vers l'inode ont été supprimés. Lorsque vous créez un fichier, son nombre de liens est de 1 car c'est le seul fichier qui pointe vers cet inode. Contrairement aux symlinks, les liens physiques ne s'étendent pas sur les systèmes de fichiers car les inodes sont uniques au système de fichiers.

### Création d'un lien symbolique

```bash
ln -s myfile mylink
```

Pour créer un lien symbolique, vous utilisez la commande `ln` avec `-s` pour symbolique, et vous spécifiez un fichier cible puis un nom de lien.

### Création d'un lien physique

```bash
ln somefile somelink
```

Similaire à la création d'un symlink, sauf que cette fois vous omettez le `-s`.

## Exercise

La pratique rend parfait ! Voici quelques laboratoires pratiques pour renforcer votre compréhension de la gestion des fichiers, des liens et des inodes :

1. **[Gérer les fichiers et les répertoires sous Linux](https://labex.io/fr/labs/comptia-manage-files-and-directories-in-linux-590835)** - Entraînez-vous à créer, copier, déplacer et supprimer des fichiers et des répertoires, et apprenez spécifiquement sur les liens symboliques et physiques, et comment analyser les inodes.
2. **[Naviguer dans le système de fichiers sous Linux](https://labex.io/fr/labs/comptia-navigate-the-filesystem-in-linux-590971)** - Maîtrisez les commandes essentielles comme `pwd`, `cd` et `ls` pour vous déplacer efficacement dans le système de fichiers Linux, une compétence fondamentale pour comprendre où résident les fichiers et leurs inodes.

Ces laboratoires vous aideront à appliquer les concepts de gestion de fichiers et de liens dans des scénarios réels et à renforcer votre confiance avec le système de fichiers Linux.

## Quiz Question

Quelle est la commande utilisée pour créer un lien symbolique ?

## Quiz Answer

ln -s
