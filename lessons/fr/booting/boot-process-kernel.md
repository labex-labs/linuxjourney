---
index: 4
lang: "fr"
title: "Processus de démarrage : Noyau"
meta_title: "Processus de démarrage : Noyau - Démarrer le système"
meta_description: "Découvrez le processus de démarrage de Linux, l'initialisation du noyau et le rôle de l'initramfs. Comprenez comment le noyau monte le système de fichiers racine. Guide du processus de démarrage de Linux."
meta_keywords: "processus de démarrage Linux, démarrage du noyau, initramfs, initrd, système de fichiers racine, tutoriel Linux, Linux débutant, guide Linux"
---

## Lesson Content

Maintenant que notre chargeur de démarrage a transmis les paramètres nécessaires, voyons comment il démarre :

### Initrd vs Initramfs

Il y a un peu un problème de la poule et de l'œuf lorsque nous parlons du démarrage du noyau. Le noyau gère le matériel de notre système ; cependant, tous les pilotes ne sont pas disponibles pour le noyau pendant le démarrage. Nous dépendons donc d'un système de fichiers racine temporaire qui contient uniquement les modules essentiels dont le noyau a besoin pour accéder au reste du matériel. Dans les anciennes versions de Linux, ce travail était confié à l'initrd (initial ramdisk). Le noyau montait l'initrd, obtenait les pilotes de démarrage nécessaires, puis, une fois qu'il avait fini de charger tout ce dont il avait besoin, il remplaçait l'initrd par le système de fichiers racine réel. De nos jours, nous avons ce qu'on appelle l'initramfs ; c'est un système de fichiers racine temporaire qui est intégré au noyau lui-même pour charger tous les pilotes nécessaires au véritable système de fichiers racine, il n'y a donc plus besoin de localiser le fichier initrd.

### Montage du système de fichiers racine

Maintenant, le noyau a tous les modules dont il a besoin pour créer un périphérique racine et monter la partition racine. Avant d'aller plus loin, la partition racine est d'abord montée en mode lecture seule afin que fsck puisse s'exécuter en toute sécurité et vérifier l'intégrité du système. Ensuite, il remonte le système de fichiers racine en mode lecture-écriture. Ensuite, le noyau localise le programme init et l'exécute.

## Exercise

La pratique rend parfait ! Voici un laboratoire pratique pour renforcer votre compréhension du processus de démarrage de Linux :

- **[Personnaliser le menu de démarrage GRUB2 sous Linux](https://labex.io/fr/labs/comptia-customize-the-grub2-boot-menu-in-linux-590859)** - Apprenez à modifier le menu de démarrage GRUB2, y compris la modification du délai d'attente et de l'entrée par défaut, et l'application de ces changements. Ce laboratoire vous aidera à comprendre comment le chargeur de démarrage peut être configuré.

Ce laboratoire vous aidera à appliquer les concepts dans un scénario réel et à renforcer votre confiance dans la configuration du démarrage de Linux.

## Quiz Question

Qu'est-ce qui est utilisé dans les systèmes modernes pour charger un système de fichiers racine temporaire ?

## Quiz Answer

initramfs
