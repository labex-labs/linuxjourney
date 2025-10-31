---
index: 5
lang: "fr"
title: "Emplacement du Noyau"
meta_title: "Emplacement du Noyau Linux - Noyau"
meta_description: "Découvrez où le noyau est stocké sous Linux. Ce guide explique l'emplacement du noyau Linux dans le répertoire /boot, détaillant les fichiers clés comme vmlinuz et initrd."
meta_keywords: "emplacement noyau linux, où est le noyau, localisation noyau, où se trouve le noyau, où est stocké le noyau linux, vmlinuz, répertoire /boot"
---

## Lesson Content

Lorsque vous installez un nouveau noyau, votre système ajoute plusieurs fichiers importants dans un répertoire spécifique. Si vous vous êtes déjà demandé **où le noyau est stocké sous Linux**, la réponse est généralement le répertoire `/boot`. Ce répertoire est l'**emplacement standard du noyau Linux** sur la plupart des systèmes.

### Le Répertoire /boot

Le répertoire `/boot` contient tous les fichiers nécessaires pour démarrer le processus de démarrage. Lorsque vous regardez à l'intérieur, vous verrez souvent des fichiers correspondant à différentes versions du noyau, vous permettant de démarrer sur un ancien noyau si un nouveau pose problème. Comprendre cet **emplacement du noyau** est crucial pour la maintenance du système.

### Fichiers Clés du Noyau

Alors, **où se situe le noyau** dans ce répertoire ? Il est accompagné de quelques autres fichiers critiques. Voici les principaux que vous rencontrerez :

- `vmlinuz`: C'est le noyau Linux exécutable et compressé. Le 'z' à la fin indique qu'il est compressé.
- `initrd`: C'est le disque RAM initial. Comme nous l'avons mentionné, l'`initrd` est un système de fichiers racine temporaire chargé en mémoire au démarrage pour monter le véritable système de fichiers racine.
- `System.map`: Ce fichier contient une table de symboles, qui mappe les noms de fonctions du noyau à leurs adresses mémoire. Il est principalement utilisé pour déboguer les paniques et les erreurs du noyau (oops).
- `config`: Ce fichier stocke les paramètres de configuration qui ont été utilisés pour compiler cette version spécifique du noyau. Il détaille quels pilotes et fonctionnalités ont été inclus.

### Gestion des Fichiers du Noyau

Avec le temps, votre répertoire `/boot` peut se remplir de fichiers provenant d'anciens noyaux. Si vous manquez d'espace, vous pouvez supprimer les fichiers des anciennes versions inutilisées. La manière la plus sûre de le faire est d'utiliser le gestionnaire de paquets de votre distribution (comme `apt` ou `dnf`). Supprimer manuellement des fichiers peut être risqué, soyez donc extrêmement prudent de ne pas supprimer les fichiers du noyau que vous utilisez actuellement.

## Exercise

Appliquez vos connaissances avec ce laboratoire pratique pour renforcer votre compréhension du processus de démarrage Linux et de la gestion du noyau :

1. **[Personnaliser le menu de démarrage GRUB2 sous Linux](https://labex.io/fr/labs/comptia-customize-the-grub2-boot-menu-in-linux-590859)** - Entraînez-vous à modifier la configuration GRUB2, ce qui a un impact direct sur la manière dont votre système Linux démarre et sélectionne les versions du noyau. Ce laboratoire vous aidera à comprendre les implications pratiques des fichiers discutés dans le répertoire `/boot`.

Ce laboratoire vous aidera à appliquer ces concepts dans un scénario réel et à gagner en confiance avec la gestion du noyau et du démarrage Linux.

## Quiz Question

Dans le répertoire `/boot`, quel est le nom typique du fichier image du noyau Linux compressé ? Veuillez répondre en anglais, en faisant attention à la sensibilité de la casse.

## Quiz Answer

vmlinuz
