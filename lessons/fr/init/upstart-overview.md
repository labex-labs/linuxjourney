---
index: 3
lang: "fr"
title: "Présentation d'Upstart"
meta_title: "Présentation d'Upstart - Init"
meta_description: "Découvrez Upstart, son modèle événementiel et comment il gère les services sous Linux. Comprenez les configurations de tâches Upstart et son rôle en tant que système init."
meta_keywords: "Upstart, système init, services Linux, Ubuntu, SysV, tutoriel débutant, guide Linux"
---

## Lesson Content

Upstart a été développé par Canonical, il a donc été l'implémentation init sur Ubuntu pendant un certain temps ; cependant, sur les installations Ubuntu modernes, systemd est maintenant utilisé. Upstart a été créé pour améliorer les problèmes de SysV, tels que les processus de démarrage stricts, le blocage des tâches, etc. Le modèle événementiel et basé sur les tâches d'Upstart lui permet de répondre aux événements au fur et à mesure qu'ils se produisent.

Pour savoir si vous utilisez Upstart, si vous avez un répertoire `/usr/share/upstart`, c'est un assez bon indicateur.

Les tâches (jobs) sont les actions qu'Upstart exécute, et les événements sont des messages reçus d'autres processus pour déclencher des tâches. Pour voir une liste des tâches et de leur configuration :

```plaintext
pete@icebox:~$ ls /etc/init
acpid.conf                   mountnfs.sh.conf
alsa-restore.conf            mtab.sh.conf
alsa-state.conf              networking.conf
alsa-store.conf              network-interface.conf
anacron.conf                 network-interface-container.conf
```

À l'intérieur de ces configurations de tâches, vous trouverez des informations sur la manière et le moment de démarrer les tâches.

Par exemple, dans le fichier `networking.conf`, il pourrait y avoir quelque chose d'aussi simple que :

```plaintext
start on runlevel [235]
stop on runlevel [0]
```

Cela signifie qu'il commencera à configurer le réseau aux niveaux d'exécution 2, 3 ou 5 et arrêtera le réseau au niveau d'exécution 0. Il existe de nombreuses façons d'écrire le fichier de configuration, et vous le découvrirez en examinant les différentes configurations de tâches disponibles.

Le fonctionnement d'Upstart est le suivant :

1. Tout d'abord, il charge les configurations de tâches depuis `/etc/init`.
2. Une fois qu'un événement de démarrage se produit, il exécute les tâches déclenchées par cet événement.
3. Ces tâches généreront de nouveaux événements, et ces événements déclencheront d'autres tâches.
4. Upstart continue de faire cela jusqu'à ce qu'il ait terminé toutes les tâches nécessaires.

## Exercise

La pratique rend parfait ! Bien qu'Upstart soit un système init plus ancien, comprendre comment les processus sont gérés et les tâches sont planifiées est crucial pour tout administrateur Linux. Voici quelques laboratoires pratiques pour renforcer votre compréhension de la gestion des processus et de l'automatisation des tâches, qui sont fondamentales pour le fonctionnement des systèmes init :

1. **[Gérer et surveiller les processus Linux](https://labex.io/fr/labs/comptia-manage-and-monitor-linux-processes-590864)** - Entraînez-vous à interagir avec les processus de premier plan et d'arrière-plan, à les inspecter avec `ps`, à surveiller les ressources avec `top` et à les terminer avec `kill`. Ce laboratoire vous aide à comprendre le cycle de vie des processus, que les systèmes init comme Upstart gèrent.
2. **[Planifier des tâches avec at et cron sous Linux](https://labex.io/fr/labs/comptia-schedule-tasks-with-at-and-cron-in-linux-590870)** - Apprenez à planifier des tâches uniques avec `at` et des tâches récurrentes avec `cron`. Cela fournit une expérience pratique de l'automatisation des tâches, une fonction essentielle que les systèmes init facilitent pour les services système.

Ces laboratoires vous aideront à appliquer les concepts de contrôle des processus et d'automatisation des tâches dans des scénarios réels, renforçant ainsi votre confiance dans la gestion d'un système Linux, quel que soit le système init spécifique utilisé.

## Quiz Question

Quelle est l'implémentation init utilisée par Ubuntu ?

## Quiz Answer

upstart
