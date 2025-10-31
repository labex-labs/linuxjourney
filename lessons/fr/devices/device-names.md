---
index: 3
lang: "fr"
title: "Noms des Périphériques"
meta_title: "Noms des Périphériques - Appareils"
meta_description: "Explorez les noms courants des périphériques Linux pour le stockage et les périphériques. Ce guide explique la convention de nommage des disques SCSI (comme sda), ce que signifie sda, et les pseudo-périphériques comme /dev/null."
meta_keywords: "noms périphériques linux, nom périphérique linux, que signifie sda, nom élément sd, quel serait le nom de périphérique courant pour la première partition sur le deuxième disque scsi, /dev, périphériques SCSI, périphériques pseudo, périphériques PATA"
---

## Lesson Content

Sous Linux, chaque périphérique est représenté par un fichier dans le répertoire `/dev`. Comprendre les conventions de nommage de ces fichiers est crucial pour l'administration système. Voici les types de noms de périphériques Linux les plus courants que vous rencontrerez.

### Périphériques SCSI et Stockage Modernes

Même si votre machine utilise un stockage moderne comme SATA, NVMe ou des lecteurs USB, le noyau Linux les gère souvent via son sous-système SCSI (Small Computer System Interface). C'est pourquoi le préfixe le plus courant pour les périphériques de stockage est `sd`, qui signifiait à l'origine "SCSI disk" (disque SCSI).

Le `sd element name` suit un schéma clair :

- Le préfixe `sd` indique un périphérique de stockage de masse.
- La lettre suivante représente le disque lui-même, attribuée dans l'ordre de détection (`a` pour le premier, `b` pour le second, et ainsi de suite).
- Un nombre à la fin indique la partition sur ce disque.

Les fichiers de périphériques SCSI courants incluent :

- `/dev/sda`: Le premier disque de stockage.
- `/dev/sdb`: Le deuxième disque de stockage.
- `/dev/sda3`: La troisième partition sur le premier disque de stockage.

Alors, quel serait couramment le nom du périphérique pour la première partition sur le deuxième disque SCSI ? En suivant le schéma, le deuxième disque est `sdb`, et sa première partition est `1`. Par conséquent, le nom du périphérique est `/dev/sdb1`.

### Pseudo-Périphériques

Les pseudo-périphériques sont des fichiers spéciaux qui ne correspondent à aucun matériel physique mais fournissent des fonctions système utiles. Ce sont généralement des périphériques de type caractère.

- `/dev/zero`: Accepte et supprime toutes les entrées. Lorsqu'il est lu, il produit un flux continu d'octets NULL (valeur zéro).
- `/dev/null`: Accepte et supprime toutes les entrées qui lui sont écrites, et ne produit aucune sortie lorsqu'il est lu.
- `/dev/random`: Produit un flux de nombres aléatoires générés à partir du bruit environnemental.

### Périphériques PATA Hérités

Sur les systèmes plus anciens, vous pourriez rencontrer des disques durs qui utilisent l'interface Parallel ATA (PATA). Le nom de périphérique Linux pour ces disques utilise le préfixe `hd`.

- `/dev/hda`: Le premier disque dur PATA.
- `/dev/hdd2`: La deuxième partition sur le quatrième disque dur PATA.

## Exercise

La pratique rend parfait ! Voici quelques laboratoires pratiques pour renforcer votre compréhension des noms de périphériques Linux et de la gestion du stockage :

1. **[Gérer les partitions et les systèmes de fichiers Linux](https://labex.io/fr/labs/comptia-manage-linux-partitions-and-filesystems-590845)** - Entraînez-vous à créer, formater et monter des partitions, ce qui implique directement de travailler avec des noms de périphériques.
2. **[Explorer les périphériques matériels sous Linux](https://labex.io/fr/labs/comptia-explore-hardware-devices-in-linux-590861)** - Apprenez à identifier et à inspecter divers périphériques matériels et leurs noms associés dans un environnement Linux.

Ces laboratoires vous aideront à appliquer les concepts dans des scénarios réels et à renforcer votre confiance dans la gestion du stockage et la compréhension du matériel sous Linux.

## Quiz Question

Quel serait couramment le nom du périphérique pour la première partition sur le deuxième disque SCSI ? Veuillez fournir la réponse en anglais, en faisant attention à la casse correcte.

## Quiz Answer

/dev/sdb1
