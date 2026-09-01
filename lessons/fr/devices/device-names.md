---
lesson_id: "device-names"
course_id: "devices"
lang: "fr"
order_index: 3
title: "Noms des Périphériques"
description: "Découvrez comment Linux nomme les périphériques de stockage courants, leurs partitions, les périphériques logiques et les liens persistants."
meta_title: "Noms des Périphériques - Appareils"
meta_description: "Explorez les noms courants des périphériques Linux pour le stockage et les périphériques. Ce guide explique la convention de nommage des disques SCSI (comme sda), ce que signifie sda, et les pseudo-périphériques comme /dev/null."
meta_keywords: "noms périphériques linux, nom périphérique linux, que signifie sda, nom élément sd, quel serait le nom de périphérique courant pour la première partition sur le deuxième disque scsi, /dev, périphériques SCSI, périphériques pseudo, périphériques PATA"
---

Les noms de périphériques Linux reflètent le sous-système et le pilote du noyau qui présentent l'interface, pas toujours le connecteur physique indiqué sur le matériel. Apprenez les motifs courants, mais découvrez la correspondance réelle du système actuel avant toute modification du stockage.

## Noms des disques de la couche SCSI

Les disques présentés par la couche disque SCSI utilisent couramment des noms en `sd`. Cela comprend de nombreux disques SCSI, SATA, USB et virtuels :

- `/dev/sda` : un disque entier ;
- `/dev/sdb` : un autre disque entier ;
- `/dev/sda3` : la partition 3 de `/dev/sda` ;
- `/dev/sdb1` : la partition 1 de `/dev/sdb`.

Les lettres reflètent l'ordre d'énumération, pas une identité durable. L'ajout d'un contrôleur, une modification de l'ordre du micrologiciel ou la connexion d'un périphérique peut changer la lettre d'un disque.

