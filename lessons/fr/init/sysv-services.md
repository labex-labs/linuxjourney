---
index: 2
lang: "fr"
title: "Service System V"
meta_title: "Service System V - Init"
meta_description: "Apprenez à gérer les services traditionnels System V (SysV) sous Linux. Ce guide couvre l'utilisation de la commande `service` pour lister, démarrer, arrêter et redémarrer les services sur un système d'initialisation System V."
meta_keywords: "system v, init sysv, services linux, commande service, gérer services linux, démarrer service, arrêter service, redémarrer service, system v linux"
---

## Lesson Content

**System V** (ou SysV) est l'un des systèmes d'initialisation classiques des systèmes d'exploitation de type Unix. Bien que de nombreuses distributions Linux modernes soient passées à des systèmes plus récents comme `systemd`, comprendre comment gérer les services **System V** reste une compétence précieuse, car de nombreux systèmes maintiennent une rétrocompatibilité.

### La commande service

L'outil principal pour interagir avec les services sur un système d'initialisation **System V** est la commande `service`. Elle agit comme un script enveloppant, simplifiant le processus de contrôle des services.

### Lister tous les services

Pour obtenir un aperçu de tous les services disponibles et de leur état actuel, vous pouvez utiliser l'indicateur `--status-all`. Cette commande liste chaque service et indique s'il est en cours d'exécution (`+`), arrêté (`-`), ou si son état est inconnu (`?`).

```bash
service --status-all
```

### Contrôler un service spécifique

Pour gérer un service individuel, vous spécifiez le nom du service suivi d'une action telle que `start` (démarrer), `stop` (arrêter) ou `restart` (redémarrer). Ces actions nécessitent des privilèges administratifs, vous utiliserez donc généralement `sudo`.

Pour démarrer un service, tel que le service réseau :

```bash
sudo service networking start
```

Pour arrêter un service en cours d'exécution :

```bash
sudo service networking stop
```

Pour arrêter puis redémarrer immédiatement un service, ce qui est utile pour appliquer les modifications de configuration :

```bash
sudo service networking restart
```

Ces commandes ne sont pas exclusives aux systèmes d'initialisation **System V** ; vous pouvez souvent les utiliser pour gérer également les services Upstart. À mesure que les distributions Linux continuent d'évoluer, des couches de compatibilité comme la commande `service` sont maintenues pour faciliter la transition à partir des scripts d'initialisation traditionnels.

## Exercise

La pratique rend parfait ! Voici quelques laboratoires pratiques pour renforcer votre compréhension de la gestion des processus et des tâches, qui sont fondamentales pour la gestion des services sous Linux :

1. **[Gérer et surveiller les processus Linux](https://labex.io/fr/labs/comptia-manage-and-monitor-linux-processes-590864)** - Entraînez-vous à interagir, inspecter, surveiller et terminer des processus dans un environnement Linux réel.
2. **[Planifier des tâches avec at et cron sous Linux](https://labex.io/fr/labs/comptia-schedule-tasks-with-at-and-cron-in-linux-590870)** - Apprenez à automatiser des tâches à l'aide de `at` pour les travaux uniques et de `cron` pour les tâches récurrentes, une compétence clé pour l'automatisation des services.

Ces laboratoires vous aideront à appliquer les concepts dans des scénarios réels et à gagner en confiance dans la gestion des opérations système.

## Quiz Question

Quelle est la commande complète pour arrêter un service nommé `peanut` sur un système System V ? Veuillez fournir la commande exacte en anglais, en faisant attention à la casse.

## Quiz Answer

sudo service peanut stop
