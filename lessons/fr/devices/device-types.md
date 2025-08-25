---
index: 2
lang: "fr"
title: "types de périphériques"
meta_title: "types de périphériques - Périphériques"
meta_description: "Découvrez les types de périphériques Linux (caractère, bloc, tube, socket) et comment les identifier à l'aide de `ls -l /dev`. Comprenez les numéros de périphérique majeur/mineur. Tutoriel Linux pour débutants."
meta_keywords: "types de périphériques Linux, ls -l /dev, périphérique de caractères, périphérique de blocs, numéro de périphérique majeur mineur, tutoriel Linux, guide Linux, débutant"
---

## Lesson Content

Avant de discuter de la gestion des périphériques, examinons quelques-uns d'entre eux.

```bash
$ ls -l /dev
brw-rw----   1 root disk      8,   0 Dec 20 20:13 sda
crw-rw-rw-   1 root root      1,   3 Dec 20 20:13 null
srw-rw-rw-   1 root root           0 Dec 20 20:13 log
prw-r--r--   1 root root           0 Dec 20 20:13 fdata
```

Les colonnes sont les suivantes, de gauche à droite :

- Permissions
- Owner
- Group
- Major Device Number
- Minor Device Number
- Timestamp
- Device Name

Rappelez-vous, dans la commande `ls`, vous pouvez voir le type de fichier avec le premier bit sur chaque ligne. Les fichiers de périphérique sont désignés comme suit :

- c - caractère
- b - bloc
- p - pipe
- s - socket

### Périphérique de caractères

Ces périphériques transfèrent des données, mais un caractère à la fois. Vous verrez beaucoup de pseudo-périphériques (`/dev/null`) comme des périphériques de caractères. Ces périphériques ne sont pas réellement connectés physiquement à la machine, mais ils offrent au système d'exploitation une plus grande fonctionnalité.

### Périphérique de blocs

Ces périphériques transfèrent des données, mais par grands blocs de taille fixe. Vous verrez le plus souvent des périphériques qui utilisent des blocs de données comme périphériques de blocs, tels que les disques durs, les systèmes de fichiers, etc.

### Périphérique de tube (pipe)

Les tubes nommés permettent à deux processus ou plus de communiquer entre eux. Ils sont similaires aux périphériques de caractères, mais au lieu d'envoyer la sortie à un périphérique, elle est envoyée à un autre processus.

### Périphérique de socket

Les périphériques de socket facilitent la communication entre les processus, de manière similaire aux périphériques de tube, mais ils peuvent communiquer avec de nombreux processus simultanément.

### Caractérisation des périphériques

Les périphériques sont caractérisés à l'aide de deux nombres : le **numéro de périphérique majeur** et le **numéro de périphérique mineur**. Vous pouvez voir ces nombres dans l'exemple `ls` ci-dessus ; ils sont séparés par une virgule. Par exemple, supposons qu'un périphérique ait les numéros de périphérique : **8, 0** :

Le numéro de périphérique majeur représente le pilote de périphérique utilisé, dans ce cas 8, qui est souvent le numéro majeur pour les périphériques de blocs sd. Le numéro mineur indique au noyau quel périphérique unique il s'agit dans cette classe de pilotes ; dans ce cas, 0 est utilisé pour représenter le premier périphérique (a).

## Exercise

La pratique rend parfait ! Voici quelques laboratoires pratiques pour renforcer votre compréhension des fichiers de périphériques Linux et de leur gestion :

1. **[Gérer les partitions et les systèmes de fichiers Linux](https://labex.io/fr/labs/comptia-manage-linux-partitions-and-filesystems-590845)** - Entraînez-vous à créer et à gérer des partitions de disque et des systèmes de fichiers, qui sont des périphériques de blocs fondamentaux sous Linux.
2. **[Explorer les périphériques matériels sous Linux](https://labex.io/fr/labs/comptia-explore-hardware-devices-in-linux-590861)** - Apprenez à identifier et à inspecter divers périphériques matériels, en comprenant comment ils sont représentés dans le répertoire `/dev`.
3. **[Créer et activer un fichier d'échange sous Linux](https://labex.io/fr/labs/comptia-create-and-activate-a-swap-file-in-linux-590858)** - Acquérez une expérience pratique de la création et de l'activation d'un fichier d'échange, qui fonctionne comme un périphérique de mémoire virtuelle.

Ces laboratoires vous aideront à appliquer les concepts d'interaction et de gestion des périphériques dans des scénarios réels et à renforcer votre confiance en l'administration des systèmes Linux.

## Quiz Question

Quel est le symbole pour les périphériques de caractères dans la commande `ls -l` ?

## Quiz Answer

c
