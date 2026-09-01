---
lesson_id: "kernel-location"
course_id: "kernel"
lang: "fr"
order_index: 5
title: "Emplacement du noyau"
description: "Découvrez où les distributions placent les images du noyau, fichiers initramfs, configurations, symboles et modules versionnés."
meta_title: "Emplacement du noyau - Noyau"
meta_description: "Découvrez où le noyau est stocké sous Linux, notamment les fichiers vmlinuz et initramfs dans /boot et les modules versionnés."
meta_keywords: "emplacement noyau Linux, où se trouve noyau, vmlinuz, répertoire /boot, initramfs, modules noyau"
---

Les distributions Linux stockent couramment les artefacts amorçables du noyau sous `/boot`, mais les organisations UEFI et Boot Loader Specification peuvent aussi les placer sur une partition système EFI ou une partition de démarrage étendue, montée par exemple dans `/boot`, `/boot/efi` ou `/efi`. Examinez les montages et la configuration du chargeur plutôt que de supposer un chemin universel.

## Fichiers versionnés sous `/boot`

Une organisation traditionnelle de distribution peut contenir :

- `vmlinuz-VERSION_DU_NOYAU` : une image amorçable du noyau Linux ;
- `initrd.img-VERSION_DU_NOYAU` ou `initramfs-VERSION_DU_NOYAU.img` : une image de l'espace utilisateur précoce ;
- `config-VERSION_DU_NOYAU` : la configuration employée pour construire le noyau empaqueté ;
- `System.map-VERSION_DU_NOYAU` : la carte entre symboles et adresses issue de la construction du noyau.

Les noms varient. Sur une distribution moderne, un fichier nommé `initrd` contient souvent une archive initramfs. La convention `vmlinuz` ne révèle ni la compression interne exacte, ni le format d'amorçage de la plateforme ; examinez-le avec les outils de la distribution.

