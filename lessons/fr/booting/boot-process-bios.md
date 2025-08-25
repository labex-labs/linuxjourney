---
index: 2
lang: "fr"
title: "Processus de démarrage : BIOS"
meta_title: "Processus de démarrage : BIOS - Démarrer le système"
meta_description: "Découvrez le processus de démarrage Linux, le BIOS et le MBR. Comprenez comment votre système démarre avec ce guide convivial pour débutants. Explorez les concepts UEFI !"
meta_keywords: "processus de démarrage Linux, BIOS, MBR, UEFI, tutoriel Linux, chargeur de démarrage, Linux débutant, démarrage système"
---

## Lesson Content

### BIOS

La première étape du processus de démarrage Linux est le BIOS, qui effectue des vérifications d'intégrité du système. Le BIOS est un micrologiciel très courant dans les ordinateurs compatibles IBM PC, le type d'ordinateurs dominant aujourd'hui. Vous avez probablement utilisé le micrologiciel BIOS pour modifier l'ordre de démarrage de vos disques durs, vérifier l'heure du système, l'adresse MAC de votre machine, etc. L'objectif principal du BIOS est de trouver le chargeur de démarrage du système.

Ainsi, une fois que le BIOS démarre le disque dur, il recherche le bloc de démarrage pour savoir comment démarrer le système. Selon la façon dont vous partitionnez votre disque, il se tournera vers le Master Boot Record (MBR) ou GPT. Le MBR est situé dans le premier secteur du disque dur, les 512 premiers octets. Le MBR contient le code pour charger un autre programme quelque part sur le disque ; ce programme charge ensuite notre chargeur de démarrage.

Maintenant, si vous avez partitionné votre disque avec GPT, l'emplacement du chargeur de démarrage change un peu.

### UEFI

Il existe une autre façon de démarrer votre système au lieu d'utiliser le BIOS, et c'est avec l'UEFI (qui signifie "Unified Extensible Firmware Interface"). L'UEFI a été conçu pour succéder au BIOS ; la plupart des matériels actuels sont livrés avec le micrologiciel UEFI intégré. Les machines Macintosh utilisent le démarrage EFI depuis des années, et Windows a majoritairement transféré tout son contenu vers le démarrage UEFI. Le format GPT était destiné à être utilisé avec EFI. Vous n'avez pas nécessairement besoin d'EFI si vous démarrez un disque GPT. Le premier secteur d'un disque GPT est réservé à un "MBR protecteur" pour permettre le démarrage d'une machine basée sur le BIOS.

L'UEFI stocke toutes les informations de démarrage dans un fichier `.efi`. Ce fichier est stocké sur une partition spéciale appelée partition système EFI sur le matériel. À l'intérieur de cette partition, il contiendra le chargeur de démarrage. L'UEFI apporte de nombreuses améliorations par rapport au micrologiciel BIOS traditionnel. Cependant, comme nous utilisons Linux, la majorité d'entre nous utilisons le BIOS. Toutes ces leçons suivront donc cette prémisse.

## Exercise

La pratique rend parfait ! Voici quelques laboratoires pratiques pour renforcer votre compréhension de la gestion des utilisateurs et des groupes Linux :

1. **[Gérer les comptes d'utilisateurs Linux avec useradd, usermod et userdel](https://labex.io/fr/labs/comptia-manage-linux-user-accounts-with-useradd-usermod-and-userdel-590837)** - Pratiquez le cycle de vie complet de l'administration des utilisateurs, de la création et la sécurisation de nouveaux comptes à leur modification et suppression.
2. **[Gérer les groupes Linux avec groupadd, usermod et groupdel](https://labex.io/fr/labs/comptia-manage-linux-groups-with-groupadd-usermod-and-groupdel-590836)** - Acquérez une expérience pratique avec les utilitaires en ligne de commande pour l'administration des groupes, y compris la création de nouveaux groupes, la modification des appartenances des utilisateurs et la suppression de groupes.
3. **[Configurer les comptes d'utilisateurs et les privilèges Sudo sous Linux](https://labex.io/fr/labs/comptia-configure-user-accounts-and-sudo-privileges-in-linux-590856)** - Apprenez les techniques essentielles pour gérer les comptes d'utilisateurs et les privilèges sudo afin d'améliorer la sécurité d'un système Linux.

Ces laboratoires vous aideront à appliquer les concepts dans des scénarios réels et à renforcer votre confiance dans la gestion des utilisateurs et des groupes sous Linux.

## Quiz Question

Que charge le BIOS ?

## Quiz Answer

bootloader
