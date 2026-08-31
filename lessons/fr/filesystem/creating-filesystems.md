---
lesson_id: "creating-filesystems"
course_id: "filesystem"
lang: "fr"
order_index: 5
title: "Créer des systèmes de fichiers"
description: "Découvrez comment vérifier un périphérique bloc cible et y créer un système de fichiers avec les outils propres à son format."
meta_title: "Créer des systèmes de fichiers - Le système de fichiers"
meta_description: "Apprenez à créer un système de fichiers sur une partition Linux avec mkfs, à formater en ext4 et à vérifier la cible."
meta_keywords: "mkfs, créer système de fichiers, ext4, partitionnement Linux, tutoriel Linux, gestion disque, formater disque Linux"
---

La création d'un système de fichiers écrit de nouvelles structures d'allocation et de métadonnées sur un périphérique bloc. Il s'agit d'une initialisation destructive, pas d'un simple changement d'étiquette. Utilisez uniquement un stockage jetable pour vous exercer et conservez une sauvegarde testée avant de formater un périphérique qui a déjà contenu des données importantes.

## Comprendre `mkfs`

`mkfs` est généralement une interface qui délègue l'opération à un programme propre au système de fichiers, comme `mkfs.ext4`, `mkfs.xfs` ou `mkfs.btrfs`. Une commande générique prend cette forme :

```bash
$ sudo mkfs -t ext4 /dev/PARTITION-VÉRIFIÉE
```

Ne remplacez le paramètre fictif qu'après vérification. La syntaxe équivalente propre au format est couramment :

```bash
$ sudo mkfs.ext4 /dev/PARTITION-VÉRIFIÉE
```

Les options prises en charge, valeurs par défaut, ensembles de fonctionnalités et demandes de confirmation avant écrasement diffèrent selon les implémentations. Consultez le manuel local de l'outil de formatage précis plutôt que de supposer que tous les moteurs de `mkfs` se comportent de la même façon.

