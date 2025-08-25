---
index: 4
lang: "fr"
title: "sysfs"
meta_title: "sysfs - Périphériques"
meta_description: "Découvrez sysfs, un système de fichiers virtuel pour des informations détaillées et la gestion des périphériques Linux. Comprenez /sys vs /dev. Commencez votre parcours Linux !"
meta_keywords: "sysfs, répertoire /sys, périphériques Linux, système de fichiers virtuel, tutoriel Linux, guide du débutant"
---

## Lesson Content

Sysfs a été créé il y a longtemps pour mieux gérer les périphériques sur notre système, une tâche que le répertoire `/dev` n'a pas réussi à accomplir de manière adéquate. Sysfs est un système de fichiers virtuel, le plus souvent monté sur le répertoire `/sys`. Il nous donne des informations plus détaillées que ce que nous pourrions voir dans le répertoire `/dev`. Les deux répertoires, `/sys` et `/dev`, semblent très similaires et le sont à certains égards, mais ils présentent des différences majeures. En gros, le répertoire `/dev` est simple ; il permet à d'autres programmes d'accéder aux périphériques eux-mêmes, tandis que le système de fichiers `/sys` est utilisé pour afficher des informations et gérer le périphérique.

Le système de fichiers `/sys` contient essentiellement toutes les informations pour tous les périphériques de votre système, telles que le fabricant et le modèle, l'endroit où le périphérique est branché, l'état du périphérique, la hiérarchie des périphériques, et bien plus encore. Les fichiers que vous voyez ici ne sont pas des nœuds de périphérique, vous n'interagissez donc pas vraiment avec les périphériques à partir du répertoire `/sys` ; vous gérez plutôt les périphériques.

Jetez un œil au contenu du répertoire `/sys` :

```bash
pete@icebox:~$ ls /sys/block/sda
alignment_offset  discard_alignment  holders   removable  sda6       trace
bdi               events             inflight  ro         size       uevent
capability        events_async       power     sda1       slaves
dev               events_poll_msecs  queue     sda2       stat
device            ext_range          range     sda5       subsystem
```

## Exercise

La pratique rend parfait ! Voici quelques laboratoires pratiques pour renforcer votre compréhension de l'exploration des périphériques matériels sous Linux :

1. **[Explorer les périphériques matériels sous Linux](https://labex.io/fr/labs/comptia-explore-hardware-devices-in-linux-590861)** - Entraînez-vous à identifier et à inspecter les périphériques matériels dans un environnement Linux, de la même manière que le système de fichiers `/sys` fournit des informations sur les périphériques.

Ce laboratoire vous aidera à appliquer les concepts de compréhension du matériel système et de sa représentation sous Linux, renforçant ainsi votre confiance dans l'exploration des périphériques.

## Quiz Question

Quel répertoire est utilisé pour afficher des informations détaillées sur les périphériques ?

## Quiz Answer

/sys
