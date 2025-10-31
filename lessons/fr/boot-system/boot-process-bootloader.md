---
index: 3
lang: "fr"
title: "Processus de Démarrage : Chargeur d'Amorçage"
meta_title: "Processus de Démarrage : Chargeur d'Amorçage - Démarrer le Système"
meta_description: "Guide sur le chargeur d'amorçage (bootloader) sous Linux. Découvrez ce qu'est un chargeur d'amorçage Linux, ses fonctions principales et comment GRUB utilise des paramètres noyau comme initrd et root pour démarrer le système."
meta_keywords: "chargeur d'amorçage linux, bootloader linux, chargeur d'amorçage linux, grub, qu'est-ce qu'un bootloader linux, paramètres noyau, initrd, système de fichiers root, processus de démarrage linux"
---

## Lesson Content

### Qu'est-ce qu'un chargeur de démarrage (Bootloader) sous Linux

Une fois que le BIOS/UEFI a terminé ses tâches, il transfère le contrôle à l'étape suivante du processus de démarrage : le chargeur de démarrage. Un **chargeur de démarrage sous Linux** est un petit programme qui charge le noyau du système d'exploitation en mémoire, puis l'exécute. Il sert de pont entre le micrologiciel (firmware) du système et le noyau Linux.

### Le rôle du chargeur de démarrage Linux

Les responsabilités principales d'un **chargeur de démarrage Linux** sont simples mais cruciales :

- **Sélection du système d'exploitation** : Il peut présenter un menu pour démarrer différents systèmes d'exploitation, y compris des systèmes non-Linux, si vous avez une configuration multi-amorçage.
- **Sélection du noyau** : Il vous permet de choisir quelle version du noyau Linux charger, ce qui est utile pour le dépannage ou les tests.
- **Transmission des paramètres du noyau** : Il spécifie les paramètres essentiels dont le noyau a besoin pour démarrer correctement.

Le **chargeur de démarrage Linux** le plus courant est GRUB (GRand Unified Bootloader), que vous utilisez très probablement. Bien qu'il existe d'autres chargeurs de démarrage comme LILO, SYSLINUX et Coreboot, cette leçon se concentrera sur GRUB.

### Paramètres courants du noyau dans GRUB

L'objectif principal du chargeur de démarrage est de charger le noyau, mais il a besoin d'instructions sur comment et où le trouver. Ces instructions sont fournies sous forme de paramètres du noyau. Vous pouvez généralement visualiser ou modifier ces paramètres en appuyant sur la touche 'e' dans le menu **GRUB** lors du démarrage.

Voici quelques-uns des paramètres les plus courants que vous rencontrerez :

- `initrd` - Spécifie l'emplacement du disque RAM initial (initial RAM disk), un système de fichiers racine temporaire chargé en mémoire. Nous aborderons cela plus en détail dans la leçon suivante.
- `BOOT_IMAGE` - Définit le chemin d'accès au fichier image du noyau qui doit être chargé.
- `root` - Indique l'emplacement du système de fichiers racine réel. Le noyau utilise ce chemin pour trouver le processus `init`. Ceci est souvent représenté par un nom de périphérique (par exemple, `/dev/sda1`) ou un UUID.
- `ro` - Un paramètre standard qui demande au noyau de monter le système de fichiers racine en lecture seule initialement. C'est une mesure de sécurité pour permettre l'exécution de vérifications du système de fichiers avant que toute modification ne soit effectuée.
- `quiet` - Ce paramètre supprime la plupart des messages de démarrage détaillés, offrant un écran de démarrage plus propre et moins verbeux.
- `splash` - Active l'affichage d'un écran de démarrage graphique au lieu de messages texte pendant le processus de démarrage.

## Exercise

La pratique rend parfait ! Voici un laboratoire pratique pour renforcer votre compréhension du chargeur de démarrage GRUB2 et de sa configuration :

1. **[Personnaliser le menu de démarrage GRUB2 sous Linux](https://labex.io/fr/labs/comptia-customize-the-grub2-boot-menu-in-linux-590859)** - Entraînez-vous à modifier le fichier de configuration principal de GRUB2 pour changer les paramètres du menu de démarrage et appliquer ces changements.

Ce laboratoire vous aidera à appliquer les concepts dans un scénario réel et à gagner en confiance dans la gestion des chargeurs de démarrage.

## Quiz Question

Quel paramètre du noyau fait en sorte que vous ne voyiez pas les messages de démarrage ? Veuillez répondre avec le paramètre unique en anglais minuscule.

## Quiz Answer

quiet
