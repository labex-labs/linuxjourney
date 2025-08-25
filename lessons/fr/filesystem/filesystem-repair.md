---
index: 10
lang: "fr"
title: "Réparation du système de fichiers"
meta_title: "Réparation du système de fichiers - Le système de fichiers"
meta_description: "Apprenez à utiliser fsck pour la réparation du système de fichiers Linux et la récupération de données. Comprenez comment vérifier et corriger les erreurs de disque avec cette commande essentielle. Commencez votre parcours Linux !"
meta_keywords: "fsck, réparation du système de fichiers, commandes Linux, erreurs de disque, récupération de données, tutoriel Linux, guide du débutant"
---

## Lesson Content

Parfois, notre système de fichiers n'est pas toujours dans les meilleures conditions. Si nous avons un arrêt soudain, nos données peuvent être corrompues. C'est au système d'essayer de nous remettre dans un état de fonctionnement (bien que nous puissions certainement essayer nous-mêmes).

La commande **fsck** (filesystem check) est utilisée pour vérifier la cohérence d'un système de fichiers et peut même essayer de le réparer pour nous. Habituellement, lorsque vous démarrez un disque, fsck s'exécute avant que votre disque ne soit monté pour s'assurer que tout est en ordre. Parfois, cependant, votre disque est si endommagé que vous devrez le faire manuellement. Cependant, assurez-vous de le faire pendant que vous êtes sur un disque de secours ou à un endroit où vous pouvez accéder à votre système de fichiers sans qu'il ne soit monté.

```bash
sudo fsck /dev/sda
```

## Exercise

La pratique rend parfait ! Voici quelques laboratoires pratiques pour renforcer votre compréhension des systèmes de fichiers Linux et de leur gestion :

1. **[Gérer les partitions et les systèmes de fichiers Linux](https://labex.io/fr/labs/comptia-manage-linux-partitions-and-filesystems-590845)** - Dans ce laboratoire, vous acquerrez une expérience pratique de la création, du formatage et du montage de partitions, ce qui est crucial pour comprendre comment les systèmes de fichiers sont structurés et maintenus. Cette connaissance fondamentale vous aidera à mieux appréhender des concepts tels que l'intégrité et la récupération des systèmes de fichiers.

Ces laboratoires vous aideront à appliquer les concepts dans des scénarios réels et à renforcer votre confiance dans l'administration des systèmes de fichiers Linux.

## Quiz Question

Quelle commande est utilisée pour vérifier l'intégrité d'un système de fichiers ?

## Quiz Answer

fsck
