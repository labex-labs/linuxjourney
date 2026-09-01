---
lesson_id: "swap-space"
course_id: "filesystem"
lang: "fr"
order_index: 8
title: "swap"
description: "Découvrez comment Linux emploie, initialise, active, dimensionne et désactive sans risque l'espace de swap."
meta_title: "swap - Le système de fichiers"
meta_description: "Découvrez l'espace de swap Linux, son fonctionnement et la création et gestion de partitions ou fichiers de swap."
meta_keywords: "swap Linux, mkswap, swapon, swapoff, /etc/fstab, mémoire virtuelle, tutoriel Linux, partition swap"
---

Linux peut déplacer certaines pages de mémoire anonyme entre la RAM et un stockage servant de swap. Cela permet de conserver la mémoire inactive tout en libérant de la RAM pour les charges actives et le cache du système de fichiers, mais le stockage est bien plus lent que la RAM. Le swap est un outil de capacité et de gestion de la mémoire, pas un substitut à une quantité suffisante de mémoire ni une limite de mémoire applicative.

## Participation du swap à la gestion de la mémoire

Le noyau peut employer le swap avant l'épuisement complet de la RAM, selon la charge, la pression mémoire, les cgroups et des réglages comme swappiness. Les pages propres adossées à des fichiers peuvent souvent être abandonnées puis relues depuis ceux-ci, tandis que les pages anonymes ont besoin du swap ou doivent rester en RAM.

Une utilisation intensive et prolongée du swap peut provoquer une forte latence ou un emballement des échanges, appelé thrashing. Diagnostiquez la demande de mémoire, les ensembles de travail, la pression et les limites applicatives au lieu de considérer un swap plus grand comme une solution universelle aux problèmes de performances.

