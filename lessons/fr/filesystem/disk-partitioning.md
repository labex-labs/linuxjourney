---
index: 4
lang: "fr"
title: "Partitionnement de Disque"
meta_title: "Partitionnement de Disque - Le Système de Fichiers"
meta_description: "Apprenez le partitionnement de disque sous Linux avec la commande parted. Ce guide explique comment visualiser les partitions avec `sudo parted -l`, les créer et les redimensionner. Présente également gparted, une alternative graphique populaire."
meta_keywords: "Partitionnement disque Linux, commande parted, sudo parted -l, gparted, alternative gparted windows, fdisk, gestion de disque, créer partition, redimensionner partition, guide Linux"
---

## Lesson Content

Cette leçon fournit un guide pratique pour gérer les systèmes de fichiers en partitionnant un disque, tel qu'une clé USB. Si vous n'avez pas de disque de rechange, vous pouvez toujours suivre pour comprendre les concepts.

Premièrement, nous devrons partitionner notre disque. De nombreux outils sont disponibles pour cette tâche :

- **fdisk** : Un outil de partitionnement en ligne de commande de base ; il ne prend pas en charge GPT.
- **parted** : Un outil en ligne de commande puissant qui prend en charge le partitionnement MBR et GPT.
- **gparted** : La version graphique de `parted`. Pour les utilisateurs qui préfèrent une interface visuelle, `gparted` est un outil intuitif, souvent considéré comme une excellente `alternative windows gparted`.
- **gdisk** : Similaire à `fdisk`, mais il ne prend en charge que GPT.

Nous utiliserons `parted` pour nos exemples.

### Lister les Partitions Existantes

Avant d'apporter des modifications, il est crucial d'identifier votre disque et sa configuration actuelle. Un moyen rapide d'y parvenir est d'utiliser la commande `sudo parted -l`, qui liste les tables de partitions pour tous les périphériques de bloc connectés.

```bash
sudo parted -l
```

Cette commande vous aide à trouver le nom de périphérique correct, tel que `/dev/sdb`, avant de commencer à le modifier.

### Lancer le Mode Interactif

Pour commencer à effectuer des modifications, lancez `parted` en mode interactif. Supposons que votre périphérique cible soit `/dev/sdb`.

```bash
sudo parted
```

Vous entrerez dans le shell de l'outil `parted`, où vous pourrez exécuter des commandes pour gérer les partitions de votre périphérique.

### Sélectionner un Périphérique

Une fois dans le shell `parted`, vous devez sélectionner le disque que vous souhaitez modifier. Soyez très prudent en choisissant le bon pour éviter toute perte de données.

```bash
select /dev/sdb
```

### Afficher la Table de Partitions

Utilisez la commande `print` pour afficher la table de partitions du disque sélectionné.

```plaintext
(parted) print
Model: ATA VBOX HARDDISK (scsi)
Disk /dev/sdb: 10.7GB
Sector size (logical/physical): 512B/512B
Partition Table: msdos
Disk Flags:

Number  Start   End     Size    Type      File system  Flags
 1      1049kB  10.7GB  10.7GB  primary   ext4         boot
```

Ce résultat montre les partitions disponibles sur le périphérique. Les colonnes **Start** et **End** indiquent où se situe chaque partition sur le disque.

### Créer une Partition

La commande `mkpart` crée une nouvelle partition. Vous devez spécifier le type de partition (par exemple, `primary`), un type de système de fichiers optionnel, ainsi que les points de début et de fin.

```bash
mkpart primary ext4 1MB 5000MB
```

Cette commande crée une partition primaire formatée avec ext4, commençant à 1MB et se terminant à 5000MB.

### Redimensionner une Partition

Vous pouvez également redimensionner une partition existante avec la commande `resize`. Vous aurez besoin du numéro de partition et des nouveaux points de début et de fin.

```bash
resize 1 1MB 8000MB
```

Cette commande redimensionne la partition numéro 1 pour qu'elle se termine à la marque des 8000MB.

`parted` est un outil très puissant. Vérifiez toujours vos commandes avant de les exécuter pour éviter toute perte de données accidentelle.

## Exercise

La pratique rend parfait ! Voici quelques laboratoires pratiques pour renforcer votre compréhension du partitionnement de disque Linux et de la gestion des systèmes de fichiers :

1. [Gérer les Partitions et les Systèmes de Fichiers Linux](https://labex.io/fr/labs/comptia-manage-linux-partitions-and-filesystems-590845) - Dans ce laboratoire, vous apprendrez à gérer les partitions de disque et les systèmes de fichiers sous Linux. Vous utiliserez fdisk pour créer une nouvelle partition, la formater avec ext4, la monter, configurer le montage persistant dans /etc/fstab, et créer une partition swap, le tout sur un disque virtuel secondaire sécurisé.

Ce laboratoire vous aidera à appliquer les concepts de partitionnement de disque et de gestion de système de fichiers dans un scénario réel et à renforcer votre confiance dans ces compétences essentielles d'administration Linux.

## Quiz Question

Quelle est la commande `parted` pour créer une partition ? (Veuillez répondre en anglais, en faisant attention à la casse).

## Quiz Answer

mkpart
