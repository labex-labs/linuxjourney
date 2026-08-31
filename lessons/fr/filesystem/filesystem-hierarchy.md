---
lesson_id: "filesystem-hierarchy"
course_id: "filesystem"
lang: "fr"
order_index: 1
title: "Hiérarchie du système de fichiers"
description: "Découvrez le rôle prévu des principaux répertoires Linux et les différences possibles dans les organisations fusionnées modernes."
meta_title: "Hiérarchie du système de fichiers - Le système de fichiers"
meta_description: "Explorez la hiérarchie standard du système de fichiers Linux et le rôle des répertoires essentiels comme /bin, /etc, /home et /var."
meta_keywords: "hiérarchie système de fichiers Linux, arborescence Linux, structure répertoires Linux, FHS, /bin, /etc, /home, /var"
---

Linux présente les systèmes de fichiers montés sous la forme d'une seule arborescence enracinée dans `/`. Le Filesystem Hierarchy Standard, ou FHS, attribue un rôle conventionnel à de nombreux répertoires, mais les distributions, conteneurs, systèmes immuables et règles locales peuvent différer. Examinez toujours la machine réelle avant de vous fier à un chemin.

```bash
$ ls -ld /*
```

## Racine et chemins système essentiels

- `/` est la racine de l'arborescence visible.
- `/etc` contient la configuration système propre à la machine. Il peut aussi renfermer des scripts exécutables d'assistance ou de démarrage : il serait donc inexact d'affirmer qu'il ne contient jamais de contenu exécutable.
- `/boot` contient les fichiers liés au démarrage, notamment les données du chargeur d'amorçage et, sur de nombreux systèmes, les noyaux et images du système de fichiers RAM initial.
- `/bin` et `/sbin` contiennent traditionnellement les commandes essentielles destinées aux utilisateurs et à l'administration système.
- `/lib` et ses variantes propres à une architecture contiennent traditionnellement les bibliothèques partagées et composants de chargement essentiels.

De nombreuses distributions actuelles utilisent une organisation `/usr` fusionnée, dans laquelle `/bin`, `/sbin` et `/lib` sont des liens symboliques vers les répertoires correspondants sous `/usr`. Servez-vous de la découverte des commandes et des informations des paquets plutôt que de supposer qu'un chemin est un répertoire physique ou un lien.