:::single-choice{#creating-filesystems-mkfs-role}
Que demande `mkfs -t ext4 CIBLE` ?

::option[Le montage sans modification d'un système de fichiers existant.]{#creating-filesystems-mount-existing explanation="Le montage est une opération distincte ; mkfs initialise les métadonnées sur le périphérique."}
::option[La création des structures d'un système de fichiers ext4 sur la cible.]{#creating-filesystems-create-ext4 .correct explanation="L'interface sélectionne l'implémentation de formatage ext4 pour le périphérique bloc indiqué."}
::option[L'affichage de tous les systèmes de fichiers actuellement montés.]{#creating-filesystems-list-mounted explanation="Des outils comme `findmnt` réalisent l'inventaire des montages en lecture seule."}
:::

## Vérifier chaque couche de stockage

Avant le formatage, identifiez la cible par son modèle, son numéro de série, sa taille, sa topologie, son lien persistant et son rôle prévu :

```bash
$ lsblk -o NAME,PATH,TYPE,SIZE,MODEL,SERIAL,FSTYPE,UUID,MOUNTPOINTS
$ findmnt --real
$ sudo wipefs --no-act /dev/PARTITION-VÉRIFIÉE
```

`wipefs --no-act` signale les signatures reconnues sans les effacer. Vérifiez aussi l'utilisation par le swap, LVM, RAID, le chiffrement, les machines virtuelles, les conteneurs et les applications. Un périphérique peut être actif même si `MOUNTPOINTS` est vide.

Démontez ou désactivez chaque couche concernée avec son propre outil. Revérifiez l'identité juste avant de lancer le formatage, car les noms d'énumération peuvent changer.

:::single-choice{#creating-filesystems-wipefs-no-act}
Que fournit `wipefs --no-act CIBLE` dans cette méthode ?

::option[Un rapport en lecture seule des signatures reconnues.]{#creating-filesystems-signature-report .correct explanation="Le mode no-act aide à révéler les signatures de systèmes de fichiers, tables de partitions, RAID ou autres sans les supprimer."}
::option[Un nouveau système de fichiers vide prêt à monter.]{#creating-filesystems-wipefs-formats explanation="L'examen des signatures n'initialise pas un nouveau système de fichiers."}
::option[La garantie qu'aucun processus n'utilise la cible.]{#creating-filesystems-wipefs-no-users explanation="L'utilisation doit être vérifiée séparément dans les montages et l'ensemble de la pile de stockage."}
:::

## Choisir délibérément le système de fichiers

Choisissez un type pris en charge par la distribution, l'environnement de démarrage, les outils de sauvegarde et de réparation ainsi que la charge de travail. Tenez compte des limites requises, instantanés, sommes de contrôle, quotas, couches de chiffrement, possibilités d'agrandissement ou de réduction et accès multiplateforme.

Ne sélectionnez pas un format uniquement parce qu'il est répandu. Par exemple, ext4, XFS et Btrfs offrent des fonctions d'exploitation et des procédures de récupération différentes. Un périphérique amovible destiné à l'interopérabilité peut exiger un autre format, avec une sémantique différente pour les permissions Unix.

:::single-choice{#creating-filesystems-type-choice}
Sur quelle base est-il judicieux de choisir un type de système de fichiers ?

::option[Le nom le plus court à saisir.]{#creating-filesystems-shortest-name explanation="La longueur de la commande ne dit rien sur la durabilité, les fonctions ou la prise en charge."}
::option[La promesse qu'aucune panne de stockage ne pourra jamais se produire.]{#creating-filesystems-no-failure explanation="Aucun système de fichiers n'élimine les pannes matérielles ni le besoin de sauvegardes."}
::option[Les besoins de la charge et la prise en charge par les outils de sauvegarde, démarrage et récupération.]{#creating-filesystems-supported-workflow .correct explanation="Le format doit satisfaire les exigences techniques et les capacités d'exploitation et de récupération de l'environnement."}
:::

## Étiquettes, UUID et vérification

Les outils de formatage génèrent normalement un UUID de système de fichiers et permettent souvent de définir une étiquette lisible. Choisissez des étiquettes suffisamment uniques dans l'environnement et veillez à ce que des systèmes de fichiers clonés ne conservent pas d'identifiants conflictuels s'ils sont montés ensemble.

Après une création réussie, examinez le résultat sans le monter :

```bash
$ lsblk -f /dev/PARTITION-VÉRIFIÉE
$ sudo blkid /dev/PARTITION-VÉRIFIÉE
```

Consignez l'UUID pour la future configuration du montage. Créer un système de fichiers ne le monte pas, ne crée pas les répertoires applicatifs, ne restaure pas les sauvegardes et ne rend pas son montage persistant entre les démarrages.

:::single-choice{#creating-filesystems-after-mkfs}
Quelle opération reste distincte après la création d'un système de fichiers ?

::option[Le monter dans le répertoire prévu.]{#creating-filesystems-mount-separate .correct explanation="Le formatage écrit les structures du système de fichiers, tandis que le montage le rattache à l'arborescence visible."}
::option[Attribuer la moindre capacité au périphérique bloc.]{#creating-filesystems-capacity explanation="La partition ou le périphérique logique sous-jacent fournit déjà la capacité qui est formatée."}
::option[Créer de zéro le répertoire `/dev` du noyau.]{#creating-filesystems-create-dev explanation="La gestion des nœuds de périphériques est indépendante du formatage d'une cible."}
:::

Utilisez [Gérer les partitions et systèmes de fichiers Linux](https://labex.io/fr/labs/comptia-manage-linux-partitions-and-filesystems-590845) uniquement sur le disque secondaire jetable du laboratoire.

## Résumé

Vous savez maintenant décrire la création d'un système de fichiers comme une opération destructive précédée de vérifications.

1. Considérer `mkfs` comme une interface vers les outils propres aux formats.
2. Vérifier l'identité persistante, les signatures et chaque consommateur actif.
3. Choisir un système de fichiers selon les exigences de prise en charge et de récupération.
4. Examiner le type, l'étiquette et l'UUID générés avant le montage.
