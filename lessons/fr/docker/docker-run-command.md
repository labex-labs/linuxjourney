---
lesson_id: "docker-run-command"
course_id: "docker"
lang: "fr"
order_index: 3
title: "docker run"
description: "Apprenez à créer et à démarrer un conteneur à partir d’une image avec docker run."
meta_title: "docker run - Docker"
meta_description: "Lisez une commande docker run, choisissez un nom de conteneur et distinguez une tâche de premier plan d’un serveur en arrière-plan."
meta_keywords: "docker run, lancer un conteneur Docker, noms de conteneurs, premier plan, arrière-plan"
---

Vous avez une image de serveur web. Pour le démarrer, lancez `docker run`, qui crée et démarre un conteneur à partir de l’image. Commencez par une commande courte pour voir à quel moment le terminal vous rend la main.

## Exécuter une tâche courte

BusyBox est une petite image qui contient des commandes Linux de base. Dans l’exemple, `echo` affiche un message. Placez la référence d’image avant la commande à exécuter dans le conteneur. Docker télécharge normalement l’image si elle est absente. Le `$` marque l’invite du terminal. Si Docker doit d’abord télécharger l’image, il peut afficher des messages de téléchargement avant la ligne indiquée.

```text
$ docker run busybox:1.36 echo Hello
Hello
```

Le résultat s’affiche dans le terminal. Quand `echo` a terminé, le conteneur s’arrête et l’invite revient.

:::single-choice{#docker-run-command-short-task} Qu’est-ce qui s’exécute dans le conteneur dans cet exemple ?

::option[`busybox:1.36` en tant que commande shell.]{#docker-run-command-short-image explanation="BusyBox est l’image qui fournit les outils. La commande vient après la référence de l’image."}
::option[`echo Hello` avec les outils fournis par l’image.]{#docker-run-command-short-echo .correct explanation="Après la référence de l’image, on indique la commande echo et le texte qu’elle doit afficher."}
::option[`docker run` en tant que deuxième commande Docker.]{#docker-run-command-short-docker explanation="Vous lancez docker run dans votre terminal. C’est lui qui démarre la commande dans le conteneur."}
:::

## Nommer le conteneur

Placez `--name` avant la référence de l’image pour donner au conteneur un nom facile à reconnaître. Cette commande appelle `report` le conteneur de la tâche courte.

```bash
$ docker run --name report busybox:1.36 echo Ready
```

Un conteneur conserve son nom même après son arrêt. Dans un même environnement Docker, choisissez un nom disponible avant de créer un autre conteneur.

:::single-choice{#docker-run-command-name-choice} Report a terminé, mais le conteneur existe toujours. Que pouvez-vous changer pour créer un deuxième conteneur à partir de la même image ?

::option[Choisir un autre nom de conteneur et garder la référence de l’image.]{#docker-run-command-name-new .correct explanation="Avec un nom disponible, Docker peut créer un conteneur distinct à partir de la même image."}
::option[Changer le tag de l’image et garder le nom du conteneur.]{#docker-run-command-name-change-tag explanation="Le premier conteneur conserve son nom même si vous choisissez une autre image."}
::option[Changer le message et garder le nom du conteneur.]{#docker-run-command-name-change-message explanation="Le message est une entrée pour echo. Le modifier ne libère pas le nom report."}
:::

## Démarrer un serveur en arrière-plan

Une image peut définir une commande par défaut. Avec `nginx:alpine`, un serveur web démarre si vous n’indiquez pas de commande après la référence. Ajoutez `-d` pour lancer le conteneur **en arrière-plan** et retrouver votre invite pendant que le serveur tourne.

```bash
$ docker run -d --name web nginx:alpine
```

Docker affiche un identifiant de conteneur, une longue chaîne qui désigne le conteneur lancé. Vous vérifierez dans la prochaine leçon si le serveur est toujours en cours d’exécution.

![Terminal LabEx affichant Hello et Ready pour des tâches courtes et l’identifiant d’un conteneur lancé en arrière-plan](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/docker/docker-run-command/foreground-and-detached.png)

Les tâches courtes affichent leur message dans le terminal. Le lancement du serveur en arrière-plan renvoie un identifiant de conteneur.

:::single-choice{#docker-run-command-detach-meaning} Docker affiche un identifiant et l’invite revient. Que permet ce mode ?

::option[Utiliser le terminal seulement une fois le serveur arrêté.]{#docker-run-command-detach-wait explanation="Le terminal vous rend la main pendant que le serveur continue de tourner."}
::option[Laisser l’image disponible sans démarrer le serveur.]{#docker-run-command-detach-skip explanation="Docker démarre aussi le conteneur en arrière-plan."}
::option[Utiliser le terminal alors que le serveur est encore en cours d’exécution.]{#docker-run-command-detach-continue .correct explanation="Ce mode vous rend la main après le démarrage du conteneur."}
:::

## Reconnaître un nouveau conteneur

Chaque exécution réussie de `docker run` crée un conteneur. Si vous réutilisez la même image de serveur avec un nom disponible, Docker crée un deuxième conteneur. Le premier garde son nom et son état.

:::single-choice{#docker-run-command-second-instance} Web est en cours d’exécution. Que fait `docker run -d --name demo nginx:alpine` si le nom demo est disponible ?

::option[La commande renomme le conteneur web en demo.]{#docker-run-command-second-rename explanation="Docker run crée un conteneur. Le conteneur web existant garde son nom."}
::option[La commande ajoute à l’image un tag nommé demo.]{#docker-run-command-second-tag explanation="L’option nomme un conteneur. La référence de l’image reste nginx:alpine."}
::option[La commande démarre un autre conteneur nommé demo.]{#docker-run-command-second-new .correct explanation="Docker crée un nouveau conteneur à partir de l’image et lui attribue le nom demo."}
:::

Pour vous entraîner à démarrer un conteneur et à lire sa sortie, essayez [Votre premier atelier Docker](https://labex.io/labs/docker-your-first-docker-lab-92719).

## Résumé

Vous savez maintenant lire une commande docker run et prévoir ce que Docker va créer.

1. Identifier l’image et l’éventuelle commande à exécuter dans le conteneur.
2. Utiliser `--name` pour retrouver un conteneur plus tard.
3. Décrire ce qui se passe lorsqu’une tâche courte se termine.
4. Utiliser `-d` pour retrouver le terminal pendant que le serveur tourne.