:::single-choice{#filesystem-hierarchy-configuration-directory}
Quel répertoire contient conventionnellement la configuration système propre à la machine ?

::option[`/proc`]{#filesystem-hierarchy-proc-config explanation="Procfs présente des interfaces actives pour les processus et le noyau, et non des fichiers persistants de configuration de la machine."}
::option[`/etc`]{#filesystem-hierarchy-etc .correct explanation="La configuration du système et des services est conventionnellement organisée sous `/etc`."}
::option[`/dev`]{#filesystem-hierarchy-dev-config explanation="`/dev` contient des objets d'exécution liés aux périphériques, pas la hiérarchie générale de configuration."}
:::

## Logiciels de la distribution et logiciels locaux

- `/usr` contient la principale hiérarchie partageable et largement en lecture seule du système d'exploitation et des applications, notamment les commandes, bibliothèques et données indépendantes de l'architecture.
- `/usr/local` est réservé aux logiciels et données installés par l'administrateur local en dehors de la gestion normale de `/usr` par la distribution.
- `/opt` peut accueillir des paquets applicatifs complémentaires dans des sous-arborescences autonomes.

Malgré son nom, `/usr` n'est normalement pas l'emplacement des fichiers personnels des utilisateurs. Les gestionnaires de paquets possèdent souvent une grande partie de cette arborescence ; copier des fichiers compilés localement dans `/usr/bin` peut donc entrer en conflit avec les paquets gérés.

:::single-choice{#filesystem-hierarchy-local-software}
Quel préfixe est conventionnellement réservé aux logiciels installés localement hors du contenu de `/usr` géré par la distribution ?

::option[`/usr/local`]{#filesystem-hierarchy-usr-local .correct explanation="La hiérarchie locale sépare les logiciels installés par l'administrateur de l'arborescence `/usr` principale de la distribution."}
::option[`/proc/local`]{#filesystem-hierarchy-proc-local explanation="Procfs est une interface virtuelle du noyau, et non un préfixe logiciel persistant."}
::option[`/dev/local`]{#filesystem-hierarchy-dev-local explanation="Le stockage des nœuds de périphériques n'est pas l'emplacement conventionnel des applications locales."}
:::

## Données des utilisateurs et des services

- `/home` contient conventionnellement les répertoires personnels des utilisateurs autres que root, même si un service d'annuaire ou une règle locale peut les placer ailleurs.
- `/root` est le répertoire personnel conventionnel du compte root.
- `/srv` est destiné aux données propres au site que sert ce système.

Le chemin d'un répertoire personnel provient des informations du compte, et non de la simple concaténation de `/home` et d'un nom d'utilisateur. Utilisez `getent passwd UTILISATEUR` ou le répertoire personnel résolu par le shell plutôt que de coder cette hypothèse en dur.

:::single-choice{#filesystem-hierarchy-root-home}
Quel est le répertoire personnel conventionnel du compte root ?

::option[`/home/root`]{#filesystem-hierarchy-home-root explanation="Les répertoires personnels ordinaires se trouvent souvent sous `/home`, mais root possède un chemin conventionnel distinct."}
::option[`/root`]{#filesystem-hierarchy-root .correct explanation="Le répertoire personnel du compte privilégié se situe conventionnellement directement sous la racine du système de fichiers."}
::option[`/usr/root`]{#filesystem-hierarchy-usr-root explanation="`/usr` est la hiérarchie des logiciels et données partagées, pas le répertoire personnel de root."}
:::

## Données variables, temporaires et d'exécution

- `/var` contient des données variables telles que journaux, caches, files d'attente et état applicatif. Les journaux système se trouvent souvent sous `/var/log`, bien que certains systèmes reposent surtout sur une interface de journalisation.
- `/run` contient l'état d'exécution volatil du démarrage en cours, comme les sockets, l'état des services et les fichiers PID. Il est normalement recréé au démarrage.
- `/tmp` accueille les fichiers temporaires et est généralement accessible en écriture à tous les utilisateurs avec la protection du sticky bit.
- `/var/tmp` est destiné aux fichiers temporaires qui doivent survivre plus longtemps que ceux de `/tmp`.

La politique de nettoyage de `/tmp` varie : ne supposez ni que les fichiers persistent jusqu'au redémarrage, ni qu'ils sont toujours supprimés à ce moment-là. Les applications doivent créer leurs fichiers temporaires de façon sûre, sans noms prévisibles.

:::single-choice{#filesystem-hierarchy-log-path}
Quel chemin stocke conventionnellement les fichiers journaux du système ?

::option[`/etc/log`]{#filesystem-hierarchy-etc-log explanation="`/etc` sert à la configuration, et non aux données de journal qui s'accumulent normalement."}
::option[`/var/log`]{#filesystem-hierarchy-var-log .correct explanation="Les journaux sont une catégorie de données système changeantes organisée sous la hiérarchie des données variables."}
::option[`/boot/log`]{#filesystem-hierarchy-boot-log explanation="`/boot` est réservé aux éléments liés au démarrage, pas aux journaux généraux des services."}
:::

## Périphériques, interfaces du noyau et points de montage

- `/dev` contient les nœuds de périphériques et les liens d'exécution associés.
- `/proc` expose des interfaces des processus et du noyau au moyen de procfs.
- `/sys` expose les objets, périphériques, pilotes et attributs du noyau au moyen de sysfs.
- `/media` sert souvent au montage automatique des supports amovibles.
- `/mnt` est un emplacement conventionnel pour les montages temporaires effectués par l'administrateur.

Il s'agit de conventions, pas d'autorisations. Monter un autre système de fichiers sur un répertoire non vide masque temporairement le contenu antérieur de ce répertoire jusqu'au démontage.

:::single-choice{#filesystem-hierarchy-sysfs-path}
Quel chemin expose normalement le modèle de périphériques du noyau au moyen de sysfs ?

::option[`/srv`]{#filesystem-hierarchy-srv explanation="`/srv` est destiné aux données servies par le système."}
::option[`/sys`]{#filesystem-hierarchy-sys .correct explanation="Sysfs est conventionnellement monté dans `/sys` et présente périphériques, pilotes, bus et attributs."}
::option[`/opt`]{#filesystem-hierarchy-opt explanation="`/opt` contient les arborescences d'applications complémentaires facultatives."}
:::

Utilisez [Naviguer dans le système de fichiers sous Linux](https://labex.io/fr/labs/comptia-navigate-the-filesystem-in-linux-590971) pour examiner ces chemins et [Trouver des fichiers et des commandes sous Linux](https://labex.io/fr/labs/comptia-find-files-and-commands-in-linux-590834) pour éviter de vous fier à des emplacements supposés.

## Résumé

Vous savez maintenant associer les principaux chemins Linux à leur rôle prévu tout en tenant compte des variations réelles entre systèmes.

1. Partir de l'arborescence unifiée enracinée dans `/`.
2. Distinguer configuration, logiciels gérés, logiciels locaux et données variables.
3. Séparer les répertoires personnels et données de services de l'état d'exécution.
4. Reconnaître `/dev`, `/proc` et `/sys` comme des interfaces d'exécution particulières.
5. Examiner les liens symboliques, montages, données des comptes et règles de la distribution avant de supposer une organisation.
