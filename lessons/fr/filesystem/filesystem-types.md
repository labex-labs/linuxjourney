---
lesson_id: "filesystem-types"
course_id: "filesystem"
lang: "fr"
order_index: 2
title: "Types de systèmes de fichiers"
description: "Découvrez comment le VFS de Linux présente les systèmes de fichiers locaux, réseau et virtuels au moyen d'une interface unique."
meta_title: "Types de systèmes de fichiers - Le système de fichiers"
meta_description: "Découvrez les systèmes de fichiers Linux ext4, Btrfs et XFS, ainsi que les notions de journalisation et de Virtual Filesystem."
meta_keywords: "types systèmes de fichiers Linux, ext4, Btrfs, XFS, journalisation, VFS, système de fichiers virtuel, tutoriel Linux"
---

Linux prend en charge de nombreuses implémentations de systèmes de fichiers, avec des formats sur disque, protocoles réseau, modèles de cohérence, fonctionnalités et outils d'exploitation différents. Le bon choix dépend de la prise en charge par la distribution, de la charge de travail, des besoins de récupération, de la topologie du stockage et de l'expérience de l'administrateur.

## La couche Virtual Filesystem

La couche Virtual Filesystem du noyau, ou VFS, fournit des opérations communes comme l'ouverture, la lecture, l'écriture, le renommage et le contrôle des permissions. Les implémentations de systèmes de fichiers relient ces opérations à leurs propres structures de données et supports de stockage.

Un même processus peut ainsi accéder à ext4, XFS, NFS, tmpfs et procfs au moyen d'un modèle commun de chemins et de descripteurs de fichiers. Cela ne rend pas toutes leurs fonctionnalités ni tous leurs comportements identiques : sensibilité à la casse, verrouillage, permissions, garanties de renommage, attributs étendus et gestion des erreurs peuvent différer.

