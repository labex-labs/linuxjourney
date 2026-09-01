---
lesson_id: "dd-command"
course_id: "devices"
lang: "fr"
order_index: 7
title: "dd"
description: "Apprenez comment `dd` copie des flux de blocs et comment éviter les erreurs destructrices de source, destination et taille."
meta_title: "dd - Périphériques"
meta_description: "Explorez l'outil puissant dd sous Linux. Ce guide explique comment utiliser la commande dd linux pour la copie de données efficace, l'imagerie disque et les sauvegardes. Apprenez les options clés comme if, of et bs."
meta_keywords: "commande dd, dd linux, outil dd, copier des données, imagerie disque, tutoriel Linux, débutant, guide, sauvegarde de données"
---

`dd` copie des données d'un flux d'entrée vers un flux de sortie en appliquant les tailles de blocs et conversions demandées. Elle ne comprend ni les systèmes de fichiers, ni les limites de partitions, ni la valeur des données de la cible. Elle est donc utile pour les images et périphériques bruts, mais immédiatement destructrice si la cible est mauvaise.

## Entrée, sortie et taille de bloc

Une commande possède cette forme générale :

```bash
$ dd if=input.img of=output.img bs=4M status=progress
```

- `if=` choisit l'entrée ; sans cette option, `dd` lit l'entrée standard ;
- `of=` choisit la sortie ; sans cette option, `dd` écrit sur la sortie standard ;
- `bs=` fixe la taille des blocs d'entrée et de sortie d'une copie ordinaire ;
- `status=progress` demande à GNU `dd` de rapporter périodiquement l'avancement.

`dd` copie des blocs, pas nécessairement un octet à la fois. Une grande valeur de `bs` peut réduire le coût des appels système, mais la valeur optimale dépend des périphériques, de l'alignement, du cache et de la charge. Elle ne change pas les données logiques copiées.

