---
lesson_id: "kernel-overview"
course_id: "kernel"
lang: "fr"
order_index: 1
title: "Présentation du noyau"
description: "Découvrez comment le noyau Linux sert d'intermédiaire pour le matériel, les ressources, l'isolation et les demandes de l'espace utilisateur."
meta_title: "Présentation du noyau - Noyau"
meta_description: "Découvrez le rôle essentiel du noyau Linux dans la gestion du matériel, des ressources et de l'espace utilisateur."
meta_keywords: "noyau Linux, système exploitation, matériel, espace utilisateur, ressources, isolation, présentation noyau"
---

Linux est le noyau du système d'exploitation : le logiciel privilégié qui gère les processeurs, la mémoire, les périphériques, les processus et les abstractions communes de ressources. Un système Linux complet comprend aussi des bibliothèques, utilitaires, services, shells et logiciels graphiques dans l'espace utilisateur, ainsi que les règles de la distribution.

## Ressources matérielles

Les processeurs exécutent les instructions, la mémoire conserve l'état actif et les contrôleurs relient le stockage, les réseaux, les écrans, les périphériques d'entrée et les autres appareils. Le matériel expose des mécanismes propres à l'architecture et aux périphériques plutôt qu'une interface unique et sûre pour chaque application.

Le noyau initialise et contrôle ces ressources au moyen du code d'architecture et des pilotes. Il traite les interruptions, la coordination DMA, les minuteurs et les événements de gestion de l'alimentation tout en imposant des limites d'accès entre les charges.

