---
index: 2
lang: "fr"
title: "types de périphériques"
meta_title: "types de périphériques - Périphériques"
meta_description: "Découvrez les types de périphériques Linux (caractère, bloc, tube, socket) et comment les identifier à l'aide de `ls -l /dev`. Comprenez les numéros de périphérique majeur/mineur. Tutoriel Linux pour débutants."
meta_keywords: "types de périphériques Linux, ls -l /dev, périphérique de caractères, périphérique de blocs, numéro de périphérique majeur mineur, tutoriel Linux, guide Linux, débutant"
---

## Lesson Content

Avant de discuter de la gestion des périphériques, examinons quelques périphériques.

```bash
$ ls -l /dev
brw-rw----   1 root disk      8,   0 Dec 20 20:13 sda
crw-rw-rw-   1 root root      1,   3 Dec 20 20:13 null
srw-rw-rw-   1 root root           0 Dec 20 20:13 log
prw-r--r--   1 root root           0 Dec 20 20:13 fdata
```

Les colonnes sont les suivantes de gauche à droite :

- Permissions
- Owner
- Group
- Major Device Number
- Minor Device Number
- Timestamp
- Device Name

N'oubliez pas que dans la commande `ls`, vous pouvez voir le type de fichier avec le premier bit sur chaque ligne. Les fichiers de périphérique sont désignés comme suit :

- c - character
- b - block
- p - pipe
- s - socket

### Character Device

Ces périphériques transfèrent des données, mais un caractère à la fois. Vous verrez beaucoup de pseudo-périphériques (`/dev/null`) comme des périphériques de caractères. Ces périphériques ne sont pas réellement connectés physiquement à la machine, mais ils permettent au système d'exploitation une plus grande fonctionnalité.

### Block Device

Ces périphériques transfèrent des données, mais par grands blocs de taille fixe. Vous verrez le plus souvent des périphériques qui utilisent des blocs de données comme des périphériques de blocs, tels que les disques durs, les systèmes de fichiers, etc.

### Pipe Device

Les tubes nommés permettent à deux processus ou plus de communiquer entre eux. Ceux-ci sont similaires aux périphériques de caractères, mais au lieu d'envoyer la sortie à un périphérique, elle est envoyée à un autre processus.

### Socket Device

Les périphériques de socket facilitent la communication entre les processus, de manière similaire aux périphériques de tube, mais ils peuvent communiquer avec de nombreux processus à la fois.

### Device Characterization

Les périphériques sont caractérisés à l'aide de deux nombres : le **numéro de périphérique majeur** et le **numéro de périphérique mineur**. Vous pouvez voir ces nombres dans l'exemple `ls` ci-dessus ; ils sont séparés par une virgule. Par exemple, supposons qu'un périphérique ait les numéros de périphérique : **8, 0** :

Le numéro de périphérique majeur représente le pilote de périphérique utilisé, dans ce cas 8, qui est souvent le numéro majeur pour les périphériques de bloc sd. Le numéro mineur indique au noyau de quel périphérique unique il s'agit dans cette classe de pilotes ; dans ce cas, 0 est utilisé pour représenter le premier périphérique (a).

## Exercise

Regardez votre répertoire `/dev` et découvrez les types de périphériques que vous pouvez voir.

## Quiz Question

Quel est le symbole pour les périphériques de caractères dans la commande `ls -l` ?

## Quiz Answer

c
