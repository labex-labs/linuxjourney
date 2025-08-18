---
lang: "fr"
title: "Réparation du système de fichiers"
meta_title: "Réparation du système de fichiers - Le Filesystem"
meta_description: "Apprenez à utiliser fsck pour la réparation du système de fichiers Linux et la récupération de données. Comprenez comment vérifier et corriger les erreurs de disque avec cette commande essentielle. Commencez votre parcours Linux !"
meta_keywords: "fsck, réparation du système de fichiers, commandes Linux, erreurs de disque, récupération de données, tutoriel Linux, guide pour débutants"
---

## Lesson Content

Parfois, notre système de fichiers n'est pas toujours dans les meilleures conditions. Si nous avons un arrêt soudain, nos données peuvent être corrompues. C'est au système d'essayer de nous remettre dans un état de fonctionnement (bien que nous puissions certainement essayer nous-mêmes).

La commande **fsck** (filesystem check) est utilisée pour vérifier la cohérence d'un système de fichiers et peut même essayer de le réparer pour nous. Habituellement, lorsque vous démarrez un disque, fsck s'exécute avant que votre disque ne soit monté pour s'assurer que tout va bien. Parfois, cependant, votre disque est si endommagé que vous devrez le faire manuellement. Cependant, assurez-vous de le faire pendant que vous êtes sur un disque de secours ou quelque part où vous pouvez accéder à votre système de fichiers sans qu'il ne soit monté.

```bash
sudo fsck /dev/sda
```

## Exercise

Consultez la page de manuel de fsck pour voir ce qu'il peut faire d'autre.

## Quiz Question

Quelle commande est utilisée pour vérifier l'intégrité d'un système de fichiers ?

## Quiz Answer

fsck
