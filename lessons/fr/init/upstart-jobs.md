---
lang: "fr"
title: "Tâches Upstart"
description: "Apprenez à gérer les tâches Upstart sous Linux à l'aide des commandes initctl. Comprenez le statut des tâches, démarrez, arrêtez et redémarrez les services. Améliorez vos compétences en administration de systèmes Linux."
keywords: "Tâches Upstart, initctl, services Linux, administration système, tutoriel Linux, guide du débutant"
---

## Lesson Content

Upstart peut déclencher de nombreux événements et tâches à exécuter. Malheureusement, il n'y a pas de moyen facile de voir d'où un événement ou une tâche est originaire, vous devrez donc fouiller dans les configurations de tâches dans `/etc/init`. La plupart du temps, vous n'aurez jamais besoin de regarder les fichiers de configuration des tâches Upstart, mais vous voudrez contrôler plus facilement certaines tâches spécifiques. Il existe de nombreuses commandes utiles que vous pouvez utiliser dans un système Upstart.

### View jobs

```plaintext
initctl list

shutdown stop/waiting
console stop/waiting
...
```

Vous verrez une liste de tâches Upstart avec différents statuts appliqués. Dans chaque ligne, le nom de la tâche est la première valeur, et le deuxième champ (avant le `/`) est en fait l'objectif de la tâche. La troisième valeur (après le `/`) est le statut actuel. Ainsi, nous voyons que notre tâche `shutdown` veut finalement s'arrêter, mais elle est actuellement dans un état d'attente. Le statut et les objectifs de la tâche changeront lorsque vous démarrerez ou arrêterez des tâches.

### View specific job

```plaintext
initctl status networking
networking start/running
```

Nous n'entrerons pas dans les détails de la façon d'écrire une configuration de tâche Upstart ; cependant, nous savons déjà que les tâches sont arrêtées, démarrées et redémarrées dans ces configurations. Ces tâches émettent également des événements, elles peuvent donc démarrer d'autres tâches. Nous allons passer en revue les commandes manuelles de l'opération Upstart, mais si vous êtes curieux, vous devriez approfondir les fichiers `.conf`.

### Manually start a job

```bash
sudo initctl start networking
```

### Manually stop a job

```bash
sudo initctl stop networking
```

### Manually restart a job

```bash
sudo initctl restart networking
```

### Manually emit an event

```bash
sudo initctl emit some_event
```

## Exercise

Observez votre liste de tâches Upstart. Maintenant, changez l'état de la tâche avec l'une des commandes que nous avons apprises aujourd'hui. Qu'observez-vous ensuite ?

## Quiz Question

Comment redémarrerais-je manuellement une tâche Upstart appelée `peanuts` ?

## Quiz Answer

sudo initctl restart peanuts
