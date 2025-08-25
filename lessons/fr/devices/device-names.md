---
index: 3
lang: "fr"
title: "Noms des périphériques"
meta_title: "Noms des périphériques - Périphériques"
meta_description: "Apprenez les noms des périphériques Linux comme les périphériques SCSI (sd), pseudo et PATA (hd). Comprenez /dev/sda, /dev/null, et plus encore dans ce guide pour débutants."
meta_keywords: "noms de périphériques Linux, /dev, périphériques SCSI, périphériques pseudo, périphériques PATA, tutoriel Linux, Linux pour débutants, fichiers de périphériques"
---

## Lesson Content

Voici les noms de périphériques les plus courants que vous rencontrerez :

### Périphériques SCSI

Si vous avez une sorte de stockage de masse sur votre machine, il y a de fortes chances qu'il utilise le protocole SCSI (prononcé "scuzzy"). SCSI signifie Small Computer System Interface ; c'est un protocole utilisé pour permettre la communication entre les disques, les imprimantes, les scanners et d'autres périphériques et votre système. Vous avez peut-être entendu parler des périphériques SCSI, qui ne sont plus réellement utilisés dans les systèmes modernes ; cependant, nos systèmes Linux associent les disques SCSI aux disques durs dans `/dev`. Ils sont représentés par un préfixe `sd` (disque SCSI) :

Fichiers de périphériques SCSI courants :

- `/dev/sda` - Premier disque dur
- `/dev/sdb` - Deuxième disque dur
- `/dev/sda3` - Troisième partition sur le premier disque dur

### Périphériques Pseudo

Comme nous l'avons vu précédemment, les périphériques pseudo ne sont pas réellement connectés physiquement à votre système. La plupart des périphériques pseudo courants sont des périphériques de caractères :

- `/dev/zero` - accepte et ignore toutes les entrées, produit un flux continu d'octets NULL (valeur zéro)
- `/dev/null` - accepte et ignore toutes les entrées, ne produit aucune sortie
- `/dev/random` - produit des nombres aléatoires

### Périphériques PATA

Parfois, dans les systèmes plus anciens, vous pouvez voir des disques durs désignés par un préfixe `hd` :

- `/dev/hda` - Premier disque dur
- `/dev/hdd2` - Deuxième partition sur le 4ème disque dur

## Exercise

La pratique rend parfait ! Voici quelques laboratoires pratiques pour renforcer votre compréhension des noms de périphériques Linux et de la gestion du stockage :

1. **[Gérer les partitions et les systèmes de fichiers Linux](https://labex.io/fr/labs/comptia-manage-linux-partitions-and-filesystems-590845)** - Entraînez-vous à créer, formater et monter des partitions, ce qui implique directement de travailler avec des noms de périphériques.
2. **[Explorer les périphériques matériels sous Linux](https://labex.io/fr/labs/comptia-explore-hardware-devices-in-linux-590861)** - Apprenez à identifier et à inspecter divers périphériques matériels et leurs noms associés dans un environnement Linux.

Ces laboratoires vous aideront à appliquer les concepts dans des scénarios réels et à renforcer votre confiance dans la gestion du stockage et la compréhension du matériel sous Linux.

## Quiz Question

Quel serait généralement le nom du périphérique pour la première partition sur le deuxième disque SCSI ?

## Quiz Answer

sdb1