:::single-choice{#kernel-overview-hardware-manager} Quelle couche coordonne normalement les pilotes de périphériques et les interruptions matérielles sous Linux ?

::option[Le fichier d'historique du shell de chaque utilisateur.]{#kernel-overview-shell-history explanation="L'historique consigne les commandes et ne traite pas l'exécution matérielle."}
::option[L'index du dépôt de paquets.]{#kernel-overview-repository-index explanation="Les métadonnées du dépôt décrivent les paquets logiciels, pas les événements matériels réels."}
::option[Le noyau.]{#kernel-overview-kernel-layer .correct explanation="Le code privilégié du noyau relie les événements matériels et les opérations des pilotes à des interfaces système contrôlées."}
:::

## Responsabilités du noyau

Ses principales responsabilités comprennent :

- planifier les threads exécutables sur les processeurs ;
- créer et isoler les espaces d'adressage virtuels ;
- appliquer les identifiants, permissions et règles de sécurité des processus ;
- fournir les systèmes de fichiers, le réseau, l'IPC et les interfaces de périphériques ;
- traiter les signaux, minuteurs et le cycle de vie des processus ;
- allouer, comptabiliser et récupérer les ressources.

Linux est couramment décrit comme un noyau monolithique, car les services centraux et de nombreux pilotes s'exécutent dans un même espace d'adressage privilégié. Il est aussi modulaire : les composants pris en charge peuvent être chargés et déchargés comme modules du noyau. Un bogue dans du code privilégié peut compromettre tout le système ; les mises à jour du noyau et l'origine des modules sont donc essentielles à la sécurité.

:::single-choice{#kernel-overview-scheduler-role} Que gère l'ordonnanceur du noyau ?

::option[La prochaine page de documentation que l'utilisateur lira.]{#kernel-overview-documentation explanation="La navigation dans l'apprentissage ne relève pas de l'ordonnancement du noyau."}
::option[Les threads exécutables qui reçoivent du temps processeur.]{#kernel-overview-thread-scheduling .correct explanation="L'ordonnanceur choisit les contextes d'exécution selon les règles, priorités, affinités et processeurs disponibles."}
::option[La clé de signature du dépôt à laquelle l'administrateur doit faire confiance.]{#kernel-overview-repository-key explanation="La configuration de confiance relève des règles de gestion des paquets."}
:::

## Espace utilisateur

L'espace utilisateur contient les processus ordinaires : init et les services, outils en ligne de commande, environnements d'exécution des langages, bases de données, shells et applications de bureau. Les privilèges matériels empêchent ces programmes d'exécuter directement de nombreuses instructions sensibles ou d'accéder arbitrairement à la mémoire du noyau.

Les processus demandent du travail au noyau au moyen des appels système et interagissent avec les interfaces exposées, comme les descripteurs de fichiers, sockets, nœuds de périphériques, procfs, sysfs, netlink et mappages mémoire. Des bibliothèques enveloppent souvent ces interfaces dans des API de plus haut niveau.

L'utilisateur root de l'espace utilisateur possède de vastes autorisations selon les règles, mais s'exécute normalement toujours dans le mode utilisateur du processeur. L'identité de l'utilisateur et le mode de privilège du processeur sont des notions distinctes.

:::single-choice{#kernel-overview-root-user-mode} Une application ordinaire appartenant à root exécute-t-elle toutes ses instructions en mode noyau ?

::option[Oui ; l'UID 0 transforme définitivement chaque instruction en ring 0.]{#kernel-overview-root-ring-zero explanation="Un processus root ordinaire reste un processus de l'espace utilisateur."}
::option[Oui ; les applications root deviennent automatiquement des modules chargeables du noyau.]{#kernel-overview-root-module explanation="L'UID propriétaire ne transforme pas un exécutable utilisateur en code du noyau."}
::option[Non ; elle s'exécute normalement en mode utilisateur et entre dans le noyau par des interfaces contrôlées.]{#kernel-overview-root-userspace .correct explanation="Les identifiants root influencent les autorisations, tandis que le mode du processeur ne change que pendant l'entrée et l'exécution du noyau."}
:::

## Limites et abstractions

Le noyau présente des processus, fichiers, sockets et espaces d'adressage virtuels au lieu d'exposer directement les mécanismes physiques bruts. Ces abstractions favorisent l'isolation et la portabilité, mais ne constituent pas à elles seules des frontières de sécurité parfaites. Les espaces de noms, cgroups, capacités, modules de sécurité, seccomp et la virtualisation ajoutent des contrôles spécialisés.

Pendant un dépannage, demandez-vous quelle couche possède le comportement : application, bibliothèque, interface d'appel système, système de fichiers, pilote, sous-système du noyau, micrologiciel ou matériel. Des preuves recueillies dans la mauvaise couche peuvent conduire à des corrections erronées.

:::single-choice{#kernel-overview-system-call-boundary} Qu'est-ce qu'un appel système ?

::option[Une demande contrôlée de l'espace utilisateur pour obtenir un service du noyau.]{#kernel-overview-controlled-request .correct explanation="Le processeur entre en mode noyau par une interface définie, où le noyau valide puis effectue l'opération."}
::option[Une commande directe qui contourne tous les contrôles d'accès.]{#kernel-overview-bypass-checks explanation="Les appels système sont précisément l'endroit où s'effectuent de nombreux contrôles de validation et d'autorisation."}
::option[Une archive de paquet qui contient un pilote de périphérique.]{#kernel-overview-package-archive explanation="Les paquets peuvent fournir des logiciels, mais un appel système est une interface d'exécution."}
:::

Utilisez [Gérer les modules du noyau sous Linux](https://labex.io/fr/labs/comptia-manage-kernel-modules-in-linux-590865) pour observer une partie modulaire du noyau dans un environnement contrôlé.

## Résumé

Vous savez maintenant placer le noyau entre les ressources physiques et les processus isolés de l'espace utilisateur.

1. Relier les pilotes et le code d'architecture au contrôle du matériel.
2. Identifier les responsabilités liées à l'ordonnancement, la mémoire, la sécurité, les systèmes de fichiers et le réseau.
3. Distinguer les identifiants root du mode noyau du processeur.
4. Situer l'interaction utilisateur-noyau dans les interfaces contrôlées à l'exécution.
