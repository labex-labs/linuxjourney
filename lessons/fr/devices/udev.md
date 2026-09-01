---
lesson_id: "udev"
course_id: "devices"
lang: "fr"
order_index: 5
title: "udev"
description: "Découvrez comment udev traite les événements de périphériques du noyau pour appliquer règles, permissions et liens persistants."
meta_title: "udev - Périphériques"
meta_description: "Apprenez-en davantage sur udev, comment il gère dynamiquement les fichiers de périphériques Linux et utilisez udevadm. Comprenez la création de nœuds de périphériques pour les débutants."
meta_keywords: "udev, udevadm, gestion des périphériques Linux, fichiers de périphériques, tutoriel Linux, Linux pour débutants, règles udev, guide Linux"
---

Le noyau Linux signale à l'espace utilisateur les changements de périphériques par des uevents. Sur de nombreuses distributions actuelles, `systemd-udevd` traite ces événements avec des règles udev et une base de périphériques. Avec le `devtmpfs` alimenté par le noyau, ce mécanisme produit les propriétaires, permissions, propriétés et liens symboliques visibles autour de `/dev`.

## De l'événement du noyau à la politique des périphériques

Lorsqu'un périphérique est ajouté, modifié, déplacé ou retiré, udev peut :

- lire ses attributs sysfs et les propriétés de l'événement ;
- appliquer une politique de propriétaire, groupe et mode à son nœud ;
- ajouter des liens stables comme `/dev/disk/by-id/...` ;
- étiqueter le périphérique pour d'autres services ;
- lancer des traitements auxiliaires précisément délimités.

Le noyau reste responsable du périphérique réel et de son pilote. Supprimer un nœud de `/dev` ne retire pas physiquement le matériel, et créer un nœud avec `mknod` ne fait ni apparaître un matériel non pris en charge ni associer un pilote.

:::single-choice{#udev-kernel-event-input} Qu'est-ce qui déclenche normalement le traitement udev lors d'un changement de périphérique ?

::option[Une actualisation des dépôts de paquets par APT.]{#udev-apt-refresh explanation="Les mises à jour de métadonnées de paquets n'ont aucun rapport avec le traitement des événements matériels actifs."}
::option[Le renommage manuel de tous les fichiers sous `/dev`.]{#udev-manual-renaming explanation="La politique dynamique est pilotée par les événements du noyau et les règles, pas par un renommage manuel en masse."}
::option[Un uevent du noyau décrivant l'action sur le périphérique.]{#udev-kernel-uevent .correct explanation="Udev reçoit les événements du noyau et applique les règles correspondantes en espace utilisateur."}
:::

## Emplacements et priorité des règles

Les règles se trouvent couramment dans :

- `/usr/lib/udev/rules.d/` pour les règles des fournisseurs ou des paquets ;
- `/run/udev/rules.d/` pour les règles d'exécution volatiles ;
- `/etc/udev/rules.d/` pour la politique locale de l'administrateur.

Les fichiers sont traités dans l'ordre lexical de leur nom ; selon l'implémentation installée, un fichier de même nom dans un répertoire prioritaire remplace la version de priorité inférieure. Une règle locale doit porter un nom choisi et correspondre à des propriétés stables plutôt qu'à des noms d'énumération.

Une règle peut toucher tous les périphériques correspondants : testez soigneusement sa portée. Ne modifiez pas directement les règles fournies par un paquet lorsqu'une surcharge ou une règle locale supplémentaire convient.

:::single-choice{#udev-local-rules-directory} Quel répertoire est destiné aux règles udev locales et persistantes de l'administrateur ?

::option[`/proc/udev/rules.d/`]{#udev-proc-rules explanation="Procfs ne fournit pas le répertoire persistant des règles locales."}
::option[`/etc/udev/rules.d/`]{#udev-etc-rules .correct explanation="La politique locale appartient sous `/etc`, séparément des règles des fournisseurs gérées par les paquets."}
::option[`/dev/udev/rules.d/`]{#udev-dev-rules explanation="`/dev` contient des objets d'exécution tournés vers les périphériques, pas une configuration persistante de règles."}
:::

## Inspecter un périphérique avec `udevadm`

Interrogez les propriétés udev d'un nœud existant :

```bash
$ udevadm info --query=all --name=/dev/sda
```

Utilisez un nœud présent sur le système actuel. `udevadm info --attribute-walk --name=...` affiche les attributs le long de la chaîne de parents sysfs, ce qui aide à construire une règle. `udevadm monitor --kernel --udev --property` observe les événements bruts et traités ; sa sortie peut exposer des identifiants, qu'il faut manipuler avec prudence.

:::single-choice{#udev-info-purpose} Que demande `udevadm info --query=all --name=/dev/sda` ?

::option[Une réécriture destructive de la table de partitions.]{#udev-info-partition-write explanation="Cette requête est une inspection ; elle ne formate ni ne repartitionne le stockage."}
::option[L'installation sur Internet d'un pilote manquant.]{#udev-info-install-driver explanation="L'inspection avec udevadm n'est pas un téléchargement de paquets."}
::option[Les propriétés udev connues du nœud indiqué.]{#udev-info-properties .correct explanation="La commande info interroge la base de périphériques et les informations sysfs associées."}
:::

## Appliquer avec soin les changements de règles

Le rechargement des fichiers de règles modifie le traitement des futurs événements ; il ne reconstruit pas automatiquement l'état de tous les périphériques existants. Le déclenchement manuel d'événements peut toucher de nombreux périphériques et services : limitez la cible et consultez la documentation de l'`udevadm` installé. Une commande de test peut simuler l'évaluation sans reproduire tous les effets d'un véritable événement.

Sauvegardez les règles locales, validez leur syntaxe, observez un périphérique de test connu et conservez un moyen de récupération avant de changer des permissions ou des noms. N'exécutez pas de longues tâches directement dans le traitement d'un événement udev ; déléguez-les à un service approprié.

:::single-choice{#udev-reload-effect} Que modifie principalement le rechargement des règles udev ?

::option[Le traitement des futurs événements qui correspondent.]{#udev-future-events .correct explanation="Le rechargement actualise les règles en mémoire ; un événement doit encore se produire ou être déclenché pour réévaluer le périphérique."}
::option[Le câblage physique de chaque périphérique connecté.]{#udev-physical-wiring explanation="Le chargement de règles logicielles ne peut pas changer les connexions matérielles."}
::option[Tous les nœuds existants, quels que soient leurs événements ou correspondances.]{#udev-all-existing explanation="Un rechargement seul ne garantit pas la réévaluation immédiate de tous les périphériques présents."}
:::

Utilisez [Explorer les périphériques matériels sous Linux](https://labex.io/fr/labs/comptia-explore-hardware-devices-in-linux-590861) pour relier les propriétés `udevadm`, les chemins sysfs et les liens `/dev`.

## Résumé

Vous savez maintenant situer udev entre les événements du noyau et la politique des périphériques en espace utilisateur.

1. Relier les uevents et attributs sysfs à la correspondance des règles udev.
2. Distinguer les emplacements de règles des fournisseurs, d'exécution et locales.
3. Inspecter les propriétés et le flux d'événements avec `udevadm`.
4. Ne recharger et déclencher des règles qu'avec une portée étroite et testée.
