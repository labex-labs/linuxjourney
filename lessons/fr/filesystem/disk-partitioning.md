---
lesson_id: "disk-partitioning"
course_id: "filesystem"
lang: "fr"
order_index: 4
title: "Partitionnement d'un disque"
description: "Découvrez une méthode fondée sur la vérification pour examiner, créer et redimensionner les limites de partitions avec `parted`."
meta_title: "Partitionnement d'un disque - Le système de fichiers"
meta_description: "Apprenez à partitionner un disque Linux avec parted : examiner, créer et redimensionner les partitions en toute sécurité."
meta_keywords: "partitionnement disque Linux, commande parted, sudo parted -l, GParted, fdisk, créer partition, redimensionner partition, guide Linux"
---

La modification des partitions change la carte qui définit les limites du stockage. Une erreur de périphérique, de début ou de fin peut rendre des données existantes inaccessibles ou écraser des métadonnées essentielles. Exercez-vous uniquement sur un disque virtuel jetable et conservez une sauvegarde testée séparément avant de modifier un stockage important.

## Choisir un outil

Parmi les outils courants figurent :

- `fdisk`, un éditeur de partitions en terminal fourni par util-linux qui prend en charge MBR et GPT ;
- `parted`, un éditeur en terminal et scriptable pour GPT, MBR et d'autres formats de tables ;
- `gdisk`, un éditeur interactif centré sur GPT ;
- GParted, une interface graphique pour les partitions et systèmes de fichiers.

La prise en charge des outils évolue : consultez donc le manuel local et la documentation de la distribution. Une interface graphique ne rend pas les opérations destructrices sûres ; elle modifie les mêmes métadonnées du disque.