:::single-choice{#device-names-sdb-first-partition} Dans le motif de nommage `sd`, quel chemin désigne la partition 1 de `/dev/sdb` ?

::option[`/dev/sda2`]{#device-names-sda-two explanation="Ce chemin désigne la partition 2 du disque actuellement nommé `/dev/sda`."}
::option[`/dev/sdbp1`]{#device-names-sdb-p-one explanation="Le séparateur `p` s'utilise lorsque le nom de base se termine déjà par un chiffre, pas pour les noms `sd` ordinaires."}
::option[`/dev/sdb1`]{#device-names-sdb-one .correct explanation="Pour les disques `sd`, le numéro de partition est ajouté directement au nom du disque entier."}
:::

## Noms qui se terminent par des chiffres

Certains noms de périphériques entiers contiennent déjà des chiffres ; leurs partitions utilisent donc `p` comme séparateur :

- `/dev/nvme0n1` : espace de noms NVMe 1 du contrôleur 0 ;
- `/dev/nvme0n1p2` : partition 2 de cet espace de noms ;
- `/dev/mmcblk0` : périphérique bloc MMC ;
- `/dev/mmcblk0p1` : partition 1 de ce périphérique.

Les périphériques NVMe ne sont normalement pas nommés `/dev/sdX` ; ils suivent la convention du sous-système NVMe.

:::single-choice{#device-names-nvme-partition} Quel chemin désigne la partition 2 de `/dev/nvme0n1` ?

::option[`/dev/nvme0n1p2`]{#device-names-nvme-p-two .correct explanation="Les noms de partitions NVMe insèrent `p` avant le numéro."}
::option[`/dev/nvme0n12`]{#device-names-nvme-no-p explanation="Sans séparateur, les derniers chiffres seraient ambigus avec le numéro d'espace de noms."}
::option[`/dev/sda2`]{#device-names-nvme-sda explanation="Ce chemin désigne une partition de disque de la couche `sd`, pas l'espace de noms NVMe indiqué."}
:::

## Périphériques bloc logiques et virtuels

Linux crée aussi des périphériques bloc sans correspondance directe avec un disque physique :

- `/dev/dm-N` pour device mapper, souvent avec des liens explicites sous `/dev/mapper/` ;
- `/dev/mdN` pour les ensembles RAID logiciel Linux ;
- `/dev/loopN` pour les fichiers ordinaires attachés comme périphériques bloc loop.

Partitions, couches de chiffrement, RAID, volumes logiques et systèmes de fichiers forment une pile. Utilisez `lsblk` pour voir les relations parent-enfant au lieu de les déduire du seul nom.

:::single-choice{#device-names-device-mapper-link} Quel emplacement fournit couramment des liens descriptifs pour les périphériques device mapper ?

::option[`/dev/mapper/`]{#device-names-mapper-directory .correct explanation="Les utilisateurs de device mapper comme LVM et le chiffrement exposent souvent des liens nommés dans ce répertoire."}
::option[`/dev/null/`]{#device-names-null-directory explanation="`/dev/null` est un périphérique caractère, pas un répertoire de périphériques bloc mappés."}
::option[`/proc/partitions/mapper/`]{#device-names-proc-mapper explanation="Ce n'est pas le chemin normal des liens de noms device mapper."}
:::

## Liens de stockage persistants

La gestion des périphériques en espace utilisateur crée des liens sous `/dev/disk/`, souvent regroupés en :

- `by-id` pour les identifiants matériels ou de transport ;
- `by-uuid` pour les UUID de systèmes de fichiers ;
- `by-label` pour leurs étiquettes ;
- `by-partuuid` pour les UUID de tables de partitions ;
- `by-path` pour les chemins dépendant de la topologie.

Choisissez l'identifiant selon ce qui doit rester stable. Un UUID de système de fichiers identifie celui-ci, pas nécessairement le disque physique sous-jacent. Le clonage peut dupliquer un UUID ; vérifiez donc son unicité avant de vous y fier.

:::single-choice{#device-names-persistent-config} Pourquoi les liens `/dev/disk/by-id/` sont-ils souvent préférables à `/dev/sdX` dans une configuration propre à un périphérique ?

::option[Ils rendent automatiquement réversibles les écritures destructrices.]{#device-names-by-id-reversible explanation="Un nom stable ne fournit ni instantané, ni sauvegarde, ni protection en écriture."}
::option[Ils convertissent un périphérique bloc en fichier ordinaire.]{#device-names-by-id-regular explanation="L'entrée est un lien symbolique qui pointe toujours vers un nœud bloc."}
::option[Ils proviennent de l'identité du périphérique plutôt que de l'ordre actuel d'énumération.]{#device-names-by-id-stable .correct explanation="La cible du lien peut changer, tandis que le lien fondé sur l'identité reste associé au même périphérique reconnu."}
:::

## Noms de pseudo-périphériques

Les noms `/dev/null`, `/dev/zero` et `/dev/urandom` décrivent des pseudo-périphériques du noyau et non du stockage physique. `/dev/null` élimine les écritures et renvoie une fin de fichier en lecture ; `/dev/zero` fournit des octets nuls ; `/dev/urandom` fournit des octets du générateur aléatoire du noyau.

:::single-choice{#device-names-zero-read} Que produit la lecture de `/dev/zero` ?

::option[Une liste des périphériques de stockage inutilisés.]{#device-names-zero-storage-list explanation="Il s'agit d'un périphérique caractère producteur d'octets, pas d'une commande de découverte."}
::option[Un flux d'octets de valeur zéro.]{#device-names-zero-bytes .correct explanation="Le pseudo-périphérique zero renvoie des octets nuls pour les lectures demandées."}
::option[Une fin de fichier immédiate, comme `/dev/null`.]{#device-names-zero-eof explanation="`/dev/zero` continue de produire des octets, tandis que les lectures de `/dev/null` renvoient une fin de fichier."}
:::

Utilisez [Explorer les périphériques matériels sous Linux](https://labex.io/fr/labs/comptia-explore-hardware-devices-in-linux-590861) pour comparer les noms, les liens persistants et les relations `lsblk` avant tout partitionnement.

## Résumé

Vous savez maintenant décoder les noms courants du stockage Linux sans les considérer comme des identités permanentes.

1. Lire `sdXNUMBER` comme une partition d'un disque `sd`.
2. Utiliser `pNUMBER` lorsque le nom du périphérique entier finit par un chiffre.
3. Reconnaître les périphériques logiques device mapper, RAID et loop.
4. Préférer le lien persistant adapté à l'identité voulue.
5. Distinguer les noms de stockage des pseudo-périphériques du noyau.