:::single-choice{#dd-command-output-operand} Quel opérande choisit la destination écrite par `dd` ?

::option[`if=`]{#dd-command-input-file explanation="`if` identifie la source d'entrée."}
::option[`of=`]{#dd-command-output-file .correct explanation="`of` nomme le flux ou fichier de sortie qui reçoit les données copiées."}
::option[`bs=`]{#dd-command-block-size explanation="`bs` choisit une taille de bloc de transfert, pas un chemin."}
:::

## Limiter la copie

`count=` limite le nombre de blocs d'entrée traités. Pour un fichier ordinaire :

```bash
$ dd if=source.img of=prefix.img bs=1M count=2 status=progress
```

Cette commande demande deux blocs d'entrée d'au plus 1 Mio chacun, soit au maximum 2 Mio. Des lectures courtes compliquent cette multiplication pour des flux comme les tubes ; GNU `dd` fournit `iflag=fullblock` lorsque des blocs d'entrée complets sont requis. Distinguez les unités binaires et la syntaxe des suffixes selon l'implémentation locale.

:::single-choice{#dd-command-count-result} Pour un fichier ordinaire, quelle quantité maximale demande `bs=1M count=2` ?

::option[1 Mio.]{#dd-command-one-mib explanation="Cela correspondrait à un seul bloc de la taille choisie."}
::option[2 Mio.]{#dd-command-two-mib .correct explanation="Deux blocs d'entrée multipliés par 1 Mio par bloc donnent un maximum de 2 Mio."}
::option[2 Gio.]{#dd-command-two-gib explanation="Dans GNU `dd`, le suffixe `M` désigne des blocs de la taille d'un mébioctet, pas d'un gibioctet."}
:::

## Écrire une image vers un périphérique bloc

Une restauration brute peut ressembler à :

```bash
$ sudo dd if=backup.img of=/dev/sdX bs=4M status=progress conv=fsync
```

`/dev/sdX` est volontairement un espace réservé, pas une commande à recopier. Avant de le remplacer :

1. Conservez une sauvegarde testée de toutes les données précieuses.
2. Identifiez la cible par modèle, numéro de série, taille, transport et lien persistant avec `lsblk`, `udevadm` ou un équivalent.
3. Confirmez qu'aucune partition cible n'est montée, utilisée comme swap, intégrée à RAID ou LVM, ou ouverte par un service.
4. Revérifiez le périphérique après toute déconnexion, tout redémarrage ou changement de topologie.
5. Assurez-vous que l'image tient et que vous voulez réellement écrire le périphérique entier.

Le périphérique de sortie est écrasé depuis son début. Inverser `if` et `of`, choisir le disque système ou utiliser un disque entier lorsqu'une partition était visée peut détruire des données sans confirmation.

:::single-choice{#dd-command-target-verification} Quelle est la raison la plus importante de vérifier modèle, numéro de série, taille et utilisation active avant une écriture brute ?

::option[Les lettres peuvent changer et `dd` écrase la cible sans comprendre son contenu.]{#dd-command-target-can-change .correct explanation="Les contrôles d'identité et d'utilisation réduisent le risque de détruire un autre disque ou une pile de stockage active."}
::option[`dd` refuse d'écrire si l'étiquette du système de fichiers ne correspond pas à l'image.]{#dd-command-label-check explanation="L'outil ne réalise aucune vérification de sécurité fondée sur le système de fichiers."}
::option[Un périphérique bloc ne peut pas être ouvert tant qu'une sauvegarde existe.]{#dd-command-backup-prevents-open explanation="Une sauvegarde n'empêche pas techniquement les écritures ; elle offre une récupération si elle est maintenue et testée."}
:::

## Créer une image cohérente

Lire un périphérique actif pendant que son système de fichiers change peut produire une image incohérente. Préférez un système non monté, un instantané cohérent avec l'application ou une procédure documentée de gel et d'instantané. Les bases de données et machines virtuelles peuvent exiger leur propre mise au repos.

Une image brute copie les blocs, y compris les métadonnées et régions inutilisées. Elle peut donc être beaucoup plus grande qu'une sauvegarde par fichiers et reproduire des identifiants à modifier avant de monter un clone à côté de l'original.

:::single-choice{#dd-command-live-filesystem-image} Pourquoi l'imagerie d'un système monté et en cours de modification peut-elle être peu fiable ?

::option[Les systèmes montés n'autorisent jamais la lecture du périphérique bloc.]{#dd-command-mounted-no-read explanation="Les lectures brutes peuvent être possibles ; leur cohérence doit donc être planifiée plutôt que présumée."}
::option[Différents blocs peuvent être lus à des instants différents de l'état du système de fichiers.]{#dd-command-inconsistent-moments .correct explanation="Les modifications concurrentes peuvent empêcher l'image de représenter un seul instant cohérent."}
::option[`dd` convertit automatiquement le système de fichiers en archive tar.]{#dd-command-converts-tar explanation="L'outil copie des données brutes et ne crée pas une archive consciente du système de fichiers."}
:::

## Achèvement et vérification

Une fin sans erreur d'E/S ne prouve pas que les bonnes source et cible ont été choisies ni que l'image est utilisable. Notez les identités et tailles exactes, assurez-vous que les tampons ont atteint le stockage, comparez une relecture correctement bornée ou des hachages cryptographiques, puis testez la récupération selon le plan de sauvegarde.

Ne présentez pas les passes d'écrasement de `dd` comme un effacement sûr garanti pour les SSD, les couches de traduction flash, le stockage à allocation fine, les instantanés ou les secteurs remappés. Utilisez la méthode de nettoyage prise en charge par le périphérique et la plateforme, selon une politique explicite de destruction.

:::single-choice{#dd-command-success-meaning} Qu'est-ce qu'un état de terminaison nul de `dd` ne prouve pas à lui seul ?

::option[Que la commande a analysé tous les opérandes fournis.]{#dd-command-parsed-operands explanation="Des opérandes invalides provoquent normalement une erreur plutôt qu'une fin réussie."}
::option[Que l'opérateur a choisi les source et destination voulues.]{#dd-command-does-not-prove-intent .correct explanation="L'outil peut réussir à copier vers la mauvaise cible, car il ne peut pas déduire l'intention de l'opérateur."}
::option[Que le processus a atteint sa terminaison normale.]{#dd-command-normal-exit explanation="Un état nul indique bien une réussite au niveau de la commande, mais pas la correction sémantique des cibles choisies."}
:::

Exercez-vous uniquement avec des fichiers ordinaires ou des disques virtuels jetables avant de toucher au matériel brut. Le laboratoire [Gérer les partitions et systèmes de fichiers Linux](https://labex.io/fr/labs/comptia-manage-linux-partitions-and-filesystems-590845) fournit le contexte nécessaire.

## Résumé

Vous savez maintenant raisonner sur `dd` comme outil de copie brute dépourvu de connaissance de votre intention.

1. Distinguer `if`, `of`, `bs` et `count`.
2. Vérifier l'identité persistante de la cible et tous ses utilisateurs actifs.
3. Créer des images depuis un état de stockage cohérent.
4. Vider les tampons, vérifier la copie et tester la récupération.
5. Considérer toute sortie vers un périphérique brut comme potentiellement destructive.
