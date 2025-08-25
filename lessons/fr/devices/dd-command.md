---
index: 7
lang: "fr"
title: "dd"
meta_title: "dd - Périphériques"
meta_description: "Apprenez la commande Linux dd pour la copie de données et l'imagerie disque. Comprenez ses options comme if, of et bs. Commencez votre parcours de gestion de données Linux !"
meta_keywords: "commande dd, Linux dd, copier des données, imagerie disque, tutoriel Linux, débutant, guide, sauvegarde de données"
---

## Lesson Content

L'outil `dd` est super utile pour convertir et copier des données. Il lit l'entrée d'un fichier ou d'un flux de données et l'écrit dans un fichier ou un flux de données.

Considérez la commande suivante :

```bash
dd if=/home/pete/backup.img of=/dev/sdb bs=1024
```

Cette commande copie le contenu de `backup.img` vers `/dev/sdb`. Elle copiera les données par blocs de 1024 octets jusqu'à ce qu'il n'y ait plus de données à copier.

- `if=file` - Fichier d'entrée ; lit à partir d'un fichier au lieu de l'entrée standard.
- `of=file` - Fichier de sortie ; écrit dans un fichier au lieu de la sortie standard.
- `bs=bytes` - Taille de bloc ; il lit et écrit ce nombre d'octets de données à la fois. Vous pouvez utiliser différentes métriques de taille en désignant la taille avec un `k` pour kilooctet, `m` pour mégaoctet, etc., donc 1024 octets est 1k.
- `count=number` - Nombre de blocs à copier.

Vous verrez des commandes `dd` qui utilisent l'option `count`. Habituellement, avec `dd`, si vous voulez copier un fichier d'un mégaoctet, vous voudrez généralement voir ce fichier comme un mégaoctet une fois la copie terminée. Supposons que vous exécutiez la commande suivante :

```bash
dd if=/home/pete/backup.img of=/dev/sdb bs=1M count=2
```

Notre fichier `backup.img` fait 10M ; cependant, nous disons dans cette commande de copier 1M 2 fois, donc seulement 2M sont copiés, laissant nos données copiées incomplètes. `count` peut être utile dans de nombreuses situations, mais si vous ne faites que copier des données, vous pouvez pratiquement omettre `count` et même `bs` d'ailleurs. Si vous voulez vraiment optimiser vos transferts de données, alors vous voudrez commencer à utiliser ces options.

`dd` est extrêmement puissant ; vous pouvez l'utiliser pour faire des sauvegardes de n'importe quoi, y compris des disques durs entiers, restaurer des images disque, et plus encore. Soyez prudent, cet outil puissant peut avoir un prix si vous n'êtes pas sûr de ce que vous faites.

## Exercise

La pratique rend parfait ! Voici quelques laboratoires pratiques pour renforcer votre compréhension de la manipulation des données et de la gestion des disques sous Linux :

1. **[Créer et Restaurer une Sauvegarde avec tar sous Linux](https://labex.io/fr/labs/comptia-create-and-restore-a-backup-with-tar-in-linux-590843)** - Entraînez-vous à créer et restaurer des sauvegardes de systèmes de fichiers, une compétence essentielle liée à l'intégrité et à la récupération des données, pour laquelle `dd` peut également être utilisé.
2. **[Gérer les Partitions et les Systèmes de Fichiers Linux](https://labex.io/fr/labs/comptia-manage-linux-partitions-and-filesystems-590845)** - Apprenez à gérer les partitions de disque et les systèmes de fichiers, y compris la création, le formatage et le montage, qui sont des concepts fondamentaux lorsque vous travaillez avec des outils comme `dd` pour l'imagerie disque.

Ces laboratoires vous aideront à appliquer les concepts de manipulation des données et d'opérations sur disque dans des scénarios réels et à renforcer votre confiance dans les tâches d'administration système.

## Quiz Question

Quelle est l'option `dd` pour la taille de bloc ?

## Quiz Answer

bs
