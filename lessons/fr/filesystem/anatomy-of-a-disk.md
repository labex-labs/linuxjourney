---
index: 3
lang: "fr"
title: "Anatomie d'un Disque"
meta_title: "Anatomie d'un Disque - Le Système de Fichiers"
meta_description: "Explorez l'anatomie d'un disque sous Linux. Ce guide explique quel composant d'un disque indique au système d'exploitation comment le disque est partitionné, couvrant les tables de partition MBR et GPT, les différents types de partitions Linux et leur organisation."
meta_keywords: "disque linux, partitions linux, types de partitions linux, composant disque indique os partitionnement, informations organisation partitions disque dur, MBR, GPT, table de partition, système de fichiers"
---

## Lesson Content

Un disque dur sous Linux peut être subdivisé en partitions, qui fonctionnent comme des périphériques de bloc individuels. Vous vous souvenez peut-être d'exemples comme `/dev/sda1` et `/dev/sda2`. Ici, `/dev/sda` représente le disque entier, tandis que `/dev/sda1` est la première partition sur ce disque. Les partitions sont incroyablement utiles pour séparer les données. Si vous avez besoin d'un système de fichiers spécifique pour une partie de votre stockage, vous pouvez créer une nouvelle partition pour cela au lieu de formater le disque entier.

### La Table de Partition

Alors, quel composant d'un disque indique au système d'exploitation comment le disque est partitionné ? La réponse est la **table de partition**. Ce composant crucial contient des informations sur la manière dont les partitions du disque dur sont organisées. La table de partition spécifie où chaque partition commence et se termine, quelles partitions sont amorçables et quels secteurs du disque sont alloués à chaque partition. Il existe deux schémas principaux de table de partition : Master Boot Record (MBR) et GUID Partition Table (GPT).

### Comprendre les Partitions Linux

Les disques sont composés de partitions qui nous aident à organiser nos données. Vous pouvez avoir plusieurs partitions sur un seul disque, mais elles ne peuvent pas se chevaucher. Tout espace sur le disque non alloué à une partition est appelé espace libre. Les types de partitions Linux disponibles dépendent du schéma de table de partition que vous utilisez. À l'intérieur d'une partition, vous pouvez créer un système de fichiers ou la dédier à d'autres usages, comme l'espace swap.

### Partitions MBR

Le Master Boot Record (MBR) est la norme traditionnelle de table de partition.

- Il prend en charge les partitions primaires, étendues et logiques.
- MBR a une limite de quatre partitions primaires.
- Pour créer plus de partitions, une partition primaire doit être désignée comme partition étendue (une seule est autorisée par disque). Dans cette partition étendue, vous pouvez créer plusieurs partitions logiques, qui fonctionnent comme n'importe quelle autre partition.
- Il prend en charge les disques jusqu'à 2 téraoctets de taille.

### Partitions GPT

The GUID Partition Table (GPT) est la norme moderne pour le partitionnement de disque.

- Elle n'a qu'un seul type de partition, et vous pouvez en créer un grand nombre.
- Chaque partition se voit attribuer un Identifiant Global Unique (GUID).
- GPT est couramment utilisé avec les systèmes de démarrage basés sur UEFI.

### Structure du Système de Fichiers

Comme nous l'avons appris précédemment, un système de fichiers est un ensemble organisé de fichiers et de répertoires. À la base, il se compose d'une base de données pour gérer les fichiers et des fichiers eux-mêmes. Explorons sa structure plus en détail.

- **Bloc d'amorçage (Boot block)** : Situé dans les premiers secteurs d'un système de fichiers, ce bloc n'est pas utilisé par le système de fichiers lui-même. Au lieu de cela, il contient des informations utilisées pour démarrer le système d'exploitation. Un seul bloc d'amorçage est nécessaire par système d'exploitation. Bien que d'autres partitions puissent avoir des blocs d'amorçage, ils restent souvent inutilisés.
- **Superbloc (Superblock)** : C'est un seul bloc suivant le bloc d'amorçage qui contient des métadonnées sur le système de fichiers, telles que la taille de la table d'inodes, la taille des blocs logiques et la taille totale du système de fichiers.
- **Table d'inodes (Inode table)** : C'est la base de données qui gère les fichiers et les répertoires. Chaque fichier ou répertoire a une entrée unique dans la table d'inodes, qui stocke divers attributs le concernant. Nous aborderons les inodes dans une leçon dédiée.
- **Blocs de données (Data blocks)** : C'est là que le contenu réel de vos fichiers et répertoires est stocké.

Ci-dessous se trouve un exemple de disque utilisant la table de partition MBR (étiquetée comme `msdos`). Vous pouvez voir les partitions primaires, étendues et logiques.

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

Ce deuxième exemple montre une table de partition GPT, qui utilise des identifiants uniques pour ses partitions.

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

Pour renforcer votre compréhension du partitionnement de disque et des systèmes de fichiers, nous vous recommandons ce laboratoire pratique :

1.  **[Gérer les Partitions et les Systèmes de Fichiers Linux](https://labex.io/fr/labs/comptia-manage-linux-partitions-and-filesystems-590845)** - Entraînez-vous à créer de nouvelles partitions, à les formater avec des systèmes de fichiers comme ext4, à les monter et à configurer le montage persistant dans `/etc/fstab`.

Ce laboratoire vous aidera à appliquer les concepts de gestion de disque dans des scénarios réels et à gagner en confiance avec le stockage Linux.

## Quiz Question

Quel type de partition est utilisé pour créer plus de 4 partitions dans le schéma de partitionnement MBR ? (Veuillez répondre par un seul mot anglais en minuscules.)

## Quiz Answer

extended
