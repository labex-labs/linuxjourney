---
lesson_id: "boot-process-kernel"
course_id: "boot-system"
lang: "fr"
order_index: 4
title: "Processus de démarrage : Noyau"
description: "Découvrez comment le noyau initialise le matériel, exécute l'espace utilisateur précoce de l'initramfs, atteint la véritable racine et lance le PID 1."
meta_title: "Processus de démarrage : Noyau - Démarrer le système"
meta_description: "Explorez le processus de démarrage du noyau Linux. Apprenez comment initramfs charge les pilotes à partir d'un système de fichiers temporaire pour monter la partition racine de démarrage finale. Comprenez les étapes du chargement du noyau à l'exécution d'init."
meta_keywords: "racine de démarrage, initramfs, démarrage noyau, partition de démarrage, initramfs ubuntu, /etc/default/grub, processus de démarrage Linux, système de fichiers racine, initialisation du noyau"
---

Après avoir reçu le contrôle, le noyau Linux initialise la gestion de la mémoire, l'ordonnancement, les interruptions, les pilotes intégrés, les cadres de sécurité et d'autres sous-systèmes essentiels. Il analyse la ligne de commande et se prépare à lancer le premier processus de l'espace utilisateur.

## Pourquoi un espace utilisateur précoce existe

Un système de fichiers racine simple peut parfois être monté grâce aux pilotes intégrés au noyau. Les systèmes plus complexes nécessitent des modules et des outils avant que la véritable racine puisse être atteinte, par exemple pour :

- les modules d'un contrôleur de stockage ou d'un système de fichiers ;
- le déverrouillage d'une racine chiffrée ;
- l'assemblage LVM ou RAID ;
- la configuration réseau d'une racine en réseau ;
- la découverte des périphériques et la résolution d'identifiants persistants.

Un initramfs rassemble ces composants dans un environnement précoce en espace utilisateur fourni avec le noyau.

:::single-choice{#boot-kernel-initramfs-purpose}
Quel problème un initramfs résout-il couramment ?

::option[Il fournit les premiers outils et modules nécessaires avant que la véritable racine soit disponible.]{#boot-kernel-early-tools .correct explanation="L'espace utilisateur précoce peut découvrir et assembler un stockage auquel le noyau ne peut pas accéder avec sa seule prise en charge intégrée."}
::option[Il stocke définitivement dans le micrologiciel le répertoire personnel de chaque utilisateur.]{#boot-kernel-home-firmware explanation="Cette archive est un artefact de démarrage, pas un stockage permanent de données utilisateur."}
::option[Il remplace le noyau Linux après la première connexion.]{#boot-kernel-replace-kernel explanation="Le noyau reste actif pendant que le code de l'initramfs s'exécute en espace utilisateur."}
:::

## Initramfs et ancien initrd

Un initramfs moderne se compose généralement d'une ou plusieurs archives cpio, souvent compressées, que le noyau extrait dans son système de fichiers racine initial. Il exécute ensuite un programme précoce `/init` dans cet environnement.

Un ancien initrd est conceptuellement une image de système de fichiers chargée dans un périphérique bloc en RAM, puis montée. Les termes sont souvent employés approximativement dans les noms de fichiers et commandes du chargeur ; examinez donc les outils réels plutôt que de déduire le format du seul nom.

L'initramfs doit correspondre au noyau et à la conception du démarrage. Des modules absents, des identifiants de périphériques obsolètes ou l'omission des outils cryptographiques et LVM peuvent rendre un nouveau noyau impossible à démarrer, même si son image est valide.

:::single-choice{#boot-kernel-initramfs-format}
Sous quelle forme un initramfs moderne est-il généralement présenté au noyau ?

::option[Comme un dépôt de paquets interactif accessible uniquement par HTTP.]{#boot-kernel-http-repository explanation="Le réseau peut être configuré dans l'espace utilisateur précoce, mais il ne définit pas le format de l'initramfs."}
::option[Comme une archive fondée sur cpio, extraite dans la racine initiale.]{#boot-kernel-cpio-archive .correct explanation="Le noyau développe l'archive et exécute son programme d'initialisation précoce en espace utilisateur."}
::option[Comme l'en-tête de sauvegarde GPT du disque.]{#boot-kernel-gpt-header explanation="La redondance de la table de partitions est indépendante de l'archive de l'espace utilisateur précoce."}
:::

## Atteindre la véritable racine

L'espace utilisateur précoce interprète des paramètres comme `root=`, attend les périphériques nécessaires, active les couches de stockage et monte le système de fichiers racine voulu. Il emploie ensuite une opération de changement de racine pour faire de ce système de fichiers le nouveau `/` et libérer si possible l'environnement précoce temporaire.

La demande initiale `ro` de la ligne de commande peut faciliter les contrôles de cohérence et un démarrage maîtrisé, mais la séquence exacte dépend de la distribution. Les vérifications de systèmes de fichiers sont des opérations de l'espace utilisateur ; l'initramfs ou le système init ultérieur peut remonter la racine en lecture-écriture si la politique l'autorise.

:::single-choice{#boot-kernel-root-switch}
Que se passe-t-il après le montage réussi de la véritable racine par l'espace utilisateur précoce ?

::option[La table de partitions de chaque disque est recréée.]{#boot-kernel-recreate-tables explanation="Le changement de racine ne repartitionne pas le stockage."}
::option[Le noyau s'arrête et le micrologiciel reprend l'ordonnancement des processus.]{#boot-kernel-firmware-schedules explanation="Le noyau Linux reste responsable des processus et du matériel après le passage de relais."}
::option[Le démarrage fait de ce système de fichiers la racine visible et poursuit le lancement de l'espace utilisateur.]{#boot-kernel-switch-root .correct explanation="La racine précoce temporaire transmet le contrôle à la hiérarchie racine du système installé."}
:::

## Démarrer le PID 1

Le noyau exécute le programme init configuré, normalement atteint par un chemin comme `/sbin/init` ou choisi avec `init=`. Ce processus reçoit le PID 1 et prend en charge l'environnement principal des services de l'espace utilisateur.

Si aucun programme init utilisable ne peut être exécuté, le noyau ne peut pas atteindre un système normal en espace utilisateur et signale généralement un échec du démarrage ou une panique. Déboguez la première couche qui échoue : noyau et ligne de commande, contenu de l'initramfs, découverte ou montage de la racine, puis exécution du PID 1.

:::single-choice{#boot-kernel-pid-one}
Quel est le dernier grand passage de relais du noyau dans cette étape simplifiée du démarrage ?

::option[Exécuter le premier programme de l'espace utilisateur avec le PID 1.]{#boot-kernel-exec-init .correct explanation="Le PID 1 lance ensuite les services et l'état configuré du système."}
::option[Transformer `/proc` en base persistante de paquets.]{#boot-kernel-proc-package explanation="Procfs reste une interface d'exécution du noyau."}
::option[Attribuer le même PID à tous les processus ultérieurs.]{#boot-kernel-same-pid explanation="Chaque processus vivant reçoit son propre PID au sein d'un espace de noms."}
:::

## Résumé

Vous savez maintenant suivre le démarrage du noyau, de l'espace utilisateur précoce au PID 1.

1. Distinguer l'initialisation intégrée au noyau des modules précoces chargeables.
2. Relier l'initramfs à une racine temporaire fondée sur cpio et à `/init`.
3. Suivre l'assemblage du stockage et le passage à la véritable racine.
4. Identifier l'exécution du PID 1 comme le passage de relais vers l'espace utilisateur.
