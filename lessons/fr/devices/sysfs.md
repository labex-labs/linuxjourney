---
lesson_id: "sysfs"
course_id: "devices"
lang: "fr"
order_index: 4
title: "sysfs"
description: "Découvrez comment sysfs expose sous `/sys` le modèle actif des périphériques, pilotes, bus et classes du noyau Linux."
meta_title: "sysfs - Périphériques"
meta_description: "Découvrez ce qu'est sysfs et son rôle dans le système sys de Linux. Ce guide explique le répertoire /sys de Linux, un système de fichiers virtuel pour les informations sur les périphériques, et le compare à /dev."
meta_keywords: "sysfs, qu'est-ce que sysfs, /sys, linux /sys, sys linux, système sys, système de fichiers virtuel, périphériques linux, /dev"
---

`sysfs` est un système de fichiers virtuel normalement monté sur `/sys`. Il représente les objets du noyau et leurs relations par des répertoires, des liens symboliques et de petits fichiers d'attributs. Les outils de découverte et gestionnaires de périphériques l'utilisent pour comprendre le modèle actuel du noyau.

## Parcourir le modèle des périphériques

Les principales vues de premier niveau comprennent :

- `/sys/devices/` : hiérarchie des périphériques physiques et logiques ;
- `/sys/class/` : périphériques regroupés par classe fonctionnelle, comme bloc ou réseau ;
- `/sys/bus/` : bus, périphériques et pilotes associés ;
- `/sys/block/` : vue pratique des périphériques bloc ;
- `/sys/dev/` : liens indexés par type caractère ou bloc et par numéros majeur et mineur.

De nombreuses entrées extérieures à `/sys/devices` sont des liens vers la hiérarchie canonique. Résolvez un lien avec `readlink -f` lorsque vous avez besoin du véritable chemin parent :

```bash
$ readlink -f /sys/class/block/sda
```

Ce nom d'exemple peut être absent sur les systèmes qui utilisent d'autres interfaces de stockage.

:::single-choice{#sysfs-canonical-device-tree}
Quelle sous-arborescence de sysfs contient la hiérarchie principale des périphériques du noyau ?

::option[`/sys/passwords/`]{#sysfs-passwords-tree explanation="Sysfs n'est pas un dépôt de secrets d'authentification utilisateur."}
::option[`/sys/devices/`]{#sysfs-devices-tree .correct explanation="La sous-arborescence devices représente la topologie parent-enfant ; les vues par classe et bus y renvoient."}
::option[`/sys/packages/`]{#sysfs-packages-tree explanation="L'état des paquets installés est géré par les outils de la distribution, pas par ce chemin sysfs."}
:::

## Lire les attributs

Les fichiers d'attributs exposent des valeurs ou contrôles individuels. Pour un périphérique bloc :

```bash
$ cat /sys/class/block/sda/dev
8:0
$ cat /sys/class/block/sda/ro
0
$ cat /sys/class/block/sda/size
1953525168
```

`dev` indique les numéros majeur et mineur. `ro` indique l'état de lecture seule. Pour les périphériques bloc Linux, `size` s'exprime conventionnellement en secteurs de 512 octets, quelle que soit la taille des secteurs physiques. Consultez toujours la documentation ABI du noyau pour les unités et le sens d'un attribut précis.

:::single-choice{#sysfs-dev-attribute}
Que contient normalement l'attribut sysfs `dev` d'un périphérique bloc ?

::option[Tous les fichiers actuellement stockés sur le périphérique.]{#sysfs-file-list explanation="L'arborescence d'un système de fichiers n'est pas intégrée dans ce petit attribut."}
::option[Le nom du paquet qui a installé le matériel.]{#sysfs-package-name explanation="Le matériel n'est pas installé comme un paquet identifié par l'attribut `dev`."}
::option[Ses numéros majeur et mineur.]{#sysfs-major-minor .correct explanation="Cet attribut relie l'objet sysfs à l'identité du périphérique bloc correspondant."}
:::

## Relier `/sys` et `/dev`

`/dev` contient les nœuds que les applications ouvrent pour les E/S. `/sys` expose les relations, propriétés, états et certains contrôles des objets. Un nœud bloc comme `/dev/sda` peut correspondre à `/sys/dev/block/8:0`, lequel se résout vers l'objet sysfs concerné.

Ces deux interfaces se complètent. Aucune ne constitue à elle seule un inventaire exhaustif de tous les faits matériels, et un périphérique peut disparaître pendant son inspection.

:::single-choice{#sysfs-versus-dev}
Quelle affirmation distingue correctement `/sys` de `/dev` ?

::option[`/sys` stocke les documents utilisateur et `/dev` les archives de paquets.]{#sysfs-dev-user-files explanation="Aucun de ces répertoires n'a ces rôles ordinaires de stockage de données."}
::option[`/sys` expose les attributs des objets du noyau ; `/dev` fournit des nœuds pour les E/S.]{#sysfs-dev-distinction .correct explanation="Sysfs modélise les objets et contrôles, tandis que les nœuds acheminent les opérations vers des pilotes caractère ou bloc."}
::option[Les deux sont des listes statiques créées une fois à l'installation.]{#sysfs-dev-static explanation="Leur état visible change avec l'apparition et la disparition des périphériques et objets du noyau."}
:::

## Écrire des attributs sans risque

Certains attributs sysfs sont inscriptibles et peuvent modifier l'état d'alimentation, l'association des pilotes, le comportement des files, l'autorisation des périphériques, les LED ou d'autres contrôles actifs. Une écriture textuelle réussie peut agir immédiatement sur le matériel ou les services ; elle n'équivaut pas à la modification d'une configuration persistante.

Lisez l'ABI documentée et la valeur actuelle, déterminez comment rendre le réglage persistant, et ne testez que sur un système autorisé. Ne modifiez jamais récursivement les permissions et n'écrivez pas de valeurs devinées dans `/sys`.

:::single-choice{#sysfs-write-risk}
Pourquoi une écriture dans un attribut sysfs peut-elle être importante pour l'exploitation ?

::option[Chaque écriture crée une copie de sauvegarde ordinaire sur le disque.]{#sysfs-backup-copy explanation="Sysfs est virtuel et ne fournit pas de sauvegarde automatique des changements de contrôle."}
::option[Sysfs ignore toutes les écritures, même dans un attribut inscriptible.]{#sysfs-ignore-writes explanation="Les attributs inscriptibles existent précisément pour accepter des valeurs de contrôle prises en charge."}
::option[L'écriture peut invoquer un contrôle actif du noyau ou du pilote.]{#sysfs-live-control .correct explanation="Les attributs inscriptibles sont des interfaces actives qui peuvent modifier immédiatement le comportement d'un périphérique."}
:::

Utilisez [Explorer les périphériques matériels sous Linux](https://labex.io/fr/labs/comptia-explore-hardware-devices-in-linux-590861) pour parcourir sysfs en lecture seule et le relier aux nœuds de périphériques.

## Résumé

Vous savez maintenant utiliser sysfs comme une vue structurée des objets actifs du noyau.

1. Parcourir les vues par périphérique, classe, bus, bloc et numéro.
2. Lire un attribut documenté à la fois avec ses unités correctes.
3. Relier les objets sysfs aux nœuds de `/dev`.
4. Considérer les attributs inscriptibles comme des interfaces de contrôle actives.
