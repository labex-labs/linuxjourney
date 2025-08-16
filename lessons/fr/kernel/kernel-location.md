---
title: "Emplacement du noyau"
description: "Découvrez l'emplacement du noyau Linux dans le répertoire /boot, en comprenant vmlinuz, initrd et System.map. Explorez les fichiers du noyau et gérez l'espace efficacement."
keywords: "noyau Linux, répertoire /boot, vmlinuz, initrd, System.map, débutant Linux, tutoriel noyau, guide Linux"
---

## Lesson Content

Que se passe-t-il lorsque vous installez un nouveau noyau ? Eh bien, cela ajoute en fait quelques fichiers à votre système ; ces fichiers sont généralement ajoutés au répertoire `/boot`.

Vous verrez plusieurs fichiers pour différentes versions du noyau :

- `vmlinuz` - c'est le noyau Linux réel
- `initrd` - comme nous l'avons déjà mentionné, l'`initrd` est utilisé comme un système de fichiers temporaire, utilisé avant le chargement du noyau
- `System.map` - table de correspondance symbolique
- `config` - paramètres de configuration du noyau ; si vous compilez votre propre noyau, vous pouvez définir quels modules peuvent être chargés

Si votre répertoire `/boot` manque d'espace, vous pouvez toujours supprimer les anciennes versions de ces fichiers ou simplement utiliser un gestionnaire de paquets. Mais soyez prudent lors de la maintenance dans ce répertoire, et ne supprimez pas accidentellement le noyau que vous utilisez actuellement.

## Exercise

Go into your boot directory and see what files are in there.

## Quiz Question

Comment s'appelle l'image du noyau dans `/boot` ?

## Quiz Answer

vmlinuz
