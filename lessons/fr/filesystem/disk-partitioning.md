---
index: 4
lang: "fr"
title: "Partitionnement de disque"
meta_title: "Partitionnement de disque - Le système de fichiers"
meta_description: "Apprenez le partitionnement de disque sous Linux en utilisant parted. Comprenez comment partitionner, sélectionner, afficher et redimensionner des disques. Démarrez avec ce guide convivial pour débutants !"
meta_keywords: "partitionnement de disque Linux, commande parted, fdisk, gparted, tutoriel Linux, Linux débutant, gestion de disque, guide Linux"
---

## Lesson Content

Faisons des choses pratiques avec les systèmes de fichiers en parcourant le processus sur une clé USB. Si vous n'en avez pas, pas de soucis, vous pouvez toujours suivre ces quelques leçons.

Tout d'abord, nous devrons partitionner notre disque. De nombreux outils sont disponibles pour ce faire :

- fdisk - outil de partitionnement en ligne de commande basique ; il ne prend pas en charge GPT
- parted - c'est un outil en ligne de commande qui prend en charge le partitionnement MBR et GPT
- gparted - c'est la version GUI de parted
- gdisk - fdisk, mais il ne prend pas en charge MBR, seulement GPT

Utilisons parted pour notre partitionnement. Supposons que je connecte le périphérique USB et que le nom du périphérique soit /dev/sdb2.

### Lancer parted

```bash
sudo parted
```

Vous entrerez dans l'outil parted ; ici, vous pouvez exécuter des commandes pour partitionner votre périphérique.

### Sélectionner le périphérique

```bash
select /dev/sdb2
```

Pour sélectionner le périphérique avec lequel vous travaillerez, sélectionnez-le par son nom de périphérique.

### Afficher la table de partition actuelle

```plaintext
(parted) print
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

Ici, vous verrez les partitions disponibles sur le périphérique. Les points de **début** et de **fin** sont l'endroit où les partitions occupent de l'espace sur le disque dur ; vous voudrez trouver un bon emplacement de début et de fin pour vos partitions.

### Partitionner le périphérique

```bash
mkpart primary 123 4567
```

Maintenant, choisissez simplement un point de début et de fin et créez la partition ; vous devrez spécifier le type de partition en fonction de la table que vous avez utilisée.

### Redimensionner une partition

Vous pouvez également redimensionner une partition si vous n'avez plus d'espace.

```bash
resize 2 1245 3456
```

Sélectionnez le numéro de partition, puis les points de début et de fin où vous souhaitez la redimensionner.

Parted est un outil très puissant, et vous devez être prudent lorsque vous partitionnez vos disques.

## Exercise

La pratique rend parfait ! Voici quelques laboratoires pratiques pour renforcer votre compréhension du partitionnement de disque Linux et de la gestion des systèmes de fichiers :

1. [Gérer les partitions et les systèmes de fichiers Linux](https://labex.io/fr/labs/comptia-manage-linux-partitions-and-filesystems-590845) - Dans ce laboratoire, vous apprendrez à gérer les partitions de disque et les systèmes de fichiers sous Linux. Vous utiliserez fdisk pour créer une nouvelle partition, la formater avec ext4, la monter, configurer le montage persistant dans /etc/fstab, et créer une partition d'échange, le tout sur un disque virtuel secondaire sécurisé.

Ce laboratoire vous aidera à appliquer les concepts de partitionnement de disque et de gestion des systèmes de fichiers dans un scénario réel et à renforcer votre confiance avec ces compétences essentielles d'administration Linux.

## Quiz Question

Quelle est la commande parted pour créer une partition ?

## Quiz Answer

mkpart
