---
index: 8
lang: "fr"
title: "swap"
meta_title: "swap - L'espace d'échange"
meta_description: "Découvrez l'espace swap Linux, son fonctionnement, et comment créer et gérer les partitions d'échange. Optimisez l'utilisation de la mémoire de votre système avec ce guide !"
meta_keywords: "swap Linux, mkswap, swapon, swapoff, /etc/fstab, mémoire virtuelle, débutant Linux, tutoriel Linux"
---

## Lesson Content

Dans notre exemple précédent, je vous ai montré comment visualiser votre table de partitions. Revenons à cet exemple, plus spécifiquement à cette ligne :

```
Number  Start   End     Size    Type      File system     Flags
 5      6861MB  7380MB  519MB   logical   linux-swap(v1)
```

Qu'est-ce que cette partition swap ? Eh bien, le swap est ce que nous utilisons pour allouer de la mémoire virtuelle à notre système. Si votre mémoire est faible, le système utilise cette partition pour "échanger" des morceaux de mémoire des processus inactifs vers le disque, afin que vous ne soyez pas ralenti par un manque de mémoire.

### Utilisation d'une partition pour l'espace swap

Disons que nous voulions configurer notre partition `/dev/sdb2` pour être utilisée comme espace swap.

1. Assurez-vous d'abord que nous n'avons rien sur la partition.
2. Exécutez : `mkswap /dev/sdb2` pour initialiser les zones de swap.
3. Exécutez : `swapon /dev/sdb2`. Cela activera le périphérique de swap.
4. Si vous souhaitez que la partition swap persiste au démarrage, vous devez ajouter une entrée au fichier `/etc/fstab`. `sw` est le type de système de fichiers que vous utiliserez.
5. Pour supprimer le swap : `swapoff /dev/sdb2`.

En général, vous devriez allouer environ deux fois plus d'espace swap que de mémoire vive. Cependant, les systèmes modernes sont généralement suffisamment puissants et disposent déjà de suffisamment de RAM.

## Exercise

La pratique rend parfait ! Voici quelques laboratoires pratiques pour renforcer votre compréhension de l'espace swap Linux et de la gestion de la mémoire virtuelle :

1. **[Créer et Activer un Fichier Swap sous Linux](https://labex.io/fr/labs/comptia-create-and-activate-a-swap-file-in-linux-590858)** - Entraînez-vous à créer et activer un fichier swap, une compétence cruciale pour gérer la mémoire virtuelle de votre système.

Ce laboratoire vous aidera à appliquer les concepts des partitions swap dans des scénarios réels et à renforcer votre confiance dans la gestion des ressources système.

## Quiz Question

Quel est la commande pour activer l'espace swap sur un périphérique ?

## Quiz Answer

swapon