:::single-choice{#disk-partitioning-fdisk-gpt} Quelle affirmation à propos de la version actuelle de `fdisk` sous Linux est exacte ?

::option[Elle prend en charge les tables de partitions MBR et GPT.]{#disk-partitioning-fdisk-supports-gpt .correct explanation="La version actuelle de fdisk fournie par util-linux peut modifier les organisations DOS/MBR et GPT, entre autres."}
::option[Elle ne peut modifier que GPT, jamais MBR.]{#disk-partitioning-fdisk-only-gpt explanation="`gdisk`, centré sur GPT, correspond davantage à cette description ; fdisk prend en charge plusieurs types d'étiquettes."}
::option[Elle crée des systèmes de fichiers, mais ne peut pas modifier les entrées de partitions.]{#disk-partitioning-fdisk-filesystem-only explanation="Sa fonction centrale consiste à afficher et modifier les tables de partitions."}
:::

## Identifier et mettre la cible au repos

Commencez par un inventaire en lecture seule :

```bash
$ lsblk -o NAME,PATH,TYPE,SIZE,MODEL,SERIAL,TRAN,PTTYPE,FSTYPE,MOUNTPOINTS
$ findmnt --real
$ sudo parted --list
```

Confirmez le périphérique entier au moyen d'une identité persistante, du modèle, du numéro de série, de la taille, du transport et de la topologie, pas seulement de `/dev/sdX`. Identifiez ensuite chacun de ses consommateurs : systèmes de fichiers montés, swap, LVM, RAID, chiffrement, conteneurs, machines virtuelles, bases de données et descripteurs de fichiers ouverts.

Démontez ou désactivez toutes les couches concernées en suivant leurs procédures documentées. Ne modifiez pas la table de partitions du disque du système en cours d'exécution au seul motif que l'outil s'ouvre correctement. Consignez la table existante sous une forme restaurable et confirmez que votre sauvegarde se trouve dans un autre domaine de défaillance.

:::single-choice{#disk-partitioning-target-identity} Pourquoi un nom de périphérique comme `/dev/sdb` ne suffit-il pas comme unique vérification de la cible ?

::option[Linux n'expose jamais les disques entiers sous `/dev`.]{#disk-partitioning-no-whole-disks explanation="Les disques entiers possèdent couramment des nœuds blocs sous `/dev`."}
::option[Les noms d'énumération peuvent changer lorsque les périphériques ou la topologie changent.]{#disk-partitioning-enumeration-changes .correct explanation="Une lettre est attribuée selon l'ordre de détection et peut désigner un autre disque lors d'une session ultérieure."}
::option[Les outils de partitionnement n'acceptent que les UUID de systèmes de fichiers comme opérandes.]{#disk-partitioning-only-uuid explanation="Les éditeurs agissent normalement sur le chemin d'un périphérique bloc entier, après vérification de son identité."}
:::

## Examiner un périphérique dans `parted`

Ouvrez le périphérique entier que vous avez explicitement vérifié :

```bash
$ sudo parted /dev/DISQUE-VÉRIFIÉ
```

Choisissez ensuite des unités d'affichage cohérentes et affichez la table :

```text
(parted) unit MiB
(parted) print free
```

`print free` montre les entrées actuelles et les régions non allouées. Les commandes de Parted peuvent mettre immédiatement à jour les métadonnées du disque au lieu d'attendre une opération finale d'enregistrement ; considérez donc l'invite interactive comme un accès actif en écriture.

:::single-choice{#disk-partitioning-print-free} Qu'aide à afficher `print free` dans `parted` ?

::option[Les fichiers qui peuvent être supprimés pour réduire sans risque n'importe quel système de fichiers.]{#disk-partitioning-free-files explanation="Parted lit l'organisation des partitions, pas l'allocation des fichiers à l'intérieur du système de fichiers."}
::option[Toutes les sauvegardes stockées sur des systèmes distants.]{#disk-partitioning-remote-backups explanation="L'inventaire des sauvegardes distantes ne relève pas d'un éditeur de partitions."}
::option[Les entrées de partitions existantes et les régions non allouées.]{#disk-partitioning-free-regions .correct explanation="Cette vue permet de choisir les limites à partir de la table actuelle et des espaces encore libres."}
:::

## Créer une entrée de partition

La syntaxe exacte de `mkpart` dépend du type de table. Un exemple GPT exprimé en Mio ressemble à ceci :

```text
(parted) mkpart data ext4 1MiB 5000MiB
```

Cette commande crée une entrée de partition avec un nom, un type de contenu suggéré, un début et une fin. Elle ne crée **pas** de système de fichiers ext4. Le formatage est une étape destructive distincte, exécutée seulement après que le noyau a reconnu la nouvelle partition prévue et que son identité a été vérifiée.

Respectez l'alignement recommandé par l'outil et déterminez si les extrémités sont inclusives et comment elles sont arrondies. Examinez le résultat avec `print` et `lsblk` ; ne supposez pas qu'une limite décimale demandée a été enregistrée à l'identique.

:::single-choice{#disk-partitioning-mkpart-effect} Que crée la commande `mkpart` de `parted` ?

::option[Un système de fichiers ext4 monté contenant un répertoire personnel.]{#disk-partitioning-mounted-filesystem explanation="Le formatage et le montage sont des opérations distinctes effectuées après la création de la partition."}
::option[Une sauvegarde complète du contenu antérieur de la partition.]{#disk-partitioning-automatic-backup explanation="Les éditeurs de partitions ne créent pas automatiquement de sauvegarde de récupération."}
::option[Une entrée de table de partitions, sans formater de système de fichiers.]{#disk-partitioning-entry-only .correct explanation="L'argument de type de système de fichiers influence les métadonnées de partition, mais n'exécute pas `mkfs`."}
:::

## Redimensionner les limites et le contenu

`resizepart NUMÉRO FIN` déplace uniquement la limite de fin d'une partition. Il ne redimensionne pas le système de fichiers ou l'autre structure stockée à l'intérieur.

L'ordre est essentiel :

- pour agrandir, étendez d'abord la partition ou le périphérique logique conteneur, puis agrandissez le système de fichiers avec l'outil qu'il prend en charge ;
- pour réduire, vérifiez que le système de fichiers accepte la réduction, réduisez-le d'abord en respectant ses exigences d'exécution hors ligne ou en ligne, puis réduisez la limite du conteneur sans dépasser sa nouvelle fin.

Certains systèmes de fichiers ne peuvent pas être réduits. Le chiffrement, LVM, RAID et les organisations imbriquées ajoutent d'autres couches à traiter dans l'ordre. Le noyau peut aussi refuser de relire une table modifiée tant que des périphériques sont occupés, ce qui impose un redémarrage contrôlé avant de pouvoir employer la nouvelle organisation.

:::single-choice{#disk-partitioning-shrink-order} Lorsqu'un système de fichiers peut être réduit, quel ordre évite de tronquer ses données actives ?

::option[Réduire d'abord la partition, puis vérifier si le système de fichiers tient encore dedans.]{#disk-partitioning-shrink-partition-first explanation="Raccourcir d'abord le conteneur peut tronquer les structures et les données du système de fichiers."}
::option[Réduire d'abord le système de fichiers, puis la limite de la partition qui le contient.]{#disk-partitioning-shrink-filesystem-first .correct explanation="Le contenu doit tenir dans la plage plus petite avant de raccourcir le périphérique bloc extérieur."}
::option[Supprimer la table de partitions et laisser le système de fichiers la recréer.]{#disk-partitioning-delete-table explanation="Un système de fichiers ne reconstruit pas une table de partitions sûre dans le cadre de sa réduction normale."}
:::

Utilisez [Gérer les partitions et systèmes de fichiers Linux](https://labex.io/fr/labs/comptia-manage-linux-partitions-and-filesystems-590845) sur son disque virtuel secondaire prévu à cet effet ; ne lui substituez pas un disque de la machine hôte.

## Résumé

Vous savez maintenant décrire la modification des partitions comme une opération de stockage destructive et organisée en couches.

1. Choisir un outil qui prend en charge la table et la méthode réelles.
2. Vérifier l'identité persistante du disque et désactiver chaque consommateur.
3. Examiner unités, entrées et régions libres avant toute écriture.
4. Se rappeler que `mkpart` ne crée pas de système de fichiers.
5. Redimensionner le contenu intérieur et les limites extérieures dans l'ordre sûr.
