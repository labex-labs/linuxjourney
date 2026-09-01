---
lesson_id: "systemd-overview"
course_id: "init"
lang: "fr"
order_index: 5
title: "Présentation de systemd"
description: "Découvrez comment systemd charge des unités, résout leurs dépendances, active des targets et gère les ressources système et utilisateur."
meta_title: "Présentation de systemd - Init"
meta_description: "Découvrez le système d'initialisation systemd, ses unités et targets pour gérer le démarrage de Linux et les services système."
meta_keywords: "systemd, système init, unités systemd, targets systemd, démarrage Linux, services Linux, gestion système"
---

Systemd est le gestionnaire d'initialisation et de services employé comme PID 1 par de nombreuses distributions Linux actuelles. Le projet fournit aussi des composants de journalisation, périphériques, sessions, réseau et temps, entre autres, mais les distributions choisissent ceux qu'elles déploient.

## Confirmer le gestionnaire actif

Examinez l'état réel plutôt que la présence de répertoires installés :

```bash
$ ps -p 1 -o pid,comm,args=
$ systemctl is-system-running
```

`/usr/lib/systemd/` peut exister alors qu'un autre programme joue le rôle de PID 1, et un conteneur peut exposer son propre espace de noms de PID. `systemctl` possède aussi des modes pour le gestionnaire utilisateur et pour les machines distantes ou conteneurs ; identifiez donc le gestionnaire visé par l'opération.