:::single-choice{#swap-space-anonymous-pages} Quel type de mémoire est un candidat privilégié au stockage dans le swap ?

::option[Tous les fichiers exécutables installés sous `/usr`.]{#swap-space-installed-files explanation="Les fichiers installés restent dans leurs systèmes de fichiers ; les pages propres mappées peuvent y être relues."}
::option[Les pages de mémoire anonyme inactives.]{#swap-space-anonymous-memory .correct explanation="Les pages anonymes ne possèdent pas de fichier de stockage ordinaire depuis lequel elles pourraient simplement être relues."}
::option[Les entrées de la table de partitions du disque.]{#swap-space-partition-table explanation="Les métadonnées de partition restent sur le périphérique bloc et ne sont pas de la mémoire de processus transférée depuis la RAM."}
:::

## Examiner le swap actif

Commencez par des commandes en lecture seule :

```bash
$ swapon --show
$ cat /proc/swaps
$ free -h
```

Elles affichent le swap actif configuré et les chiffres globaux de la mémoire. Une valeur « utilisée » non nulle ne constitue pas automatiquement un problème ; mettez-la en relation avec les débits d'entrée et de sortie du swap, la pression mémoire, la latence et le comportement de la charge.

:::single-choice{#swap-space-show-active} Quelle commande répertorie les espaces de swap actifs dans une vue structurée ?

::option[`swapon --show`]{#swap-space-swapon-show .correct explanation="Le mode show indique les périphériques ou fichiers de swap actifs ainsi que leur taille, utilisation et priorité lorsqu'elles sont disponibles."}
::option[`mkswap --all`]{#swap-space-mkswap-all explanation="Mkswap initialise les signatures de swap ; ce n'est pas la commande d'affichage en lecture seule des espaces actifs."}
::option[`mkfs -t swap`]{#swap-space-mkfs-swap explanation="L'outil d'initialisation standard est `mkswap`, et le formatage n'est pas une requête d'état."}
:::

## Initialiser et activer un périphérique de swap

`mkswap` écrit une signature de swap et détruit les métadonnées utilisables précédentes de la cible. Exercez-vous uniquement sur une cible jetable vérifiée :

```bash
$ sudo mkswap /dev/CIBLE-SWAP-VÉRIFIÉE
$ sudo swapon /dev/CIBLE-SWAP-VÉRIFIÉE
```

Avant `mkswap`, vérifiez modèle, numéro de série, taille, identité persistante, signatures existantes, montages, RAID, LVM, chiffrement et sauvegardes, comme vous le feriez avant `mkfs`. Après l'activation, confirmez la source exacte avec `swapon --show`.

Pour rendre l'activation persistante, employez l'UUID du swap dans `/etc/fstab`, avec un type et des options conformes aux règles locales :

```text
UUID=UUID-SWAP-VÉRIFIÉ none swap sw 0 0
```

:::single-choice{#swap-space-enable-command} Quelle commande active un espace de swap initialisé ?

::option[`swapon`]{#swap-space-command-swapon .correct explanation="Swapon ajoute un périphérique ou fichier de swap valide à l'ensemble des espaces actifs du noyau."}
::option[`mkswap`]{#swap-space-command-mkswap explanation="Mkswap initialise la signature, mais n'active pas lui-même l'espace."}
::option[`mount`]{#swap-space-command-mount explanation="Le swap est activé par le sous-système de swap, et non monté comme système de fichiers dans un répertoire."}
:::

## Fichiers de swap et autres supports

Un fichier de swap offre une capacité flexible sans repartitionnement, mais les exigences de création dépendent du système de fichiers. Le fichier doit posséder des permissions restrictives, une allocation adaptée sans trous ni comportement copy-on-write non pris en charge, une signature de swap et être activé. Suivez la documentation du système de fichiers et de la distribution au lieu de reproduire partout une recette générique fondée sur `fallocate`.

Les périphériques de RAM compressée comme zram peuvent fournir un autre niveau de swap, avec des compromis différents entre processeur et capacité. Un swap chiffré peut protéger les pages au repos, tandis que l'hibernation exige une configuration de reprise et une capacité de stockage adaptée suffisante. Ces objectifs influencent le dimensionnement et la conception.

Il n'existe aucune règle universelle imposant un swap deux fois plus grand que la RAM. Dimensionnez-le selon les pics de la charge, le comportement souhaité en cas d'échec, les besoins d'hibernation, la latence et l'endurance du stockage, la conception des vidages sur incident et la surveillance opérationnelle.

:::single-choice{#swap-space-sizing-rule} Quelle est la meilleure base pour dimensionner le swap ?

::option[Toujours exactement deux fois la RAM installée.]{#swap-space-twice-ram explanation="Cette ancienne règle empirique ne convient pas à toutes les charges ni aux quantités de mémoire modernes."}
::option[Les besoins mesurés de la charge, les objectifs d'hibernation et les règles en cas d'échec.]{#swap-space-sizing-requirements .correct explanation="La fonction du système et le comportement observé de la mémoire comptent davantage qu'un multiplicateur fixe de la RAM."}
::option[Toujours zéro dès que le système possède un SSD.]{#swap-space-zero-ssd explanation="Le type de stockage ne détermine pas à lui seul les besoins liés à la pression mémoire ou à l'hibernation."}
:::

## Désactiver le swap sans risque

Désactivez un espace précis et vérifié avec :

```bash
$ sudo swapoff /dev/CIBLE-SWAP-VÉRIFIÉE
```

Le noyau doit déplacer ailleurs les pages résidentes qui s'y trouvent. Si la RAM et le swap restant ne peuvent pas les accueillir, l'opération peut échouer ou créer une pression mémoire dangereuse. Arrêtez ou limitez d'abord les charges, surveillez la mémoire, ne supprimez l'entrée fstab persistante qu'après avoir vérifié la bonne cible, puis confirmez la désactivation avec `swapon --show` avant de réaffecter le stockage.

:::single-choice{#swap-space-swapoff-capacity} Pourquoi `swapoff` peut-il échouer ou mettre en danger un système fortement chargé ?

::option[Swapoff reformate toujours chaque module de RAM.]{#swap-space-formats-ram explanation="Il modifie la configuration du swap actif et ne formate pas le matériel de mémoire physique."}
::option[Les pages de cet espace doivent trouver de la place en RAM ou dans un autre swap.]{#swap-space-pages-need-capacity .correct explanation="La désactivation exige de déplacer les pages actives du swap pendant que le système continue de fonctionner."}
::option[Un espace de swap inactif doit rester monté dans `/swap`.]{#swap-space-mounted-path explanation="Les espaces de swap ne sont pas des systèmes de fichiers montés dans un répertoire."}
:::

Utilisez [Créer et activer un fichier de swap sous Linux](https://labex.io/fr/labs/comptia-create-and-activate-a-swap-file-in-linux-590858) dans un environnement contrôlé pour vous exercer aux permissions, à l'activation et à la persistance.

## Résumé

Vous savez maintenant considérer le swap comme une ressource explicite de gestion de la mémoire.

1. Relier le swap principalement à la mémoire anonyme soumise à la pression.
2. Examiner le swap actif et le comportement de la charge avant de modifier sa capacité.
3. Initialiser uniquement une cible jetable vérifiée, puis l'activer avec `swapon`.
4. Dimensionner et sécuriser le swap selon la charge et les besoins d'hibernation.
5. Garantir une capacité de relogement avant d'employer `swapoff`.
