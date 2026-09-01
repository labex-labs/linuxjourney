---
lesson_id: "boot-process-overview"
course_id: "boot-system"
lang: "fr"
order_index: 1
title: "Aperçu du processus de démarrage"
description: "Découvrez les principaux passages de relais, du micrologiciel de la plateforme au premier processus en espace utilisateur, en passant par le noyau."
meta_title: "Processus de démarrage - Démarrer le système"
meta_description: "Un aperçu clair du processus de démarrage Linux, détaillant les quatre étapes clés : BIOS, chargeur de démarrage, noyau et init. Découvrez le processus complet de démarrage du système d'exploitation Linux, de la mise sous tension à l'invite de connexion."
meta_keywords: "processus de démarrage Linux, démarrage linux, processus de démarrage linux, processus de démarrage du système d'exploitation linux, BIOS, chargeur de démarrage, noyau, init, tutoriel Linux, guide Linux, débutant"
---

Le démarrage est une chaîne de confiance et de transferts de contrôle qui transforme la réinitialisation de la plateforme en un environnement fonctionnel en espace utilisateur. Sur un PC courant, le parcours peut se résumer au micrologiciel, au gestionnaire ou chargeur de démarrage, au noyau avec un éventuel espace utilisateur précoce, puis au système init de PID 1. Les architectures, machines virtuelles, systèmes embarqués et conteneurs peuvent suivre d'autres parcours.

## Initialisation du micrologiciel

Le micrologiciel de la plateforme initialise suffisamment le processeur, la mémoire et les périphériques pour choisir une cible de démarrage. Les PC traditionnels suivent les conventions du BIOS ; les PC actuels emploient généralement l'UEFI. Les réglages du micrologiciel, l'ordre de démarrage, la vérification de la plateforme et la politique Secure Boot peuvent déterminer quel exécutable de l'étape suivante est autorisé.

Le micrologiciel ne comprend pas nécessairement le système de fichiers racine Linux installé. Il localise un chemin de démarrage selon son interface : par exemple, du code BIOS sur un disque choisi ou une entrée UEFI pointant vers un exécutable EFI dans une partition système EFI.