:::single-choice{#kernel-location-vmlinuz} Que contient normalement un fichier versionné `vmlinuz-*` ?

::option[Une image amorçable du noyau Linux.]{#kernel-location-kernel-image .correct explanation="Le chargeur d'amorçage ou le micrologiciel charge cet artefact du noyau propre à l'architecture."}
::option[Tous les modules chargeables de tous les noyaux installés.]{#kernel-location-all-modules explanation="Les modules sont stockés séparément dans une arborescence propre à chaque version."}
::option[L'historique du shell de l'utilisateur lors du démarrage précédent.]{#kernel-location-shell-history explanation="Les images de noyau n'embarquent pas l'historique personnel des commandes."}
:::

## Système de fichiers RAM initial et métadonnées de construction

L'initramfs doit contenir les modules et outils précoces requis par le noyau correspondant et la conception du stockage racine. La concordance du nom de fichier ne suffit pas : une génération obsolète ou défaillante peut tout de même produire une entrée impossible à démarrer.

`config-*` aide à déterminer les fonctionnalités intégrées, modulaires ou omises. `System.map-*` peut aider à la symbolisation et au débogage, mais la randomisation des adresses, les informations de débogage séparées et les outils de la distribution influencent son utilisation. Ces fichiers sont des artefacts auxiliaires, pas d'autres noyaux.

:::single-choice{#kernel-location-initramfs-match} Pourquoi un initramfs est-il lié à une version précise du noyau et à la configuration du système ?

::option[Il stocke définitivement le contenu de chaque système de fichiers monté.]{#kernel-location-all-filesystems explanation="Un initramfs est un petit environnement de démarrage précoce, pas une sauvegarde complète du système."}
::option[Il attribue de nouveaux UID aux utilisateurs à chaque démarrage.]{#kernel-location-user-ids explanation="La gestion des identités de comptes ne relève pas de son rôle normal."}
::option[Il contient les modules et outils précoces nécessaires à cette voie de démarrage.]{#kernel-location-early-modules .correct explanation="L'ABI des modules et les composants nécessaires à l'assemblage du stockage doivent correspondre au noyau sélectionné."}
:::

## Modules versionnés du noyau

Les modules chargeables de la version active résident couramment sous :

```bash
$ printf '/lib/modules/%s\n' "$(uname -r)"
```

Dans les organisations de systèmes de fichiers fusionnées, ce chemin peut se résoudre vers `/usr/lib/modules/VERSION_DU_NOYAU`. Chaque noyau installé a besoin d'une arborescence de modules compatible et d'index de dépendances. `modprobe` emploie des métadonnées propres à la version au lieu de rechercher des fichiers `.ko` arbitraires sur le disque.

:::single-choice{#kernel-location-module-tree} Quel répertoire contient conventionnellement les modules de la version active du noyau ?

::option[`/home/modules/current/`]{#kernel-location-home-modules explanation="Les répertoires personnels ne sont pas l'arborescence standard des modules système."}
::option[`/lib/modules/$(uname -r)/`]{#kernel-location-lib-modules .correct explanation="Le composant de version sépare l'ABI des modules et les données de dépendances de chaque noyau installé."}
::option[`/proc/modules/files/`]{#kernel-location-proc-files explanation="`/proc/modules` signale les modules chargés et n'est pas un répertoire de binaires de modules."}
:::

## Images unifiées du noyau et chemins du micrologiciel

Une Unified Kernel Image, ou UKI, est un seul exécutable EFI signé qui peut réunir un noyau, un initrd, une ligne de commande et des métadonnées. Les UKI sont généralement conservées dans un emplacement de démarrage accessible à EFI plutôt que représentées par des fichiers `vmlinuz` et initramfs séparés.

Une organisation traditionnelle de `/boot` apparemment vide ne prouve donc pas qu'aucun noyau n'est installé. Employez `findmnt`, la base des paquets, les outils du gestionnaire de démarrage et la configuration du chargeur afin de cartographier les artefacts actifs.

:::single-choice{#kernel-location-uki} Que peut réunir une Unified Kernel Image ?

::option[Tous les répertoires personnels dans un en-tête GPT.]{#kernel-location-uki-homes explanation="Une UKI est un exécutable de démarrage, pas un conteneur de données utilisateur ni une table de partitions."}
::option[Chaque paquet installé dans un unique script shell.]{#kernel-location-uki-packages explanation="Elle regroupe les composants de démarrage, pas tout le dépôt du système d'exploitation."}
::option[Le noyau, l'initrd, la ligne de commande et des métadonnées dans un exécutable EFI.]{#kernel-location-uki-components .correct explanation="L'artefact combiné peut participer à une chaîne d'amorçage UEFI signée."}
:::

## Gérer l'espace sans risque

Si le système de fichiers de démarrage est plein, cartographiez d'abord les chemins montés et déterminez par la base des paquets le propriétaire de chaque artefact. Employez la méthode de nettoyage des noyaux du gestionnaire de paquets, conservez le noyau actif et une solution de repli connue, régénérez ou examinez les entrées d'amorçage, puis vérifiez l'espace libre.

Ne supprimez pas manuellement des fichiers `vmlinuz`, initramfs, UKI ou des arborescences de modules en vous fondant seulement sur leur ancienneté. Un fichier peut être la seule entrée de récupération amorçable même s'il n'est pas actuellement actif.

## Résumé

Vous savez maintenant relier un paquet de noyau à ses artefacts de démarrage et de modules.

1. Examiner les montages réels de `/boot` et liés à EFI.
2. Distinguer image du noyau, initramfs, configuration et carte des symboles.
3. Faire correspondre les arborescences de modules à la version exacte du noyau.
4. Tenir compte des Unified Kernel Images et des organisations propres aux distributions.
5. Ne récupérer l'espace de démarrage qu'avec un plan vérifié de paquets et de repli.
