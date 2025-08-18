---
index: 8
lang: "fr"
title: "swap"
meta_title: "swap - Le Filesystem"
meta_description: "Découvrez l'espace de swap Linux, son fonctionnement, et comment créer et gérer des partitions de swap. Optimisez l'utilisation de la mémoire de votre système avec ce guide !"
meta_keywords: "swap Linux, mkswap, swapon, swapoff, /etc/fstab, mémoire virtuelle, débutant Linux, tutoriel Linux"
---

## Lesson Content

Dans notre exemple précédent, je vous ai montré comment visualiser votre table de partitions. Revoyons cet exemple, plus précisément cette ligne :

```
Number  Start   End     Size    Type      File system     Flags
 5      6861MB  7380MB  519MB   logical   linux-swap(v1)
```

Qu'est-ce que cette partition swap ? Eh bien, le swap est ce que nous utilisons pour allouer de la mémoire virtuelle à notre système. Si vous manquez de mémoire, le système utilise cette partition pour « échanger » des morceaux de mémoire de processus inactifs vers le disque, afin que vous ne soyez pas ralenti par le manque de mémoire.

### Utilisation d'une partition pour l'espace de swap

Supposons que nous voulions utiliser notre partition `/dev/sdb2` pour l'espace de swap.

1. Tout d'abord, assurez-vous que la partition est vide.
2. Exécutez : `mkswap /dev/sdb2` pour initialiser les zones de swap.
3. Exécutez : `swapon /dev/sdb2`. Cela activera le périphérique de swap.
4. Si vous voulez que la partition de swap persiste au démarrage, vous devez ajouter une entrée au fichier `/etc/fstab`. `sw` est le type de système de fichiers que vous utiliserez.
5. Pour supprimer le swap : `swapoff /dev/sdb2`.

En général, vous devriez allouer environ deux fois plus d'espace de swap que de mémoire. Cependant, les systèmes modernes sont aujourd'hui généralement suffisamment puissants et disposent de suffisamment de RAM.

## Exercise

Partitionnez l'espace libre du lecteur USB pour l'espace de swap.

## Quiz Question

Quelle est la commande pour activer l'espace de swap sur un périphérique ?

## Quiz Answer

swapon
