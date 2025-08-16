---
lang: "fr"
title: "Processus de démarrage : Init"
description: "Découvrez les systèmes init de Linux : System V, Upstart et systemd. Comprenez leurs rôles dans le processus de démarrage et comment ils gèrent les services. Commencez votre parcours Linux !"
keywords: "Linux init, systemd, System V init, Upstart, processus de démarrage Linux, tutoriel Linux, Linux pour débutants, guide Linux"
---

## Lesson Content

Nous avons discuté d'init dans les leçons précédentes et savons que c'est le premier processus qui démarre, et qu'il lance tous les autres services essentiels sur notre système. Mais comment ?

Il existe en fait trois implémentations majeures d'init sous Linux :

### System V init (sysv)

C'est le système init traditionnel. Il démarre et arrête séquentiellement les processus basés sur des scripts de démarrage. L'état de la machine est désigné par des runlevels ; chaque runlevel démarre ou arrête une machine d'une manière différente.

### Upstart

C'est l'init que vous trouverez sur les anciennes installations Ubuntu. Upstart utilise l'idée de jobs et d'événements et fonctionne en démarrant des jobs qui effectuent certaines actions en réponse à des événements.

### Systemd

C'est le nouveau standard pour init ; il est orienté objectif. En gros, vous avez un objectif que vous voulez atteindre, et systemd essaie de satisfaire les dépendances de l'objectif pour le compléter.

Nous avons un cours entier sur les systèmes Init où nous approfondirons chacun de ces systèmes.

## Exercise

No exercises for this lesson.

## Quiz Question

Quel est le nouveau standard pour init ?

## Quiz Answer

systemd
