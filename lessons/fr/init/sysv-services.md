---
index: 2
lang: "fr"
title: "Service System V"
meta_title: "Service System V - Init"
meta_description: "Apprenez à gérer les services System V à l'aide d'outils en ligne de commande. Découvrez comment lister, démarrer, arrêter et redémarrer des services avec ce tutoriel Linux pour débutants."
meta_keywords: "services System V, services Linux, commande service, SysV init, tutoriel Linux, Linux débutant, gestion des services, guide Linux"
---

## Lesson Content

Il existe de nombreux outils en ligne de commande que vous pouvez utiliser pour gérer les services Sys V.

### Lister les services

```bash
service --status-all
```

### Démarrer un service

```bash
sudo service networking start
```

### Arrêter un service

```bash
sudo service networking stop
```

### Redémarrer un service

```bash
sudo service networking restart
```

Ces commandes ne sont pas spécifiques aux systèmes d'initialisation Sys V ; vous pouvez également les utiliser pour gérer les services Upstart. Étant donné que Linux essaie de s'éloigner des scripts d'initialisation Sys V plus traditionnels, des mécanismes sont toujours en place pour faciliter cette transition.

## Exercise

C'est en forgeant qu'on devient forgeron ! Voici quelques laboratoires pratiques pour renforcer votre compréhension de la gestion des processus et des tâches, qui sont fondamentales pour la gestion des services sous Linux :

1. **[Gérer et surveiller les processus Linux](https://labex.io/fr/labs/comptia-manage-and-monitor-linux-processes-590864)** - Entraînez-vous à interagir avec, inspecter, surveiller et terminer des processus dans un environnement Linux réel.
2. **[Planifier des tâches avec at et cron sous Linux](https://labex.io/fr/labs/comptia-schedule-tasks-with-at-and-cron-in-linux-590870)** - Apprenez à automatiser des tâches en utilisant `at` pour les tâches uniques et `cron` pour les tâches récurrentes, une compétence clé pour l'automatisation des services.

Ces laboratoires vous aideront à appliquer les concepts dans des scénarios réels et à renforcer votre confiance dans la gestion des opérations système.

## Quiz Question

Quelle est la commande pour arrêter un service nommé `peanut` avec Sys V ?

## Quiz Answer

sudo service peanut stop
