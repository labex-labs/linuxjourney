---
lang: "fr"
title: "Création de systèmes de fichiers"
meta_description: "Apprenez à créer des systèmes de fichiers sur Linux en utilisant mkfs. Ce guide convivial pour les débutants couvre ext4 et le partitionnement de disque. Commencez votre parcours Linux !"
meta_keywords: "mkfs, créer un système de fichiers, ext4, partitionnement Linux, tutoriel Linux, Linux pour débutants, gestion de disque, guide Linux"
---

## Lesson Content

Maintenant que vous avez réellement partitionné un disque, créons un système de fichiers !

```bash
sudo mkfs -t ext4 /dev/sdb2
```

C'est aussi simple que ça ! L'outil **mkfs** (make filesystem) nous permet de spécifier le type de système de fichiers que nous voulons et où nous le voulons. Vous ne voudrez créer un système de fichiers que sur un disque nouvellement partitionné ou si vous repartitionnez un ancien. Vous laisserez très probablement votre système de fichiers dans un état corrompu si vous essayez d'en créer un par-dessus un existant.

## Exercise

Créez un système de fichiers ext4 sur la clé USB.

## Quiz Question

Quelle commande est utilisée pour créer un système de fichiers ?

## Quiz Answer

mkfs
