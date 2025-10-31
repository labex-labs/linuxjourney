---
index: 4
lang: "fr"
title: "Tâches Upstart"
meta_title: "Tâches Upstart - Init"
meta_description: "Un guide pour gérer les services avec les tâches Upstart dans un environnement Linux. Apprenez à utiliser l'utilitaire initctl pour lister, démarrer, arrêter et redémarrer des tâches sur un système Linux Upstart."
meta_keywords: "Tâches Upstart, initctl, upstart linux, services Linux, administration système, système init, tutoriel Linux"
---

## Lesson Content

Upstart est un système d'initialisation basé sur les événements utilisé dans certaines distributions **upstart linux** pour gérer les services et les tâches pendant le démarrage et lorsque le système est en cours d'exécution. Il fonctionne via un système de jobs (tâches) et d'événements. Bien que retracer l'origine de chaque événement puisse être complexe, nécessitant souvent d'explorer les configurations des jobs dans `/etc/init`, vous aurez plus couramment besoin de gérer ces jobs directement depuis la ligne de commande. L'utilitaire `initctl` fournit une suite de commandes à cet effet.

### Visualiser l'état des Jobs

Pour voir une liste de tous les jobs Upstart connus et leurs états actuels, utilisez la commande `list`.

```plaintext
initctl list

shutdown stop/waiting
console stop/waiting
...
```

La sortie affiche le nom du job, son objectif (`goal`) et son statut actuel. Dans l'exemple `shutdown stop/waiting`, le nom du job est `shutdown`, son objectif est `stop` et son statut actuel est `waiting`. Le statut et les objectifs du job changeront lorsque vous interagirez avec eux.

Pour vérifier le statut d'un job spécifique, utilisez la commande `status`.

```plaintext
initctl status networking
networking start/running
```

### Contrôler Manuellement les Jobs

Bien que les fichiers de configuration des jobs dans `/etc/init` définissent comment les jobs démarrent, s'arrêtent et interagissent avec les événements, vous pouvez outrepasser manuellement ces actions en utilisant `initctl`. Ceci est utile pour le dépannage ou l'exécution de tâches administratives.

Pour démarrer manuellement un job :

```bash
sudo initctl start networking
```

Pour arrêter manuellement un job :

```bash
sudo initctl stop networking
```

Pour redémarrer manuellement un job, ce qui est un raccourci pratique pour l'arrêter puis le démarrer :

```bash
sudo initctl restart networking
```

### Émettre des Événements Personnalisés

Les jobs Upstart sont déclenchés par des événements. Vous pouvez également "émettre" manuellement un événement, ce qui peut être utile pour déclencher des jobs personnalisés ou à des fins de test. Tout job configuré pour démarrer sur `some_event` serait déclenché par la commande suivante.

```bash
sudo initctl emit some_event
```

## Exercise

La pratique rend parfait ! Bien qu'il n'y ait pas de laboratoires spécifiques pour Upstart, comprendre comment planifier et gérer les tâches est crucial pour contrôler les processus système. Voici un laboratoire pratique pour renforcer votre compréhension de la gestion des tâches :

1. **[Planifier des tâches avec at et cron sous Linux](https://labex.io/fr/labs/comptia-schedule-tasks-with-at-and-cron-in-linux-590870)** - Entraînez-vous à créer, gérer et supprimer des tâches uniques et récurrentes, qui sont des concepts fondamentaux liés à la manière dont les services et les tâches sont gérés dans les environnements Linux comme ceux gérés par Upstart.

Ce laboratoire vous aidera à appliquer les concepts d'automatisation des tâches dans des scénarios réels et à gagner en confiance dans la gestion des opérations système.

## Quiz Question

Comment redémarreriez-vous manuellement un job Upstart nommé `peanuts` ? Veuillez fournir la commande complète. (Note : La réponse est sensible à la casse et doit être en anglais.)

## Quiz Answer

sudo initctl restart peanuts