:::single-choice{#filesystem-types-vfs-role}
Quel est le rôle principal du VFS de Linux ?

::option[Convertir sur disque chaque système de fichiers monté en ext4.]{#filesystem-types-vfs-convert-ext4 explanation="L'abstraction conserve les implémentations et formats distincts des systèmes de fichiers."}
::option[Sauvegarder chaque fichier avant qu'une application ne l'écrive.]{#filesystem-types-vfs-backup explanation="Le VFS répartit les opérations et ne fournit pas automatiquement un historique de sauvegarde."}
::option[Fournir des opérations de fichiers communes dans le noyau aux différentes implémentations.]{#filesystem-types-vfs-common-interface .correct explanation="Le VFS permet aux applications d'employer des appels système communs tandis que chaque système de fichiers réalise le comportement sous-jacent."}
:::

## Journalisation et cohérence après incident

Un système de fichiers journalisé consigne certaines mises à jour dans un journal afin de pouvoir rejouer ou abandonner les transactions incomplètes après une panne. La journalisation sert avant tout à rétablir la cohérence structurelle du système de fichiers plus rapidement qu'une analyse complète.

Elle ne garantit ni la survie des dernières données applicatives, ni la validité des transactions applicatives portant sur plusieurs fichiers, ni le respect par le matériel de stockage de toutes les écritures déclarées terminées. Les systèmes de fichiers offrent différents modes de données et garanties d'ordonnancement ; les applications doivent employer les opérations de vidage et de mise à jour atomique appropriées. Un journal n'est pas une sauvegarde et ne protège ni contre la suppression, ni contre un logiciel malveillant, ni contre la panne d'un périphérique.

:::single-choice{#filesystem-types-journal-scope}
Que permet principalement de récupérer la journalisation d'un système de fichiers après une panne ?

::option[Des métadonnées cohérentes et les transactions consignées du système de fichiers.]{#filesystem-types-journal-consistency .correct explanation="Le rejeu du journal aide à ramener les structures du système de fichiers dans un état cohérent."}
::option[Toutes les versions historiques de chaque document utilisateur.]{#filesystem-types-journal-versions explanation="Un journal n'est pas un stockage de sauvegardes versionnées."}
::option[Les données d'un périphérique de stockage physiquement détruit.]{#filesystem-types-journal-hardware-loss explanation="La récupération après la perte d'un périphérique exige une redondance ou des sauvegardes extérieures à celui-ci."}
:::

## Systèmes de fichiers locaux courants

- **ext4** est un système de fichiers journalisé mature, largement pris en charge par les distributions Linux et les outils de récupération.
- **XFS** est un système de fichiers journalisé extensible, souvent choisi pour les grands volumes et les charges d'entrées-sorties parallèles.
- **Btrfs** est un système de fichiers copy-on-write doté de sommes de contrôle, sous-volumes, instantanés et fonctions multipériphériques intégrées.

Les fonctionnalités doivent être évaluées dans leur contexte d'exploitation. Un instantané Btrfs partage initialement le stockage avec sa source et ne constitue pas une sauvegarde indépendante s'il reste sur le même périphérique défaillant. XFS et ext4 offrent des possibilités différentes d'agrandissement, réduction, réparation et réglage. Vérifiez la prise en charge par le noyau installé, l'environnement de démarrage et les outils de récupération avant de choisir ou de modifier un système de fichiers racine.

:::single-choice{#filesystem-types-btrfs-snapshot}
Pourquoi un instantané Btrfs situé sur le même périphérique n'est-il pas une sauvegarde complète ?

::option[Les instantanés suppriment toujours immédiatement le sous-volume d'origine.]{#filesystem-types-snapshot-deletes explanation="Un instantané crée une autre vue du sous-volume et ne supprime pas intrinsèquement sa source."}
::option[Il partage le même domaine de défaillance du stockage que l'original.]{#filesystem-types-snapshot-failure-domain .correct explanation="La perte du périphérique ou de graves dommages au système de fichiers peuvent toucher la source comme son instantané local."}
::option[Btrfs ne peut représenter qu'un seul fichier.]{#filesystem-types-btrfs-one-file explanation="Btrfs est un système de fichiers généraliste conçu pour des arborescences et de nombreux fichiers."}
:::

## Interopérabilité, réseau et systèmes de fichiers virtuels

Linux peut monter des formats d'interopérabilité comme les variantes de FAT, exFAT et NTFS, mais leur gestion des propriétaires, permissions, liens et noms de fichiers diffère de celle d'Unix. Les options de montage et l'implémentation du pilote déterminent la manière dont Linux présente les fonctions absentes.

Les systèmes de fichiers réseau comme NFS et SMB dépendent d'un serveur et d'un protocole réseau, avec leurs propres règles de cache et d'identité. Les systèmes de fichiers virtuels comme tmpfs, procfs et sysfs n'emploient pas de format persistant ordinaire sur disque : tmpfs conserve des données volatiles dans des pages soutenues par la mémoire, tandis que procfs et sysfs exposent des interfaces du noyau.

:::single-choice{#filesystem-types-procfs-category}
Quelle description correspond le mieux à procfs ?

::option[Un format d'échange Windows pour les supports amovibles.]{#filesystem-types-procfs-windows explanation="FAT ou exFAT correspondent mieux à cet usage ; procfs est une interface vers le noyau Linux."}
::option[Un système de fichiers virtuel qui expose les interfaces des processus et du noyau.]{#filesystem-types-procfs-virtual .correct explanation="Procfs génère une vue active du noyau au lieu de stocker des fichiers persistants ordinaires sur disque."}
::option[Un système de fichiers journalisé conçu pour les volumes de bases de données.]{#filesystem-types-procfs-journal explanation="Procfs ne possède ni journal normal sur disque, ni rôle de volume de données."}
:::

## Découvrir les types actifs

Affichez le type des systèmes de fichiers montés avec :

```bash
$ findmnt -o TARGET,SOURCE,FSTYPE,OPTIONS
```

Parmi les autres vues figurent `df -T` pour l'utilisation de l'espace monté, `lsblk -f` pour les périphériques blocs et signatures détectées, et `/proc/filesystems` pour les types pris en charge ou connus du noyau en cours d'exécution. Ces commandes répondent à des questions différentes ; un système de fichiers non monté n'apparaît pas dans une liste ordinaire des systèmes montés.

:::single-choice{#filesystem-types-findmnt-output}
Quelle commande dresse directement la liste des cibles montées avec leur source, leur type et leurs options dans cette leçon ?

::option[`findmnt -o TARGET,SOURCE,FSTYPE,OPTIONS`]{#filesystem-types-findmnt .correct explanation="Findmnt lit la table des montages et met en forme les champs demandés pour les systèmes de fichiers montés."}
::option[`lsblk -o NAME,SIZE,MODEL,SERIAL,ROTA`]{#filesystem-types-mkfs-destructive explanation="Cette commande affiche des détails matériels sur les périphériques blocs plutôt que les types et options effectifs des systèmes montés."}
::option[`cat /proc/filesystems | sort --unique`]{#filesystem-types-rm-proc explanation="Cette commande indique les types pris en charge par le noyau plutôt que les sources et options de montage effectives."}
:::

Utilisez [Gérer les partitions et systèmes de fichiers Linux](https://labex.io/fr/labs/comptia-manage-linux-partitions-and-filesystems-590845) sur un stockage jetable afin de comparer les types, options de montage et vues d'inventaire.

## Résumé

Vous savez maintenant comparer les catégories de systèmes de fichiers sans supposer qu'elles partagent une sémantique identique.

1. Relier le VFS aux opérations communes des différentes implémentations.
2. Considérer la journalisation comme une aide à la cohérence après incident, pas comme une sauvegarde.
3. Comparer ext4, XFS et Btrfs selon les opérations prises en charge et la charge de travail.
4. Distinguer les systèmes de fichiers locaux, réseau, d'interopérabilité et virtuels.
5. Employer les outils de montage et de périphériques blocs selon la question d'inventaire posée.
