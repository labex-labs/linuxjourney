---
lang: "fr"
title: "Présentation d'Upstart"
meta_description: "Découvrez Upstart, son modèle événementiel et comment il gère les services sous Linux. Comprenez les configurations de job Upstart et son rôle en tant que système init."
meta_keywords: "Upstart, système init, services Linux, Ubuntu, SysV, tutoriel débutant, guide Linux"
---

## Lesson Content

Upstart a été développé par Canonical, il a donc été l'implémentation init sur Ubuntu pendant un certain temps ; cependant, sur les installations Ubuntu modernes, systemd est maintenant utilisé. Upstart a été créé pour améliorer les problèmes de SysV, tels que les processus de démarrage stricts, le blocage des tâches, etc. Le modèle événementiel et basé sur les tâches d'Upstart lui permet de répondre aux événements au fur et à mesure qu'ils se produisent.

Pour savoir si vous utilisez Upstart, si vous avez un répertoire `/usr/share/upstart`, c'est un assez bon indicateur.

Les jobs sont les actions qu'Upstart exécute, et les events sont des messages reçus d'autres processus pour déclencher des jobs. Pour voir une liste des jobs et de leur configuration :

```plaintext
pete@icebox:~$ ls /etc/init
acpid.conf                   mountnfs.sh.conf
alsa-restore.conf            mtab.sh.conf
alsa-state.conf              networking.conf
alsa-store.conf              network-interface.conf
anacron.conf                 network-interface-container.conf
```

À l'intérieur de ces configurations de job, vous trouverez des informations sur comment et quand démarrer les jobs.

Par exemple, dans le fichier `networking.conf`, il pourrait y avoir quelque chose d'aussi simple que :

```plaintext
start on runlevel [235]
stop on runlevel [0]
```

Cela signifie qu'il commencera à configurer le réseau aux runlevels 2, 3 ou 5 et arrêtera le réseau au runlevel 0. Il existe de nombreuses façons d'écrire le fichier de configuration, et vous le découvrirez en examinant les différentes configurations de job disponibles.

Le fonctionnement d'Upstart est le suivant :

1. Tout d'abord, il charge les configurations de job depuis `/etc/init`.
2. Une fois qu'un événement de démarrage se produit, il exécute les jobs déclenchés par cet événement.
3. Ces jobs créeront de nouveaux événements, et ces événements déclencheront ensuite d'autres jobs.
4. Upstart continue de faire cela jusqu'à ce qu'il ait terminé tous les jobs nécessaires.

## Exercise

Si vous utilisez Upstart, essayez de comprendre les configurations de job dans `/etc/init`.

## Quiz Question

Quelle est l'implémentation init utilisée par Ubuntu ?

## Quiz Answer

upstart
