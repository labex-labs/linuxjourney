---
lesson_id: "boot-process-init"
course_id: "boot-system"
lang: "fr"
order_index: 5
title: "Processus de Démarrage : Init"
description: "Découvrez comment le PID 1 initialise l'espace utilisateur, supervise les services, récupère les processus enfants et coordonne l'arrêt."
meta_title: "Processus de Démarrage : Init - Démarrer le Système"
meta_description: "Explorez le cœur du processus de démarrage Linux dans ce guide pour débutants. Apprenez les différents systèmes init Linux, incluant le traditionnel System V, Upstart, et la norme moderne, systemd. Comprenez comment ces systèmes démarrent et gèrent les services sur votre machine."
meta_keywords: "Init Linux, systemd, System V init, Upstart, processus de démarrage Linux, tutoriel Linux, Linux débutant, guide Linux"
---

Le noyau lance le premier processus de l'espace utilisateur avec le PID 1 dans un espace de noms de PID. Sur un système Linux complet, ce processus init établit l'environnement de services. Dans un conteneur, le PID 1 peut être une petite enveloppe init ou l'application elle-même, mais il conserve des responsabilités particulières concernant les signaux et la récupération des processus enfants.

## Responsabilités du PID 1

Un système init :

- démarre et supervise généralement les services, les connexions, les montages et d'autres unités de travail ;
- ordonne ces travaux selon leurs dépendances et l'état cible configuré ;
- adopte et récupère les processus enfants orphelins ;
- réagit aux défaillances des services selon la politique définie ;
- coordonne l'arrêt et le redémarrage ordonnés.

La frontière exacte varie. La gestion des périphériques, le réseau, la journalisation et les tâches planifiées peuvent être des programmes distincts supervisés par init plutôt que du code intégré au PID 1.

:::single-choice{#boot-init-pid-one-role} Quelle responsabilité est propre au PID 1 dans son espace de noms de PID ?

::option[Compiler chaque application depuis ses sources à chaque démarrage.]{#boot-init-compile-apps explanation="Le démarrage normal des services utilise des programmes installés au lieu de reconstruire tous les logiciels."}
::option[Définir la taille des secteurs physiques du disque.]{#boot-init-sector-size explanation="Le matériel de stockage et ses pilotes exposent la géométrie des secteurs avant qu'init ne gère les services."}
::option[Adopter et récupérer les processus enfants orphelins.]{#boot-init-reap-orphans .correct explanation="Le PID 1 est le parent final et doit récupérer l'état de terminaison afin d'éviter l'accumulation de processus zombies."}
:::

## Init System V et niveaux d'exécution

Le sysvinit traditionnel emploie une configuration comme `/etc/inittab` et des scripts de démarrage et d'arrêt propres à chaque niveau d'exécution. Un niveau d'exécution représente un mode de fonctionnement, mais le sens des niveaux numérotés peut différer selon les distributions. L'ordre des scripts suit des conventions et les outils de la distribution peuvent l'étendre ou le paralléliser.

Ne déduisez pas le système init actif de la seule existence de `/etc/init.d/` ; des scripts de compatibilité peuvent subsister alors que le PID 1 appartient à une autre implémentation.

:::single-choice{#boot-init-sysv-runlevel} Que représente un niveau d'exécution System V ?

::option[Un numéro de version du noyau choisi par le chargeur.]{#boot-init-runlevel-kernel explanation="Le choix du noyau relève du chargeur et n'est pas codé par un niveau d'exécution init."}
::option[Un mode de fonctionnement configuré et associé à des actions sur les services.]{#boot-init-runlevel-mode .correct explanation="Les dispositions SysV associent les niveaux à des ensembles de scripts de démarrage ou d'arrêt et à leur ordre."}
::option[Le pourcentage actuel d'utilisation des inodes d'un système de fichiers.]{#boot-init-runlevel-inodes explanation="La capacité des métadonnées du système de fichiers n'a aucun rapport avec les modes de fonctionnement des services."}
:::

## Systèmes fondés sur les événements et les dépendances

Upstart a introduit un modèle de tâches piloté par les événements. Il a été utilisé par d'anciennes versions d'Ubuntu et quelques autres systèmes, mais présente aujourd'hui surtout un intérêt historique ou pour l'exploitation de systèmes anciens.

systemd est très répandu dans les distributions généralistes actuelles. Il modélise les services, sockets, montages, minuteurs, périphériques, cibles et autres ressources comme des unités. Les dépendances déclaratives et les mécanismes d'activation permettent aux travaux indépendants de progresser simultanément tout en respectant l'ordre nécessaire.

Parmi les autres conceptions actives d'init et de supervision figurent OpenRC, runit, s6 et l'init de BusyBox. « Le plus récent » n'est pas une règle de compatibilité utile : identifiez ce qu'exécute réellement le système et consultez sa documentation.

:::single-choice{#boot-init-systemd-unit-model} Comment systemd représente-t-il les ressources gérées comme les services et les montages ?

::option[Comme des entrées de partitions primaires MBR.]{#boot-init-systemd-partitions explanation="Les métadonnées de partitionnement du disque n'ont aucun rapport avec les unités du gestionnaire de services."}
::option[Uniquement comme des liens physiques vers l'exécutable du PID 1.]{#boot-init-systemd-hard-links explanation="Les unités sont des objets de configuration et d'exécution, pas de simples alias d'inodes."}
::option[Comme des unités dotées de dépendances et de relations d'activation.]{#boot-init-systemd-units .correct explanation="Les types d'unités fournissent un modèle commun pour l'ordre, l'état et la supervision."}
:::

## Identifier le système init actif

Inspectez le PID 1 plutôt que de vous fier à des fichiers installés :

```bash
$ ps -p 1 -o pid,comm,args=
$ readlink /proc/1/exe
```

Les permissions, conteneurs et espaces de noms influencent ce que vous voyez. Une commande exécutée dans un conteneur indique le PID 1 de cet espace de noms, pas nécessairement l'init de l'hôte. Une fois le système identifié, utilisez ses outils natifs d'état et de journalisation au lieu de mélanger les commandes de plusieurs familles d'init.

:::single-choice{#boot-init-detect-running} Pourquoi l'inspection du PID 1 est-elle préférable à la recherche d'un ancien répertoire de scripts ?

::option[Le PID 1 porte toujours le même nom d'exécutable sur tous les systèmes Linux.]{#boot-init-same-name explanation="systemd, sysvinit, BusyBox, les programmes init de conteneurs et d'autres peuvent occuper le PID 1."}
::option[Des fichiers de compatibilité peuvent exister même si une autre implémentation d'init fonctionne.]{#boot-init-compatibility-files .correct explanation="L'exécutable actif du PID 1 constitue une preuve plus forte du système init réellement utilisé."}
::option[Les anciens répertoires sont automatiquement supprimés à chaque démarrage.]{#boot-init-directories-deleted explanation="Les fichiers de compatibilité installés peuvent subsister d'un démarrage à l'autre."}
:::

## Résumé

Vous savez maintenant expliquer init comme un rôle plutôt que comme une implémentation obligatoire.

1. Relier le PID 1 à l'initialisation des services, à la récupération des processus et à l'arrêt.
2. Reconnaître les niveaux d'exécution System V comme des modes définis par la distribution.
3. Relier les ressources et dépendances de systemd à des unités.
4. Inspecter le PID 1 actif dans l'espace de noms concerné avant de choisir les outils.
