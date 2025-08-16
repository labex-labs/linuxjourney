---
title: "Aperçu du processus de démarrage"
description: "Apprenez les étapes du processus de démarrage de Linux : BIOS, bootloader, kernel et init. Comprenez comment Linux démarre de la mise sous tension à la connexion. Guide essentiel pour les débutants Linux."
keywords: "processus de démarrage Linux, BIOS, bootloader, kernel, init, tutoriel Linux, guide Linux, débutant"
---

## Lesson Content

Maintenant que nous avons une assez bonne compréhension de certains des composants importants de Linux, assemblons-les en apprenant comment le système démarre. Lorsque vous allumez votre machine, elle fait des choses astucieuses comme afficher l'écran du logo, parcourir différents messages, puis à la fin, vous êtes invité à une fenêtre de connexion. En fait, il se passe une tonne de choses entre le moment où vous appuyez sur le bouton d'alimentation et le moment où vous vous connectez, et nous en discuterons dans ce cours.

Le processus de démarrage de Linux peut être décomposé en 4 étapes simples :

### 1. BIOS

Le BIOS (pour "Basic Input/Output System") initialise le matériel et s'assure, via un Power-on Self-Test (POST), que tout le matériel est prêt à fonctionner. Le rôle principal du BIOS est de charger le bootloader.

### 2. Bootloader

Le bootloader charge le kernel en mémoire, puis démarre le kernel avec un ensemble de kernel parameters. L'un des bootloaders les plus courants est GRUB, qui est un standard universel de Linux.

### 3. Kernel

Lorsque le kernel est chargé, il initialise immédiatement les devices et la mémoire. Le rôle principal du kernel est de charger le processus init.

### 4. Init

N'oubliez pas, le processus init est le premier processus qui démarre. Init démarre et arrête les processus de service essentiels sur le système. Il existe trois implémentations majeures d'init dans les distributions Linux. Nous les aborderons brièvement, puis nous les approfondirons dans un autre cours.

Voilà, l'explication (très) simple du processus de démarrage de Linux. Nous entrerons plus en détail sur ces étapes dans les prochaines leçons.

## Exercise

Redémarrez votre système et voyez si vous pouvez repérer chaque étape au fur et à mesure que votre machine démarre.

## Quiz Question

Quelle est la dernière étape du processus de démarrage de Linux ?

## Quiz Answer

init