:::single-choice{#systemd-overview-detection} Qu'est-ce qui identifie le plus directement systemd comme gestionnaire d'initialisation du système ?

::option[Un répertoire nommé `/usr/lib/systemd` existe.]{#systemd-overview-directory explanation="Les bibliothèques et fichiers d'unités peuvent rester installés sans que systemd joue le rôle de PID 1."}
::option[Un utilisateur a exécuté une commande nommée `systemctl`.]{#systemd-overview-command-executed explanation="Le programme client peut exister même si aucun gestionnaire systemd système n'est disponible."}
::option[Le PID 1 de l'hôte est systemd.]{#systemd-overview-pid-one .correct explanation="Le premier processus en cours d'exécution constitue une preuve plus forte que les fichiers installés ou les noms de paquets."}
:::

## Les unités comme objets gérés

Une unité est le modèle nommé d'une ressource ou activité dans systemd. Parmi les types courants :

- `.service` pour les processus et démons ;
- `.socket` pour l'activation par socket ;
- `.mount` et `.automount` pour les systèmes de fichiers ;
- `.timer` et `.path` pour l'activation pilotée par des événements ;
- `.target` pour le regroupement et la synchronisation ;
- `.device`, `.swap`, `.slice` et `.scope` pour les autres ressources gérées.

L'état d'une unité n'est pas toujours « en cours d'exécution ». Un montage peut être monté, un minuteur en attente, un périphérique présent et une target active une fois ses dépendances atteintes.

:::single-choice{#systemd-overview-group-unit} Quel type d'unité regroupe couramment d'autres unités et fournit un point de synchronisation ?

::option[`.socket`]{#systemd-overview-socket explanation="Les unités socket exposent des points d'accès IPC ou réseau et peuvent activer des services."}
::option[`.target`]{#systemd-overview-target .correct explanation="Les unités target rassemblent des dépendances et représentent des étapes du démarrage ou du fonctionnement."}
::option[`.timer`]{#systemd-overview-timer explanation="Les unités timer planifient une activation selon une heure calendaire ou monotone."}
:::

## Chemins de chargement et surcharges des unités

Les unités système peuvent être chargées depuis des chemins de la distribution et de l'administrateur, notamment :

- `/usr/lib/systemd/system/` pour les unités fournies par les paquets sur de nombreuses distributions ;
- `/run/systemd/system/` pour la configuration générée à l'exécution ou transitoire ;
- `/etc/systemd/system/` pour la configuration locale persistante et les surcharges de l'administrateur.

Les chemins exacts des fournisseurs peuvent différer. Une configuration locale prioritaire remplace les fichiers moins prioritaires de même nom. Préférez les surcharges partielles créées par `systemctl edit UNITÉ` à la copie et modification d'un fichier fournisseur complet, afin que les mises à jour des paquets restent visibles.

:::single-choice{#systemd-overview-local-override} Où les surcharges locales persistantes des unités système doivent-elles normalement résider ?

::option[Dans `/proc/systemd/`.]{#systemd-overview-proc-systemd explanation="Procfs est une interface d'exécution du noyau, pas une configuration persistante d'unités."}
::option[Sous `/etc/systemd/system/`.]{#systemd-overview-etc-system .correct explanation="La couche de configuration de l'administrateur prend la priorité sur les unités fournies par les paquets."}
::option[Dans les octets de code d'amorçage MBR du disque.]{#systemd-overview-mbr-units explanation="Les unités de services sont des fichiers de configuration de l'espace utilisateur."}
:::

## Dépendances et ordre

Systemd construit une transaction à partir des relations de dépendances. `Wants=` et `Requires=` ajoutent d'autres unités à la transaction avec des degrés d'exigence différents. `Before=` et `After=` précisent l'ordre lorsque les deux unités sont planifiées ; à eux seuls, ils ne provoquent pas le démarrage de l'autre unité.

Une ligne `After=network.target` ne prouve pas que la connectivité, le DNS ou un point d'accès distant précis est disponible. Les services doivent employer l'intégration network-online appropriée ou mettre en œuvre leurs propres tentatives et leur propre détection de disponibilité.

:::single-choice{#systemd-overview-after-semantics} Que précise à lui seul `After=other.service` ?

::option[La garantie que le point d'accès applicatif de l'autre service est sain.]{#systemd-overview-after-health explanation="La fin de l'ordonnancement et la disponibilité de l'application sont deux notions distinctes."}
::option[L'ordre si les deux unités font partie de la transaction.]{#systemd-overview-after-ordering .correct explanation="Une exigence distincte comme Wants ou Requires est nécessaire pour ajouter l'autre unité."}
::option[L'activation automatique des deux unités lors de chaque futur démarrage.]{#systemd-overview-after-enable explanation="L'activation relève des métadonnées d'installation et n'est pas impliquée par l'ordre."}
:::

## Targets et transaction de démarrage par défaut

`default.target` est généralement un alias vers une target comme `multi-user.target` ou `graphical.target`. Systemd lance une transaction pour celle-ci et ses dépendances, ce qui permet au travail indépendant de progresser simultanément tout en respectant les ordres explicites.

Les targets ne ressemblent aux niveaux d'exécution qu'à un niveau général de compatibilité. Plusieurs peuvent être actives en même temps, il est possible d'en créer de personnalisées et l'activité d'une target ne signifie pas que chaque service de la machine est sain.

:::single-choice{#systemd-overview-default-target} Que sélectionne normalement `default.target` ?

::option[Le périphérique bloc par défaut que `mkfs` doit effacer.]{#systemd-overview-default-disk explanation="Les targets décrivent l'activation des unités, pas le choix destructif d'un stockage."}
::option[La seule target qui puisse jamais être active.]{#systemd-overview-only-target explanation="Les targets sont des regroupements et plusieurs peuvent être actives pendant un même démarrage."}
::option[La transaction de target employée pour un démarrage normal du système.]{#systemd-overview-normal-boot .correct explanation="Il s'agit généralement d'un alias vers la target multi-utilisateur ou graphique choisie par l'administrateur."}
:::

## Résumé

Vous savez maintenant décrire systemd au moyen des gestionnaires réels, des unités et des transactions.

1. Confirmer systemd au moyen du PID 1 et de la connexion au gestionnaire concernés.
2. Associer les types de ressources aux suffixes d'unités.
3. Placer les surcharges locales au-dessus de la configuration du fournisseur.
4. Distinguer force des dépendances, ordre et disponibilité applicative.
5. Considérer les targets comme des regroupements et étapes, pas comme des états exclusifs.
