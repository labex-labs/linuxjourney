---
lesson_id: "filesystem-repair"
course_id: "filesystem"
lang: "fr"
order_index: 10
title: "Réparation d'un système de fichiers"
description: "Découvrez comment diagnostiquer les dommages d'un système de fichiers et choisir une méthode de réparation hors ligne, propre à son type et accompagnée de sauvegardes."
meta_title: "Réparation d'un système de fichiers - Le système de fichiers"
meta_description: "Apprenez à diagnostiquer et réparer un système de fichiers Linux avec fsck et les outils propres à chaque format, tout en protégeant les données."
meta_keywords: "fsck, réparation système de fichiers, commandes Linux, erreurs disque, récupération données, e2fsck, xfs_repair"
---

La réparation d'un système de fichiers réécrit ses métadonnées afin de rétablir sa cohérence interne. Elle peut abandonner des références ou des données endommagées et aggraver la perte lorsque le matériel de stockage est défaillant. Considérez-la comme une opération de récupération : préservez d'abord les preuves et les données récupérables, puis employez l'outil documenté pour le système de fichiers exact.

## Diagnostiquer avant de réparer

Des symptômes comme des erreurs d'entrées-sorties, un remontage en lecture seule, des fichiers manquants ou un échec de montage ne prouvent pas tous que le système de fichiers est corrompu. Commencez par recueillir des indices en lecture seule :

```bash
$ findmnt --target /affected/path
$ lsblk -f
$ journalctl -k -b
```

Vérifiez la pile de stockage, l'état du périphérique, les câbles ou le chemin réseau, l'état du RAID, le chiffrement et les événements récents. Si le périphérique est défaillant, des analyses répétées peuvent épuiser sa durée de vie restante. Lorsque c'est possible, capturez une image ou un clone avec un outil orienté récupération et travaillez sur la copie.

