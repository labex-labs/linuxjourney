---
lesson_id: "anatomy-of-a-disk"
course_id: "filesystem"
lang: "fr"
order_index: 3
title: "Anatomie d'un disque"
description: "Découvrez comment périphériques blocs, tables de partitions, partitions et systèmes de fichiers forment des couches de stockage distinctes."
meta_title: "Anatomie d'un disque - Le système de fichiers"
meta_description: "Explorez l'anatomie d'un disque sous Linux, les tables de partitions MBR et GPT, les partitions et les systèmes de fichiers."
meta_keywords: "disque Linux, partitions Linux, MBR, GPT, table de partitions, système de fichiers, périphérique bloc, anatomie disque"
---

Un périphérique de stockage est exposé comme un périphérique bloc, par exemple `/dev/sda` ou `/dev/nvme0n1`. Il peut contenir une table de partitions, dont les entrées décrivent des régions exposées comme des périphériques blocs enfants. Une partition peut ensuite accueillir un système de fichiers, une signature de swap, un membre RAID, un conteneur chiffré, un volume physique de gestionnaire de volumes logiques ou un autre format de données.

Ces couches sont indépendantes : tous les disques ne possèdent pas de table de partitions, toutes les partitions ne contiennent pas un système de fichiers, et un système de fichiers peut résider sur un volume logique ou sur un périphérique entier.

## Tables de partitions et limites

Une table de partitions consigne les positions de départ, longueurs, identifiants de type et attributs propres au schéma. Le noyau la lit pour créer des périphériques blocs de partition comme `/dev/sda1` ou `/dev/nvme0n1p1`.

Dans une organisation ordinaire, les limites des partitions ne doivent pas se chevaucher. L'espace qui n'appartient à aucune entrée est non alloué du point de vue de la table, même s'il peut encore contenir d'anciennes signatures ou données. Modifier la table ne déplace pas automatiquement le contenu des systèmes de fichiers pour le faire correspondre aux nouvelles limites.