:::single-choice{#boot-overview-first-stage} Quel composant commence l'initialisation de la plateforme après la réinitialisation d'un PC typique ?

::option[Le shell interactif de l'utilisateur.]{#boot-overview-shell explanation="Un shell est lancé bien plus tard par les services de l'espace utilisateur ou le processus de connexion."}
::option[Le micrologiciel de la plateforme, comme le BIOS ou l'UEFI.]{#boot-overview-firmware .correct explanation="Le micrologiciel établit l'état matériel initial et choisit la cible de démarrage suivante avant l'exécution de Linux."}
::option[L'utilitaire de réparation du système de fichiers.]{#boot-overview-fsck explanation="Un outil de vérification peut intervenir plus tard selon la politique de démarrage, mais il ne constitue pas l'étape initiale du micrologiciel."}
:::

## Chargeur ou gestionnaire de démarrage

Un chargeur comme GRUB peut présenter des entrées, charger en mémoire le noyau Linux choisi et le système de fichiers RAM initial, construire la ligne de commande du noyau, puis lui transférer le contrôle. L'UEFI peut aussi charger directement un noyau construit comme exécutable EFI ; un chargeur distinct à plusieurs étapes est donc fréquent, mais pas universel.

Les artefacts choisis doivent être cohérents : la version du noyau, le contenu de l'initramfs, l'identifiant de la racine, les signatures de sécurité et les options de ligne de commande influencent tous la réussite du passage de relais suivant.

:::single-choice{#boot-overview-loader-role} Quelle responsabilité incombe couramment à un chargeur de démarrage Linux ?

::option[Charger le noyau choisi et lui transmettre sa ligne de commande.]{#boot-overview-load-kernel .correct explanation="Le chargeur prépare l'image du noyau et ses paramètres, souvent avec un initramfs."}
::option[Recréer tous les comptes utilisateur à chaque démarrage.]{#boot-overview-create-users explanation="Les bases persistantes de comptes relèvent de la configuration en espace utilisateur et ne sont pas recréées par le chargeur."}
::option[Planifier tous les processus d'application après la connexion.]{#boot-overview-schedule-apps explanation="L'ordonnancement du processeur relève du noyau en cours d'exécution."}
:::

## Noyau et espace utilisateur précoce

Le noyau se décompresse ou se reloge selon les besoins, initialise ses sous-systèmes essentiels, analyse sa ligne de commande et découvre le matériel disponible. Un initramfs peut fournir les modules et outils précoces nécessaires à la découverte du stockage, au RAID, au chiffrement, à LVM, au réseau ou à d'autres travaux permettant d'assembler le véritable système de fichiers racine.

Une fois la racine voulue disponible, l'espace utilisateur précoce bascule vers celle-ci et le noyau exécute le premier programme configuré de l'espace utilisateur. L'entité qui vérifie les systèmes de fichiers ou les remonte en lecture-écriture dépend de la conception de démarrage de la distribution, et non d'une séquence universelle.

:::single-choice{#boot-overview-initramfs-purpose} Pourquoi un système peut-il utiliser un initramfs ?

::option[Pour conserver définitivement dans le micrologiciel la session graphique de chaque utilisateur.]{#boot-overview-desktop-firmware explanation="Un initramfs est une image de système de fichiers utilisée au démarrage, pas un stockage de sessions dans le micrologiciel."}
::option[Pour fournir les premiers outils et pilotes nécessaires à l'accès au véritable système de fichiers racine.]{#boot-overview-early-root-tools .correct explanation="L'espace utilisateur précoce peut assembler une racine chiffrée, logique, en réseau ou dépendante d'un pilote."}
::option[Pour remplacer l'ordonnanceur de processus du noyau après la connexion.]{#boot-overview-replace-scheduler explanation="Le noyau conserve la responsabilité de l'ordonnancement pendant tout le fonctionnement."}
:::

## PID 1 et disponibilité du système

Le premier processus de l'espace utilisateur reçoit le PID 1. Sur de nombreuses distributions, il s'agit de systemd ; d'autres systèmes emploient sysvinit, OpenRC, runit, l'init de BusyBox ou un programme spécialisé. Le PID 1 établit l'environnement de services de l'espace utilisateur, récupère les processus enfants orphelins et gère les responsabilités d'arrêt.

Atteindre le PID 1 ne signifie pas que le système est entièrement prêt. Des services peuvent encore démarrer, des supports être montés, la configuration réseau rester en attente, et une connexion graphique ou en console n'est qu'un état cible possible.

:::single-choice{#boot-overview-final-stage} Qu'est-ce qui commence la principale étape d'initialisation de l'espace utilisateur ?

::option[La création du MBR protecteur du disque à chaque démarrage.]{#boot-overview-create-mbr explanation="La création de la table de partitions n'est pas une étape récurrente du démarrage normal."}
::option[La suppression de tous les paramètres de la ligne de commande du noyau.]{#boot-overview-delete-command-line explanation="Le noyau analyse et expose sa ligne de commande ; une telle suppression n'est pas requise."}
::option[L'exécution du programme init de PID 1.]{#boot-overview-pid-one .correct explanation="Après la préparation de la racine, le premier processus de l'espace utilisateur lance ou supervise les services nécessaires à l'état configuré du système."}
:::

Le laboratoire [Personnaliser le menu de démarrage GRUB2](https://labex.io/fr/labs/comptia-customize-the-grub2-boot-menu-in-linux-590859) illustre une méthode de configuration du chargeur. N'appliquez ces changements que dans un système de laboratoire permettant la récupération.

## Résumé

Vous savez maintenant suivre les principaux passages de relais du démarrage Linux sans les prendre pour des détails universels d'implémentation.

1. Commencer par l'initialisation du micrologiciel et le choix de la cible.
2. Relier le chargeur au noyau, à l'initramfs et à la ligne de commande.
3. Utiliser l'espace utilisateur précoce pour comprendre l'assemblage complexe de la racine.
4. Voir le PID 1 comme le début de l'initialisation des services, pas comme une preuve de disponibilité.
