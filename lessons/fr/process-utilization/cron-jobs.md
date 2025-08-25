---
index: 8
lang: "fr"
title: "Tâches Cron"
meta_title: "Tâches Cron - Utilisation des Processus"
meta_description: "Apprenez à planifier des tâches Linux avec les tâches cron. Comprenez la syntaxe crontab et automatisez les scripts pour les opérations quotidiennes. Démarrez avec ce guide convivial pour débutants !"
meta_keywords: "tâches cron, crontab, planifier des tâches, automatisation Linux, commandes Linux, Linux pour débutants, tutoriel Linux, crontab -e"
---

## Lesson Content

Bien que nous ayons parlé de l'utilisation des ressources, je pense que ce serait un bon moment pour mentionner un outil astucieux sous Linux qui est utilisé pour planifier des tâches à l'aide de cron. Il existe un service qui exécute des programmes pour vous à l'heure que vous spécifiez. C'est vraiment utile si vous avez un script que vous voulez exécuter une fois par jour et qui doit exécuter quelque chose pour vous.

Par exemple, disons que j'ai un script situé dans `/home/pete/scripts/change_wallpaper`. J'utilise ce script chaque matin pour changer l'image que j'utilise pour mon fond d'écran, mais chaque matin, je dois exécuter ce script manuellement. Au lieu de cela, ce que je peux faire est de créer une tâche cron qui exécute mon script via cron. Je peux spécifier l'heure à laquelle je veux que cette tâche cron s'exécute et exécute mon script.

```plaintext
30 08 * * * /home/pete/scripts/change_wallpaper
```

Les champs sont les suivants de gauche à droite :

- Minute - (0-59)
- Heure - (0-23)
- Jour du mois - (1-31)
- Mois - (1-12)
- Jour de la semaine - (0-7). 0 et 7 sont désignés comme dimanche

L'astérisque dans le champ signifie correspondre à chaque valeur. Donc, dans mon exemple ci-dessus, je veux que cela s'exécute tous les jours de chaque mois à 8h30 du matin.

Pour créer une tâche cron, il suffit de modifier le fichier crontab :

```bash
crontab -e
```

## Exercise

La pratique rend parfait ! Voici quelques laboratoires pratiques pour renforcer votre compréhension de la planification des tâches sous Linux :

1. **[Planifier des tâches avec at et cron sous Linux](https://labex.io/fr/labs/comptia-schedule-tasks-with-at-and-cron-in-linux-590870)** - Entraînez-vous à créer, gérer et supprimer des tâches avec `at`, `atq`, `atrm` et `crontab`, en acquérant une expérience pratique dans l'automatisation des tâches d'administration système.

Ce laboratoire vous aidera à appliquer les concepts dans des scénarios réels et à renforcer votre confiance dans la planification des tâches.

## Quiz Question

Quelle est la commande pour modifier vos tâches cron ?

## Quiz Answer

crontab -e
