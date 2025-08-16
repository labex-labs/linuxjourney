---
title: "Processus de démarrage : Chargeur de démarrage"
description: "Découvrez le chargeur de démarrage Linux, ses fonctions et les paramètres courants du noyau comme initrd et root. Comprenez GRUB et optimisez votre processus de démarrage Linux."
keywords: "chargeur de démarrage Linux, GRUB, paramètres du noyau, initrd, système de fichiers racine, processus de démarrage Linux, tutoriel Linux, Linux pour débutants"
---

## Lesson Content

Les principales responsabilités du chargeur de démarrage sont :

- Démarrer un système d'exploitation ; il peut également être utilisé pour démarrer des systèmes d'exploitation non-Linux.
- Sélectionner un noyau à utiliser.
- Spécifier les paramètres du noyau.

Le chargeur de démarrage le plus courant pour Linux est GRUB ; vous l'utilisez très probablement sur votre système. Il existe de nombreux autres chargeurs de démarrage que vous pouvez utiliser, tels que LILO, EFILINUX, Coreboot, SYSLINUX, et plus encore. Cependant, nous travaillerons uniquement avec GRUB comme chargeur de démarrage.

Donc, nous savons que l'objectif principal du chargeur de démarrage est de charger le noyau, mais où trouve-t-il le noyau ? Pour le trouver, nous devrons examiner nos paramètres de noyau. Les paramètres peuvent être trouvés en accédant au menu GRUB au démarrage en utilisant la touche 'e'. Si vous n'avez pas GRUB, pas de soucis, nous allons passer en revue les paramètres de démarrage que vous verrez :

- `initrd` - Spécifie l'emplacement du disque RAM initial (nous en parlerons plus en détail dans la prochaine leçon).
- `BOOT_IMAGE` - C'est là que se trouve l'image du noyau.
- `root` - L'emplacement du système de fichiers racine ; le noyau recherche à cet emplacement pour trouver `init`. Il est souvent représenté par son UUID ou le nom du périphérique, tel que `/dev/sda1`.
- `ro` - Ce paramètre est assez standard ; il monte le système de fichiers en mode lecture seule.
- `quiet` - Ceci est ajouté afin que vous ne voyiez pas les messages d'affichage qui se déroulent en arrière-plan pendant le démarrage.
- `splash` - Cela permet d'afficher l'écran de démarrage.

## Exercise

Si vous avez GRUB comme chargeur de démarrage, accédez au menu GRUB avec 'e' et examinez les paramètres.

## Quiz Question

Quel paramètre du noyau fait en sorte que vous ne voyez pas les messages de démarrage ?

## Quiz Answer

quiet
