---
index: 5
lang: "fr"
title: "Emplacement du noyau"
meta_title: "Emplacement du noyau - Noyau"
meta_description: "Découvrez l'emplacement du noyau Linux dans le répertoire /boot, en comprenant vmlinuz, initrd et System.map. Explorez les fichiers du noyau et gérez l'espace efficacement."
meta_keywords: "noyau Linux, répertoire /boot, vmlinuz, initrd, System.map, débutant Linux, tutoriel noyau, guide Linux"
---

## Lesson Content

Que se passe-t-il lorsque vous installez un nouveau noyau ? Eh bien, cela ajoute en fait quelques fichiers à votre système ; ces fichiers sont généralement ajoutés au répertoire `/boot`.

Vous verrez plusieurs fichiers pour différentes versions du noyau :

- `vmlinuz` - c'est le noyau Linux réel
- `initrd` - comme nous l'avons déjà mentionné, l'`initrd` est utilisé comme système de fichiers temporaire, utilisé avant le chargement du noyau
- `System.map` - table de recherche symbolique
- `config` - paramètres de configuration du noyau ; si vous compilez votre propre noyau, vous pouvez définir les modules qui peuvent être chargés

Si votre répertoire `/boot` manque d'espace, vous pouvez toujours supprimer les anciennes versions de ces fichiers ou simplement utiliser un gestionnaire de paquets. Mais soyez prudent lors de la maintenance dans ce répertoire, et ne supprimez pas accidentellement le noyau que vous utilisez actuellement.

## Exercise

La pratique rend parfait ! Voici quelques laboratoires pratiques pour renforcer votre compréhension du processus de démarrage Linux et de la gestion du noyau :

1. **[Personnaliser le menu de démarrage GRUB2 sous Linux](https://labex.io/fr/labs/comptia-customize-the-grub2-boot-menu-in-linux-590859)** - Entraînez-vous à modifier la configuration de GRUB2, ce qui a un impact direct sur la façon dont votre système Linux démarre et sélectionne les versions du noyau. Ce laboratoire vous aidera à comprendre les implications pratiques des fichiers discutés dans le répertoire `/boot`.

Ce laboratoire vous aidera à appliquer les concepts dans des scénarios réels et à renforcer votre confiance dans la gestion du noyau et du démarrage Linux.

## Quiz Question

Comment s'appelle l'image du noyau dans `/boot` ?

## Quiz Answer

vmlinuz
