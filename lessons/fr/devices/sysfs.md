---
index: 4
lang: "fr"
title: "sysfs"
meta_title: "sysfs - Périphériques"
meta_description: "Découvrez ce qu'est sysfs et son rôle dans le système sys de Linux. Ce guide explique le répertoire /sys de Linux, un système de fichiers virtuel pour les informations sur les périphériques, et le compare à /dev."
meta_keywords: "sysfs, qu'est-ce que sysfs, /sys, linux /sys, sys linux, système sys, système de fichiers virtuel, périphériques linux, /dev"
---

## Lesson Content

Le système de fichiers `sysfs` a été introduit pour fournir une meilleure façon de gérer les périphériques sur un système Linux, une tâche pour laquelle le répertoire `/dev` n'était pas entièrement équipé. Comprendre **qu'est-ce que /sys sous Linux** est essentiel pour l'administration système moderne.

### Qu'est-ce que sysfs ?

`sysfs` est un système de fichiers virtuel, généralement monté à `/sys`, qui exporte des informations sur les objets du noyau, les périphériques matériels et les pilotes depuis le modèle de périphériques du noyau vers l'espace utilisateur. Contrairement aux fichiers sur un disque physique, les fichiers et répertoires dans `/sys` sont générés à la volée et représentent l'état actuel du **système sys**.

### Le rôle du répertoire linux /sys

L'objectif principal du répertoire **linux /sys** est de fournir une vue structurée de tous les périphériques de votre système. Il contient des informations détaillées telles que le fabricant et le modèle, où le périphérique est branché, son état actuel et sa position dans la hiérarchie des périphériques.

Les fichiers que vous voyez ici ne sont pas des nœuds de périphériques comme ceux de `/dev`. Vous n'interagissez pas directement avec le périphérique lui-même via `/sys` ; vous l'utilisez plutôt pour visualiser des informations et gérer les attributs du périphérique.

### sysfs vs. /dev

Bien que `/sys` et `/dev` soient tous deux liés aux périphériques, ils servent des fonctions différentes.

- Le répertoire `/dev` fournit des nœuds de périphériques, qui sont des fichiers spéciaux permettant aux programmes d'accéder aux périphériques eux-mêmes.
- Le système de fichiers `/sys` est utilisé pour visualiser des informations sur les périphériques et les gérer. Il expose le modèle de périphérique sous-jacent.

Par exemple, inspectons le contenu d'un répertoire de périphérique bloc dans `/sys` :

```bash
pete@icebox:~$ ls /sys/block/sda
alignment_offset  discard_alignment  holders   removable  sda6       trace
bdi               events             inflight  ro         size       uevent
capability        events_async       power     sda1       slaves
dev               events_poll_msecs  queue     sda2       stat
device            ext_range          range     sda5       subsystem
```

Ce résultat montre divers attributs et sous-répertoires liés au disque dur `sda`, offrant une vue beaucoup plus détaillée que `/dev/sda` seul.

## Exercise

La pratique rend parfait ! Voici quelques laboratoires pratiques pour renforcer votre compréhension de l'exploration des périphériques matériels sous Linux :

1. **[Explorer les périphériques matériels sous Linux](https://labex.io/fr/labs/comptia-explore-hardware-devices-in-linux-590861)** - Entraînez-vous à identifier et à inspecter les périphériques matériels dans un environnement Linux, de manière similaire à la façon dont le système de fichiers `/sys` fournit des informations sur les périphériques.

Ce laboratoire vous aidera à appliquer les concepts de compréhension du matériel système et de sa représentation sous Linux, renforçant ainsi votre confiance dans l'exploration des périphériques.

## Quiz Question

Quel répertoire est utilisé pour visualiser des informations détaillées sur les périphériques ? Veuillez répondre en anglais.

## Quiz Answer

/sys
