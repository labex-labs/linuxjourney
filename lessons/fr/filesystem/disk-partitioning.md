---
index: 4
lang: "fr"
title: "Partitionnement de disque"
meta_title: "Partitionnement de disque - Le Filesystem"
meta_description: "Apprenez le partitionnement de disque sous Linux à l'aide de parted. Comprenez comment partitionner, sélectionner, afficher et redimensionner des disques. Démarrez avec ce guide convivial pour débutants !"
meta_keywords: "partitionnement de disque Linux, commande parted, fdisk, gparted, tutoriel Linux, Linux pour débutants, gestion de disque, guide Linux"
---

## Lesson Content

Faisons des choses pratiques avec les systèmes de fichiers en travaillant sur une clé USB. Si vous n'en avez pas, pas de soucis, vous pouvez toujours suivre ces prochaines leçons.

Tout d'abord, nous devrons partitionner notre disque. De nombreux outils sont disponibles pour ce faire :

- fdisk - outil de partitionnement en ligne de commande basique ; il ne prend pas en charge GPT
- parted - c'est un outil en ligne de commande qui prend en charge le partitionnement MBR et GPT
- gparted - c'est la version GUI de parted
- gdisk - fdisk, mais il ne prend pas en charge MBR, seulement GPT

Utilisons parted pour notre partitionnement. Disons que je connecte le périphérique USB et que le nom du périphérique est /dev/sdb2.

### Launch parted

```bash
sudo parted
```

Vous entrerez dans l'outil parted ; ici, vous pouvez exécuter des commandes pour partitionner votre périphérique.

### Select the device

```bash
select /dev/sdb2
```

Pour sélectionner le périphérique avec lequel vous allez travailler, sélectionnez-le par son nom de périphérique.

### View current partition table

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

### Partition the device

```bash
mkpart primary 123 4567
```

Maintenant, choisissez simplement un point de début et de fin et créez la partition ; vous devrez spécifier le type de partition en fonction de la table que vous avez utilisée.

### Resize a partition

Vous pouvez également redimensionner une partition si vous n'avez pas d'espace.

```bash
resize 2 1245 3456
```

Sélectionnez le numéro de partition, puis les points de début et de fin où vous souhaitez la redimensionner.

Parted est un outil très puissant, et vous devez être prudent lorsque vous partitionnez vos disques.

## Exercise

Partitionnez une clé USB avec la moitié du disque en ext4 et l'autre moitié en espace libre.

## Quiz Question

Quelle est la commande parted pour créer une partition ?

## Quiz Answer

mkpart
