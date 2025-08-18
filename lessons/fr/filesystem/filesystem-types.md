---
index: 2
lang: "fr"
title: "Types de systèmes de fichiers"
meta_title: "Types de systèmes de fichiers - Le Filesystem"
meta_description: "Découvrez les types de systèmes de fichiers Linux comme ext4, Btrfs et XFS. Comprenez le journaling et le VFS pour des données cohérentes. Explorez les systèmes de fichiers Linux courants dans ce guide pour débutants."
meta_keywords: "types de systèmes de fichiers Linux, ext4, Btrfs, XFS, journaling, VFS, tutoriel Linux, guide pour débutants"
---

## Lesson Content

Il existe de nombreuses implémentations de systèmes de fichiers différentes. Certains sont plus rapides que d'autres, certains prennent en charge le stockage de plus grande capacité, et d'autres ne fonctionnent qu'avec le stockage de plus petite capacité. Les différents systèmes de fichiers ont différentes façons d'organiser leurs données, et nous allons détailler les types de systèmes de fichiers existants. Puisqu'il existe tant d'implémentations différentes, les applications ont besoin d'un moyen de gérer les différentes opérations. Il existe donc une couche d'abstraction appelée Virtual File System (VFS). C'est une couche entre les applications et les différents types de systèmes de fichiers, de sorte que, quel que soit le système de fichiers que vous avez, vos applications pourront fonctionner avec.

Vous pouvez avoir plusieurs systèmes de fichiers sur vos disques, selon la façon dont ils sont partitionnés, et nous aborderons cela dans une prochaine leçon.

### Journaling

Le journaling est activé par défaut sur la plupart des types de systèmes de fichiers, mais au cas où ce ne serait pas le cas, vous devriez savoir ce qu'il fait. Supposons que vous copiez un gros fichier et que tout d'un coup vous perdez l'alimentation. Eh bien, si vous êtes sur un système de fichiers non journalisé, le fichier serait corrompu et votre système de fichiers serait incohérent. Ensuite, lorsque vous redémarrez, votre système effectuerait une vérification du système de fichiers pour s'assurer que tout est en ordre. Cependant, les réparations pourraient prendre un certain temps en fonction de la taille de votre système de fichiers.

Maintenant, si vous étiez sur un système journalisé, avant même que votre machine ne commence à copier le fichier, elle écrira ce que vous allez faire dans un fichier journal (journal). Lorsque vous copiez réellement le fichier, une fois terminé, le journal marque cette tâche comme terminée. Le système de fichiers est toujours dans un état cohérent grâce à cela, il saura donc exactement où vous en étiez si votre machine s'arrêtait soudainement. Cela diminue également le temps de démarrage car au lieu de vérifier l'ensemble du système de fichiers, il ne regarde que votre journal.

### Common Desktop Filesystem Types

- ext4 - C'est la version la plus actuelle des systèmes de fichiers natifs Linux. Il est compatible avec les anciennes versions ext2 et ext3. Il prend en charge des volumes de disque allant jusqu'à 1 exaoctet et des tailles de fichiers allant jusqu'à 16 téraoctets et bien plus encore. C'est le choix standard pour les systèmes de fichiers Linux.
- Btrfs - "Better or Butter FS" est un nouveau système de fichiers pour Linux qui offre des instantanés, des sauvegardes incrémentielles, une augmentation des performances, et bien plus encore. Il est largement disponible, mais pas encore tout à fait stable et compatible.
- XFS - Système de fichiers journalisé haute performance, idéal pour un système avec de gros fichiers comme un serveur multimédia.
- NTFS and FAT - Systèmes de fichiers Windows
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

Faites une petite recherche en ligne sur les autres types de systèmes de fichiers : ReiserFS, ZFS, JFS, et d'autres que vous pouvez trouver.

## Quiz Question

Quel est le type de système de fichiers Linux courant ?

## Quiz Answer

ext4
