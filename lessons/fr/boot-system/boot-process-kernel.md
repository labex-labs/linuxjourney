---
index: 4
lang: "fr"
title: "Processus de démarrage : Noyau"
meta_title: "Processus de démarrage : Noyau - Démarrer le système"
meta_description: "Explorez le processus de démarrage du noyau Linux. Apprenez comment initramfs charge les pilotes à partir d'un système de fichiers temporaire pour monter la partition racine de démarrage finale. Comprenez les étapes du chargement du noyau à l'exécution d'init."
meta_keywords: "racine de démarrage, initramfs, démarrage noyau, partition de démarrage, initramfs ubuntu, /etc/default/grub, processus de démarrage Linux, système de fichiers racine, initialisation du noyau"
---

## Lesson Content

Une fois que le chargeur de démarrage a chargé le noyau en mémoire et lui a transmis les paramètres nécessaires, le noyau prend le contrôle du système. Explorons ce qui se passe ensuite.

### Initialisation du Noyau et l'Initramfs

Un défi classique lors du démarrage est que le noyau a besoin de pilotes pour accéder aux périphériques matériels, mais ces pilotes résident souvent sur un périphérique de stockage auquel le noyau ne peut pas encore accéder. Pour résoudre ce problème, Linux utilise un système de fichiers racine temporaire.

Dans les systèmes plus anciens, cela était géré par un `initrd` (initial RAM disk). Le noyau chargeait cette image disque, trouvait les pilotes nécessaires, puis basculait vers le véritable système de fichiers racine. Les systèmes modernes, y compris les distributions comme Ubuntu, utilisent `initramfs` (initial RAM filesystem). Contrairement à `initrd`, `initramfs` est une archive `cpio` qui est décompressée dans un système de fichiers temporaire directement en mémoire. Cette approche est plus efficace car elle évite la surcharge liée à la création et au montage d'un périphérique bloc. L'`initramfs` contient uniquement les modules essentiels dont le noyau a besoin pour accéder à la partition de démarrage réelle (`boot partition`) et à d'autres matériels.

### Montage du Système de Fichiers Racine de Démarrage

Avec les pilotes chargés depuis l'`initramfs`, le noyau peut maintenant localiser et monter le système de fichiers racine de démarrage principal (`boot root`). L'emplacement de ce système de fichiers est généralement transmis comme paramètre par le chargeur de démarrage, ce qui peut être configuré dans des fichiers comme `/etc/default/grub`.

Premièrement, le noyau monte la partition racine de démarrage (`boot root`) en lecture seule. C'est une mesure de sécurité qui permet à l'utilitaire `fsck` (vérification du système de fichiers) de s'exécuter et de vérifier l'intégrité du système de fichiers sans risquer la corruption des données. Une fois la vérification terminée avec succès, le noyau remonte le système de fichiers en mode lecture-écriture.

Enfin, le système de fichiers racine étant entièrement disponible, le noyau démarre le tout premier programme de l'espace utilisateur : `init`. Ce programme est responsable de la mise en ligne du reste du système.

## Exercise

La pratique rend parfait ! Voici un laboratoire pratique pour renforcer votre compréhension du processus de démarrage Linux :

- **[Personnaliser le menu de démarrage GRUB2 sous Linux](https://labex.io/fr/labs/comptia-customize-the-grub2-boot-menu-in-linux-590859)** - Apprenez à modifier le menu de démarrage GRUB2, y compris la modification du délai d'attente et de l'entrée par défaut, et l'application de ces changements. Ce laboratoire vous aidera à comprendre comment le chargeur de démarrage peut être configuré.

Ce laboratoire vous aidera à appliquer les concepts dans un scénario réel et à gagner en confiance avec la configuration du démarrage Linux.

## Quiz Question

What is used in modern systems to load a temporary root filesystem? Please answer in English, using only lowercase letters.

## Quiz Answer

initramfs
