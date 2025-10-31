---
index: 2
lang: "fr"
title: "Processus de Démarrage : BIOS"
meta_title: "Processus de Démarrage : BIOS - Démarrer le Système"
meta_description: "Découvrez la première étape du démarrage Linux : le BIOS. Apprenez comment il trouve le chargeur de démarrage via MBR ou GPT, et comprenez le rôle de l'UEFI. Ce guide explique le démarrage du système et aborde comment accéder au BIOS pour la configuration."
meta_keywords: "processus démarrage Linux, BIOS, MBR, UEFI, bios sous linux, bios linux, comment accéder au bios, chargeur de démarrage, démarrage système"
---

## Lesson Content

La première étape du processus de démarrage de Linux est le BIOS (Basic Input/Output System), qui effectue des vérifications cruciales de l'intégrité du système au démarrage. Le BIOS est un micrologiciel couramment trouvé dans les ordinateurs compatibles IBM PC, qui représentent la majorité des ordinateurs en usage aujourd'hui.

### Le Rôle du BIOS sous Linux

Lorsque vous allumez votre ordinateur, le **BIOS sous Linux** est le premier logiciel à s'exécuter. Sa fonction principale est d'initialiser et de tester le matériel du système, tel que le CPU, la mémoire et les disques durs. Vous avez probablement déjà interagi avec le micrologiciel BIOS pour modifier l'ordre de démarrage, vérifier l'heure du système ou consulter l'adresse MAC de votre machine. Une fois les vérifications matérielles terminées, l'objectif principal du processus **bios linux** est de localiser et de transférer le contrôle au chargeur de démarrage du système.

### Comment le BIOS Trouve le Chargeur de Démarrage

Une fois que le BIOS a initialisé le disque dur, il recherche un bloc de démarrage pour déterminer comment démarrer le système d'exploitation. L'emplacement qu'il vérifie dépend du schéma de partitionnement du disque : Master Boot Record (MBR) ou GUID Partition Table (GPT).

Le MBR est situé dans les 512 premiers octets du disque dur. Cette petite section contient le code de démarrage initial et la table de partition. Le code du MBR est responsable du chargement d'un autre programme, qui à son tour charge notre chargeur de démarrage réel. Si vous utilisez un disque partitionné GPT, le processus est légèrement différent.

### Comment Démarrer dans le BIOS

De nombreux utilisateurs ont besoin de savoir **comment démarrer dans le BIOS** pour configurer les paramètres matériels. La méthode pour y parvenir implique généralement d'appuyer sur une touche spécifique (telle que F2, F10, DEL ou ESC) immédiatement après avoir allumé l'ordinateur. Apprendre **comment démarrer dans le bios** est essentiel pour des tâches telles que la modification de la priorité du périphérique de démarrage ou l'activation de la technologie de virtualisation. La touche exacte varie selon le fabricant, vous devrez donc peut-être consulter la documentation de votre ordinateur.

### L'Avènement de l'UEFI

Une alternative au BIOS traditionnel est l'UEFI (Unified Extensible Firmware Interface). Conçu comme le successeur du BIOS, l'UEFI est désormais standard sur la plupart des matériels modernes. Il stocke toutes les informations de démarrage dans un fichier `.efi` situé sur une partition système EFI (ESP) dédiée. Cette partition contient le chargeur de démarrage pour le système d'exploitation installé.

L'UEFI offre de nombreuses améliorations par rapport au BIOS, notamment des temps de démarrage plus rapides et la prise en charge de disques durs plus volumineux. Bien que le format GPT ait été conçu pour l'UEFI, un "MBR protecteur" sur les disques GPT assure la rétrocompatibilité, rendant possible le démarrage à partir de ceux-ci sur d'anciennes machines basées sur le BIOS. Bien que de nombreux systèmes Linux utilisent désormais l'UEFI, ce guide se concentrera sur le processus de démarrage BIOS traditionnel pour une compréhension fondamentale.

## Exercise

La pratique rend parfait ! Voici quelques laboratoires pratiques pour renforcer votre compréhension de la gestion des utilisateurs et des groupes sous Linux :

1. **[Gérer les comptes utilisateurs Linux avec useradd, usermod et userdel](https://labex.io/fr/labs/comptia-manage-linux-user-accounts-with-useradd-usermod-and-userdel-590837)** - Entraînez-vous au cycle complet de l'administration des utilisateurs, de la création et de la sécurisation des nouveaux comptes à leur modification et suppression.
2. **[Gérer les groupes Linux avec groupadd, usermod et groupdel](https://labex.io/fr/labs/comptia-manage-linux-groups-with-groupadd-usermod-and-groupdel-590836)** - Acquérir une expérience pratique avec les utilitaires en ligne de commande pour l'administration des groupes, y compris la création de nouveaux groupes, la modification des appartenances des utilisateurs et la suppression de groupes.
3. **[Configurer les comptes utilisateurs et les privilèges Sudo sous Linux](https://labex.io/fr/labs/comptia-configure-user-accounts-and-sudo-privileges-in-linux-590856)** - Apprendre les techniques essentielles pour gérer les comptes utilisateurs et les privilèges sudo afin d'améliorer la sécurité d'un système Linux.

Ces laboratoires vous aideront à appliquer les concepts dans des scénarios réels et à gagner en confiance avec la gestion des utilisateurs et des groupes sous Linux.

## Quiz Question

Que charge le BIOS ? Veuillez répondre par un seul mot, en anglais et en minuscules.

## Quiz Answer

bootloader
