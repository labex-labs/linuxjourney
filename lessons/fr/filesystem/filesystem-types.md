---
index: 2
lang: "fr"
title: "Types de systèmes de fichiers"
meta_title: "Types de systèmes de fichiers - Le système de fichiers"
meta_description: "Découvrez les types de systèmes de fichiers Linux comme ext4, Btrfs et XFS. Comprenez la journalisation et le VFS pour une cohérence des données. Explorez les systèmes de fichiers Linux courants dans ce guide pour débutants."
meta_keywords: "types de systèmes de fichiers Linux, ext4, Btrfs, XFS, journalisation, VFS, tutoriel Linux, guide pour débutants"
---

## Lesson Content

Il existe de nombreuses implémentations de systèmes de fichiers différentes. Certaines sont plus rapides que d'autres, certaines prennent en charge des stockages de plus grande capacité, et d'autres ne fonctionnent que sur des stockages de plus petite capacité. Les différents systèmes de fichiers ont des manières différentes d'organiser leurs données, et nous allons détailler les types de systèmes de fichiers existants. Puisqu'il y a tant d'implémentations différentes disponibles, les applications ont besoin d'un moyen de gérer les différentes opérations. Il existe donc une couche d'abstraction appelée Système de Fichiers Virtuel (VFS). C'est une couche entre les applications et les différents types de systèmes de fichiers, donc quel que soit le système de fichiers que vous avez, vos applications pourront travailler avec.

Vous pouvez avoir de nombreux systèmes de fichiers sur vos disques, selon la façon dont ils sont partitionnés, et nous aborderons cela dans une prochaine leçon.

### Journalisation

La journalisation est activée par défaut sur la plupart des types de systèmes de fichiers, mais au cas où ce ne serait pas le cas, vous devriez savoir ce qu'elle fait. Supposons que vous copiez un gros fichier et que tout d'un coup vous perdez le courant. Eh bien, si vous êtes sur un système de fichiers non journalisé, le fichier serait corrompu et votre système de fichiers serait incohérent. Ensuite, lorsque vous redémarrez, votre système effectuerait une vérification du système de fichiers pour s'assurer que tout est en ordre. Cependant, les réparations pourraient prendre un certain temps en fonction de la taille de votre système de fichiers.

Maintenant, si vous étiez sur un système journalisé, avant même que votre machine ne commence à copier le fichier, elle écrira ce que vous allez faire dans un fichier journal (journal). Lorsque vous copiez réellement le fichier, une fois terminé, le journal marque cette tâche comme terminée. Le système de fichiers est toujours dans un état cohérent grâce à cela, il saura donc exactement où vous en étiez si votre machine s'est arrêtée soudainement. Cela diminue également le temps de démarrage car au lieu de vérifier l'ensemble du système de fichiers, il ne fait que consulter votre journal.

### Types de systèmes de fichiers de bureau courants

- ext4 - C'est la version la plus récente des systèmes de fichiers natifs de Linux. Elle est compatible avec les anciennes versions ext2 et ext3. Elle prend en charge des volumes de disque allant jusqu'à 1 exaoctet et des tailles de fichiers allant jusqu'à 16 téraoctets et bien plus encore. C'est le choix standard pour les systèmes de fichiers Linux.
- Btrfs - "Better or Butter FS" est un nouveau système de fichiers pour Linux qui offre des instantanés, des sauvegardes incrémentielles, une augmentation des performances, et bien plus encore. Il est largement disponible, mais pas encore tout à fait stable et compatible.
- XFS - Système de fichiers journalisé haute performance, idéal pour un système avec de gros fichiers comme un serveur multimédia.
- NTFS et FAT - Systèmes de fichiers Windows
- HFS+ - Système de fichiers Macintosh

Vérifiez quels systèmes de fichiers sont sur votre machine :

```plaintext
pete@icebox:~$ df -T
Filesystem     Type     1K-blocks    Used Available Use% Mounted on
/dev/sda1      ext4       6461592 2402708   3707604  40% /
udev           devtmpfs    501356       4    501352   1% /dev
tmpfs          tmpfs       102544    1068    101476   2% /run
/dev/sda6      xfs       13752320  460112  13292208   4% /home
```

La commande **df** rapporte l'utilisation de l'espace disque du système de fichiers et d'autres détails sur votre disque ; nous parlerons plus en détail de cet outil plus tard.

## Exercise

La pratique rend parfait ! Voici un laboratoire pratique pour renforcer votre compréhension des systèmes de fichiers et des partitions Linux :

1. **[Gérer les partitions et les systèmes de fichiers Linux](https://labex.io/fr/labs/comptia-manage-linux-partitions-and-filesystems-590845)** - Entraînez-vous à créer une nouvelle partition, à la formater, à la monter et à configurer un montage persistant, toutes des compétences fondamentales liées à la gestion des différentes implémentations de systèmes de fichiers.

Ce laboratoire vous aidera à appliquer les concepts dans des scénarios réels et à renforcer votre confiance dans la gestion du stockage disque sous Linux.

## Quiz Question

Quel est le type de système de fichiers Linux courant ?

## Quiz Answer

ext4
