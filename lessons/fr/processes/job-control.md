---
index: 11
lang: "fr"
title: "Contrôle des jobs"
meta_title: "Contrôle des jobs - Processus"
meta_description: "Apprenez le contrôle des jobs Linux pour gérer les processus en arrière-plan. Comprenez les commandes 'jobs', 'bg', 'fg' et 'kill' pour une utilisation efficace du shell. Commencez votre parcours Linux !"
meta_keywords: "contrôle des jobs Linux, processus en arrière-plan, commande jobs, commande bg, commande fg, commande kill, tutoriel Linux, Linux pour débutants"
---

## Lesson Content

Supposons que vous travailliez sur une seule fenêtre de terminal et que vous exécutiez une commande qui prend une éternité. Vous ne pouvez pas interagir avec le shell tant qu'elle n'est pas terminée. Cependant, nous voulons continuer à travailler sur nos machines, nous avons donc besoin que ce shell soit ouvert. Heureusement, nous pouvons contrôler la façon dont nos processus s'exécutent avec les jobs :

### Envoyer un job en arrière-plan

Ajouter une esperluette (`&`) à la commande l'exécutera en arrière-plan afin que vous puissiez toujours utiliser votre shell. Voyons un exemple :

```bash
sleep 1000 &
sleep 1001 &
sleep 1002 &
```

### Afficher tous les jobs en arrière-plan

Vous pouvez maintenant visualiser les jobs que vous venez d'envoyer en arrière-plan.

```bash
$ jobs

[1]    Running     sleep 1000 &
[2]-   Running     sleep 1001 &
[3]+   Running     sleep 1002 &
```

Ceci vous montrera l'ID du job dans la première colonne, puis le statut et la commande qui a été exécutée. Le **+** à côté de l'ID du job signifie qu'il s'agit du job en arrière-plan le plus récent qui a démarré. Le job avec le **-** est la deuxième commande la plus récente.

### Envoyer un job existant en arrière-plan

Si vous avez déjà exécuté un job et que vous souhaitez l'envoyer en arrière-plan, vous n'avez pas besoin de le terminer et de recommencer. D'abord, suspendez le job avec Ctrl-Z, puis exécutez la commande **bg** pour l'envoyer en arrière-plan.

```bash
pete@icebox ~ $ sleep 1003
^Z
[4]+    Stopped     sleep 1003

pete@icebox ~ $ bg
[4]+    sleep 1003 &

pete@icebox ~ $ jobs

[1]    Running     sleep 1000 &
[2]    Running     sleep 1001 &
[3]-   Running     sleep 1002 &
[4]+   Running     sleep 1003 &
```

### Déplacer un job de l'arrière-plan vers le premier plan

Pour sortir un job de l'arrière-plan, spécifiez simplement l'ID du job que vous souhaitez. Si vous exécutez `fg` sans aucune option, il ramènera le job en arrière-plan le plus récent (le job avec le signe + à côté).

```bash
fg %1
```

### Tuer les jobs en arrière-plan

De manière similaire au déplacement des jobs hors de l'arrière-plan, vous pouvez utiliser la même forme pour tuer les processus en utilisant leur ID de job.

```bash
kill %1
```

## Exercise

La pratique rend parfait ! Voici quelques laboratoires pratiques pour renforcer votre compréhension de la gestion des processus sous Linux :

1. **[Gérer et surveiller les processus Linux](https://labex.io/fr/labs/comptia-manage-and-monitor-linux-processes-590864)** - Entraînez-vous à interagir avec les processus de premier plan et d'arrière-plan, à surveiller les ressources et à terminer les processus, en abordant directement le scénario des commandes de longue durée.

Ce laboratoire vous aidera à appliquer les concepts dans des scénarios réels et à renforcer votre confiance en la gestion des processus.

## Quiz Question

Quelle commande est utilisée pour lister les jobs en arrière-plan ?

## Quiz Answer

jobs
