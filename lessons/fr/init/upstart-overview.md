---
index: 3
lang: "fr"
title: "Aperçu d'Upstart"
meta_title: "Aperçu d'Upstart - Init"
meta_description: "Apprenez l'architecture d'Upstart, son modèle piloté par les événements et la manière dont il gère les services sous Linux. Comprenez les configurations des tâches Upstart et son rôle en tant que système d'initialisation (init)."
meta_keywords: "Upstart, système d'init, services Linux, Ubuntu, SysV, tutoriel débutant, guide Linux"
---

## Lesson Content

Upstart a été développé par Canonical, c'était donc l'implémentation d'init sur Ubuntu pendant un certain temps ; cependant, sur les installations Ubuntu modernes, systemd est maintenant utilisé. Upstart a été créé pour améliorer les problèmes rencontrés avec SysV, tels que les processus de démarrage stricts, le blocage des tâches, etc. Le modèle piloté par les événements et les tâches d'Upstart lui permet de réagir aux événements au fur et à mesure qu'ils se produisent.

Pour savoir si vous utilisez Upstart, si vous possédez un répertoire `/usr/share/upstart`, c'est un très bon indicateur.

Les tâches (Jobs) sont les actions qu'Upstart exécute, et les événements (Events) sont des messages reçus d'autres processus pour déclencher des tâches. Pour voir une liste des tâches et leur configuration :

```plaintext
pete@icebox:~$ ls /etc/init
acpid.conf                   mountnfs.sh.conf
alsa-restore.conf            mtab.sh.conf
alsa-state.conf              networking.conf
alsa-store.conf              network-interface.conf
anacron.conf                 network-interface-container.conf
```

À l'intérieur de ces configurations de tâches, vous trouverez des informations sur comment et quand démarrer les tâches.

Par exemple, dans le fichier `networking.conf`, il pourrait être écrit quelque chose d'aussi simple que :

```plaintext
start on runlevel [235]
stop on runlevel [0]
```

Cela signifie qu'il commencera à configurer le réseau au niveau d'exécution (runlevel) 2, 3 ou 5 et arrêtera le réseau au niveau d'exécution 0. Il existe de nombreuses façons d'écrire le fichier de configuration, et vous le découvrirez en examinant les différentes configurations de tâches disponibles.

La manière dont Upstart fonctionne est la suivante :

1. D'abord, il charge les configurations des tâches depuis `/etc/init`.
2. Une fois qu'un événement de démarrage se produit, il exécute les tâches déclenchées par cet événement.
3. Ces tâches généreront de nouveaux événements, et ces événements déclencheront d'autres tâches.
4. Upstart continue de faire cela jusqu'à ce qu'il ait terminé toutes les tâches nécessaires.

## Exercise

La pratique rend parfait ! Bien qu'Upstart soit un système d'init plus ancien, comprendre comment les processus sont gérés et les tâches sont planifiées est crucial pour tout administrateur Linux. Voici quelques laboratoires pratiques pour renforcer votre compréhension de la gestion des processus et de l'automatisation des tâches, qui sont fondamentales pour le fonctionnement des systèmes d'init :

1. **[Gérer et surveiller les processus Linux](https://labex.io/fr/labs/comptia-manage-and-monitor-linux-processes-590864)** - Entraînez-vous à interagir avec les processus au premier plan et en arrière-plan, à les inspecter avec `ps`, à surveiller les ressources avec `top` et à les terminer avec `kill`. Ce laboratoire vous aide à comprendre le cycle de vie des processus, que les systèmes d'init comme Upstart gèrent.
2. **[Planifier des tâches avec at et cron sous Linux](https://labex.io/fr/labs/comptia-schedule-tasks-with-at-and-cron-in-linux-590870)** - Apprenez à planifier des tâches uniques avec `at` et des tâches récurrentes avec `cron`. Cela vous donne une expérience pratique de l'automatisation des tâches, une fonction principale que les systèmes d'init facilitent pour les services système.

Ces laboratoires vous aideront à appliquer les concepts de contrôle des processus et d'automatisation des tâches dans des scénarios réels, renforçant ainsi votre confiance dans la gestion d'un système Linux, quel que soit le système d'init spécifique utilisé.

## Quiz Question

Quel est l'implémentation d'init utilisée par Ubuntu ?

## Quiz Answer

systemd
