---
index: 4
lang: "fr"
title: "Tâches Upstart"
meta_title: "Tâches Upstart - Init"
meta_description: "Apprenez à gérer les tâches Upstart sous Linux à l'aide des commandes initctl. Comprenez le statut des tâches, démarrez, arrêtez et redémarrez les services. Améliorez vos compétences en administration système Linux."
meta_keywords: "Tâches Upstart, initctl, services Linux, administration système, tutoriel Linux, guide du débutant"
---

## Lesson Content

Upstart peut déclencher de nombreux événements et tâches à exécuter. Malheureusement, il n'y a pas de moyen facile de voir d'où un événement ou une tâche est originaire, vous devrez donc fouiller dans les configurations de tâches dans `/etc/init`. La plupart du temps, vous n'aurez jamais besoin de consulter les fichiers de configuration des tâches Upstart, mais vous voudrez contrôler plus facilement certaines tâches spécifiques. Il existe de nombreuses commandes utiles que vous pouvez utiliser dans un système Upstart.

### Afficher les tâches

```plaintext
initctl list

shutdown stop/waiting
console stop/waiting
...
```

Vous verrez une liste de tâches Upstart avec différents statuts appliqués. Dans chaque ligne, le nom de la tâche est la première valeur, et le deuxième champ (avant le `/`) est en fait l'objectif de la tâche. La troisième valeur (après le `/`) est le statut actuel. Ainsi, nous voyons que notre tâche `shutdown` veut finalement s'arrêter, mais elle est actuellement en état d'attente. Le statut et les objectifs de la tâche changeront lorsque vous démarrerez ou arrêterez des tâches.

### Afficher une tâche spécifique

```plaintext
initctl status networking
networking start/running
```

Nous n'entrerons pas dans les détails de la façon d'écrire une configuration de tâche Upstart ; cependant, nous savons déjà que les tâches sont arrêtées, démarrées et redémarrées dans ces configurations. Ces tâches émettent également des événements, elles peuvent donc démarrer d'autres tâches. Nous allons passer en revue les commandes manuelles de l'opération Upstart, mais si vous êtes curieux, vous devriez approfondir les fichiers `.conf`.

### Démarrer manuellement une tâche

```bash
sudo initctl start networking
```

### Arrêter manuellement une tâche

```bash
sudo initctl stop networking
```

### Redémarrer manuellement une tâche

```bash
sudo initctl restart networking
```

### Émettre manuellement un événement

```bash
sudo initctl emit some_event
```

## Exercise

La pratique rend parfait ! Bien qu'il n'y ait pas de laboratoires spécifiques pour Upstart, comprendre comment planifier et gérer des tâches est crucial pour contrôler les processus système. Voici un laboratoire pratique pour renforcer votre compréhension de la gestion des tâches :

1. **[Planifier des tâches avec at et cron sous Linux](https://labex.io/fr/labs/comptia-schedule-tasks-with-at-and-cron-in-linux-590870)** - Entraînez-vous à créer, gérer et supprimer des tâches uniques et récurrentes, qui sont des concepts fondamentaux liés à la façon dont les services et les tâches sont gérés dans les environnements Linux comme ceux gérés par Upstart.

Ce laboratoire vous aidera à appliquer les concepts d'automatisation des tâches dans des scénarios réels et à renforcer votre confiance dans la gestion des opérations système.

## Quiz Question

Comment redémarrerais-je manuellement une tâche Upstart appelée `peanuts` ?

## Quiz Answer

sudo initctl restart peanuts
