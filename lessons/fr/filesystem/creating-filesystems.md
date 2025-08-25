---
index: 5
lang: "fr"
title: "Création de systèmes de fichiers"
meta_title: "Création de systèmes de fichiers - Le système de fichiers"
meta_description: "Apprenez à créer des systèmes de fichiers sur Linux en utilisant mkfs. Ce guide convivial pour débutants couvre ext4 et le partitionnement de disque. Commencez votre parcours Linux !"
meta_keywords: "mkfs, créer un système de fichiers, ext4, partitionnement Linux, tutoriel Linux, Linux pour débutants, gestion de disque, guide Linux"
---

## Lesson Content

Maintenant que vous avez réellement partitionné un disque, créons un système de fichiers !

```bash
sudo mkfs -t ext4 /dev/sdb2
```

C'est aussi simple que ça ! L'outil **mkfs** (make filesystem) nous permet de spécifier le type de système de fichiers que nous voulons et où nous le voulons. Vous ne voudrez créer un système de fichiers que sur un disque nouvellement partitionné ou si vous en repartitionnez un ancien. Vous laisserez très probablement votre système de fichiers dans un état corrompu si vous essayez d'en créer un par-dessus un existant.

## Exercise

La pratique rend parfait ! Voici quelques laboratoires pratiques pour renforcer votre compréhension de la gestion des systèmes de fichiers Linux :

1. **[Gérer les partitions et les systèmes de fichiers Linux](https://labex.io/fr/labs/comptia-manage-linux-partitions-and-filesystems-590845)** - Dans ce laboratoire, vous apprendrez à gérer les partitions de disque et les systèmes de fichiers sous Linux. Vous utiliserez fdisk pour créer une nouvelle partition, la formater avec ext4 (en utilisant `mkfs`), la monter, configurer le montage persistant dans /etc/fstab, et créer une partition swap, le tout sur un disque virtuel secondaire sécurisé.

Ce laboratoire vous aidera à appliquer les concepts de création et de gestion de systèmes de fichiers dans des scénarios réels et à renforcer votre confiance dans la gestion des disques sous Linux.

## Quiz Question

Quelle commande est utilisée pour créer un système de fichiers ?

## Quiz Answer

mkfs