:::single-choice{#anatomy-disk-partition-table-role} Qu'est-ce qui indique au système d'exploitation où les partitions d'un disque commencent et se terminent ?

::option[Le répertoire de travail actuel du shell.]{#anatomy-disk-shell-directory explanation="Un chemin du shell ne joue aucun rôle dans les limites de partitions inscrites sur le disque."}
::option[La table de partitions du disque.]{#anatomy-disk-table-boundaries .correct explanation="Les entrées de partition décrivent les régions que le noyau peut exposer comme périphériques blocs enfants."}
::option[Le groupe principal du compte utilisateur.]{#anatomy-disk-user-group explanation="Les identifiants du compte ne définissent ni la géométrie du disque, ni l'organisation des partitions."}
:::

## Partitionnement MBR

L'ancien schéma DOS/MBR stocke sa table principale dans le premier secteur logique. Il comporte quatre entrées de partitions principales. L'une d'elles peut décrire une partition étendue servant de conteneur à une série chaînée de partitions logiques, ce qui permet de disposer de plus de quatre régions utilisables.

Avec des adresses de secteurs sur 32 bits et des secteurs logiques de 512 octets, MBR atteint une limite souvent donnée à environ 2 Tio. L'adressage exact dépend de la taille des secteurs et de la prise en charge par les outils. MBR ne possède pas non plus les copies redondantes d'en-tête et de table, ni les GUID propres à chaque partition qu'offre GPT.

:::single-choice{#anatomy-disk-mbr-more-than-four} Quelle structure MBR permet de disposer de plus de quatre partitions utilisables ?

::option[Une partition de journal contenant davantage d'entrées principales.]{#anatomy-disk-mbr-journal explanation="La journalisation d'un système de fichiers est sans rapport avec les quatre entrées de la table MBR."}
::option[Une partition étendue contenant des partitions logiques.]{#anatomy-disk-mbr-extended .correct explanation="Une entrée principale peut définir un conteneur étendu dans lequel les partitions logiques sont chaînées."}
::option[Un superbloc de système de fichiers qui renumérote les entrées.]{#anatomy-disk-mbr-superblock explanation="Les métadonnées d'un système de fichiers n'agrandissent pas la table de partitions du disque."}
:::

## Partitionnement GPT

La GUID Partition Table, ou GPT, emploie des adresses de blocs logiques sur 64 bits et conserve normalement un en-tête principal et un tableau d'entrées près du début du disque, avec des copies de secours près de sa fin. Un MBR protecteur évite que les anciens logiciels limités au MBR ne considèrent le disque comme vide.

Chaque entrée GPT comprend un GUID de type de partition et un GUID unique de partition ; GPT ne se limite donc pas à un seul type de partition. Le nombre d'entrées disponibles dépend de la table allouée et des outils, mais il est couramment très supérieur à quatre sans nécessiter de partitions étendues ou logiques.

GPT est normalement utilisé pour les disques de démarrage UEFI, mais le partitionnement et le mode de démarrage du micrologiciel sont deux notions distinctes. Un système UEFI a également besoin des fichiers d'amorçage appropriés et d'une partition système EFI ; GPT seul ne rend pas un disque amorçable.

:::single-choice{#anatomy-disk-gpt-identifiers} Quels identifiants une entrée de partition GPT contient-elle ?

::option[Un GUID de type et un GUID de partition unique.]{#anatomy-disk-gpt-guids .correct explanation="Le type décrit l'usage prévu, tandis que le GUID unique identifie cette entrée de partition particulière."}
::option[Un seul type universel partagé par toutes les partitions GPT.]{#anatomy-disk-gpt-one-type explanation="GPT définit de nombreux GUID de type correspondant à différents usages des partitions."}
::option[L'UID et le GID de connexion de l'utilisateur qui l'a créée.]{#anatomy-disk-gpt-user-ids explanation="Les identifiants de comptes du système de fichiers ne sont pas des champs d'identité des partitions GPT."}
:::

## Des structures propres à chaque format de système de fichiers

Après le partitionnement, un outil de création de système de fichiers écrit les structures définies par ce dernier. De nombreux formats possèdent des notions telles que superblocs, métadonnées d'allocation, enregistrements de répertoires et étendues ou blocs de données, mais leur organisation, leur redondance et leur terminologie diffèrent.

Par exemple, les systèmes de fichiers ext emploient des inodes et des groupes de blocs, tandis que d'autres organisent leurs métadonnées au moyen d'arbres ou de structures d'allocation différents. N'appliquez pas à tous les systèmes de fichiers un même schéma simplifié composé d'un « bloc de démarrage, un superbloc, une table d'inodes et des blocs de données ».

:::single-choice{#anatomy-disk-filesystem-layer} La création d'une partition crée-t-elle automatiquement un système de fichiers à l'intérieur ?

::option[Non ; le formatage ou un autre usage explicite constitue une étape distincte.]{#anatomy-disk-partition-not-filesystem .correct explanation="La table de partitions ne définit qu'une région de blocs ; son contenu reste indépendant."}
::option[Oui ; chaque partition est automatiquement formatée en ext4.]{#anatomy-disk-auto-ext4 explanation="Les outils de partitionnement ne créent pas systématiquement un système de fichiers ext4."}
::option[Oui ; les entrées GPT sont elles-mêmes des répertoires montés.]{#anatomy-disk-gpt-mounted explanation="Une entrée de partition décrit un espace de stockage et n'est pas un point de montage de système de fichiers."}
:::

## Examiner l'organisation actuelle

Utilisez des vues en lecture seule avant toute modification :

```bash
$ lsblk -o NAME,PATH,TYPE,SIZE,PTTYPE,PARTTYPE,FSTYPE,MOUNTPOINTS
$ sudo parted --list
```

`PTTYPE` décrit le schéma de table de partitions détecté, `PARTTYPE` l'identifiant de type d'une partition et `FSTYPE` une signature de contenu détectée. Une détection constitue un indice, pas la garantie que le contenu est sain ou peut être monté sans danger.

Les noms des périphériques peuvent changer et d'anciennes signatures peuvent perturber la détection. Vérifiez modèle, numéro de série, taille, transport, liens persistants, montages actifs, swap, RAID, LVM, chiffrement et sauvegardes avant d'ouvrir un outil de partitionnement en mode écriture.

:::single-choice{#anatomy-disk-lsblk-fields} Quel champ de `lsblk` distingue le contenu de système de fichiers détecté du schéma de la table de partitions ?

::option[`FSTYPE`]{#anatomy-disk-fstype .correct explanation="`FSTYPE` indique un système de fichiers ou une autre signature de contenu reconnue, tandis que `PTTYPE` indique le schéma de la table."}
::option[`NAME`]{#anatomy-disk-name-field explanation="`NAME` désigne l'entrée de périphérique bloc du noyau et n'identifie pas précisément le format du contenu."}
::option[`SIZE`]{#anatomy-disk-size-field explanation="La taille indique la capacité, pas le type du système de fichiers."}
:::

Utilisez [Gérer les partitions et systèmes de fichiers Linux](https://labex.io/fr/labs/comptia-manage-linux-partitions-and-filesystems-590845) uniquement sur un stockage jetable pour vous exercer à distinguer ces couches.

## Résumé

Vous savez maintenant séparer les métadonnées d'organisation du disque des formats de données qu'il contient.

1. Identifier les périphériques entiers et leurs périphériques enfants de partition.
2. Relier les partitions étendues MBR à l'ancienne limite de quatre entrées.
3. Relier GPT à ses tables redondantes et aux GUID propres à chaque partition.
4. Considérer la création du système de fichiers comme distincte de celle de la partition.
5. Examiner chaque couche de stockage et chaque consommateur actif avant toute modification.
