---
index: 3
lang: "fr"
title: "Processus de démarrage : Chargeur de démarrage"
meta_title: "Processus de démarrage : Chargeur de démarrage - Démarrer le système"
meta_description: "Découvrez le chargeur de démarrage Linux, ses fonctions et les paramètres de noyau courants comme initrd et root. Comprenez GRUB et optimisez votre processus de démarrage Linux."
meta_keywords: "chargeur de démarrage Linux, GRUB, paramètres du noyau, initrd, système de fichiers racine, processus de démarrage Linux, tutoriel Linux, Linux pour débutants"
---

## Lesson Content

Les principales responsabilités du chargeur de démarrage sont :

- Démarrer un système d'exploitation ; il peut également être utilisé pour démarrer des systèmes d'exploitation non-Linux.
- Sélectionner un noyau à utiliser.
- Spécifier les paramètres du noyau.

Le chargeur de démarrage le plus courant pour Linux est GRUB ; vous l'utilisez très probablement sur votre système. Il existe de nombreux autres chargeurs de démarrage que vous pouvez utiliser, tels que LILO, EFILINUX, Coreboot, SYSLINUX, et bien d'autres. Cependant, nous ne travaillerons qu'avec GRUB comme chargeur de démarrage.

Donc, nous savons que l'objectif principal du chargeur de démarrage est de charger le noyau, mais où le trouve-t-il ? Pour le trouver, nous devrons examiner nos paramètres de noyau. Les paramètres peuvent être trouvés en accédant au menu GRUB au démarrage en utilisant la touche 'e'. Si vous n'avez pas GRUB, pas de soucis, nous allons passer en revue les paramètres de démarrage que vous verrez :

- `initrd` - Spécifie l'emplacement du disque RAM initial (nous en parlerons plus en détail dans la prochaine leçon).
- `BOOT_IMAGE` - C'est là que se trouve l'image du noyau.
- `root` - L'emplacement du système de fichiers racine ; le noyau recherche à l'intérieur de cet emplacement pour trouver `init`. Il est souvent représenté par son UUID ou le nom du périphérique, tel que `/dev/sda1`.
- `ro` - Ce paramètre est assez standard ; il monte le système de fichiers en mode lecture seule.
- `quiet` - Ceci est ajouté afin que vous ne voyiez pas les messages d'affichage qui se déroulent en arrière-plan pendant le démarrage.
- `splash` - Cela permet d'afficher l'écran de démarrage.

## Exercise

La pratique rend parfait ! Voici un laboratoire pratique pour renforcer votre compréhension du chargeur de démarrage GRUB et de sa configuration :

1. **[Personnaliser le menu de démarrage GRUB2 sous Linux](https://labex.io/fr/labs/comptia-customize-the-grub2-boot-menu-in-linux-590859)** - Entraînez-vous à modifier le fichier de configuration principal de GRUB2 pour changer les paramètres du menu de démarrage et appliquer ces changements.

Ce laboratoire vous aidera à appliquer les concepts dans un scénario réel et à renforcer votre confiance dans la gestion du chargeur de démarrage.

## Quiz Question

Quel paramètre du noyau permet de ne pas voir les messages de démarrage ?

## Quiz Answer

quiet
