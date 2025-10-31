---
index: 11
lang: "fr"
title: "Inodes"
meta_title: "Inodes - Le Système de Fichiers"
meta_description: "Explorez le concept de l'inode Linux. Découvrez ce qu'est un i-node, comment les inodes Linux gèrent les métadonnées des fichiers, et comment vérifier l'utilisation des inodes avec `df -i` et `ls -li`."
meta_keywords: "inode linux, inode dans linux, i node, inode, inode linux, numéro d'inode, système de fichiers, df -i, ls -li, stat"
---

## Lesson Content

Rappelez-vous que notre système de fichiers est composé de tous nos fichiers réels et d'une base de données qui les gère ? Cette base de données est connue sous le nom de table d'inodes, une partie fondamentale du fonctionnement des `inodes sous Linux`.

### Qu'est-ce qu'un Inode Linux

Un inode (abréviation de index node) est une entrée dans cette table. Chaque fichier et répertoire possède son propre `inode`. Il décrit tout sur le fichier, tel que :

- Type de fichier (par exemple, fichier régulier, répertoire, périphérique caractère)
- Propriétaire
- Groupe
- Permissions d'accès
- Horodatages : mtime (dernière modification), ctime (dernier changement d'attribut), atime (dernier accès)
- Nombre de liens physiques vers le fichier
- Taille du fichier
- Nombre de blocs alloués au fichier
- Pointeurs vers les blocs de données du fichier (le plus important !)

essentiellement, un `i node` stocke toutes les métadonnées sur le fichier, à l'exception de son nom et du contenu réel.

### Création et Allocation d'Inodes

Lorsqu'un système de fichiers est créé, de l'espace pour les inodes est également alloué. Des algorithmes déterminent la quantité d'espace `inode` dont vous avez besoin en fonction du volume du disque et d'autres facteurs. Vous avez probablement déjà vu des erreurs de type « espace disque insuffisant ». La même chose peut se produire avec les inodes, bien que ce soit moins courant. Si vous manquez d'inodes, vous ne pouvez pas créer de nouveaux fichiers. Le stockage des données dépend à la fois des blocs de données et de la base de données (la table des `inodes`).

Pour voir combien d'inodes il reste sur votre système, utilisez la commande `df -i`. C'est une vérification cruciale pour les administrateurs système gérant un grand nombre de petits fichiers.

### Affichage des Informations sur les Inodes

Chaque `inode linux` est identifié par un numéro unique. Lorsqu'un fichier est créé, il se voit attribuer un numéro d'inode, souvent séquentiellement. Cependant, vous pourriez remarquer qu'un nouveau fichier obtient un numéro d'inode inférieur à celui des fichiers plus anciens. Cela se produit car les numéros d'inode supprimés peuvent être réutilisés pour de nouveaux fichiers. Pour afficher les numéros d'inode, exécutez `ls -li` :

```bash
pete@icebox:~$ ls -li
140 drwxr-xr-x 2 pete pete 6 Jan 20 20:13 Desktop
141 drwxr-xr-x 2 pete pete 6 Jan 20 20:01 Documents
```

Le premier champ dans la sortie de cette commande est le numéro d'inode. Vous pouvez également voir des informations détaillées sur l'`i node` d'un fichier avec la commande `stat` :

```bash
pete@icebox:~$ stat ~/Desktop/
  File: ‘/home/pete/Desktop/’
  Size: 6               Blocks: 0          IO Block: 4096   directory
Device: 806h/2054d      Inode: 140         Links: 2
Access: (0755/drwxr-xr-x)  Uid: ( 1000/   pete)   Gid: ( 1000/   pete)
Access: 2016-01-20 20:13:50.647435982 -0800
Modify: 2016-01-20 20:13:06.191675843 -0800
Change: 2016-01-20 20:13:06.191675843 -0800
 Birth: -
```

### Comment un I-Node Pointeur vers les Données

Nous savons que nos données sont stockées sur le disque, mais elles ne se trouvent probablement pas dans un seul bloc continu. C'est là que la structure de l'`inode linux` devient essentielle. Les inodes pointent vers les blocs de données réels de vos fichiers. Dans un système de fichiers typique (bien que les implémentations varient), chaque inode contient 15 pointeurs. Les 12 premiers pointeurs pointent directement vers des blocs de données. Le 13e pointeur pointe vers un bloc qui contient plus de pointeurs. Les 14e et 15e pointeurs pointent vers des blocs de pointeurs encore plus imbriqués. Cela peut sembler déroutant, mais cette structure permet à l'`i node` de conserver une taille fixe tout en étant capable de référencer des fichiers de tailles variables. Les petits fichiers peuvent être consultés rapidement à l'aide des pointeurs directs, tandis que les fichiers plus volumineux sont localisés via les pointeurs imbriqués.

## Exercise

La pratique rend parfait ! Voici quelques laboratoires pratiques pour renforcer votre compréhension du système de fichiers Linux et de la gestion des fichiers :

1. **[Gérer les fichiers et les répertoires sous Linux](https://labex.io/fr/labs/comptia-manage-files-and-directories-in-linux-590835)** - Entraînez-vous à créer, supprimer, copier et déplacer des fichiers et des répertoires, et explorez la création de liens symboliques et physiques tout en analysant les inodes.
2. **[Naviguer dans le système de fichiers sous Linux](https://labex.io/fr/labs/comptia-navigate-the-filesystem-in-linux-590971)** - Apprenez les compétences fondamentales pour naviguer dans le système de fichiers Linux à l'aide de commandes shell essentielles telles que `pwd`, `cd` et `ls`.
3. **[Trouver des fichiers et des commandes sous Linux](https://labex.io/fr/labs/comptia-find-files-and-commands-in-linux-590834)** - Maîtrisez les techniques essentielles pour localiser des fichiers et des commandes sous Linux à l'aide de `find`, `locate`, `whereis`, `which` et `type`.

Ces laboratoires vous aideront à appliquer les concepts dans des scénarios réels et à renforcer votre confiance dans la gestion du système de fichiers Linux.

## Quiz Question

Comment voir combien d'inodes il reste sur votre système ? (Veuillez répondre en anglais, en faisant attention à la casse.)

## Quiz Answer

df -i