:::single-choice{#filesystem-repair-first-response} Que faut-il faire avant une réparation capable d'écrire lorsque le matériel pourrait être défaillant ?

::option[Exécuter chaque outil de réparation en boucle jusqu'à ce que l'un renvoie zéro.]{#filesystem-repair-repeat-tools explanation="L'emploi d'outils inadaptés et les écritures répétées peuvent aggraver les dommages."}
::option[Créer immédiatement une nouvelle table de partitions par-dessus le périphérique.]{#filesystem-repair-new-table explanation="Écraser les métadonnées d'organisation détruit des preuves et peut compliquer la récupération."}
::option[Préserver les données récupérables ou une image et examiner l'état du périphérique.]{#filesystem-repair-preserve-first .correct explanation="La réparation modifie les métadonnées, tandis qu'un support défaillant peut se détériorer au fil des accès."}
:::

## Identifier précisément le système de fichiers et le périphérique

Déterminez si le système de fichiers réside sur une partition, un volume logique, un périphérique RAID, un mappage chiffré ou un disque entier. N'exécutez pas un vérificateur sur `/dev/sda` au seul motif qu'une partition enfant comme `/dev/sda1` est touchée.

Utilisez `lsblk -f`, `blkid`, `findmnt` et les outils des différentes couches de stockage pour cartographier la cible. Les signatures détectées peuvent être obsolètes ; rapprochez-les donc de la configuration connue et des sauvegardes.

:::single-choice{#filesystem-repair-target-layer} Si ext4 se trouve sur `/dev/sda1`, quelle couche son vérificateur doit-il normalement recevoir ?

::option[`/dev/sda`, quelle que soit sa table de partitions.]{#filesystem-repair-whole-disk explanation="Le disque entier contient la table de partitions et éventuellement plusieurs régions enfants, pas directement l'instance ext4."}
::option[`/dev/sda1`, après sa mise hors ligne sans risque.]{#filesystem-repair-partition-target .correct explanation="Le vérificateur agit sur le périphérique bloc qui contient directement le système de fichiers."}
::option[`/mnt/data` pendant que les applications continuent d'y écrire.]{#filesystem-repair-live-mount explanation="Le chemin du point de montage n'est pas la cible bloc hors ligne attendue par le vérificateur."}
:::

## Mettre le système de fichiers hors ligne

La plupart des vérificateurs traditionnels de cohérence exigent que le système de fichiers soit démonté. Un système monté change pendant sa lecture par l'outil, et les écritures de réparation peuvent entrer en conflit avec l'état mis en cache par le noyau et provoquer une corruption.

Arrêtez les services dépendants, démontez les systèmes imbriqués, déplacez les répertoires de travail des processus et désactivez les couches supérieures selon les besoins. Pour le système de fichiers racine, démarrez un environnement de secours ou employez le mécanisme de vérification hors ligne documenté par la distribution. Confirmez avec `findmnt` que la cible n'est pas montée dans l'espace de noms concerné.

:::single-choice{#filesystem-repair-mounted-risk} Pourquoi faut-il normalement démonter un système de fichiers avant qu'un vérificateur de réparation n'y écrive ?

::option[Les mises à jour simultanées du noyau et du vérificateur peuvent entrer en conflit et corrompre les métadonnées.]{#filesystem-repair-concurrent-writes .correct explanation="Une vue hors ligne empêche le système de fichiers de changer pendant l'opération de réparation."}
::option[Le démontage restaure automatiquement chaque fichier endommagé depuis une sauvegarde.]{#filesystem-repair-unmount-restores explanation="Le détachement assure la stabilité nécessaire à la vérification, mais ne restaure pas les données."}
::option[Les outils de systèmes de fichiers ne peuvent lire que des répertoires, jamais des périphériques blocs.]{#filesystem-repair-tools-directories explanation="Les outils de réparation agissent normalement directement sur les périphériques blocs hors ligne."}
:::

## Employer l'outil propre au système de fichiers

`fsck` est une interface qui peut appeler des assistants propres aux systèmes de fichiers. Ce n'est pas un moteur de réparation universel. Les méthodes distinctes comprennent par exemple `e2fsck` pour les systèmes ext, `xfs_repair` pour XFS et les outils de diagnostic et de récupération propres à Btrfs.

Des options aux noms similaires peuvent posséder une sémantique différente. N'appliquez surtout pas des options `--repair` ou de forçage copiées depuis le guide d'un autre système de fichiers. Lisez le manuel installé ainsi que la documentation actuelle du projet ou de la distribution relative à la récupération. Commencez par un mode sans modification ou de diagnostic si l'implémentation en fournit un fiable, capturez sa sortie et comprenez les corrections proposées.

:::single-choice{#filesystem-repair-fsck-role} De quoi `fsck` est-il couramment responsable sous Linux ?

::option[De déléguer les vérifications à un assistant adapté au type du système de fichiers.]{#filesystem-repair-fsck-dispatch .correct explanation="La logique réelle de validation et de réparation appartient aux outils et méthodes propres au format."}
::option[De convertir chaque système de fichiers en ext4 avant de le vérifier.]{#filesystem-repair-fsck-convert explanation="Un vérificateur doit préserver et comprendre le format existant."}
::option[De réparer les secteurs matériels défaillants en garantissant l'absence de perte de données.]{#filesystem-repair-fsck-hardware explanation="Les outils de cohérence ne peuvent ni réparer le matériel physique, ni garantir la récupération des données."}
:::

## Vérifier et rétablir le service

Consignez l'outil de réparation, sa version, ses options, sa sortie et son état de fin. Après la réparation, vérifiez de nouveau l'état du périphérique, montez d'abord en lecture seule lorsque cela convient, examinez les données essentielles et comparez-les aux sauvegardes connues. Rétablissez ensuite progressivement les montages et services normaux tout en surveillant les journaux du noyau et des applications.

Le fait qu'un système de fichiers puisse de nouveau être monté ne prouve pas que tous ses fichiers sont corrects. Restaurez les données applicatives perdues ou endommagées depuis les sauvegardes et validez-les au niveau de l'application.

:::single-choice{#filesystem-repair-mountable-proof} Un montage réussi après réparation prouve-t-il que toutes les données applicatives sont correctes ?

::option[Non ; la réparation de cohérence et la validation des données au niveau applicatif sont distinctes.]{#filesystem-repair-not-data-proof .correct explanation="Le système de fichiers peut être structurellement montable alors que des fichiers ou transactions restent absents ou endommagés."}
::option[Oui ; le montage vérifie cryptographiquement chaque fichier par rapport à une sauvegarde.]{#filesystem-repair-mount-verifies explanation="Un montage ordinaire n'effectue pas de comparaison complète avec une sauvegarde."}
::option[Oui ; les outils de réparation recréent automatiquement tout contenu inconnu.]{#filesystem-repair-recreates-data explanation="La réparation des métadonnées ne peut pas déduire arbitrairement les données utilisateur perdues."}
:::

## Résumé

Vous savez maintenant planifier la réparation d'un système de fichiers comme une procédure de récupération par étapes.

1. Diagnostiquer le matériel et préserver les données récupérables avant toute écriture.
2. Cartographier la couche bloc exacte qui contient le système de fichiers.
3. Mettre le système de fichiers hors ligne dans l'espace de noms concerné.
4. Employer l'outil documenté de diagnostic et de réparation propre au format.
5. Valider séparément l'état du périphérique, celui du système de fichiers et les données applicatives.
