---
lang: "fr"
title: "Inodes"
description: "Apprenez-en davantage sur les inodes Linux, leur structure et comment ils gèrent les fichiers. Comprenez les numéros d'inode et utilisez `df -i` et `ls -li` pour vérifier l'utilisation des inodes. Commencez votre parcours Linux !"
keywords: "inodes Linux, tutoriel inode, df -i, ls -li, système de fichiers Linux, Linux pour débutants, guide Linux"
---

## Lesson Content

Vous souvenez-vous comment notre système de fichiers est composé de tous nos fichiers réels et d'une base de données qui gère ces fichiers ? Cette base de données est connue sous le nom de table d'inodes.

### Qu'est-ce qu'un inode ?

Un inode (index node) est une entrée dans cette table, et il y en a un pour chaque fichier. Il décrit tout sur le fichier, tel que :

- File type - regular file, directory, character device, etc.
- Owner
- Group
- Access permissions
- Timestamps - mtime (heure de la dernière modification du fichier), ctime (heure du dernier changement d'attribut), atime (heure du dernier accès)
- Number of hardlinks to the file
- Size of the file
- Number of blocks allocated to the file
- Pointers to the data blocks of the file - le plus important !

En gros, les inodes stockent tout sur le fichier, sauf le nom du fichier et le fichier lui-même !

### Quand les inodes sont-ils créés ?

Lorsqu'un filesystem est créé, de l'espace pour les inodes est également alloué. Des algorithmes déterminent la quantité d'espace d'inode dont vous avez besoin en fonction du volume du disque et plus encore. Vous avez probablement déjà rencontré des erreurs de manque d'espace disque. La même chose peut se produire pour les inodes (bien que moins courant) ; vous pouvez manquer d'inodes et donc être incapable de créer plus de fichiers. N'oubliez pas que le stockage des données dépend à la fois des données et de la base de données (inodes).

Pour voir combien d'inodes il reste sur votre système, utilisez la commande `df -i`.

### Informations sur les inodes

Les inodes sont identifiés par des numéros. Lorsqu'un fichier est créé, un numéro d'inode lui est attribué, et le numéro est attribué dans l'ordre séquentiel. Cependant, vous remarquerez parfois que lorsque vous créez un nouveau fichier, il obtient un numéro d'inode inférieur à d'autres. C'est parce qu'une fois les inodes supprimés, ils peuvent être réutilisés par d'autres fichiers. Pour afficher les numéros d'inode, exécutez `ls -li` :

```bash
pete@icebox:~$ ls -li
140 drwxr-xr-x 2 pete pete 6 Jan 20 20:13 Desktop
141 drwxr-xr-x 2 pete pete 6 Jan 20 20:01 Documents
```

Le premier champ de cette commande liste le numéro d'inode.

Vous pouvez également voir des informations détaillées sur un fichier avec `stat` ; il vous donne également des informations sur l'inode.

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

### Comment les inodes localisent-ils les fichiers ?

Nous savons que nos données sont quelque part sur le disque. Malheureusement, elles n'ont probablement pas été stockées séquentiellement, nous devons donc utiliser les inodes. Les inodes pointent vers les blocs de données réels de vos fichiers. Dans un filesystem typique (tous ne fonctionnent pas de la même manière), chaque inode contient 15 pointeurs. Les 12 premiers pointeurs pointent directement vers les blocs de données. Le 13ème pointeur pointe vers un bloc contenant des pointeurs vers plus de blocs, le 14ème pointeur pointe vers un autre bloc de pointeurs imbriqué, et le 15ème pointeur pointe encore vers un autre bloc de pointeurs ! C'est déroutant, je sais ! La raison pour laquelle cela est fait de cette manière est de garder la structure de l'inode la même pour chaque inode, mais de pouvoir référencer des fichiers de différentes tailles. Si vous aviez un petit fichier, vous pourriez le trouver plus rapidement avec les 12 premiers pointeurs directs ; les fichiers plus grands peuvent être trouvés avec les nids de pointeurs. Quoi qu'il en soit, la structure de l'inode est la même.

## Exercise

Observez les numéros d'inode pour différents fichiers. Lesquels sont généralement créés en premier ?

## Quiz Question

Comment voyez-vous combien d'inodes il reste sur votre système ?

## Quiz Answer

df -i
