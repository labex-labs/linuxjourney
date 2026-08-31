---
lesson_id: "device-types"
course_id: "devices"
lang: "fr"
order_index: 2
title: "types de périphériques"
description: "Apprenez à distinguer les nœuds caractère et bloc des tubes, sockets et objets ordinaires du système de fichiers."
meta_title: "types de périphériques - Périphériques"
meta_description: "Explorez les différents types de périphériques Linux, y compris les périphériques caractère, bloc, tube (pipe) et socket. Apprenez comment Linux gère les périphériques, comment identifier un fichier de périphérique avec `ls -l /dev`, et comprenez le rôle des numéros de périphérique majeurs et mineurs."
meta_keywords: "périphériques linux, types de périphériques linux, fichier de périphérique, périphérique caractère, périphérique bloc, numéros majeurs mineurs, linux pour périphériques, répertoire /dev"
---

Le premier caractère du mode affiché par `ls -l` indique le type d'objet du système de fichiers. Sous `/dev`, les fichiers spéciaux caractère et bloc sont des nœuds de périphériques. Des tubes et des sockets Unix peuvent aussi s'y trouver, mais ce sont des objets de communication interprocessus, pas des nœuds matériels.

```text
$ ls -l /dev/null /dev/sda /run/systemd/journal/dev-log /tmp/example-fifo
crw-rw-rw- 1 root root 1, 3 ... /dev/null
brw-rw---- 1 root disk 8, 0 ... /dev/sda
srw-rw-rw- 1 root root      ... /run/systemd/journal/dev-log
prw------- 1 user user      ... /tmp/example-fifo
```

Les entrées et permissions dépendent du système ; cet exemple illustre uniquement les caractères de type.

## Nœuds de périphériques caractère

Un `c` indique un périphérique caractère. Il expose généralement une interface orientée flux ou propre au périphérique, plutôt qu'un stockage adressable en blocs de taille fixe. Les terminaux et les pseudo-périphériques comme `/dev/null` en sont des exemples.

Le terme « caractère » ne signifie pas que chaque appel système transfère exactement un caractère. Les applications peuvent lire ou écrire des tampons, tandis que le pilote définit le blocage, le cadrage et les opérations de contrôle.

:::single-choice{#device-types-character-marker}
Quel premier caractère de mode désigne un nœud de périphérique caractère ?

::option[`b`]{#device-types-marker-block explanation="Le marqueur `b` désigne un nœud de périphérique bloc."}
::option[`p`]{#device-types-marker-pipe explanation="Le marqueur `p` désigne une FIFO, ou tube nommé."}
::option[`c`]{#device-types-marker-character .correct explanation="Les fichiers spéciaux caractère commencent par `c` dans le mode d'une liste longue."}
:::

## Nœuds de périphériques bloc

Un `b` indique un périphérique bloc. Ces périphériques fournissent un stockage adressable par blocs au travers de la couche bloc du noyau et prennent en charge des opérations comme les E/S avec tampon, le partitionnement et les systèmes de fichiers. Disques, partitions et volumes logiques possèdent couramment des nœuds bloc.

Un nœud bloc n'est pas un système de fichiers monté. Il représente un périphérique de stockage ou une région logique ; un système de fichiers peut y être créé puis monté séparément. Écrire des données brutes dans le mauvais nœud peut détruire des tables de partitions, des systèmes de fichiers ou des données utilisateur.

:::single-choice{#device-types-block-marker}
Que signifie le premier caractère de mode `b` ?

::option[Une tâche du shell exécutée en arrière-plan.]{#device-types-background-job explanation="L'état d'une tâche du shell n'est pas codé comme caractère de type du système de fichiers."}
::option[Une interface de périphérique bloc.]{#device-types-block-device .correct explanation="Les fichiers spéciaux bloc exposent un stockage adressable par l'intermédiaire du sous-système bloc du noyau."}
::option[Un lien symbolique cassé.]{#device-types-broken-link explanation="Les liens symboliques utilisent `l`, que leur cible existe ou non."}
:::

## FIFO et nœuds de sockets

Un `p` désigne une FIFO, ou tube nommé. Elle fournit un flux d'octets nommé par lequel des processus communiquent. Après leur consommation, les données ne sont pas stockées durablement dans le nœud.

Un `s` désigne un nœud de socket de domaine Unix. Il nomme un point de terminaison local et peut offrir des communications connectées ou par datagrammes, le passage de descripteurs et des informations d'identification des pairs. Les sockets réseau à adresses Internet n'ont pas nécessairement de nœud dans le système de fichiers.

Ni les FIFO ni les sockets Unix n'utilisent de numéros majeur et mineur pour sélectionner un pilote matériel.

:::single-choice{#device-types-pipe-socket-distinction}
Quelle affirmation distingue correctement ces types d'objets de communication ?

::option[`p` marque une partition et `s` un stockage à l'état solide.]{#device-types-storage-letters explanation="Les partitions sont normalement des périphériques bloc et ces lettres ne codent pas la technologie de stockage."}
::option[`p` marque une FIFO et `s` un nœud de socket de domaine Unix.]{#device-types-p-and-s .correct explanation="Ce sont deux types distincts d'objets du système de fichiers employés pour les communications interprocessus locales."}
::option[Les deux types identifient des pilotes bloc par des numéros majeurs.]{#device-types-ipc-major explanation="Les FIFO et sockets ne sont pas des nœuds de périphériques caractère ou bloc."}
:::

## Numéros majeur et mineur

Les nœuds caractère et bloc stockent un numéro de périphérique divisé en parties majeure et mineure. Dans une liste longue, ils remplacent la colonne habituelle de taille :

```text
brw-rw---- 1 root disk 8, 0 ... /dev/sda
```

Cette paire indique au noyau l'interface enregistrée et l'instance auxquelles le nœud s'adresse. Le numéro majeur est associé à un pilote ou une classe, et le pilote interprète le numéro mineur. Ne figez pas d'hypothèse telle que « le mineur zéro désigne toujours le premier disque » : la correspondance dépend du sous-système et des interfaces du noyau.

Affichez explicitement le type et les numéros avec :

```bash
$ stat -c 'type=%F major=%t minor=%T path=%n' /dev/null
```

GNU `stat` affiche les valeurs `%t` et `%T` en hexadécimal.

:::single-choice{#device-types-major-minor-scope}
Quels objets utilisent des numéros majeur et mineur pour identifier une interface de périphérique du noyau ?

::option[Tous les fichiers ordinaires et répertoires.]{#device-types-all-files explanation="Les fichiers ordinaires utilisent une taille et des métadonnées de système de fichiers plutôt qu'une paire majeur/mineur."}
::option[Uniquement les liens symboliques dont la cible manque.]{#device-types-broken-symlinks explanation="Les liens symboliques stockent un chemin et ne deviennent pas des nœuds lorsque leur cible est absente."}
::option[Les nœuds de périphériques caractère et bloc.]{#device-types-device-number-nodes .correct explanation="Leurs métadonnées spéciales d'inode contiennent le numéro acheminé vers l'interface d'un pilote."}
:::

## Résumé

Vous savez maintenant interpréter les types spéciaux du système de fichiers sans tous les prendre pour des périphériques matériels.

1. Lire `c` comme nœud caractère et `b` comme nœud bloc.
2. Lire `p` comme FIFO et `s` comme socket Unix.
3. Associer les numéros majeur et mineur aux seuls nœuds de périphériques.
4. Considérer l'accès brut aux périphériques bloc comme potentiellement destructeur.
