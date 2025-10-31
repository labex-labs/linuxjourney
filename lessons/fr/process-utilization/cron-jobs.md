---
index: 8
lang: "fr"
title: "Tâches Cron"
meta_title: "Tâches Cron - Utilisation des Processus"
meta_description: "Apprenez à planifier des tâches et à automatiser des scripts sous Linux avec les tâches cron. Ce guide couvre la syntaxe crontab, les commandes essentielles comme crontab -e, et des exemples pratiques pour débutants."
meta_keywords: "tâches cron, crontab, planifier des tâches, automatisation Linux, commandes Linux, Linux débutant, tutoriel Linux, crontab -e, cron"
---

## Lesson Content

Bien que l'utilisation des processus soit importante, c'est aussi le moment idéal pour introduire un outil puissant pour l'`automatisation Linux` : le démon `cron`. Ce service d'arrière-plan vous permet de `planifier des tâches` pour qu'elles s'exécutent automatiquement à des heures ou des intervalles spécifiques. Ces tâches planifiées sont communément appelées `tâches cron`. Ceci est incroyablement utile pour automatiser des actions de routine, comme l'exécution d'un script de sauvegarde chaque nuit ou le nettoyage des fichiers temporaires une fois par semaine.

### Que sont les tâches Cron

Imaginez que vous ayez un script à `/home/pete/scripts/change_wallpaper` que vous exécutez chaque matin pour définir un nouveau fond d'écran. Au lieu de l'exécuter manuellement chaque jour, vous pouvez créer une `tâche cron` pour l'exécuter à votre place. En définissant une planification, vous pouvez indiquer au service `cron` exactement quand exécuter votre script, ce qui en fait une véritable solution "configurez et oubliez".

### Comprendre la syntaxe Crontab

Pour créer une `tâche cron`, vous devez spécifier la planification et la commande à exécuter. La planification est définie par cinq champs, suivis de la commande.

```plaintext
30 08 * * * /home/pete/scripts/change_wallpaper
```

Les cinq champs d'heure et de date sont, de gauche à droite :

- **Minute** : 0-59
- **Heure** : 0-23 (au format 24 heures)
- **Jour du mois** : 1-31
- **Mois** : 1-12
- **Jour de la semaine** : 0-7 (où 0 et 7 représentent tous deux le dimanche)

Un astérisque (`*`) dans un champ agit comme un joker, signifiant "chaque". Dans l'exemple ci-dessus, la planification `30 08 * * *` indique à `cron` d'exécuter la commande à 8h30, chaque jour du mois, chaque mois et chaque jour de la semaine.

### Gérer les tâches Cron avec Crontab

Vous gérez vos `tâches cron` personnelles à l'aide de la commande `crontab`, qui vous permet d'éditer votre fichier crontab spécifique à l'utilisateur. Ce fichier contient toutes les `tâches cron` que vous avez planifiées.

Pour ajouter ou modifier vos `tâches cron`, utilisez l'indicateur `-e` (éditer). Cela ouvrira votre fichier crontab dans votre éditeur de texte par défaut.

```bash
crontab -e
```

Une fois que vous avez ajouté la définition de votre tâche et enregistré le fichier, `cron` lira automatiquement la nouvelle planification. Vous pouvez également lister vos `tâches cron` actives avec `crontab -l` ou toutes les supprimer avec `crontab -r`. L'utilisation des `tâches cron` est une compétence fondamentale pour quiconque s'intéresse à l'`automatisation Linux`.

## Exercise

La pratique rend parfait ! Ce laboratoire pratique vous aidera à renforcer votre compréhension de la façon de `planifier des tâches` sous Linux.

1.  **[Planifier des tâches avec at et cron sous Linux](https://labex.io/fr/labs/comptia-schedule-tasks-with-at-and-cron-in-linux-590870)** - Entraînez-vous à créer, gérer et supprimer des tâches avec `at`, `atq`, `atrm` et `crontab`, en acquérant une expérience pratique dans l'automatisation des tâches d'administration système.

Ce laboratoire vous aidera à appliquer les concepts de cette leçon dans un scénario réel et à renforcer votre confiance dans l'`automatisation Linux`.

## Quiz Question

Quelle est la commande pour éditer vos tâches cron personnelles ? (Veuillez répondre en utilisant la commande exacte en minuscules et son option.)

## Quiz Answer

crontab -e
