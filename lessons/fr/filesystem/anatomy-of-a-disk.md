---
index: 3
lang: "fr"
title: "Anatomie d'un Disque"
meta_title: "Anatomie d'un Disque - Le Système de Fichiers"
meta_description: "Découvrez le partitionnement de disque Linux, MBR vs GPT, et la structure du système de fichiers. Comprenez les partitions, les tables et comment organiser les données. Démarrez avec ce guide pour débutants !"
meta_keywords: "partitionnement de disque Linux, MBR, GPT, structure du système de fichiers, partitions Linux, débutant, tutoriel, guide"
---

## Lesson Content

Les disques durs peuvent être subdivisés en partitions, créant essentiellement plusieurs périphériques de bloc. Rappelez-vous des exemples tels que `/dev/sda1` et `/dev/sda2`. `/dev/sda` est le disque entier, mais `/dev/sda1` est la première partition sur ce disque. Les partitions sont extrêmement utiles pour séparer les données, et si vous avez besoin d'un certain système de fichiers, vous pouvez facilement créer une partition au lieu de faire du disque entier un seul type de système de fichiers.

### Table de Partition

Chaque disque aura une table de partition. Cette table indique au système comment le disque est partitionné. Cette table vous indique où les partitions commencent et se terminent, quelles partitions sont amorçables, quels secteurs du disque sont alloués à quelle partition, etc. Il existe deux principaux schémas de table de partition utilisés : Master Boot Record (MBR) et GUID Partition Table (GPT).

### Partition

Les disques sont composés de partitions qui nous aident à organiser nos données. Vous pouvez avoir plusieurs partitions sur un disque, et elles ne peuvent pas se chevaucher. S'il y a de l'espace non alloué à une partition, il est alors connu sous le nom d'espace libre. Les types de partitions dépendent de votre table de partition. À l'intérieur d'une partition, vous pouvez avoir un système de fichiers ou dédier une partition à d'autres choses comme le swap (nous y reviendrons bientôt).

_MBR_

- Table de partition traditionnelle, utilisée comme standard
- Peut avoir des partitions primaires, étendues et logiques
- MBR a une limite de quatre partitions primaires
- Des partitions supplémentaires peuvent être créées en transformant une partition primaire en une partition étendue (il ne peut y avoir qu'une seule partition étendue sur un disque). Ensuite, à l'intérieur de la partition étendue, vous ajoutez des partitions logiques. Les partitions logiques sont utilisées comme n'importe quelle autre partition. Bizarre, je sais.
- Prend en charge les disques jusqu'à 2 téraoctets

_GPT_

- GUID Partition Table (GPT) est en train de devenir le nouveau standard pour le partitionnement de disque
- N'a qu'un seul type de partition, et vous pouvez en créer beaucoup
- Chaque partition a un ID globalement unique (GUID)
- Principalement utilisé en conjonction avec le démarrage basé sur UEFI (nous entrerons dans les détails dans un autre cours)

### Structure du Système de Fichiers

Nous savons, d'après notre leçon précédente, qu'un système de fichiers est une collection organisée de fichiers et de répertoires. Dans sa forme la plus simple, il est composé d'une base de données pour gérer les fichiers et des fichiers eux-mêmes ; cependant, nous allons entrer un peu plus dans les détails.

- Bloc de démarrage - Il est situé dans les premiers secteurs du système de fichiers, et il n'est pas vraiment utilisé par le système de fichiers. Il contient plutôt des informations utilisées pour démarrer le système d'exploitation. Un seul bloc de démarrage est nécessaire au système d'exploitation. Si vous avez plusieurs partitions, elles auront des blocs de démarrage, mais beaucoup d'entre eux sont inutilisés.
- Superbloc - C'est un seul bloc qui vient après le bloc de démarrage, et il contient des informations sur le système de fichiers, telles que la taille de la table d'inodes, la taille des blocs logiques et la taille du système de fichiers.
- Table d'inodes - Considérez cela comme la base de données qui gère nos fichiers (nous avons une leçon entière sur les inodes, alors ne vous inquiétez pas). Chaque fichier ou répertoire a une entrée unique dans la table d'inodes, et elle contient diverses informations sur le fichier.
- Blocs de données - C'est la donnée réelle pour les fichiers et les répertoires.

Examinons les différentes tables de partition. Ci-dessous un exemple de partition utilisant la table de partitionnement MBR (msdos). Vous pouvez voir les partitions primaires, étendues et logiques sur la machine.

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

La pratique rend parfait ! Voici quelques laboratoires pratiques pour renforcer votre compréhension du partitionnement de disque et des systèmes de fichiers :

1. **[Gérer les Partitions et les Systèmes de Fichiers Linux](https://labex.io/fr/labs/comptia-manage-linux-partitions-and-filesystems-590845)** - Entraînez-vous à créer de nouvelles partitions, à les formater avec des systèmes de fichiers comme ext4, à les monter et à configurer le montage persistant dans `/etc/fstab`.

Ce laboratoire vous aidera à appliquer les concepts de gestion de disque dans des scénarios réels et à renforcer votre confiance avec le stockage Linux.

## Quiz Question

Quel type de partition est utilisé pour créer plus de 4 partitions dans le schéma de partitionnement MBR ?

## Quiz Answer

extended
