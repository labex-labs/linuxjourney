---
title: "Processus de démarrage : Noyau"
description: "Découvrez le processus de démarrage de Linux, l'initialisation du noyau et le rôle d'initramfs. Comprenez comment le noyau monte le système de fichiers racine. Guide du processus de démarrage de Linux."
keywords: "processus de démarrage Linux, démarrage du noyau, initramfs, initrd, système de fichiers racine, tutoriel Linux, Linux pour débutants, guide Linux"
---

## Lesson Content

Maintenant que notre chargeur de démarrage a transmis les paramètres nécessaires, voyons comment il démarre :

### Initrd vs Initramfs

Il y a un peu un problème de poule et d'œuf quand on parle du démarrage du noyau. Le noyau gère le matériel de notre système ; cependant, tous les pilotes ne sont pas disponibles pour le noyau pendant le démarrage. Nous dépendons donc d'un système de fichiers racine temporaire qui contient uniquement les modules essentiels dont le noyau a besoin pour accéder au reste du matériel. Dans les anciennes versions de Linux, cette tâche était confiée à l'initrd (initial ramdisk). Le noyau montait l'initrd, obtenait les pilotes de démarrage nécessaires, puis, une fois qu'il avait fini de charger tout ce dont il avait besoin, il remplaçait l'initrd par le système de fichiers racine réel. De nos jours, nous avons ce qu'on appelle l'initramfs ; c'est un système de fichiers racine temporaire qui est intégré au noyau lui-même pour charger tous les pilotes nécessaires au véritable système de fichiers racine, il n'y a donc plus besoin de localiser le fichier initrd.

### Mounting the root filesystem

Maintenant, le noyau a tous les modules dont il a besoin pour créer un périphérique racine et monter la partition racine. Avant d'aller plus loin, la partition racine est d'abord montée en mode lecture seule afin que fsck puisse s'exécuter en toute sécurité et vérifier l'intégrité du système. Ensuite, il remonte le système de fichiers racine en mode lecture-écriture. Puis le noyau localise le programme init et l'exécute.

## Exercise

Pas d'exercices pour cette leçon.

## Quiz Question

Qu'est-ce qui est utilisé dans les systèmes modernes pour charger un système de fichiers racine temporaire ?

## Quiz Answer

initramfs
