---
index: 11
lang: "fr"
title: "Contrôle des Tâches"
meta_title: "Contrôle des Tâches - Processus"
meta_description: "Explorez notre tutoriel Linux sur le contrôle des tâches pour gérer efficacement les processus en arrière-plan. Apprenez à utiliser les commandes jobs, bg, fg et kill pour un multitâche shell puissant."
meta_keywords: "Contrôle des tâches Linux, processus en arrière-plan, commande jobs, commande bg, commande fg, commande kill, tutoriel Linux, Linux débutant"
---

## Lesson Content

Sous Linux, vous rencontrez souvent des commandes qui prennent beaucoup de temps à s'exécuter. Au lieu d'attendre et de laisser votre terminal inutilisable, vous pouvez utiliser le **contrôle des tâches Linux (job control)** pour gérer ces tâches. Cette fonctionnalité puissante vous permet d'exécuter et de gérer plusieurs **processus d'arrière-plan** au sein d'une seule session shell, améliorant ainsi considérablement votre flux de travail.

### Exécuter une commande en arrière-plan

Pour démarrer un processus directement en arrière-plan, ajoutez simplement une esperluette (`&`) à votre commande. Cela renvoie immédiatement votre invite shell, vous permettant de continuer à travailler pendant que la commande s'exécute.

```bash
sleep 1000 &
sleep 1001 &
sleep 1002 &
```

### Lister les tâches d'arrière-plan

Vous pouvez visualiser toutes les tâches s'exécutant en arrière-plan en utilisant la commande `jobs`.

```bash
$ jobs

[1]    Running     sleep 1000 &
[2]-   Running     sleep 1001 &
[3]+   Running     sleep 1002 &
```

Le résultat fournit l'ID de la tâche dans la première colonne, son statut et la commande d'origine. Le symbole `+` indique la tâche d'arrière-plan la plus récemment démarrée, tandis que le symbole `-` marque la deuxième plus récente.

### Gérer les processus actifs

Et si une commande est déjà en cours d'exécution au premier plan et que vous décidez d'avoir besoin de votre terminal ? Vous n'avez pas besoin de l'arrêter. D'abord, suspendez le processus en cours en appuyant sur `Ctrl-Z`. Ensuite, utilisez la commande `bg` pour envoyer cette tâche suspendue à l'arrière-plan.

```bash
pete@icebox ~ $ sleep 1003
^Z
[4]+    Stopped     sleep 1003

pete@icebox ~ $ bg
[4]+    sleep 1003 &
```

Maintenant, le processus `sleep 1003` s'exécute comme une tâche d'arrière-plan, et vous pouvez le vérifier avec la commande `jobs`.

### Ramener une tâche au premier plan

Pour ramener un processus d'arrière-plan au premier plan, utilisez la commande `fg`. Vous pouvez spécifier une tâche particulière par son ID (par exemple, `fg %1`). Si vous exécutez la commande `fg` sans aucun argument, elle ramènera la tâche d'arrière-plan la plus récente (celle marquée par `+`) au premier plan.

```bash
fg %1
```

### Terminer les tâches d'arrière-plan

Si vous avez besoin d'arrêter un processus d'arrière-plan, vous pouvez utiliser la commande `kill`. Semblable à la commande `fg`, vous référencez la tâche en utilisant son ID précédé d'un signe de pourcentage (`%`). C'est une fonction clé du contrôle des tâches Linux.

```bash
kill %1
```

Maîtriser ces commandes est essentiel pour tout utilisateur Linux débutant souhaitant effectuer plusieurs tâches efficacement dans le shell.

## Exercise

Pour mettre en pratique vos connaissances sur le contrôle des tâches Linux, essayez ce laboratoire pratique. Il vous aidera à consolider votre compréhension de la gestion des processus au premier plan et d'arrière-plan.

1. **[Gérer et surveiller les processus Linux](https://labex.io/fr/labs/comptia-manage-and-monitor-linux-processes-590864)** - Entraînez-vous à interagir avec les processus au premier plan et d'arrière-plan, à surveiller les ressources et à terminer les processus, répondant directement au scénario des commandes de longue durée.

## Quiz Question

What command is used to list background jobs? (Please answer in English, using only lowercase letters.)

## Quiz Answer

jobs
