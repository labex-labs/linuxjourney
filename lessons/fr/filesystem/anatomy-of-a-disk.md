---
index: 3
lang: "fr"
title: "Anatomie d'un Disque"
meta_title: "Anatomie d'un Disque - Le Filesystem"
meta_description: "Découvrez le partitionnement de disque Linux, MBR vs GPT, et la structure du système de fichiers. Comprenez les partitions, les tables et comment organiser les données. Démarrez avec ce guide pour débutants !"
meta_keywords: "partitionnement de disque Linux, MBR, GPT, structure du système de fichiers, partitions Linux, débutant, tutoriel, guide"
---

## Lesson Content

Les disques durs peuvent être subdivisés en partitions, créant essentiellement plusieurs périphériques de bloc. Rappelez-vous des exemples tels que `/dev/sda1` et `/dev/sda2`. `/dev/sda` est le disque entier, mais `/dev/sda1` est la première partition sur ce disque. Les partitions sont extrêmement utiles pour séparer les données, et si vous avez besoin d'un certain système de fichiers, vous pouvez facilement créer une partition au lieu de faire de l'ensemble du disque un seul type de système de fichiers.

### Partition Table

Chaque disque aura une table de partition. Cette table indique au système comment le disque est partitionné. Cette table vous indique où les partitions commencent et se terminent, quelles partitions sont amorçables, quels secteurs du disque sont alloués à quelle partition, etc. Il existe deux principaux schémas de table de partition utilisés : Master Boot Record (MBR) et GUID Partition Table (GPT).

### Partition

Les disques sont composés de partitions qui nous aident à organiser nos données. Vous pouvez avoir plusieurs partitions sur un disque, et elles ne peuvent pas se chevaucher. S'il y a de l'espace qui n'est pas alloué à une partition, il est alors connu sous le nom d'espace libre. Les types de partitions dépendent de votre table de partition. À l'intérieur d'une partition, vous pouvez avoir un filesystem ou dédier une partition à d'autres choses comme le swap (nous y reviendrons bientôt).

_MBR_

- Table de partition traditionnelle, était utilisée comme standard
- Peut avoir des partitions primary, extended et logical
- MBR a une limite de quatre partitions primary
- Des partitions supplémentaires peuvent être créées en transformant une partition primary en une partition extended (il ne peut y avoir qu'une seule partition extended sur un disque). Ensuite, à l'intérieur de la partition extended, vous ajoutez des partitions logical. Les partitions logical sont utilisées comme n'importe quelle autre partition. Bête, je sais.
- Prend en charge les disques jusqu'à 2 téraoctets

_GPT_

- GUID Partition Table (GPT) est en train de devenir le nouveau standard pour le partitionnement de disque
- N'a qu'un seul type de partition, et vous pouvez en créer beaucoup
- Chaque partition a un ID globalement unique (GUID)
- Utilisé principalement en conjonction avec le démarrage basé sur UEFI (nous entrerons dans les détails dans un autre cours)

### Filesystem Structure

Nous savons, d'après notre leçon précédente, qu'un filesystem est une collection organisée de fichiers et de répertoires. Dans sa forme la plus simple, il est composé d'une base de données pour gérer les fichiers et des fichiers eux-mêmes ; cependant, nous allons entrer un peu plus dans les détails.

- Boot block - Ceci est situé dans les premiers secteurs du filesystem, et il n'est pas vraiment utilisé par le filesystem. Il contient plutôt des informations utilisées pour démarrer le système d'exploitation. Un seul boot block est nécessaire au système d'exploitation. Si vous avez plusieurs partitions, elles auront des boot blocks, mais beaucoup d'entre eux sont inutilisés.
- Super block - C'est un seul bloc qui vient après le boot block, et il contient des informations sur le filesystem, telles que la taille de la table d'inodes, la taille des blocs logiques et la taille du filesystem.
- Inode table - Considérez cela comme la base de données qui gère nos fichiers (nous avons une leçon entière sur les inodes, alors ne vous inquiétez pas). Chaque fichier ou répertoire a une entrée unique dans la table d'inodes, et elle contient diverses informations sur le fichier.
- Data blocks - Ce sont les données réelles pour les fichiers et les répertoires.

Jetons un coup d'œil aux différentes tables de partition. Ci-dessous un exemple de partition utilisant la table de partitionnement MBR (msdos). Vous pouvez voir les partitions primary, extended et logical sur la machine.

```plaintext
pete@icebox:~$ sudo parted -l
Model: Seagate (scsi)
Disk /dev/sda: 21.5GB
Sector size (logical/physical): 512B/512B
Partition Table: msdos

Number  Start   End     Size    Type      File system     Flags
 1      1049kB  6860MB  6859MB  primary   ext4            boot
 2      6861MB  21.5GB  14.6GB  extended
 5      6861MB  7380MB  519MB   logical   linux-swap(v1)
 6      7381MB  21.5GB  14.1GB  logical   xfs
```

Cet exemple est GPT, utilisant juste un ID unique pour les partitions.

```plaintext
Model: Thumb Drive (scsi)
Disk /dev/sdb: 4041MB
Sector size (logical/physical): 512B/512B
Partition Table: gpt

Number  Start   End     Size     File system  Name        Flags
 1      17.4kB  1000MB  1000MB                first
 2      1000MB  4040MB  3040MB                second
```

## Exercise

Exécutez **parted -l** sur votre machine et évaluez vos résultats.

## Quiz Question

Quel type de partition est utilisé pour créer plus de 4 partitions dans le schéma de partitionnement MBR ?

## Quiz Answer

extended
